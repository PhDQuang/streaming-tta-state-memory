"""Immutable matched histories with base-image disjointness checks."""
from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from typing import Callable, Sequence

import numpy as np
import torch

from .utils import object_sha256


@dataclass(frozen=True)
class Sample:
    base_id: str
    domain: str
    severity: int = 0
    path: str = ""
    label: int = -1  # Evaluator metadata only; never sent to adapt_batch.

    def key(self):
        return (self.base_id, self.domain, self.severity, self.path)


@dataclass(frozen=True)
class StreamPanel:
    history_ab: tuple[tuple[Sample, ...], ...]
    history_ba: tuple[tuple[Sample, ...], ...]
    washout: tuple[tuple[Sample, ...], ...]
    suffix: tuple[tuple[Sample, ...], ...]

    def validate(self) -> None:
        def batch_keys(batches):
            return Counter(tuple(s.key() for s in batch) for batch in batches)
        if not self.history_ab or not self.suffix:
            raise ValueError("History and suffix cannot be empty")
        if batch_keys(self.history_ab) != batch_keys(self.history_ba):
            raise ValueError("Histories must contain exactly the same preformed batches")
        pools = [[s.base_id for b in batches for s in b] for batches in (self.history_ab, self.washout, self.suffix)]
        for pool in pools:
            if len(pool) != len(set(pool)):
                raise ValueError("An original image occurs more than once within a panel component")
        for i in range(3):
            for j in range(i):
                if set(pools[i]) & set(pools[j]):
                    raise ValueError("Original-image leakage between history, washout and suffix")
        sizes = {len(b) for batches in (self.history_ab, self.history_ba, self.washout, self.suffix) for b in batches}
        if len(sizes) != 1 or 0 in sizes:
            raise ValueError("Use nonempty equal-sized preformed batches; no silent truncation")

    def manifest(self) -> dict:
        from dataclasses import asdict
        data = {name: [[asdict(s) for s in b] for b in getattr(self, name)] for name in ("history_ab", "history_ba", "washout", "suffix")}
        data["sha256"] = object_sha256(data)
        return data


def batches(samples: Sequence[Sample], batch_size: int) -> tuple[tuple[Sample, ...], ...]:
    if batch_size <= 0 or len(samples) % batch_size:
        raise ValueError("Sample count must be divisible by positive batch size")
    return tuple(tuple(samples[i:i + batch_size]) for i in range(0, len(samples), batch_size))


def make_panel(prefix_ids: Sequence, washout_ids: Sequence, suffix_ids: Sequence,
               domains: tuple[str, str], suffix_domain: str, batch_size: int,
               seed: int, sample_factory: Callable | None = None) -> StreamPanel:
    if len(prefix_ids) % (2 * batch_size):
        raise ValueError("Prefix must contain equal whole-batch domain blocks")
    factory = sample_factory or (lambda idx, domain: Sample(str(idx), domain))
    rng = np.random.default_rng(seed)
    ids = rng.permutation(prefix_ids).tolist()
    half = len(ids) // 2
    a = batches([factory(i, domains[0]) for i in ids[:half]], batch_size)
    b = batches([factory(i, domains[1]) for i in ids[half:]], batch_size)
    panel = StreamPanel(a + b, b + a,
                        batches([factory(i, suffix_domain) for i in washout_ids], batch_size),
                        batches([factory(i, suffix_domain) for i in suffix_ids], batch_size))
    panel.validate()
    return panel


def load_batch(batch: Sequence[Sample], loader: Callable[[Sample], torch.Tensor], device: str) -> torch.Tensor:
    return torch.stack([loader(s) for s in batch]).to(device)

