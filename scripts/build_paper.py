"""Build the honest Stage A manuscript and claim provenance from recorded results."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import pandas as pd
import _bootstrap
from historytta.utils import file_sha256, write_json


def table(headers, rows):
    return "\n".join(["| " + " | ".join(headers) + " |", "| " + " | ".join(["---"] * len(headers)) + " |"] +
                     ["| " + " | ".join(map(str, row)) + " |" for row in rows])


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--results", type=Path, default=Path("results/stage_a_uci_v2"))
    args = p.parse_args()
    root = args.results
    status = json.loads((root / "run_status.json").read_text())
    if status.get("status") != "complete" or status.get("stage") != "A":
        raise ValueError("This manuscript template only reports a completed local Stage A run")
    runs, paired, training = [pd.read_csv(root / name) for name in ("runs.csv", "paired.csv", "training.csv")]
    if set(runs.seed) != {17, 29, 43} or runs.panel_id.nunique() != 1:
        raise ValueError("Template assumptions require the fixed three-source-seed, one-panel local design")
    methods = [("source", "Source"), ("norm", "Normalization only"), ("tent", "Tent"), ("sar_complete", "SAR complete")]
    final = training.sort_values("epoch").groupby("seed").tail(1).sort_values("seed")
    # Training output uses explicit dev_accuracy; these are not Q accuracies.
    train_table = table(["Seed", "Final-epoch training loss", "Internal development accuracy (%)"],
                        [[int(row.seed), f"{row.train_loss:.6f}", f"{100 * row.dev_accuracy:.4f}"] for row in final.itertuples()])
    no_reset = paired[paired.intervention == "none"]
    d_rows, perf_rows = [], []
    for key, label in methods:
        for w in (0, 4):
            seed = no_reset[(no_reset.method == key) & (no_reset.washout_batches == w)].groupby("seed").disagreement.mean() * 100
            d_rows.append([label, w, *[f"{seed.loc[s]:.6f}" for s in (17, 29, 43)], f"{seed.mean():.6f}", f"{seed.std(ddof=1):.6f}"])
        selected = runs[(runs.method == key) & (runs.intervention == "none") & (runs.washout_batches == 4)]
        seed = selected.groupby("seed")[["accuracy", "nll"]].mean()
        perf_rows.append([label, *[f"{100 * seed.loc[s, 'accuracy']:.4f}" for s in (17, 29, 43)],
                          f"{100 * seed.accuracy.mean():.4f} ± {100 * seed.accuracy.std(ddof=1):.4f}", f"{seed.nll.mean():.6f}"])
    values = {"N_RUNS": len(runs), "N_PAIRS": len(paired), "N_CONTROLS": status["controls_total"],
              "SECONDS": f"{status['seconds']:.2f}", "MAX_D": f"{100 * no_reset.disagreement.max():.7f}",
              "SAR_RECOVERIES": int(runs[runs.method == "sar_complete"].recoveries.sum()),
              "SAR_SKIPS": int(runs[runs.method == "sar_complete"].skipped.sum()),
              "TRAINING_TABLE": train_table,
              "DISAGREEMENT_TABLE": table(["Method", "W", "Seed17 D (pp)", "Seed29 D (pp)", "Seed43 D (pp)", "Mean (pp)", "Seed SD (pp)"], d_rows),
              "PERFORMANCE_TABLE": table(["Method", "Seed17 accuracy (%)", "Seed29 accuracy (%)", "Seed43 accuracy (%)", "Mean ± seed SD (%)", "Mean NLL"], perf_rows),
              "EXPERIMENT": str(runs.experiment_id.iloc[0]), "RESULTS": root.as_posix()}
    template = Path("paper/manuscript_template.md")
    text = template.read_text(encoding="utf-8")
    for key, value in values.items():
        text = text.replace(f"@@{key}@@", str(value))
    if "@@" in text:
        raise ValueError("Unresolved manuscript token")
    output = Path("paper/paper.md")
    output.write_text(text, encoding="utf-8")
    sources = [root / f for f in ("runs.csv", "paired.csv", "training.csv", "run_status.json", "provenance.json")]
    sources += [template, Path(__file__), Path("results/stage_a_sar_recovery_comparison/summary.json")]
    write_json("paper/claims.json", {"status": "Stage A draft; full empirical study incomplete", "generated_values": values,
                                   "input_sha256": {str(path): file_sha256(path) for path in sources},
                                   "paper_sha256": file_sha256(output),
                                   "static_context": "Protocol and comparison prose are reviewed separately; dynamic Stage A tables derive from CSVs."})
    print(json.dumps({"paper": str(output), "runs": len(runs), "pairs": len(paired)}, indent=2))


if __name__ == "__main__":
    main()
