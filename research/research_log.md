# Research log

All dates use Asia/Ho_Chi_Minh unless specified. Failed runs remain recorded. Sanity checks are not benchmark evidence.

## INIT-001 — 2026-09-08
- Hypothesis: not selected; compare research directions before implementation.
- Action: read request; initialize repository; delegate independent literature scans; audit hardware and software.
- Hardware: Windows 11, Intel i5-1145G7, 4 cores/8 threads, approximately 31.7 GiB RAM, integrated Iris Xe graphics.
- Observation: only about 7.57 GiB disk free; no NVIDIA CLI found. Avoid large local datasets or GPU-library installations.
- Failed check: initial Git status returned 'not a git repository'; initialized repository afterward. First hardware print used heterogeneous PowerShell table formatting and omitted fields; repeated as structured JSON.
- Interpretation: use existing Python/PyTorch for correctness tests; select scientific direction independent of hardware.
- Next decision: integrate verified literature and candidate matrix.

## LIT-001 — completed broad review and selection

Three independent primary-source scans covered adaptation, segmentation/dense vision and VLM robustness/synthetic data. Generated nine full candidate profiles and weighted matrix; top three T1 controlled histories/state, R2 compositional hard-positive/negative robustness, S1 vocabulary-risk segmentation. Selected T1 after adversarial searches. Novelty/importance/falsifiability dominate weights; compute has 2% and no local-GPU eligibility filter. Consolidated 66 BibTeX entries, including foundational dataset/model/optimizer records. ASR, OATTA, TTABC, GoTTA, AttenDence v1 and AETTA prevent generic novelty claims. Tent/RDumb conference records later resolved from primary sources. Bounded search does not certify absence of prior work. Ledger, candidate matrix and exact evidence retained.

## DESIGN-001 — falsifiable protocol and design corrections

Fixed AB/BA exact preformed batch multiset; original-ID disjoint H/W/Q; final-k tail; intervene after H+W; emit Q pre-update logits; no target labels in adapter API. Independent audit flagged shared-seed pseudoreplication, impossible identity budgets, unjustified sign-flip assumptions and state closure. Revised confirmation sketch to 24 disjoint 1,536-image panels (36,864 IDs) from reserved 80%. Three pilot panels reuse scenarios but remain three units. H1 and H2 exact settings were fixed after local development but before benchmark execution; local results are not preregistered confirmation. Frozen-Q/momentum/swaps/recent-baseline/cross-backbone/dataset requirements remain explicit future work.

## UPSTREAM_SAM_STATE_CPU_001 — actual optimizer audit

Pinned untouched SAR/SAM at `20f6e24b17525f34503510afccedc0629b67b7c4`. Executed deterministic float64 two-parameter quadratic, no dataset/labels. Ordinary wrapper state omitted base-SGD momentum; wrapper-only restore retained intervening momentum. Next-parameter max difference 0.08171052043422922; duration approximately 1.82 CPU seconds. Config/targets/vectors in `third_party/sar_reference/audit_result.json`. This is optimizer restoration evidence, not CV performance. Implemented explicit complete nested state and separate `sar_complete` name; retained faithful code/licenses.

## IMPLEMENT-001 — working baseline and protocol

Implemented source, current-batch norm, Tent, SAR-complete; ordinary reference parity, full state/source-anchor contract, label isolation, paired identities, complete/cold replay, first-batch parameter reset and invariance controls. Actual untrained ResNet50/ViT-B16 BN/LN smoke tests exercise state paths, not pretrained accuracy; random ViT classifier exists only in a smoke fixture. Downloaded original UCI training member after archive/member SHA256 checks (563,639 bytes). Sklearn digits metadata/shape indicated original test partition, so it was excluded; no official test member was extracted or used. Local corruptions are deterministic software probes, not released ImageNet-C corruptions.

## STAGE_A_UCI_V1 — actual tiny experiment

Config `configs/sanity.yaml`; CPU two threads; source seeds 17/29/43; split seed 20260908; train2048/dev384/H512/W128/Q512/unused239. DigitCNN fixed 12 epochs, Adam lr 0.003 B64; adaptation B32 SGD lr 0.001 momentum 0.9; two scenarios, W0/4; nine adaptive arms, source/norm two controls. Output `results/stage_a_uci_v1`: 528 directional runs, 264 pairs, 408/408 controls, 111.9867792 seconds. Fixed-final source development accuracy 98.1771%,97.6563%,98.1771%.

Only two no-reset paired rows differ, each 1/512 =0.1953125 point: Tent seed 17 blur Q/W0 and SAR-complete seed 17 blur Q/W4. Affected scenario/seed-averaged mean 0.03255208 point. All other no-reset decision rows zero; nonzero logits/loss changes retained. SAR logs 2,108 recoveries across 216 overlapping suffix branches and zero skips. Seed17 blur adaptation harms accuracy/NLL; seed 43's approximately 30-point gain drives pooled improvement. Interpretation: implementation evidence with nearly absent local history disagreement, not H1 support or a powered equivalence result.

## REVIEW-FIX-001 — reproducibility hardening

Fixed data API/CLI B64 mismatch to B32. Changed cloud panel IDs to exclude scenario, preventing false panel multiplication. Added per-batch H/W/Q common-random-number schedules excluding labels/direction/method, so matching W draws no longer depend on prefix exposure. This explicitly controls random-history carryover. Added durable checksummed junctions including source anchor/RNG, config/manifest/source validation, failure IDs/inputs/partial traces/state, and per-result source checkpoint collision guards. All changes tested; original v1 preserved under its original ID.

## STAGE_A_UCI_V2 — actual hardened replay

Config `configs/sanity_v2.yaml`, same scientific settings. 144.6726187 CPU seconds; 528 directional/264 paired/408 passing controls. Independent audit recomputed 5,016 scalars, checked all 528 Q manifests, zero failures (max numeric error 2.22e-16). All 528 prediction arrays and scientific CSV/training values exactly match v1; time/experiment IDs excluded. No best-seed/epoch selection. Raw `evaluation_audit.json` and `v1_parity_audit.json` retain evidence.

Initial run provenance correctly records null Git commit. `producer_source.zip` archives 17 exact matching source/config files, including all runtime modules and Stage A entry point. Three later-changed nonproducer analysis/cloud scripts are listed as drift and separately hashed. The final source commit must not be misrepresented as a historical producer commit.

## STAGE_A_SAR_RECOVERY_COMPARISON — actual faithful comparison

Six fixed AB+W4+Q image trajectories: three trained sources × two scenarios, no tuning. Untouched hash-verified official SAR/SAM vs complete adapter. 9.21 CPU seconds; 216 paired batches, 78 ordinary pre-recovery exact controls, valid reliability/finite guards. Each variant logs 103 intrinsic recoveries over full trajectories. One seed 17 blur suffix decision differs and favors faithful SAR by 0.1953125 accuracy point. Other five suffix decisions identical; maximum logit difference 0.04099655, max absolute NLL gap 0.00332255 nats. Complete outputs exactly match corresponding v1 trajectories. Four dedicated tests pass. All raw/source hashes in `sar_recovery_comparison.md`. This does not reproduce published benchmark accuracy or show uniform improvement.

## ANALYSIS-001 — actual summaries and error analysis

Generated all per-run/seed/panel tables, source/norm matched contrasts, P/O/A factorial and reset-performance effects, source training, controls and six PNG/PDF/SVG figure sets. All six types visually inspected; full scales and empty correctness groups explicit; schematic marked nonempirical. One image panel means no local independent-panel CI/p-value. Harmful/negative conditions retained. Strict analysis now requires complete status, frozen config, full expected cells and manifests; partial import is explicit and descriptive. Standalone raw audit and 19 analysis/evaluation tests pass. Final whole-suite outcome recorded under `results/verification`.

## CLOUD-PREP-001 — free preparation only

Implemented safe checksummed archive extraction, pinned canonical class map, hash pilot/reserve split, disjoint sampling, immutable image/manifests/index, absolute-path cloud handshake and strict role/panel/matrix checks. Tiny fixtures only: no local ImageNet-C archive or pretrained cloud weight download. Prepared fixed pilot config and plan-only CLI: 594 pairs /1,188 directional Q runs, 1,216,512 main Q forwards excluding histories/controls/backward/SAR overhead. Three independent panels, three reused scenarios, ResNet50V1, severity 5, B32, W0/4/16.

Cost request: one 24 GB RTX 4090-class GPU, estimated 8–16 experiment hours, 120 GB temporary disk, $20 total ceiling. 108 complete junctions estimated approximately 22 GB, archives 42.48 GB, uncompressed Q logits 4.87 GB. Runtime/storage unprofiled; cost includes setup/idle/storage/fees. Process timeout does not terminate provider billing. No provider/account/payment mutation occurred; full confirmation needs a later justified budget.

## WRITE-REVIEW-001 — honest manuscript and review

Generated all manuscript sections from actual Stage A tables with explicit incomplete evidence status, raw claim values and hashes. No benchmark placeholders filled with fictitious values. Initial hostile rating Strong Reject as a completed paper: absent external evidence, narrow novelty, insufficient baselines, mechanism ambiguities and inadequate precision. Free fixes documented in `reviewer_response.md`; second review retained in `reviewer_audit.md`. Real benchmark/mechanism/generalization blockers remain unresolved.

## NEXT GATE — explicit cost approval

Finish verification/source freeze, then request the concrete $20 Stage B pilot. Until explicit approval, no paid action. Local correctness completion is not completion of the full research objective. Resume from `status.md`, `cloud_gpu_request.md`, reviewer response and raw statuses.

## VERIFY-FINAL-001 ? completed checks

Final full pytest suite: 126 passed, 1 skipped, 18 warnings, 36.23 seconds; JUnit in `results/verification/pytest.xml`. Skip is the existing Windows symlink-privilege case; warnings are Matplotlib dependency deprecations and deliberately exercised partial-import warnings. Independent final audit passed; cloud CLI and local orchestration plan-only commands ran without paid execution. Second reviewer found no substantive remaining free-preparation blocker. Nominal interval coverage and pilot/confirmation size mismatch are explicit. Final source commit is recorded separately without rewriting historical run provenance.
