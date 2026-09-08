# Literature review

Review date: 2026-09-08. Bounded primary-source review, not an exhaustive systematic review. Three independent scans cover streaming adaptation, open-vocabulary dense perception, and VLM robustness/composition/synthetic data. Most emphasis is 2023–2026, with necessary foundations. Evidence depth and unknowns are explicit per record. All external numerical results are author reports, never our experiments.

## Synthesis

Recent work shifts from nominal accuracy toward temporal deployment, confidence reliability, language-dependent evaluation, and source/generator shortcuts. Large pretrained encoders make strong frozen baselines essential. Several intuitive ideas are already occupied: long-term collapse and selective resets; synonym/vocabulary sensitivity; hard-positive brittleness; and synthetic source shortcuts. The useful residual questions isolate mechanisms with paired interventions and independent evaluation rather than add modules.

We considered nine projects before selection. The top three are controlled adaptation-history effects (T1), compositional training × multimodal perturbation interactions (R2), and selective-risk transfer after vocabulary expansion (S1). See topic_candidates.md and novelty_analysis.md for decision logic.

## Coverage and limits

Sources include CVPR/ICCV/ECCV, NeurIPS, ICLR, ICML, WACV, BMVC, IJCV/TPAMI-linked records, arXiv, and official repositories. A targeted broad search is not an audit of every AAAI/Pattern Recognition paper or complete Google/Semantic Scholar citation graph. Some records are abstract-depth and explicitly lack exact datasets or tables; those missing details are not invented. Core selected-project works receive additional full-text/code inspection. Dated query trails remain in research/scans/*.md.


## Independent adaptation evidence ledger

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



## Independent segmentation evidence ledger

# Open-vocabulary dense prediction and prompt robustness scan

Search date: 2026-09-08. Investigator: independent segmentation literature agent. This is a bounded primary-source scan, not a systematic review or a claim of exhaustive novelty clearance. No experiments or paid actions were performed. Numerical results below are author-reported, not reproduced.

## Decision-relevant findings

The generic ideas “measure vocabulary expansion sensitivity,” “make synonymous prompts consistent,” “test SAM with imperfect prompts,” and “replace exact-label segmentation metrics with semantic similarity” are already occupied. RevisitOVS (ICLR 2025), FreeCP (ICCV 2025), SynCLIP (CVPR 2026), Stable-SAM (ICLR 2025), SCAN (CVPR 2024), and Rethinking Evaluation Metrics directly threaten these ideas. They must not be presented as new discoveries. The three candidates below preserve narrower, falsifiable investigations, but should be demoted relative to an equally important candidate with less direct overlap.

A potentially useful distinction is between **accuracy under vocabulary expansion**, which is established, and **transfer of a precommitted selective-risk threshold under vocabulary interventions**, which was not found as the exact subject of a paper in this scan. Even that narrower question inherits strong calibration and conformal-prediction precedents. Its empirical contribution must exceed showing the elementary softmax denominator effect.

## Evidence conventions

- F: inspected full-text methods or tables, plus primary metadata. This does not mean every appendix or code path was audited.
- A: primary abstract/proceedings record inspected; dataset/metric details outside that record remain unknown.
- P: primary PDF indexed excerpts inspected, with some direct downloads blocked (403/bot challenge).
- Limits and relationships below are this reviewer's assessments unless explicitly attributed.
- Several search-result “published ago” dates were inconsistent. Years are taken from actual proceedings headers or arXiv submission records, not search-engine relative dates.

## Important paper records

### P01 — CLIP

**Title:** Learning Transferable Visual Models From Natural Language Supervision. **Authors:** Alec Radford, Jong Wook Kim, Chris Hallacy, Aditya Ramesh, Gabriel Goh, Sandhini Agarwal, Girish Sastry, Amanda Askell, Pamela Mishkin, Jack Clark, Gretchen Krueger, Ilya Sutskever. **Year/venue:** ICML 2021. **Primary:** https://proceedings.mlr.press/v139/radford21a.html ; https://arxiv.org/abs/2103.00020 . **Depth:** A.

**Question/method:** Can image-caption contrastive training support broad zero-shot recognition? Dual encoders learn aligned image/text embeddings; class text prototypes instantiate a classifier. **Data/metrics:** 400M pretraining pairs; over 30 downstream datasets, including ImageNet; classification accuracy. **Result:** Author reports ImageNet zero-shot accuracy comparable to original supervised ResNet-50. **Limits:** Pretraining corpus not recreated here; global alignment does not establish dense grounding or reliable confidence. **Relation:** Foundation for semantic matching; prompt and vocabulary construction are part of the classifier and must be versioned.

### P02 — SAM

**Title:** Segment Anything. **Authors:** Alexander Kirillov, Eric Mintun, Nikhila Ravi, Hanzi Mao, Chloe Rolland, Laura Gustafson, Tete Xiao, Spencer Whitehead, Alexander C. Berg, Wan-Yen Lo, Piotr Dollar, Ross Girshick. **Year/venue:** ICCV 2023. **Primary:** https://openaccess.thecvf.com/content/ICCV2023/html/Kirillov_Segment_Anything_ICCV_2023_paper.html ; https://arxiv.org/abs/2304.02643 . **Depth:** A.

**Question/method:** General promptable segmentation through a large image encoder, prompt encoder and mask decoder, coupled to a data engine. **Data/metrics:** SA-1B, over 1B masks on 11M images; zero-shot segmentation tasks; complete metric suite not extracted here. **Result:** Broad zero-shot transfer reported; no exact downstream performance number transcribed. **Limits:** A supplied prompt defines target intent; original released model predicts masks without category labels. **Relation:** Baseline for prompt-distribution studies, not evidence that arbitrary user prompts have uniform reliability.

### P03 — FC-CLIP

**Title:** Convolutions Die Hard: Open-Vocabulary Segmentation with Single Frozen Convolutional CLIP. **Authors:** Qihang Yu, Ju He, Xueqing Deng, Xiaohui Shen, Liang-Chieh Chen. **Year/venue:** NeurIPS 2023. **Primary:** https://arxiv.org/abs/2308.02487 ; https://proceedings.neurips.cc/paper_files/paper/2023/file/661caac7729aa7d8c6b8ac0d39ccbc6a-Paper-Conference.pdf . **Depth:** A/P.

**Question/method:** Can one frozen convolutional CLIP backbone provide both masks and open-vocabulary recognition? Shared single-stage features replace repeated image encoding. **Data/metrics:** COCO panoptic training; zero-shot ADE20K, Mapillary Vistas, Cityscapes; PQ/AP/mIoU. **Result:** Author-reported ADE20K 26.8 PQ, 16.8 AP, 34.1 mIoU. **Limits:** COCO mask supervision and large pretraining remain; claims depend on specified test taxonomy. **Relation:** Credible mask-first OVS baseline for separating mask availability, classification, and postprocessing. Warning: a third-party model card incorrectly linked arXiv:2311.15539; direct opening showed an unrelated optimization paper. That identifier is excluded.

### P04 — CAT-Seg

**Title:** CAT-Seg: Cost Aggregation for Open-Vocabulary Semantic Segmentation. **Authors:** Seokju Cho, Heeseong Shin, Sunghwan Hong, Anurag Arnab, Paul Hongsuck Seo, Seungryong Kim. **Year/venue:** CVPR 2024; preprint 2023. **Primary:** https://arxiv.org/abs/2303.11797 ; https://openaccess.thecvf.com/content/CVPR2024/papers/Cho_CAT-Seg_Cost_Aggregation_for_Open-Vocabulary_Semantic_Segmentation_CVPR_2024_paper.pdf . **Depth:** A/P.

**Question/method:** Adapt CLIP to dense prediction by aggregating image-text cosine-similarity volumes using spatial and class aggregation, with encoder finetuning. **Data/metrics:** Standard OVS benchmarks including ADE20K-847 and Pascal Context-459; mIoU. **Result:** Paper reports +3.6 and +8.1 mIoU respectively over its recent comparator. **Limits:** Comparator and pretraining settings must be matched before numerical reuse; class aggregation can make outputs depend on the full query set. **Relation:** Contrasts naturally with mask-first and independently queried models for intervention experiments.

### P05 — OWLv2

**Title:** Scaling Open-Vocabulary Object Detection. **Authors:** Matthias Minderer, Alexey Gritsenko, Neil Houlsby. **Year/venue:** NeurIPS 2023. **Primary:** https://arxiv.org/abs/2306.09683 ; https://proceedings.neurips.cc/paper_files/paper/2023/hash/e6d58fc68c0f3c36ae6e0e64478a69c0-Abstract-Conference.html . **Depth:** A.

**Question/method:** Scale object detection with web pseudo-box supervision; OWLv2 plus OWL-ST improve filtering, label-space choices and training efficiency. **Data/metrics:** More than 1B web examples at largest scale; LVIS rare AP. **Result:** L/14 rare AP rises from 31.2 to 44.6 in the reported scaling comparison. **Limits:** Large inaccessible/self-generated training supervision; rare-category performance does not equal calibrated per-instance confidence. **Relation:** Detection generalization baseline and contrasting scoring architecture, not a cheap-from-scratch baseline.

### P06 — Grounding DINO

**Title:** Grounding DINO: Marrying DINO with Grounded Pre-Training for Open-Set Object Detection. **Authors (arXiv record):** Shilong Liu, Zhaoyang Zeng, Tianhe Ren, Feng Li, Hao Zhang, Jie Yang, Qing Jiang, Chunyuan Li, Jianwei Yang, Hang Su, Jun Zhu, Lei Zhang. **Year/venue:** ECCV 2024; preprint 2023. **Primary:** https://arxiv.org/abs/2303.05499 ; https://github.com/IDEA-Research/GroundingDINO . **Depth:** A.

**Question/method:** Ground language within a detector using a feature enhancer, language-guided query selection and cross-modal decoding. **Data/metrics:** COCO, LVIS, ODinW, RefCOCO/+/g; AP and referring-expression evaluation. **Result:** Abstract reports 52.5 COCO zero-shot AP and 26.1 mean ODinW AP. **Limits:** Version/checkpoint and training data matter; repository's displayed author list differs from arXiv, so bibliography retains the verified arXiv version. **Relation:** Joint text-conditioned representation provides a useful architectural contrast to independent class scores.

### P07 — SCAN

**Title:** Open-Vocabulary Segmentation with Semantic-Assisted Calibration. **Authors:** Yong Liu, Sule Bai, Guanbin Li, Yitong Wang, Yansong Tang. **Year/venue:** CVPR 2024, pages 3491–3500; preprint 2023. **Primary:** https://arxiv.org/abs/2312.04089 ; https://openaccess.thecvf.com/content/CVPR2024/html/Liu_Open-Vocabulary_Segmentation_with_Semantic-Assisted_Calibration_CVPR_2024_paper.html . **Depth:** A/P.

**Question/method:** Mitigate seen-vocabulary embedding bias and masked-region domain mismatch using CLIP semantic priors and contextual shift. Introduces SG-IoU to credit semantic relationships. **Data/metrics:** COCO-Stuff training; ADE150/847, VOC, PC59/459; mIoU and SG-IoU. **Result:** Author reports leading results on evaluated benchmarks; exact scores not transcribed. **Limits:** Treating a parent category as correct changes the task's specificity requirements. **Relation:** Direct novelty blocker for “synonym/hypernym-aware metrics”; representation calibration is distinct from probabilistic confidence calibration.

### P08 — Stable-SAM

**Title:** Stable Segment Anything Model. **Authors:** Qi Fan, Xin Tao, Lei Ke, Mingqiao Ye, Di Zhang, Pengfei Wan, Yu-Wing Tai, Chi-Keung Tang. **Year/venue:** ICLR 2025. **Primary:** https://proceedings.iclr.cc/paper_files/paper/2025/hash/78288ef33b18a351c3cd679dc9a15c8d-Abstract-Conference.html ; https://proceedings.iclr.cc/paper_files/paper/2025/file/78288ef33b18a351c3cd679dc9a15c8d-Paper-Conference.pdf . **Depth:** F (methods and Table 1).

**Question/method:** Why does SAM fail under casual prompts? Deformable sampling and dynamic routing plugins counter attention drift. **Data/metrics:** DIS validation, ThinObject-5K test, COIFT, HR-SOD; mIoU, boundary mIoU, stability; 20 random prompts per image/type. **Result:** SAM ViT-L average mIoU is 79.5 with GT boxes, 48.8 noisy boxes, 43.3 one point, 84.8 ten points (Table 1). **Limits:** Specified synthetic noise/random-mask points need not match human actions; these are SAM baseline results, not Stable-SAM improvement numbers. **Relation:** Directly defeats generic prompt-quality/stability novelty.

### P09 — Human versus automated prompting

**Title:** Benchmarking Human and Automated Prompting in the Segment Anything Model. **Authors:** Jorge Quesada, Zoe Fowler, Mohammad Alotaibi, Mohit Prabhushankar, Ghassan AlRegib. **Year/venue:** arXiv 2024; later venue not verified here. **Primary:** https://arxiv.org/abs/2410.22048 ; https://github.com/olivesgatech/PointPrompt . **Depth:** A.

**Question/method:** How well do automated point-selection strategies represent human prompting? Use PointPrompt, geometric features and finetuning comparisons. **Data/metrics:** PointPrompt; segmentation scores and regression R-squared. **Result:** Abstract reports approximately 29% higher human segmentation scores and feature prediction R-squared above 0.5; precise denominator/aggregation not audited, so these must not become benchmark targets. **Limits:** Actual annotator split, prompt histories, license and score definition require full audit. **Relation:** Strong prior for any human-versus-synthetic prompt study; merely demonstrating a gap is not new.

### P10 — RevisitOVS

**Title:** Revisit the Open Nature of Open Vocabulary Semantic Segmentation. **Authors:** Qiming Huang, Han Hu, Jianbo Jiao. **Year/venue:** ICLR 2025. **Primary:** https://proceedings.iclr.cc/paper_files/paper/2025/hash/17c89f4c14a4aa238616c126f5af19bb-Abstract-Conference.html ; https://openreview.net/forum?id=2vHIHrJAcI ; https://qiming-huang.github.io/RevisitOVS/ . **Depth:** A/P.

**Question/method:** Evaluation under expanded, ambiguous query vocabularies; mask-wise matching replaces strict pixelwise label matching and vocabulary ambiguity is analyzed. **Data/metrics:** Common OVS datasets; full dataset list not extracted; mask-wise metrics. **Result:** Reports degradation under expansion and improved capabilities when ambiguities are reduced. **Limits:** Semantic tolerance changes target granularity; complete implementation/statistical validation not audited. **Relation:** Directly invalidates an unqualified claim to first study vocabulary-set sensitivity; relevant metric baseline.

### P11 — FreeCP

**Title:** Training-Free Class Purification for Open-Vocabulary Semantic Segmentation. **Authors:** Qi Chen, Lingxiao Yang, Yun Chen, Nailong Zhao, Jianhuang Lai, Jie Shao, Xiaohua Xie. **Year/venue:** ICCV 2025. **Primary:** https://arxiv.org/abs/2508.00557 ; https://arxiv.org/html/2508.00557v1 ; https://openaccess.thecvf.com/content/ICCV2025/papers/Chen_Training-Free_Class_Purification_for_Open-Vocabulary_Semantic_Segmentation_ICCV_2025_paper.pdf . **Depth:** F.

**Question/method:** Remove irrelevant classes and resolve locally ambiguous classes using CAM/refined-CAM consistency and fine-grained descriptions. **Data/metrics:** VOC20/21, PC59/60, COCO Object/Stuff, Cityscapes, ADE20K; mIoU. **Result:** Table 2 reports MaskCLIP average 30.3 versus 41.2 with FreeCP across eight settings. **Limits:** “Eight benchmarks” includes alternate background conventions; LLM-generated descriptions are extra information. **Relation:** Strong baseline/novelty blocker for vocabulary filtering. Its oracle GT-vocabulary comparison must not be confused with a deployable method or used to tune on test annotations.

### P12 — What holds back OVS?

**Title:** What Holds Back Open-Vocabulary Segmentation? **Authors:** Josip Saric, Ivan Martinovic, Matej Kristan, Sinisa Segvic (diacritics in bibliography). **Year/venue:** ICCV Workshops 2025, MMFM. **Primary:** https://arxiv.org/abs/2508.04211 ; https://arxiv.org/html/2508.04211v1 ; https://openaccess.thecvf.com/content/ICCV2025W/MMFM/papers/Saric_What_Holds_Back_Open-Vocabulary_Segmentation_ICCVW_2025_paper.pdf . **Depth:** F/P.

**Question/method:** Decompose mask-transformer OVS bottlenecks with ground-truth oracles. **Data/metrics:** COCO-to-ADE20K comparisons; semantic mIoU and panoptic PQ. **Result:** Analysis attributes shortcomings to region recognition, mask proposal quality, and useful internal masks discarded by inference. **Limits:** Oracles use information absent at deployment; a gap to an oracle is not a proposed achievable improvement. **Relation:** Direct prior for pipeline-stage decomposition; an investigation must add controlled interventions beyond repeating oracle gaps.

### P13 — SynCLIP

**Title:** SynCLIP: Synonym-Coherent Language-Image Pretraining for Robust Open-Vocabulary Dense Perception. **Authors:** Mingjie Xie, Guangjun He, Dongli Xu, Youtian Lin, Hongjue Li, Pengming Feng, Jian Guan, Yue Deng. **Year/venue:** CVPR 2026 (CVF indexed accepted PDF); arXiv submitted July 2026. **Primary:** https://arxiv.org/abs/2607.11008 ; https://openaccess.thecvf.com/content/CVPR2026/papers/Xie_SynCLIP_Synonym-Coherent_Language-Image_Pretraining_for_Robust_Open-Vocabulary_Dense_Perception_CVPR_2026_paper.pdf . **Depth:** A/P.

**Question/method:** Align spatial grounding across synonyms; semantic-consistent spatial attention, spatial refinement and SEViC synonym/definition corpus. **Data/metrics:** SEViC uses COCO2017 training images and COCO/LVIS vocabulary; dense grounding consistency and downstream detection/segmentation; complete metric/table suite not inspected. **Result:** Reports improved linguistic-variant consistency; exact downstream scores not verified. **Limits:** Public checkpoint and reproduction details require audit; synonym corpus potentially changes supervision. **Relation:** Direct novelty defeat for synonym-invariance loss or synonym-robust grounding claimed in isolation.

### P14 — SAM 3

**Title:** SAM 3: Segment Anything with Concepts. **Authors:** Nicolas Carion and 37 coauthors (full verified arXiv author list in bibliography). **Year/venue:** ICLR 2026, preprint November 2025. **Primary:** https://arxiv.org/abs/2511.16719 ; https://openreview.net/pdf/407b3abdb82eba58bb391e9799acb5d12b09bd7b.pdf . **Depth:** A/P.

**Question/method:** Find all instances matching text/image concept prompts in images and video; shared detector/tracker backbone and a separate presence head. **Data/metrics:** SA-Co concept benchmark; training corpus includes 4M concept labels and hard negatives. Full metric protocol not audited. **Result:** Abstract reports approximately twice previous system accuracy; do not reuse that broad statement as an exact benchmark target. **Limits:** Concept presence differs from target-instance identity; model/data access and deployment license require verification. **Relation:** A modern concept-segmentation baseline is necessary before broad 2026 claims about SAM-based open-vocabulary systems.

### P15 — Open-vocabulary confidence calibration

**Title:** Open-Vocabulary Calibration for Fine-tuned CLIP. **Authors:** Shuoyuan Wang, Jindong Wang, Guoqing Wang, Bob Zhang, Kaiyang Zhou, Hongxin Wei. **Year/venue:** arXiv 2024; accepted venue not verified in this scan. **Primary:** https://arxiv.org/abs/2402.04655 . **Depth:** A.

**Question/method:** Calibrate confidence when prompt learning transfers to novel classes; Distance-Aware Calibration changes temperature based on distance to base class text embeddings. **Data/metrics:** Seven prompt-learning methods, eleven classification datasets; confidence-calibration metrics, exact metric suite not extracted. **Result:** Reports improved calibration with negligible inference overhead; exact values unverified. **Limits:** Classification and base-to-new class shifts differ from set interventions on the same image/target. **Relation:** Strong baseline inspiration; adding a temperature adapter is not independently novel.

### P16 — Conf-OT

**Title:** Conformal Prediction for Zero-Shot Models. **Authors:** Julio Silva-Rodriguez, Ismail Ben Ayed, Jose Dolz. **Year/venue:** CVPR 2025. **Primary:** https://arxiv.org/abs/2505.24693 ; https://arxiv.org/html/2505.24693v1 ; https://openaccess.thecvf.com/content/CVPR2025/papers/Silva-Rodriguez_Conformal_Prediction_for_Zero-Shot_Models_CVPR_2025_paper.pdf . **Depth:** F.

**Question/method:** Improve CLIP conformal-set efficiency using symmetric transductive optimal transport over calibration and query data. **Data/metrics:** 15 classification datasets; coverage, set size, class-conditional coverage variation; LAC/APS/RAPS. **Result:** Table 3 at alpha=.10, ViT-B/16: RAPS mean set size 8.12 versus Conf-OT 6.68, both .900 coverage. **Limits:** Guarantees require stated exchangeability/symmetry assumptions; they do not automatically cover adaptive vocabulary changes or correlated pixels. **Relation:** Necessary principled comparator; a new OVS risk study must distinguish prediction-set coverage from selective error among accepted masks.

### P17 — Semantic evaluation metrics

**Title:** Rethinking Evaluation Metrics of Open-Vocabulary Segmentaion [sic, arXiv title]. **Authors (arXiv version):** Hao Zhou, Tiancheng Shen, Xu Yang, Hai Huang, Xiangtai Li, Lu Qi, Ming-Hsuan Yang. **Year/venue:** arXiv 2023; author publication page confirms a TPAMI 2025 journal version, but conflicting page/author-order metadata means bibliography cites only the unambiguous arXiv version. **Primary:** https://arxiv.org/abs/2311.03352 ; https://faculty.ucmerced.edu/mhyang/pubs.html . **Depth:** A.

**Question/method:** Compare eleven semantic similarity functions and derive Open mIoU/AP/PQ. **Data/metrics:** Twelve OVS methods; quantitative analysis and user study; full dataset list unverified. **Result:** Reports better reflection of open-vocabulary ability. **Limits:** Similarity is partly subjective and can favor coarse labels; this scan did not audit whether monotonicity/gaming tests already exist in appendices. **Relation:** Directly defeats “first semantic metric” and “first evaluator comparison” claims.

### P18 — VocAlign

**Title:** Lost in Translation? Vocabulary Alignment for Source-Free Adaptation in Open-Vocabulary Semantic Segmentation. **Authors:** Silvio Mazzucco, Carl Persson, Mattia Segu, Pier Luigi Dovesi, Federico Tombari, Luc Van Gool, Matteo Poggi. **Year/venue:** BMVC 2025. **Primary:** https://bmva-archive.org.uk/bmvc/2025/assets/papers/Paper_875/paper.pdf ; https://github.com/Sisso16/VocAlign ; https://arxiv.org/abs/2509.15225 . **Depth:** A/P.

**Question/method:** Source-free OVS adaptation via teacher/student vocabulary alignment, additional concepts, LoRA, and top-K student class selection. **Data/metrics:** Cityscapes and zero-shot segmentation benchmarks; mIoU. **Result:** Abstract reports +6.11 Cityscapes mIoU. **Limits:** Pseudolabel assumptions, vocabulary choice, and teacher/student selection are potential confounders. **Relation:** Vocabulary-conditioned adaptation already exists; relevant if the main project concerns adaptive model state.



## Independent robustness evidence ledger

# Independent scan: vision-language robustness, composition, and synthetic shortcuts

Search date: 2026-09-08. Scope: primary conference repositories, arXiv, official author repositories; emphasis 2023–2026 with foundations. This is an independent candidate-generation input, not the final project selection. Results below are **published author reports, not reproduced experiments**. An abstract establishes a claim's existence, not its validity. Numerical percentages retain the source's terminology unless the table establishes percentage points.

## Search audit

All queries below ran on 2026-09-08 using web search, followed by primary-source opens. Search-result summaries from third-party aggregators were used only to discover primary papers.

| Query family (representative exact queries) | Finding / decision |
|---|---|
| `site:openaccess.thecvf.com CVPR 2023 Winoground ARO vision language compositionality bag words`; `"SugarCrepe" "2023" Hsieh authors`; `"SugarCrepe++" authors 2024` | Found foundations, CREPE, ARO, SugarCrepe, hard-positive evaluation. |
| `site:arxiv.org 2025 2026 compositionality CLIP hard negative text shortcuts benchmark` | Found CVPR 2026 C2LIP; generic hard-negative improvement is highly saturated. |
| `"synthetic data" "spurious correlations" "2026"`; `"counterfactual" "augmentation" "Waterbirds" "2025"` | Found SAGE (Sep 2026), AutoBackSwap, provenance-gradient guidance. |
| `"synthetic" "augmentation" "provenance" "spurious"`; `"synthetic data" "shortcut" "minority"`; `"augmentation" "generator artifacts" classification robust`; `"synthetic" "real" "source" "spurious" augmentation Waterbirds` | **Disproved** generic synthetic-source shortcut novelty via From Fake to Real and Synthetic Simplicity. |
| `"CLIP" "compositionality" "corruptions"`; `"SugarCrepe" "corruption"`; `"hard positives" "corruption" "CLIP"`; `"vision language" "paraphrase" "joint" "robustness" corruption` | Broad image/text robustness already exists. No exact matched factorial study of hard-positive robustness after compositional fine-tuning found. |
| `"vision-language" "joint" "corruptions" benchmark`; `"CLIP" "paraphrases" "blur"`; `"Scaling Vision-Language Models" "Al-Tahan"` | Found NeurIPS 2023 adaptation benchmark, CVPRW 2024 four-axis analysis, ACM MM 2026 modality shift work. Narrowed candidate R2 away from merely adding corruptions. |
| `RoboShot spurious correlations zero shot robustness task relevant features 2024`; `"CLIP" "spurious" "2025" "orthogonal"`; `"spurious" "task-specific" "CLIP" debiasing`; `"debiasing" "CLIP" "collateral"` | Found RoboShot, RaVL, task-specific visual probing; naive prompt-conditioned debiasing is not new. |

Backward checking: read related-work/reference and experiment sections of C2LIP, The Hard Positive Truth, and From Fake to Real; followed their foundation/benchmark references through primary repositories. Forward checking: searched exact titles and synonymous mechanisms through 2026. This is not an exhaustive citation-graph crawl. Google Scholar and paywalled full texts were not required or comprehensively inspected.

## Verified paper records

### P01 — Counterfactual Generative Networks

- Authors/year/venue: Axel Sauer; Andreas Geiger. 2021, ICLR. [Paper](https://openreview.net/pdf?id=BXewfAYMmJw), [official code](https://github.com/autonomousvision/counterfactual_generative_networks).
- Question/method: Can independent shape, texture, and background generation produce useful counterfactual training images? Disentangle those mechanisms with pretrained inductive biases.
- Data/metrics: MNIST variants, ImageNet; classification and shifted classification accuracy.
- Result: Authors report improved OOD robustness with a small original-task accuracy cost; exact comparative numbers not audited here.
- Limitations: Generated mechanism separation depends on inductive assumptions; realism and intervention validity matter.
- Relation/evidence: Foundational obstacle to claiming counterfactual augmentation is new. Primary abstract, paper front matter, and official implementation documentation inspected.

### P02 — Winoground: Probing Vision and Language Models for Visio-Linguistic Compositionality

- Authors/year/venue: Tristan Thrush; Ryan Jiang; Max Bartolo; Amanpreet Singh; Adina Williams; Douwe Kiela; Candace Ross. 2022, CVPR. [Paper record](https://openaccess.thecvf.com/content/CVPR2022/html/Thrush_Winoground_Probing_Vision_and_Language_Models_for_Visio-Linguistic_Compositionality_CVPR_2022_paper.html).
- Question/method: Can VLMs bind identical words in different orders to the correct images? Expert-curated two-image/two-caption matching.
- Data/metrics: 400 groups; text, image, and joint group accuracy.
- Result: Tested models largely fail to exceed chance meaningfully.
- Limitations: Small sample size and ambiguous/difficult examples complicate fine distinctions; a test-only benchmark cannot supply tuning data.
- Relation/evidence: Paired semantic control for R2/R3; primary metadata/abstract and paper task description inspected.

### P03 — Last Layer Re-Training is Sufficient for Robustness to Spurious Correlations

- Authors/year/venue: Polina Kirichenko; Pavel Izmailov; Andrew Gordon Wilson. 2023, ICLR; first preprint 2022. [Paper](https://arxiv.org/abs/2204.02937).
- Question/method: Do biased ERM features retain useful core information? Freeze features and retrain a linear layer using balanced data (DFR).
- Data/metrics: Spurious-correlation and ImageNet background/texture evaluations; worst-group and average accuracy. Exact dataset-by-table inventory not audited here.
- Result: Authors report matching or exceeding more complex robustness methods with inexpensive retraining.
- Limitations: Balanced retraining data is an informational advantage; representation sufficiency is not universal.
- Relation/evidence: Mandatory baseline for any synthetic group-balancing project. Primary abstract verified; final ICLR venue corroborated by proceedings discovery and official researcher publication metadata; table results not reproduced.

### P04 — When and why vision-language models behave like bags-of-words, and what to do about it?

- Authors/year/venue: Mert Yuksekgonul; Federico Bianchi; Pratyusha Kalluri; Dan Jurafsky; James Zou. 2023, ICLR. [Paper](https://arxiv.org/abs/2210.01936), [official code](https://github.com/mertyg/vision-language-models-are-bows).
- Question/method: Do contrastive VLMs encode order, relations, and attributes? ARO benchmark and hard-negative fine-tuning (NegCLIP).
- Data/metrics: Visual Genome relations/attributes, COCO/Flickr30k order tasks; image-caption discrimination accuracy and retrieval.
- Result: Compositional failures and hard-negative improvements reported; exact gains not quoted because benchmark artifacts complicate interpretation.
- Limitations: SugarCrepe subsequently shows artifacts can exaggerate gains.
- Relation/evidence: R2 hard-negative baseline, with positive-only matched fine-tuning needed. Primary repository/metadata and later primary paper's detailed baseline descriptions inspected.

### P05 — CREPE: Can Vision-Language Foundation Models Reason Compositionally?

- Authors/year/venue: Zixian Ma; Jerry Hong; Mustafa Omer Gul; Mona Gandhi; Irena Gao; Ranjay Krishna. 2023, CVPR. [Paper record](https://openaccess.thecvf.com/content/CVPR2023/html/Ma_CREPE_Can_Vision-Language_Foundation_Models_Reason_Compositionally_CVPR_2023_paper.html).
- Question/method: Evaluate systematic recombination and increasing compositional complexity with scene-graph-derived positives/foils.
- Data/metrics: Over 370k systematicity image-text pairs; 17k productivity pairs and 278k negatives; retrieval/discrimination across seen/unseen compounds and complexity.
- Result: Seven architectures/four algorithms exhibit composition weaknesses despite extensive pretraining.
- Limitations: Synthetic text foils can contain artifacts; inferred pretraining membership and scene graphs may be noisy.
- Relation/evidence: R2 complementary evaluation, not sole primary endpoint. Official record and paper scene-graph/evaluation sections inspected.

### P06 — SugarCrepe: Fixing Hackable Benchmarks for Vision-Language Compositionality

- Authors/year/venue: Cheng-Yu Hsieh; Jieyu Zhang; Zixian Ma; Aniruddha Kembhavi; Ranjay Krishna. 2023, NeurIPS Datasets and Benchmarks. [Paper](https://arxiv.org/abs/2306.14610), [official code](https://github.com/RAIVNLab/sugar-crepe).
- Question/method: Can language-only artifacts make compositional benchmarks misleading? Construct fluent hard negatives and reduce textual biases.
- Data/metrics: COCO-2017 validation images with replace/swap/add negatives; pairwise accuracy by edit type.
- Result: Re-evaluated compositional improvement is substantially smaller; swap and relation/attribute binding remain difficult.
- Limitations: Pairwise preference does not require invariance across multiple equivalent captions; COCO domain and residual artifacts remain relevant.
- Relation/evidence: Core R2 evaluation. Primary abstract and official dataset/evaluation instructions inspected. COCO image licenses must be handled separately from repository code license.

### P07 — Mitigating Spurious Correlations in Multi-modal Models during Fine-tuning

- Authors/year/venue: Yu Yang; Besmira Nushi; Hamid Palangi; Baharan Mirzasoleiman. 2023, ICML. [Paper record](https://proceedings.mlr.press/v202/yang23j.html).
- Question/method: Can language expose and separate spurious attributes during CLIP adaptation? Multimodal contrastive supervision of spuriosity.
- Data/metrics: Waterbirds prominently; worst-group/average accuracy and activation analyses.
- Result: Abstract reports worst-group improvements of 23% for CLIP ResNet-50 and 32% for ViT relative to ERM, maintaining average accuracy. Absolute-versus-relative convention requires table recheck before reuse.
- Limitations: Depends on identifying and describing spurious concepts; attribution visualizations alone cannot establish causal correctness.
- Relation/evidence: Credible R3 baseline and strong overlap threat. Metadata and primary abstract verified; detailed tables not audited.

### P08 — Benchmarking Robustness of Adaptation Methods on Pre-trained Vision-Language Models

- Authors/year/venue: Shuo Chen; Jindong Gu; Zhen Han; Yunpu Ma; Philip Torr; Volker Tresp. 2023, NeurIPS Datasets and Benchmarks. [Proceedings](https://proceedings.neurips.cc/paper_files/paper/2023/hash/a2a544e43acb8b954dc5846ff0d77ad5-Abstract-Datasets_and_Benchmarks.html).
- Question/method: How do prompt/adaptor/LoRA/full adaptation methods tolerate multimodal corruption? Controlled benchmark of 11 methods.
- Data/metrics: Four source VLM datasets expanded to seven corrupted benchmarks, 96 visual and 87 textual corruptions; task accuracy/robustness. Dataset-specific protocol not fully audited.
- Result: Text shifts can hurt more; more data/parameters and full fine-tuning do not guarantee greater robustness.
- Limitations: General task robustness is different from semantic-equivalence preservation in composition.
- Relation/evidence: Direct prior art against any broad claim that multimodal adaptation robustness is unexplored. Proceedings abstract and PDF opening inspected.

### P09 — SUGARCREPE++ Dataset: Vision-Language Model Sensitivity to Semantic and Lexical Alterations

- Authors/year/venue: Sri Harsha Dumpala; Aman Jaiswal; Chandramouli Sastry; Evangelos Milios; Sageev Oore; Hassan Sajjad. 2024, NeurIPS Datasets and Benchmarks. [Proceedings](https://papers.nips.cc/paper_files/paper/2024/hash/200661bf8f4993b7828a45a2a90f2ecf-Abstract-Datasets_and_Benchmarks_Track.html), [official data](https://github.com/Sri-Harsha/scpp).
- Question/method: Separate lexical change from semantic change with two equivalent positive captions and one negative.
- Data/metrics: SugarCrepe/COCO-derived triplets; image-to-text and text-only triplet accuracy.
- Result: Existing composition rankings do not reliably predict performance on semantic/lexical alterations.
- Limitations: Text-only performance is a semantic diagnostic, not evidence of image grounding; triplets share source images.
- Relation/evidence: R2 factorial text intervention without generating new text. Primary abstract and official dataset README inspected; license stated CC BY 4.0 for work, while image rights require separate check.

### P10 — The Hard Positive Truth about Vision-Language Compositionality

- Authors/year/venue: Amita Kamath; Cheng-Yu Hsieh; Kai-Wei Chang; Ranjay Krishna. 2024, ECCV. [Paper](https://arxiv.org/abs/2409.17958), [full text](https://arxiv.org/html/2409.17958v1).
- Question/method: Does hard-negative learning preserve equivalent captions? Add hard positives, define brittleness, train with both positive/negative examples.
- Data/metrics: 112,382 evaluation examples, 1,775,259 training pairs; original/augmented test accuracy and brittleness; retrieval/classification checks.
- Result: Table 1 reports CLIP B/32 REPLACE accuracy 61.6 to 46.8 under hard-positive augmentation; NegCLIP 68.6 to 52.1. This is a published table, not our reproduction.
- Limitations: Single B/32 architecture for main controlled comparison; lexical oversensitivity itself is already established.
- Relation/evidence: Most important R2 baseline and novelty restriction. Inspected method, table 1, perturbation-transfer discussion, appendix D/E; do not claim discovering hard-positive brittleness.

### P11 — From Fake to Real: Pretraining on Balanced Synthetic Images to Prevent Spurious Correlations in Image Recognition

- Authors/year/venue: Maan Qraitem; Kate Saenko; Bryan A. Plummer. 2024, ECCV; arXiv first 2023, inspected version revised Aug 2026. [Paper](https://arxiv.org/abs/2308.04553), [full text](https://arxiv.org/html/2308.04553).
- Question/method: Does balancing nuisance marginals leave joint nuisance/source shortcuts? Pretrain on balanced synthetic samples, then train on real data.
- Data/metrics: CelebA-HQ, UTK-Face, SpuCo Animals; worst and balanced group accuracy across multiple bias strengths.
- Result: Reports up to 20% worst-group gain; experiments include source-aware GroupDRO/DFR/resampling controls with matched synthetic counts.
- Limitations: Unspecified generator biases may remain; source separation does not prove semantic validity.
- Relation/evidence: **Invalidates generic R1 provenance-balancing novelty**, including joint (nuisance, source) rationale. Full mechanism equations, datasets, comparisons, limitations and appendix training settings inspected.

### P12 — Synthetic Simplicity: Unveiling Bias in Medical Data Augmentation

- Authors/year/venue: Krishan Agyakari Raja Babu; Rachana Sathish; Mrunal Pattanaik; Rahul Venkataramani. 2024, MICCAI Workshop on Data Engineering in Medical Imaging; LNCS 15265, 64–72. [Paper](https://arxiv.org/abs/2407.21674), [DOI](https://doi.org/10.1007/978-3-031-73748-0_7).
- Question/method: Does source–label correlation create shortcuts? Vary real/synthetic class proportions under controlled binary classification.
- Data/metrics: MNIST 2/4 and CAMUS 2-/4-chamber views; accuracy stratified by source/class.
- Result: Extreme source confounding creates near-zero accuracy for unsupported source/class combinations; balanced augmentation is more stable.
- Limitations: Narrow binary settings; task difficulty interpretation is not isolated causally.
- Relation/evidence: Further defeats R1's generic mechanism claim. Primary full text method/results inspected; exact figure values not digitized.

### P13 — Zero-Shot Robustification of Zero-Shot Models

- Authors/year/venue: Dyah Adila; Changho Shin; Linrong Cai; Frederic Sala. 2024, ICLR. [Proceedings](https://proceedings.iclr.cc/paper_files/paper/2024/hash/92ce40962b4098f7bf6eed33128fc606-Abstract-Conference.html), [official code](https://github.com/SprocketLab/roboshot).
- Question/method: Can task descriptions guide zero-shot robustness? RoboShot uses LM-generated helpful/harmful directions to modify embeddings.
- Data/metrics: Nine image/NLP tasks; worst-group/overall accuracy, including Waterbirds/CelebA and PACS/VLCS per official code.
- Result: Authors report average 15.98% improvement across evaluated tasks/baselines; aggregate convention should be checked before comparison.
- Limitations: Helpful/spurious roles depend on the task; generated insights are uncertain and subspaces may overlap.
- Relation/evidence: R3 must compare task-specific RoboShot directly, not mischaracterize it as unconditional. Proceedings abstract, paper overview, author explanation, official repo inspected.

### P14 — RaVL: Discovering and Mitigating Spurious Correlations in Fine-Tuned Vision-Language Models

- Authors/year/venue: Maya Varma; Jean-Benoit Delbrouck; Zhihong Chen; Akshay Chaudhari; Curtis Langlotz. 2024, NeurIPS (as stated in primary arXiv record). [Paper](https://arxiv.org/abs/2411.04097).
- Question/method: Can localized image features reveal and correct spurious alignment? Region clustering identifies failure-associated features; region-aware loss mitigates them.
- Data/metrics: 654 VLMs across model/domain/spuriosity configurations; discovery quality and worst-group image classification accuracy. Exact dataset/metric inventory not yet audited.
- Result: Abstract reports 191% discovery improvement and 8.2% worst-group improvement; cannot treat these as matched numbers for our protocol.
- Limitations: Error-based region selection is associative; transfer to changed concept roles requires testing.
- Relation/evidence: Direct prior art against proposing region-aware spurious correction as new. Primary metadata/abstract inspected.

### P15 — ASPIRE: Language-Guided Data Augmentation for Improving Robustness Against Spurious Correlations

- Authors/year/venue: Sreyan Ghosh; Chandra Kiran Evuru; Sonal Kumar; Utkarsh Tyagi; S Sakshi; Sanjoy Chowdhury; Dinesh Manocha. 2024, Findings of ACL. [Paper](https://aclanthology.org/2024.findings-acl.22/), DOI 10.18653/v1/2024.findings-acl.22.
- Question/method: Generate examples lacking shortcuts without group labels; use language descriptions, editing-based shortcut discovery, and personalized generation.
- Data/metrics: Four datasets and nine baselines, including Hard ImageNet test-set contribution; worst-group classification accuracy. Other dataset identities not fully audited.
- Result: Abstract reports 1–38% improvements depending on method/setting.
- Limitations: Generation/editing quality and discovery errors; extra pretrained information must be accounted for.
- Relation/evidence: Mandatory synthetic-augmentation comparison if R1 pursued. Primary metadata/abstract verified; full experimental tables pending.

### P16 — Learning the Power of "No": Foundation Models with Negations

- Authors/year/venue: Jaisidh Singh; Ishaan Shrivastava; Mayank Vatsa; Richa Singh; Aparna Bharati. 2025, WACV. [Proceedings](https://openaccess.thecvf.com/content/WACV2025/html/Singh_Learning_the_Power_of_No_Foundation_Models_with_Negations_WACV_2025_paper.html).
- Question/method: Can targeted negation training improve CLIP? CC-Neg captions and CoN-CLIP contrastive objective.
- Data/metrics: CC-Neg 228,246 images, eight zero-shot classification datasets, SugarCrepe; top-1 and compositional accuracy.
- Result: Abstract reports 3.85% average classification improvement and 4.4% compositional improvement.
- Limitations: Absence/negation differs from relation binding and paraphrase invariance; benchmark gains need broad transfer tests.
- Relation/evidence: Optional additional R2 family; primary metadata/abstract and benchmark discussion inspected. Numbers not reproduced.

### P17 — No Hard Negatives Required: Concept Centric Learning Leads to Compositionality without Degrading Zero-shot Capabilities of Contrastive Models

- Authors/year/venue: Hai X. Pham; David T. Hoffmann; Ricardo Guerrero; Brais Martinez. 2026, CVPR. [Paper](https://arxiv.org/abs/2603.25722), [full text](https://arxiv.org/html/2603.25722v2).
- Question/method: Can phrase-level supervision and concept-conditioned pooling preserve binding without bespoke hard negatives? C2LIP adds noun-phrase and cross-attention contrastive losses to SigLIP.
- Data/metrics: DreamLIP-recaptioned CC3M; SugarCrepe/++, retrieval/classification; five epochs, eight A40 GPUs, batch 768.
- Result: Table 5 reports SugarCrepe mean 81.7 matched CC3M baseline versus 85.6 full method; Flickr8K 95.2 versus 96.4.
- Limitations: Most comparative checkpoints have differing training data; matched baseline is essential. No joint visual-corruption/hard-positive factorial test found in inspected sections.
- Relation/evidence: Required strong non-hard-negative family for R2. Full training setup, objective, ablation table, references, supplementary tasks inspected.

### P18 — SAGE: Subpopulation-Aware Generative Enhancement for Mitigating Spurious Correlations

- Authors/year/venue: Yiming Luo; Rongqiang Zhao; Jie Liu. 2026 arXiv preprint, submitted September 1; no peer-reviewed venue verified. [Paper](https://arxiv.org/abs/2609.01051).
- Question/method: Can subgroup discovery plus generation overcome insufficient minority diversity without group labels? Cluster-derived labels train conditional generation; synthetic balanced data supports last-layer reweighting.
- Data/metrics: Waterbirds, CelebA, MetaShift; worst-group accuracy.
- Result: Abstract reports 89.5%, 85.7%, 79.1% respectively; up to 7.7 percentage-point gain over group-label-free baselines.
- Limitations: Very recent, unreplicated preprint; cluster fidelity, synthetic evaluation independence, and complete compute unknown here.
- Relation/evidence: Direct overlap with synthetic-balanced DFR idea. Primary abstract and metadata verified only; no claim of paper-level validity.

### P19 — Majorization-Guided Test-Time Adaptation for Vision-Language Models under Modality-Specific Shift

- Authors/year/venue: Lixian Chen; Mingxuan Huang; Yanhui Chen; Junyi Lin; Yang Shi. 2026; arXiv states accepted ACM MM 2026. [Paper](https://arxiv.org/abs/2604.24602).
- Question/method: Can unreliable modality confidence cause harmful adaptation? Frozen encoders plus fusion adaptation use drift/conflict signals.
- Data/metrics: ImageNet/CIFAR corruption, text prompt shifts, joint conditions; accuracy and wrong-more-confident events.
- Result: Abstract reports ImageNet text 57.97 to 66.51 and joint 21.68 to 26.27.
- Limitations: Label-prompt classification/fusion protocol is different from two-encoder compositional matching; accepted venue claim not separately verified against proceedings.
- Relation/evidence: Prevents claiming modality interactions in general are new. Primary metadata/abstract verified; full method not yet audited.

Other verified discovery leads needing fuller records if selected: [provenance-gradient guidance (2026)](https://arxiv.org/abs/2604.02946), [AutoBackSwap (2026)](https://arxiv.org/abs/2606.32018), [post-generation selection (2026)](https://arxiv.org/abs/2607.02637), [four-axis scaling study (CVPRW 2024)](https://openaccess.thecvf.com/content/CVPR2024W/AdvML/html/Al-Tahan_Scaling_Vision-Language_Models_Does_Not_Improve_Relational_Understanding_The_Right_CVPRW_2024_paper.html), [semantic guidance (CVPR 2025)](https://openaccess.thecvf.com/content/CVPR2025/papers/Stone_Learning_Visual_Composition_through_Improved_Semantic_Guidance_CVPR_2025_paper.pdf). None supports a claim of exhaustive coverage.



## Primary-researcher independent checks

# Independent cross-checks by primary researcher

Search date: 2026-09-08. Primary pages opened, with targeted full-text inspection where stated. Searches are evidence of a bounded review, not proof that an idea does not exist.

## Query ledger

- `site.thecvf.com CVPR 2026 test time adaptation benchmark`
- `site.arxiv.org 2026 vision language models robustness benchmark test time adaptation`
- `site.openreview.net ICLR 2026 vision robustness evaluation`
- `"test-time adaptation" "hysteresis"`; `"test-time adaptation" "path dependence"` — mostly irrelevant results; low recall cannot establish absence.
- `"test-time adaptation" "order" "benchmark" 2025 2026`
- `"test-time adaptation" "carryover"`; `"test-time adaptation" "recovery" reset poisoning`
- `"When and Where to Reset Matters for Long-Term Test-Time Adaptation"`
- `"test-time adaptation" "common suffix"`; `"test-time adaptation" "matched" "history"`
- `"test-time adaptation" "state" "optimizer" "reset"`
- `"What Drives Test-Time Adaptation for CLIP?"`; `"AttenDence: Maximizing Attention Confidence"`
- `"test-time adaptation" "counterfactual" "state"`; `"test-time adaptation" "prefix" "suffix"`

## Important verified records and consequences

### Huang et al., 2026 — What Drives Test-Time Adaptation for CLIP? A Controlled Empirical Study from an Update Perspective

Authors: Jiazhen Huang, Xiao Chen, Zhiming Liu, Yaru Sun, Jingyan Jiang, Zhi Wang. arXiv preprint; no conference acceptance asserted. [Metadata](https://arxiv.org/abs/2606.14299), [v2 full text](https://arxiv.org/html/2606.14299v2). The v2 HTML title uses “a Update”; preserve the metadata title in bibliography.

Question/method: which test-time update targets and evidence sources explain CLIP adaptation? TTABC unifies over 20 methods and controlled comparisons. Data include ImageNet variants/C, fine-grained classification datasets and overlaid label shift. Metrics include classification accuracy and efficiency. Author-reported finding: gains often reflect evidence quality more than optimization; continuous TPT updates can be unstable. Exact benchmark numbers not used here. Inspected §§2, 5 and implementation appendix. Limitation for our question: periodic resets and broad paradigm comparisons do not by themselves identify history effects on an identical, disjoint suffix. This paper defeats novelty claims based solely on a controlled TTA benchmark or parameter/state taxonomy.

### Mali, 2025 — AttenDence: Maximizing Attention Confidence for Test Time Adaptation

Author: Yash Mali (arXiv v1 metadata). arXiv preprint. [Metadata](https://arxiv.org/abs/2511.18925), [v1 full text](https://arxiv.org/html/2511.18925v1). Question/method: can CLS-to-patch attention entropy support adaptation? CIFAR-10-C, DINOv3 with a fine-tuned classification head; accuracy/mCA. Inspected §4.2 and optimizer discussion. Author reports optimizer-history benefits when model parameters reset; no numerical result reused. Thus optimizer carryover is known. The text's suggestion that parameter-reset predictions are independent is mathematically too strong when the retained optimizer affects the current update. Limitations: narrow dataset/backbone and insufficient separation of reset policies from order effects for our purpose. Any project must cite this prior observation explicitly.

### Lim, Hwang and Lee, 2026 — When and Where to Reset Matters for Long-Term Test-Time Adaptation

Authors: Taejun Lim, Joong-Won Hwang, Kibok Lee (arXiv metadata; proceedings spells Joongwon). ICLR 2026 status verified on [OpenReview paper](https://openreview.net/pdf?id=0JayjvOKxt). [Metadata](https://arxiv.org/abs/2603.03796), [full text](https://arxiv.org/html/2603.03796v1). Question/method: avoid collapse while retaining useful adaptation through adaptive/selective layer resets, regularization and adjustment. Benchmarks include ImageNet-C and CCC; accuracy, reset drop and recovery delay. Inspected §3.3, A.1, C.1–C.3; no exact reported number reused. They explicitly compare reset timing and target layers. This defeats generic selective-reset and recovery-time novelty. Their before/after-reset comparison uses different incoming batches; a matched-future intervention has a distinct estimand, subject to deeper verification.

### Kim et al., 2026 — Order-Aware Test-Time Adaptation: Leveraging Temporal Dynamics for Robust Streaming Inference

Authors: Young Kyung Kim, Oded Schlesinger, Qiangqiang Wu, J. Matías Di Martino, Guillermo Sapiro. arXiv preprint, 2026-01-28. [Primary metadata](https://arxiv.org/abs/2601.21012). Abstract/metadata verified; v2 HTML request failed because the observed record lists v1. Temporal inference already treats order as useful information. Dataset details and numerical results require full-text extraction; do not assert them from secondary snippets. This defeats “order matters” as a standalone contribution.

### Sheng et al., 2025 — The Illusion of Progress? A Critical Look at Test-Time Adaptation for Vision-Language Models

Authors: Lijun Sheng, Jian Liang, Ran He, Zilei Wang, Tieniu Tan. [arXiv metadata](https://arxiv.org/abs/2506.24000). Venue not independently established here. Abstract-verified TTA-VLM evaluates episodic/online methods across datasets, CLIP and SigLIP, with accuracy, robustness, calibration, OOD and stability measures. Author-reported conclusion: accuracy gains can reduce trustworthiness and progress over pioneering methods is limited. No benchmark numbers reused. It reinforces need for strong baselines and multiple metrics; generic benchmarking is already occupied.

## Provisional inference

Do not claim a new optimizer-memory phenomenon, a new reset mechanism, or first order-sensitivity benchmark. A potentially defensible contribution is a narrowly identified experimental estimand: the effect of two histories containing identical preformed batches on the same never-seen future images, after a common recency-control tail, and its response to explicitly defined state interventions. No equivalent combined protocol was found in these searches, but that is a bounded negative search result.

## Reviewer-requested foundation and close-prior checks

All checked 2026-09-08. These records complete citations used by implementation and manuscript, rather than expand the selected novelty claim.

- **AETTA: Label-Free Accuracy Estimation for Test-Time Adaptation** — Taeckyung Lee, Sorn Chottananurak, Taesik Gong, Sung-Ju Lee; CVPR2024,28643–28652. [CVF record](https://openaccess.thecvf.com/content/CVPR2024/html/Lee_AETTA_Label-Free_Accuracy_Estimation_for_Test-Time_Adaptation_CVPR_2024_paper.html). Predict accuracy from dropout disagreement without target labels; image-corruption benchmarks, accuracy-estimation error and downstream recovery. Inspected primary abstract and §5 recovery excerpt. It compares episodic, stochastic, Fisher and distribution-shift reset controls. Exact numbers not reused. Limitation: its estimator/reset mechanism is different from our matched-future estimand; a generic label-free reset proposal would overlap directly.
- **Benchmarking Neural Network Robustness to Common Corruptions and Perturbations** — Dan Hendrycks, Thomas Dietterich; ICLR2019. [Author repository](https://github.com/hendrycks/robustness), [dataset](https://zenodo.org/records/2235448). Establishes ImageNet-C/P and related corruption evaluation, mCE/mFR. Original project documents released JPEGs and protocols; no leaderboard number used as a matched target. Synthetic shifts do not establish natural temporal prevalence. Dataset source, archive sizes/checksums and record rights verified via API.
- **Sharpness-Aware Minimization for Efficiently Improving Generalization** — Pierre Foret, Ariel Kleiner, Hossein Mobahi, Behnam Neyshabur; 2020 preprint [arXiv2010.01412](https://arxiv.org/abs/2010.01412). Minimize loss in a local parameter neighborhood; classification on CIFAR/ImageNet and transfer tasks, accuracy. Authors report improved generalization; exact scores not reused. Abstract and official SAM algebra referenced through pinned SAR code. It supplies SAR's optimizer, not a new contribution here.
- **Deep Residual Learning for Image Recognition** — Kaiming He, Xiangyu Zhang, Shaoqing Ren, Jian Sun; CVPR2016. [CVF](https://openaccess.thecvf.com/content_cvpr_2016/html/He_Deep_Residual_Learning_CVPR_2016_paper.html). Residual connections enable deep classification/detection networks; ImageNet/COCO, classification error and detection metrics. Foundational architecture metadata verified; no exact paper number reused. Our torchvision V1 checkpoint/transform is separately pinned and is not a claim of retraining the paper.
- **An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale** — Alexey Dosovitskiy, Lucas Beyer, Alexander Kolesnikov, Dirk Weissenborn, Xiaohua Zhai, Thomas Unterthiner, Mostafa Dehghani, Matthias Minderer, Georg Heigold, Sylvain Gelly, Jakob Uszkoreit, Neil Houlsby; ICLR2021 camera-ready status in [arXiv metadata](https://arxiv.org/abs/2010.11929). Patch-sequence transformer; ImageNet/CIFAR100/VTAB transfer, accuracy and compute. Abstract reports strong large-pretraining transfer; no scores reused. Architecture replication here addresses normalization-family robustness, not original training claims.
- **Optical Recognition of Handwritten Digits** — E. Alpaydin, C. Kaynak; UCI1998, DOI10.24432/C50P49. [Primary data record](https://archive.ics.uci.edu/dataset/80/optical+recognition+of+handwritten+digits). NIST-derived8×8 digit counts from separate writer groups; dataset source and training-file checksum verified. We use only the original training partition for software tests. It is narrow, old, and not a meaningful primary benchmark for the research hypothesis.

Tent's ICLR2021 attribution is independently verified by its archived official author repository. RDumb's main NeurIPS2023 proceedings PDF was discovered by the independent reviewer; root direct PDF open failed, so the reviewer verification is retained without claiming root full-text access. Version/venue details remain traceable in scan files.
