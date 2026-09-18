"""Local correctness model and lazy cloud backbones."""
from __future__ import annotations

import torch
from torch import nn


class DigitCNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.features = nn.Sequential(
            nn.Conv2d(1, 16, 3, padding=1), nn.BatchNorm2d(16), nn.ReLU(),
            nn.Conv2d(16, 32, 3, padding=1), nn.BatchNorm2d(32), nn.ReLU(),
            nn.MaxPool2d(2))
        self.head = nn.Sequential(nn.Flatten(), nn.Linear(32 * 4 * 4, 64), nn.ReLU(), nn.Linear(64, 10))

    def forward(self, x):
        return self.head(self.features(x))


class ProjectedClassifier(nn.Module):
    """Select fixed source logits before probabilities and adaptation losses.

    This is conditional classification over a declared subset, not a newly
    trained head or a Tiny ImageNet-trained model.
    """

    def __init__(self, backbone: nn.Module, source_indices: list[int]):
        super().__init__()
        if (len(source_indices) < 2 or len(set(source_indices)) != len(source_indices)
                or any(type(i) is not int or not 0 <= i < 1000 for i in source_indices)):
            raise ValueError("Projection requires distinct integer ImageNet indices in [0, 1000)")
        self.backbone = backbone
        self.register_buffer("source_indices", torch.tensor(source_indices, dtype=torch.long))

    def forward(self, x):
        logits = self.backbone(x)
        if logits.ndim != 2 or logits.shape[1] != 1000:
            raise ValueError("Projected classifier requires a 1000-logit ImageNet backbone")
        return logits.index_select(1, self.source_indices)


def cloud_model(name: str, pretrained: bool = True):
    from torchvision import models
    if name == "resnet50":
        weights = models.ResNet50_Weights.IMAGENET1K_V1
        return models.resnet50(weights=weights if pretrained else None), weights.transforms()
    if name == "vit_b_16":
        weights = models.ViT_B_16_Weights.IMAGENET1K_V1
        return models.vit_b_16(weights=weights if pretrained else None), weights.transforms()
    raise ValueError(f"Unknown backbone {name}")
