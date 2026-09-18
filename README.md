# What Does Adaptation Remember?

Controlled history and state interventions in streaming vision. This repository contains a research investigation, a working experiment harness, and real **local sanity results**. It is not a completed ImageNet study or a publication-ready empirical claim. No paid GPU has been rented or used.

The central question is whether two permutations of the same historical image batches still change predictions on an identical unseen future after a shared recent tail. Parameter, optimizer and auxiliary-state resets probe that dependence. The proposal explicitly allows a negative result.

## Read first

- [Current status](research/status.md), [proposal](research/proposal.md), [costed GPU request](research/cloud_gpu_request.md).
- [Literature review](research/literature_review.md), [nine candidates and decision matrix](research/topic_candidates.md), [top-three novelty audit](research/novelty_analysis.md), [66-entry bibliography](research/references.bib).
- [Actual Stage A analysis](research/stage_a_analysis.md), [manuscript draft](paper/paper.md), [skeptical review](research/reviewer_audit.md), [response and remaining blockers](research/reviewer_response.md).
- [Experiment log](research/research_log.md), [baseline semantics](research/baseline_implementation.md), [data preparation](research/data_preparation.md).

## Environment

For a free exploratory ImageNet-C run on Kaggle, use [the Kaggle notebook](notebooks/kaggle_stage_b_preliminary.ipynb), [preliminary config](configs/kaggle_preliminary.yaml), and [Vietnamese setup guide](research/kaggle_preliminary.md). This separate one-panel experiment keeps W16 and tests none/all resets; it is not the full cloud pilot or a confirmatory study.

For the attached 200-class 64x64 Tiny ImageNet-C mirror, use [the Tiny notebook](notebooks/kaggle_tiny_imagenetc_preliminary.ipynb) and [Tiny setup guide](research/kaggle_tiny_preliminary.md). Its separate experiment projects ImageNet-pretrained ResNet50 to the dataset's 200 synsets; no Tiny-trained source baseline or ImageNet-C Stage B result is claimed.

Recorded local environment: Python 3.10.0, PyTorch 2.9.1+cpu, torchvision 0.24.1+cpu, Windows 11, Intel i5-1145G7, 31.7 GiB RAM, no CUDA GPU. Existing packages were used; no large local dataset was downloaded. See [audit](research/environment.md).

For a fresh CPU environment, create a virtual environment, activate it, and run:

```text
python -m pip install torch==2.9.1 torchvision==0.24.1 --index-url https://download.pytorch.org/whl/cpu
python -m pip install -r requirements.txt
python -m pip install --no-deps -e .
```

On an approved Linux CUDA 12.8-compatible machine, replace the first command with:

```text
python -m pip install torch==2.9.1 torchvision==0.24.1 --index-url https://download.pytorch.org/whl/cu128
```

These version-specific wheel commands follow the [official PyTorch previous-version instructions](https://pytorch.org/get-started/previous-versions/#v2-9-1), verified 2026-09-08. Driver compatibility must be checked on the selected host. Pinning records the tested software, rather than claiming it is the newest release.

## Reproduce the free local stage

Run commands from the repository root. Download uses only the original UCI **training** file (about 0.56 MB extracted). The official test file is not extracted or used.

```text
python scripts/download_data.py uci-train
python -m pytest -q
python scripts/run_sanity.py --config configs/sanity_v2.yaml
python scripts/evaluate.py --results results/stage_a_uci_v2
python scripts/generate_tables.py --results results/stage_a_uci_v2 --stage A
python scripts/generate_figures.py --results results/stage_a_uci_v2 --stage A
python scripts/build_paper.py --results results/stage_a_uci_v2
```

The completed output already exists in this workspace. The runner deliberately refuses to overwrite it. To repeat training, copy the YAML and change both `experiment_id` and `output`; retain the seeds, split and settings. `run_all_experiments.py --run --reuse-existing` audits and analyzes an existing matching completed Stage A run; without `--run` it prints a plan. It never starts a paid stage.

Additional actual code audit and faithful baseline comparison:

```text
python scripts/audit_upstream_sar.py
python scripts/compare_sar_recovery.py --stage-a results/stage_a_uci_v2 --output results/stage_a_sar_recovery_comparison_replay
```

The original reference code and licenses are preserved under `third_party/sar_reference`. `sar_complete` is deliberately named separately from faithful upstream SAR. No claim is made that published benchmark accuracy has been reproduced.

The recorded original fidelity comparison used v1 source records. The command above uses the reproduced v2 sources and a new output ID, so it can also run after a fresh Stage A reproduction. Source checkpoints are intentionally excluded from Git; reproduce training to reconstruct them. Saved checkpoint records use absolute paths on the producing machine.

The complete [LaTeX source](paper/paper.tex) is reproducible with `python scripts/export_latex.py` after rebuilding the Markdown manuscript. All sections, three tables and two figures are retained. LuaLaTeX compilation/layout has **not** been verified because no TeX engine is installed; no compiled manuscript PDF is claimed. The six individual scientific figures are available as verified PDF/SVG/PNG assets.

## Cloud pilot — prepared, awaiting explicit budget approval

```text
python scripts/run_cloud_pilot.py --config configs/cloud_pilot.yaml
python scripts/download_data.py imagenet-c
```

Both commands are plan-only by default. After approval, provision one 24 GB GPU with 120 GB temporary storage and establish provider billing shutdown before launching. Then follow [the executable shell sequence](scripts/cloud_pilot.sh). It downloads the three released archive groups, extracts only severity-5 pilot IDs for the three selected corruptions, pins class mapping and image hashes, freezes manifests, and executes the configured pilot. No script rents hardware, reads payment credentials or calls a billing API. `timeout` and the Python process limit stop computation; **neither terminates provider billing**. Export artifacts and terminate the rented instance/storage within the approved ceiling.

The pilot has 3 disjoint image panels, 3 reused scenarios per panel, 4 methods, 3 common-tail lengths, and 9 intervention arms for adaptive methods (2 controls each for source and norm). This yields 594 paired / 1,188 directional suffix runs. Three panels estimate engineering behavior and variance; they do not justify a definitive significance or equivalence claim.

## Protocol contract

- Form batches once. AB and BA contain exactly the same batches and image realizations. Original IDs are disjoint across prefix, common tail and suffix.
- Use the final k batches of a fixed maximum common tail. Intervene after prefix + tail, before the unseen suffix.
- Predict from the first forward pass before that batch's parameter update. Batch statistics may use the current unlabeled batch. Adapter APIs receive images, never target labels.
- Use matched per-batch random draws (`batch_crn_v1`) across orders, methods and interventions, keyed to seed, panel, stream role and image keys. This version includes absolute paths: stochastic bitwise replay after relocating the dataset requires preserved paths; a path-independent key needs a new protocol version. This controls external randomness; natural RNG-history carryover is not the estimand.
- Save all parameters, forward state, optimizer state including nested SGD momentum, auxiliary state and RNG. Preserve the immutable source anchor. Full reset must agree with the same freshly initialized adapter on Q.
- Infer population uncertainty from independent image panels, not repeated scenarios, correlated Q images, interventions or source seeds sharing the same panel.

## Artifacts and limits

`src/historytta` implements data, streams, models, adapters, paired execution and metrics. `configs` fixes experiments; `scripts` downloads, prepares, runs, audits and analyzes. `results/<id>` preserves manifests, configurations/provenance, raw logits/labels/IDs, traces, CSVs, controls and status; model/junction checkpoints are retained locally but excluded from Git. `figures/<id>` contains visually checked PNG/PDF/SVG figures and captions. `research` contains evidence and decisions; `paper` contains the honest current manuscript draft.

The final verification suite passed **126 tests, with one Windows symlink-privilege skip**. Stage A v2 produced 528 directional trajectories, 264 comparisons and 408 passing controls in about 145 seconds. Only two no-reset comparisons differed, each on 1 of 512 future decisions (0.1953 percentage point). Source-training seeds share one image panel: their SD is descriptive, not independent-panel uncertainty. Adaptation sometimes harms accuracy or NLL. These observations neither support the prespecified large-benchmark persistence hypothesis nor establish practical equivalence.

The confirmation study still requires independent panels, stronger recent baselines, frozen-versus-adapting suffix controls, momentum ablations, component swaps, a second backbone and a second dataset. Their absence is explicitly recorded as a reason the current draft would be rejected as a completed paper.
