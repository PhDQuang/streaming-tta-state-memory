from copy import deepcopy
import importlib.util
import io
from pathlib import Path

import pytest
import torch
from torch import nn

from historytta.adapters import make_adapter


REFERENCE = Path(__file__).resolve().parents[1] / "third_party" / "sar_reference"


def reference_module(name):
    spec = importlib.util.spec_from_file_location(f"upstream_{name}", REFERENCE / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class Tiny(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = nn.Conv2d(2, 4, 3, padding=1)
        self.bn = nn.BatchNorm2d(4)
        self.head = nn.Linear(4, 3)
        self.register_buffer("independent_buffer", torch.tensor(17.))

    def forward(self, x):
        return self.head(self.bn(self.conv(x)).tanh().mean((2, 3)))


@pytest.fixture
def setup():
    torch.set_num_threads(1)
    torch.manual_seed(13)
    return Tiny(), [torch.randn(5, 2, 5, 5) + .1 * i for i in range(8)]


def equal_tree(a, b):
    if isinstance(a, torch.Tensor):
        assert torch.equal(a, b)
    elif isinstance(a, dict):
        assert a.keys() == b.keys()
        for k in a:
            equal_tree(a[k], b[k])
    elif isinstance(a, (list, tuple)):
        assert len(a) == len(b)
        for x, y in zip(a, b):
            equal_tree(x, y)
    else:
        assert a == b


@pytest.mark.parametrize("method", ["source", "norm", "tent", "sar"])
def test_preupdate_logits_and_grad_scope(setup, method):
    model, batches = setup
    adapter = make_adapter(model, method, lr=.1, sar_margin=5., reset_threshold=-1.)
    before = adapter.snapshot()
    with torch.no_grad():
        expected = model(batches[0]).clone()
    actual = adapter.adapt_batch(batches[0])
    assert not actual.requires_grad
    torch.testing.assert_close(actual, expected, rtol=0, atol=0)
    changed = [n for n, p in model.named_parameters() if not torch.equal(p, before["parameters"][n])]
    if method in {"tent", "sar"}:
        assert changed
        assert set(changed) <= {"bn.weight", "bn.bias"}
        assert {n for n, p in model.named_parameters() if p.requires_grad} == {"bn.weight", "bn.bias"}
    else:
        assert not changed
    assert all(p.grad is None for p in model.parameters())
    if method != "source":
        assert model.bn.running_mean is None and model.bn.running_var is None
        assert not model.bn.track_running_stats
    with pytest.raises(TypeError):
        adapter.adapt_batch(batches[0], torch.zeros(5))


def test_tent_matches_pinned_reference_over_momentum_steps(setup):
    model, batches = setup
    ref = reference_module("tent")
    ref_model = ref.configure_model(deepcopy(model))
    params, _ = ref.collect_params(ref_model)
    upstream = ref.Tent(ref_model, torch.optim.SGD(params, lr=.02, momentum=.9))
    ours = make_adapter(model, "tent", lr=.02)
    for batch in batches:
        torch.testing.assert_close(ours.adapt_batch(batch), upstream(batch).detach(), rtol=0, atol=0)
        equal_tree(ours.model.state_dict(), upstream.model.state_dict())


def test_sar_matches_pinned_reference_nonempty_no_recovery(setup):
    model, batches = setup
    ref, ref_sam = reference_module("sar"), reference_module("sam")
    ref_model = ref.configure_model(deepcopy(model))
    params, _ = ref.collect_params(ref_model)
    upstream = ref.SAR(ref_model, ref_sam.SAM(params, torch.optim.SGD, lr=.02, momentum=.9), margin_e0=5.)
    ours = make_adapter(model, "sar", lr=.02, sar_margin=5.)
    for batch in batches:
        torch.testing.assert_close(ours.adapt_batch(batch), upstream(batch).detach(), rtol=0, atol=0)
        equal_tree(ours.model.state_dict(), upstream.model.state_dict())
        assert ours.aux["ema"] == pytest.approx(upstream.ema, abs=1e-14)
        assert ours.aux["recoveries"] == 0


@pytest.mark.parametrize("method", ["tent", "sar"])
def test_snapshot_resume_exact_including_momentum_and_aux(setup, method):
    model, batches = setup
    adapter = make_adapter(model, method, lr=.03, sar_margin=5., reset_threshold=-1.)
    for batch in batches[:3]:
        adapter.adapt_batch(batch)
    saved = adapter.snapshot()
    optimizer = adapter.optimizer.base_optimizer if method == "sar" else adapter.optimizer
    assert any("momentum_buffer" in s for s in optimizer.state.values())
    serialized = io.BytesIO()
    torch.save(saved, serialized)
    expected_outputs = [adapter.adapt_batch(b) for b in batches[3:]]
    expected_end = adapter.snapshot()
    serialized.seek(0)
    adapter.restore(torch.load(serialized, weights_only=True))
    # The snapshot object is independent of subsequent adaptation.
    equal_tree(saved, torch.load(io.BytesIO(serialized.getvalue()), weights_only=True))
    for batch, expected in zip(batches[3:], expected_outputs):
        assert torch.equal(adapter.adapt_batch(batch), expected)
    equal_tree(adapter.snapshot(), expected_end)


@pytest.mark.parametrize("component", ["parameters", "optimizer", "buffers", "aux"])
def test_component_reset_isolation(setup, component):
    model, batches = setup
    adapter = make_adapter(model, "sar", lr=.03, sar_margin=5., reset_threshold=-1.)
    original = adapter.snapshot()
    for batch in batches[:3]:
        adapter.adapt_batch(batch)
    model.independent_buffer.add_(3)
    before = adapter.snapshot()
    adapter.reset_components([component])
    after = adapter.snapshot()
    equal_tree(after[component], original[component])
    for untouched in adapter.COMPONENTS - {component}:
        equal_tree(after[untouched], before[untouched])


@pytest.mark.parametrize("method", ["source", "norm", "tent", "sar"])
def test_cold_reset_exact_replay(setup, method):
    model, batches = setup
    adapter = make_adapter(model, method, lr=.03, sar_margin=5., reset_threshold=-1.)
    outputs = [adapter.adapt_batch(b) for b in batches]
    final_state = adapter.snapshot()
    adapter.reset_components(["all"])
    for batch, expected in zip(batches, outputs):
        assert torch.equal(adapter.adapt_batch(batch), expected)
    equal_tree(adapter.snapshot(), final_state)


def test_no_reliable_samples_safely_skip(setup):
    model, batches = setup
    adapter = make_adapter(model, "sar", sar_margin=-1.)
    before = adapter.snapshot()
    logits = adapter.adapt_batch(batches[0])
    assert torch.isfinite(logits).all()
    equal_tree(adapter.snapshot()["parameters"], before["parameters"])
    equal_tree(adapter.snapshot()["optimizer"], before["optimizer"])
    assert adapter.aux["skipped"] == 1
    assert adapter.aux["last_skip_reason"] == "no_reliable_first_samples"


@pytest.mark.parametrize("failure", ["unreliable", "nonfinite", "exception"])
def test_second_pass_failure_restores_perturbation(setup, monkeypatch, failure):
    model, batches = setup
    adapter = make_adapter(model, "sar", sar_margin=.8, reset_threshold=-1.)
    original_forward = model.forward
    calls = [0]

    def changed(x):
        calls[0] += 1
        logits = original_forward(x) * 10
        if calls[0] == 2:
            if failure == "exception":
                raise RuntimeError("injected failure")
            return logits * (0 if failure == "unreliable" else float("nan"))
        return logits

    monkeypatch.setattr(model, "forward", changed)
    before = adapter.snapshot()
    if failure == "exception":
        with pytest.raises(RuntimeError, match="injected failure"):
            adapter.adapt_batch(batches[0])
    else:
        adapter.adapt_batch(batches[0])
        assert adapter.aux["skipped"] == 1
    equal_tree(adapter.snapshot()["parameters"], before["parameters"])
    assert not adapter.optimizer._perturbed
    assert all(p.grad is None for p in model.parameters())


def test_sar_recovery_clears_momentum_but_retains_upstream_ema(setup):
    model, batches = setup
    adapter = make_adapter(model, "sar", sar_margin=5., reset_threshold=-1.)
    initial = adapter.snapshot()
    adapter.adapt_batch(batches[0])
    assert adapter.optimizer.base_optimizer.state
    adapter.reset_threshold = 5.
    adapter.adapt_batch(batches[1])
    assert not adapter.optimizer.base_optimizer.state
    assert adapter.aux["ema"] is not None
    assert adapter.aux["recoveries"] == 1
    equal_tree(adapter.snapshot()["parameters"], initial["parameters"])


def test_sar_exclusions_include_torchvision_vit_names():
    class Names(nn.Module):
        def __init__(self):
            super().__init__()
            self.early = nn.LayerNorm(4)
            self.gn = nn.GroupNorm(2, 4)
            self.norm = nn.LayerNorm(4)
            self.layer4 = nn.Sequential(nn.BatchNorm2d(4))
            self.blocks = nn.ModuleList([nn.LayerNorm(4) for _ in range(12)])
            self.encoder = nn.Module()
            self.encoder.ln = nn.LayerNorm(4)
            self.encoder.layers = nn.ModuleDict({f"encoder_layer_{i}": nn.LayerNorm(4) for i in (8, 9, 10, 11)})

    adapter = make_adapter(Names(), "sar")
    names = adapter.adapted_parameter_names
    assert "early.weight" in names and "gn.weight" in names
    assert "blocks.8.weight" in names
    assert "encoder.layers.encoder_layer_8.weight" in names
    assert all(not any(s in n for s in ["blocks.9", "blocks.10", "blocks.11", "layer4", "norm.", "encoder.ln"])
               for n in names)
    assert not any(f"encoder_layer_{i}." in n for n in names for i in (9, 10, 11))


def test_invalid_components_and_methods(setup):
    model, _ = setup
    with pytest.raises(ValueError):
        make_adapter(deepcopy(model), "invented")
    adapter = make_adapter(model, "norm")
    with pytest.raises(ValueError):
        adapter.reset_components(["invented"])
    with pytest.raises(ValueError):
        make_adapter(nn.Linear(3, 2), "tent")
