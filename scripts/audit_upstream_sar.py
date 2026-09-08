"""Minimal CPU audit of pinned upstream SAM serialization (no CV benchmark).

The target sequence changes a tiny quadratic objective. It proves an optimizer
state omission and its effect on resumed parameters; it measures no accuracy.
"""
from __future__ import annotations

import argparse
from copy import deepcopy
import importlib.util
import json
from pathlib import Path
import platform
from time import perf_counter

import torch


def run_audit() -> dict:
    started = perf_counter()
    torch.set_num_threads(1)
    root = Path(__file__).resolve().parents[1]
    path = root / "third_party/sar_reference/sam.py"
    spec = importlib.util.spec_from_file_location("pinned_sam_audit", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    initial = torch.tensor([1., -2.], dtype=torch.float64)
    parameter = torch.nn.Parameter(initial.clone())
    optimizer = module.SAM([parameter], torch.optim.SGD, lr=.1, momentum=.9)
    initial_wrapper = deepcopy(optimizer.state_dict())

    def step(p, opt, target):
        opt.zero_grad()
        ((p - target) ** 2).mean().backward()
        opt.first_step(zero_grad=True)
        ((p - target) ** 2).mean().backward()
        opt.second_step(zero_grad=True)

    for target in (0., .3, -.2):
        step(parameter, optimizer, target)
    checkpoint_parameter = parameter.detach().clone()
    checkpoint_wrapper = deepcopy(optimizer.state_dict())
    checkpoint_base = deepcopy(optimizer.base_optimizer.state_dict())
    checkpoint_momentum = optimizer.base_optimizer.state[parameter]["momentum_buffer"].clone()
    for target in (2., -1.):
        step(parameter, optimizer, target)
    future_momentum = optimizer.base_optimizer.state[parameter]["momentum_buffer"].clone()

    with torch.no_grad():
        parameter.copy_(checkpoint_parameter)
    optimizer.load_state_dict(checkpoint_wrapper)
    loaded_momentum = optimizer.base_optimizer.state[parameter]["momentum_buffer"].clone()
    step(parameter, optimizer, .5)
    wrapper_only_next = parameter.detach().clone()

    correct_parameter = torch.nn.Parameter(checkpoint_parameter.clone())
    correct_optimizer = module.SAM([correct_parameter], torch.optim.SGD, lr=.1, momentum=.9)
    correct_optimizer.load_state_dict(checkpoint_wrapper)
    correct_optimizer.base_optimizer.load_state_dict(checkpoint_base)
    step(correct_parameter, correct_optimizer, .5)

    optimizer.load_state_dict(initial_wrapper)
    residual_momentum_after_cold_wrapper_load = bool(optimizer.base_optimizer.state)
    result = {
        "experiment_id": "UPSTREAM_SAM_STATE_CPU_001",
        "date": "2026-09-08",
        "repository": "https://github.com/mr-eggplant/SAR",
        "commit": "20f6e24b17525f34503510afccedc0629b67b7c4",
        "purpose": "Audit optimizer snapshot completeness on a two-parameter quadratic objective",
        "dataset": "none; deterministic synthetic quadratic targets",
        "seed": None,
        "hardware": {"device": "cpu", "platform": platform.platform(), "torch": torch.__version__},
        "config": {"dtype": "float64", "initial_parameter": initial.tolist(), "lr": .1,
                   "momentum": .9, "rho": .05, "checkpoint_targets": [0., .3, -.2],
                   "intervening_targets": [2., -1.], "next_target": .5},
        "wrapper_state_fields": sorted({key for state in checkpoint_wrapper["state"].values() for key in state}),
        "base_state_fields": sorted({key for state in checkpoint_base["state"].values() for key in state}),
        "checkpoint_parameter": checkpoint_parameter.tolist(),
        "checkpoint_momentum": checkpoint_momentum.tolist(),
        "future_momentum": future_momentum.tolist(),
        "momentum_after_wrapper_restore": loaded_momentum.tolist(),
        "wrapper_restore_keeps_future_momentum": torch.equal(loaded_momentum, future_momentum),
        "wrapper_restore_recovers_checkpoint_momentum": torch.equal(loaded_momentum, checkpoint_momentum),
        "wrapper_only_next_parameter": wrapper_only_next.tolist(),
        "complete_restore_next_parameter": correct_parameter.detach().tolist(),
        "next_parameter_max_abs_difference": (wrapper_only_next - correct_parameter.detach()).abs().max().item(),
        "cold_wrapper_load_leaves_base_state": residual_momentum_after_cold_wrapper_load,
        "duration_seconds": perf_counter() - started,
        "training_duration_seconds": 0.,
        "interpretation": "Pinned wrapper state omits SGD momentum; loading wrapper state alone does not restore complete optimizer dynamics.",
        "limits": "No image data, labels, benchmark accuracy, or evidence about the magnitude of any CV performance effect.",
    }
    assert result["wrapper_restore_keeps_future_momentum"]
    assert not result["wrapper_restore_recovers_checkpoint_momentum"]
    assert result["next_parameter_max_abs_difference"] > 0
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path,
                        default=Path(__file__).resolve().parents[1] / "third_party/sar_reference/audit_result.json")
    args = parser.parse_args()
    report = run_audit()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))
