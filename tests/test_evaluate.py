"""Independent metrics and artifact-tampering tests; data stay in temporary dirs."""
from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path
import subprocess
import sys

import numpy as np
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from evaluate import audit_results, compute_metrics, paired_metrics, validate_inventory
from generate_tables import generate_tables


def write_csv(path, rows):
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def fixture_run(tmp_path):
    (tmp_path / "predictions").mkdir()
    (tmp_path / "manifests").mkdir()
    config = {"experiment_id": "fixture_only", "stage": "A", "source_seeds": [0],
              "scenarios": [{"name": "fixture"}], "methods": ["tent"], "interventions": ["none"],
              "washout_batches": [0], "adaptation": {"batch_size": 2}}
    digest = hashlib.sha256(json.dumps(config, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    (tmp_path / "provenance.json").write_text(json.dumps({"config": config, "config_sha256": digest}))
    (tmp_path / "run_status.json").write_text('{"status":"complete"}')
    identity = {"experiment_id": "fixture_only", "seed": "0", "panel_id": "uci_internal_fixed",
                "scenario": "fixture", "method": "tent", "intervention": "none", "washout_batches": 0}
    a = {"ids": np.array(["1", "2", "3", "4"]), "labels": np.array([0, 1, 0, 1], dtype=np.int64),
         "logits": np.array([[2, 0], [0, 2], [0, 2], [2, 0]], dtype=np.float32)}
    b = {**a, "logits": a["logits"].copy()}
    b["logits"][0] = [0, 2]
    runs = []
    for direction, data in [("ab", a), ("ba", b)]:
        path = f"predictions/{direction}.npz"
        np.savez_compressed(tmp_path / path, **data)
        runs.append({**identity, "direction": direction, "prediction_file": path,
                     **compute_metrics(data["logits"], data["labels"])})
    pair = {**identity, **paired_metrics(a, b, 2)}
    write_csv(tmp_path / "runs.csv", runs)
    write_csv(tmp_path / "paired.csv", [pair])
    suffix = [[{"base_id": str(i), "label": label} for i, label in zip([1, 2], [0, 1])],
              [{"base_id": str(i), "label": label} for i, label in zip([3, 4], [0, 1])]]
    (tmp_path / "manifests" / "0_uci_internal_fixed_fixture_tent.json").write_text(json.dumps({"suffix": suffix}))
    return runs, pair, a, b


def test_metrics_match_closed_form_and_extreme_logits():
    logits = np.zeros((4, 2), dtype=np.float32)
    result = compute_metrics(logits, np.array([0, 1, 0, 1]))
    assert result == pytest.approx({"n": 4, "accuracy": .5, "nll": np.log(2), "brier": .5, "ece15": 0.})
    extreme = compute_metrics(np.array([[1000., -1000.], [-1000., 1000.]]), np.array([0, 1]))
    assert extreme == pytest.approx({"n": 2, "accuracy": 1., "nll": 0., "brier": 0., "ece15": 0.})


def test_complete_saved_fixture_audits_metrics_ids_and_manifest(tmp_path):
    fixture_run(tmp_path)
    report = audit_results(tmp_path)
    assert report["passed"]
    assert report["counts"]["predictions_audited"] == 2
    assert report["counts"]["pairs_audited"] == 1
    assert report["counts"]["manifest_checks"] == 2
    assert any(key.endswith("ab.npz") and len(value) == 64 for key, value in report["input_sha256"].items())
    assert report["failures"] == []


@pytest.mark.parametrize("tamper", ["scalar", "labels", "id_order", "duplicate_file"])
def test_saved_artifact_tampering_is_rejected(tmp_path, tamper):
    runs, pair, a, b = fixture_run(tmp_path)
    if tamper == "scalar":
        runs[0]["accuracy"] += .1
        write_csv(tmp_path / "runs.csv", runs)
    elif tamper == "labels":
        b["labels"] = b["labels"].copy()
        b["labels"][0] = 1
        np.savez_compressed(tmp_path / "predictions" / "ba.npz", **b)
    elif tamper == "id_order":
        b["ids"] = b["ids"][::-1]
        np.savez_compressed(tmp_path / "predictions" / "ba.npz", **b)
    else:
        runs[1]["prediction_file"] = runs[0]["prediction_file"]
        write_csv(tmp_path / "runs.csv", runs)
    report = audit_results(tmp_path)
    assert not report["passed"]
    assert report["failures"]


def test_complete_marker_cannot_hide_missing_mandatory_cell(tmp_path):
    runs, _, _, _ = fixture_run(tmp_path)
    write_csv(tmp_path / "runs.csv", runs[:1])
    assert any("mandatory cells missing" in item for item in validate_inventory(tmp_path))
    with pytest.raises(RuntimeError, match="mandatory cells missing"):
        generate_tables(tmp_path)
    assert not audit_results(tmp_path)["passed"]


def test_cli_returns_nonzero_for_inconsistent_metrics(tmp_path):
    runs, _, _, _ = fixture_run(tmp_path)
    runs[0]["nll"] += 1
    write_csv(tmp_path / "runs.csv", runs)
    script = Path(__file__).resolve().parents[1] / "scripts" / "evaluate.py"
    result = subprocess.run([sys.executable, str(script), "--results", str(tmp_path)], capture_output=True, text=True)
    assert result.returncode == 1
    assert not json.loads((tmp_path / "evaluation_audit.json").read_text())["passed"]
