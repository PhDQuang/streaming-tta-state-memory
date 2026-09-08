# Adversarial novelty analysis and selection

Dated 2026-09-08. The starting assumption for all three shortlisted candidates was that their generic ideas were already known. This file follows the nine-candidate matrix; detailed searches and verified paper records are retained in `scans/` and consolidated in `literature_review.md`. Negative searches are bounded evidence, never proof of novelty.

## T1 — Controlled history interventions in streaming vision

**Threats tested:** order sensitivity, continual collapse, periodic and selective resets, optimizer memory, recovery delay, repeated base images, memory-policy ablations, teacher drift, update-target benchmarking. Primary full text was inspected for TTABC, AttenDence v1, ASR, OATTA, UniTTA, PeTTA, GoTTA and recent teacher work, with evidence depth in the ledgers. Official Tent/SAR source was additionally inspected and pinned for executable checks.

| Close prior | Claim it already covers | Residual distinction |
|---|---|---|
| [RDumb](https://arxiv.org/abs/2306.05401), [ASR](https://arxiv.org/abs/2603.03796) | Collapse, reset timing, reset location, performance loss and recovery | Compare interventions on the *same* future image sequence after matched histories, rather than different before/after samples |
| [OATTA](https://arxiv.org/abs/2601.21012) | Useful temporal order and transition priors | Histories with identical batches and a controlled common recent tail isolate persistent conditioning |
| [AttenDence v1](https://arxiv.org/html/2511.18925v1) | Retained optimizer moments affect adaptation despite parameter resets | Quantify duration and interactions after common recency control; optimizer memory itself is not new |
| [TTABC](https://arxiv.org/html/2606.14299v2) | Controlled study of parameter/state/inference updates and periodic-reset instability | Factorial interventions on fully serialized history states and paired unseen continuations |
| [PeTTA](https://arxiv.org/abs/2311.18193), [GoTTA](https://arxiv.org/abs/2605.19890) | Recurring-domain persistence, full resets, memory-policy contributions | Fixed batch multiset and identical probes separate altered data from altered state |
| [POEM](https://openreview.net/pdf?id=qamfjyhPeg) | One corrupted version per original image | Base-ID exclusion is a validity control, not a contribution |
| [Teacher-student critique](https://arxiv.org/abs/2609.02507) | Long-run teacher drift and frozen-teacher benefit | Teacher drift alone cannot support the proposed paper |

Root query ledger includes exact/synonymous `common suffix`, `matched history`, `prefix suffix`, `path dependence`, `counterfactual stream`, `state transplant`, `optimizer state reset`, and broader reset/order queries. Backward checking followed ASR's reset comparisons and OATTA's temporal priors; forward searches found 2026 TTABC and teacher/memory studies. Search-engine indexing and accessible versions limit coverage.

**Classification:** B for the experimental protocol; potentially A for a replicated nontrivial finding. Neither a new reset algorithm nor the observation that updates fail to commute is claimed. Elementary first-batch invariance under full forward-state reset is a correctness theorem, not a research discovery. A checkpoint omission is an engineering audit finding; it must be separated from algorithmic effects and from published benchmark claims.

**Surviving question:** do nontrivial functional differences persist on unseen shared images after common recent exposure, under correct state serialization, and can a prespecified state intervention predictably alter those differences across methods/backbones without merely making both histories fail? No equivalent complete design was found in the searched literature. Full experimental evidence is still missing.

## R2 — Composition-specific cross-modal brittleness

[The Hard Positive Truth](https://arxiv.org/html/2409.17958v1) already establishes lexical brittleness induced by negative fine-tuning; SugarCrepe++ probes semantic equivalence; [the 2023 adaptation benchmark](https://proceedings.neurips.cc/paper_files/paper/2023/hash/a2a544e43acb8b954dc5846ff0d77ad5-Abstract-Datasets_and_Benchmarks.html) already evaluates image/text corruptions; [C2LIP](https://arxiv.org/html/2603.25722v2) explicitly seeks compositionality without zero-shot degradation. Joint modality shifts are also studied in a [2026 preprint](https://arxiv.org/abs/2604.24602).

Adversarial searches covered `CLIP compositionality corruptions`, `SugarCrepe corruption`, `hard positives corruption CLIP`, `paraphrase joint robustness`, exact titles and backward references. Root independently opened Hard Positive Truth and C2LIP, confirming the important overlap. The remaining candidate is a controlled *interaction change* under matched training, not a broad corruption benchmark. A score difference-in-differences can be written as an embedding inner product; that algebra is elementary, not a contribution.

**Classification:** A/B, conditional. **Novelty risk:** observed interactions may be fully explained by margin geometry, reduced clean performance, or corruptions removing semantic evidence. A blinded semantic-validity assessment and matched retraining across objectives are substantial prerequisites. No exact equivalent found, but the full 2023 benchmark and joint-shift preprint need a deeper appendix audit if revived. Strong reserve direction; not selected because causal validity of visual/text interventions is less directly checkable than state replay.

## S1 — Selective-risk transfer under vocabulary expansion

[Revisit the Open Nature of Open Vocabulary Semantic Segmentation](https://proceedings.iclr.cc/paper_files/paper/2025/hash/17c89f4c14a4aa238616c126f5af19bb-Abstract-Conference.html) already establishes vocabulary-expansion sensitivity. [FreeCP](https://arxiv.org/html/2508.00557v1) handles ambiguity/redundancy, SCAN and SynCLIP address semantic/synonym inconsistency, What Holds Back OVS uses pipeline oracles, and [Conf-OT](https://arxiv.org/html/2505.24693v1) provides zero-shot conformal methods. The source ledger supplies author/proceedings links and evidence depth.

Search families included expanding query vocabularies, ambiguous classes, distractors, label-set changes, open-vocabulary confidence, selective prediction, conformal prediction and risk control. Forward/backward checks followed FreeCP, RevisitOVS, SCAN, CAT-Seg, FC-CLIP and newer vocabulary-alignment work.

**Classification:** B with potential A finding only for source-threshold selective-risk transfer under paired vocabulary interventions. **Novelty risk:** elementary softmax normalization may explain the result; “absent” distractors may actually be present in incompletely annotated images. Conformal set coverage is not selective accepted-mask risk. Demoted because these semantic and annotation confounders are harder to eliminate, and the closest prior art already occupies most generic claims.

## Final decision

Select **T1** based on the highest weighted scientific score, important deployment question, executable negative controls, strong public baselines, and an interpretable null outcome. R2 remains a serious reserve, S1 is third. Compute efficiency has only 2% matrix weight; local hardware does not enter scoring. T1 may still fail the novelty or empirical tests; selecting it is not asserting success.

Full hypotheses, protocol, state contracts and stop/funding gates are in `proposal.md`. Primary completion requires real large-scale evidence and a fresh reviewer audit; the present repository is preparation plus Stage A validation.
