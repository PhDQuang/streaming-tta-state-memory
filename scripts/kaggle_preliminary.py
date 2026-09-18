"""Prepare, run, audit and export an exploratory ImageNet-C Kaggle experiment.

Uses the existing cloud runner unchanged. Never provisions or downloads a paid
resource. ImageNet-C files must already be attached to the notebook.
"""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import subprocess
import sys
import threading
from zipfile import ZIP_DEFLATED, ZipFile

# Set before importing Torch or creating a CUDA context.
os.environ.setdefault("CUBLAS_WORKSPACE_CONFIG", ":4096:8")
import _bootstrap
import yaml

from historytta.utils import file_sha256, write_json
from prepare_data import build_manifests, download_class_index
from run_cloud_pilot import experiment_plan, load_index

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CONFIG = ROOT / "configs/kaggle_preliminary.yaml"


def load_config(path):
    return yaml.safe_load(Path(path).read_text(encoding="utf-8"))


def attached_source(data_root: Path, source_url: str, dataset="ImageNet-C") -> list[dict]:
    if not source_url.startswith(("https://", "http://")):
        raise ValueError("Set DATA_SOURCE_URL to the actual attached dataset page (https://...).")
    return [{"attached_dataset": {
        "source_url": source_url,
        "runtime_root": str(data_root.resolve()),
        "claimed_dataset": dataset,
        "verification": "selected_image_hashes_only_not_official_archive_verified",
        "note": "User-declared source; selected image bytes and labels are checked locally. "
                "No official tar checksum or equivalence to the official distribution is claimed.",
    }}]


def prepare(config_path: Path, data_root: Path, source_url: str, class_index: Path, download: bool):
    cfg = load_config(config_path)
    get_plan(cfg)
    if download:
        download_class_index(class_index)
    if not class_index.is_file():
        raise FileNotFoundError("Provide the pinned imagenet_class_index.json or use --download-class-index")
    if cfg.get("dataset_profile") == "tiny_imagenet_c":
        from tiny_imagenetc import prepare_tiny
        prepare_tiny(cfg, data_root, class_index, attached_source(data_root, source_url, cfg["dataset"]))
        return
    p = cfg["planning"]
    if p["independent_panels"] != 1 or p["scenarios_per_panel"] != 3:
        raise ValueError("This preliminary wrapper is frozen to one panel and all three scenarios")
    # Preserve existing verified extraction records when present. An attached
    # tree without those records is explicitly marked as declared provenance.
    verified = any((data_root / "_provenance").glob("extract_*.json"))
    records = None if verified else attached_source(data_root, source_url)
    index_path = Path(cfg["manifest_index"])
    index = build_manifests(
        data_root, index_path.parent, class_index, severities=(5,), seeds=(101,),
        prefix_size=p["prefix_images"], washout_size=p["washout_images_max"],
        suffix_size=p["suffix_images"], batch_size=cfg["adaptation"]["batch_size"],
        source_records=records, allow_attached_source=not verified,
    )
    load_index(index_path, cfg["adaptation"]["batch_size"], expected_planning=p)
    print(json.dumps({"index": str(index_path.resolve()), "panels": len(index["panels"]),
                      "unique_base_images": 2560,
                      "provenance_mode": "verified_extraction" if verified else "declared_attached_dataset"}, indent=2))


def checked_command(arguments: list[str], log: Path, max_seconds: float | None = None):
    log.parent.mkdir(parents=True, exist_ok=True)
    print("Running:", " ".join(arguments), flush=True)
    with log.open("w", encoding="utf-8") as stream:
        process = subprocess.Popen([sys.executable, "-u", *arguments], cwd=ROOT,
                                   stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                   text=True, encoding="utf-8", errors="replace")
        timed_out = threading.Event()
        def stop_process():
            if process.poll() is None:
                timed_out.set()
                process.kill()
        timer = threading.Timer(max_seconds, stop_process) if max_seconds is not None else None
        if timer is not None:
            timer.daemon = True
            timer.start()
        try:
            for line in process.stdout:
                print(line, end="", flush=True)
                stream.write(line)
                stream.flush()
            code = process.wait()
        finally:
            if timer is not None:
                timer.cancel()
        if timed_out.is_set():
            raise TimeoutError("Preliminary runner process killed at its wall-clock cap; exported results are incomplete.")
    if code:
        raise subprocess.CalledProcessError(code, arguments)


def get_plan(cfg):
    if cfg.get("dataset_profile") == "tiny_imagenet_c":
        from tiny_imagenetc import tiny_plan
        return tiny_plan(cfg)
    return experiment_plan(cfg)


def summarize(results: Path):
    import pandas as pd
    paired = pd.read_csv(results / "paired.csv")
    runs = pd.read_csv(results / "runs.csv")
    # Keep scenarios separate; means below average only the two directions.
    performance = runs.groupby(["scenario", "method", "washout_batches", "intervention"],
                               as_index=False)[["accuracy", "nll", "brier", "ece15"]].mean()
    performance["accuracy_percent"] = performance["accuracy"] * 100
    performance.to_csv(results / "preliminary_performance.csv", index=False)
    history = paired[["panel_id", "scenario", "method", "washout_batches", "intervention",
                      "n", "disagreement", "absolute_error_gap", "nll_gap", "first_batch_max_logit_diff"]].copy()
    history["disagreement_pp"] = history["disagreement"] * 100
    history.to_csv(results / "preliminary_history.csv", index=False)
    cfg = json.loads((results / "provenance.json").read_text(encoding="utf-8"))["config"]
    write_json(results / "preliminary_interpretation.json", {
        "stage": cfg["stage"], "dataset": cfg.get("dataset", "ImageNet-C"),
        "classifier": cfg.get("classifier", "imagenet_1000_class"),
        "interpretation": cfg.get("interpretation", "Exploratory one-panel run"),
        "status": "exploratory", "independent_panels": 1,
        "scenarios_reuse_images": True, "confidence_interval_claimed": False,
        "p_value_claimed": False, "factorial_state_ablation_complete": False,
        "scope": "Describe this panel, W16 history sensitivity, and none/all reset comparisons only.",
        "provenance": "See manifest_index.json metadata.source_records for verified vs declared source.",
    })
    print("\nW16 results, disagreement in percentage points:")
    print(history[history.washout_batches == 16][
        ["scenario", "method", "intervention", "disagreement_pp", "nll_gap"]].to_string(index=False))


def execute(config_path: Path, max_hours: float):
    cfg = load_config(config_path)
    get_plan(cfg)
    if not 0 < max_hours <= 10:
        raise ValueError("Kaggle preliminary process allowance must be in (0, 10] hours")
    import torch
    import torchvision
    if not torch.cuda.is_available():
        raise RuntimeError("Enable a Kaggle GPU accelerator before running this cell")
    output = Path(cfg["output"])
    if output.exists() and any(output.iterdir()):
        raise FileExistsError("Existing results retained. For another attempt change experiment_id AND output in the config.")
    output.mkdir(parents=True, exist_ok=True)
    # Keep environment diagnostics outside results until the runner creates it.
    # run_cloud_pilot refuses a nonempty output directory, intentionally.
    logs = ROOT / "kaggle_logs" / cfg["experiment_id"]
    write_json(logs / "environment.json", {
        "torch": str(torch.__version__), "torchvision": str(torchvision.__version__),
        "cuda_runtime": torch.version.cuda, "gpu": torch.cuda.get_device_name(0),
        "python": sys.version, "cublas_workspace_config": os.environ["CUBLAS_WORKSPACE_CONFIG"],
        "version_policy": "Kaggle installed Torch/torchvision retained; local Stage A pins not silently enforced.",
    })
    try:
        runner = "scripts/tiny_imagenetc.py" if cfg.get("dataset_profile") == "tiny_imagenet_c" else "scripts/run_cloud_pilot.py"
        checked_command([runner, "--config", str(config_path),
                         "--execute", "--max-hours", str(max_hours)], logs / "run.log",
                        max_seconds=max_hours * 3600)
    except Exception as exc:
        write_json(logs / "wrapper_failure.json", {"status": "failed", "error": str(exc),
                   "note": "Runner run_status can remain running if forcibly killed; do not interpret partial outputs."})
        raise
    checked_command(["scripts/evaluate.py", "--results", str(output)], logs / "audit.log")
    controls = json.loads((output / "controls.json").read_text(encoding="utf-8"))
    audit = json.loads((output / "evaluation_audit.json").read_text(encoding="utf-8"))
    if not audit["passed"] or not controls or any(c.get("passed") is not True for c in controls):
        raise RuntimeError("Artifact audit or deterministic controls failed; inspect exported diagnostics")
    checked_command(["scripts/generate_tables.py", "--results", str(output), "--stage", cfg["stage"]], logs / "tables.log")
    checked_command(["scripts/generate_figures.py", "--results", str(output), "--output", str(output / "figures"),
                     "--stage", cfg["stage"]], logs / "figures.log")
    summarize(output)


def export(config_path: Path, destination: Path) -> Path:
    cfg = load_config(config_path)
    destination.mkdir(parents=True, exist_ok=True)
    archive = destination / f'{cfg["experiment_id"]}_artifacts.zip'
    if archive.exists():
        raise FileExistsError(f"Export already exists: {archive}; use a different export directory")
    roots = [Path(cfg["output"]), Path(cfg["manifest_index"]).parent,
             ROOT / "kaggle_logs" / cfg["experiment_id"], ROOT / "src", ROOT / "scripts", ROOT / "configs",
             ROOT / "notebooks", ROOT / "third_party", ROOT / "datasets/metadata",
             ROOT / "research/kaggle_preliminary.md", ROOT / "research/kaggle_tiny_preliminary.md", ROOT / "pyproject.toml",
             ROOT / "requirements.txt"]
    files = set()
    for root in roots:
        if root.is_file():
            files.add(root.resolve())
        elif root.is_dir():
            files.update(p.resolve() for p in root.rglob("*")
                         if p.is_file() and "__pycache__" not in p.parts and p.suffix != ".pyc")
    with ZipFile(archive, "x", compression=ZIP_DEFLATED) as target:
        for path in sorted(files):
            if not path.is_relative_to(ROOT):
                raise ValueError(f"Export path must be inside repository: {path}")
            target.write(path, path.relative_to(ROOT).as_posix())
    checksum = file_sha256(archive)
    archive.with_suffix(".zip.sha256").write_text(f"{checksum}  {archive.name}\n", encoding="utf-8")
    print(json.dumps({"archive": str(archive), "sha256": checksum,
                      "note": "May contain partial/failed results; check run_status and audit before interpretation."}, indent=2))
    return archive


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["plan", "prepare", "run", "export"])
    parser.add_argument("--config", type=Path, default=DEFAULT_CONFIG)
    parser.add_argument("--data-root", type=Path)
    parser.add_argument("--source-url", default="")
    parser.add_argument("--class-index", type=Path, default=ROOT / "datasets/metadata/imagenet_class_index.json")
    parser.add_argument("--download-class-index", action="store_true")
    parser.add_argument("--max-hours", type=float, default=10)
    parser.add_argument("--export-dir", type=Path, default=ROOT.parent / "kaggle_exports")
    args = parser.parse_args()
    os.chdir(ROOT)
    if args.command == "plan":
        plan = get_plan(load_config(args.config))
        plan["scheduling_note"] = "0-10h is an allowance, not a benchmark; Kaggle quota must be checked in your account."
        print(json.dumps(plan, indent=2))
    elif args.command == "prepare":
        if args.data_root is None:
            parser.error("prepare requires --data-root")
        prepare(args.config, args.data_root, args.source_url, args.class_index, args.download_class_index)
    elif args.command == "run":
        execute(args.config, args.max_hours)
    else:
        export(args.config, args.export_dir)


if __name__ == "__main__":
    main()
