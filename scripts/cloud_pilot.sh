#!/usr/bin/env bash
# Run only on an already provisioned machine after explicit user budget approval.
# This script has no payment/provisioning API. Process timeout is not billing shutdown.
set -euo pipefail

python -c 'import torch; assert torch.cuda.is_available(), "CUDA GPU required"; print(torch.cuda.get_device_name(0))'
python scripts/run_cloud_pilot.py --config configs/cloud_pilot.yaml
python scripts/download_data.py imagenet-c --destination datasets/raw/archives --groups noise blur weather --execute
python scripts/prepare_data.py extract \
  --archives datasets/raw/archives/noise.tar datasets/raw/archives/blur.tar datasets/raw/archives/weather.tar \
  --destination datasets/processed/imagenet-c --severities 5 --partition pilot --execute
python scripts/prepare_data.py manifest --download-class-index --batch-size 32
timeout --signal=TERM --kill-after=60s 16h \
  python scripts/run_cloud_pilot.py --config configs/cloud_pilot.yaml --execute --max-hours 16
python scripts/evaluate.py --results results/stage_b_imagenetc_pilot_v1
python scripts/generate_tables.py --results results/stage_b_imagenetc_pilot_v1 --stage B
python scripts/generate_figures.py --results results/stage_b_imagenetc_pilot_v1 --stage B
printf '%s\n' 'Export results/checkpoints/manifests, record actual cost, and terminate the provider instance/storage within the approved ceiling.'
