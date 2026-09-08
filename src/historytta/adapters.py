"""Label-free source, batch normalization, TENT and complete-state SAR adapters.

SAR/TENT algorithms follow mr-eggplant/SAR at commit
20f6e24b17525f34503510afccedc0629b67b7c4 (BSD-3-Clause; see third_party).
The SAR implementation deliberately repairs optimizer serialization/recovery and
empty/nonfinite updates. It is identified as ``sar_complete``, not an unchanged
published implementation. Snapshot/reset interventions are experimental controls.
"""
from __future__ import annotations

from copy import deepcopy
import math
import re
from typing import Iterable

import torch
from torch import nn


def softmax_entropy(logits: torch.Tensor) -> torch.Tensor:
    return -(logits.softmax(1) * logits.log_softmax(1)).sum(1)


def _sar_excluded(name: str) -> bool:
    # Exact upstream naming policy, plus equivalent torchvision ViT names.
    return ("layer4" in name or any(f"blocks.{i}" in name for i in (9, 10, 11))
            or "norm." in name or name == "norm" or name == "encoder.ln"
            or re.search(r"(?:^|\.)encoder_layer_(?:9|10|11)(?:\.|$)", name) is not None)


def configure_model(model: nn.Module, method: str) -> list[str]:
    """Configure original model in place; return selected affine parameter names."""
    model.requires_grad_(False)
    model.train(method != "source")
    names: list[str] = []
    for module_name, module in model.named_modules():
        if method != "source" and isinstance(module, nn.modules.batchnorm._BatchNorm):
            module.track_running_stats = False
            module.running_mean = None
            module.running_var = None
        if method in {"tent", "sar"} and isinstance(
                module, (nn.modules.batchnorm._BatchNorm, nn.LayerNorm, nn.GroupNorm)):
            if method == "sar" and _sar_excluded(module_name):
                continue
            for name, parameter in module.named_parameters(recurse=False):
                if name in {"weight", "bias"}:
                    parameter.requires_grad_(True)
                    names.append(f"{module_name}.{name}" if module_name else name)
    return names


class CompleteSAM(torch.optim.Optimizer):
    """SAM with the upstream update algebra and explicit nested SGD state.

    Original algorithm: Foret et al., ICLR 2021; upstream implementation credits
    https://github.com/davda54/sam. Crucially, wrapper and SGD have separate state.
    """
    def __init__(self, params, lr: float, momentum: float = .9, rho: float = .05):
        super().__init__(params, dict(lr=lr, momentum=momentum, rho=rho, adaptive=False))
        self.base_optimizer = torch.optim.SGD(self.param_groups, lr=lr, momentum=momentum)
        self.param_groups = self.base_optimizer.param_groups
        self.defaults.update(self.base_optimizer.defaults)
        self._perturbed: list[torch.Tensor] = []

    @torch.no_grad()
    def first_step(self, zero_grad: bool = True) -> None:
        grads = [p.grad.norm(p=2) for g in self.param_groups for p in g["params"]
                 if p.grad is not None]
        if not grads:
            raise RuntimeError("SAM first step requires gradients")
        norm = torch.norm(torch.stack(grads), p=2)
        if not torch.isfinite(norm):
            raise FloatingPointError("nonfinite SAM gradient norm")
        self._perturbed = []
        for group in self.param_groups:
            scale = group["rho"] / (norm + 1e-12)
            for p in group["params"]:
                if p.grad is not None:
                    self.state[p]["old_p"] = p.detach().clone()
                    p.add_(p.grad * scale.to(p))
                    self._perturbed.append(p)
        if zero_grad:
            self.zero_grad(set_to_none=True)

    @torch.no_grad()
    def cancel_perturbation(self) -> None:
        # Restore *all* perturbed parameters, including ones with no second grad.
        for p in self._perturbed:
            p.copy_(self.state[p]["old_p"])
        self._perturbed = []

    @torch.no_grad()
    def second_step(self, zero_grad: bool = True) -> None:
        self.cancel_perturbation()
        self.base_optimizer.step()
        if zero_grad:
            self.zero_grad(set_to_none=True)

    def state_dict(self):
        if self._perturbed:
            raise RuntimeError("Snapshots are supported only between complete batches")
        return {"wrapper": super().state_dict(),
                "base_optimizer": self.base_optimizer.state_dict()}

    def load_state_dict(self, state_dict):
        self.cancel_perturbation()
        super().load_state_dict(state_dict["wrapper"])
        self.base_optimizer.param_groups = self.param_groups
        self.base_optimizer.load_state_dict(state_dict["base_optimizer"])
        self.param_groups = self.base_optimizer.param_groups


def _buffers(model: nn.Module) -> dict:
    return {f"{nm}.{name}" if nm else name: value
            for nm, module in model.named_modules() for name, value in module._buffers.items()}


class Adapter:
    """One prequential batch update with complete, independent branch state."""
    COMPONENTS = {"parameters", "optimizer", "buffers", "aux"}

    def __init__(self, model: nn.Module, method: str, lr: float = 1e-3,
                 momentum: float = .9, sar_margin: float | None = None,
                 reset_threshold: float = .2):
        if method == "sar_complete":
            method = "sar"
        if method not in {"source", "norm", "tent", "sar"}:
            raise ValueError(f"Unsupported method: {method}")
        if lr < 0 or momentum < 0 or momentum > 1:
            raise ValueError("Expected nonnegative lr and momentum in [0, 1]")
        self.model, self.method = model, method
        self.implementation = "sar_complete" if method == "sar" else method
        self.sar_margin, self.reset_threshold = sar_margin, reset_threshold
        self.adapted_parameter_names = configure_model(model, method)
        params = [p for p in model.parameters() if p.requires_grad]
        if method in {"tent", "sar"} and not params:
            raise ValueError(f"{method} has no eligible normalization affine parameters")
        self.optimizer = (CompleteSAM(params, lr, momentum) if method == "sar" else
                          torch.optim.SGD(params, lr=lr, momentum=momentum)
                          if method == "tent" else None)
        self.aux = {"ema": None, "updates": 0, "skipped": 0, "recoveries": 0,
                    "last_skip_reason": None}
        self._source_state = self.snapshot()

    def snapshot(self) -> dict:
        """Serializable deep independent snapshot, including nonpersistent buffers.

        Random-number generators and input-stream position are external state and
        must be saved by the runner. Model object identity is intentionally stable.
        """
        return deepcopy({
            "schema": 1, "method": self.method, "implementation": self.implementation,
            "parameters": {n: p.detach().clone() for n, p in self.model.named_parameters()},
            "buffers": {n: None if b is None else b.detach().clone()
                        for n, b in _buffers(self.model).items()},
            "optimizer": None if self.optimizer is None else self.optimizer.state_dict(),
            "aux": self.aux,
            "training": {n: m.training for n, m in self.model.named_modules()},
            "requires_grad": {n: p.requires_grad for n, p in self.model.named_parameters()},
            "batchnorm_tracking": {n: m.track_running_stats for n, m in self.model.named_modules()
                                   if isinstance(m, nn.modules.batchnorm._BatchNorm)},
            "config": {"sar_margin": self.sar_margin, "reset_threshold": self.reset_threshold},
        })

    @torch.no_grad()
    def _restore_components(self, state: dict, components: set[str]) -> None:
        if "parameters" in components:
            current = dict(self.model.named_parameters())
            if current.keys() != state["parameters"].keys():
                raise ValueError("Snapshot parameter names do not match")
            for name, parameter in current.items():
                parameter.copy_(state["parameters"][name])
        if "buffers" in components:
            modules = dict(self.model.named_modules())
            if _buffers(self.model).keys() != state["buffers"].keys():
                raise ValueError("Snapshot buffer names do not match")
            for name, buffer in state["buffers"].items():
                module_name, _, leaf = name.rpartition(".")
                current = modules[module_name]._buffers[leaf]
                if buffer is None:
                    modules[module_name]._buffers[leaf] = None
                elif current is None:
                    modules[module_name]._buffers[leaf] = buffer.clone()
                else:
                    current.copy_(buffer)
        if "optimizer" in components and self.optimizer is not None:
            self.optimizer.load_state_dict(deepcopy(state["optimizer"]))
        if "aux" in components:
            self.aux = deepcopy(state["aux"])
            for name, module in self.model.named_modules():
                module.training = state["training"][name]
                if name in state["batchnorm_tracking"]:
                    module.track_running_stats = state["batchnorm_tracking"][name]
            for name, parameter in self.model.named_parameters():
                parameter.requires_grad_(state["requires_grad"][name])
            self.sar_margin = state["config"]["sar_margin"]
            self.reset_threshold = state["config"]["reset_threshold"]
        self.model.zero_grad(set_to_none=True)

    def restore(self, snapshot: dict) -> None:
        if snapshot.get("schema") != 1 or snapshot.get("method") != self.method:
            raise ValueError("Incompatible adapter snapshot")
        self._restore_components(snapshot, self.COMPONENTS)

    def reset_components(self, components: Iterable[str]) -> None:
        if isinstance(components, str):
            components = [components]
        requested = set(components)
        if requested - (self.COMPONENTS | {"all"}):
            raise ValueError(f"Unknown reset components: {requested - self.COMPONENTS - {'all'}}")
        if "all" in requested:
            requested = self.COMPONENTS
        self._restore_components(self._source_state, requested)

    def state_inventory(self) -> dict:
        return {"method": self.method, "implementation": self.implementation,
                "adapted_parameters": list(self.adapted_parameter_names),
                "parameter_count": sum(p.numel() for p in self.model.parameters()),
                "adapted_parameter_count": sum(p.numel() for p in self.model.parameters() if p.requires_grad),
                "buffers": {n: None if b is None else {"shape": list(b.shape), "dtype": str(b.dtype)}
                            for n, b in _buffers(self.model).items()},
                "optimizer": None if self.optimizer is None else type(self.optimizer).__name__,
                "nested_optimizer": "SGD" if self.method == "sar" else None,
                "aux": deepcopy(self.aux),
                "source_state": "initial post-configuration model/optimizer/buffers/aux",
                "rng_owner": "runner"}

    def _finite_grads(self) -> bool:
        grads = [p.grad for p in self.model.parameters() if p.requires_grad and p.grad is not None]
        return bool(grads) and all(torch.isfinite(g).all().item() for g in grads)

    def _skip(self, reason: str) -> None:
        if isinstance(self.optimizer, CompleteSAM):
            self.optimizer.cancel_perturbation()
        self.model.zero_grad(set_to_none=True)
        self.aux["skipped"] += 1
        self.aux["last_skip_reason"] = reason

    def _commit_step(self, sam: bool = False) -> bool:
        """Protect the small adapted parameter/optimizer state from overflow."""
        if sam:
            self.optimizer.cancel_perturbation()
        parameters = [p for p in self.model.parameters() if p.requires_grad]
        original = [p.detach().clone() for p in parameters]
        optimizer_state = deepcopy(self.optimizer.state_dict())
        if sam:
            self.optimizer.base_optimizer.step()
        else:
            self.optimizer.step()
        if not all(torch.isfinite(p).all().item() for p in parameters):
            with torch.no_grad():
                for p, previous in zip(parameters, original):
                    p.copy_(previous)
            self.optimizer.load_state_dict(optimizer_state)
            self._skip("nonfinite_update")
            return False
        self.optimizer.zero_grad(set_to_none=True)
        self.aux["updates"] += 1
        self.aux["last_skip_reason"] = None
        return True

    @torch.enable_grad()
    def adapt_batch(self, x: torch.Tensor) -> torch.Tensor:
        """Return detached PRE-update logits; no labels are accepted or consumed."""
        if self.method in {"source", "norm"}:
            with torch.no_grad():
                return self.model(x).detach().clone()
        self.optimizer.zero_grad(set_to_none=True)
        logits = self.model(x)
        output = logits.detach().clone()
        entropy = softmax_entropy(logits)
        if not torch.isfinite(entropy).all():
            self._skip("nonfinite_first_entropy")
            return output
        if self.method == "tent":
            entropy.mean().backward()
            if self._finite_grads():
                self._commit_step()
            else:
                self._skip("nonfinite_first_gradients")
            return output

        margin = .4 * math.log(logits.shape[1]) if self.sar_margin is None else self.sar_margin
        reliable = entropy < margin
        if not reliable.any():
            self._skip("no_reliable_first_samples")
            return output
        entropy[reliable].mean().backward()
        if not self._finite_grads():
            self._skip("nonfinite_first_gradients")
            return output
        try:
            self.optimizer.first_step()
        except FloatingPointError:
            self._skip("nonfinite_first_gradient_norm")
            return output
        try:
            second_entropy = softmax_entropy(self.model(x))[reliable]
            if not torch.isfinite(second_entropy).all():
                self._skip("nonfinite_second_entropy")
                return output
            reliable_second = second_entropy < margin
            if not reliable_second.any():
                self._skip("no_reliable_second_samples")
                return output
            loss = second_entropy[reliable_second].mean()
            loss.backward()
            if not self._finite_grads():
                self._skip("nonfinite_second_gradients")
                return output
            if not self._commit_step(sam=True):
                return output
            previous_ema = self.aux["ema"]
            self.aux["ema"] = loss.item() if previous_ema is None else .9 * previous_ema + .1 * loss.item()
            if self.aux["ema"] < self.reset_threshold:
                # Match upstream EMA persistence, but restore complete SGD state.
                self.reset_components(["parameters", "optimizer", "buffers"])
                self.aux["recoveries"] += 1
            return output
        finally:
            # Also guarantees no perturbed parameters survive an unexpected error.
            self.optimizer.cancel_perturbation()
            self.model.zero_grad(set_to_none=True)


def make_adapter(model: nn.Module, method: str, lr: float = 1e-3,
                 momentum: float = .9, sar_margin: float | None = None,
                 reset_threshold: float = .2) -> Adapter:
    return Adapter(model, method, lr, momentum, sar_margin, reset_threshold)
