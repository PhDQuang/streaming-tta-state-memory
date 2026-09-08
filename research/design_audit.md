# Independent skeptical audit: matched-history test-time adaptation

Date: 2026-09-08. Audit input: parent design specification; `research/scans/root_novelty.md`; current `src/historytta/metrics.py`; `research/status.md`. This is a design audit, not evidence that the implementation or experiments pass. No implementation files were edited. No new adaptation algorithm is proposed.

**Provisional judgment:** The controlled history/common-future investigation is scientifically defensible if the estimand, complete algorithm state, and independent experimental units are made explicit. A claim that order affects TTA, optimizer memory matters, or selective resets aid recovery would not be novel given the prior work already found. The strongest potential contribution is separating residual history effects from recent observations and measuring which state interventions remove them on an identical future stream. The scientific result may be null.

## 1. Exact experiment and estimand

Let a preformed batch be an immutable ordered list of `(base_image_id, corruption, severity, transform_seed)` records. Define a panel as disjoint prefix batches H, terminal common-tail batches W, and future batches Q. The same set of prefix batches is visited once in each history, H_AB and H_BA; only block order changes. Both start from the same source model, fresh TTA optimizer, and explicitly defined auxiliary state. Per-batch randomness must travel with batch identity, or be coupled by a clearly declared common-randomness rule, so permutation does not unintentionally change augmentation assignment.

Recommended primary timing:

`source -> H_AB or H_BA -> common W_l -> checkpoint -> state intervention R -> identical Q`.

R occurs **after W, immediately before the first prediction on Q**. This asks which carried state sustains residual differences after shared recent observations. Resetting before W instead asks how a common tail repairs an intervention; reserve it as a separate analysis. Do not pool these timings.

Use W lengths 0, 4, 16. Construct W_4 as the **last four batches of W_16**, so the most recent four observations are identical across the two nonzero-length conditions. Otherwise comparisons of tail length are confounded by different recent content. Within each W length the matched-history contrast is still valid even if tails are not nested, but the claimed washout curve is less controlled. Describe W=0 as an immediate order/recency contrast; it cannot establish long memory.

Prefer one prespecified terminal domain C for W and Q in the primary experiment. State whether C equals A, equals B, or is distinct. Q has new identities even if its corruption distribution matches W. A second C tests external validity; a mixed-domain Q changes the interpretation to memory during renewed shift. Q batch composition and ordering must match exactly across all compared arms.

The main unit-level estimands, calculated on the same panel/algorithm/backbone/W/R, are:

- Prediction disagreement: `D = mean_Q 1[argmax p_AB != argmax p_BA]`. This measures differing decisions, not a performance benefit or harm.
- Signed accuracy effect: `a = accuracy_AB - accuracy_BA`. Orient AB and BA using a fixed domain convention; averaging arbitrary pair labels can cancel by construction.
- Finite-panel absolute gap: `G = |a|`. Useful descriptive instability magnitude, but not an unbiased estimator of an absolute population accuracy effect. Finite-Q sampling alone can produce positive G even when expected signed accuracies coincide.
- Signed NLL effect: `n = mean_Q(NLL_AB - NLL_BA)`. Positive means AB is worse. Preserve orientation and raw per-batch values. Report Brier and mean probability distance as bounded secondary diagnostics when NLL has extreme outliers.

Compute predictions **before the update from that Q batch**. Save time-resolved effects as well as the average Q effect. Pre-register early Q (e.g. batches 1–4) and late Q (e.g. 13–16) summaries. A full-Q average may conceal rapid decay or sign reversal. The active Q trajectory itself generates further adaptation; these are residual-history effects under a specified future adaptation policy, not static checkpoint effects. A frozen-Q readout arm can distinguish checkpoint prediction differences from additional adaptation dynamics.

## 2. Mechanism attribution: what the factorial can and cannot show

For each history checkpoint, intervene on parameters P and optimizer O using source values, yielding keep/keep, reset/keep, keep/reset, reset/reset. Reuse the same prefix/W checkpoints; rerun only Q. The factorial is a controlled **state intervention**, but resetting parameters while keeping moments creates an artificial parameter–optimizer combination. It can be diagnostic without being a sensible deployment strategy.

For a chosen scalar history-sensitivity outcome Y (e.g. panel D), report all four values and simple contrasts:

- Parameter-reset change with optimizer retained: `Y10 - Y00`.
- Parameter-reset change with optimizer reset: `Y11 - Y01`.
- Optimizer-reset changes analogously.
- Interaction: `Y11 - Y10 - Y01 + Y00`.

Index 1 means reset. A negative simple contrast means reduced measured sensitivity. Calling one state the sole cause because one reset reduces D is too strong: the effect may depend on the other state, auxiliary state, reset-trigger logic, and the chosen Q. An interaction on a nonnegative outcome can also reflect a floor at zero; inspect signed probability/performance outcomes and full trajectories.

**Predict-before-update implication:** If P and every forward-affecting buffer are reset to the same source state, first-Q-batch predictions should match between histories even when optimizer moments are retained. Optimizer history can first alter predictions on Q batch 2 after the first different update. Differences in batch 1 under those conditions identify hidden forward state, different random numbers, differing data, or an implementation bug. Reset-trigger conditions based on carried SAR EMA may affect the first update and thus batch 2.

The state inventory must include more than trainable weights:

| State | Required treatment |
|---|---|
| Parameters and normalization affine values | Define exact source snapshot; reset only declared tensors. |
| BN running mean/variance, tracked-batch counters, train/eval mode | Forward state, distinct from optimizer. Either reset with P or hold identical explicitly. |
| Optimizer moments, momentum, step counters | Reset to a freshly initialized TTA optimizer, not the unknown pretraining optimizer. |
| Learning-rate scheduler, global iteration, warmup | Reset or retain explicitly; a fresh optimizer with an old schedule is not a full optimizer reset. |
| SAM wrapper/base optimizer, perturbation buffers | Snapshot only at a completed update; ensure old weights/perturbations do not leak between branches. |
| SAR EMA and auto-reset bookkeeping | Separate state; reset/reset P/O is not all-state reset when EMA remains factual. |
| Teacher/EMA weights, sample memory/queue, confidence history | Include for algorithms that use them; otherwise assert absent. |
| Python/NumPy/Torch/CUDA RNG, data-loader generators | Couple deterministically for exact controls; do not restore loader cursor to prefix content. |
| Internal saved source snapshots and algorithm flags | Must be immutable and identical; later internal reset must use the same source. |

For SAR, prefer a complete P × O × EMA factorial (eight suffix branches) if feasible. A smaller alternative is the P/O factorial **with EMA fixed to the same source value in every cell**, plus the natural unmodified trajectory and explicit EMA-only contrasts. Name the keep/keep cell correctly in that case: it still resets EMA. A P/O factorial with history-specific EMA retained has valid conditional intervention contrasts, but cannot cleanly attribute all residual memory to parameters and optimizer alone. Log every automatic reset, threshold crossing, and EMA value so discontinuous reset events are visible.

## 3. Batch normalization and deterministic controls

`no_grad()` does not stop BN running-statistic updates or all stochastic behavior. A prediction forward followed by a second adaptation forward can alter state twice. Define whether the prediction is the first differentiable forward reused for the update, or an isolated read-only forward. Preserve the published baseline's normalization/update semantics; document any adaptation of its prequential evaluation protocol.

Source `.eval()` and Tent-style train-mode batch normalization differ even with no gradient steps. Include a normalization-only control if claiming weight/optimizer adaptation explains the contrast. Within-batch statistics can use the current batch without its labels; this is transductive current-batch inference, not per-image online prediction. Report batch size and this allowance explicitly.

Required gates before empirical interpretation:

1. No-reset same-history checkpoint/replay returns identical logits, state tensors, and reset logs, not merely equal rounded accuracy.
2. Fresh full replay of the same history with the same identity-coupled randomness matches the saved trajectory.
3. All-state reset before Q matches a cold-start run of **the same adaptation algorithm and Q policy**, not necessarily a source-eval classifier. Check every Q batch, not just first predictions.
4. Source-only and read-only controls are invariant to prefix order, as applicable to their declared normalization semantics.
5. Multiset hashes, ordered manifests, and base-image disjointness assertions pass.
6. Resetting a state component changes only declared components; optimizer tensors remain attached to the correct parameter objects after cloning/loading.
7. Empty histories, empty W, zero accepted adaptation samples, SAR auto-reset, and interrupted checkpoint restoration are exercised.

Exact bitwise controls are appropriate in a fixed deterministic local environment. On cloud hardware, first enable deterministic kernels and record unsupported operations. If exactness cannot be attained, quantify a same-history numerical noise floor and fix tolerances **before** AB/BA outcome inspection. A loose post-hoc tolerance that hides trajectory divergence invalidates the mechanism attribution.

## 4. Images, leakage, and replication units

ImageNet-C corruption files reuse original clean image identities across conditions. Disjoint paths are insufficient: no clean base image may appear in both H and W, H and Q, or W and Q, including other corruptions/severities. Prefer unique base identities across independent panels. All variants/crops of one identity belong to the same partition. The same Q identities across treatments are deliberate pairing and must not be counted as new independent observations.

Use immutable hashed manifests. Stream assembly should not inspect test labels to select hard classes or choose corruption combinations. Join labels to predictions only for evaluation after the protocol is frozen. If class balancing is part of a benchmark protocol, define it in advance and disclose that annotation use; given the user's strict policy, unlabeled deterministic identity sampling is simpler.

Local sanity data must be the **official UCI optical-recognition TRAIN file**, with internal source-training/development/trajectory partitions. Never use `sklearn.load_digits` as a substitute: it is a different data access/protocol and may expose the official test set. Record URL, filename, checksum, row counts, and split hashes. Local results validate code and finite toy trajectories; they are not evidence for ImageNet-scale scientific claims.

Separate three random variables: source-training seed (if training a small local source), stream panel/assembly seed, and stochastic adaptation seed. Repeating a deterministic pretrained source with five nominal seeds may produce no additional information. Pair source initialization and adaptation randomness across histories/interventions. Average adaptation-seed repeats within panel for the primary panel-level analysis; expose their individual results as a numerical/stochastic sensitivity check.

Do **not** treat Q images, Q batches, reset branches, W lengths, corruption variants, or source seeds as independent stream panels. The state trajectory couples Q outcomes. A bootstrap of individual saved predictions conditions on a realized adaptation history and does not reproduce how a resampled earlier example would change later state. For inference on newly sampled streams, resample whole panels; a bootstrap that changes the stream's internal images must rerun adaptation.

If independent random streams are sampled with replacement from a fixed benchmark, they can be independent Monte Carlo draws **conditional on that finite benchmark**, even if some images overlap by chance. That supports inference on randomized stream assembly over those exact images, not new-image-population generalization. Fixed reused panels with new RNG seeds provide only conditional seed variance. State the population of inference and avoid describing all repeats as independent image evidence.

When each image panel is reused across multiple corruption-domain pairs, treat domain pair as a repeated condition. Compute the prespecified pair-average effect within each panel, then form uncertainty across panels. Display per-pair effects separately. Generalization to new corruption families requires more families, not more seeds on the same families. ResNet and ViT and a second benchmark are replication settings, not interchangeable IID replicates.

## 5. Statistical tests, intervals, and multiplicity

The current `paired_summary` implements a t interval for independent scalar contrasts. It is suitable as an approximate panel-level summary for moderately regular outcomes; it must not be fed all images, correlated W cells, or panel×seed rows. For skewed nonnegative D/G with many zeros and small panel count, show all panels and bootstrap whole panels as sensitivity. With eight pilot panels, neither a bootstrap nor a t interval establishes precise tail behavior; treat intervals as planning uncertainty.

The helper `exact_sign_flip_pvalue` is **not automatically valid** for deterministic paired AB/BA outputs. Pairing alone does not imply exchangeability. Exact sign-flip inference needs a genuinely justified randomized assignment under a sharp null or a sign-symmetric joint null distribution. A null of zero mean signed effect does not imply symmetry. Randomly renaming which domain is A can make signed effects cancel and changes the estimand. Never sign-flip nonnegative disagreement or absolute gaps. Recommendation: do not use exact sign-flip p-values as the primary analysis here; use panel-level effect intervals and prespecified practical thresholds. The general requirement for exchangeability is discussed in [this methodological preprint](https://arxiv.org/abs/2406.07756); the recommendation is this audit's application to the design.

NLL is unbounded and rare confidently wrong predictions can dominate it. Report the raw mean, per-panel distribution, and a prespecified robust secondary summary (e.g. median panel effect), without silently clipping or removing failures. Computation through stable log-softmax avoids probability-floor artifacts. ECE with fixed bins is noisy and bin-dependent; use Brier/NLL as primary calibration diagnostics and ECE only secondary.

Pick one confirmatory question, for example: residual history disagreement at W=16 under no external reset for a prespecified algorithm/backbone/domain-pair mixture. Primary D assesses persistence, and the signed accuracy/NLL gaps assess consequences. Then test the few planned state contrasts as a separate family with Holm correction or simultaneous panel-bootstrap intervals. Do not scan every W/algorithm/severity/backbone/reset and present only the significant cell. A second benchmark is a prespecified replication rather than another search opportunity.

Absence of significance is not evidence of washout. To claim an effect is practically negligible, require an upper confidence bound below a prespecified small-effect threshold. For signed effects, use an equivalence interval entirely inside `[−delta, +delta]`; for D use one-sided upper bound `< delta_D`. Power for zero is not the target: bound a scientifically meaningful magnitude. No monotone decay assumption is justified; an adaptive system can forget and later diverge again under Q.

## 6. Concrete pilot size, thresholds, and progression gates

These are recommended **planning values**, not post-hoc scientific standards. Freeze them before paid pilot outcome inspection. A failure to meet them can justify modifying the hypothesis, but should not lead to searching random settings until a positive result appears.

| Stage | Minimum design | Gate / decision |
|---|---|---|
| Free local correctness | Official UCI TRAIN-only internal splits; at least 3 source seeds and several distinct trajectory manifests; complete deterministic controls | All invariants in section 3 pass. Any violation blocks scientific interpretation. Toy order effects are not a scale-selection criterion. |
| Paid pilot (only after user approval) | One ImageNet-C backbone (ResNet-50), source + Tent + SAR; 8 distinct panels, three prespecified A/B/C choices; W=0/4/16; Q=16 batches; fixed batch size; P/O factorial and explicit SAR EMA controls | Correct baselines, no leakage, deterministic noise floor far below effects, measured compute. Estimate variance and practical magnitude; no publication-level significance claim. |
| Full confirmation | 32 independent image panels if available, 3–5 adaptation randomness repeats only when genuinely stochastic; frozen corruption choices; ResNet-50 plus ViT with a method appropriate to its normalization; second benchmark | Replicate effect or establish narrow null; report all panels/conditions. Full-stage N may be adjusted using pilot variance before opening disjoint full data, within an approved cost ceiling. |

Use the pilot to measure GPU time, state-snapshot size, and variance; final hardware/cost estimate must be based on those measurements. Replaying 4–8 suffix branches can dominate cost even when prefix checkpoints are shared. The audit author has not measured throughput and does not authorize any spend.

Suggested practical thresholds:

- Persistence: `delta_D = 1 percentage point` mean Q disagreement after W=16. Continue toward a positive-mechanism claim when the point estimate exceeds 2 points on more than one prespecified domain setting and the uncertainty is compatible with exceeding 1 point; this is a funding/prioritization gate, not proof.
- Consequence: `delta_accuracy = 1 percentage point` absolute signed accuracy magnitude within a prespecified oriented setting; `delta_NLL = 0.02 nats/example`. These are candidate engineering-significance values. Report smaller precise findings honestly but do not automatically call them important.
- State contribution: a prespecified reset contrast reduces D by at least 0.5 percentage point **and** does not merely trigger universal collapse; inspect accuracy/calibration and automatic-reset traces. A reduction in disagreement achieved by making both paths wrong is not improved robustness.
- Null completion: after adequate full replication, upper 95% confidence bound for D below 1 point at W=16, and signed performance equivalence within thresholds, supports practical washout for the evaluated conditions. It does not establish universal absence of memory.
- Modify/abandon central claim: effects occur only at W=0, only from altered batch membership or future-image reuse, only in invalid baseline settings, only below the deterministic noise floor, or vanish after a justified hidden-state control. Report these negatives and revise the claim.

For a rough two-sided 5% / 80%-power mean paired contrast, `n ≈ (2.8 * sigma_panel / delta)^2`. This is an asymptotic planning approximation, not an exact guarantee. If panel SD is 2 points and target effect is 1 point, n≈32; SD 4 points needs n≈126. For SD 1 point and target 1 point, n≈8, but eight panels still poorly characterize heterogeneity and tails. A CI half-width of 0.5 point with SD 2 points needs approximately 62 panels before small-sample correction. Report the measured SD and resulting power/precision tradeoff rather than asserting 3–5 seeds suffice.

Feasible ImageNet-C panel example at batch size 32: 16 prefix batches (8 A, 8 B), 16 maximum W, 16 Q = 1,536 unique base identities per panel. Thirty-two fully identity-disjoint panels need 49,152 base images. That nearly exhausts the usual 50k evaluation pool, leaving no room for an equally large separate pilot from the same pool. Therefore choose the pilot/full image budget jointly: e.g. a smaller disjoint pilot, shorter prefix or Q, 24 full panels, or explicitly conditional random-stream inference. Do not accidentally reuse pilot images as untouched confirmation or silently shrink Q after observing results. A separate development source/benchmark can support pilot engineering, while ImageNet-C remains locked confirmation.

## 7. Limits and reviewer verdict

The design can show intervention-specific dependence on earlier observations under controlled identical future data. It cannot by itself establish real-world prevalence, identify one unique internal cause, claim training order is useless, or show a new reset algorithm is superior. AB/BA blocks are an intentionally strong temporal manipulation; natural slowly varying streams and random permutations are external-validity checks, not replacements for the controlled contrast.

The paper should retain rejected novelty claims and acknowledge explicit prior optimizer-carryover, order-aware, selective-reset, and TTA-benchmark work documented in `root_novelty.md`. If only simple order sensitivity is found, provisional rating is **Reject** for insufficient new science. If matched-history effects persist after shared recency, survive complete state controls, have bounded statistical uncertainty, and reveal a reproducible state-dependent mechanism on two backbones/benchmarks, the design could support a useful paper. At present the appropriate project status is **unvalidated investigation**, not a completed research contribution.

Priority fixes before pilot: complete state ledger; reset timing; base-image identity splits; independent panel definitions; removal of unjustified exact sign-flip claims; distinguish disagreement from harm; pilot/full image-budget arithmetic; frozen thresholds and baseline protocol. No paid action was taken for this audit.

## 8. Design response and implemented analysis safeguards

Update 2026-09-08 following the primary researcher's design decisions. The following supersedes the preliminary panel-count recommendations above; it is a description of the agreed design, not a claim that runs have completed.

- Interventions are `none`, `parameters`, `optimizer`, `parameters_optimizer`, `aux`, `parameters_aux`, `optimizer_aux`, `parameters_optimizer_aux`, and `all`. The first eight form a complete P/O/aux factorial; `all` additionally restores every declared buffer. Auxiliary state is SAR EMA plus bookkeeping, and Tent bookkeeping; figures do not label it EMA-only.
- Reset timing is after H+W, before Q; W4 is the final four batches of W16. Source and normalization controls use none/all only.
- Stage A uses one reused image panel (`uci_internal_fixed`) across source-training seeds/scenarios. Analysis therefore reports no independent-panel confidence interval. Separate seed tables and thin-line/dot plots display descriptive seed variability, never claim three independent image panels.
- The cloud pilot has three disjoint panels with 2,560 base identities each (7,680 total) within a 20% identity-hash development pool. Three panels are severely underpowered for variance/heterogeneity estimation: use measured runtime and code diagnostics to plan full experiments; do not interpret a wide or nominally significant pilot interval as convincing scientific evidence.
- Full confirmation plans 24 disjoint panels of 1,536 base identities (36,864 total) in an 80% reserve. This resolves the earlier image-budget arithmetic. Twenty-four panels may not resolve a 1-point effect if panel SD is near or above 2 points; report resulting precision honestly or request a revised design before opening confirmation outcomes.
- Primary persistence remains disagreement at W16 with a 1-percentage-point practical threshold. Harmfulness is a separate claim requiring performance/calibration consequences.

`scripts/generate_tables.py` now averages scenarios within seed/panel, then seeds within globally unique panel IDs, before descriptive panel summaries. It retains seed/panel individual CSVs and a distinct mean/SD/individual-seed table. Reset contrasts and full factorial main/interaction contrasts are formed within exact scenario/seed/panel before any averaging. Incomplete factorial cells are never filled. Duplicate trajectory identifiers fail explicitly; unequal scenario inventories warn and retain descriptive labeling. The scripts generate no p-values.

`scripts/generate_figures.py` reads recorded CSV/NPZ data for washout, paired reset/factorial effects, source-training curves, and all four correctness groups. Outcome examples use the first eligible sorted recorded comparison and lexicographically first image IDs within each group, with full IDs/counts in a JSON manifest. No outcome-based selection chooses favorable samples. Empty input creates only an explicitly labeled protocol schematic and missing-input notes. PNG, PDF, and SVG outputs have captions and provenance manifests.

Ten targeted analysis tests passed at the latest update: replication-unit aggregation, shared-panel no-CI handling, matched-scenario reset contrasts, factorial scale/completeness, duplicate rejection, paired image-label consistency, empty-input honesty, unfinished-run rejection, exact matched performance-reference comparisons, and end-to-end plotting using fixtures confined to temporary test directories. Test fixture values were not stored as experimental results. All six figure types were visually checked against completed Stage A v1 recorded data. State-effect axes were aligned across methods and single-category plot padding was corrected; revised state/factorial/schematic renders were inspected again and passed visual QA. Protocol and training footers identify their distinct evidence types. Source/no-reset, normalization-only/no-reset, and same-method/no-reset performance references are paired on exact seed/panel/scenario/W/direction before aggregation. Positive error/NLL/Brier/ECE changes denote worse reference-relative performance; these harm contrasts are kept separate from AB/BA disagreement. Analysis manifests record current script/input hashes, and the example manifest hashes its selected prediction files.


## 9. Completed local artifact audit (v2)

The final local v2 artifacts pass an independent NumPy recomputation audit: 528 prediction archives, 264 AB/BA pairs, 5,016 scalar comparisons, and 528 immutable-manifest Q identity/label checks. Nineteen analysis/evaluation tests pass, including tampered scalar/label/order/file rejection, missing mandatory cell/status rejection, and nonzero audit CLI status on inconsistent metrics. Default table/figure generation now requires both a completed marker and the entire frozen-config expected matrix; absent cells are not silently interpreted as a completed factorial. An explicit `--allow-partial-import` option produces visibly labeled exploratory outputs, and was not used for Stage A.

All 528 corresponding v1/v2 NPZ arrays and all non-timing scientific CSV values match exactly. The local results remain descriptive, conditional on one reused UCI image panel, and do not test the primary W16 claim. See `stage_a_analysis.md` for separated observations, interpretation, and speculation, including source-relative harms hidden by seed averaging.
