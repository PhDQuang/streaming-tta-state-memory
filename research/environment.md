# Environment audit

Measured 2026-09-08 22:01–22:05, Asia/Ho_Chi_Minh. This audit allocates work; it does not set the scientific ambition.

| Item | Observed |
|---|---|
| OS | Microsoft Windows 11 Home, 64-bit, version 10.0.26200 |
| CPU | Intel Core i5-1145G7 @ 2.60 GHz; 4 cores, 8 logical processors |
| RAM | 34,048,368,640 bytes = 31.71 GiB; approximately 17.5 GiB initially available |
| GPU | Intel Iris Xe integrated graphics, driver 32.0.101.7026 |
| VRAM | Win32_VideoController reports 2,147,479,552 bytes; integrated/shared-memory reporting is not dedicated usable ML VRAM |
| NVIDIA / CUDA | No NVIDIA GPU, nvidia-smi, or nvcc detected; torch.cuda.is_available() false, zero CUDA devices |
| Python | 3.10.0, C:/Program Files/Python310/python.exe |
| PyTorch | 2.9.1+cpu; CUDA build: null |
| torchvision | 0.24.1+cpu |
| NumPy / SciPy | 2.2.6 / 1.13.1 |
| pandas / matplotlib | 2.3.3 / 3.9.0 |
| scikit-learn / Pillow | 1.7.2 / 11.3.0 |
| pytest / PyYAML | 9.0.3 / 6.0.3 |
| transformers | 4.57.3 |
| timm / open_clip_torch | Not installed |
| C: disk free | 8,132,296,704 bytes = 7.57 GiB at audit; shared system disk |
| CLI tools found | python, py, git, rg, wsl, ssh, scp, tar |
| CLI tools not found on PATH | nvidia-smi, nvcc, docker, uv |
| Internet | Web search and primary paper pages accessible; direct HTTPS separately tested in research log |

## Allocation

Local: literature, source development, unit/integration tests, small synthetic or real-data correctness runs, statistical analysis, plots, manuscript. Reuse installed dependencies; limit local datasets to tens of MB initially. Do not download ImageNet-C, large checkpoints, or CUDA wheels here.

Cloud (only after explicit cost approval): pretrained ImageNet-scale baselines, independent streams/seeds, realistic-resolution domain-shift experiments, architecture replication. Keep data and model caches on cloud storage; return compact metrics, manifests, and selected qualitative outputs.

No cloud credentials were inspected and no paid services were started.
