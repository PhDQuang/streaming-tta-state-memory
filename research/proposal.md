# Title

**What Does Adaptation Remember? Controlled History and State Interventions in Streaming Vision**

Selected 2026-09-08 after nine candidates and adversarial examination of T1, R2, and S1. Status: protocol and Stage A implementation; large-scale hypotheses untested. This is a scientific investigation, not a proposed accuracy-improving module.

# Problem Statement

An adapting image classifier's prediction depends on incoming images and accumulated state. Comparing average accuracy over different streams mixes history effects with different evaluated examples. Even resetting model weights may leave optimizer or auxiliary state active. We need to distinguish persistent functional history from immediate recency, changed batch membership, random variation, and incomplete resets.

# Motivation

Streaming adaptation is intended for deployment under change. Prior work already studies collapse, temporal correlation, memory and selective resets. A stronger empirical question is what earlier experience still changes on an *identical unseen future*, and which explicit state interventions change that effect. Both persistence and practical washout would be informative.

# Research Question

When two histories contain identical preformed image batches in different orders, do their predictions remain meaningfully different after identical recent observations? How do parameter, optimizer and auxiliary-state interventions change that difference, and what are its accuracy/calibration consequences?

# Hypothesis

H1 (persistence): at the prespecified W=16-batch common recent tail, mean shared-suffix prediction disagreement exceeds 1 percentage point for **SAR complete / ResNet-50, no external reset**, averaged equally across the three frozen domain-pair scenarios. A full-stage positive claim requires a 95% panel-level interval whose lower bound exceeds 1 point and replication with a second architecture and dataset. A sufficiently precise upper bound below 1 point supports practical washout in the evaluated setting. An imprecise null is inconclusive.

H2 (state sensitivity, conditional on H1): the primary optimizer contrast is **parameters+aux reset versus parameters+optimizer+aux reset**, keeping forward parameters and SAR EMA source-clamped in both arms. The secondary auxiliary contrast is **none versus aux reset**. Define reduction as D(first arm) minus D(second arm), forming scenario averages within independent panels first. Report both contrasts regardless of outcome. For confirmation, use two-sided 97.5% Student-t intervals for each panel-mean contrast (Bonferroni nominal familywise coverage 95% across these two contrasts under the stated approximation; critical value t[0.9875, n−1]). An H2 practical-positive claim for a contrast requires its simultaneous **lower bound to exceed 0.5 percentage point**, not merely its point estimate. Independent panels and an adequate approximation for panel means are assumptions; diagnose them, report individual panels, and treat inadequate precision/model fit as inconclusive. Whole-panel bootstrap is a sensitivity analysis when enough panels exist. Parameters × optimizer × auxiliary interactions are secondary diagnostics. Reduction of disagreement by making both trajectories inaccurate does not establish improved robustness. This is an intervention-specific effect, not unique causal mediation.

Consequences are separate: report oriented signed error difference (AB minus BA), its absolute magnitude, NLL/Brier and excess error versus the source. A difference in predictions does not imply harmfulness. Practical consequence reference thresholds are 1 accuracy point and 0.02 NLL nats/example; these are design choices, not observed effects.

# Related Work

Core precedents: Tent; SAR; RoTTA; RDumb; UniTTA; PeTTA; POEM; ASR; OATTA; TTABC; GoTTA; AttenDence v1/LookSharp; recent teacher-plasticity work. See `literature_review.md`, version-aware `references.bib`, and `novelty_analysis.md`. No first claim is made for order sensitivity, optimizer memory, resetting, disjoint corrupted views, recovery delay or controlled TTA benchmarking.

# Research Gap

The searched literature does not establish the full combination of matched batch multisets, identical recent tail, disjoint common suffix and complete-state factorial intervention used here. This bounded search supports investigating the question; it does not certify novelty. The contribution must exceed the predictable fact that gradient updates need not commute.

# Proposed Contribution

1. A precisely defined paired history estimand and reproducible stream generator.
2. A complete-state replay/reset contract and negative controls that separate implementation failures from history effects.
3. An empirically validated map of persistence, practical consequences and intervention responses, or a well-bounded negative result.
4. Public configurations, raw predictions, manifests, provenance, analysis and skeptical review.

# Proposed Method

Write an algorithm's state as S=(P,B,O,A,R): parameters P, forward buffers/modes B, optimizer O (including nested momentum), auxiliary state A (SAR entropy EMA), and random state R. Fixed source anchors are immutable. A batch update U_x emits its first unperturbed forward prediction, then updates from unlabeled x.

Construct two disjoint domain blocks H_A and H_B from different base images. The histories H_AB=H_A followed by H_B and H_BA=H_B followed by H_A contain **exactly the same preformed batches**. Neither batch membership nor corruption realization changes. Append W and then Q, with original image IDs disjoint between H, W and Q. No original image repeats inside a panel. For W lengths 0/4/16, use the final k batches of one 16-batch tail so the most recent content is matched across k.

Intervene **after H+W, immediately before Q**. Run the full P/O/A source-reset factorial: none, P, O, P+O, A, P+A, O+A, P+O+A. Add all-state reset including buffers/modes and common RNG. All-state reset must match a fresh instance of the same adapter on Q, not necessarily a frozen source-eval model. Factorial states are diagnostic hybrids, not proposed deployment policies.

For panel j, D_j = mean_Q 1[argmax f_AB != argmax f_BA]. Signed error contrast is E_AB−E_BA; absolute gap is |E_AB−E_BA|, not mean per-image absolute loss. NLL uses stable log-softmax. Analyze prefix-order effects and reset contrasts separately. The common-tail experiment controls immediate exposure but does not guarantee washout or monotonic decay.

# Why This Method Should Work

Pairing fixes future observations, labels, preprocessing and batch composition, so only declared historical state differs. Deterministic replay controls test whether serialization and branching are correct. Parameter reset implies equal first-Q-batch predictions when all forward state is equal; optimizer memory can first change predictions on Q batch 2 under this timing. This is a checkable implication, not a novelty claim. Perturbing state can reveal interventional sensitivity but cannot prove a unique natural mechanism when hybrid states are unnatural.

# Datasets

- Stage A: only official **UCI optdigits.tra**, CC BY 4.0; internal source/development/history/tail/suffix partitions. These toy results test software, not generalization. Official test file excluded.
- Stage B: released ImageNet-C JPEGs, severity 5, gaussian_noise/brightness/defocus_blur. Deterministic original-ID hashing selects pilot pool (<20% bucket), reserving the other 80% image contents and evaluation outcomes for confirmation; filename/class-folder inventories may be inspected. Source rights and checksums documented in `datasets/README.md`.
- Stage C/D: reserved ImageNet-C identities, prespecified additional severities/corruptions and a second public benchmark (CIFAR-100-C plus a natural-domain replication such as DomainNet-126 when access/splits are audited). Do not call synthetic corruption order natural chronology.

# Evaluation Metrics

Primary: panel-averaged suffix disagreement at W=16. Consequences: accuracy/error, oriented and absolute error gaps, NLL, multiclass Brier, and source-relative cumulative error. Secondary: fixed-bin ECE, per-class errors, reset timing and per-batch trajectories. Report update/skip counts, total compute and state inventory. No claim of mCE unless all required corruption/severity and AlexNet normalization terms are actually evaluated.

# Baselines

Implemented initial set: frozen source; current-batch normalization only; Tent; SAR with documented complete-state serialization and guarded empty updates. Ordinary non-recovery steps are compared against pinned official code. The corrected implementation is explicitly `sar_complete`; native reference semantics are audited separately and must be compared on images if corrections affect recovery.

Required before a strong final-paper claim: faithful-versus-corrected SAR comparison, recent ASR and a persistent method (RoTTA/PeTTA or ROID) with state inventory; EATA if source Fisher data can be obtained without test-label leakage. These are staged requirements, not falsely reported as implemented/reproduced. Use ResNet-50 BN and ViT-B/16 LN; Tent on LN is an explicit extension, not an exact original BN reproduction.

# Experimental Protocol

Freeze configs/manifests before image benchmark evaluation. Source checkpoints and transforms are shared across histories and interventions. Source labels train only the tiny source model; no target labels reach adapter APIs. No target-label tuning. ImageNet class-index mapping is verified against a pinned canonical mapping; sampler uses only original IDs.

Stage A: three source-training seeds [17,29,43], identical internal split, fixed 12-epoch schedule, two local domain pairs and W=[0,4]. These seeds measure conditional software/optimization behavior on one image panel, not independent population samples.

Stage B: ResNet-50 IMAGENET1K_V1, batch 32, SGD learning rate 0.00025, momentum .9, SAR rho .05, reliability margin .4 log(1000), reset threshold .2. Three **identity-disjoint** pilot panels, each 1,024 history images + 512 maximum tail + 1,024 suffix = 2,560 unique IDs; 7,680 total. Three prespecified domain pairs reuse each panel as paired conditions. W=[0,4,16], eight factorial arms plus full-reset control. Frozen source/norm are invariance controls. This is deliberately an underpowered engineering/variance pilot; do not make significance claims from three panels.

Stage C/D initial design: 24 disjoint confirmation panels, each 512 history +512 tail+512 suffix =1,536 unique IDs, total 36,864 from reserved 80% (~40k). This jointly respects the 50k base-ID budget. Source/model/manifest availability is validated before launch. Longer histories require a separate clearly labeled conditional-stream sensitivity analysis or additional data. The proposed 24 panels are a capacity-limited initial design, not a power guarantee. Pilot H/Q sizes (1,024/1,024) differ from confirmation (512/512), changing both the history estimand and outcome variance; its variance cannot be substituted directly into a confirmation sample-size formula. Freeze N=24 if that design is approved and judge precision from its prespecified intervals without optional stopping. A different N requires a separately budgeted, confirmation-sized calibration design and a new freeze before reserved outcomes are opened. Insufficient precision is inconclusive; never inflate seed counts or select a new design after viewing confirmation outcomes.

# Ablation Plan

Full P/O/A factorial; all-state and sham resets; component swaps between history states in Stage D; W length; prefix length; momentum 0/.9; reliable-filter and automatic-recovery event analysis; severity; within-batch reshuffling only as a separately labeled experiment. **Frozen-state versus adapting Q and momentum 0/.9 are mandatory before an optimizer-mechanism claim.** These Stage D extensions are requirements, not currently claimed completed implementations. All arbitrary search is excluded. Additional ablations are frozen before confirmation outcomes.

# Robustness Tests

Different corruption families and severities; return-to-clean Q; BN versus LN backbone; random batch permutations beyond AB/BA; natural domain shifts on a second audited dataset. Test failures and negative intervals remain in raw output. Inspect both beneficial and harmful state interventions.

# Statistical Validation

Unit: independently assembled image panel, with scenario average formed inside panel first. Repeated seeds on identical images are not additional image panels. Report all individual runs, mean, SD and panel-level intervals; use whole-panel bootstrap as sensitivity only when enough panels exist. A bootstrap of saved individual predictions cannot simulate changing an adapting stream. No unjustified exact sign-flip or pixel/image IID significance tests.

Primary family fixed in advance; state contrasts use simultaneous intervals or Holm-adjusted valid tests if assumptions hold. Report bounds relative to practical thresholds; failure to reject zero is not evidence of negligible memory. Approximate paired-mean planning n≈(2.8 sigma/delta)^2 illustrates why three seeds are insufficient; full sample size is a precision decision. See the independent `design_audit.md` and documented resolutions.

# Compute Requirements

Local uses existing CPU PyTorch and under 1 MB of downloaded training data. Stage B needs one 24 GB RTX 4090-class GPU, approximately 8–16 GPU-hours including debugging allowance and repeated suffixes, around120 GB temporary cloud disk. This is an unprofiled planning estimate; throughput and variance measurements are themselves pilot outputs. At the observed $0.74/hour pod rate, compute is $5.92–$11.84; storage and contingency suggest a $20 all-in pilot ceiling. Exact arithmetic, matrix, duration and sources in `cloud_gpu_request.md`. No paid action is authorized yet.

# Risks

Known order/reset phenomena may explain everything; effects could disappear after complete resets; block ordering may exaggerate real deployment; corrected versus original implementation may differ; H1 may be inconclusive at feasible panel counts; archive transport may dominate runtime. Resolve implementation failures before interpreting any effect. Report nulls honestly.

# Expected Contributions

Expected outputs are a validated protocol, auditable findings and a reproducible empirical paper. Expected **performance improvements are unspecified**. A negative result that bounds persistent effects can be useful; a toy success or isolated bug does not satisfy the research objective.

# Limitations

No new adaptation algorithm, universal causal identification, or guarantee of deployment risk improvement. Pretrained-data overlap cannot be fully audited. ImageNet-C shifts are synthetic and the models' source pretraining used ImageNet. Stage A alone has no external-validity claim. A complete manuscript requires Stage C/D evidence and reviewer fixes.

# Reproducibility Plan

Pinned versions and upstream code; complete-state roundtrip tests; immutable source checkpoints, manifests, seeds, per-image predictions and raw CSV/JSON; code/config hashes per experiment; deterministic controls; scripted tables/figures; preserved failures; paper claims linked to result files. README supplies executable local/cloud commands. Paid actions remain gated by explicit user approval, as requested.
