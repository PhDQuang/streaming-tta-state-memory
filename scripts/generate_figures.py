"""Render static scientific figures from real recorded CSV/NPZ experiment files."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch
import numpy as np
import pandas as pd

from generate_tables import (ROOT, NO_RESET, PAIRED_METRICS, analysis_caption,
                             collapse_panels, intervention_effects, factorial_contrasts,
                             intervention_label, method_label, read_csv, require_completed,
                             file_sha256, analysis_fingerprints)

COLORS = ["#2468a2", "#d17620", "#2c8c6c", "#99558e", "#b24a4a", "#646b76"]


def style():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10,
                         "axes.spines.top": False, "axes.spines.right": False,
                         "axes.titlesize": 11, "axes.labelsize": 10,
                         "legend.frameon": False, "savefig.dpi": 250,
                         "pdf.fonttype": 42, "ps.fonttype": 42,
                         "svg.fonttype": "none", "axes.grid": True,
                         "grid.alpha": .18, "grid.linewidth": .6})


def save_figure(fig, output: Path, name: str, caption: str, metadata: dict, stage: str):
    footer = ("Protocol illustration; no empirical measurements" if name == "protocol_schematic" else
              f"Stage {stage} · all recorded source-training seeds and epochs" if name == "source_training" else
              f"Stage {stage} · descriptive recorded results · panels carry equal weight")
    if metadata.get("partial_import") and name != "protocol_schematic":
        footer = "PARTIAL IMPORT · completion/inventory unchecked · " + footer
    fig.text(.015, .012, footer,
             fontsize=8, color="#555555", ha="left")
    for extension in ("png", "pdf", "svg"):
        fig.savefig(output / f"{name}.{extension}", bbox_inches="tight", facecolor="white")
    plt.close(fig)
    metadata["figures"].append({"name": name, "caption": caption,
                                "files": [f"{name}.{ext}" for ext in ("png", "pdf", "svg")]})


def plot_disagreement(panels, output, metadata, stage, seed_panels=None):
    if panels.empty or "disagreement" not in panels:
        return
    selected = panels.loc[panels.intervention.isin(NO_RESET)]
    if selected.empty:
        metadata["skipped"].append("disagreement: no explicit no-reset condition")
        return
    use_seeds = stage.upper() == "A" and selected.panel_id.nunique() == 1 and seed_panels is not None
    individuals = seed_panels.loc[seed_panels.intervention.isin(NO_RESET)] if use_seeds else selected
    common_y_max = max(1., 110 * float(individuals.disagreement.max()))
    methods = sorted(selected.method.unique())
    fig, axes = plt.subplots(1, len(methods), figsize=(max(5, 4.3 * len(methods)), 3.6), squeeze=False)
    for k, method in enumerate(methods):
        ax = axes[0, k]
        data = selected.loc[selected.method.eq(method)]
        repeated = individuals.loc[individuals.method.eq(method)]
        for _, group in repeated.groupby(["panel_id", "seed"] if use_seeds else ["panel_id"]):
            group = group.sort_values("washout_batches")
            ax.plot(group.washout_batches, 100 * group.disagreement, color=COLORS[k % len(COLORS)],
                    alpha=.25, marker="o", markersize=3, linewidth=.75)
        mean = data.groupby("washout_batches").disagreement.mean().sort_index()
        ax.plot(mean.index, mean.values * 100, color=COLORS[k % len(COLORS)], marker="D",
                linewidth=2.1, markersize=5, label="Mean (shared panel)" if use_seeds else "Panel mean")
        ax.set(title=method_label(method), xlabel="Common-tail length (batches)",
               ylabel="AB–BA prediction disagreement (%)")
        ax.set_xticks(sorted(data.washout_batches.unique()))
        ax.set_ylim(0, common_y_max)
        ax.legend(fontsize=8)
    fig.suptitle("Residual history sensitivity after identical recent observations", y=1.03)
    fig.tight_layout(rect=(0, .05, 1, 1))
    save_figure(fig, output, "disagreement_washout",
                ("No external reset. Thin lines are descriptive seed repetitions on the same image panel; " if use_seeds else
                 "No external reset. Thin lines are individual panel means after averaging reused scenarios and seeds; ") +
                "diamonds average panels equally. Disagreement indicates different decisions, not necessarily worse accuracy. "
                "No interpolation-based recovery-time claim or statistical-significance claim is made.", metadata, stage)


def plot_state_effects(paired, output, metadata, stage):
    contrasts = intervention_effects(paired)
    if contrasts.empty:
        metadata["skipped"].append("state effects: matched no-reset/reset rows unavailable")
        return
    seed_panels, panels, _ = collapse_panels(contrasts, ["disagreement_change"])
    if panels.empty:
        return
    largest_w = panels.washout_batches.max()
    data = panels.loc[panels.washout_batches.eq(largest_w)]
    use_seeds = stage.upper() == "A" and data.panel_id.nunique() == 1
    if use_seeds:
        data = seed_panels.loc[seed_panels.washout_batches.eq(largest_w)]
    methods = sorted(data.method.unique())
    extent = max(.05, float(np.abs(data.disagreement_change.to_numpy()).max()) * 110)
    fig, axes = plt.subplots(len(methods), 1, figsize=(9.2, max(3.5, 2.8 * len(methods))), squeeze=False)
    for k, method in enumerate(methods):
        ax = axes[k, 0]
        group = data.loc[data.method.eq(method)]
        interventions = sorted(group.intervention.unique())
        for j, intervention in enumerate(interventions):
            values = group.loc[group.intervention.eq(intervention)].sort_values("panel_id").disagreement_change.to_numpy() * 100
            offsets = np.linspace(-.12, .12, len(values)) if len(values) > 1 else [0]
            ax.scatter(values, j + np.asarray(offsets), s=21, alpha=.42, color=COLORS[k % len(COLORS)])
            ax.scatter([values.mean()], [j], s=68, marker="D", color=COLORS[k % len(COLORS)], zorder=4)
        ax.axvline(0, color="#222222", linewidth=.9, linestyle="--")
        ax.set_yticks(range(len(interventions)), [intervention_label(x) for x in interventions])
        ax.set(title=f"{method_label(method)} · W={largest_w:g} batches",
               xlabel="Change in AB–BA disagreement versus no reset (percentage points)")
        ax.set_ylim(len(interventions) - .5, -.5)
        ax.set_xlim(-extent, extent)
    fig.suptitle("Effects of declared state interventions", y=1.01)
    fig.tight_layout(rect=(0, .04, 1, 1))
    save_figure(fig, output, "state_reset_effects",
                "Each contrast pairs the exact scenario/seed/panel/W with its no-reset reference before aggregation. " +
                ("Circles show seed repetitions on the shared panel and diamonds their mean. " if use_seeds else
                 "Circles show panels and diamonds their mean. ") +
                "Negative values reduce history disagreement; they do not "
                "establish improved accuracy or identify a unique cause. Auxiliary-state resets include exactly the components "
                "declared by the runner; unknown intervention identifiers are printed verbatim.", metadata, stage)


def plot_factorial(paired, output, metadata, stage):
    contrasts = factorial_contrasts(paired)
    if contrasts.empty:
        metadata["skipped"].append("factorial contrasts: no complete eight-cell P/O/aux trajectory")
        return
    seed_panels, panels, _ = collapse_panels(contrasts, ["disagreement_factorial"])
    w = panels.washout_batches.max()
    data = panels.loc[panels.washout_batches.eq(w)]
    use_seeds = stage.upper() == "A" and data.panel_id.nunique() == 1
    if use_seeds:
        data = seed_panels.loc[seed_panels.washout_batches.eq(w)]
    methods = sorted(data.method.unique())
    extent = max(.05, float(np.abs(data.disagreement_factorial.to_numpy()).max()) * 110)
    fig, axes = plt.subplots(len(methods), 1, figsize=(9.5, 3.3 * len(methods)), squeeze=False)
    terms = ["factorial:" + x for x in ["P", "O", "E", "PO", "PE", "OE", "POE"]]
    for k, method in enumerate(methods):
        ax = axes[k, 0]
        group = data.loc[data.method.eq(method)]
        for j, term in enumerate(terms):
            values = group.loc[group.intervention.eq(term)].disagreement_factorial.to_numpy() * 100
            if not len(values):
                continue
            offsets = np.linspace(-.12, .12, len(values)) if len(values) > 1 else [0]
            ax.scatter(values, j + np.asarray(offsets), alpha=.4, s=20, color=COLORS[k % len(COLORS)])
            ax.scatter([values.mean()], [j], marker="D", s=60, color=COLORS[k % len(COLORS)])
        ax.axvline(0, linestyle="--", color="#333333", linewidth=.8)
        ax.set_yticks(range(len(terms)), [intervention_label(x) for x in terms])
        ax.set_ylim(len(terms) - .5, -.5)
        ax.set_xlim(-extent, extent)
        ax.set(title=f"{method_label(method)} · W={w:g}", xlabel="Factorial contrast in history disagreement (percentage points)")
    fig.tight_layout(rect=(0, .04, 1, 1))
    save_figure(fig, output, "factorial_state_effects",
                "Complete P/O/aux factorial only, excluding the extra all-state/buffer reset. Main effects average over other "
                "reset factors; pair interactions average over the third factor; the three-state interaction is a difference "
                "of pair interactions. Contrasts are formed within scenario/seed/panel before aggregation. " +
                ("Circles are descriptive source-seed repetitions on the same image panel. " if use_seeds else "Circles are independent-design panel summaries, if the recorded design justifies that assumption. ") +
                "Diamonds show means. Auxiliary is EMA plus bookkeeping for SAR and bookkeeping for Tent; it is not labeled EMA-only. "
                "These response-scale contrasts are diagnostic and do not establish a unique causal state component.", metadata, stage)


def plot_training(training, output, metadata, stage):
    if training.empty or not {"seed", "epoch", "train_loss", "dev_accuracy"}.issubset(training):
        metadata["skipped"].append("training curves: recorded epoch data unavailable")
        return
    fig, axes = plt.subplots(1, 2, figsize=(8.5, 3.6))
    for i, (seed, group) in enumerate(training.groupby("seed")):
        group = group.sort_values("epoch")
        axes[0].plot(group.epoch, group.train_loss, color=COLORS[i % len(COLORS)], label=f"Seed {seed}")
        axes[1].plot(group.epoch, group.dev_accuracy * 100, color=COLORS[i % len(COLORS)], label=f"Seed {seed}")
    axes[0].set(xlabel="Epoch", ylabel="Training loss", title="Source model fitting")
    axes[1].set(xlabel="Epoch", ylabel="Development accuracy (%)", title="Internal development split")
    axes[1].set_ylim(0, 100)
    axes[1].legend(fontsize=8)
    fig.tight_layout(rect=(0, .05, 1, 1))
    save_figure(fig, output, "source_training",
                "Every recorded source-training epoch/seed is shown. The development split supports source fitting and "
                "does not constitute untouched benchmark evaluation. Curves do not report held-out test accuracy.", metadata, stage)


def prediction_path(raw: str, results: Path) -> Path | None:
    path = Path(str(raw))
    candidates = [path] if path.is_absolute() else [results / path, ROOT / path, results / "predictions" / path.name]
    return next((candidate for candidate in candidates if candidate.is_file()), None)


def load_prediction(path: Path) -> dict:
    with np.load(path, allow_pickle=False) as data:
        required = {"logits", "labels", "ids"}
        if not required.issubset(data.files):
            raise ValueError(f"Prediction archive missing fields: {path}")
        result = {key: data[key].copy() for key in required}
        if "images" in data:
            result["images"] = data["images"].copy()
    if result["logits"].ndim != 2 or not np.isfinite(result["logits"]).all():
        raise ValueError("Expected finite [N,C] logits")
    n = len(result["ids"])
    if any(len(result[key]) != n for key in result) or len(set(result["ids"].astype(str))) != n:
        raise ValueError("Prediction fields must align and IDs must be unique")
    return result


def outcome_examples(a: dict, b: dict, limit: int = 3) -> tuple[dict, dict]:
    """Use identical IDs/labels; first lexicographic IDs within all four groups."""
    ids_a, ids_b = a["ids"].astype(str), b["ids"].astype(str)
    if set(ids_a) != set(ids_b):
        raise ValueError("Qualitative comparisons require the same complete image-ID set")
    b_lookup = {identity: index for index, identity in enumerate(ids_b)}
    order_a = np.argsort(ids_a, kind="stable")
    order_b = np.asarray([b_lookup[ids_a[i]] for i in order_a])
    if not np.array_equal(a["labels"][order_a], b["labels"][order_b]):
        raise ValueError("Matched prediction IDs have different true labels")
    pred_a = a["logits"][order_a].argmax(1)
    pred_b = b["logits"][order_b].argmax(1)
    labels = a["labels"][order_a]
    correct_a, correct_b = pred_a == labels, pred_b == labels
    masks = {"Both correct": correct_a & correct_b, "A correct, B wrong": correct_a & ~correct_b,
             "A wrong, B correct": ~correct_a & correct_b, "Both wrong": ~correct_a & ~correct_b}
    groups, counts = {}, {}
    for label, mask in masks.items():
        indexes = np.flatnonzero(mask)
        counts[label] = int(len(indexes))
        groups[label] = [{"id": ids_a[order_a[i]], "label": int(labels[i]),
                          "prediction_a": int(pred_a[i]), "prediction_b": int(pred_b[i]),
                          "image_index_a": int(order_a[i]), "image_index_b": int(order_b[i])}
                         for i in indexes[:limit]]
    return groups, counts


def candidate_prediction_pairs(runs: pd.DataFrame):
    if runs.empty or "prediction_file" not in runs or "intervention" not in runs:
        return []
    data = runs.loc[runs.prediction_file.notna() & runs.intervention.isin(NO_RESET)].copy()
    sort_columns = [k for k in ["seed", "panel_id", "scenario", "washout_batches", "direction", "method"] if k in data]
    data = data.sort_values(sort_columns)
    match_keys = [k for k in ["experiment_id", "seed", "panel_id", "scenario", "washout_batches", "direction"] if k in data]
    candidates = []
    source = data.loc[data.method.eq("source")]
    for _, adapted in data.loc[~data.method.isin(["source", "norm"])].iterrows():
        matches = source
        for key in match_keys:
            matches = matches.loc[matches[key].eq(adapted[key])]
        if not matches.empty:
            baseline = matches.iloc[0]
            candidates.append((baseline, adapted, "Source", method_label(adapted.method) + " / no reset"))
    if "direction" in data:
        for _, row in data.loc[data.direction.astype(str).str.upper().eq("AB") & ~data.method.eq("source")].iterrows():
            other = data.loc[data.direction.astype(str).str.upper().eq("BA")]
            for key in [k for k in match_keys if k != "direction"] + ["method"]:
                other = other.loc[other[key].eq(row[key])]
            if not other.empty:
                candidates.append((row, other.iloc[0], method_label(row.method) + " / AB", method_label(row.method) + " / BA"))
    return candidates


def plot_outcomes(runs, results, output, metadata, stage):
    selected = None
    for row_a, row_b, name_a, name_b in candidate_prediction_pairs(runs):
        path_a, path_b = prediction_path(row_a.prediction_file, results), prediction_path(row_b.prediction_file, results)
        if not path_a or not path_b:
            continue
        a, b = load_prediction(path_a), load_prediction(path_b)
        if "images" not in a and "images" not in b:
            continue
        groups, counts = outcome_examples(a, b)
        selected = a, b, groups, counts, name_a, name_b, row_a, row_b
        break
    if selected is None:
        metadata["skipped"].append("qualitative outcomes: no matched pair with recorded images")
        return
    a, b, groups, counts, name_a, name_b, row_a, row_b = selected
    fig, axes = plt.subplots(4, 3, figsize=(9, 10.5), squeeze=False)
    for r, (label, examples) in enumerate(groups.items()):
        for c, ax in enumerate(axes[r]):
            ax.grid(False)
            ax.set_xticks([])
            ax.set_yticks([])
            if c < len(examples):
                item = examples[c]
                source, image_key = (a, "image_index_a") if "images" in a else (b, "image_index_b")
                image = source["images"][item[image_key]]
                if image.ndim == 3 and image.shape[0] in (1, 3):
                    image = np.moveaxis(image, 0, -1)
                if image.ndim == 3 and image.shape[-1] == 1:
                    image = image[..., 0]
                if image.ndim == 2:
                    ax.imshow(image, cmap="gray", interpolation="nearest", vmin=0, vmax=1)
                else:
                    ax.imshow(np.clip(image, 0, 1))
                identity = item["id"]
                if len(identity) > 32:
                    identity = identity[:13] + "…" + identity[-16:]
                ax.set_title(f"{identity}\ny={item['label']} · A={item['prediction_a']} · B={item['prediction_b']}", fontsize=8)
            else:
                ax.text(.5, .5, "No further examples", ha="center", va="center", color="#777777")
                ax.set_xlim(0, 1)
                ax.set_ylim(0, 1)
            if c == 0:
                ax.set_ylabel(f"{label}\n(n={counts[label]})", fontsize=10, labelpad=9)
    fig.suptitle(f"Recorded outcome groups\nA: {name_a}   |   B: {name_b}", fontsize=12, y=1.005)
    fig.tight_layout(rect=(0, .035, 1, .97))
    manifest = {"comparison_a": name_a, "comparison_b": name_b,
                "prediction_file_a": str(row_a.prediction_file), "prediction_file_b": str(row_b.prediction_file),
                "prediction_sha256_a": file_sha256(path_a), "prediction_sha256_b": file_sha256(path_b),
                "selection": "First eligible recorded run pair in sorted identifiers; first lexicographic image IDs in each outcome group",
                "counts": counts, "examples": groups}
    (output / "outcome_examples.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    save_figure(fig, output, "outcome_groups",
                "A and B are identified in the figure; this may be source versus adaptation or AB versus BA, never mislabeled. "
                "All four correctness groups are displayed, including empty groups. The first eligible sorted run pair and "
                "first lexicographic IDs within each group determine examples without performance-based selection. "
                "The JSON manifest preserves full image IDs and counts. Images are recorded local normalized inputs.", metadata, stage)


def plot_schematic(output, metadata, stage):
    fig, ax = plt.subplots(figsize=(10.5, 3.25))
    ax.set_xlim(0, 11)
    ax.set_ylim(-.6, 2.1)
    ax.axis("off")
    def box(x, y, w, text, color):
        ax.add_patch(FancyBboxPatch((x, y), w, .52, boxstyle="round,pad=0.06", facecolor=color, edgecolor="white"))
        ax.text(x + w / 2, y + .26, text, va="center", ha="center", fontsize=10)
    for y, first, second in [(1.12, "A", "B"), (.22, "B", "A")]:
        box(.05, y, 1.15, "Same source", "#e3e8ee")
        box(1.65, y, .9, first, "#bcd7e9" if first == "A" else "#f1d8bc")
        box(2.75, y, .9, second, "#bcd7e9" if second == "A" else "#f1d8bc")
        box(4.12, y, 1.72, "Identical W", "#c9e4d9")
        box(6.3, y, 1.75, "State intervention", "#e3d5eb")
        box(8.52, y, 2.3, "Identical disjoint Q", "#e3e8ee")
        for x1, x2 in [(1.21, 1.6), (3.7, 4.06), (5.9, 6.23), (8.11, 8.45)]:
            ax.add_patch(FancyArrowPatch((x1, y + .26), (x2, y + .26), arrowstyle="->", mutation_scale=12, color="#59636b"))
    ax.text(2.64, -.08, "Same immutable prefix-batch multiset", ha="center", fontsize=9)
    ax.text(9.64, -.08, "Predict before each batch update", ha="center", fontsize=9)
    ax.text(5.5, 1.92, "Matched histories, shared recent observations, and shared future", ha="center", fontsize=13)
    fig.tight_layout(rect=(0, .035, 1, 1))
    save_figure(fig, output, "protocol_schematic",
                "Experimental protocol schematic, not measured data. Prefixes differ only in immutable-batch block order; "
                "H/W/Q are disjoint by original identity. Common-tail length and intervention are recorded conditions. "
                "The intervention occurs after W and before pre-update Q prediction.", metadata, stage)


def generate_figures(results: Path, output: Path | None = None, stage: str = "A", *, allow_partial: bool = False) -> dict:
    results = results.resolve()
    if not results.is_dir():
        raise FileNotFoundError(f"Results directory does not exist: {results}")
    require_completed(results, allow_partial)
    output = (output or ROOT / "figures" / results.name).resolve()
    output.mkdir(parents=True, exist_ok=True)
    style()
    metadata = {"results": str(results), "stage": stage, "scope": analysis_caption(stage),
                "figures": [], "skipped": [], "partial_import": allow_partial, **analysis_fingerprints(results)}
    if allow_partial:
        metadata["scope"] = "EXPLICIT PARTIAL IMPORT: completion and frozen inventory unchecked; descriptive exploration only. " + metadata["scope"]
    paired, runs, training = [read_csv(results / name) for name in ("paired.csv", "runs.csv", "training.csv")]
    if not paired.empty:
        seed_panels, panels, _ = collapse_panels(paired, PAIRED_METRICS)
        plot_disagreement(panels, output, metadata, stage, seed_panels)
        plot_state_effects(paired, output, metadata, stage)
        plot_factorial(paired, output, metadata, stage)
    else:
        metadata["skipped"].append("paired plots: no recorded paired rows")
    plot_training(training, output, metadata, stage)
    plot_outcomes(runs, results, output, metadata, stage)
    plot_schematic(output, metadata, stage)
    (output / "figure_manifest.json").write_text(json.dumps(metadata, indent=2), encoding="utf-8")
    captions = [f"# Figures: {results.name}", metadata["scope"]]
    for figure in metadata["figures"]:
        captions.extend([f"## {figure['name']}", figure["caption"], f"![{figure['name']}]({figure['name']}.png)"])
    if metadata["skipped"]:
        captions.extend(["## Missing inputs", "\n".join(f"- {item}" for item in metadata["skipped"])])
    (output / "captions.md").write_text("\n\n".join(captions) + "\n", encoding="utf-8")
    return metadata


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--results", type=Path, required=True)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--stage", default="A", help="Caption only; default A")
    parser.add_argument("--allow-partial-import", action="store_true", help="Explicit exploratory import bypassing strict completion/inventory requirements")
    args = parser.parse_args()
    print(json.dumps(generate_figures(args.results, args.output, args.stage, allow_partial=args.allow_partial_import), indent=2))


if __name__ == "__main__":
    main()
