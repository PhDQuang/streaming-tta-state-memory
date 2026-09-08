"""Statistical-unit and paired-identity safeguards; fixtures stay in pytest temp dirs."""
from __future__ import annotations

import json
from pathlib import Path
import sys

import numpy as np
import pandas as pd
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from generate_tables import (collapse_panels, describe_seed_variation, factorial_contrasts,
                             generate_tables, intervention_effects, performance_reference_effects)
from generate_figures import generate_figures, outcome_examples


def row(panel="p1", seed="0", scenario="s1", intervention="none", value=.1):
    return {"experiment_id": "fixture_only", "panel_id": panel, "seed": seed,
            "scenario": scenario, "method": "tent", "intervention": intervention,
            "washout_batches": 16, "disagreement": value}


def test_scenario_and_seed_reuse_do_not_inflate_panel_count():
    frame = pd.DataFrame([row(panel, seed, scenario, value=value)
                          for panel, value in [("p1", .1), ("p2", .3)]
                          for seed in ["0", "1", "2"] for scenario in ["a", "b", "c", "d"]])
    seed_panels, panels, summary = collapse_panels(frame, ["disagreement"])
    assert len(seed_panels) == 6
    assert len(panels) == 2
    assert summary.iloc[0].n_panels == 2
    assert summary.iloc[0]["mean"] == pytest.approx(.2)
    assert summary.iloc[0].sd == pytest.approx(np.std([.1, .3], ddof=1))
    assert panels.n_seeds.tolist() == [3, 3]


def test_one_shared_panel_has_no_ci_but_retains_seed_variation():
    frame = pd.DataFrame([row(seed=str(i), value=value) for i, value in enumerate([.1, .2, .3])])
    seed_panels, panels, summary = collapse_panels(frame, ["disagreement"])
    assert summary.iloc[0].n_panels == 1
    assert pd.isna(summary.iloc[0].ci95_low)
    assert pd.isna(summary.iloc[0].sd)
    description = describe_seed_variation(seed_panels, ["disagreement"])
    assert description.iloc[0].seed_sd_descriptive == pytest.approx(.1)
    assert len(json.loads(description.iloc[0].individual_seeds)) == 3


def test_reset_contrasts_match_scenarios_before_aggregation():
    frame = pd.DataFrame([row(scenario="a", value=.1), row(scenario="b", value=.9),
                          row(scenario="a", intervention="all", value=.01)])
    effects = intervention_effects(frame)
    assert len(effects) == 1
    assert effects.iloc[0].scenario == "a"
    assert effects.iloc[0].disagreement_change == pytest.approx(-.09)


def test_duplicate_trajectory_cannot_silently_overweight_results():
    with pytest.raises(ValueError, match="Duplicate"):
        collapse_panels(pd.DataFrame([row(), row()]), ["disagreement"])


def test_performance_references_pair_seed_scenario_and_direction_before_aggregation():
    records = []
    for seed in ["0", "1"]:
        for method, intervention, accuracy in [("source", "none", .8), ("source", "all", .99),
                                               ("tent", "none", .6), ("tent", "all", .7)]:
            item = row(seed=seed, intervention=intervention)
            item.update(method=method, direction="ab", accuracy=accuracy + int(seed) * .005)
            records.append(item)
    effects = performance_reference_effects(pd.DataFrame(records), "source")
    assert len(effects) == 4
    assert effects.loc[effects.intervention.eq("none"), "error_change"].tolist() == pytest.approx([.2, .2])
    reset = performance_reference_effects(pd.DataFrame(records), None)
    assert reset.loc[reset.method.eq("tent"), "accuracy_change"].tolist() == pytest.approx([.1, .1])


def test_factorial_contrasts_have_declared_scale_and_require_complete_cells():
    names = ["none", "parameters", "optimizer", "parameters_optimizer", "aux",
             "parameters_aux", "optimizer_aux", "parameters_optimizer_aux"]
    records = []
    for i, name in enumerate(names):
        p, o, e = i % 2, (i // 2) % 2, i // 4
        records.append(row(intervention=name, value=1 + 2*p + 3*o + 4*e + 5*p*o))
    contrasts = factorial_contrasts(pd.DataFrame(records)).set_index("intervention")
    assert contrasts.loc["factorial:P", "disagreement_factorial"] == pytest.approx(4.5)
    assert contrasts.loc["factorial:O", "disagreement_factorial"] == pytest.approx(5.5)
    assert contrasts.loc["factorial:PO", "disagreement_factorial"] == pytest.approx(5)
    assert contrasts.loc["factorial:POE", "disagreement_factorial"] == pytest.approx(0)
    assert factorial_contrasts(pd.DataFrame(records[:-1])).empty


def test_outcome_groups_align_ids_and_choose_first_ids():
    a = {"ids": np.array(["z", "b", "a", "d", "c"]), "labels": np.zeros(5, dtype=int),
         "logits": np.array([[2, 0], [2, 0], [0, 2], [0, 2], [2, 0]])}
    b = {"ids": np.array(["c", "d", "z", "a", "b"]), "labels": np.zeros(5, dtype=int),
         "logits": np.array([[2, 0], [0, 2], [2, 0], [2, 0], [0, 2]])}
    examples, counts = outcome_examples(a, b, limit=1)
    assert counts == {"Both correct": 2, "A correct, B wrong": 1, "A wrong, B correct": 1, "Both wrong": 1}
    assert examples["Both correct"][0]["id"] == "c"
    assert examples["A wrong, B correct"][0]["id"] == "a"
    b["labels"][0] = 1
    with pytest.raises(ValueError, match="different true labels"):
        outcome_examples(a, b)


def test_missing_results_do_not_create_empirical_values(tmp_path):
    results = tmp_path / "empty"
    results.mkdir()
    tables = generate_tables(results, allow_partial=True)
    assert not (results / "tables" / "paired_summary.csv").exists()
    assert tables["pvalues_computed"] is False
    figures = generate_figures(results, tmp_path / "plots", allow_partial=True)
    assert [item["name"] for item in figures["figures"]] == ["protocol_schematic"]
    assert figures["skipped"]


def test_unfinished_run_cannot_produce_partial_empirical_report(tmp_path):
    (tmp_path / "run_status.json").write_text('{"status":"running"}', encoding="utf-8")
    with pytest.raises(RuntimeError, match="unfinished"):
        generate_tables(tmp_path)
    with pytest.raises(RuntimeError, match="unfinished"):
        generate_figures(tmp_path, tmp_path / "plots")
    assert not (tmp_path / "tables").exists()


def test_missing_status_is_not_silently_treated_as_completed(tmp_path):
    with pytest.raises(RuntimeError, match="Missing mandatory run_status"):
        generate_tables(tmp_path)
    with pytest.raises(RuntimeError, match="Missing mandatory run_status"):
        generate_figures(tmp_path, tmp_path / "plots")


def test_full_pipeline_uses_only_temporary_fixture(tmp_path):
    results = tmp_path / "fixture_only"
    results.mkdir()
    records = []
    for seed in ["0", "1", "2"]:
        for w in [0, 4, 16]:
            for intervention, value in [("none", .12), ("parameters", .04), ("optimizer", .06), ("all", 0.)]:
                item = row(seed=seed, intervention=intervention, value=value)
                item["washout_batches"] = w
                records.append(item)
    pd.DataFrame(records).to_csv(results / "paired.csv", index=False)
    generate_tables(results, allow_partial=True)
    metadata = generate_figures(results, tmp_path / "plots", allow_partial=True)
    assert {"disagreement_washout", "state_reset_effects", "protocol_schematic"} == {x["name"] for x in metadata["figures"]}
    assert (results / "tables" / "paired_seed_descriptive.csv").exists()
