"""Kaggle exploratory provenance, artifact export and none/all analysis checks."""
import copy
import json
from pathlib import Path
import sys
from zipfile import ZipFile

import pandas as pd
import pytest
import torch
import yaml

SCRIPT_DIR = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPT_DIR))
import kaggle_preliminary as kaggle
import prepare_data as prep
from evaluate import audit_results
from generate_tables import generate_tables
from generate_figures import generate_figures
from historytta.adapters import make_adapter
from historytta.models import DigitCNN
from historytta.runner import execute_panel, from_manifest
from historytta.utils import provenance, write_json, seed_all


def test_preliminary_plan_is_small_but_keeps_w16():
    config = kaggle.load_config(kaggle.DEFAULT_CONFIG)
    plan = kaggle.experiment_plan(config)
    assert config["washout_batches"] == [0, 4, 16]
    assert config["interventions"] == ["none", "all"]
    assert plan["matrix"]["unique_base_images"] == 2560
    assert plan["matrix"]["paired_suffix_runs"] == 72
    assert plan["matrix"]["directional_suffix_runs"] == 144
    assert plan["matrix"]["main_suffix_image_forwards"] == 147456
    assert plan["matrix"]["saved_junction_checkpoints"] == 0
    assert plan["budget"]["gpu_cost_usd"] == [0, 0]


def tiny_attached_tree(tmp_path):
    root = tmp_path / "images"
    for domain in {d for scenario in prep.SCENARIOS for d in scenario}:
        folder = root / domain / "5/n00000001"
        folder.mkdir(parents=True)
        for i in range(1, 201):
            (folder / f"ILSVRC2012_val_{i:08d}.JPEG").write_bytes(f"fixture {domain} {i}".encode())
    mapping = tmp_path / "classes.json"
    mapping.write_text(json.dumps({"0": ["n00000001", "fixture class"]}))
    return root, mapping


def test_declared_source_requires_explicit_opt_in_and_retains_checks(tmp_path):
    root, mapping = tiny_attached_tree(tmp_path)
    with pytest.raises(ValueError, match="DATA_SOURCE_URL"):
        kaggle.attached_source(root, "")
    records = kaggle.attached_source(root, "https://example.org/user-declared-fixture")
    kwargs = dict(seeds=(101,), prefix_size=4, washout_size=4, suffix_size=4,
                  batch_size=2, expected_classes=1, source_records=records)
    with pytest.raises(ValueError, match="explicit exploratory opt-in"):
        prep.build_manifests(root, tmp_path / "panels", mapping, **kwargs)
    index = prep.build_manifests(root, tmp_path / "panels", mapping,
                                 allow_attached_source=True, **kwargs)
    assert "archives" not in index["metadata"]["source_records"][0]
    path = tmp_path / "panels/index.json"
    kaggle.load_index(path, 2)
    document = json.loads((path.parent / index["panels"][0]["path"]).read_text())
    image = Path(next(iter(document["metadata"]["image_sha256"])))
    image.write_bytes(b"tampered")
    with pytest.raises(ValueError, match="Image content changed"):
        kaggle.load_index(path, 2)


def test_none_all_end_to_end_fixture_audit_tables_figures_and_summary(tmp_path):
    root, mapping = tiny_attached_tree(tmp_path)
    panels = tmp_path / "panels"
    index = prep.build_manifests(root, panels, mapping, seeds=(101,), prefix_size=4,
                                washout_size=4, suffix_size=4, batch_size=2, expected_classes=1,
                                source_records=kaggle.attached_source(root, "https://example.org/fixture"),
                                allow_attached_source=True)
    cfg = copy.deepcopy(kaggle.load_config(kaggle.DEFAULT_CONFIG))
    cfg["experiment_id"] = "fixture"
    cfg["washout_batches"] = [0, 1, 2]
    cfg["planning"].update(prefix_images=4, washout_images_max=4, suffix_images=4)
    output = tmp_path / "results"
    write_json(output / "provenance.json", provenance(cfg))
    write_json(output / "manifest_index.json", index)
    seed_all(101)
    model = DigitCNN()
    controls = []
    for entry in index["panels"]:
        panel = from_manifest(json.loads((panels / entry["path"]).read_text()))
        def loader(sample):
            generator = torch.Generator().manual_seed(int(sample.base_id.split("_")[-1].split(".")[0]))
            return torch.rand((1, 8, 8), generator=generator)
        for method in cfg["methods"]:
            _, checks = execute_panel(make_adapter(copy.deepcopy(model), method), panel, loader, output,
                                      {"experiment_id": "fixture", "seed": 101,
                                       "panel_id": entry["panel_id"], "scenario": entry["scenario"]},
                                      cfg["washout_batches"], cfg["interventions"], save_images=False)
            controls.extend(checks)
    assert controls and all(c["passed"] for c in controls)
    write_json(output / "controls.json", controls)
    write_json(output / "run_status.json", {"status": "complete"})
    audit = audit_results(output)
    assert audit["passed"], audit["failures"]
    assert audit["counts"]["run_rows"] == 144
    assert audit["counts"]["paired_rows"] == 72
    assert audit["counts"]["scalar_comparisons"] == 1368
    generate_tables(output, stage="B")
    generate_figures(output, output=output / "figures", stage="B")
    kaggle.summarize(output)
    history = pd.read_csv(output / "preliminary_history.csv")
    assert len(history) == 72 and history.scenario.nunique() == 3
    assert (history.disagreement_pp == history.disagreement * 100).all()
    interpretation = json.loads((output / "preliminary_interpretation.json").read_text())
    assert interpretation["independent_panels"] == 1 and not interpretation["p_value_claimed"]
    assert not (output / "tables/factorial_summary.csv").exists()
    assert (output / "figures/figure_manifest.json").is_file()


def test_export_preserves_diagnostics_and_figures_without_input_images(tmp_path, monkeypatch):
    monkeypatch.setattr(kaggle, "ROOT", tmp_path)
    config = tmp_path / "configs/kaggle_preliminary.yaml"
    config.parent.mkdir()
    config.write_text(yaml.safe_dump({"experiment_id": "fixture", "output": "results/fixture",
                                     "manifest_index": "datasets/processed/panels/index.json"}))
    monkeypatch.chdir(tmp_path)
    for name in ["results/fixture/predictions/ab.npz", "results/fixture/figures/plot.png",
                 "kaggle_logs/fixture/run.log", "datasets/processed/panels/index.json",
                 "datasets/raw/image.JPEG"]:
        path = tmp_path / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(b"diagnostic fixture")
    archive = kaggle.export(config, tmp_path / "exports")
    with ZipFile(archive) as saved:
        assert "results/fixture/figures/plot.png" in saved.namelist()
        assert "kaggle_logs/fixture/run.log" in saved.namelist()
        assert not any(name.endswith(".JPEG") for name in saved.namelist())
    with pytest.raises(FileExistsError):
        kaggle.export(config, tmp_path / "exports")


def test_runner_subprocess_wall_clock_cap(tmp_path):
    with pytest.raises(TimeoutError, match="wall-clock cap"):
        kaggle.checked_command(["-c", "import time; time.sleep(10)"], tmp_path / "timeout.log", max_seconds=0.2)


def test_notebook_code_cells_compile():
    notebook = json.loads((SCRIPT_DIR.parent / "notebooks/kaggle_stage_b_preliminary.ipynb").read_text(encoding="utf-8"))
    for index, cell in enumerate(notebook["cells"]):
        if cell["cell_type"] == "code":
            compile("".join(cell["source"]), f"cell_{index}", "exec")
