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
