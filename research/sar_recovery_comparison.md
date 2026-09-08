# Faithful versus complete SAR recovery: actual Stage A comparison

Executed 2026-09-08. Experiment ID: `stage_a_sar_recovery_comparison`. **Complete as a local mechanics experiment; no ImageNet-scale or publication-level empirical claim.** This comparison was added in response to the independent review's concern that ordinary non-recovery parity does not establish recovery fidelity.

## Question and scope

Does faithful pinned SAR behave identically to the complete-state implementation during intrinsic recovery on the actual local image streams? The official SAM wrapper omits its nested SGD momentum from the wrapper checkpoint. `sar_complete` deliberately restores that momentum on recovery. A prior two-parameter quadratic audit established the serialization difference; this experiment asks whether it is expressed on the existing local images. It does not assume the corrected behavior is more accurate.

The reference is [official SAR](https://github.com/mr-eggplant/SAR) at commit `20f6e24b17525f34503510afccedc0629b67b7c4`. Archived `sar.py` and `sam.py` are hash-checked and imported untouched. The complete adapter is the repository implementation documented in [baseline_implementation.md](baseline_implementation.md). No test-time hyperparameters, images or seeds were searched to produce a favorable result.

## Frozen inputs and implementation

- Source: three existing Stage A v1 `DigitCNN` checkpoints trained for 12 epochs on the same 2,048-image internal subset of the official UCI `optdigits.tra` file. Source seeds 17, 29 and 43. The official UCI test file is unused. No model is retrained here.
- Source data SHA256: `e1b683cc211604fe8fd8c4417e6a69f31380e0c61d4af22e93cc21e9257ffedd`. Data loading rejects another file/hash or an unexpected shape.
- Panel: the saved Stage A v1 manifests, `uci_internal_fixed`, split seed 20260908; AB history only, followed by W4 and Q. History 512 images / 16 batches; W 128 images / 4 batches; Q 512 images / 16 batches; batch size 32. Original IDs are disjoint among H/W/Q. One trajectory has 1,152 observations and 36 complete batches per implementation.
- Scenarios: noise + brightness to blur; blur + noise to clean. Corruption transforms and their deterministic image-specific seeds are unchanged from Stage A. The same original-image panel is intentionally reused across scenarios and source seeds: six trajectories are not six independent image panels.
- Both implementations: SGD learning rate .001, momentum .9, SAM rho .05, one two-pass update per batch, entropy margin `.4 * log(10)`, intrinsic threshold .2, current-batch BatchNorm, pre-update prediction. The 10-class margin is explicitly supplied to the reference, whose original default is written for 1,000 classes. This is a local matched recipe, not a reproduction of published ImageNet hyperparameters.
- Each pair receives an independent copy of exactly the same source model. Adapted parameter names and source parameter tensors must match. No external reset intervention is inserted; only each implementation's native automatic recovery runs.
- A read-only forward hook records the actual first/perturbed forward outputs. There is no extra diagnostic forward. The returned tensor must equal the first unperturbed forward. Hooks are removed after each step. Official reset notifications are captured verbatim from stdout.
- Reliable first- and second-pass sample counts, finite forwards/parameters/optimizer state, complete-adapter skips, EMA, per-step resets, parameter/momentum differences and prediction differences are recorded. Any empty filtering, nonfinite state, skipped complete update, or ordinary pre-recovery mismatch fails the comparison and preserves a failed trace. No such failure occurred.
- `step_pair` has no label argument. The stream is adapted before evaluator labels are assembled for metrics. NPZ files retain labels as evaluation metadata, never as adaptation inputs.

The ordinary control applies to the initial trajectory segment before either implementation's first recovery, excluding the recovery step itself. It requires exact equality of logits, post-step model parameters and SGD momentum. It does not require equality after different recovery semantics have intentionally changed the state. Tests additionally compare the observed faithful reference with an independently instantiated unobserved faithful reference.

## Executed commands and observed checks

```text
python -m pytest tests/test_sar_recovery_comparison.py -q
python scripts/compare_sar_recovery.py
```

The final targeted test invocation reported **4 passed in 4.70 seconds**. The actual comparison completed in **9.2081902 seconds** on the existing CPU environment. There were six paired trajectories, 216 valid paired batches, 78 exact ordinary pre-recovery controls, zero empty/nonfinite/skipped batches, and 103 intrinsic recoveries in each implementation (61 in Q, 42 in H/W). There is no GPU throughput inference from this runtime.

A separate read-only check compared the six saved complete-version Q arrays with `results/stage_a_uci_v1/predictions/<seed>_uci_internal_fixed_<scenario>_sar_complete_w4_none_ab.npz`. All six had bit-identical logits, IDs and labels. This verifies that the comparison did not accidentally change the local complete-adapter recipe or panel.

## Recorded suffix results

Errors below are faithful minus complete; negative favors faithful. Disagreement is a fraction of different argmax decisions, not inherently a loss. NLL is stable-log-softmax mean in nats/example. All percentages in this table are explicitly converted from the raw fractions in CSV.

| Seed | Scenario | Total resets faithful / complete | Q resets faithful / complete | Q disagreement (%) | Error gap (points) | NLL gap (nats) | Max Q logit difference |
|---|---|---:|---:|---:|---:|---:|---:|
| 17 | noise_brightness_to_blur | 15 / 15 | 4 / 4 | 0.1953125 | -0.1953125 | -0.000561859892 | 0.0125265121 |
| 17 | blur_noise_to_clean | 18 / 18 | 16 / 16 | 0 | 0 | 0 | 0 |
| 29 | noise_brightness_to_blur | 12 / 12 | 2 / 2 | 0 | 0 | 0.00332255354 | 0.0409965515 |
| 29 | blur_noise_to_clean | 20 / 20 | 16 / 16 | 0 | 0 | 0 | 0 |
| 43 | noise_brightness_to_blur | 18 / 18 | 7 / 7 | 0 | 0 | -0.000627155776 | 0.0187983513 |
| 43 | blur_noise_to_clean | 20 / 20 | 16 / 16 | 0 | 0 | 0 | 0 |

On the corrupted suffix, logits differ for all three source seeds. The largest absolute logit difference is 0.0409965515; the largest absolute NLL difference is 0.00332255354 nats. Only seed 17 changes an argmax decision: 1/512 = 0.1953125 percentage points disagreement, with faithful accuracy 0.736328125 versus complete accuracy 0.734375. This single decision favors the faithful implementation. The other five suffix comparisons have identical decisions; clean-suffix logits are exactly identical.

The first recorded post-step momentum difference occurs at global zero-based batches 9, 10 and 9 for the three corrupted-suffix trajectories; their first logit difference occurs only at batches 25, 23 and 26, respectively. Q begins at batch 20. For the clean-suffix trajectories, momentum differs after batches 18, 16 and 16, but logits remain equal throughout. Both implementations reset on every one of the 16 clean Q batches. These observations illustrate that a state difference can persist without affecting the next reported prediction, and equal recovery counts do not imply equivalent underlying update dynamics.

No confidence interval, p-value, model-superiority claim, or independent-panel mean is reported. This is descriptive evidence on one reused local image panel. Inspect the exact individual scenarios/seeds rather than treating all 6,912 per-implementation observations as independent tests.

## Interpretation and unresolved requirements

The narrow resolved fact is that the two documented recovery semantics can lead to different later outputs on these actual local images. Their mean accuracy difference is neither assumed desirable nor large; complete recovery is not claimed to improve accuracy. In the evaluated trajectories the first/second filters remain nonempty and the finite/skip guards never activate, reducing concern that the observed difference was caused by those extra numerical safeguards. This still does not establish unique causal mediation or a general optimizer-memory law.

The central matched AB/BA history hypotheses are not tested by this comparison, which fixes AB and changes implementation. ImageNet-scale source accuracy and baseline fidelity, the actual history effect after W16, uncertainty across independent image panels, frozen-Q and momentum controls, recent/persistent baselines and second-backbone/dataset replication remain outstanding. This local UCI training-only result cannot choose favorable benchmark hyperparameters or justify a positive continuation gate by itself. See [reviewer_audit.md](reviewer_audit.md).

## Artifact contract and checksums

`runs.csv` contains 12 implementation-level suffix evaluations. `paired.csv` contains six comparisons. Twelve NPZ files retain full H/W/Q logits `[1152,10]`, labels, original IDs, phases and domains; select `phases == 'suffix'` to reproduce the reported metrics. Six JSON traces contain 36 paired batch records each. Six stdout logs retain actual reset notices. Saved manifests and source checkpoint hashes make the input history explicit. Per-batch traces save scalar state diagnostics rather than every full optimizer tensor; the fixed script/checkpoints reproduce those states.

The following SHA256 values were computed from the actual completed artifacts on 2026-09-08. Paths are relative to `results/stage_a_sar_recovery_comparison/`; timestamps and elapsed-time fields make rerun file hashes differ even when predictions replay identically. The runner refuses to overwrite a nonempty output. A fresh rerun needs a new `--output` directory and the preserved Stage A v1 checkpoint paths recorded in provenance.

| Artifact | Bytes | SHA256 |
|---|---:|---|
| `logs/17_blur_noise_to_clean_faithful_stdout.txt` | 1536 | `7aa52f6dfdb9d41a4ca28dceede98d025993ae2a01f99afd47427dd352c42c58` |
| `logs/17_noise_brightness_to_blur_faithful_stdout.txt` | 1440 | `5056a4bf00a74b7ea2fef5f82ab27b0a4ed25ef0cd49625813b3f38ef6ce84c3` |
| `logs/29_blur_noise_to_clean_faithful_stdout.txt` | 1600 | `b3bd23ac7a5bf75b963e12bf26f57112186df485dbf2c230f18bad7640c15962` |
| `logs/29_noise_brightness_to_blur_faithful_stdout.txt` | 1344 | `9b9c8aaf9721491c2cff945853a278afd74ddaab583e073900dc83d3d76467c3` |
| `logs/43_blur_noise_to_clean_faithful_stdout.txt` | 1600 | `b3bd23ac7a5bf75b963e12bf26f57112186df485dbf2c230f18bad7640c15962` |
| `logs/43_noise_brightness_to_blur_faithful_stdout.txt` | 1536 | `2621c3c05d5bc0e9631e21c93ba8093199e50f03b386b9bdfd26b8bdd95daff6` |
| `manifests/17_uci_internal_fixed_blur_noise_to_clean_sar_complete.json` | 232872 | `a794b41bd301d96f91ae4c0b0db5473be6b8ae96f96b90b01c7faf13b96bbcb8` |
| `manifests/17_uci_internal_fixed_noise_brightness_to_blur_sar_complete.json` | 235304 | `1a108a60b2e8ca57543667aa3ce414cb9e4ff060f92c4c11751783e5ef84e694` |
| `manifests/29_uci_internal_fixed_blur_noise_to_clean_sar_complete.json` | 232872 | `a794b41bd301d96f91ae4c0b0db5473be6b8ae96f96b90b01c7faf13b96bbcb8` |
| `manifests/29_uci_internal_fixed_noise_brightness_to_blur_sar_complete.json` | 235304 | `1a108a60b2e8ca57543667aa3ce414cb9e4ff060f92c4c11751783e5ef84e694` |
| `manifests/43_uci_internal_fixed_blur_noise_to_clean_sar_complete.json` | 232872 | `a794b41bd301d96f91ae4c0b0db5473be6b8ae96f96b90b01c7faf13b96bbcb8` |
| `manifests/43_uci_internal_fixed_noise_brightness_to_blur_sar_complete.json` | 235304 | `1a108a60b2e8ca57543667aa3ce414cb9e4ff060f92c4c11751783e5ef84e694` |
| `paired.csv` | 2194 | `9b55e7c15d78f1c455a70ac1fa4b0b7380c393ea2c576b99ae60dee18a413dec` |
| `predictions/17_blur_noise_to_clean_sar_complete.npz` | 48357 | `1b937e03c92820587d4654f9d78f0aaaebbc23501681849404d1f69fb3c5e1b6` |
| `predictions/17_blur_noise_to_clean_sar_faithful_pinned.npz` | 48357 | `1b937e03c92820587d4654f9d78f0aaaebbc23501681849404d1f69fb3c5e1b6` |
| `predictions/17_noise_brightness_to_blur_sar_complete.npz` | 48406 | `dcee8682ddaf92f23e0ca07058fd5838f6aed127ddfe5a65ebfd5072b3309d57` |
| `predictions/17_noise_brightness_to_blur_sar_faithful_pinned.npz` | 48418 | `995ab92a54ca97a14be0b6508c2136051f19db7a266067496bae9e01b46c7327` |
| `predictions/29_blur_noise_to_clean_sar_complete.npz` | 48290 | `ebd4e754831ea56e323538463f8335580392a146318b2614b3350d9a41e8974b` |
| `predictions/29_blur_noise_to_clean_sar_faithful_pinned.npz` | 48290 | `ebd4e754831ea56e323538463f8335580392a146318b2614b3350d9a41e8974b` |
| `predictions/29_noise_brightness_to_blur_sar_complete.npz` | 48390 | `ac39a577d0ee12abe9ba32449a6a033450ba60cf0397ae60037fceef366cc94d` |
| `predictions/29_noise_brightness_to_blur_sar_faithful_pinned.npz` | 48374 | `4935204e8aebd0ee488cbe2973143fba9a52d2cb4249a34ebf4b2e16c4bda7ae` |
| `predictions/43_blur_noise_to_clean_sar_complete.npz` | 48349 | `728d0301e0eb05618e5774d833e15b55c48eade88d8a8de7fff972bbf61c53e6` |
| `predictions/43_blur_noise_to_clean_sar_faithful_pinned.npz` | 48349 | `728d0301e0eb05618e5774d833e15b55c48eade88d8a8de7fff972bbf61c53e6` |
| `predictions/43_noise_brightness_to_blur_sar_complete.npz` | 48408 | `7a64d513982547b2520428c1b6e121d39d9f13edac5267941ca5ca7cee38838b` |
| `predictions/43_noise_brightness_to_blur_sar_faithful_pinned.npz` | 48405 | `dc0dbef672b95283b307f7eb6329e2662fbd2bbcb9c653a3ec5ce33f54ddc167` |
| `provenance.json` | 6750 | `181333f1d993057ffd6bdc431cfeba850ca21f71acad42c6266c4fb86a1990eb` |
| `run_status.json` | 251 | `4cab09fcdcfe2507506aa8d3a3623e50231f98d6e6feffc1f0d50da9c75bf8c1` |
| `runs.csv` | 4768 | `f80cbde3ce4baf8104c4519d5c01fe52cc90b7ae7d23f4f4ba2effdf0104c05e` |
| `summary.json` | 6448 | `05d3a010687dd0bd5eb1f898789b11e63c2ce71a6d6088485392f3a63bc096e3` |
| `traces/17_blur_noise_to_clean.json` | 69247 | `b3db0a5927d7694500a908fafaabec0a7f7f683d363fe909baec760eb66910ad` |
| `traces/17_noise_brightness_to_blur.json` | 69870 | `ddc9a0cea5328e705425c48e742c6a3e6d060ac767811ebb8a96e5178834f674` |
| `traces/29_blur_noise_to_clean.json` | 69357 | `fa42bcbd2828defe3bd924ba231cd3173093b3fd486a2d52079684e2c5481880` |
| `traces/29_noise_brightness_to_blur.json` | 69805 | `cfccab80a2ad2e506dbe99423e85eb1d4547994dd749a26304f5268c37fad0d7` |
| `traces/43_blur_noise_to_clean.json` | 69368 | `a8ac0ea7c79546956491168cab130f94fbdee7569dee21d27829e61ee9640b5c` |
| `traces/43_noise_brightness_to_blur.json` | 69859 | `d8bd81cd562c7304ac79128cab9ede3c598891ccb569ae5339eb8656c8a591d6` |

Source checkpoint hashes recorded by the producer and verified before loading:

| Seed | Recorded path | SHA256 |
|---|---|---|
| 17 | `checkpoints/stage_a_uci_v1_source_17.pt` | `72b0d7194c46341e9c25b27fd37c580bc7736df9bdea2a4259da5ed33ca6be52` |
| 29 | `checkpoints/stage_a_uci_v1_source_29.pt` | `72e87ee75027b756f3652e763a9495fb8b2dfa51966a4a8f771fc1401bdc78ea` |
| 43 | `checkpoints/stage_a_uci_v1_source_43.pt` | `5a1c6afd31e65dff2f8c4b243d88aad4fe3922b10442f06507dc83e21861131d` |

Pinned reference file hashes: `sar.py` = `0553a395ac2bc087049720f1f162789079fe5ee25aa6a1cf82b2ea6286d66eff`; `sam.py` = `b0569de29015016996feae257d30be6cc36f80d42d0f51d4a201eb39d2491712`. Complete adapter and comparison script source hashes, software versions, original Stage A config and source-provenance checksum are recorded in `provenance.json`. No original run file was overwritten.
