"""Independently audit saved NPZ predictions against directional and paired CSVs.

Uses NumPy metric formulas, not the runner's Torch metric implementation. This is
an artifact-consistency audit, not a fresh model evaluation or inferential test.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
from itertools import product
from pathlib import Path
import sys

import numpy as np

PAIR_KEYS = ["experiment_id", "seed", "panel_id", "scenario", "method", "intervention", "washout_batches"]
RUN_METRICS = ["n", "accuracy", "nll", "brier", "ece15"]
PAIR_METRICS = ["n", "disagreement", "accuracy_ab", "accuracy_ba", "signed_error_gap",
                "absolute_error_gap", "nll_gap", "brier_gap", "first_batch_max_logit_diff"]


def validate_inventory(results: Path) -> list[str]:
    """Check the complete planned directional/pair matrix, independent of metrics.

Stage A panel identities follow its frozen source seeds/scenarios and documented
fixed panel. Cloud identities come from the copied frozen manifest index. Never
infer the expected matrix from observed CSV rows, which could omit whole arms.
"""
    failures = []
    try:
        provenance = json.loads((results / "provenance.json").read_text(encoding="utf-8"))
        config = provenance["config"]
        digest = hashlib.sha256(json.dumps(config, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
        if digest != provenance.get("config_sha256"):
            failures.append("Frozen provenance config hash missing or mismatched")
        if str(config["stage"]).upper() == "A":
            bases = [(str(seed), str(config.get("panel_id", "uci_internal_fixed")), str(scenario["name"]))
                     for seed, scenario in product(config["source_seeds"], config["scenarios"])]
        else:
            index = json.loads((results / "manifest_index.json").read_text(encoding="utf-8"))
            body = {k: v for k, v in index.items() if k != "sha256"}
            digest = hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
            if digest != index.get("sha256"):
                failures.append("Frozen manifest-index hash missing or mismatched")
            bases = [(str(row["seed"]), str(row["panel_id"]), str(row["scenario"])) for row in index["panels"]]
            planning = config.get("planning", {})
            if "independent_panels" in planning and len({row[1] for row in bases}) != planning["independent_panels"]:
                failures.append("Manifest independent-panel count differs from frozen config")
            if "scenarios_per_panel" in planning:
                for panel in {row[1] for row in bases}:
                    if len({row[2] for row in bases if row[1] == panel}) != planning["scenarios_per_panel"]:
                        failures.append(f"Manifest scenario count differs from config for {panel}")
        if not bases or len(set(bases)) != len(bases):
            failures.append("Expected base identity inventory is empty or duplicated")
        expected_pairs = set()
        for (seed, panel, scenario), method in product(bases, config["methods"]):
            manifest = results / "manifests" / f"{seed}_{panel}_{scenario}_{method}.json"
            if not manifest.is_file():
                failures.append(f"Missing mandatory stream manifest: {manifest.name}")
            interventions = ["none", "all"] if method in {"source", "norm"} else config["interventions"]
            for intervention, w in product(interventions, config["washout_batches"]):
                expected_pairs.add((str(config["experiment_id"]), seed, panel, scenario, str(method), str(intervention), str(w)))
        if not expected_pairs:
            failures.append("Expected experiment matrix is empty")
        for filename, keys, expected in [
            ("paired.csv", PAIR_KEYS, expected_pairs),
            ("runs.csv", PAIR_KEYS + ["direction"], {key + (d,) for key in expected_pairs for d in ["ab", "ba"]}),
        ]:
            with (results / filename).open(newline="", encoding="utf-8-sig") as handle:
                rows = list(csv.DictReader(handle))
            observed = [tuple(row[name] for name in keys) for row in rows]
            if len(observed) != len(set(observed)):
                failures.append(f"{filename}: duplicate trajectory identities")
            missing, extra = expected - set(observed), set(observed) - expected
            if missing:
                failures.append(f"{filename}: {len(missing)} mandatory cells missing; first={sorted(missing)[0]}")
            if extra:
                failures.append(f"{filename}: {len(extra)} unplanned cells; first={sorted(extra)[0]}")
    except (OSError, ValueError, KeyError, TypeError) as exc:
        failures.append(f"Cannot validate frozen experiment inventory: {exc}")
    return failures


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def identity_digest(ids: np.ndarray, labels: np.ndarray) -> str:
    values = list(zip(ids.astype(str).tolist(), labels.astype(int).tolist()))
    return hashlib.sha256(json.dumps(values, separators=(",", ":")).encode()).hexdigest()


def read_predictions(path: Path) -> dict:
    with np.load(path, allow_pickle=False) as archive:
        if not {"logits", "labels", "ids"}.issubset(archive.files):
            raise ValueError("NPZ requires logits, labels, and ids")
        data = {name: archive[name].copy() for name in ["logits", "labels", "ids"]}
        if "images" in archive:
            images = archive["images"]
            if len(images) != len(data["labels"]) or not np.isfinite(images).all():
                raise ValueError("Optional images have invalid count or nonfinite values")
    logits, labels, ids = data["logits"], data["labels"], data["ids"]
    if logits.ndim != 2 or len(logits) == 0 or logits.shape[1] < 2 or logits.dtype.kind != "f":
        raise ValueError("Expected nonempty floating [N,C] logits with at least two classes")
    if not np.isfinite(logits).all():
        raise ValueError("Nonfinite logits")
    if labels.ndim != 1 or labels.dtype.kind not in "iu" or len(labels) != len(logits):
        raise ValueError("Expected aligned integer [N] labels")
    if labels.min() < 0 or labels.max() >= logits.shape[1]:
        raise ValueError("Labels outside class range")
    if ids.ndim != 1 or ids.dtype.kind not in "US" or len(ids) != len(labels):
        raise ValueError("Expected aligned string [N] image IDs")
    ids = ids.astype(str)
    if any(not identity.strip() for identity in ids) or len(set(ids)) != len(ids):
        raise ValueError("Image IDs must be nonempty and unique within Q")
    data["ids"] = ids
    return data


def compute_metrics(logits: np.ndarray, labels: np.ndarray) -> dict:
    """Stable float64 softmax; multiclass Brier sum; left-closed 15-bin ECE."""
    z = logits.astype(np.float64)
    z -= z.max(axis=1, keepdims=True)
    exp_z = np.exp(z)
    denominator = exp_z.sum(axis=1, keepdims=True)
    probabilities = exp_z / denominator
    rows = np.arange(len(labels))
    predicted = np.argmax(probabilities, axis=1)
    correct = predicted == labels
    nll = np.log(denominator[:, 0]) - z[rows, labels]
    residual = probabilities.copy()
    residual[rows, labels] -= 1
    confidence = probabilities.max(axis=1)
    edges = np.linspace(0., 1., 16)
    ece = 0.
    for i in range(15):
        mask = (confidence >= edges[i]) & ((confidence < edges[i + 1]) if i < 14 else (confidence <= 1.))
        if mask.any():
            ece += mask.mean() * abs(confidence[mask].mean() - correct[mask].mean())
    return {"n": len(labels), "accuracy": float(correct.mean()), "nll": float(nll.mean()),
            "brier": float(np.square(residual).sum(axis=1).mean()), "ece15": float(ece)}


def paired_metrics(a: dict, b: dict, first_batch_size: int) -> dict:
    if not np.array_equal(a["ids"], b["ids"]):
        raise ValueError("AB/BA Q image IDs or their chronological order differ")
    if not np.array_equal(a["labels"], b["labels"]):
        raise ValueError("AB/BA labels differ for the same image IDs")
    if a["logits"].shape != b["logits"].shape:
        raise ValueError("AB/BA logit shapes differ")
    if not 1 <= first_batch_size <= len(a["labels"]):
        raise ValueError("First Q batch size must be positive and no greater than Q")
    am, bm = [compute_metrics(item["logits"], item["labels"]) for item in [a, b]]
    gap = bm["accuracy"] - am["accuracy"]
    # Saved logits preserve the original dtype; replicate its subtraction rounding.
    first = np.abs(a["logits"][:first_batch_size] - b["logits"][:first_batch_size]).max()
    return {"n": am["n"], "disagreement": float((a["logits"].argmax(1) != b["logits"].argmax(1)).mean()),
            "accuracy_ab": am["accuracy"], "accuracy_ba": bm["accuracy"],
            "signed_error_gap": gap, "absolute_error_gap": abs(gap),
            "nll_gap": am["nll"] - bm["nll"], "brier_gap": am["brier"] - bm["brier"],
            "first_batch_max_logit_diff": float(first)}


def audit_results(results: Path, output: Path | None = None, *, atol: float = 1e-7,
                  batch_size: int | None = None) -> dict:
    results = results.resolve()
    if not results.is_dir():
        raise FileNotFoundError(results)
    if not np.isfinite(atol) or atol < 0:
        raise ValueError("atol must be finite and nonnegative")
    output = output or results / "evaluation_audit.json"
    failures, notes, hashes = [], [], {}
    for detail in validate_inventory(results):
        failures.append({"kind": "experiment_inventory", "identity": results.name, "detail": detail})
    counts = {"run_rows": 0, "paired_rows": 0, "predictions_audited": 0,
              "pairs_audited": 0, "scalar_comparisons": 0, "manifest_checks": 0}
    maxima = {}

    def fail(kind, identity, detail):
        failures.append({"kind": kind, "identity": str(identity), "detail": str(detail)})

    def hash_file(path):
        label = str(path.relative_to(results)) if path.is_relative_to(results) else str(path)
        if label not in hashes:
            hashes[label] = sha256(path)

    def csv_rows(name, required):
        path = results / name
        try:
            hash_file(path)
            with path.open(newline="", encoding="utf-8-sig") as handle:
                reader = csv.DictReader(handle)
                missing = set(required) - set(reader.fieldnames or [])
                if missing:
                    raise ValueError(f"Missing required fields: {sorted(missing)}")
                rows = list(reader)
            if not rows:
                raise ValueError("No recorded rows")
            return rows
        except (OSError, ValueError) as exc:
            fail("csv_schema", name, exc)
            return []

    def compare(row, recomputed, metric_names, identity, table):
        for name in metric_names:
            counts["scalar_comparisons"] += 1
            try:
                recorded, expected = float(row[name]), float(recomputed[name])
                difference = abs(recorded - expected)
                if not np.isfinite(recorded) or not np.isfinite(expected):
                    raise ValueError("Nonfinite scalar")
                maxima[f"{table}.{name}"] = max(maxima.get(f"{table}.{name}", 0.), difference)
                if (recorded != expected if name == "n" else difference > atol):
                    fail("metric_mismatch", identity, f"{name}: CSV={recorded:.17g}, recomputed={expected:.17g}, abs_diff={difference:.17g}")
            except (KeyError, ValueError, TypeError) as exc:
                fail("metric_invalid", identity, f"{name}: {exc}")

    try:
        status_path = results / "run_status.json"
        hash_file(status_path)
        status = json.loads(status_path.read_text(encoding="utf-8"))
        if status.get("status") != "complete":
            fail("run_status", "run_status.json", f"Expected complete, got {status.get('status')}")
    except (OSError, ValueError) as exc:
        fail("run_status", "run_status.json", exc)
    provenance_path = results / "provenance.json"
    if provenance_path.is_file():
        try:
            hash_file(provenance_path)
            provenance = json.loads(provenance_path.read_text(encoding="utf-8"))
            if batch_size is None:
                batch_size = provenance.get("config", {}).get("adaptation", {}).get("batch_size")
        except (OSError, ValueError) as exc:
            fail("provenance", provenance_path.name, exc)

    runs = csv_rows("runs.csv", PAIR_KEYS + ["direction", "prediction_file"] + RUN_METRICS)
    paired = csv_rows("paired.csv", PAIR_KEYS + PAIR_METRICS)
    counts.update(run_rows=len(runs), paired_rows=len(paired))
    run_map, panel_identities, labels_by_id, manifests = {}, {}, {}, {}
    seen_runs, used_files = set(), set()
    for row_number, row in enumerate(runs, start=2):
        key = tuple(row.get(name, "") for name in PAIR_KEYS) + (row.get("direction", "").lower(),)
        identity = "|".join(key)
        try:
            if any(not value for value in key) or key[-1] not in {"ab", "ba"}:
                raise ValueError("Missing identity field or unrecognized history direction")
            if key in seen_runs:
                raise ValueError("Duplicate directional trajectory")
            seen_runs.add(key)
            path = Path(row["prediction_file"])
            path = path if path.is_absolute() else results / path
            path = path.resolve()
            if path in used_files:
                raise ValueError("Prediction file reused for multiple directional rows")
            used_files.add(path)
            hash_file(path)
            data = read_predictions(path)
            values = compute_metrics(data["logits"], data["labels"])
            compare(row, values, RUN_METRICS, identity, "runs")
            signature = identity_digest(data["ids"], data["labels"])
            # panel_id denotes a shared Q panel across methods, W, interventions,
            # directions, and source/algorithm seeds for this exact scenario.
            panel_key = (row["experiment_id"], row["panel_id"], row["scenario"])
            if panel_key in panel_identities and panel_identities[panel_key] != signature:
                raise ValueError("Repeated panel/scenario changed Q ID order or labels")
            panel_identities[panel_key] = signature
            for image_id, label in zip(data["ids"], data["labels"]):
                global_key = (row["experiment_id"], str(image_id))
                if global_key in labels_by_id and labels_by_id[global_key] != int(label):
                    raise ValueError(f"Repeated original image ID has inconsistent label: {image_id}")
                labels_by_id[global_key] = int(label)
            manifest_path = results / "manifests" / ("_".join(row[name] for name in ["seed", "panel_id", "scenario", "method"]) + ".json")
            first_batch = batch_size
            if manifest_path.is_file():
                if manifest_path not in manifests:
                    hash_file(manifest_path)
                    manifests[manifest_path] = json.loads(manifest_path.read_text(encoding="utf-8"))
                suffix = manifests[manifest_path]["suffix"]
                expected_ids = np.array([str(sample["base_id"]) for batch in suffix for sample in batch])
                expected_labels = np.array([int(sample["label"]) for batch in suffix for sample in batch])
                if not np.array_equal(data["ids"], expected_ids) or not np.array_equal(data["labels"], expected_labels):
                    raise ValueError("Prediction Q ID order/labels differ from immutable stream manifest")
                first_batch = len(suffix[0])
                counts["manifest_checks"] += 1
            if first_batch is None:
                raise ValueError("First Q batch size unavailable: provide --batch-size or manifest/provenance")
            run_map[key] = {"path": path, "first_batch": int(first_batch), "metrics": values}
            counts["predictions_audited"] += 1
        except (OSError, ValueError, KeyError, TypeError, IndexError) as exc:
            fail("prediction_audit", identity or f"runs.csv:{row_number}", exc)

    seen_pairs = set()
    for row_number, row in enumerate(paired, start=2):
        key = tuple(row.get(name, "") for name in PAIR_KEYS)
        identity = "|".join(key)
        try:
            if key in seen_pairs:
                raise ValueError("Duplicate paired trajectory")
            seen_pairs.add(key)
            a_record, b_record = run_map[key + ("ab",)], run_map[key + ("ba",)]
            if a_record["first_batch"] != b_record["first_batch"]:
                raise ValueError("AB/BA first Q batch lengths differ")
            a, b = read_predictions(a_record["path"]), read_predictions(b_record["path"])
            values = paired_metrics(a, b, a_record["first_batch"])
            compare(row, values, PAIR_METRICS, identity, "paired")
            counts["pairs_audited"] += 1
        except (OSError, ValueError, KeyError, TypeError, IndexError) as exc:
            fail("pair_audit", identity or f"paired.csv:{row_number}", exc)
    for key in seen_runs:
        if key[:-1] not in seen_pairs:
            fail("orphan_run", "|".join(key), "No corresponding paired CSV row")
    if not manifests:
        notes.append("No immutable stream manifests found; IDs/labels checked across NPZs only.")
    report = {"passed": not failures, "results": str(results), "scope": "Saved-artifact consistency only; no model rerun or generalization claim",
              "tolerance": {"absolute": atol, "relative": 0., "counts": "exact"},
              "definitions": {"signed_error_gap": "error_AB - error_BA = accuracy_BA - accuracy_AB",
                              "nll_gap": "NLL_AB - NLL_BA", "brier": "sum over classes per image",
                              "ece15": "15 equal-width [left,right) bins, last includes 1"},
              "counts": {**counts, "unique_original_ids": len(labels_by_id), "panel_scenario_groups": len(panel_identities)},
              "max_absolute_metric_differences": maxima, "failures": failures, "notes": notes,
              "evaluator_sha256": sha256(Path(__file__)), "numpy_version": np.__version__, "input_sha256": hashes}
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, indent=2, allow_nan=False) + "\n", encoding="utf-8")
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--results", type=Path, required=True)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--atol", type=float, default=1e-7, help="Absolute scalar tolerance; relative tolerance is zero")
    parser.add_argument("--batch-size", type=int, help="Fallback first Q batch size if no manifest/provenance records it")
    args = parser.parse_args()
    report = audit_results(args.results, args.output, atol=args.atol, batch_size=args.batch_size)
    print(json.dumps({"passed": report["passed"], "counts": report["counts"], "failure_count": len(report["failures"]),
                      "output": str(args.output or args.results / "evaluation_audit.json")}, indent=2))
    if report["failures"]:
        print(json.dumps(report["failures"][:10], indent=2), file=sys.stderr)
    raise SystemExit(0 if report["passed"] else 1)


if __name__ == "__main__":
    main()
