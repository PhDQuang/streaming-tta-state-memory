"""Per-example metrics and paired, stream-level uncertainty.

Images in an adaptive trajectory are not independent experimental replicates.
Confidence intervals operate on independent stream-level contrasts.
"""
from __future__ import annotations

import numpy as np
from scipy import stats
import torch


def prediction_metrics(logits: torch.Tensor, labels: torch.Tensor) -> dict:
    logits = logits.detach().double().cpu()
    labels = labels.detach().long().cpu()
    if logits.ndim != 2 or labels.ndim != 1 or logits.shape[0] != len(labels) or len(labels) == 0:
        raise ValueError("Expected nonempty [N,C] logits and [N] labels")
    if not torch.isfinite(logits).all():
        raise ValueError("Non-finite logits")
    if labels.min() < 0 or labels.max() >= logits.shape[1]:
        raise ValueError("Class index out of range")
    prob = logits.softmax(-1)
    confidence, prediction = prob.max(-1)
    correct = prediction.eq(labels)
    nll = -logits.log_softmax(-1)[torch.arange(len(labels)), labels]
    one_hot = torch.nn.functional.one_hot(labels, logits.shape[1])
    brier = (prob - one_hot).square().sum(-1)
    ece = 0.0
    edges = torch.linspace(0, 1, 16, dtype=torch.double)
    for i in range(15):
        mask = (confidence >= edges[i]) & ((confidence < edges[i + 1]) if i < 14 else (confidence <= edges[i + 1]))
        if mask.any():
            ece += mask.double().mean().item() * abs(confidence[mask].mean().item() - correct[mask].double().mean().item())
    return {"n": len(labels), "accuracy": correct.double().mean().item(),
            "error": 1 - correct.double().mean().item(), "nll": nll.mean().item(),
            "brier": brier.mean().item(), "ece15": ece,
            "predictions": prediction.tolist(), "confidence": confidence.tolist(),
            "correct": correct.tolist(), "nll_per_example": nll.tolist()}


def paired_summary(values: list[float], confidence: float = 0.95) -> dict:
    a = np.asarray(values, dtype=float)
    if a.ndim != 1 or not len(a) or not np.isfinite(a).all():
        raise ValueError("Need finite, nonempty independent stream contrasts")
    mean = float(a.mean())
    if len(a) < 2:
        return {"n": len(a), "mean": mean, "sd": None, "ci_low": None, "ci_high": None, "individual": a.tolist()}
    sd = float(a.std(ddof=1))
    half = float(stats.t.ppf((1 + confidence) / 2, len(a) - 1) * sd / np.sqrt(len(a)))
    return {"n": len(a), "mean": mean, "sd": sd, "ci_low": mean - half,
            "ci_high": mean + half, "individual": a.tolist()}


def exact_sign_flip_pvalue(values: list[float]) -> float:
    """Two-sided randomization test; requires exchangeable paired assignments.

    Do not apply to a nonnegative disagreement statistic or arbitrary absolute gaps.
    """
    a = np.asarray(values, dtype=float)
    if not len(a) or len(a) > 20 or not np.isfinite(a).all():
        raise ValueError("Require 1–20 finite independent paired contrasts")
    observed = abs(a.mean())
    signs = ((np.arange(2**len(a))[:, None] >> np.arange(len(a))) & 1) * 2 - 1
    return float((np.abs((signs * a).mean(1)) >= observed - 1e-12).mean())


def holm(pvalues: list[float]) -> list[float]:
    p = np.asarray(pvalues, dtype=float)
    if not np.isfinite(p).all() or np.any((p < 0) | (p > 1)):
        raise ValueError("Invalid p-values")
    order = np.argsort(p)
    corrected = np.maximum.accumulate(p[order] * (len(p) - np.arange(len(p))))
    out = np.empty_like(p)
    out[order] = np.minimum(corrected, 1)
    return out.tolist()
