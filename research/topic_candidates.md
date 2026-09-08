# Candidate projects and decision matrix

Generated after independent literature reviews; nine complete candidate profiles follow. Scores are subjective research judgments, not measurements. The weights prioritize scientific merit: novelty .20, importance .16, hypothesis .14, feasibility .10, experimental clarity .14, reproducibility .10, dataset quality .08, paper potential .06, compute efficiency .02. Local hardware was excluded from topic scoring. Estimates in individual profiles are unprofiled broad ranges; the selected project's concrete pilot is costed separately.

| ID | Candidate | Novelty | Importance | Hypothesis | Feasibility | Clarity | Reproducibility | Data | Paper | Compute efficiency | Weighted |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| T1 | Controlled history interventions | 7 | 9 | 8 | 8 | 9 | 9 | 9 | 8 | 8 | 8.28 |
| R2 | Composition-specific cross-modal brittleness | 7 | 8 | 9 | 8 | 9 | 9 | 8 | 8 | 8 | 8.18 |
| S1 | Selective-risk transfer under vocabulary expansion | 6 | 8 | 8 | 8 | 9 | 9 | 8 | 7 | 8 | 7.78 |
| T2 | Prior-shift identifiability under feature failure | 6 | 9 | 8 | 6 | 8 | 8 | 9 | 8 | 7 | 7.62 |
| T3 | Mixture versus conditional calibration after adaptation | 6 | 8 | 7 | 8 | 8 | 9 | 9 | 7 | 8 | 7.58 |
| S3 | Semantic metrics under loss of specificity | 5 | 7 | 8 | 8 | 9 | 9 | 8 | 6 | 9 | 7.38 |
| R3 | Concept-role reversal after VLM debiasing | 6 | 8 | 8 | 7 | 8 | 8 | 7 | 7 | 8 | 7.36 |
| R1 | Generator dependence in synthetic model selection | 5 | 8 | 8 | 7 | 8 | 8 | 8 | 7 | 6 | 7.20 |
| S2 | Human-prompt model-ranking transfer | 5 | 8 | 8 | 7 | 8 | 8 | 7 | 6 | 8 | 7.10 |

## Shortlist before final selection

T1, R2, and S1 advance to the adversarial comparison in novelty_analysis.md. This matrix generates a shortlist; the evidence-based final choice is documented separately in proposal.md. Generic versions of several candidates were defeated by prior work and deliberately retained in their profiles.

## Adaptation candidate profiles

## Three research candidates

Scores below are subjective planning judgments, not probabilities or empirical results. Compute estimates are unprofiled 4090/A100-class GPU planning ranges, not rental quotations. Dataset licenses and access conditions need separate verification before execution.

### T1 — What does adaptation remember? Controlled history interventions in streaming vision

- Problem: stream-average performance confounds exposure order, class/domain composition, current samples and residual internal state. A low mean error can mask harmful effects of a previous segment on later unseen images.
- Research question: after matching fixed batches into AB/BA prefixes, a common terminal washout W and a common disjoint probe suffix Q, which state components retain a measurable effect of previous ordering, and how long does that effect persist?
- Hypothesis: at least two architecture/method families exhibit persistent suffix error differences after order-permuted prefixes with identical multisets, and targeted removal of one state component explains a substantial pre-registered fraction of this difference without erasing all useful adaptation. A practical pilot threshold could be ≥1 percentage-point paired mean suffix effect and ≥50% attenuation under a targeted intervention; these are proposed decision thresholds, not expected results.
- Prior work: A01–A09, A13–A16, A20–A21; RDumb/PeTTA/reset studies, UniTTA stream samplers, TTABC controlled update-target study, AttenDence optimizer-memory observation and frozen-teacher work prohibit broad first claims.
- Gap: no equivalent matched-prefix/common-suffix intervention protocol found in this scan; this is provisional until reset/order-aware papers identified by the root are fully checked.
- Contribution: define a history-conditioned test risk contrast; build a sample-ID-preserving stream generator; identify which state causes carryover and whether a source-free diagnostic predicts it; publish negative results if effects vanish.
- Potential novelty: A (new finding) if mechanistic effects generalize; B (combination of controlled experimental design and state intervention) for protocol. A new reset heuristic alone is D.
- Datasets: ImageNet-C with unique base identities partitioned into prefixes/suffixes and development/test identities; CIFAR-100-C for small-scale replication; DomainNet-126 and/or chronological FMoW/EVIS for natural-shift external validity. Never infer chronology from synthetic corruption order.
- Baselines: source, normalization-only, Tent, SAR, EATA, RoTTA, RDumb, PeTTA, and frozen-teacher adaptation where supported. Preserve original algorithm code/hyperparameters and disclose source-statistics needs.
- Metrics: paired suffix error/NLL/Brier differences, risk at fixed coverage, prediction disagreement, recovery horizon with censoring, cumulative excess error versus source; runtime/state memory. Compare signed effects and absolute path variability. A small parameter distance is not evidence of functional equivalence.
- Experiments: permutation pairs with identical batches and prefix multiset; shared suffix; no-update probe at junction; suffix frozen-state and continued-adaptation conditions; fresh-source suffix; sham reset; component reset and factorial combinations; multi-seed/multi-order draws; disjoint-image recurrence; held-out corruptions/backbones; real chronological streams analyzed separately.
- Ablations: factorial source resets and same-component swaps between AB/BA histories for optimizer moments, normalization running state, affine weights, teacher, memory, and all state; within-batch versus between-batch ordering; shared terminal washout of several lengths; prefix duration, severity, class correlation; sample recurrence excluded versus explicitly allowed. All-state reset must produce suffix invariance under common RNG; failure first indicates incomplete serialization, not a scientific history effect.
- Difficulty: medium–high; complete state serialization and truly controlled RNG are difficult. State hybrids can be off-manifold, so resets establish intervention effects, not automatically natural causal mediation.
- Compute: pilot ~20–60 GPU-hours with pretrained backbones; full matrix ~150–400 GPU-hours before profiling, dominated by sequence length/methods/paired orders, storage approximately 150–400 GB if broad corruptions retained remotely. Cache only permitted fixed representations; gradient TTA cannot reuse frozen features as equivalent input.
- Scientific risk: high overlap with order/reset literature; effects might reduce to current batch composition or deliberate shift recency. Shared suffix and washout distinguish persistent history from immediate composition but cannot imply invariance should be desirable in every real stream.
- Probability of interpretable result: subjective 0.85, including a well-powered null. Success does not require a winning algorithm.

### T2 — When prior correction cannot distinguish prevalence from feature failure

- Problem: a changed prediction histogram can reflect class prevalence, a damaged visual representation, or both; correcting a prior may amplify a representation failure.
- Research question: under matched changes in predicted class frequencies, can common prior estimators identify genuine label shift and avoid harmful correction when class-conditionals shift?
- Hypothesis: equal observed prediction-histogram drift can accompany opposite optimal prior-correction directions; estimator disagreement/conditioning explains a measurable failure region better than entropy alone. A source-only learned gate will not uniformly identify all harmful shifts; characterize that boundary honestly.
- Prior work: A04, A06, A09, A12, A18, Bayesian Class Adaptation CVPR2025 (verified abstract at https://cvpr.thecvf.com/virtual/2025/poster/34196).
- Gap: pure-label-shift consistency and joint-shift adaptation exist. Remaining potential is a controlled identifiability stress test using visually realistic shifts and explicit failure contours, not a new general impossibility claim.
- Contribution: generate matched-observable shift pairs, quantify empirical identification limits and compare conservative abstention from prior correction. Analyze a small mixture model as an explanatory example without presenting it as a novel theorem unless further searches support it.
- Potential novelty: A for a generalizable empirical finding; B for a mechanism-specific diagnostic; high risk of prior overlap.
- Datasets: ImageNet-C and ImageNetV2, DomainNet-126 with class-prior resampling; source validation only for calibrators; include pure-label, pure-conditional, joint-shift and no-shift controls.
- Baselines: source, BBSE, EM prior correction (exact reference to verify), LSA, BCA, STAD, RoTTA; oracle target prior only as labeled diagnostic upper-bound, never deployable competitor.
- Metrics: target-prior L1 error, held-out class-conditional error, balanced accuracy, ordinary accuracy, NLL/Brier, harmful-update rate, prediction-histogram residual and estimator condition number.
- Experiments: match predictive marginal shifts across different latent mechanisms; source confusion conditioning sweep; gradual/abrupt prior changes; 3–5 independent source checkpoints where practical and paired stream seeds; compare corrected posteriors with fixed representations to jointly adapted representations.
- Ablations: soft versus hard confusion, regularization, source calibration, sample-window size, fixed/estimated/oracle prior, fixed/adapted backbone, head/tail categories, unseen shift types.
- Difficulty: high mathematical/protocol burden; matched observables may require constrained sampling whose ecological validity must be disclosed.
- Compute: ~30–80 GPU-hours pilot including embedding extraction; ~150–350 GPU-hours full, remote storage 100–300 GB, all unprofiled.
- Scientific risk: abstract nonidentifiability is already known; overly constructed shift pairs could be scientifically uninteresting; unlabeled detection is impossible without assumptions in general.
- Probability of interpretable result: subjective 0.75. Robust negative evidence about detection would be a valid outcome.

### T3 — Does adaptation improve uncertainty, or only change which classes are observed?

- Problem: aggregate calibration and selective-risk changes confound changing class/domain mixtures with within-condition reliability. Entropy-based adaptation may improve accuracy yet damage error detection for rare classes or after transitions.
- Research question: which apparent uncertainty improvements remain after standardizing to a fixed class–domain mixture and holding the image set constant, and which are due to adaptation-induced ranking changes?
- Hypothesis: for a pre-registered subset of streaming methods, aggregate calibration gains reverse or substantially attenuate under fixed-mixture standardization, while conditional risk–coverage exposes harmful carryover not visible in accuracy. Falsify by tight paired intervals excluding a practically relevant mixture/conditional discrepancy.
- Prior work: A07, A10, A11, A17, A19; ordinary TTA calibration benchmarking is expressly not the contribution.
- Gap: potential decomposition of mixture change, score scale and error ranking across time; thorough further search needed before selection.
- Contribution: a paired reliability decomposition and standardized temporal reliability protocol; simple source-calibrated or rank-conservative policies only as explanatory baselines.
- Potential novelty: A for a reproducible mechanism finding, B for a protocol; easily falls to D if reduced to reporting extra ECE tables.
- Datasets: ImageNet-C with fixed identity panels, DomainNet-126, real temporal EVIS/FMoW (condition availability/access checked separately); both actual imbalanced streams and class-reweighted evaluation.
- Baselines: frozen source, source temperature scaling, Tent, SAR, COME, POEM, RoTTA; CLIP/SigLIP TTA-VLM methods for architectural replication if core result warrants it.
- Metrics: proper scores NLL/Brier; class/domain standardized versions; calibration with pre-fixed bins and bin sensitivity; selective risk at fixed coverage, AURC and per-class retention, error-detection AUROC. Avoid treating AUROC or ECE as interchangeable.
- Experiments: same images before/after adaptation; clean to corrupted and return sequences; matched imbalanced/uniform panels; within-class conditional reliability; frozen versus online score calibration; bootstrap by stream/image identity rather than naive batch independence.
- Ablations: prior correction on/off, scalar temperature only, reweighted mixture only, learned-parameter updates only, class-conditional evaluation, held-out confidence thresholds, short versus long streams.
- Difficulty: medium; statistical decomposition is harder than metric computation and missing class support can make reweighting unstable.
- Compute: pilot ~20–50 GPU-hours; full ~120–300 GPU-hours plus shared inference assets; storage 100–300 GB remotely, estimates unprofiled.
- Scientific risk: generic calibration degradation already documented by TTA-VLM and 2026 prompt work; must demonstrate a novel conditional phenomenon across methods and data, not a mathematical Simpson's-paradox illustration.
- Probability of interpretable result: subjective 0.80, including a null conditional-mixture effect.

### Decision matrix (1 low, 10 high)

| ID | Novelty | Importance | Hypothesis | Feasibility | Experimental clarity | Reproducibility | Dataset quality | Paper potential | Compute efficiency |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| T1 | 7 | 9 | 8 | 8 | 9 | 9 | 9 | 8 | 8 |
| T2 | 6 | 9 | 8 | 6 | 8 | 8 | 9 | 8 | 7 |
| T3 | 6 | 8 | 7 | 8 | 8 | 9 | 9 | 7 | 8 |

No overall project is selected by this subagent. T1 is the strongest within this scan, conditional on the root's additional order/reset prior-work audit.

## Adversarial novelty search for T1

### Tested formulations

Exact/synonym queries included `test-time adaptation prefix suffix`, `test-time adaptation common suffix`, `test-time adaptation matched order`, `test-time adaptation path dependence`, `test-time adaptation counterfactual stream`, `test-time adaptation commutator`, `test-time adaptation state transplant`, `test-time adaptation optimizer state`, `test-time adaptation state reset`, `test-time adaptation repeated images`, and `test-time adaptation same images corruptions`. Added `continual test-time adaptation order reset 2026` and `test-time adaptation history controlled` restricted to arXiv/CVF/OpenReview. These returned much unrelated NLP material; a no-hit exact phrase is weak evidence.

### Closest equivalences and boundaries

| Prior | Equivalent portion already occupied | Narrow difference still to test |
|---|---|---|
| UniTTA | factorized domain/class correlation, multiple stream settings | identical complete prefix multiset and identical continuation gives a paired history estimand |
| RDumb | long-horizon collapse, periodic source reset | identify state-specific history effects under a common suffix; no claim that resets are new |
| PeTTA | recurrent domains, perturbation analysis, reset of model/optimizer/memory | cross-order matched exposure and controlled component interventions, rather than average recurring performance |
| POEM | one corrupted version per base image | this alone is not new; disjoint identity is a validity control |
| GoTTA | separately benchmark memory policy, interchangeable memory modules | intervene on complete post-prefix state and carryover horizon; memory-only findings may overlap |
| Intransigent Teacher | isolates teacher plasticity and long-run EMA failure | teacher drift alone insufficient; require general cross-component finding or informative null |
| Recovery Complexity | post-shift recovery and theoretical limits | history-conditioned empirical recovery, under fixed destination samples |
| TTABC | controlled update-target taxonomy; periodic-reset TPT collapse | AB/BA batch-multiset histories, W, Q and component-state interactions |
| AttenDence v1 | optimizer moments affect adaptation even when weights reset | persistent and interacting effects after W on Q; do not claim discovery of optimizer memory |

Root has independently identified AETTA, a 2026 reset-localization paper and an order-aware paper for full checking; this scan does not assert that those have been ruled out. No equivalence claim is settled until those exact primary sources are read.

### Strong skeptical objections and required controls

1. “Order matters” is predictable from noncommuting gradient updates. Merely measuring it is not enough; predict and validate which state retains the effect, its sign, and when it vanishes.
2. Different terminal domains create obvious recency effects. Match a terminal washout segment and vary its length; do not conflate past conditioning with current marginal mismatch.
3. Same prefix multiset still differs in batch composition. Use a primary between-batch permutation of fixed batches, plus a distinct within-batch/mixture experiment.
4. Same-image reuse across corruption domains can create transductive memorization. Split by original image identity and audit it. Explicit recurrence is a separate condition.
5. Component resets create unnatural joint states. Include sham reset, all-state reset, source-reference intervention, fresh optimizer controls and pairwise reset interactions. Call results controlled state-intervention effects, not unqualified causal mediation.
6. Stochastic augmentation can masquerade as order history. Key augmentation randomness to sample identity and exposure count for matched conditions; report that this slightly differs from uncontrolled production stochasticity.
7. A fixed predictor can have worse deployment risk than an adaptive one despite greater path invariance. Judge error/calibration alongside history sensitivity, never minimize sensitivity alone.
8. Thresholds and hyperparameters must be frozen using a separate development identity/shift set. Test-label access belongs only in final metrics and post-hoc scientific diagnosis.

### Current classification

T1 is provisionally A/B only for a specific experimentally supported mechanism and reusable controlled protocol. Generic reset policy, general “history matters,” teacher freezing, memory diversity or recovery-time metric claims are excluded from novelty. Strongest scientifically useful negative result: once current batches, sample identity, update count, terminal washout and complete random state are controlled, purported long-lived history effects vanish or become too small to matter.

An implementation issue (for example a wrapper optimizer omitting nested optimizer state from its checkpoint) is an audit finding, not the proposed scientific mechanism. Any suspected official-baseline issue needs a minimal executable reproduction and faithful-versus-corrected results reported separately; do not silently patch a baseline and describe it as published behavior.

## Search log and verification caveats

All searches dated 2026-09-08 through available web search/open tools. Search families, in order:

1. CVPR2025 TTA class imbalance/label shift; OpenReview TTA temporal correlation; CVPR2023/24 SAR/RoTTA.
2. Evaluation/prequential timing, order/hysteresis, entropy calibration and broad surveys.
3. Primary 2026 probabilistic TTA, recovery theory, calibration-objective preprints.
4. Repeated image/corruption identity, counterfactual streams and component-state interventions.
5. GoTTA memory-policy independence, Protected TTA, RDumb, PeTTA, current teacher-student critique.
6. Exact matched-prefix/shared-suffix terms and synonymous path/optimizer-state terms; recent domain-filtered searches.
7. Metadata/venue resolution through proceedings and author institutional sources; foundational BBSE and temperature scaling.
8. Same-day skeptical-review follow-up: verified Tent's ICLR 2021 conference PDF and RDumb's main NeurIPS 2023 proceedings/poster record; corrected A01/A05 and this scan's BibTeX. These supersede the earlier unresolved-venue notes without changing any numerical result claim.

OpenReview browser challenges blocked some final forum pages. arXiv HTML for unavailable versions failed; successful version numbers are stated explicitly. Secondary search results occasionally mismatched a paper title to an unrelated arXiv ID (notably a discovery result pointing teacher-student work to 2603.02934); that ID was checked, rejected, and replaced with the exact primary 2609.02507. Do not trust generated literature summaries as bibliographic evidence. In particular, UniTTA has only arXiv-2024 status verified here; an earlier informal message suggesting ECCV was corrected.

This scan deliberately marks missing dataset rosters/numerical results as unverified rather than filling from memory. Before manuscript use, relevant selected-project core references need final-version full-text and code audits. No experiments or paid actions were part of this literature scan. Subsequent local implementation/recovery experiments are documented separately in `research/sar_recovery_comparison.md`; no paid action was taken.


## Segmentation candidate profiles

## Three candidates (not a final topic selection)

All compute figures below are planning ranges, not measurements or provider quotations. They assume rented GPU execution only after explicit user approval. All datasets require final source/license/access checks. No benchmark test annotations may be used for tuning; use source training/development partitions to lock all settings.

### S1. Does selective segmentation risk survive vocabulary expansion?

- **Problem:** A confidence threshold chosen for one query vocabulary can change meaning when users alter the vocabulary, despite identical images and target objects.
- **Research question:** How much of risk-transfer failure comes from normalization, joint class-conditioned representation, or mask postprocessing?
- **Hypothesis:** Under prespecified nuisance-label additions, a fixed source threshold exceeds its target accepted-mask error rate by at least five percentage points in at least two model families; at least half the excess disappears after a stage-specific normalization intervention in independent-scoring models but not joint class-aggregation models. These numerical thresholds are preregistration choices, not observations.
- **Prior work:** P04, P07, P10–P16; FreeCP, RevisitOVS and DAC are particularly close.
- **Gap:** Existing verified literature establishes vocabulary accuracy sensitivity and semantic ambiguity. No exact matched-image, matched-target decomposition of transferred selective-risk thresholds was found in this bounded search.
- **Contribution:** A controlled risk-transfer protocol plus stage interventions; only propose a correction after identifying a repeatable mechanism.
- **Potential novelty:** B; narrow conditional finding may be A if replicated across architectures. Generic vocabulary sensitivity is defeated.
- **Datasets:** ADE20K, Pascal Context; COCO panoptic for development; optional LVIS/OmniLabel detection transfer using verified negatives and federated evaluation.
- **Baselines:** FC-CLIP, CAT-Seg, FreeCP; modern SAM 3 concept predictions; maximum probability, raw similarity, entropy, margin, temperature calibration, distance-aware calibration; source-frozen versus vocabulary-recalibrated oracle comparator. Conformal sets are a separate comparator, not interchangeable with selective risk.
- **Metrics:** Image-aggregated accepted-mask error and coverage, risk–coverage area, mIoU/PQ, mask availability/recall, calibration error, latency; confidence intervals clustered by image.
- **Experiments:** Same image/target under random absent labels, hard semantic distractors, duplicate aliases, order permutations and vocabulary cardinality; independently alter normalization, class aggregation and postprocessing; evaluate held-out vocabulary-generation rules. Negative controls include independent logits where irrelevant additions provably leave raw scores unchanged.
- **Ablations:** Fixed versus changing mask proposals, image domain, score type, source calibration size, vocabulary composition versus size, semantic equivalence policy, rare/small objects; three or more calibration seeds, paired image bootstrap.
- **Difficulty:** Medium/high; architecture hooks and matching masks across conditions are substantial.
- **Compute:** Pilot 20–50 GPU-hours on 24–48GB GPU; full inference/ablations 150–400 GPU-hours; approximately 100–250GB cloud storage. Must profile before purchase.
- **Scientific risk:** Simple softmax effects may explain everything; no useful intervention beyond existing calibration; “absent” classes may be incompletely annotated. An image-presence oracle cannot be deployed.
- **Interpretable-result probability:** Estimated 0.85, subjective; even complete normalization explanation is interpretable but may have limited paper novelty.
- **Decision:** Demote relative to less occupied directions. Do not sell generic class filtering or new conformal guarantees.

### S2. Do synthetic prompt protocols preserve human model rankings and tail risk?

- **Problem:** Promptable segmenters are often evaluated with random interior points or perturbed GT boxes, while users choose spatially and sequentially structured prompts.
- **Research question:** Do synthetic protocols correctly rank model quality and predict low-IoU failures on held-out human prompts?
- **Hypothesis:** At matched point count, at least one model-pair ranking reverses between random-point and held-out-human evaluation, with paired confidence interval excluding zero, and synthetic calibration underestimates the human probability of IoU below .5 by at least five points in a prespecified group.
- **Prior work:** SAM, Stable-SAM, PointPrompt; CPC-SAM preprint additionally treats prompt-related confounding (https://arxiv.org/abs/2505.06524).
- **Gap:** Human–automated gaps are established. The narrower prospective question is transfer of **ranking and tail-risk calibration**, controlling object, point count, history and annotator identity.
- **Contribution:** Annotator-held-out paired evaluation and a validated prompt simulator only if it improves out-of-domain predictive validity.
- **Potential novelty:** B, possibly a limited A finding; merely measuring a human gap is defeated.
- **Datasets:** PointPrompt primary; DIS/ThinObject-5K/COIFT/HR-SOD for synthetic controls; add a second legally usable human-prompt dataset if available. Availability of annotator identifiers/histories must be checked before commitment.
- **Baselines:** SAM, HQ-SAM, Stable-SAM, SAM2/SAM3 visual prompting; uniform interior, distance-transform center, boundary-biased, error-driven iterative sampling; original confidence and calibrated confidence.
- **Metrics:** mIoU, boundary IoU, probability IoU<.5, number of clicks to threshold, risk–coverage, Kendall model-rank correlation; image/annotator-cluster uncertainty.
- **Experiments:** Fixed images, equal number of prompts; evaluate real and simulated distributions; compare one-shot and interactive prefixes; hold out annotators and domains; separate literal prompt replay from feedback-dependent simulation.
- **Ablations:** Count, signed distance to boundary, interpoint distance, points versus boxes, negative points, uncertainty-based mask selection, history truncation. Three simulator/calibration seeds; no fictitious model-training seeds for deterministic inference.
- **Difficulty:** Medium; data parsing moderate, history alignment and causal claims difficult.
- **Compute:** Pilot 10–30 GPU-hours, full 100–250 GPU-hours on 24–48GB; 50–150GB storage, depending on embedding caching.
- **Scientific risk:** Human dataset too small or narrow; ranking differences are estimator noise; original PointPrompt study already includes closely equivalent analyses.
- **Interpretable-result probability:** Estimated .80, subjective.
- **Decision:** Demote pending full PointPrompt appendix/code audit; this is not the first human-prompt comparison.

### S3. When semantic segmentation metrics reward loss of specificity

- **Problem:** Metrics giving partial credit to related category names may increase when a predictor emits broader, less informative concepts.
- **Research question:** Which semantic evaluation rules satisfy explicit monotonicity under controlled information loss, and does violating it change empirical model rankings?
- **Hypothesis:** At least one published semantic metric gives a statistically positive score change after prespecified prediction-only taxonomy coarsening while exact class information decreases, and the effect changes at least one model-pair ranking across two taxonomies.
- **Prior work:** SCAN SG-IoU, RevisitOVS mask-wise evaluation, Rethinking Evaluation Metrics, SHiNe hierarchy classifiers (https://arxiv.org/abs/2405.10053), Auto-Vocabulary Segmentation (ICCV 2025).
- **Gap:** Metric subjectivity, semantic similarity and human validation are prior art. Candidate contribution is falsification via prediction-preserving geometry and deliberate semantic information removal, not another arbitrary similarity formula.
- **Contribution:** Explicit task-conditioned axioms, counterexamples, and empirical stress tests; report separate localization, semantic compatibility and specificity rather than assuming a universal scalar score.
- **Potential novelty:** B/A finding conditional on full metric-paper audit. Generic semantic evaluation is defeated.
- **Datasets:** ADE20K, Pascal Context, LVIS taxonomy; human-written category relations fixed before seeing model scores. Use only validated hierarchy relationships, because WordNet senses may differ from visual labels.
- **Baselines:** mIoU/PQ, SG-IoU, Open mIoU/Open PQ, RevisitOVS; fixed FC-CLIP/CAT-Seg/SAM3 outputs; exact synonym canonicalization and independently curated relation sets.
- **Metrics:** Each original score, exact semantic information measures, model rank, localization unchanged checks; agreement with a small held-out judgment dataset only if legally available.
- **Experiments:** Rename-only aliases, parent substitution, constant generic class, duplicate predictions, mask split/merge controls; keep geometry fixed for semantic tests; test class-frequency and hierarchy-depth changes; disclose when the metric is behaving correctly for a deliberately coarser task.
- **Ablations:** Ontology versus text-encoder similarity, thresholds, label priors, category granularity, thing/stuff, evaluator/model encoder sharing; paired image bootstrap, not pixelwise IID tests.
- **Difficulty:** Medium. Correct reproduction of three metric families is more important than architectural engineering.
- **Compute:** 20–60 GPU-hours to create several frozen prediction sets; 50–120 total with replicates/second dataset; subsequent metric sweeps mainly CPU; 50–150GB cloud storage.
- **Scientific risk:** “Information loss” is not harmful when the user requested coarse semantics; every score embodies a utility choice. Prior appendices may already cover attacks or granularity tradeoffs. A theorem about an ill-posed universal metric alone is insufficient CV evidence.
- **Interpretable-result probability:** Estimated .90, subjective; publication novelty only moderate.
- **Decision:** Demote; strengthen only with an explicit application utility and real ranking changes, not invented universal desiderata.

## Decision matrix

Scores are review judgments from 1 (low) to 10 (high), not measured quantities. They include the novelty penalties above. Their purpose is comparison with other agents' candidates, not automatic selection.

| Candidate | Novelty | Importance | Hypothesis | Feasibility | Experimental clarity | Reproducibility | Dataset quality | Paper potential | Compute efficiency |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| S1 Risk transfer under vocabulary interventions | 6 | 8 | 8 | 8 | 9 | 9 | 8 | 7 | 8 |
| S2 Human-prompt ranking/tail-risk transfer | 5 | 8 | 8 | 7 | 8 | 8 | 7 | 6 | 8 |
| S3 Semantic metric information-loss stress test | 5 | 7 | 8 | 8 | 9 | 9 | 8 | 6 | 9 |

## Adversarial novelty assessment of strongest local candidate S1

**Starting assumption:** Not novel. Search expansion, query-vocabulary size, redundant categories, ambiguity, distractors, class-set changes, open-vocabulary confidence, conformal prediction, selective prediction, and risk control.

**Claim removed 1: “Vocabulary expansion causes OVS degradation.”** RevisitOVS directly investigates this. FreeCP explicitly treats class redundancy and ambiguity. This is established, not a discovery.

**Claim removed 2: “Synonym inconsistency is new.”** SCAN, Global Knowledge Calibration (ICCV 2023, https://arxiv.org/abs/2303.09181) and SynCLIP already motivate semantic duplication/text diversification/grounding consistency. Do not introduce a synonym-consistency loss as an original mechanism.

**Claim removed 3: “Filter classes or align source/target vocabularies.”** FreeCP, CaR (found through FreeCP backward references), and VocAlign are close. Their full implementations must be reproduced if filtering/adaptation becomes the method.

**Claim removed 4: “Pipeline oracle decomposition is new.”** What Holds Back OVS already decouples region recognition, mask quality and inference losses. A new experiment needs paired interventions and stage-level estimands, not only GT-mask/GT-label upper bounds.

**Claim removed 5: “Conformalizing a CLIP model is new.”** Conf-OT and standard LAC/APS/RAPS are direct prior art. Invariance of a raw independent-class score to appended unrelated labels is elementary; no research novelty is claimed for that identity.

**Narrow surviving question:** Does a fixed confidence-based deployment rule change accepted-mask risk under controlled vocabulary changes, after separating elementary score normalization from genuinely set-dependent representations and postprocessing? Can a source-only calibrated intervention preserve a specified useful coverage level on unseen query-set generation rules? No exact equivalent was found in the literature searched so far. This is provisional, category B with potential A finding, not novelty clearance.

**Kill criteria:** Reject this project if (a) remaining result is completely captured by softmax algebra plus existing temperature calibration; (b) no architecture shows risk changes beyond matched random variation; (c) a full audit of RevisitOVS/FreeCP/Conf-OT reveals the same protocol; or (d) legal data do not establish absent-label ground truth. Do not rescue it by swapping backbones or adding modules.

**Forward/backward search:** Followed FreeCP references to CaR and image-level class pruning, CAT-Seg references to FC-CLIP, newer SynCLIP citations to CLIPSelf/SHiNe-related ideas, and 2025/2026 searches around SCAN/RevisitOVS. Search-based forward discovery is incomplete, not a citation-graph export. PointPrompt/CPC-SAM and semantic-metric appendices remain priority audits if S2/S3 are shortlisted.

## Dated query log

All queries below ran on 2026-09-08 using the web search tool. Search results from aggregators were only leads; retained factual claims use linked author/proceedings/arXiv sources. Failed direct CVF fetches returned 403, but primary indexed PDF excerpts and arXiv alternatives were available. OpenReview sometimes returned a browser challenge. No paid paper access was used.

| Batch | Queries (exact or faithfully abbreviated) | Useful outcome |
|---|---|---|
| Q01 | site:openaccess.thecvf.com open vocabulary segmentation label names vocabulary sensitivity 2025 2024; site:arxiv.org open vocabulary segmentation vocabulary invariance label set sensitivity; site:openaccess.thecvf.com Segment Anything robustness prompt sensitivity benchmark 2024 2025 | What Holds Back OVS, Stable-SAM, prompt evaluation |
| Q02 | site:arxiv.org "vocabulary" "sensitivity" "segmentation"; site:openaccess.thecvf.com "label" "synonyms" "open-vocabulary"; site:arxiv.org "SAM 3" "Segment Anything with Concepts"; site:arxiv.org "open-vocabulary" "distractor" | SynCLIP, SCAN, SAM3, vocabulary-free methods |
| Q03 | site:arxiv.org open vocabulary detection "vocabulary size" sensitivity; site:openaccess.thecvf.com open vocabulary "negative classes" sensitivity; site:arxiv.org "open-vocabulary" "label space" "robustness" | Enhanced negatives, OmniLabel, Detic |
| Q04 | "open-vocabulary" "class names" "robustness" benchmark; "open-vocabulary" "vocabulary" "interference"; "open-vocabulary" "label set" evaluation; "open-vocabulary" "distractors" detection | FreeCP; a 2026 detector-confidence/occlusion preprint, not adopted |
| Q05 | Exact titles SynCLIP, Training-Free Class Purification, Semantic-Assisted Calibration, SHiNe | Verified authors and official implementations |
| Q06 | "open vocabulary" segmentation conformal prediction calibration vocabulary; "open-vocabulary" "calibration" "vocabulary" robustness; "conformal" "label space" "CLIP"; "open-vocabulary" "selective" segmentation | RevisitOVS, DAC, Conf-OT; strongest novelty defeats |
| Q07 | Exact RevisitOVS; Benchmarking Human and Automated Prompting arxiv; "SAM" "prompt" "calibration" segmentation uncertainty; "segmentation" "risk" "prompt shift" | PointPrompt, CPC-SAM, additional uncertainty precedents |
| Q08 | Exact Conf-OT, FC-CLIP, CAT-Seg, Segment Anything | Baseline records and primary tables |
| Q09 | Exact Convolutions Die Hard, CLIP, Scaling OVD, Grounding DINO | Correct FC-CLIP identifier; excluded erroneous third-party arXiv ID |
| Q10 | "conformal prediction" "expanding" "classes"; "conformal prediction" "vocabulary shift"; "open-vocabulary" "selective prediction"; "open-vocabulary" "risk control" | No exact S1 match; negative search evidence is weak |
| Q11 | Exact What Holds Back OVS; "Lost in Translation" "VocAlign"; "Rethinking Evaluation Metrics of Open-Vocabulary Segmentation" | Metric prior; conflicting metadata handled conservatively |
| Q12 | Official NeurIPS/ICML/CVF exact-title venue searches | Verified foundational venues |

## Remaining uncertainties

Full code/checkpoint/data-license audits are still required for any chosen segmentation project. Several records are abstract-depth; no claim that all papers were read end-to-end is justified. The scan reaches July/August 2026 preprints but does not establish complete 2026 coverage. Query-set absence under partial annotations and human-prompt annotator independence are substantive dataset concerns, not routine details. Candidate estimates should be re-profiled on exact checkpoints before requesting GPU spending.


## Robustness candidate profiles

## Candidate R1 — When synthetic validation selects the wrong robust model

- **Problem:** Synthetic minority examples can supply both training and validation data; generator-specific bias can then affect model selection even if evaluation images differ.
- **Research question:** At equal group coverage, does sharing a generator between adaptation and model selection systematically mis-rank candidates on real worst-group accuracy?
- **Hypothesis:** Selection using same-generator synthetic validation has larger real-data selection regret than equally sized cross-generator or small real-group validation. Prediction: median paired regret difference exceeds 2 percentage points on two datasets, with a 95% image/seed-resampling interval above zero; otherwise hypothesis unsupported. Threshold is a preregistration choice, not a result.
- **Prior work:** P03, P11, P12, P15, P18; provenance-gradient guidance and synthetic curation leads.
- **Gap:** General source shortcuts and joint nuisance/source balancing are already studied. Narrow remaining question is dependence between generator used for training and generator used for *model selection*, with real endpoint withheld until protocol freeze.
- **Proposed contribution:** A crossed training-generator × validation-generator experiment, rank-correlation/regret estimates, and a real-data budget curve identifying when synthetic selection is trustworthy. No new augmentation architecture required.
- **Potential novelty:** B at best, 5/10 pending deeper work on synthetic validation/domain generalization model selection. Generic initial artifact-balancing proposal is rejected.
- **Datasets:** Waterbirds for controlled foreground/background; SpuCo Animals for natural-domain transfer; optional MetaShift after split/license audit. Use public development/train portions and locked real test sets; no test data drives generation/filtering.
- **Baselines:** ERM, group-balanced sampling, DFR with real calibration, source-aware DFR/GroupDRO, FFR, ASPIRE; SAGE when code/complete recipe becomes available. Information-matched comparisons plus clearly labeled oracle references.
- **Metrics:** Real worst-group and balanced accuracy; selection regret against best candidate within a fixed family; Spearman rank correlation; synthetic-real gap; group/source detection AUROC as a diagnostic, not causal proof.
- **Experiments:** Two generators, two datasets, three model-training families, 3–5 seeds, independent validation samples, equal synthetic counts; one held-out generator; real validation sample-size curve. Select hyperparameters only on development splits, reserve real test for final matrix.
- **Ablations:** Shared versus different generator weights, prompt families, semantic filtering, source-aware groups, generation seed, image count, one-stage versus FFR; distinguish semantic failures from source dependence by blinded audit sample.
- **Difficulty/compute:** Medium-high; generation and image training dominate. Planning estimate: 50–150 A100-class GPU-hours pilot, 200–800 full, 150–400 GB cloud storage. These are unmeasured ranges and require throughput calibration before paid approval.
- **Scientific risk:** Newest SAGE may already test the exact issue; generator transfer can measure quality mismatch rather than dependence; natural groups small. Negative findings remain useful only if confidence intervals bound practically relevant regret.
- **Probability of interpretable result:** Subjective 0.80 conditional on independent generators and reliable real groups.

## Candidate R2 — Does compositional fine-tuning amplify cross-modal brittleness?

- **Problem:** Better clean caption discrimination can coexist with hard-positive failure. Deployment additionally degrades visual evidence, potentially exposing dependence between visual uncertainty and lexical fragility.
- **Research question:** After matching clean and single-modality difficulty, does hard-negative fine-tuning increase the *interaction* between meaning-preserving paraphrases and visual corruption relative to ordinary or concept-centric fine-tuning?
- **Hypothesis:** Hard-negative fine-tuning yields a larger deterioration in the image × paraphrase interaction in positive/negative cosine margin than matched ordinary fine-tuning, concentrated on attribute/relation bindings; balanced hard-positive training attenuates it. Primary operational threshold: at least 0.25 pooled clean-margin SD interaction difference, replicated on two datasets and two backbone families with paired CI excluding zero. A null or sign reversal falsifies the proposed amplification mechanism.
- **Prior work:** P02, P04–P06, P08–P10, P16–P17, P19. Four-axis scaling and joint-shift benchmarks make a generic corruption benchmark insufficient.
- **Gap:** Inspected work establishes language brittleness or broad multimodal robustness; no equivalent difficulty-controlled four-condition interaction study after composition-specific training found so far. Search completeness remains uncertain.
- **Contribution:** Factorial mechanism audit, mathematical margin decomposition, matched retraining, and test of whether hard-positive supervision changes visual-language coupling. The investigation itself is worthwhile without a new loss.
- **Potential novelty:** A for a replicated finding; B if focused on mitigation. Caution: an expected degradation under two shifts is insufficient. Primary contribution needs interaction attribution and useful predictions.
- **Datasets:** SugarCrepe++ triplets (COCO), released hard-positive evaluation/training data, Winoground locked confirmatory analysis; separate COCO training data with official held-out image IDs. Identity-group all captions and transformed images for splits/uncertainty. Do not develop on Winoground.
- **Baselines:** Frozen OpenCLIP/CLIP, ordinary image-text fine-tuning on identical data, NegCLIP-style hard negatives, matched positives+negatives (P10), C2LIP with its matched SigLIP CC3M baseline; CoN-CLIP optional. Existing checkpoints are exploratory, not sufficient for causal training claims.
- **Metrics:** Original and hard-positive accuracy, joint correctness, brittleness; margin interaction D = m(corrupted,paraphrase) − m(clean,paraphrase) − m(corrupted,original) + m(clean,original); paired seed/model contrasts; retrieval and zero-shot transfer; clean-score-normalized and raw results.
- **Experiments:** 2×2 within-image factorial for original/paraphrase and clean/corrupted, corruption severities fixed using disjoint validation data; 3–5 training seeds; two encoder families; significance by source-image clustered bootstrap and seed summaries. Avoid conditioning solely on each model's successful images; report common fixed evaluation set plus explicit stratified sensitivity analysis.
- **Ablations:** Visual-only/text-only/both encoder training; hard-negative ratio; hard positives; matched clean-margin quantiles; blur/noise/JPEG/brightness, relation versus object versus attributes, text-only tests; keep semantic visual evidence intact at moderate severity with blinded validity audit.
- **Difficulty/compute:** Medium; evaluation infrastructure easy but fair matched retraining important. Estimate 20–60 A100-class hours pilot, 150–500 full depending training pool, 80–200 GB cloud disk. C2LIP full paper uses eight A40 GPUs; do not call a tiny local version a faithful reproduction.
- **Scientific risk:** Interaction in raw accuracy may reflect saturation rather than model mechanism. Raw margin decomposition is geometry, not proof of internal causal representation. Corruption might hide the target relation, making negative changes appropriate. Address via human validity audit and equal marginal difficulty controls.
- **Probability of interpretable result:** Subjective 0.90 for whether excess interaction exists; 0.65 for an explanatory mechanism beyond generic margin geometry.

## Candidate R3 — When nuisance concepts become targets: transfer limits of VLM debiasing

- **Problem:** A concept can be a nuisance in one task and necessary evidence in another. Robustification can improve one task while changing the foundation model's retained semantic capability.
- **Research question:** Does task-aware spurious-feature suppression remove recoverable information needed for role-reversed queries, and can training-based corrections preserve it as well as inference-only task-conditioned baselines?
- **Hypothesis:** Corrections that alter shared encoder weights reduce role-reversed concept accuracy more than task-conditioned inference corrections at matched original-task worst-group improvement. A difference under 2 points with narrow CI, or preserved linear recoverability without query loss, weakens the proposed information-loss account.
- **Prior work:** P07, P13, P14, DFR and concept projection. RoboShot already uses task descriptions; region-aware correction already exists.
- **Gap/contribution:** Paired same-image concept-role reversal and distinguish score misalignment from loss of recoverable representation. Not a claim that task conditioning is new. Establish where a robustness intervention should be task-local.
- **Potential novelty:** A/B, moderate uncertainty. Adjacent concept-erasure, selective forgetting, and utility-preserving debiasing literature must be searched before selection.
- **Datasets:** Waterbirds foreground class versus background class as controlled case; COCO annotated object/attribute/scene subsets with query roles swapped; non-sensitive natural-image attributes preferred over facial protected-attribute prediction. Additional labels must be curated only on development material.
- **Baselines:** Frozen CLIP, DFR/linear probe, task-conditioned RoboShot, P07 multimodal fine-tuning, RaVL where recipe is available; simple per-task prompt ensembles; shared versus isolated adapters. Preserve each method's required supervision transparently.
- **Metrics:** Original worst-group accuracy, role-reversed accuracy, retrieval, feature-probe recovery, task-pair Pareto curves; representation CKA secondary only.
- **Experiments:** Fixed image splits, alternate queries on identical images, matched target robustness gain, 3–5 seeds, two encoders, frozen-encoder probe retraining with equal labels; confirm on natural images after controlled Waterbirds result.
- **Ablations:** Encoder versus head versus adapter, correction strength, prompt-specific correction, region/global correction, alternate nuisance directions, probe capacity/label budget.
- **Difficulty/compute:** Medium-high from valid task-pair construction. Estimate 30–80 A100-class hours pilot, 100–300 full; 100 GB cloud storage. Rates unmeasured.
- **Scientific risk:** If researchers reasonably maintain per-task models, role-reversal does not challenge their stated scope. Need demonstrate a practical shared-model tradeoff and avoid straw-man baselines. Probe failure cannot alone prove information destruction.
- **Probability of interpretable result:** Subjective 0.75.

## Decision matrix within this scan

All scores are subjective 1–10; compute efficiency 10 means efficient. They are hypotheses about project value, not measured probabilities. Do not combine by raw sum without checking scientific priority.

| Candidate | Novelty | Importance | Hypothesis | Feasibility | Experimental clarity | Reproducibility | Dataset quality | Paper quality | Compute efficiency |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R1 Synthetic validation dependence (revised) | 5 | 8 | 8 | 7 | 8 | 8 | 8 | 7 | 6 |
| R2 Composition-specific cross-modal interaction | 7 | 8 | 9 | 8 | 9 | 9 | 8 | 8 | 8 |
| R3 Concept-role reversal after debiasing | 6 | 8 | 8 | 7 | 8 | 8 | 7 | 7 | 8 |

## Adversarial novelty conclusion for the strongest surviving local candidate (R2)

Assume R2 is already known. P10 already demonstrates hard-negative-induced lexical oversensitivity, even transferring between perturbation types. P09 already tests hard-positive lexical changes. P08 already benchmarks image/text corruption after adaptation. The CVPRW scaling study already relates compositionality and corruption capability across many VLMs. P19 already evaluates joint image/text shifts. P17 already claims composition improvements without sacrificing basic zero-shot capability. Therefore none of those claims can be our contribution.

The remaining narrowly testable question is a **paired, difficulty-controlled interaction change caused by composition-specific training**, with a mechanistic link to the margin geometry. For normalized embedding scores, a same-candidate margin difference-in-differences can be written as an inner product between the change in image embedding and the change in positive-minus-negative text direction. That algebraic identity is elementary and **not itself novel**. A contribution would require evidence that a training objective systematically changes alignment of those perturbation directions beyond marginal shift magnitude, predicts which relations fail, and that a matched intervention changes that relationship on untouched data.

Classification: **A (potential finding) or B (controlled combination of existing evaluation/intervention ideas)**. No equivalent exact experiment was found in the searches above; this is not proof of novelty. Before promoting R2 to the final shortlist, inspect full P08/P19 protocols and recent 2025–2026 composition papers including semantic guidance, TripletCLIP, CLIC, and C2LIP. Strongest rejection case: the observed interaction is fully explained by lower clean margins and independent modality error; in that event publish no broad compositional robustness claim, and report the negative result or abandon.

No final overall project is selected in this file. No paid resource has been used.
