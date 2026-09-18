"""Tiny projected-label/profile checks using synthetic JPEGs and CPU models."""
import copy
import json
from pathlib import Path
import sys

import numpy as np
from PIL import Image
import pytest
import torch
from torch import nn
import yaml

SCRIPT_DIR = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPT_DIR))
import prepare_data as prep
import run_cloud_pilot as cloud
import tiny_imagenetc as tiny
import kaggle_preliminary as kaggle
from evaluate import audit_results
from generate_tables import generate_tables
from generate_figures import generate_figures
from historytta.adapters import make_adapter
from historytta.models import ProjectedClassifier
from historytta.utils import file_sha256, object_sha256, write_json

CONFIG = SCRIPT_DIR.parent / "configs/kaggle_tiny_preliminary.yaml"


def test_tiny_plan_keeps_w16_and_separate_scope_without_loading_weights(monkeypatch):
    def forbidden(*args, **kwargs):
        raise AssertionError("Planning must not load weights")
    monkeypatch.setattr(tiny, "cloud_model", forbidden)
    cfg = kaggle.load_config(CONFIG)
    plan = tiny.tiny_plan(cfg)
    assert cfg["stage"] == "TINY" and cfg["washout_batches"] == [0, 4, 16]
    assert plan["matrix"]["unique_base_images"] == 1536
    assert plan["matrix"]["paired_suffix_runs"] == 72
    assert plan["matrix"]["directional_suffix_runs"] == 144
    assert plan["matrix"]["main_suffix_image_forwards"] == 73728
    cfg["adaptation"]["sar_margin"] = .4 * np.log(1000)
    with pytest.raises(ValueError, match=r"log\(200\)"):
        tiny.tiny_plan(cfg)


def test_projection_selects_correct_classes_before_softmax_and_backprop():
    backbone = nn.Linear(3, 1000, bias=False)
    model = ProjectedClassifier(backbone, [500, 3, 999])
    x = torch.tensor([[1., 2., 3.]])
    full = backbone(x)
    selected = model(x)
    assert torch.equal(selected, full[:, [500, 3, 999]])
    selected.sum().backward()
    nonzero = backbone.weight.grad.abs().sum(1).nonzero().flatten().tolist()
    assert nonzero == [3, 500, 999]
    assert torch.equal(model.state_dict()["source_indices"], torch.tensor([500, 3, 999]))
    with pytest.raises(ValueError):
        ProjectedClassifier(backbone, [1, 1])
    with pytest.raises(ValueError, match="1000-logit"):
        ProjectedClassifier(nn.Linear(3, 200), [1, 2])(x)


@pytest.fixture
def attached_tiny(tmp_path, monkeypatch):
    # Fixture mapping has production shape but deliberately synthetic synsets.
    # Pin its own bytes for this test; no network or real mapping/data is used.
    canonical = tmp_path / "classes.json"
    rows = {str(i): [f"n{i+1:08d}", f"fixture class {i}"] for i in range(1000)}
    canonical.write_text(json.dumps(rows))
    digest = file_sha256(canonical)
    monkeypatch.setattr(prep, "CLASS_INDEX_SHA256", digest)
    monkeypatch.setattr(cloud, "CLASS_INDEX_SHA256", digest)
    root = tmp_path / "images"
    for domain in {d for scenario in prep.SCENARIOS for d in scenario}:
        for i in range(200):
            folder = root / domain / "5" / rows[str(i * 3)][0]
            folder.mkdir(parents=True)
            Image.new("RGB", (64, 64), (i % 255, 30, 90)).save(folder / f"test_{i}.JPEG")
    cfg = copy.deepcopy(kaggle.load_config(CONFIG))
    cfg["class_index"] = str(canonical)
    cfg["manifest_index"] = str(tmp_path / "panels/index.json")
    cfg["output"] = str(tmp_path / "results")
    cfg["adaptation"]["batch_size"] = 2
    cfg["washout_batches"] = [0, 1, 2]
    cfg["planning"].update(prefix_images=4, washout_images_max=4, suffix_images=4)
    sources = kaggle.attached_source(root, "https://example.org/synthetic-tiny", cfg["dataset"])
    tiny.prepare_tiny(cfg, root, canonical, sources)
    return cfg, root, canonical


def test_tiny_mapping_names_hashes_and_default_imagenet_guard(attached_tiny):
    cfg, root, canonical = attached_tiny
    index, records = tiny.load_tiny_index(cfg)
    assert len(records) == 3
    assert index["metadata"]["dataset"] == "Tiny ImageNet-C"
    assert index["metadata"]["output_imagenet_indices"] == list(range(0, 600, 3))
    assert index["metadata"]["class_to_idx"]["n00000004"] == 1
    assert all(sample.base_id.startswith("test_") for _, p, _ in records for b in p.suffix for sample in b)
    with pytest.raises(ValueError, match="1000 ImageNet classes"):
        cloud.load_index(Path(cfg["manifest_index"]), 2, expected_planning=cfg["planning"])
    sample = records[0][1].suffix[0][0]
    Path(sample.path).write_bytes(b"modified after freezing")
    with pytest.raises(ValueError, match="Image content changed"):
        tiny.load_tiny_index(cfg)


def test_tiny_rejects_arbitrary_source_projection_even_with_new_index_hash(attached_tiny):
    cfg, _, _ = attached_tiny
    path = Path(cfg["manifest_index"])
    index = json.loads(path.read_text())
    index["metadata"]["output_imagenet_indices"][0] = 900
    index["sha256"] = object_sha256({k: v for k, v in index.items() if k != "sha256"})
    write_json(path, index)
    with pytest.raises(ValueError, match="projection"):
        tiny.load_tiny_index(cfg)


def test_tiny_rejects_wrong_selected_image_size(attached_tiny, tmp_path):
    cfg, root, canonical = attached_tiny
    _, records = tiny.load_tiny_index(cfg)
    selected = records[0][1].suffix[0][0]
    Image.new("RGB", (224, 224)).save(selected.path)
    changed = copy.deepcopy(cfg)
    changed["manifest_index"] = str(tmp_path / "different/index.json")
    with pytest.raises(ValueError, match="64x64"):
        tiny.prepare_tiny(changed, root, canonical,
                          kaggle.attached_source(root, "https://example.org/synthetic-tiny", cfg["dataset"]))


def test_tiny_rejects_inconsistent_class_assignments_across_corruptions(attached_tiny, tmp_path):
    cfg, root, canonical = attached_tiny
    variant = root / "gaussian_noise/5"
    first = variant / "n00000001/test_0.JPEG"
    first.rename(variant / "n00000004/test_0.JPEG")
    changed = copy.deepcopy(cfg)
    changed["manifest_index"] = str(tmp_path / "different/index.json")
    with pytest.raises(ValueError, match="same original IDs and synset assignment"):
        tiny.prepare_tiny(changed, root, canonical,
                          kaggle.attached_source(root, "https://example.org/synthetic-tiny", cfg["dataset"]))


def test_tiny_shared_execution_audit_summary_export_contract(attached_tiny, monkeypatch):
    cfg, root, _ = attached_tiny
    cfg["device"] = "cpu"
    output = Path(cfg["output"])
    # Exercise the real shared runner with tiny trainable model and synthetic
    # JPEG loader. Mock CUDA availability/accounting only, never model metrics.
    monkeypatch.setattr(cloud.torch.cuda, "is_available", lambda: True)
    monkeypatch.setattr(cloud.torch.cuda, "get_device_name", lambda *a: "fixture")
    monkeypatch.setattr(cloud.torch.cuda, "reset_peak_memory_stats", lambda: None)
    monkeypatch.setattr(cloud.torch.cuda, "max_memory_allocated", lambda: 0)
    monkeypatch.setattr(cloud.torch.cuda, "max_memory_reserved", lambda: 0)
    monkeypatch.setattr(cloud.torch.cuda, "empty_cache", lambda: None)
    # The fixture transfers models/inputs to CPU while exercising the shared
    # runner's production CUDA guard and accounting paths without a GPU.
    class CPUModel(nn.Module):
        def __init__(self):
            super().__init__()
            self.features = nn.Sequential(nn.Conv2d(3, 4, 1), nn.BatchNorm2d(4), nn.ReLU(), nn.AdaptiveAvgPool2d(1))
            self.head = nn.Linear(4, 1000)
        def forward(self, x):
            return self.head(self.features(x).flatten(1))
    original_execute = cloud.execute_panel
    def cpu_execute(*args, **kwargs):
        kwargs["device"] = "cpu"
        return original_execute(*args, **kwargs)
    def backbone_loader(config, index):
        class CPUProjection(ProjectedClassifier):
            def to(self, *args, **kwargs):
                return super().to("cpu")
        return CPUProjection(CPUModel(), index["metadata"]["output_imagenet_indices"]), lambda image: torch.tensor(np.asarray(image).copy()).permute(2, 0, 1).float()[:, :8, :8] / 255
    monkeypatch.setattr(cloud, "execute_panel", cpu_execute)
    cfg["device"] = "cuda"
    cloud.run_experiment(cfg, 10, index_loader=tiny.load_tiny_index, backbone_loader=backbone_loader)
    report = audit_results(output)
    assert report["passed"], report["failures"]
    assert report["counts"]["run_rows"] == 144 and report["counts"]["paired_rows"] == 72
    assert report["counts"]["scalar_comparisons"] == 1368
    assert report["counts"]["unique_original_ids"] == 4
    controls = json.loads((output / "controls.json").read_text())
    assert controls and all(c["passed"] for c in controls)
    with np.load(next((output / "predictions").glob("*.npz"))) as predictions:
        assert predictions["logits"].shape[1] == 200
    generate_tables(output, stage="TINY")
    generate_figures(output, output=output / "figures", stage="TINY")
    kaggle.summarize(output)
    interpretation = json.loads((output / "preliminary_interpretation.json").read_text())
    assert interpretation["stage"] == "TINY" and interpretation["dataset"] == "Tiny ImageNet-C"
    assert interpretation["classifier"] == "imagenet_200_class_projection"
    assert "Not a Tiny-trained baseline" in interpretation["interpretation"]


def test_tiny_notebook_schema_and_code():
    import nbformat
    notebook = nbformat.read(SCRIPT_DIR.parent / "notebooks/kaggle_tiny_imagenetc_preliminary.ipynb", as_version=4)
    nbformat.validate(notebook)
    for i, cell in enumerate(notebook.cells):
        if cell.cell_type == "code":
            compile(cell.source, f"tiny_cell_{i}", "exec")
