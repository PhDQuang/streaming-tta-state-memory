# Real architecture CPU smoke validation

Date: 2026-09-08. These tests use **untrained models and random input tensors**. They establish executable architecture/adapter compatibility, not computer-vision accuracy, published-baseline reproduction, or appropriate experimental hyperparameters.

Command executed:

```text
python -m pytest tests/test_backbones.py -q --durations=6
```

Observed result: **6 passed in 20.34 seconds**, using PyTorch `2.9.1+cpu` and two PyTorch CPU threads. No model weights or datasets were downloaded. Runtime is the local pytest result and is not a cloud latency/throughput estimate.

| Architecture | Input | Adapter | Check outcome |
|---|---|---|---|
| torchvision ResNet50 | 2 × 3 × 64 × 64 | TENT | Finite 2 × 1000 pre-update logits; allowed normalization update; exact replay |
| torchvision ResNet50 | 2 × 3 × 64 × 64 | SAR complete | Finite logits; nonzero update; layer4 excluded; exact replay |
| torchvision ViT-B/16 | 1 × 3 × 224 × 224 | TENT | Finite 1 × 1000 pre-update logits; allowed LayerNorm update; exact replay |
| torchvision ViT-B/16 | 1 × 3 × 224 × 224 | SAR complete | Finite logits; nonzero update; final blocks/norm excluded; exact replay |

Each case explicitly calls `cloud_model(..., pretrained=False)`. A guarded torchvision constructor asserts `weights is None`; a patched weight downloader fails if any checkpoint download is attempted. Two additional tests verify that omitting the explicit flag activates the factory's `pretrained=True` default and is rejected by the guard. These tests do not execute/download the pretrained default.

All cases use seed 113, learning rate .01, momentum .9 and a forced SAR entropy margin of 100 with recovery disabled (`reset_threshold=-1`). These deliberately permissive values exercise optimizer code and are **not proposed settings for the scientific experiment**.

Torchvision initializes the untrained ViT classification head to zero. That produces zero gradients in upstream normalization parameters regardless of entropy filtering. To test an actual update, this smoke deterministically initializes only that head's weight from a normal distribution with standard deviation .02; all other model parameters follow the constructor initialization. This modification has no benchmark interpretation.

Validation checks include the expected output shape, finite pre-update logits, at least one changed parameter, no changes outside the selected normalization affine parameters, no lingering gradients, and SAR's exclusion of ResNet layer4 or torchvision ViT encoder layers 9–11/final `encoder.ln`. After one batch has accumulated momentum, the test saves the complete adapter snapshot, processes a fixed second batch, restores the snapshot, and requires bit-identical second-batch logits, normalization parameters, nested optimizer state and auxiliary state.

These constructor configurations have no active dropout, so the exact replay test does not require RNG restoration. The real runner must still own RNG state for stochastic backbones, augmentations or input ordering. The source checkpoint identity/configuration remains immutable external context for adapter restoration.

No source implementation changes were needed. Tests live in `tests/test_backbones.py`. CUDA operation, pretrained checkpoint accuracy, benchmark preprocessing, and full-study performance still require separate validation.
