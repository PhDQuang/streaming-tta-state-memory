# Stage A local analysis

Status: completed local correctness experiment, **not confirmation of the scientific hypothesis**. This report describes the final validated local run `results/stage_a_uci_v2`, completed in 144.6726 seconds with 408/408 deterministic controls passing. The run contains 528 directional rows and 264 paired rows. All numerical observations below come from its recorded CSV/NPZ files; no cloud results exist in this report.

## Observations: design, units, and source training

The data source is the official UCI `optdigits.tra` TRAIN file. One fixed identity split supplies 2,048 source-training images, 384 development images, 512 prefix images, 128 common-tail images, and 512 Q images. The local DigitCNN was fitted separately with seeds 17, 29, and 43 for 12 epochs. All source seeds and both scenarios reuse the same image panel, `uci_internal_fixed`. They are not three independent image panels. Scenarios are `noise_brightness_to_blur` (blur Q) and `blur_noise_to_clean` (clean Q). Only W=0 and W=4 batches were run; **W=16, the proposed primary confirmatory condition, was not run locally**.

| Source seed | Epoch-12 training loss | Epoch-12 internal development accuracy (%) |
| --- | --- | --- |
| 17 | 0.001624 | 98.1771 |
| 29 | 0.001138 | 97.6563 |
| 43 | 0.001033 | 98.1771 |

These development accuracies describe source fitting on its internal clean development split. They do not describe adaptation accuracy on corrupted Q, and are not untouched external benchmark test results. The figure `source_training` shows every recorded epoch and seed.

The tables first average reused scenarios within a seed/panel, then repeated seeds within the panel. Directional performance summaries below additionally average AB/BA equally. One panel receives one weight; source-seed SD is descriptive variability, not a population standard error. No confidence interval or p-value is claimed from these three source fits.

## Observations: history sensitivity

Only two no-reset scenario-level comparisons have different AB/BA decisions:

| Method | Seed | Q | W (batches) | AB accuracy (%) | BA accuracy (%) | AB/BA disagreement (percentage points) |
| --- | --- | --- | --- | --- | --- | --- |
| Tent | 17 | blur | 0 | 73.8281 | 73.6328 | 0.1953125 |
| SAR complete-state | 17 | blur | 4 | 73.4375 | 73.6328 | 0.1953125 |

Each row differs on exactly one of 512 Q decisions. All other no-reset decision-disagreement rows are zero. For each affected condition, averaging the clean and blur scenarios gives seed 17 a disagreement of 0.09765625 percentage point; seeds 29 and 43 are zero. Averaging the three source seeds gives **0.03255208 percentage point**, with descriptive seed SD **0.05638186 percentage point**. These tiny nonzero values are not evidence of the proposed 1-percentage-point primary W16 effect.

| Method | W | D: seed 17 (pp) | D: seed 29 (pp) | D: seed 43 (pp) | Mean D (pp) |
| --- | --- | --- | --- | --- | --- |
| Source | 0 and 4 | 0 | 0 | 0 | 0 |
| Normalization only | 0 and 4 | 0 | 0 | 0 | 0 |
| Tent | 0 | 0.09765625 | 0 | 0 | 0.03255208 |
| Tent | 4 | 0 | 0 | 0 | 0 |
| SAR complete-state | 0 | 0 | 0 | 0 | 0 |
| SAR complete-state | 4 | 0.09765625 | 0 | 0 | 0.03255208 |

Zero decision disagreement does not imply equal logits or equal loss. For example, Tent at W4 has zero disagreement but nonzero recorded signed NLL gaps. The raw signed NLL/Brier gaps and first-batch maximum logit differences remain in the generated tables. Absolute error gaps are finite-panel magnitudes; their interpretation does not assume they are unbiased estimates of an absolute population effect.

## Observations: performance and reference-relative harm

The following no-reset W4 accuracies average AB/BA and the two scenarios equally. They must not be confused with the clean source-development accuracies above.

| Method | Seed 17 accuracy (%) | Seed 29 accuracy (%) | Seed 43 accuracy (%) | Mean accuracy (%) | Descriptive seed SD (pp) | Mean NLL (nats/example) |
| --- | --- | --- | --- | --- | --- | --- |
| Source | 86.8164 | 84.3750 | 73.0469 | 81.4128 | 7.3472 | 0.551879 |
| Normalization only | 85.8398 | 84.4727 | 88.0859 | 86.1328 | 1.8244 | 0.513794 |
| SAR complete-state | 85.8887 | 84.4727 | 88.0859 | 86.1491 | 1.8207 | 0.514120 |
| Tent | 86.1328 | 84.4727 | 88.0859 | 86.2305 | 1.8086 | 0.514407 |

The mean accuracy gains relative to source are 4.7201 pp for normalization only, 4.7363 pp for SAR, and 4.8177 pp for Tent. Relative to normalization only, the adaptive gains are 0.0163 pp for SAR and 0.0977 pp for Tent. Both adaptive methods have slightly higher average NLL than normalization only. These are descriptive contrasts from one panel, not method-superiority claims.

Pooling conceals source-relative harm. On the blur-Q scenario at W4:

| Seed | Source accuracy (%) | Norm accuracy (%) | SAR accuracy (%) | Tent accuracy (%) | Source NLL | Norm NLL | SAR NLL | Tent NLL |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 17 | 75.3906 | 73.4375 | 73.5352 | 74.0234 | 0.739783 | 0.961012 | 0.960567 | 0.959028 |
| 29 | 70.7031 | 70.8984 | 70.8984 | 70.8984 | 0.937066 | 1.199997 | 1.202248 | 1.207986 |
| 43 | 47.6563 | 77.7344 | 77.7344 | 77.7344 | 1.468689 | 0.756244 | 0.756399 | 0.753599 |

Seed 17 loses 1.9531 pp under normalization only, 1.8555 pp under SAR, and 1.3672 pp under Tent versus source; all three have worse NLL. Seed 29 gains 0.1953 pp in accuracy but has worse NLL under all three. Seed 43 gains 30.0781 pp, largely accounting for the positive aggregate source-relative accuracy contrast. On clean Q, all four methods have the same recorded accuracy for each seed (98.2422%, 98.0469%, and 98.4375%), with small NLL differences.

Generated `source_reference_*`, `norm_reference_*`, and `performance_reset_effects_*` CSVs preserve exact matched scenario/seed/panel/W/direction comparisons before aggregation. Positive error/NLL/Brier/ECE changes mean worse reference-relative performance. Disagreement itself does not define harm.

## Observations: state interventions and deterministic controls

All 408 logged controls pass, each with zero maximum logit difference. The controls cover the recorded replay, cold-reset, first-batch, history-invariance, and declared auxiliary-state null checks identified by their exact IDs in `controls.json`. Every `all` reset comparison has zero AB/BA disagreement, zero first-batch logit difference, and matches its method's cold-start Q control. A cold-start adaptive suffix still updates during Q: it is not the frozen source model.

At SAR seed 17, blur Q, W4, AB/BA first-batch logits are identical, but later Q decisions differ once. The no-reset AB and BA suffixes log 4 and 3 recoveries, respectively. Resetting parameters alone, optimizer alone, or parameters plus optimizer preserves these observed results. Every auxiliary-containing reset, including `all`, gives identical AB/BA decisions and losses and logs 2 recoveries for each direction. SAR auxiliary state includes EMA plus bookkeeping; this is not an EMA-only ablation.

At W4 the complete factorial disagreement contrasts are zero for Tent. For SAR, the auxiliary marginal reset effect is -0.03255208 pp after scenario/seed averaging; other main and interaction contrasts are zero at this decision-level resolution. The extra `all` reset is excluded from the eight-cell factorial because it also restores declared buffers. Nonzero loss contrasts are retained even when decision contrasts vanish.

All-state resets do not uniformly improve performance. Averaging scenarios and directions within each seed:

| Method | W | Accuracy change: seed 17 (pp) | Seed 29 (pp) | Seed 43 (pp) |
| --- | --- | --- | --- | --- |
| Source / normalization only | 0 and 4 | 0 | 0 | 0 |
| SAR complete-state | 0 | +0.09765625 | 0 | 0 |
| SAR complete-state | 4 | +0.04882813 | 0 | 0 |
| Tent | 0 | -0.04882813 | 0 | 0 |
| Tent | 4 | -0.19531250 | 0 | 0 |

Thus eliminating history disagreement cannot be presented as a universally beneficial reset policy. In particular Tent W4 already has zero decision disagreement and the all-state reset reduces seed-17 accuracy. The tables retain the corresponding NLL/Brier/ECE contrasts, including loss changes without accuracy changes.

## Interpretation

The run supplies useful engineering evidence: exact matched streams and declared resets can be executed, replay controls pass, and the analysis separates disagreement from loss and source-relative harm. It also demonstrates why first-batch equality is insufficient to establish future equality when later updates depend on auxiliary state. This conclusion is scoped to the recorded implementation and local trajectories.

The aggregate accuracy differences are mostly associated with normalization and heterogeneous source-model sensitivity to blur. The experiment does not isolate why seed 43's source model is unusually blur-sensitive. The tiny order effects and their absence in most conditions are evidence against claiming a substantial local persistence result. They neither confirm nor refute the locked W16 hypothesis on ImageNet-C.

## Speculation and required next evidence

An EMA-dependent recovery schedule is a plausible explanation for the SAR trajectory above, but a dedicated EMA-only versus bookkeeping control plus state logs would be needed to isolate that component. It is also plausible that source calibration and normalization explain much of the performance heterogeneity; that mechanism was not tested here. These are follow-up hypotheses, not measured findings.

Advance only to the separately specified, small engineering pilot after implementation validation. Keep pilot images disjoint from the reserved confirmation pool; do not tune thresholds against these local outcomes. The planned three-panel pilot can diagnose code, compute, and gross variance but cannot establish broad generalization or adequately characterize tails. Full scientific claims require the frozen W16 estimand, appropriate independent-panel uncertainty, complete baseline/state controls, the specified larger experiment, and cross-backbone/benchmark replication. Stage A alone is not paper-level validation.

## Artifact verification

Machine-generated tables: `results/stage_a_uci_v2/tables/`; figure PNG/PDF/SVG sets and captions: `figures/stage_a_uci_v2/`. All six figure types were visually inspected. Outcome examples select the first eligible sorted source/adapted comparison and first lexicographic IDs within each of all four correctness groups. The selected clean-Q pair has 503 both-correct, 0 source-only-correct, 0 adaptation-only-correct, and 9 both-wrong cases; empty groups are shown explicitly. This deterministic example is illustrative and does not summarize the blur-Q harms above. The manifests retain input/script hashes and selected prediction hashes. Nineteen targeted analysis/evaluation tests pass; fixtures exist only in temporary test directories. Strict generation requires the completed status marker, a matching frozen configuration hash, the complete planned directional/paired cell inventory, and every required stream manifest. An explicit labeled partial-import flag is available for exploratory external data but was not used for these results.

## Independent recomputation and v1/v2 parity

`python scripts/evaluate.py --results results/stage_a_uci_v2` independently recomputed metrics with NumPy from all 528 saved prediction archives, checked all 264 AB/BA pairs, and passed 5,016 scalar comparisons with zero failures. All 528 prediction identity/label sequences matched their immutable Q manifests. The shared identity pool contains 512 original Q images across two scenario groups, again confirming that 528 directional rows are not 528 independent image panels. The audit uses absolute tolerance 1e-7 and zero relative tolerance for scalar CSV metrics, with exact counts and exact identity/order/label checks. It records each input hash, the evaluator hash, metric definitions, maximum numerical differences, counts, and an empty failure list in `results/stage_a_uci_v2/evaluation_audit.json`. A failed audit returns a nonzero CLI exit status. This checks saved-artifact consistency; it does not rerun the model or independently establish the ground-truth annotation provenance.

The retained v1 run and v2 have exactly equal non-timing scientific CSV values: 528 directional rows, 264 paired rows, and 36 source-training rows. All arrays in all 528 corresponding NPZ archives, including optional recorded images, are exactly equal. `results/stage_a_uci_v2/v1_parity_audit.json` records this check. Experiment identifiers, prediction paths, and timing fields are intentionally excluded from CSV-value parity. v2 added standardized RNG/checkpoint/failure-handling infrastructure; deterministic local predictions remained unchanged. v1 took 111.9868 seconds and v2 took 144.6726 seconds, but the latter overlapped other verification work, so these wall-clock measurements are not a controlled performance comparison.
