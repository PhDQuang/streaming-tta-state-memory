# Baseline adapter implementation and upstream state audit

Updated 2026-09-08. Scope: correctness infrastructure and a tiny deterministic optimizer experiment. This is not an ImageNet-C reproduction, a benchmark performance result, or a new adaptation method.

## Implemented API

`make_adapter(model, method, lr=1e-3, momentum=.9, sar_margin=None, reset_threshold=.2)` mutates/configures the supplied model and returns an adapter. Supported methods are `source`, `norm`, `tent`, `sar`; `sar_complete` is an explicit alias for `sar`. `state_inventory()['implementation']` always calls the SAR implementation **sar_complete**.

- `adapt_batch(x)` consumes only input tensors. It returns detached logits from the first, unperturbed, **pre-update** forward pass. Evaluation labels never enter the API. TENT takes one entropy SGD step; SAR uses its two-pass reliability-filtered sharpness-aware step.
- `snapshot()` returns deep independent, `torch.save`-compatible parameters, all registered buffers (including `None` and nonpersistent ones), optimizer state, auxiliary state, module training flags, parameter gradient flags, BatchNorm tracking flags, and adaptation configuration.
- `restore(snapshot)` restores that state in place without replacing model parameter identities. RNG state and stream position are the runner's responsibility. The immutable source anchor is supplied by adapter construction; a checkpoint loader must instantiate the same source checkpoint/configuration before restoring current state.
- `reset_components(['parameters', 'optimizer', 'buffers', 'aux'])` resets selected components to the **initial post-configuration** source state. `['all']` restores all four. Resetting parameters includes the full model, although only selected normalization affine values can normally have changed. Optimizer reset includes nested SGD momentum. Auxiliary reset includes SAR EMA, diagnostic counters, modes, gradient flags, and adaptation configuration.
- `state_inventory()` reports the parameter names/counts, registered buffer shapes, optimizer family, auxiliary counters, and implementation identity.

Model buffers are not automatically assumed to be BatchNorm running statistics. For these batch-stat adapters, `running_mean` and `running_var` are set to `None` and `track_running_stats=False`, so a buffer-reset intervention on a standard BN classifier should often be a null intervention. That is an intended negative control. Source inference uses evaluation mode. Other methods use training mode as in the pinned implementation; stochastic layers therefore require paired RNG control even without parameter updates.

## Baseline fidelity and explicit deviations

The primary reference is [official SAR repository](https://github.com/mr-eggplant/SAR), pinned to `20f6e24b17525f34503510afccedc0629b67b7c4`. Unmodified `sar.py`, `sam.py`, `tent.py`, `LICENSE`, and `README.md` are archived in `third_party/sar_reference/`; `manifest.json` stores retrieval URLs and SHA-256 checksums. The repository contains a TENT implementation extended to BN/GN/LN. Consequently our default SGD TENT recipe follows this reference and is not claimed to reproduce every optimizer/backbone recipe in the original TENT paper.

TENT enables only normalization affine scale/bias gradients and optimizes average predictive entropy. SAR selects examples with entropy below its margin, takes the SAM perturbation, filters those same examples again under perturbed weights, and updates using second-pass gradients. The default margin is `.4 * log(number_of_classes)`, agreeing with the published default for 1000 classes. ResNet layer4, timm ViT blocks 9–11/final norm, and analogous torchvision ViT encoder layers 9–11/final encoder norm are excluded for SAR. Our code freezes the excluded parameters rather than needlessly computing gradients that the optimizer never applies. BN1d/3d support generalizes the reference's BN2d-only handling.

The following changes are deliberate and must be disclosed in experimental metadata:

1. **Complete optimizer serialization and recovery.** Upstream SAM wrapper state does not contain its nested SGD momentum. Our serializer stores both. Automatic SAR recovery restores both, unlike a literal upstream wrapper-only reset. Therefore SAR with recovery is called `sar_complete`, and cannot be described as an unmodified published baseline.
2. **Empty/unreliable and nonfinite updates are skipped.** No empty means are backpropagated. If the second pass has no reliable samples, nonfinite loss/gradient, or throws an exception, all perturbed parameters are restored. Finite-gradient parameter overflow is rolled back together with optimizer state. These cases are counted and logged rather than silently discarded.
3. **Recovery threshold argument is effective.** Pinned upstream accepts `reset_constant_em` but hardcodes the condition `ema < .2`. Our default is identical; explicitly changing `reset_threshold` actually changes the condition and is a protocol variant.
4. **Automatic recovery keeps the latest entropy EMA.** This matches the effective pinned `SAR.forward` behavior: it calls reset, then reassigns the returned EMA. External `reset_components(['all'])` clears EMA to obtain a true cold replay. Diagnostic counters persist through automatic recovery so it is observable.
5. **Pre-update outputs are detached and cloned.** Numerical predictions agree with the first forward; no graph or storage alias can accidentally make a runner score a post-update tensor.

No new reset strategy is proposed by these controls. Stage-level interventions diagnose which existing state components explain a measured history effect.

## Tests actually executed

Command: `python -m pytest tests/test_adapters.py -q`.

Observed 2026-09-08 on Python environment with PyTorch `2.9.1+cpu`: **23 tests passed**, about 3.9 seconds of reported pytest test time. Tests cover:

- exact TENT and SAR parameter/logit parity with pinned reference over eight ordinary nonempty, non-recovery steps with SGD momentum;
- pre-update outputs and absence of a labels argument;
- normalization-only gradients/updates and torchvision ViT exclusion mapping;
- full snapshot save/load replay after momentum accumulates;
- separate parameter/optimizer/buffer/aux reset isolation;
- full cold-reset replay;
- all-unreliable first passes, unreliable/nonfinite/exceptional second passes, complete perturbation restoration;
- automatic recovery clearing nested momentum while retaining effective upstream EMA semantics.

Exact CPU parity is a unit-level result. It does not establish CUDA determinism, reproduce published accuracy, or prove that corrected recovery is better. Important next checks are real baseline accuracy, checkpoint/preprocessing compatibility, calibration of learning rates, and full study accounting of recovery/skip frequencies.

## Actual upstream optimizer audit

Script: `scripts/audit_upstream_sar.py`. Raw result: `third_party/sar_reference/audit_result.json`. Experiment ID: `UPSTREAM_SAM_STATE_CPU_001`.

**Hypothesis:** Pinned upstream SAM wrapper serialization omits SGD momentum, so a wrapper-only restore does not reproduce complete optimizer dynamics after intervening updates.

**Setup:** Two float64 parameters initialized to `[1, -2]`; deterministic quadratic losses with targets `[0, .3, -.2]`, checkpoint, intervening targets `[2, -1]`, then restore and process target `.5`; CPU, SGD learning rate `.1`, momentum `.9`, SAM rho `.05`. No image dataset, training labels, or random seed are needed.

**Observation:** Wrapper state contains `old_p`; base optimizer state contains `momentum_buffer`. Loading the saved wrapper state keeps future momentum rather than the checkpoint momentum. The next parameter update differs from a restore including the base optimizer by maximum absolute value **0.08171052043422922**. Loading the empty initial wrapper state also leaves accumulated base optimizer state populated.

**Interpretation:** In this pinned implementation, a model-plus-wrapper checkpoint is not a complete dynamical state. A causal history study that labels this operation “optimizer reset” would be mis-specified.

**Limitations/speculation:** This tiny example demonstrates a concrete state-serialization issue and parameter divergence only. It provides **no evidence about the size or sign of any computer-vision accuracy effect**. The correction is already standard good practice for nested optimizers and is not claimed as a new optimizer or publication contribution. The relevant scientific project must quantify whether, when and how such persistent state affects genuine held-out stream predictions.

## Faithful-versus-complete recovery on actual local images

Follow-up executed 2026-09-08: `python scripts/compare_sar_recovery.py`. The detailed setup, per-seed results and raw-file checksums are in [sar_recovery_comparison.md](sar_recovery_comparison.md). Raw artifacts are retained in `results/stage_a_sar_recovery_comparison/`; this is a separate experiment from the abstract quadratic optimizer audit above.

The script imports checksum-verified, untouched pinned official `sar.SAR` and `sam.SAM`, and compares them with `sar_complete` on the three existing Stage A v1 source checkpoints, seeds 17/29/43 and the two saved scenarios. Each pair uses exactly the same AB history, final four common-tail batches and suffix (512 + 128 + 512 images, batch size 32). Learning rate .001, momentum .9, margin .4 log(10) and threshold .2 match the fixed Stage A setup. There is no source retraining or hyperparameter search. Adaptation receives images only. A read-only hook records the actual two forward passes and filters; official reset notifications are captured verbatim.

Observed: six paired trajectories, 216 valid paired batches, 78 exact ordinary pre-recovery parameter/momentum/logit controls, no empty/nonfinite or skipped batches, and 103 intrinsic recoveries in each implementation. Runtime was 9.2081902 seconds on CPU. The four dedicated comparison tests passed. All six complete-version suffix logits/IDs/labels were independently found bit-identical to their original Stage A v1 AB/W4/none outputs.

Retained optimizer momentum changed later corrupted-suffix logits despite equal recovery counts. Maximum absolute suffix logit difference was 0.04099655. Only seed 17 on noise+brightness-to-blur changed an argmax prediction: 1/512 = 0.1953125 percentage points disagreement, with the faithful version correct on that one additional image. The other five suffix comparisons had equal decisions; all clean-suffix logits were identical. Largest absolute NLL difference was 0.00332255 nats/example. These findings do not show that complete recovery improves accuracy.

This resolves only the local question of whether the faithful and corrected recovery semantics can differ on real images under the existing Stage A recipe. The small UCI training-only split, shared image panel, three source seeds and two scenarios cannot establish an ImageNet effect, a population confidence interval, or the main history-persistence hypotheses. Faithful-versus-corrected comparison on the actual benchmark, recent baselines, frozen-Q and momentum controls remain required before a strong empirical claim.

## Licenses and citations

The SAR archive retains its BSD-3-Clause license and copyright notice. Original TENT and SAM implementation licenses are preserved separately in `third_party/tent_origin_LICENSE` and `third_party/sam_origin_LICENSE`; the corresponding provenance files pin their license-source commits. These extra license records do not imply that those later code commits were used for numerical parity.

- Dequan Wang, Evan Shelhamer, Shaoteng Liu, Bruno Olshausen, Trevor Darrell. **Tent: Fully Test-Time Adaptation by Entropy Minimization**, ICLR 2021. Official implementation: https://github.com/DequanWang/tent .
- Shuaicheng Niu, Jiaxiang Wu, Yifan Zhang, Zhiquan Wen, Yaofo Chen, Peilin Zhao, Mingkui Tan. **Towards Stable Test-Time Adaptation in Dynamic Wild World**, ICLR 2023. Official implementation and paper link: https://github.com/mr-eggplant/SAR .
- Pierre Foret, Ariel Kleiner, Hossein Mobahi, Behnam Neyshabur. **Sharpness-Aware Minimization for Efficiently Improving Generalization**, ICLR 2021. Upstream implementation credited by SAR: https://github.com/davda54/sam .
