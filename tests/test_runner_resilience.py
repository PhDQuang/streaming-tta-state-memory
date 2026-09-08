from copy import deepcopy
import importlib.util
import json
from pathlib import Path
import random

import numpy as np
import pytest
import torch
from torch import nn

from historytta.adapters import make_adapter
from historytta.runner import (batch_rng_schedule, execute_panel, forward_sequence,
                               junction_config_sha256, load_junction_checkpoint,
                               rng_snapshot, save_junction_checkpoint, tree_equal)
from historytta.streams import Sample, make_panel
from historytta.utils import file_sha256, object_sha256, seed_all


def model():
    return nn.Sequential(nn.Linear(4, 6), nn.LayerNorm(6), nn.Dropout(.35), nn.Linear(6, 3))


def panel():
    return make_panel(list(range(8)), list(range(8, 16)), list(range(16, 24)),
                      ("a", "b"), "q", 2, 17,
                      lambda i, d: Sample(str(i), d, label=i % 3))


def stochastic_loader(sample):
    # Every RNG owned by the runner participates. Labels intentionally unused.
    return (torch.rand(4) + np.random.random() + random.random()
            + int(sample.base_id) / 100.)


META = {"seed": 71, "panel_id": "test_panel", "scenario": "a_b_q", "experiment_id": "test"}


def test_common_tail_dropout_and_random_inputs_are_position_independent():
    seed_all(17, 2)
    p = panel()
    adapter = make_adapter(model(), "norm")  # train-mode dropout, no weight updates
    w_seeds = batch_rng_schedule(p.washout, META, "W")
    full, _, _ = forward_sequence(adapter, p.washout, stochastic_loader, "cpu", rng_schedule=w_seeds)
    # Arbitrarily different prior RNG history must not alter paired W batches.
    torch.rand(103)
    np.random.random(57)
    random.random()
    short, _, _ = forward_sequence(adapter, p.washout[-2:], stochastic_loader, "cpu", rng_schedule=w_seeds[-2:])
    assert torch.equal(full[-len(short):], short)
    assert w_seeds != batch_rng_schedule(p.washout, META, "Q")
    h_ab = dict(zip([tuple(s.key() for s in b) for b in p.history_ab], batch_rng_schedule(p.history_ab, META, "H")))
    h_ba = dict(zip([tuple(s.key() for s in b) for b in p.history_ba], batch_rng_schedule(p.history_ba, META, "H")))
    assert h_ab == h_ba
    relabeled = tuple(tuple(Sample(s.base_id, s.domain, label=(s.label+1)%3) for s in batch) for batch in p.washout)
    assert batch_rng_schedule(relabeled, META, "W") == w_seeds


def test_stochastic_execute_panel_controls_and_saved_images(tmp_path):
    seed_all(23, 2)
    p = panel()
    adapter = make_adapter(model(), "tent", lr=.03)
    _, controls = execute_panel(adapter, p, stochastic_loader, tmp_path, META,
                                washout_lengths=(1, 4), interventions=["none", "parameters", "all"],
                                save_images=True)
    assert controls and all(c["passed"] for c in controls)
    schedule = batch_rng_schedule(p.suffix, META, "Q")
    # Saved input images must be the same stochastic preprocessing realization
    # used in the first forward, not new draws made after suffix adaptation.
    from historytta.runner import _seed_batch
    expected_images = []
    for batch, seed in zip(p.suffix, schedule):
        _seed_batch(seed)
        expected_images.extend(stochastic_loader(s) for s in batch)
    expected = torch.stack(expected_images).numpy().astype(np.float16)
    for filename in (tmp_path / "predictions").glob("*none*.npz"):
        with np.load(filename) as raw:
            assert np.array_equal(raw["images"], expected)


@pytest.mark.parametrize("prefix_batches", [0, 3])
@pytest.mark.parametrize("method", ["tent", "sar"])
def test_disk_junction_restores_rng_optimizer_and_immutable_anchor(tmp_path, prefix_batches, method):
    seed_all(29, 2)
    p = panel()
    base = model()
    source_path = tmp_path / "source.pt"
    torch.save(base.state_dict(), source_path)
    config_hash = object_sha256({"full_yaml": "test", "method": method})
    source = {"path": str(source_path), "sha256": file_sha256(source_path), "config_sha256": config_hash}
    adapter = make_adapter(base, method, lr=.02, sar_margin=100., reset_threshold=-1.)
    source_anchor = deepcopy(adapter._source_state)
    h = p.history_ab[:prefix_batches]
    forward_sequence(adapter, h, stochastic_loader, "cpu", rng_schedule=batch_rng_schedule(h, META, "H"))
    junction = adapter.snapshot()
    saved_rng = rng_snapshot()
    filename = tmp_path / "junction.pt"
    save_junction_checkpoint(filename, adapter, junction, META, p.manifest()["sha256"], source_checkpoint=source)
    q_seeds = batch_rng_schedule(p.suffix, META, "Q")
    expected, _, _ = forward_sequence(adapter, p.suffix, stochastic_loader, "cpu", rng_schedule=q_seeds)
    expected_final = adapter.snapshot()

    # A new model intentionally has different initial weights. Loading a current
    # snapshot without the immutable source anchor would give incorrect recovery.
    seed_all(999, 2)
    restored = make_adapter(model(), method, lr=.02, sar_margin=100., reset_threshold=-1.)
    assert not tree_equal(restored._source_state["parameters"], source_anchor["parameters"])
    load_junction_checkpoint(filename, restored, expected_config_sha256=config_hash,
                             expected_manifest_sha256=p.manifest()["sha256"], source_checkpoint=source)
    assert tree_equal(restored.snapshot(), junction)
    assert tree_equal(restored._source_state, source_anchor)
    assert tree_equal(rng_snapshot(), saved_rng)
    actual, _, _ = forward_sequence(restored, p.suffix, stochastic_loader, "cpu", rng_schedule=q_seeds)
    assert torch.equal(actual, expected)
    assert tree_equal(restored.snapshot(), expected_final)
    restored.reset_components(["all"])
    assert tree_equal(restored.snapshot(), source_anchor)


def test_checkpoint_rejects_wrong_config_manifest_source_and_corruption(tmp_path):
    seed_all(31)
    p = panel()
    adapter = make_adapter(model(), "tent", lr=.02)
    source_path = tmp_path / "source.pt"
    torch.save(adapter.model.state_dict(), source_path)
    source = {"path": str(source_path), "sha256": file_sha256(source_path)}
    checkpoint = tmp_path / "junction.pt"
    config_hash = junction_config_sha256(adapter, META)
    manifest_hash = p.manifest()["sha256"]
    save_junction_checkpoint(checkpoint, adapter, adapter.snapshot(), META, manifest_hash, source)
    original = adapter.snapshot()
    with pytest.raises(FileExistsError):
        save_junction_checkpoint(checkpoint, adapter, adapter.snapshot(), META, manifest_hash, source)
    for wrong_config, wrong_manifest in [("wrong", manifest_hash), (config_hash, "wrong")]:
        with pytest.raises(ValueError, match="config/manifest"):
            load_junction_checkpoint(checkpoint, adapter, expected_config_sha256=wrong_config,
                                     expected_manifest_sha256=wrong_manifest)
    with pytest.raises(ValueError, match="configuration differs"):
        load_junction_checkpoint(checkpoint, make_adapter(model(), "tent", lr=.8),
                                 expected_config_sha256=config_hash, expected_manifest_sha256=manifest_hash)
    source_path.write_bytes(b"changed source identity")
    with pytest.raises(ValueError, match="Source checkpoint"):
        load_junction_checkpoint(checkpoint, adapter, expected_config_sha256=config_hash,
                                 expected_manifest_sha256=manifest_hash)
    data = bytearray(checkpoint.read_bytes())
    data[-1] ^= 1
    checkpoint.write_bytes(data)
    with pytest.raises(ValueError, match="integrity"):
        load_junction_checkpoint(checkpoint, adapter, expected_config_sha256=config_hash,
                                 expected_manifest_sha256=manifest_hash)
    assert tree_equal(adapter.snapshot(), original)


@pytest.mark.parametrize("failure", ["nonfinite", "exception"])
def test_failure_keeps_batch_identity_partial_trace_and_raw_state(tmp_path, monkeypatch, failure):
    seed_all(41)
    p = panel()
    adapter = make_adapter(model(), "tent")
    call = adapter.adapt_batch
    count = [0]

    def fail_second(x):
        count[0] += 1
        if count[0] == 2:
            if failure == "exception":
                raise RuntimeError("injected adaptation failure")
            return torch.full((len(x), 3), float("nan"))
        return call(x)

    monkeypatch.setattr(adapter, "adapt_batch", fail_second)
    expected_error = RuntimeError if failure == "exception" else FloatingPointError
    with pytest.raises(expected_error):
        forward_sequence(adapter, p.suffix, stochastic_loader, "cpu",
                         rng_schedule=batch_rng_schedule(p.suffix, META, "Q"),
                         failure_dir=tmp_path, context={**META, "phase": "suffix", "direction": "ab"})
    records = list(tmp_path.glob("*.json"))
    assert len(records) == 1
    record = json.loads(records[0].read_text())
    assert record["status"] == "failed" and record["context"]["batch"] == 1
    assert record["context"]["samples"][0]["base_id"] == p.suffix[1][0].base_id
    assert len(record["completed_trace"]) == 1
    raw = torch.load(tmp_path / record["raw_state_file"], weights_only=False)
    assert len(raw["completed_logits"]) == 1
    assert tree_equal(raw["adapter_snapshot"], adapter.snapshot())
    assert "source_anchor" in raw and "rng" in raw
    if failure == "nonfinite":
        assert torch.isnan(raw["failed_logits"]).all()
    else:
        assert raw["failed_logits"] is None


def test_sanity_source_checkpoint_collision_is_rejected_before_training(tmp_path, monkeypatch):
    scripts = Path(__file__).resolve().parents[1] / "scripts"
    monkeypatch.syspath_prepend(str(scripts))
    spec = importlib.util.spec_from_file_location("sanity_checkpoint_collision_test", scripts / "run_sanity.py")
    script = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(script)
    checkpoint = tmp_path / "checkpoints" / "collision_source_17.pt"
    checkpoint.parent.mkdir()
    checkpoint.write_bytes(b"preserved original anchor")
    with pytest.raises(FileExistsError, match="immutable source checkpoint"):
        # Deliberately invalid training inputs prove rejection happens first.
        script.train_source(None, None, None, 17, {"experiment_id": "collision"}, tmp_path)
    assert checkpoint.read_bytes() == b"preserved original anchor"
