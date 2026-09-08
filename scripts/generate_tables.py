"""Generate descriptive research tables from recorded experiments, never invented data.

Scenarios are repeated conditions within panels. Seeds are averaged within a
globally unique panel_id before panel uncertainty is computed. No p-values.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import warnings

import numpy as np
import pandas as pd
from scipy import stats
from evaluate import validate_inventory

ROOT = Path(__file__).resolve().parents[1]
CONDITIONS = ["experiment_id", "method", "intervention", "washout_batches"]
PAIRED_METRICS = ["disagreement", "accuracy_ab", "accuracy_ba", "signed_error_gap",
                  "absolute_error_gap", "nll_gap", "brier_gap", "first_batch_max_logit_diff"]
RUN_METRICS = ["accuracy", "nll", "brier", "ece15", "seconds", "updates", "skipped", "recoveries"]
LABELS = {
    "none": "No external reset", "no_reset": "No external reset",
    "parameters": "Reset parameters only", "reset_parameters": "Reset parameters only",
    "optimizer": "Reset optimizer only", "reset_optimizer": "Reset optimizer only",
    "aux": "Reset auxiliary state only", "reset_aux": "Reset auxiliary state only",
    "all": "Reset all declared state", "all_reset": "Reset all declared state",
    "parameters_optimizer": "Reset parameters + optimizer",
    "reset_parameters_optimizer": "Reset parameters + optimizer",
    "parameters+optimizer": "Reset parameters + optimizer",
    "parameters_aux": "Reset parameters + auxiliary state",
    "optimizer_aux": "Reset optimizer + auxiliary state",
    "parameters_optimizer_aux": "Reset parameters + optimizer + auxiliary state",
    "factorial:P": "Parameters: marginal reset effect",
    "factorial:O": "Optimizer: marginal reset effect",
    "factorial:E": "Auxiliary: marginal reset effect",
    "factorial:PO": "Parameters × optimizer interaction",
    "factorial:PE": "Parameters × auxiliary interaction",
    "factorial:OE": "Optimizer × auxiliary interaction",
    "factorial:POE": "Three-state interaction",
}
METHOD_LABELS = {"source": "Source", "norm": "Normalization only", "tent": "Tent",
                 "sar_complete": "SAR (complete-state implementation)", "sar": "SAR"}
NO_RESET = {"none", "no_reset"}


def intervention_label(value: str) -> str:
    """Unknown identifiers stay explicit rather than receiving guessed semantics."""
    return LABELS.get(str(value), str(value))


def method_label(value: str) -> str:
    return METHOD_LABELS.get(str(value), str(value))


def read_csv(path: Path) -> pd.DataFrame:
    if not path.exists() or not path.stat().st_size:
        return pd.DataFrame()
    try:
        frame = pd.read_csv(path, dtype={"seed": "string", "panel_id": "string"})
    except pd.errors.EmptyDataError:
        return pd.DataFrame()
    return frame


def require_completed(results: Path, allow_partial: bool = False):
    if allow_partial:
        warnings.warn("Explicit partial import: completion and planned-inventory checks bypassed; descriptive exploration only.")
        return
    status_path = results / "run_status.json"
    if not status_path.is_file():
        raise RuntimeError("Missing mandatory run_status.json; strict analysis requires completed, inventoried results")
    status = json.loads(status_path.read_text(encoding="utf-8"))
    if status.get("status") != "complete":
        raise RuntimeError(f"Refusing analysis of an unfinished experiment: {status.get('status')}")
    failures = validate_inventory(results)
    if failures:
        raise RuntimeError("Incomplete or mismatched frozen experiment inventory: " + "; ".join(failures[:8]))


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def analysis_fingerprints(results: Path) -> dict:
    return {"analysis_script_sha256": {name: file_sha256(ROOT / "scripts" / name)
                                      for name in ["generate_tables.py", "generate_figures.py", "evaluate.py"]},
            "input_sha256": {name: file_sha256(results / name)
                             for name in ["paired.csv", "runs.csv", "training.csv", "controls.json", "run_status.json"]
                             if (results / name).is_file()}}


def collapse_panels(frame: pd.DataFrame, metrics: list[str], *, runs: bool = False
                    ) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """Equal-weight scenarios within seed/panel, then seeds within panel.

The returned long summary counts panels, not scenarios or seed runs. Intervals
are descriptive t intervals conditional on the supplied panel design. The caller
must substantiate independent panels before making inferential claims.
"""
    if frame.empty:
        return pd.DataFrame(), pd.DataFrame(), pd.DataFrame()
    conditions = CONDITIONS + (["direction"] if runs else [])
    required = conditions + ["seed", "panel_id", "scenario"]
    missing = set(required) - set(frame)
    if missing:
        raise ValueError(f"Missing aggregation identifiers: {sorted(missing)}")
    if frame[required].isna().any().any():
        raise ValueError("Aggregation identifiers must not be missing")
    if frame.duplicated(required).any():
        raise ValueError("Duplicate run/paired identifiers would overweight a trajectory")
    values = [name for name in metrics if name in frame]
    if not values:
        return pd.DataFrame(), pd.DataFrame(), pd.DataFrame()
    work = frame.copy()
    for metric in values:
        work[metric] = pd.to_numeric(work[metric], errors="raise")
        if np.isinf(work[metric].to_numpy(dtype=float)).any():
            raise ValueError(f"Non-finite recorded metric: {metric}")
    seed_keys = conditions + ["seed", "panel_id"]
    seed_panels = work.groupby(seed_keys, dropna=False, sort=True)[values].mean().reset_index()
    counts = work.groupby(seed_keys, dropna=False)["scenario"].nunique().rename("n_scenarios").reset_index()
    seed_panels = seed_panels.merge(counts, on=seed_keys, validate="one_to_one")
    for _, group in work.groupby(conditions, dropna=False):
        inventories = group.groupby(["seed", "panel_id"])["scenario"].agg(lambda x: tuple(sorted(x)))
        if inventories.nunique() > 1:
            warnings.warn("Scenario inventories differ across panels/seeds; available-condition means are descriptive.")
    panel_keys = conditions + ["panel_id"]
    panels = seed_panels.groupby(panel_keys, dropna=False, sort=True)[values].mean().reset_index()
    counts = seed_panels.groupby(panel_keys, dropna=False).agg(
        n_seeds=("seed", "nunique"), n_scenarios_min=("n_scenarios", "min"),
        n_scenarios_max=("n_scenarios", "max")).reset_index()
    panels = panels.merge(counts, on=panel_keys, validate="one_to_one")
    records = []
    for identity, group in panels.groupby(conditions, dropna=False, sort=True):
        identity = identity if isinstance(identity, tuple) else (identity,)
        base = dict(zip(conditions, identity))
        for metric in values:
            valid = group.loc[group[metric].notna()]
            numbers = valid[metric].to_numpy(dtype=float)
            if not len(numbers):
                continue
            mean = float(numbers.mean())
            sd = float(numbers.std(ddof=1)) if len(numbers) > 1 else np.nan
            half = float(stats.t.ppf(.975, len(numbers) - 1) * sd / np.sqrt(len(numbers))) if len(numbers) > 1 else np.nan
            records.append({**base, "metric": metric, "n_panels": len(numbers), "mean": mean,
                            "sd": sd, "ci95_low": mean - half, "ci95_high": mean + half,
                            "n_seeds_min": int(valid.n_seeds.min()),
                            "n_seeds_max": int(valid.n_seeds.max()),
                            "individual_panels": json.dumps(dict(zip(valid.panel_id.astype(str), numbers)), sort_keys=True),
                            "interval_type": "descriptive panel t interval; design-conditional"})
    return seed_panels, panels, pd.DataFrame(records)


def markdown_table(frame: pd.DataFrame) -> str:
    if frame.empty:
        return "No recorded data available.\n"
    def cell(value):
        if isinstance(value, (float, np.floating)):
            return "—" if not np.isfinite(value) else f"{value:.6g}"
        return str(value).replace("|", "\\|").replace("\n", " ")
    rows = ["| " + " | ".join(map(str, frame.columns)) + " |",
            "| " + " | ".join(["---"] * len(frame.columns)) + " |"]
    rows.extend("| " + " | ".join(cell(x) for x in row) + " |" for row in frame.itertuples(index=False, name=None))
    return "\n".join(rows) + "\n"


def intervention_effects(frame: pd.DataFrame) -> pd.DataFrame:
    """Within-scenario paired reset contrasts, before any scenario/seed collapse."""
    if frame.empty or "intervention" not in frame:
        return pd.DataFrame()
    metrics = [m for m in ["disagreement", "absolute_error_gap", "nll_gap", "brier_gap"] if m in frame]
    keys = ["experiment_id", "seed", "panel_id", "scenario", "method", "washout_batches"]
    baseline = frame.loc[frame.intervention.isin(NO_RESET), keys + metrics]
    if baseline.empty:
        return pd.DataFrame()
    if baseline.duplicated(keys).any():
        raise ValueError("Multiple no-reset references for one state contrast")
    treatments = frame.loc[~frame.intervention.isin(NO_RESET)]
    joined = treatments.merge(baseline, on=keys, how="inner", suffixes=("", "_reference"), validate="many_to_one")
    if joined.empty:
        return pd.DataFrame()
    output = joined[keys + ["intervention"]].copy()
    for metric in metrics:
        output[metric + "_change"] = joined[metric] - joined[metric + "_reference"]
    return output


def performance_reference_effects(frame: pd.DataFrame, reference_method: str | None) -> pd.DataFrame:
    """Compare each run with its exact matched no-reset performance reference.

If reference_method is None, compare reset interventions against no reset within
the same method. Positive error/NLL/Brier/ECE changes indicate reference-relative
harm on this recorded Q; they are distinct from AB/BA history sensitivity.
"""
    if frame.empty or not {"method", "intervention"}.issubset(frame):
        return pd.DataFrame()
    metrics = [m for m in ["accuracy", "nll", "brier", "ece15"] if m in frame]
    keys = ["experiment_id", "seed", "panel_id", "scenario", "washout_batches", "direction"]
    if reference_method is None:
        keys += ["method"]
        reference = frame.loc[frame.intervention.isin(NO_RESET)]
        treatments = frame.loc[~frame.intervention.isin(NO_RESET)]
    else:
        reference = frame.loc[frame.method.eq(reference_method) & frame.intervention.isin(NO_RESET)]
        treatments = frame.loc[~frame.method.eq(reference_method)]
    if reference.empty or treatments.empty or not metrics:
        return pd.DataFrame()
    if reference.duplicated(keys).any():
        raise ValueError("Multiple no-reset performance references for one trajectory")
    joined = treatments.merge(reference[keys + metrics], on=keys, how="inner",
                              suffixes=("", "_reference"), validate="many_to_one")
    identity = list(dict.fromkeys(keys + ["method", "intervention"]))
    output = joined[identity].copy()
    for metric in metrics:
        output[metric + "_change"] = joined[metric] - joined[metric + "_reference"]
    if "accuracy" in metrics:
        output["error_change"] = -output["accuracy_change"]
    return output


def describe_seed_variation(seed_panels: pd.DataFrame, metrics: list[str], *, runs: bool = False) -> pd.DataFrame:
    """Descriptive source/algorithm seed variability, never independent-panel CIs."""
    if seed_panels.empty:
        return pd.DataFrame()
    conditions = CONDITIONS + (["direction"] if runs else []) + ["panel_id"]
    records = []
    for identity, group in seed_panels.groupby(conditions, sort=True, dropna=False):
        base = dict(zip(conditions, identity))
        for metric in [m for m in metrics if m in group]:
            valid = group.loc[group[metric].notna()]
            values = valid[metric].to_numpy(dtype=float)
            if len(values):
                records.append({**base, "metric": metric, "n_seeds": len(values),
                                "mean": float(values.mean()),
                                "seed_sd_descriptive": float(values.std(ddof=1)) if len(values) > 1 else np.nan,
                                "individual_seeds": json.dumps(dict(zip(valid.seed.astype(str), values)), sort_keys=True),
                                "scope": "same-panel seed variability; no CI or independence claim"})
    return pd.DataFrame(records)


def factorial_contrasts(frame: pd.DataFrame) -> pd.DataFrame:
    """Complete 2^3 P/O/aux contrasts per exact trajectory; never impute cells.

Main effects average over the other two states; two-state interactions average
over the third state. 'all' resets extra buffers and is not a factorial cell.
"""
    if frame.empty:
        return pd.DataFrame()
    cells = {"none": (0, 0, 0), "parameters": (1, 0, 0), "optimizer": (0, 1, 0),
             "parameters_optimizer": (1, 1, 0), "aux": (0, 0, 1),
             "parameters_aux": (1, 0, 1), "optimizer_aux": (0, 1, 1),
             "parameters_optimizer_aux": (1, 1, 1)}
    metrics = [m for m in ["disagreement", "absolute_error_gap", "nll_gap", "brier_gap"] if m in frame]
    keys = ["experiment_id", "seed", "panel_id", "scenario", "method", "washout_batches"]
    records = []
    for identity, group in frame.loc[frame.intervention.isin(cells)].groupby(keys, sort=True, dropna=False):
        if group.intervention.duplicated().any():
            raise ValueError("Duplicate factorial cell")
        if set(group.intervention) != set(cells):
            continue
        by_cell = group.set_index("intervention")
        for term, axes in [("P", (0,)), ("O", (1,)), ("E", (2,)),
                           ("PO", (0, 1)), ("PE", (0, 2)), ("OE", (1, 2)), ("POE", (0, 1, 2))]:
            record = dict(zip(keys, identity))
            record["intervention"] = "factorial:" + term
            for metric in metrics:
                values = by_cell[metric]
                record[metric + "_factorial"] = (sum(np.prod([2 * levels[i] - 1 for i in axes]) * values[name]
                                                     for name, levels in cells.items()) / 2 ** (3 - len(axes)))
            records.append(record)
    return pd.DataFrame(records)


def analysis_caption(stage: str) -> str:
    prefix = "Stage A: descriptive correctness/sanity results only." if stage.upper() == "A" else f"Stage {stage}: recorded experiment results."
    return (prefix + " Scenarios are averaged within each seed/panel, then repeated seeds within panel_id; "
            "each panel receives equal weight. SD and 95% t intervals describe variation across the supplied panel IDs, "
            "conditional on this dataset, model, and stream construction. Tiny local samples and three seeds cannot establish "
            "population generalization. Shared-image scenarios, suffix batches, and repeated seeds are not counted as independent "
            "panels. No p-values or statistical-superiority claims are generated. Metrics remain in raw units: accuracy/error "
            "fractions, NLL in nats/example; absolute gaps are finite-panel magnitudes, not unbiased absolute population effects.")


def generate_tables(results: Path, output: Path | None = None, stage: str = "A", *, allow_partial: bool = False) -> dict:
    results = results.resolve()
    if not results.is_dir():
        raise FileNotFoundError(f"Results directory does not exist: {results}")
    require_completed(results, allow_partial)
    output = (output or results / "tables").resolve()
    output.mkdir(parents=True, exist_ok=True)
    caption = analysis_caption(stage)
    if allow_partial:
        caption = "EXPLICIT PARTIAL IMPORT: completion and frozen inventory unchecked; descriptive exploration only. " + caption
    sections = [f"# Recorded results: {results.name}", caption]
    generated = []
    paired = read_csv(results / "paired.csv")
    runs = read_csv(results / "runs.csv")
    effects = intervention_effects(paired)
    factorial = factorial_contrasts(paired)
    sources = [("paired", paired, PAIRED_METRICS, False),
               ("runs", runs, RUN_METRICS, True),
               ("reset_effects", effects, [m + "_change" for m in ["disagreement", "absolute_error_gap", "nll_gap", "brier_gap"]], False),
               ("factorial", factorial, [m + "_factorial" for m in ["disagreement", "absolute_error_gap", "nll_gap", "brier_gap"]], False)]
    for name, reference_method in [("source_reference", "source"), ("norm_reference", "norm"),
                                   ("performance_reset_effects", None)]:
        contrast = performance_reference_effects(runs, reference_method)
        sources.append((name, contrast, [m + "_change" for m in ["accuracy", "error", "nll", "brier", "ece15"]], True))
        if not contrast.empty:
            contrast.to_csv(output / f"{name}_matched_rows.csv", index=False)
            generated.append(f"{name}_matched_rows.csv")
    sections.append("Performance-reference tables pair the exact seed, panel, scenario, W, and direction before aggregation. "
                    "source_reference compares with source/no reset; norm_reference compares with normalization-only/no reset; "
                    "performance_reset_effects compares each reset with the same method/no reset. Positive error_change, "
                    "nll_change, brier_change, or ece15_change means worse recorded performance than that reference; "
                    "positive accuracy_change means better accuracy. These are distinct from AB/BA history disagreement.")
    for name, frame, metrics, is_runs in sources:
        seed_panels, panels, summary = collapse_panels(frame, metrics, runs=is_runs)
        if summary.empty:
            sections.extend([f"## {name}", "No recorded rows available; no values have been synthesized."])
            continue
        seed_description = describe_seed_variation(seed_panels, metrics, runs=is_runs)
        for suffix, table in [("seed_panels", seed_panels), ("panels", panels), ("summary", summary),
                              ("seed_descriptive", seed_description)]:
            filename = f"{name}_{suffix}.csv"
            table.to_csv(output / filename, index=False)
            generated.append(filename)
        display = summary.copy()
        display["method"] = display["method"].map(method_label)
        display["intervention"] = display["intervention"].map(intervention_label)
        display = display.drop(columns=["experiment_id", "interval_type"], errors="ignore")
        sections.extend([f"## {name}", markdown_table(display)])
        if stage.upper() == "A":
            seed_display = seed_description.drop(columns=["experiment_id", "scope"], errors="ignore").copy()
            seed_display["method"] = seed_display["method"].map(method_label)
            seed_display["intervention"] = seed_display["intervention"].map(intervention_label)
            sections.extend([f"### {name}: descriptive seed repetitions",
                             "The same image panel is reused across seeds. These standard deviations describe seed variability only; no confidence interval is justified from treating seeds as new image panels.",
                             markdown_table(seed_display)])
    controls_file = results / "controls.json"
    if not controls_file.exists():
        controls_file = results / "Controls.json"
    if controls_file.exists():
        controls = json.loads(controls_file.read_text(encoding="utf-8"))
        if isinstance(controls, dict):
            controls = controls.get("controls", [controls])
        table = pd.json_normalize(controls)
        table.to_csv(output / "controls.csv", index=False)
        generated.append("controls.csv")
        sections.extend(["## Deterministic controls", markdown_table(table)])
    training = read_csv(results / "training.csv")
    if not training.empty:
        training.to_csv(output / "training_recorded.csv", index=False)
        generated.append("training_recorded.csv")
        sections.extend(["## Source training", "Complete recorded epochs and seeds are retained in training_recorded.csv. "
                         "Development accuracy is not a locked-test benchmark result."])
    (output / "tables.md").write_text("\n\n".join(sections) + "\n", encoding="utf-8")
    metadata = {"results": str(results), "stage": stage, "caption": caption,
                "aggregation": "mean scenarios -> mean repeated seeds -> equal panel summary",
                "pvalues_computed": False, "partial_import": allow_partial, "generated": generated + ["tables.md"],
                **analysis_fingerprints(results)}
    (output / "analysis_metadata.json").write_text(json.dumps(metadata, indent=2), encoding="utf-8")
    return metadata


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--results", type=Path, required=True)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--stage", default="A", help="Caption only; does not change estimator (default: A)")
    parser.add_argument("--allow-partial-import", action="store_true", help="Explicit exploratory import bypassing strict completion/inventory requirements")
    args = parser.parse_args()
    print(json.dumps(generate_tables(args.results, args.output, args.stage, allow_partial=args.allow_partial_import), indent=2))


if __name__ == "__main__":
    main()
