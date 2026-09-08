"""Faithful reference instrumentation checks; random fixtures are not results."""
from copy import deepcopy
import inspect
from pathlib import Path
import sys

import pytest
import torch
from torch import nn

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from compare_sar_recovery import load_reference, make_pair, run, step_pair


class Small(nn.Module):
    def __init__(self, confident=False):
        super().__init__()
        self.conv = nn.Conv2d(2, 4, 3, padding=1)
        self.bn = nn.BatchNorm2d(4)
        self.head = nn.Linear(4, 3)
        if confident:
            with torch.no_grad():
                self.head.weight.mul_(.1)
                self.head.bias.copy_(torch.tensor([5., -3., -3.]))

    def forward(self, x):
        return self.head(self.bn(self.conv(x)).tanh().mean((2,3)))


def test_instrumentation_matches_untouched_reference_on_ordinary_updates():
    torch.set_num_threads(1)
    torch.manual_seed(13)
    model = Small()
    reference = load_reference()
    a,b = make_pair(model, .02, .9, 5., reference)
    independent,_ = make_pair(deepcopy(model), .02, .9, 5., reference)
    for i in range(4):
        x = torch.randn(5,2,5,5) + .1*i
        logits,other,ad,bd,c = step_pair(a,b,x,5.)
        expected = independent(x).detach()
        assert torch.equal(logits, expected) and torch.equal(logits,other)
        assert ad['guard_passed'] and bd['guard_passed']
        assert ad['recoveries'] == bd['recoveries'] == 0
        assert c['post_step_parameter_max_diff'] == c['post_step_momentum_max_diff'] == 0
    assert 'labels' not in inspect.signature(step_pair).parameters


def test_intrinsic_recovery_is_observed_without_modifying_reference():
    torch.set_num_threads(1)
    torch.manual_seed(8)
    model = Small(confident=True)
    a,b = make_pair(model,.02,.9,5.)
    _,_,ad,bd,c = step_pair(a,b,torch.randn(5,2,5,5),5.)
    assert ad['guard_passed'] and bd['guard_passed']
    assert ad['recoveries'] == bd['recoveries'] == 1
    assert 'now reset the model' in ad['stdout']
    assert c['max_logit_diff'] == c['post_step_parameter_max_diff'] == 0
    assert c['post_step_momentum_max_diff'] > 0
    assert a.optimizer.base_optimizer.state and not b.optimizer.base_optimizer.state


def test_empty_filtering_is_detected_as_invalid_not_ordinary_parity():
    torch.set_num_threads(1)
    torch.manual_seed(13)
    a,b = make_pair(Small(), .02,.9,-1.)
    _,_,ad,bd,_ = step_pair(a,b,torch.randn(5,2,5,5),-1.)
    assert ad['first_reliable'] == bd['first_reliable'] == 0
    assert not ad['guard_passed'] and not bd['guard_passed']
    assert bd['skips'] == 1


def test_existing_result_output_is_never_overwritten(tmp_path):
    output = tmp_path/'existing'
    output.mkdir()
    marker = output/'retained.txt'
    marker.write_text('original')
    with pytest.raises(FileExistsError, match='overwrite'):
        run(tmp_path/'absent_source',output)
    assert marker.read_text() == 'original'
