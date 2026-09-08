"""Training-only sanity data and deterministic image loading/corruption."""
from __future__ import annotations

import hashlib
from pathlib import Path

import numpy as np
from PIL import Image
import torch
import torch.nn.functional as F

from .streams import Sample
from .utils import file_sha256

UCI_TRAIN_SHA = "e1b683cc211604fe8fd8c4417e6a69f31380e0c61d4af22e93cc21e9257ffedd"


def load_uci_train(path: str | Path) -> tuple[torch.Tensor, torch.Tensor]:
    path = Path(path)
    if path.name != "optdigits.tra" or file_sha256(path) != UCI_TRAIN_SHA:
        raise ValueError("Only verified official UCI TRAIN file allowed for local development")
    data = np.loadtxt(path, delimiter=",", dtype=np.float32)
    if data.shape != (3823, 65):
        raise ValueError("Unexpected UCI training data shape")
    x = torch.from_numpy(data[:, :64].reshape(-1, 1, 8, 8).copy()) / 16.0
    y = torch.from_numpy(data[:, 64].astype(np.int64))
    return x, y


def fixed_split(n: int, seed: int, counts: dict[str, int]) -> dict[str, list[int]]:
    if sum(counts.values()) > n or any(v < 0 for v in counts.values()):
        raise ValueError("Split sizes exceed data or are negative")
    indices = np.random.default_rng(seed).permutation(n).tolist()
    out, start = {}, 0
    for name, count in counts.items():
        out[name] = indices[start:start + count]
        start += count
    out["unused"] = indices[start:]
    return out


def corrupt_digit(image: torch.Tensor, domain: str, seed: int) -> torch.Tensor:
    if domain == "clean":
        return image.clone()
    if domain == "noise":
        generator = torch.Generator().manual_seed(seed)
        return (image + 0.30 * torch.randn(image.shape, generator=generator)).clamp(0, 1)
    if domain == "brightness":
        return (image * 0.45 + 0.15).clamp(0, 1)
    if domain == "blur":
        return F.avg_pool2d(image.unsqueeze(0), 3, stride=1, padding=1).squeeze(0)
    raise ValueError(f"Unknown local corruption {domain}")


class DigitLoader:
    def __init__(self, images: torch.Tensor, seed: int):
        self.images, self.seed = images, seed
        self.cache = {}

    def __call__(self, sample: Sample) -> torch.Tensor:
        key = (sample.base_id, sample.domain)
        if key not in self.cache:
            digest = hashlib.sha256(f"{self.seed}/{sample.base_id}/{sample.domain}".encode()).digest()
            self.cache[key] = corrupt_digit(self.images[int(sample.base_id)], sample.domain, int.from_bytes(digest[:4], "little"))
        return self.cache[key]


class ImageLoader:
    def __init__(self, transform):
        self.transform = transform

    def __call__(self, sample: Sample) -> torch.Tensor:
        with Image.open(sample.path) as image:
            return self.transform(image.convert("RGB"))

