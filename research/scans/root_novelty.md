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
