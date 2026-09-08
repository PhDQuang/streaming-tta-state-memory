"""Compare pinned faithful SAR and sar_complete on fixed Stage A AB+W4+Q.

Training-only UCI mechanics. No benchmark, hyperparameter search, source retraining,
or adaptation labels. Official reference files are imported without modification.
"""
from __future__ import annotations

import argparse
from contextlib import redirect_stdout
from copy import deepcopy
import importlib.util
import io
import json
import math
from pathlib import Path
import time
import traceback

import numpy as np
import torch

import _bootstrap
from historytta.adapters import make_adapter, softmax_entropy
from historytta.data import DigitLoader, load_uci_train
from historytta.metrics import prediction_metrics
from historytta.models import DigitCNN
from historytta.runner import append_csv, from_manifest
from historytta.streams import load_batch
from historytta.utils import file_sha256, provenance, seed_all, write_json

ROOT = Path(__file__).resolve().parents[1]
REFERENCE = ROOT / "third_party" / "sar_reference"
REFERENCE_COMMIT = "20f6e24b17525f34503510afccedc0629b67b7c4"
RESET_NOTICE = "ema < 0.2, now reset the model"


def load_reference(directory: Path = REFERENCE):
    manifest = json.loads((directory / "manifest.json").read_text(encoding="utf-8"))
    if manifest["commit"] != REFERENCE_COMMIT:
        raise ValueError("Unexpected SAR reference commit")
    modules = []
    for name in ("sar", "sam"):
        path = directory / (name + ".py")
        if file_sha256(path) != manifest["files"][path.name]["sha256"]:
            raise ValueError("Pinned SAR source checksum mismatch: " + path.name)
        spec = importlib.util.spec_from_file_location("recovery_reference_" + name, path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        modules.append(module)
    return (*modules, manifest)


def make_pair(model, lr: float, momentum: float, margin: float, reference=None):
    sar, sam = (reference or load_reference())[:2]
    ref_model = sar.configure_model(deepcopy(model))
    parameters, names = sar.collect_params(ref_model)
    faithful = sar.SAR(ref_model, sam.SAM(parameters, torch.optim.SGD, lr=lr,
                                       momentum=momentum), margin_e0=margin,
                       reset_constant_em=.2)
    complete = make_adapter(deepcopy(model), "sar_complete", lr=lr,
                            momentum=momentum, sar_margin=margin, reset_threshold=.2)
    if names != complete.adapted_parameter_names:
        raise AssertionError("Reference/complete adapted parameter inventory differs")
    if any(not torch.equal(p, dict(complete.model.named_parameters())[name])
           for name, p in faithful.model.named_parameters()):
        raise AssertionError("Reference/complete source parameters differ")
    return faithful, complete


def _finite_tree(value):
    if isinstance(value, torch.Tensor):
        return bool(torch.isfinite(value).all())
    if isinstance(value, dict):
        return all(_finite_tree(v) for v in value.values())
    if isinstance(value, (tuple, list)):
        return all(_finite_tree(v) for v in value)
    return True


def _observe_step(model, operation, x, margin):
    """Observe the actual two forwards with a read-only hook; no extra forward."""
    forwards = []
    handle = model.register_forward_hook(lambda module, args, output: forwards.append(output.detach().clone()))
    captured = io.StringIO()
    try:
        with redirect_stdout(captured):
            logits = operation(x).detach().clone()
    finally:
        handle.remove()
    if not forwards:
        raise AssertionError("Adapter made no forward pass")
    first = softmax_entropy(forwards[0])
    reliable = first < margin
    second = softmax_entropy(forwards[1])[reliable] if len(forwards) == 2 else torch.empty(0)
    second_reliable = second[second < margin]
    diagnostics = {"first_reliable": int(reliable.sum()), "second_reliable": len(second_reliable),
                   "forward_count": len(forwards), "stdout": captured.getvalue(),
                   "finite_forwards": all(bool(torch.isfinite(v).all()) for v in forwards),
                   "finite_parameters": all(bool(torch.isfinite(p).all()) for p in model.parameters()),
                   "second_filtered_entropy": float(second_reliable.mean()) if len(second_reliable) else None}
    if not torch.equal(logits, forwards[0]):
        raise AssertionError("Returned logits are not the first unperturbed forward")
    return logits, diagnostics


def step_pair(faithful, complete, x, margin: float):
    """Input-only paired operation. Evaluation labels are intentionally absent."""
    a, ad = _observe_step(faithful.model, faithful, x, margin)
    before = deepcopy(complete.aux)
    b, bd = _observe_step(complete.model, complete.adapt_batch, x, margin)
    ad["recoveries"] = ad["stdout"].count(RESET_NOTICE)
    bd["recoveries"] = complete.aux["recoveries"] - before["recoveries"]
    ad["ema"] = faithful.ema
    bd["ema"] = complete.aux["ema"]
    bd["skips"] = complete.aux["skipped"] - before["skipped"]
    ad["finite_optimizer"] = _finite_tree(faithful.optimizer.state_dict()) and _finite_tree(faithful.optimizer.base_optimizer.state_dict())
    bd["finite_optimizer"] = _finite_tree(complete.optimizer.state_dict())
    ad["guard_passed"] = ad["forward_count"] == 2 and ad["first_reliable"] > 0 and ad["second_reliable"] > 0 and ad["finite_forwards"] and ad["finite_parameters"] and ad["finite_optimizer"]
    bd["guard_passed"] = bd["forward_count"] == 2 and bd["first_reliable"] > 0 and bd["second_reliable"] > 0 and bd["finite_forwards"] and bd["finite_parameters"] and bd["finite_optimizer"] and bd["skips"] == 0
    params_b = dict(complete.model.named_parameters())
    parameter_diff = max(float((p.detach() - params_b[n].detach()).abs().max()) for n, p in faithful.model.named_parameters())
    momentum_diff = 0.
    for name, p in faithful.model.named_parameters():
        q = params_b[name]
        ma = faithful.optimizer.base_optimizer.state.get(p, {}).get("momentum_buffer")
        mb = complete.optimizer.base_optimizer.state.get(q, {}).get("momentum_buffer")
        if ma is not None or mb is not None:
            momentum_diff = max(momentum_diff, float(((torch.zeros_like(p) if ma is None else ma) -
                                                      (torch.zeros_like(q) if mb is None else mb)).abs().max()))
    comparison = {"max_logit_diff": float((a-b).abs().max()),
                  "disagreement": float(a.argmax(1).ne(b.argmax(1)).float().mean()),
                  "post_step_parameter_max_diff": parameter_diff,
                  "post_step_momentum_max_diff": momentum_diff}
    return a, b, ad, bd, comparison


def compare_trajectory(model, panel, loader, settings, output: Path, identity: dict,
                       reference=None):
    faithful, complete = make_pair(model, settings["lr"], settings["momentum"], settings["margin"], reference)
    stem = f'{identity["seed"]}_{identity["scenario"]}'
    sequences = (("history_ab", panel.history_ab), ("washout4", panel.washout[-4:]), ("suffix", panel.suffix))
    if len(panel.washout) < 4:
        raise ValueError("The fixed comparison requires four washout batches")
    traces, a_outputs, b_outputs, samples, phases = [], [], [], [], []
    all_resets = [0, 0]
    suffix_resets = [0, 0]
    ordinary_controls = 0
    stdout_records = []
    start = time.perf_counter()
    for phase, sequence in sequences:
        for phase_batch, batch in enumerate(sequence):
            x = load_batch(batch, loader, "cpu")
            a, b, ad, bd, comparison = step_pair(faithful, complete, x, settings["margin"])
            pre_recovery = sum(all_resets) == 0 and ad["recoveries"] == bd["recoveries"] == 0
            ordinary_equal = comparison["max_logit_diff"] == comparison["post_step_parameter_max_diff"] == comparison["post_step_momentum_max_diff"] == 0.
            record = {**identity, "batch": len(traces), "phase": phase, "phase_batch": phase_batch,
                      "ids": [s.base_id for s in batch], "faithful": ad, "complete": bd,
                      "ordinary_pre_recovery_control": pre_recovery,
                      "ordinary_control_passed": ordinary_equal if pre_recovery else None, **comparison}
            traces.append(record)
            stdout_records.append(f"batch={len(traces)-1} phase={phase}\n{ad['stdout']}")
            if not ad["guard_passed"] or not bd["guard_passed"] or (pre_recovery and not ordinary_equal):
                write_json(output / "traces" / f"{stem}_failed.json", traces)
                (output / "logs").mkdir(exist_ok=True)
                (output / "logs" / f"{stem}_faithful_stdout.txt").write_text("\n".join(stdout_records), encoding="utf-8")
                raise AssertionError("Invalid trajectory: filtering/nonfinite/skip or ordinary parity guard failed")
            ordinary_controls += int(pre_recovery)
            all_resets[0] += ad["recoveries"]
            all_resets[1] += bd["recoveries"]
            if phase == "suffix":
                suffix_resets[0] += ad["recoveries"]
                suffix_resets[1] += bd["recoveries"]
            a_outputs.append(a.cpu())
            b_outputs.append(b.cpu())
            samples.extend(batch)
            phases.extend([phase] * len(batch))
    labels = torch.tensor([s.label for s in samples])  # evaluator only, after all adaptation
    suffix_mask = np.asarray(phases) == "suffix"
    predictions = [torch.cat(a_outputs), torch.cat(b_outputs)]
    scores = []
    for index, method in enumerate(("sar_faithful_pinned", "sar_complete")):
        logits = predictions[index]
        filename = f"{stem}_{method}.npz"
        (output / "predictions").mkdir(exist_ok=True)
        np.savez_compressed(output / "predictions" / filename, logits=logits.numpy(), labels=labels.numpy(),
                            ids=np.asarray([s.base_id for s in samples]), phases=np.asarray(phases),
                            domains=np.asarray([s.domain for s in samples]))
        score = prediction_metrics(logits[suffix_mask], labels[suffix_mask])
        scores.append(score)
        append_csv(output / "runs.csv", {**identity, "method": method, "history": "ab", "washout_batches": 4,
                   **{k: score[k] for k in ("n", "accuracy", "error", "nll", "brier", "ece15")},
                   "total_recoveries": all_resets[index], "suffix_recoveries": suffix_resets[index],
                   "skipped_updates": 0, "prediction_file": "predictions/" + filename})
    first_logit = next((t["batch"] for t in traces if t["max_logit_diff"] > 0), None)
    first_momentum = next((t["batch"] for t in traces if t["post_step_momentum_max_diff"] > 0), None)
    pair = {**identity, "history": "ab", "washout_batches": 4, "n": int(suffix_mask.sum()),
            "suffix_disagreement": float(predictions[0][suffix_mask].argmax(1).ne(predictions[1][suffix_mask].argmax(1)).float().mean()),
            "signed_error_gap_faithful_minus_complete": scores[0]["error"]-scores[1]["error"],
            "nll_gap_faithful_minus_complete": scores[0]["nll"]-scores[1]["nll"],
            "max_suffix_logit_diff": float((predictions[0][suffix_mask]-predictions[1][suffix_mask]).abs().max()),
            "faithful_total_recoveries": all_resets[0], "complete_total_recoveries": all_resets[1],
            "faithful_suffix_recoveries": suffix_resets[0], "complete_suffix_recoveries": suffix_resets[1],
            "first_divergent_logit_batch": first_logit, "first_divergent_momentum_batch": first_momentum,
            "ordinary_controls_passed": ordinary_controls, "valid_batches": len(traces),
            "paired_seconds": time.perf_counter()-start}
    append_csv(output / "paired.csv", pair)
    write_json(output / "traces" / f"{stem}.json", traces)
    (output / "logs").mkdir(exist_ok=True)
    (output / "logs" / f"{stem}_faithful_stdout.txt").write_text("\n".join(stdout_records), encoding="utf-8")
    return pair


def run(stage_a: Path, output: Path):
    stage_a, output = stage_a.resolve(), output.resolve()
    if output.exists() and any(output.iterdir()):
        raise FileExistsError("Refusing to overwrite recovery comparison results")
    source_status = json.loads((stage_a / "run_status.json").read_text())
    if source_status.get("status") != "complete" or source_status.get("stage") != "A":
        raise ValueError("Require a completed Stage A producer")
    original_provenance = json.loads((stage_a / "provenance.json").read_text())
    config = original_provenance["config"]
    if config["adaptation"]["reset_threshold"] != .2 or config["source_seeds"] != [17, 29, 43]:
        raise ValueError("Unexpected fixed Stage A recovery configuration")
    records = json.loads((stage_a / "checkpoints.json").read_text())
    reference = load_reference()
    settings = {"lr": config["adaptation"]["lr"], "momentum": config["adaptation"]["momentum"],
                "margin": .4 * math.log(10), "reset_threshold": .2}
    output.mkdir(parents=True, exist_ok=True)
    comparison_config = {"experiment_id": output.name, "stage": "A", "source_results": str(stage_a),
                         "settings": settings, "source_config": config,
                         "comparison": "faithful pinned SAR versus complete-state SAR; fixed AB+W4+Q",
                         "claims": "training-only local mechanics; no ImageNet effect or generalization claim"}
    write_json(output / "provenance.json", {**provenance(comparison_config), "reference": reference[2],
               "source_provenance_sha256": file_sha256(stage_a / "provenance.json"),
               "checkpoint_records": records})
    write_json(output / "run_status.json", {"status": "running", "stage": "A"})
    start = time.perf_counter()
    try:
        images, _ = load_uci_train(ROOT / config["data"])
        pairs = []
        for seed in config["source_seeds"]:
            record = next(r for r in records if r["seed"] == seed)
            path = Path(record["path"])
            if not path.is_absolute():
                path = ROOT / path
            if not path.exists() or file_sha256(path) != record["sha256"]:
                raise ValueError("Producer checkpoint missing or changed: " + str(path))
            checkpoint = torch.load(path, map_location="cpu", weights_only=True)
            model = DigitCNN()
            model.load_state_dict(checkpoint["model"])
            model.eval()
            for scenario in config["scenarios"]:
                seed_all(seed, config["threads"])
                filename = f'{seed}_uci_internal_fixed_{scenario["name"]}_sar_complete.json'
                panel_path = stage_a / "manifests" / filename
                document = json.loads(panel_path.read_text())
                panel = from_manifest(document)
                write_json(output / "manifests" / filename, document)
                identity = {"experiment_id": output.name, "seed": seed,
                            "panel_id": "uci_internal_fixed", "scenario": scenario["name"],
                            "source_checkpoint_sha256": record["sha256"], "panel_sha256": document["sha256"]}
                pairs.append(compare_trajectory(model, panel, DigitLoader(images, config["split_seed"]),
                                                settings, output, identity, reference))
                print(f"seed={seed} scenario={scenario['name']}: compared faithful/complete", flush=True)
        summary = {"scope": comparison_config["claims"], "pairs": len(pairs),
                   "statistical_unit": "one shared original-image panel; source seeds/scenarios descriptive, no CI",
                   "ordinary_controls_passed": sum(p["ordinary_controls_passed"] for p in pairs),
                   "valid_paired_batches": sum(p["valid_batches"] for p in pairs),
                   "max_suffix_disagreement": max(p["suffix_disagreement"] for p in pairs),
                   "max_absolute_suffix_error_gap": max(abs(p["signed_error_gap_faithful_minus_complete"]) for p in pairs),
                   "faithful_total_recoveries": sum(p["faithful_total_recoveries"] for p in pairs),
                   "complete_total_recoveries": sum(p["complete_total_recoveries"] for p in pairs),
                   "all_pairs": pairs}
        write_json(output / "summary.json", summary)
        write_json(output / "run_status.json", {"status": "complete", "stage": "A",
                   "seconds": time.perf_counter()-start, **{k: summary[k] for k in ("scope", "pairs", "ordinary_controls_passed", "valid_paired_batches")}})
        return summary
    except Exception:
        write_json(output / "run_status.json", {"status": "failed", "stage": "A",
                   "seconds": time.perf_counter()-start, "traceback": traceback.format_exc()})
        raise


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--stage-a", type=Path, default=Path("results/stage_a_uci_v1"))
    parser.add_argument("--output", type=Path, default=Path("results/stage_a_sar_recovery_comparison"))
    args = parser.parse_args()
    summary = run(args.stage_a, args.output)
    print(json.dumps({k:v for k,v in summary.items() if k != "all_pairs"}, indent=2))
