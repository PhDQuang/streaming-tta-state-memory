# Literature scan: adaptation, temporal shift, priors and calibration

Search date: 2026-09-08. Scope: foundational works plus 2023–2026 computer-vision test-time adaptation (TTA), streaming/domain shift, class imbalance and calibration. This is a bounded independent scan, not an exhaustive systematic review. All claims below use primary paper, proceedings, author, or author-repository sources; search-engine snippets from secondary summaries were discovery leads only. Results are author-reported, not reproduced here. A full-text-verified entry means the stated section/table was inspected, not that every proof and implementation was audited.

## Main findings

The broad ideas “realistic streams,” “class imbalance breaks entropy minimization,” “calibration matters,” “long sequences cause collapse,” “resetting helps,” and “memory policies should be controlled” are already well occupied. A competitive project must identify a more precise phenomenon. The strongest candidate in this scan is a controlled study of history dependence with identical prefix sample multisets, an identical unseen suffix, and state-component interventions. Its defensible contribution would be an experimentally identified mechanism and estimand, not the claim that sample order matters.

The 2026 literature materially raises the novelty bar: GoTTA separately benchmarks memory policies, recovery-complexity work formalizes post-shift recovery, and a September 2 preprint isolates teacher plasticity over long streams. These must be included in the eventual adversarial review. No equivalent *matched-multiset prefixes + shared disjoint suffix + component-state intervention* design was located in the primary literature searched here. This is a limited search result, not proof of novelty.

## Evidence ledger

### A01 — Tent: Fully Test-time Adaptation by Entropy Minimization

- Authors/year/venue: Dequan Wang, Evan Shelhamer, Shaoteng Liu, Bruno Olshausen, Trevor Darrell; arXiv 2020; **ICLR 2021 verified from the primary conference PDF** during the same-day reviewer audit.
- Verified sources: https://arxiv.org/abs/2006.10726 ; https://openreview.net/pdf/4de0af9691a5dcc52de7de756676fded33d037ef.pdf
- Evidence: abstract and primary conference PDF opening/title/authors/publication line verified; detailed numerical tables not independently extracted.
- Question/method: Can an already trained classifier adapt without target labels or source data? Update normalization statistics and channel-affine parameters by prediction entropy minimization.
- Datasets/metrics: corrupted ImageNet and CIFAR-10/100; digit transfer; GTA-to-Cityscapes; VisDA-C. Generalization/classification error and segmentation performance; precise segmentation metric not checked in this scan.
- Result: abstract reports improved corruption error in one test-time epoch; no numeric effect copied.
- Limitation/gap (our inference): unsupervised confidence is not a correctness guarantee; adaptation state can carry previous errors forward. Essential baseline for all candidates.

### A02 — Robust Test-Time Adaptation in Dynamic Scenarios (RoTTA)

- Authors/year/venue: Longhui Yuan, Binhui Xie, Shuang Li; CVPR 2023.
- Sources: https://arxiv.org/abs/2303.13899 ; https://openaccess.thecvf.com/content/CVPR2023/papers/Yuan_Robust_Test-Time_Adaptation_in_Dynamic_Scenarios_CVPR_2023_paper.pdf
- Evidence: full-text introduction and protocol inspected.
- Question/method: joint domain change and correlated samples; robust normalization, category-balanced memory using uncertainty/timeliness, teacher–student updates.
- Datasets/metrics: CIFAR-10-C, CIFAR-100-C, DomainNet; average classification error.
- Result: introduction reports error reductions exceeding 5.9, 5.5 and 2.2 percentage points respectively against the best compared baseline in its PTTA setup.
- Limitation/gap (our inference): class balance and memory age are already explicit mechanisms. A new study must separate changed update batches from persistent parameter/teacher state rather than rediscover correlation sensitivity.

### A03 — Towards Stable Test-Time Adaptation in Dynamic Wild World (SAR)

- Authors/year/venue: Shuaicheng Niu, Jiaxiang Wu, Yifan Zhang, Zhiquan Wen, Yaofo Chen, Peilin Zhao, Mingkui Tan; ICLR 2023.
- Primary full paper: https://www.chenyaofo.com/papers/niu-towards-stable-test-time-adaptation-in-dynamic-wild-world.pdf ; OpenReview https://openreview.net/forum?id=g2YraF75Tj returned a browser challenge.
- Evidence: primary paper opening/abstract verified.
- Question/method: instability with mixed shifts, small batches and online class imbalance; remove unreliable samples and apply sharpness-aware entropy minimization; compare normalization choices.
- Datasets/metrics/result: image corruption classification; exact dataset roster and numerical tables not independently extracted here. Abstract reports improved stability and efficiency; no numeric claim retained.
- Limitation/gap (our inference): establishes several failures already. Include batch-agnostic normalization so a new experiment is not merely a BatchNorm singleton failure.

### A04 — Label Shift Adapter for Test-Time Adaptation under Covariate and Label Shifts

- Authors/year/venue: Sunghyun Park, Seunghan Yang, Jaegul Choo, Sungrack Yun; ICCV 2023.
- Sources: https://arxiv.org/abs/2308.08810 ; https://openaccess.thecvf.com/content/ICCV2023/papers/Park_Label_Shift_Adapter_for_Test-Time_Adaptation_under_Covariate_and_Label_ICCV_2023_paper.pdf
- Evidence: full-text evaluation setup and tables inspected.
- Question/method: joint covariate and prior shift; estimate target class distribution and predict a subset of model parameters with an adapter.
- Datasets/metrics: CIFAR-10-C, CIFAR-100-C, ImageNet-C with long-tailed source/target distributions; accuracy over 15 corruptions, forward/uniform/backward label distributions.
- Result: reports improved accuracy when integrated with existing TTA methods; numerical comparisons omitted because the extracted table was incomplete.
- Limitation/gap (our inference): prior estimation can be confounded by changes in class-conditional predictions; merely combining prior correction with TTA is already prior art. Dataset severity differs across CIFAR-C and ImageNet-C in this paper.

### A05 — RDumb: A simple approach that questions our progress in continual test-time adaptation

- Authors/year/venue: Ori Press, Steffen Schneider, Matthias Kümmerer, Matthias Bethge; **NeurIPS 2023 main conference**, verified from the official proceedings PDF and conference poster listing during the same-day reviewer audit.
- Sources: https://arxiv.org/abs/2306.05401 ; https://openreview.net/pdf?id=VfP6VTVsHc ; https://proceedings.neurips.cc/paper_files/paper/2023/file/7d640f377893fc5f22b5610e175ef7c3-Paper-Conference.pdf ; https://nips.cc/virtual/2023/poster/71448
- Evidence: abstract and full-text reset/hyperparameter passages inspected; primary proceedings title/authors/conference line verified.
- Question/method: asymptotic continual TTA performance; Continually Changing Corruptions (CCC) benchmark and periodic source reset.
- Datasets/metrics: CCC and corruption benchmarks; classification performance over long sequences.
- Result: authors report all but one compared method eventually collapse; periodic reset matches or exceeds the compared methods. Reset interval 1,000 steps selected on holdout corruptions in the inspected paper.
- Limitation/gap (our inference): reset policy and long-horizon degradation are established. Reset frequency must not be tuned on evaluated suffix labels.

### A06 — UniTTA: Unified Benchmark and Versatile Framework Towards Realistic Test-Time Adaptation

- Authors/year/venue: Chaoqun Du, Yulin Wang, Jiayi Guo, Yizeng Han, Jie Zhou, Gao Huang; arXiv 2024, venue unverified.
- Sources: https://arxiv.org/abs/2407.20080 ; https://arxiv.org/html/2407.20080v1
- Evidence: full-text benchmark construction, section 5.1 and Table 4 inspected.
- Question/method: unify class/domain imbalance and temporal correlation using Markov transition sampling; Balanced Domain Normalization and correlated feature adaptation.
- Datasets/metrics: CIFAR-10-C, CIFAR-100-C, ImageNet-C; mean error.
- Result: defines 36 possible scenarios, evaluates 24 after excluding continual-by-class cases, displays 12 main settings. ImageNet-C Table 4 averages: UniTTA 69.71%, LAME 75.12%, source 81.70% error in that setup.
- Limitation/gap (our inference): sampling-factor coverage is already broad. Different orders and marginal streams are not a controlled estimate of residual history effect on a shared suffix. Do not misstate 36 as the number actually evaluated.

### A07 — Protected Test-Time Adaptation via Online Entropy Matching: A Betting Approach (POEM)

- Authors/year/venue: Yarin Bar, Shalev Shaer, Yaniv Romano; NeurIPS 2024. DOI 10.52202/079017-2714.
- Sources: https://proceedings.neurips.cc/paper_files/paper/2024/hash/9b35a0a20d617dc68ae98a7a57df2f51-Abstract-Conference.html ; https://openreview.net/pdf?id=qamfjyhPeg
- Evidence: abstract and full-text experiment protocol inspected.
- Question/method: detect entropy-distribution shift using betting and adapt by source-entropy matching rather than unconditional confidence sharpening.
- Datasets/metrics: ImageNet/ImageNet-C, CIFAR10/100-C, Office-Home; classification accuracy and calibration.
- Result: reports improved shifted accuracy and preserved unshifted calibration; numeric values not copied. Importantly, its corruption protocol explicitly takes only one corrupted version per base image.
- Limitation/gap (our inference): excludes a novelty claim based solely on eliminating repeated corrupted views; entropy distribution can also change with class mixture. Guarantees for drift detection are not guarantees of target classification improvement.

### A08 — Persistent Test-time Adaptation in Recurring Testing Scenarios (PeTTA)

- Authors/year/venue: Trung-Hieu Hoang, Duc Minh Vo, Minh N. Do; arXiv 2023; NeurIPS 2024.
- Sources: https://arxiv.org/abs/2311.18193 ; https://papers.nips.cc/paper/2024/file/df29d63af05cb91d705cf06ba5945b9d-Paper-Conference.pdf ; https://openreview.net/pdf?id=ffeUBoTcdS
- Evidence: abstract and full-text reset-frequency protocol inspected.
- Question/method: diagnose recurring-domain error accumulation; perturbed Gaussian-mixture analysis, divergence sensing, source anchoring and adaptive update strength.
- Datasets/metrics: CIFAR10/100-C, ImageNet-C, DomainNet; average classification error and long-horizon trajectory.
- Result: reports improved stability; its reset comparisons explicitly include model, optimizer and memory state and multiple reset periods.
- Limitation/gap (our inference): recurrent environments and resetting all state are not new. Matched-prefix state decomposition must ask more than whether recovery is possible on revisited domains.

### A09 — Temporal Test-Time Adaptation with State-Space Models (STAD)

- Authors/year/venue: Mona Schirmer, Dan Zhang, Eric Nalisnick; arXiv 2024; TMLR 2025 verified by author institution record.
- Sources: https://arxiv.org/html/2407.12492v2 ; https://www.dare.uva.nl/id/5f96c58d-deaa-4fb3-a17b-1a9118e3a8dd ; final record https://openreview.net/forum?id=HFETOmUtrV (browser challenge).
- Evidence: preprint full-text sections 2–3, 5 and appendix configuration portions inspected; final revision not compared.
- Question/method: gradual temporal drift; infer time-varying class prototypes using state-space models.
- Datasets/metrics: Yearbook, EVIS, FMoW-Time, CIFAR-10.1, ImageNetV2, CIFAR-10-C; accuracy, small-batch sensitivity, runtime.
- Result: reports successful adaptation on temporal shifts, especially class-correlated settings; numeric effects omitted to avoid conflating versions.
- Limitation/gap (our inference): prototype tracking and prior modeling already exist. Inspected version performs extensive hyperparameter searches and reports best configurations; a project must specify label-free deployment selection. Use EVIS/FMoW for non-demographic real temporal evaluation.

### A10 — COME: Test-time Adaption by Conservatively Minimizing Entropy

- Authors/year/venue: Qingyang Zhang, Yatao Bian, Xinke Kong, Peilin Zhao, Changqing Zhang; ICLR 2025; preprint 2024.
- Sources: https://arxiv.org/abs/2410.10894 ; https://iclr.cc/virtual/2025/poster/30977 ; https://github.com/BlueWhaleLab/COME
- Evidence: abstract, official venue listing and repository inspected.
- Question/method: overconfidence in entropy minimization; Dirichlet opinion uncertainty induces conservative entropy optimization.
- Datasets/metrics: official implementation documents ImageNet-C and open-world OOD datasets including iNaturalist and NINCO; accuracy and false-positive rate.
- Result: abstract reports improvements in standard, lifelong and open-world TTA. No numeric superlative retained without its full comparison context.
- Limitation/gap (our inference): adding uncertainty-aware entropy is occupied; discriminative ranking, class-prior mixture and calibration need separate tests.

### A11 — The Illusion of Progress? A Critical Look at Test-Time Adaptation for Vision-Language Models

- Authors/year/venue: Lijun Sheng, Jian Liang, Ran He, Zilei Wang, Tieniu Tan; NeurIPS 2025 Datasets and Benchmarks.
- Sources: https://arxiv.org/abs/2506.24000 ; https://papers.nips.cc/paper_files/paper/2025/file/b57ddd8726c217a6fef9a48ce3e09ffd-Paper-Datasets_and_Benchmarks_Track.pdf
- Evidence: abstract and full-paper title/venue verified; detailed numerical tables not extracted.
- Question/method: unified TTA-VLM benchmark; 8 episodic and 7 online methods, 15 datasets, CLIP and SigLIP, interaction with training-time tuning.
- Metrics/result: accuracy, robustness, calibration, OOD detection and stability; reports limited gains and accuracy/trustworthiness tradeoffs.
- Datasets: 15-dataset count verified, complete roster not extracted in this scan.
- Limitation/gap (our inference): generic multi-metric benchmarking is already prior art. Conditional calibration/carryover experiments require a more precise causal intervention.

### A12 — Label Shift Meets Online Learning: Ensuring Consistent Adaptation with Universal Dynamic Regret

- Authors/year/venue: Yucong Dai, Shilin Gu, Ruidong Fan, Chao Xu, Chenping Hou; CVPR 2025, pages 15392–15401.
- Source: https://openaccess.thecvf.com/content/CVPR2025/html/Dai_Label_Shift_Meets_Online_Learning_Ensuring_Consistent_Adaptation_with_Universal_CVPR_2025_paper.html
- Evidence: proceedings metadata and abstract verified.
- Question/method: inconsistent online class-prior estimation; convex risk estimator, optimistic online learner and ensemble classifier refinement.
- Datasets/metrics: real-world datasets and human-motion task mentioned; exact names and numeric metrics not extracted.
- Result: authors state minimax-optimal universal dynamic regret and empirical superiority; theorem assumptions and numerical tables not independently audited.
- Limitation/gap (our inference): online label-prior adaptation with regret is established. Joint class-conditional shift needs explicit stress testing rather than borrowing pure-label-shift guarantees.

### A13 — GoTTA be Diverse: Rethinking Memory Policies for Test-Time Adaptation

- Authors/year/venue: Shyma Alhuwaider, Yasmeen Alsaedy, Merey Ramazanova, Silvio Giancola, Bernard Ghanem; arXiv 2026, submitted May 19; venue unverified.
- Sources: https://arxiv.org/abs/2605.19890 ; https://arxiv.org/html/2605.19890v1
- Evidence: full-text memory algorithms, protocol and Tables 1/5 inspected.
- Question/method: isolate memory-policy contribution from adaptation objective; class-balanced feature-diversity memories with/without feature refresh.
- Datasets/metrics: CIFAR-10-C, ImageNet-C, ITD video clips; mean top-1 accuracy.
- Result: Table 1, memory 32, CIFAR-10-C: RoTTA+FPS 73.90 versus RoTTA+CSTU 69.23 accuracy; benefits vary by method. ViT Table 5 shows nearly identical RoTTA values for CSTU/CDS/FPS.
- Limitation/gap (our inference): not all diversity choices help. Protocol says fixed seed within stream setting; uncertainty must be expanded before drawing general conclusions. Memory decomposition alone is no longer a fresh contribution.

### A14 — On the Learnability of Test-Time Adaptation: A Recovery Complexity Perspective

- Authors/year/venue: Zhi Zhou, Ming Yang, Shi-Yu Tian, Kun-Yang Yu, Lan-Zhe Guo, Yu-Feng Li; arXiv 2026, v1 May 27, v2 June 9; venue unverified.
- Source: https://arxiv.org/abs/2605.28057
- Evidence: primary metadata and abstract verified, proofs not audited.
- Question/method: characterize post-shift recovery; define recovery complexity and TTA learnability with a discrete surrogate for nonstationary streams.
- Datasets/metrics/result: theoretical recovery bounds and long-term reliability; no dataset or numeric benchmark claims verified here. Abstract reports order-matching upper and lower bounds.
- Limitation/gap (our inference): a project cannot claim the first recovery metric or fundamental analysis. Empirical path-conditioned component effects might complement theory, with assumptions kept distinct.

### A15 — A probabilistic framework for online test-time adaptation

- Authors/year/venue: Daniel Corrales, David Ríos Insua; arXiv 2026; venue unverified.
- Sources: https://arxiv.org/abs/2606.26457 ; https://arxiv.org/html/2606.26457v1
- Evidence: primary metadata, full-text inference/transition sections inspected; neural benchmark results not reliably extracted from HTML.
- Question/method: unify evolving adaptation parameters with uncertainty through state-space modeling and Gaussian posterior approximations; linearization, variational Bayes and Bayesian online natural gradients.
- Datasets/metrics/results: linear, nonlinear and neural TTA sections exist; exact benchmark table not verified, no numeric result retained.
- Limitation/gap (our inference): Bayesian online state estimation is occupied. A proposed uncertainty method must clarify identification assumptions and distinguish parameter uncertainty from label-prior uncertainty.

### A16 — Rethinking the Teacher-Student Framework for Test-Time Adaptation

- Authors/year/venue: Damian Sójka, Marc Masana, Bartłomiej Twardowski, Sebastian Cygert; arXiv 2026, September 2; venue unverified.
- Sources: https://arxiv.org/abs/2609.02507 ; https://arxiv.org/html/2609.02507v1
- Evidence: full-text section 4 and Table 1 inspected.
- Question/method: isolate teacher plasticity and long-run collapse; freeze teacher trainable parameters, keep per-batch BN statistics, predict using student.
- Datasets/metrics: ImageNet-C, 20-loop ImageNet-C, CCC and further image/segmentation settings; mean accuracy.
- Result: Table 1 consistency objective, 20-loop ImageNet-C: EMA teacher 7.9%, fixed teacher 31.3%; CCC 1.6% versus 27.2%.
- Limitation/gap (our inference): freezes teacher weights but not necessarily its current-batch normalization behavior. Long-term teacher drift analysis is direct prior art; state interventions must not accidentally label it a wholly fixed predictor.

### A17 — Rethinking the Test-Time Prompt Tuning Objective from the Perspective of Calibration

- Authors/year/venue: Jungwon Choi, Hyeonseo Jang, Kibok Lee, Eunwoo Kim; arXiv 2026, August 31; venue unverified.
- Source: https://arxiv.org/abs/2608.30230
- Evidence: primary abstract and metadata verified.
- Question/method: entropy-minimized augmented-view predictions become overconfident; align original-view prediction to a confidence-temperature-adjusted augmented target while preserving its uncertainty.
- Datasets/metrics: diverse classification benchmarks, accuracy and calibration; exact roster/values not primary-full-text verified in this scan.
- Result: abstract reports improved accuracy and calibration; numbers from third-party summaries deliberately excluded.
- Limitation/gap (our inference): confidence-preserving prompt adaptation and view mismatch are occupied. Temporal class-conditional effects require explicit additional evidence.

### A18 — Detecting and Correcting for Label Shift with Black Box Predictors

- Authors/year/venue: Zachary Lipton, Yu-Xiang Wang, Alexander Smola; ICML 2018, PMLR 80:3122–3130.
- Source: https://proceedings.mlr.press/v80/lipton18a.html
- Evidence: proceedings metadata, abstract and full-text setup inspected.
- Question/method: infer target priors from unlabeled observations using a source-estimated confusion matrix (BBSE).
- Datasets/metrics: natural-image experiments; estimation error and classification quality; exact roster not extracted.
- Result: consistency and error bounds under label shift and invertible confusion matrix; numerical values not retained.
- Limitation/gap: unchanged class-conditional distribution is an explicit assumption. Strong covariate/conditional shift invalidates a naive transfer of these guarantees. This is foundational for candidate T2, not a new discovery.

### A19 — On Calibration of Modern Neural Networks

- Authors/year/venue: Chuan Guo, Geoff Pleiss, Yu Sun, Kilian Q. Weinberger; ICML 2017, PMLR 70:1321–1330.
- Source: https://proceedings.mlr.press/v70/guo17a.html
- Evidence: proceedings metadata and abstract verified.
- Question/method: neural-network confidence versus correctness; post-hoc calibration including scalar temperature scaling.
- Datasets/metrics: image/document classification; calibration; exact table definitions not extracted in this scan.
- Result: temperature scaling effective across most studied datasets; no numeric result copied.
- Limitation/gap (our inference): a temperature selected on source validation is a proper cheap baseline, while selecting it on target test labels is inadmissible for deployment claims. Calibration and ranking must be treated as distinct outcomes.

### A20 — What Drives Test-Time Adaptation for CLIP? A Controlled Empirical Study from an Update Perspective

- Authors/year/venue: Jiazhen Huang, Xiao Chen, Zhiming Liu, Yaru Sun, Jingyan Jiang, Zhi Wang; arXiv 2026, v2 August 6; venue unverified. HTML v2 uses the grammatical variant “from a Update Perspective”; abstract-page title above is used.
- Sources: https://arxiv.org/abs/2606.14299 ; https://arxiv.org/html/2606.14299v2
- Evidence: full-text sections 4–5 and protocol inspected after root referral.
- Question/method: controlled taxonomy and benchmark of parameter, state and inference updates (TTABC); isolate role of evidence and optimization.
- Datasets/metrics: natural-shift, fine-grained and corruption image classification, including ImageNet-A; accuracy, latency and memory.
- Result: explicitly studies periodic-reset TPT; longer intervals cause severe collapse, with no-reset accuracy around 3% at the end in the described experiment. No universal winner across shift types.
- Limitation/gap (our inference): update-target taxonomy and controlled comparisons are prior art. Appendix states a common fixed seed; a paired history intervention needs independent stream repetitions and complete state controls.

### A21 — AttenDence: Maximizing Attention Confidence for Test Time Adaptation (v1); later LookSharp

- Authors/year/venue: Yash Mali, arXiv v1 November 24, 2025; later v3 February 7, 2026 is titled LookSharp: Attention Entropy Minimization for Test-Time Adaptation and adds Evan Shelhamer. Cite v1 for the inspected momentum discussion, not v3 with v1-only authors.
- Sources: https://arxiv.org/html/2511.18925v1 ; https://arxiv.org/abs/2511.18925
- Evidence: full-text v1 sections 3.3, 4.1–4.4 inspected.
- Question/method: minimize final-layer attention entropy; investigate persistent Adam moments despite resetting model parameters per image.
- Datasets/metrics: v1 DINOv3-based CIFAR-10-C, 19 corruption types severity 5; 1,000 images per corruption used for hyperparameter search and 9,000 for test; accuracy.
- Result: qualitative beneficial optimizer-memory observation; v1 numeric figures not independently read.
- Limitation/gap (our inference): “optimizer memory matters after parameter reset” is explicitly prior art. The paper's assertion that predictions are independent under parameter reset is too strong when optimizer state affects updates; our protocol must test functional independence directly.

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
