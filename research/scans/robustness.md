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
