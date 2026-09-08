"""CPU shape/gradient/replay tests of real untrained cloud architectures.

No pretrained checkpoint, image dataset, or benchmark metric is used. A download
guard makes accidental invocation of the factory's pretrained=True default fail.
"""
from __future__ import annotations

from copy import deepcopy

import pytest
import torch
from torch import nn
import torchvision.models as tv_models
import torchvision.models._api as tv_api

from historytta.adapters import make_adapter
from historytta.models import cloud_model


def assert_tree_equal(a, b):
    if isinstance(a, torch.Tensor):
        assert torch.equal(a, b)
    elif isinstance(a, dict):
        assert a.keys() == b.keys()
        for k in a:
            assert_tree_equal(a[k], b[k])
    elif isinstance(a, (list, tuple)):
        assert len(a) == len(b)
        for x, y in zip(a, b):
            assert_tree_equal(x, y)
    else:
        assert a == b


@pytest.mark.parametrize("backbone", ["resnet50", "vit_b_16"])
def test_factory_smoke_explicitly_disables_pretrained_default(monkeypatch, backbone):
    calls = []

    def guarded_constructor(*, weights):
        calls.append(weights)
        if weights is not None:
            raise RuntimeError("pretrained weights forbidden in CPU smoke")
        return nn.Identity()

    monkeypatch.setattr(tv_models, backbone, guarded_constructor)
    model, _ = cloud_model(backbone, pretrained=False)
    assert isinstance(model, nn.Identity)
    assert calls == [None]
    # Demonstrate that forgetting the explicit flag is caught by this guard.
    with pytest.raises(RuntimeError, match="pretrained weights forbidden"):
        cloud_model(backbone)
    assert calls[-1] is not None


@pytest.mark.parametrize("backbone,shape", [
    ("resnet50", (2, 3, 64, 64)),
    ("vit_b_16", (1, 3, 224, 224)),
])
@pytest.mark.parametrize("method", ["tent", "sar"])
def test_real_untrained_backbone_update_and_exact_resume(monkeypatch, backbone, shape, method):
    torch.set_num_threads(2)
    torch.manual_seed(113)

    def forbid_download(*args, **kwargs):
        raise AssertionError("No pretrained checkpoint download is permitted in this smoke test")

    monkeypatch.setattr(tv_api, "load_state_dict_from_url", forbid_download)
    constructor = getattr(tv_models, backbone)

    def ensure_untrained(*args, **kwargs):
        assert kwargs.get("weights") is None
        return constructor(*args, **kwargs)

    monkeypatch.setattr(tv_models, backbone, ensure_untrained)
    model, _ = cloud_model(backbone, pretrained=False)
    if backbone == "vit_b_16":
        # torchvision initializes this head to zero, blocking upstream norm
        # gradients. Nonzero random weights exercise gradients, not accuracy.
        assert torch.count_nonzero(model.heads.head.weight).item() == 0
        nn.init.normal_(model.heads.head.weight, std=.02)
    adapter = make_adapter(model, method, lr=.01, sar_margin=100., reset_threshold=-1.)
    inventory = adapter.state_inventory()
    trainable = set(inventory["adapted_parameters"])
    assert trainable
    if method == "sar" and backbone == "resnet50":
        assert not any("layer4" in n for n in trainable)
        assert any("layer3" in n for n in trainable)
    if method == "sar" and backbone == "vit_b_16":
        assert not any(f"encoder_layer_{i}." in n for n in trainable for i in (9, 10, 11))
        assert not any(n.startswith("encoder.ln.") for n in trainable)
        assert any("encoder_layer_8." in n for n in trainable)
    before = {n: p.detach().clone() for n, p in model.named_parameters()}
    x = torch.randn(shape)
    # Models have no active dropout in these constructor configurations.
    with torch.no_grad():
        expected_preupdate = model(x).detach().clone()
    logits = adapter.adapt_batch(x)
    assert logits.shape == (shape[0], 1000)
    assert not logits.requires_grad and torch.isfinite(logits).all()
    assert torch.equal(logits, expected_preupdate)
    changed = {n for n, p in model.named_parameters() if not torch.equal(p, before[n])}
    assert changed, "Smoke must exercise a real nonzero gradient update"
    assert changed <= trainable
    assert adapter.aux["updates"] == 1 and adapter.aux["skipped"] == 0
    assert all(p.grad is None for p in model.parameters())
    del before

    state = adapter.snapshot()
    next_x = torch.randn(shape) + .2
    expected_next = adapter.adapt_batch(next_x)
    expected_norms = {n: p.detach().clone() for n, p in model.named_parameters() if n in trainable}
    expected_optimizer = deepcopy(adapter.optimizer.state_dict())
    expected_aux = deepcopy(adapter.aux)
    adapter.restore(state)
    actual_next = adapter.adapt_batch(next_x)
    assert torch.equal(actual_next, expected_next)
    for name, p in model.named_parameters():
        if name in trainable:
            assert torch.equal(p, expected_norms[name])
    assert_tree_equal(adapter.optimizer.state_dict(), expected_optimizer)
    assert_tree_equal(adapter.aux, expected_aux)
    assert torch.isfinite(actual_next).all()
