"""Explicit Tiny ImageNet-C exploratory profile and projected ImageNet model.

No Tiny source training is claimed. The 200 output synsets come from the
attached dataset and are verified against the pinned 1000-class ImageNet file.
"""
from __future__ import annotations

import argparse
import json
import math
import os
from pathlib import Path

os.environ.setdefault("CUBLAS_WORKSPACE_CONFIG", ":4096:8")
import _bootstrap
import yaml

from historytta.models import ProjectedClassifier, cloud_model
from historytta.utils import object_sha256
from prepare_data import build_manifests, load_class_index, write_immutable
from run_cloud_pilot import experiment_plan, load_index, run_experiment


def tiny_plan(cfg):
    if (cfg.get("dataset") != "Tiny ImageNet-C" or cfg.get("stage") != "TINY"
            or cfg.get("dataset_profile") != "tiny_imagenet_c"
            or cfg.get("expected_classes") != 200
            or cfg.get("classifier") != "imagenet_200_class_projection"
            or cfg.get("backbone") != "resnet50"):
        raise ValueError("Use the explicit Tiny profile: stage TINY, 200-class projected ResNet50")
    if not math.isclose(cfg["adaptation"]["sar_margin"], .4 * math.log(200), abs_tol=1e-12):
        raise ValueError("Tiny projected SAR margin must be 0.4 * log(200)")
    plan = experiment_plan(cfg)
    plan["interpretation"] = cfg["interpretation"]
    return plan


def load_tiny_index(cfg):
    tiny_plan(cfg)
    # Validate the projection before processing image bytes, against the actual
    # pinned canonical mapping, not a user-supplied list of arbitrary indices.
    mapping, names = load_class_index(Path(cfg["class_index"]), 1000)
    path = Path(cfg["manifest_index"])
    index = json.loads(path.read_text(encoding="utf-8"))
    metadata = index["metadata"]
    synsets = sorted(metadata.get("class_to_idx", {}))
    if len(synsets) != 200 or not set(synsets).issubset(mapping):
        raise ValueError("Tiny output synsets must be 200 canonical ImageNet synsets")
    indices = [mapping[synset] for synset in synsets]
    fingerprint = object_sha256({"synsets": synsets, "indices": indices})
    if (metadata.get("output_imagenet_indices") != indices
            or metadata.get("model_class_names") != [names[i] for i in indices]
            or metadata.get("classifier_sha256") != fingerprint
            or metadata.get("classifier") != cfg["classifier"]
            or metadata.get("input_image_size") != [64, 64]):
        raise ValueError("Tiny output projection or image-size declaration mismatches the canonical source")
    return load_index(path, cfg["adaptation"]["batch_size"], expected_planning=cfg["planning"],
                      dataset_profile="tiny_imagenet_c")


def prepare_tiny(cfg, data_root, class_index, source_records):
    tiny_plan(cfg)
    p = cfg["planning"]
    if p["independent_panels"] != 1 or p["scenarios_per_panel"] != 3:
        raise ValueError("Tiny preliminary preparation is frozen to one panel / three scenarios")
    load_class_index(class_index, 1000)
    # Stage the verified mapping with the source so runtime and exported
    # artifacts also work when an offline mapping was attached in Input.
    runtime_mapping = Path(cfg["class_index"])
    write_immutable(runtime_mapping, class_index.read_bytes())
    index = build_manifests(
        data_root, Path(cfg["manifest_index"]).parent, runtime_mapping,
        severities=(5,), seeds=(101,), prefix_size=p["prefix_images"],
        washout_size=p["washout_images_max"], suffix_size=p["suffix_images"],
        batch_size=cfg["adaptation"]["batch_size"], expected_classes=200,
        source_records=source_records, allow_attached_source=True,
        dataset_profile="tiny_imagenet_c",
    )
    load_tiny_index(cfg)
    print(json.dumps({"index": str(Path(cfg["manifest_index"]).resolve()),
                      "dataset": cfg["dataset"], "classes": 200, "panels": len(index["panels"]),
                      "unique_base_images": p["prefix_images"] + p["washout_images_max"] + p["suffix_images"],
                      "available_pilot_ids": index["metadata"]["available_pilot_ids"],
                      "classifier": cfg["classifier"], "provenance_mode": "declared_attached_dataset"}, indent=2))


def tiny_backbone(cfg, index):
    tiny_plan(cfg)
    indices = index["metadata"]["output_imagenet_indices"]
    if len(indices) != 200:
        raise ValueError("Tiny backbone requires the verified 200-class projection")
    model, transform = cloud_model(cfg["backbone"], pretrained=True)
    return ProjectedClassifier(model, indices), transform


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, default=Path("configs/kaggle_tiny_preliminary.yaml"))
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--max-hours", type=float, default=10)
    args = parser.parse_args()
    cfg = yaml.safe_load(args.config.read_text(encoding="utf-8"))
    plan = tiny_plan(cfg)
    if not args.execute:
        print(json.dumps(plan, indent=2))
        return
    if not 0 < args.max_hours <= 10:
        raise ValueError("Tiny preliminary allowance must be in (0,10] hours")
    run_experiment(cfg, args.max_hours, index_loader=load_tiny_index, backbone_loader=tiny_backbone)


if __name__ == "__main__":
    main()
