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


def cloud_model(name: str, pretrained: bool = True):
    from torchvision import models
    if name == "resnet50":
        weights = models.ResNet50_Weights.IMAGENET1K_V1
        return models.resnet50(weights=weights if pretrained else None), weights.transforms()
    if name == "vit_b_16":
        weights = models.ViT_B_16_Weights.IMAGENET1K_V1
        return models.vit_b_16(weights=weights if pretrained else None), weights.transforms()
    raise ValueError(f"Unknown backbone {name}")
