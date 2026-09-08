"""Execute matched histories, complete-state branches and paired suffix metrics."""
from __future__ import annotations

import csv
from copy import deepcopy
import hashlib
import json
from pathlib import Path
import random
import time
import traceback

import numpy as np
import torch

from .metrics import prediction_metrics
from .streams import Sample, StreamPanel, load_batch
from .utils import write_json, object_sha256, file_sha256

INTERVENTIONS = {
    "none": [], "parameters": ["parameters"], "optimizer": ["optimizer"],
    "parameters_optimizer": ["parameters", "optimizer"], "aux": ["aux"],
    "parameters_aux": ["parameters", "aux"], "optimizer_aux": ["optimizer", "aux"],
    "parameters_optimizer_aux": ["parameters", "optimizer", "aux"], "all": ["all"],
}


def rng_snapshot():
    return {"python": random.getstate(), "numpy": np.random.get_state(),
            "torch": torch.get_rng_state().clone(),
            "cuda": [s.clone() for s in torch.cuda.get_rng_state_all()] if torch.cuda.is_available() else []}


def restore_rng(state):
    random.setstate(state["python"])
    np.random.set_state(state["numpy"])
    torch.set_rng_state(state["torch"])
    if state["cuda"]:
        torch.cuda.set_rng_state_all(state["cuda"])


def batch_rng_schedule(sequence, metadata: dict, role: str) -> list[int]:
    """Common random numbers keyed to immutable batch identity, never labels.

    H/W/Q use independent roles. Matching W batches receive identical draws even
    when their positions differ between short and long common tails. Method and
    history direction are excluded so random preprocessing and first-pass dropout
    are paired across the scientific comparison. This deliberately standardizes
    randomness at each batch boundary rather than modeling natural RNG history.
    """
    if role not in {"H", "W", "Q"}:
        raise ValueError("RNG role must be H, W, or Q")
    seeds = []
    for batch in sequence:
        value = {"protocol": "batch_crn_v1", "seed": metadata["seed"],
                 "panel_id": metadata["panel_id"], "role": role,
                 "batch": [sample.key() for sample in batch]}
        seeds.append(int(object_sha256(value)[:16], 16) % (2**63 - 1))
    return seeds


def _seed_batch(seed: int):
    random.seed(seed)
    np.random.seed(seed % 2**32)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)


def _state_sha256(value) -> str:
    """Content digest independent of torch pickle layout and tensor device."""
    digest = hashlib.sha256()

    def update(item):
        if isinstance(item, torch.Tensor):
            digest.update(f"tensor:{item.dtype}:{tuple(item.shape)}:".encode())
            raw = item.detach().cpu().contiguous().reshape(-1).view(torch.uint8)
            digest.update(raw.numpy().tobytes())
        elif isinstance(item, dict):
            digest.update(b"dict:")
            for key in sorted(item, key=str):
                update(key)
                update(item[key])
        elif isinstance(item, (list, tuple)):
            digest.update(f"{type(item).__name__}:{len(item)}:".encode())
            for child in item:
                update(child)
        else:
            digest.update(f"{type(item).__name__}:".encode())
            digest.update(json.dumps(item, sort_keys=True, allow_nan=False).encode())
        digest.update(b";")

    update(value)
    return digest.hexdigest()


def junction_config_sha256(adapter, metadata: dict) -> str:
    """Hash immutable algorithm settings and study metadata, not current state."""
    anchor = adapter._source_state
    optimizer = anchor["optimizer"]
    if optimizer is not None and "wrapper" in optimizer:
        optimizer = {"wrapper": optimizer["wrapper"]["param_groups"],
                     "base_optimizer": optimizer["base_optimizer"]["param_groups"]}
    elif optimizer is not None:
        optimizer = optimizer["param_groups"]
    return object_sha256({
        "rng_protocol": "batch_crn_v1", "metadata": metadata,
        "implementation": adapter.implementation, "config": anchor["config"],
        "optimizer_groups": optimizer, "adapted_parameters": adapter.adapted_parameter_names,
        "parameter_schema": {n: [list(p.shape), str(p.dtype)]
                             for n, p in anchor["parameters"].items()},
    })


def _verify_source_checkpoint(source_checkpoint):
    if source_checkpoint is None:
        return None
    if not isinstance(source_checkpoint, dict) or not {"path", "sha256"} <= source_checkpoint.keys():
        raise ValueError("source_checkpoint requires path and sha256")
    path = Path(source_checkpoint["path"])
    if not path.is_file() or file_sha256(path) != source_checkpoint["sha256"]:
        raise ValueError("Source checkpoint file/hash mismatch")
    return {**source_checkpoint, "path": str(path.resolve())}


def save_junction_checkpoint(path, adapter, state, metadata, manifest_sha256,
                             source_checkpoint=None, rng=None, context=None):
    """Save current state plus the immutable recovery anchor and provenance."""
    path = Path(path)
    if path.exists() or path.with_suffix(path.suffix + ".json").exists():
        raise FileExistsError(f"Refusing to overwrite junction checkpoint: {path}")
    source = _verify_source_checkpoint(source_checkpoint)
    anchor = deepcopy(adapter._source_state)
    adapter_config_hash = junction_config_sha256(adapter, metadata)
    payload = {"schema": 1, "metadata": deepcopy(metadata),
               "config_sha256": (source or {}).get("config_sha256", adapter_config_hash),
               "adapter_config_sha256": adapter_config_hash,
               "manifest_sha256": manifest_sha256, "source_checkpoint": source,
               "source_anchor_sha256": _state_sha256(anchor), "source_anchor": anchor,
               "adapter_snapshot": deepcopy(state),
               "rng": deepcopy(rng_snapshot() if rng is None else rng),
               "rng_protocol": "batch_crn_v1", "context": deepcopy(context or {})}
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    torch.save(payload, temporary)
    temporary.replace(path)
    write_json(path.with_suffix(path.suffix + ".json"),
               {"sha256": file_sha256(path), "config_sha256": payload["config_sha256"],
                "manifest_sha256": manifest_sha256,
                "source_anchor_sha256": payload["source_anchor_sha256"]})


def load_junction_checkpoint(path, adapter, *, expected_config_sha256,
                             expected_manifest_sha256, source_checkpoint=None):
    """Restore an OWN trusted checkpoint, including its immutable source anchor.

    ``weights_only=False`` is required for Python/NumPy RNG state. Only open files
    produced by this project and trusted by the caller: hashes detect accidental
    corruption, not malicious replacement of both checkpoint and sidecar.
    The existing adapter must have the same architecture/algorithm configuration;
    its initial model weights may differ because the saved anchor replaces them.
    """
    path = Path(path)
    sidecar = json.loads(path.with_suffix(path.suffix + ".json").read_text(encoding="utf-8"))
    if file_sha256(path) != sidecar["sha256"]:
        raise ValueError("Junction checkpoint integrity mismatch")
    if sidecar["config_sha256"] != expected_config_sha256 or sidecar["manifest_sha256"] != expected_manifest_sha256:
        raise ValueError("Junction config/manifest hash mismatch")
    payload = torch.load(path, map_location="cpu", weights_only=False)
    if payload.get("schema") != 1 or payload.get("rng_protocol") != "batch_crn_v1":
        raise ValueError("Unsupported junction checkpoint")
    if payload["config_sha256"] != expected_config_sha256 or payload["manifest_sha256"] != expected_manifest_sha256:
        raise ValueError("Junction payload config/manifest mismatch")
    if junction_config_sha256(adapter, payload["metadata"]) != payload["adapter_config_sha256"]:
        raise ValueError("Existing adapter configuration differs from saved configuration")
    if _state_sha256(payload["source_anchor"]) != payload["source_anchor_sha256"]:
        raise ValueError("Immutable source anchor integrity mismatch")
    # A relocated but byte-identical source file is accepted when explicitly
    # provided; otherwise verify the originally recorded local checkpoint path.
    expected_source = _verify_source_checkpoint(source_checkpoint)
    saved_source = payload["source_checkpoint"]
    if expected_source is not None:
        if saved_source is None or saved_source["sha256"] != expected_source["sha256"]:
            raise ValueError("Junction source checkpoint identity mismatch")
        if expected_source.get("config_sha256", expected_config_sha256) != expected_config_sha256:
            raise ValueError("Source descriptor configuration hash mismatch")
    else:
        _verify_source_checkpoint(saved_source)
    old_anchor = adapter._source_state
    old_state = adapter.snapshot()
    old_rng = rng_snapshot()
    try:
        adapter.restore(payload["source_anchor"])
        adapter._source_state = deepcopy(payload["source_anchor"])
        adapter.restore(payload["adapter_snapshot"])
        restore_rng(payload["rng"])
    except Exception:
        adapter._source_state = old_anchor
        adapter.restore(old_state)
        restore_rng(old_rng)
        raise
    return payload


def tree_equal(a, b):
    if isinstance(a, torch.Tensor):
        return isinstance(b, torch.Tensor) and torch.equal(a, b)
    if isinstance(a, np.ndarray):
        return isinstance(b, np.ndarray) and np.array_equal(a, b)
    if isinstance(a, dict):
        return isinstance(b, dict) and a.keys() == b.keys() and all(tree_equal(a[k], b[k]) for k in a)
    if isinstance(a, (tuple, list)):
        return type(a) == type(b) and len(a) == len(b) and all(tree_equal(x, y) for x, y in zip(a, b))
    return a == b


def append_csv(path: Path, row: dict):
    path.parent.mkdir(parents=True, exist_ok=True)
    exists = path.exists()
    with path.open("a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(row))
        if not exists:
            writer.writeheader()
        writer.writerow(row)


def from_manifest(data: dict) -> StreamPanel:
    panel = StreamPanel(**{key: tuple(tuple(Sample(**s) for s in b) for b in data[key])
                           for key in ("history_ab", "history_ba", "washout", "suffix")})
    panel.validate()
    if data.get("sha256") != panel.manifest()["sha256"]:
        raise ValueError("Panel manifest integrity mismatch")
    return panel


def _sync(device):
    if str(device).startswith("cuda"):
        torch.cuda.synchronize()


def forward_sequence(adapter, sequence, loader, device, keep_logits=True,
                     rng_schedule=None, failure_dir=None, context=None):
    """Process a sequence; persist exact failing-batch context before raising."""
    if rng_schedule is not None and len(rng_schedule) != len(sequence):
        raise ValueError("RNG schedule length must match sequence length")
    outputs, trace = [], []
    _sync(device)
    start = time.perf_counter()
    for i, batch in enumerate(sequence):
        logits = None
        try:
            if rng_schedule is not None:
                _seed_batch(rng_schedule[i])
            logits = adapter.adapt_batch(load_batch(batch, loader, device))
            if not torch.isfinite(logits).all():
                raise FloatingPointError("Non-finite predictions")
            if keep_logits:
                outputs.append(logits.detach().cpu())
            trace.append({"batch": i, **deepcopy(adapter.aux)})
        except Exception as exc:
            if failure_dir is not None:
                try:
                    from dataclasses import asdict
                    failed_context = {**(context or {}), "batch": i,
                                      "samples": [asdict(s) for s in batch],
                                      "batch_rng_seed": None if rng_schedule is None else rng_schedule[i]}
                    failure_id = f'{object_sha256(failed_context)[:16]}_{time.time_ns()}'
                    destination = Path(failure_dir)
                    destination.mkdir(parents=True, exist_ok=True)
                    diagnostics = {"status": "failed", "context": failed_context,
                                   "exception_type": type(exc).__name__, "exception": str(exc),
                                   "traceback": traceback.format_exc(), "completed_trace": trace,
                                   "elapsed_seconds": time.perf_counter() - start}
                    write_json(destination / f"{failure_id}.json", diagnostics)
                    # Raw nonfinite tensors are valid in torch files, whereas
                    # the JSON diagnostic intentionally does not encode NaNs.
                    state = adapter.snapshot()
                    raw_name = f"{failure_id}.pt"
                    torch.save({"context": failed_context, "adapter_snapshot": state,
                                "source_anchor": deepcopy(adapter._source_state), "rng": rng_snapshot(),
                                "completed_logits": outputs,
                                "failed_logits": None if logits is None else logits.detach().cpu()},
                               destination / raw_name)
                    diagnostics["raw_state_file"] = raw_name
                    write_json(destination / f"{failure_id}.json", diagnostics)
                except Exception as logging_error:
                    exc.add_note(f"Failure diagnostic persistence also failed: {logging_error}")
            raise
    _sync(device)
    elapsed = time.perf_counter() - start
    return torch.cat(outputs) if outputs else None, trace, elapsed


def execute_panel(adapter, panel: StreamPanel, loader, output: Path, metadata: dict,
                  washout_lengths=(0, 4), interventions=None, device="cpu",
                  save_images=False, verify_replay=True, save_junctions=False,
                  source_checkpoint=None):
    panel.validate()
    interventions = interventions or list(INTERVENTIONS)
    if any(i not in INTERVENTIONS for i in interventions):
        raise ValueError("Unknown intervention")
    if any(w < 0 or w > len(panel.washout) for w in washout_lengths):
        raise ValueError("Invalid washout length")
    output = Path(output)
    output.mkdir(parents=True, exist_ok=True)
    manifest = panel.manifest()
    stem = f'{metadata["seed"]}_{metadata["panel_id"]}_{metadata["scenario"]}_{adapter.implementation}'
    write_json(output / "manifests" / f"{stem}.json", manifest)
    write_json(output / "inventory" / f"{stem}.json", adapter.state_inventory())
    initial_rng = rng_snapshot()
    h_schedules = {"ab": batch_rng_schedule(panel.history_ab, metadata, "H"),
                   "ba": batch_rng_schedule(panel.history_ba, metadata, "H")}
    w_schedule = batch_rng_schedule(panel.washout, metadata, "W")
    q_schedule = batch_rng_schedule(panel.suffix, metadata, "Q")
    write_json(output / "rng_schedules" / f"{stem}.json",
               {"protocol": "batch_crn_v1", "history_ab": h_schedules["ab"],
                "history_ba": h_schedules["ba"], "washout": w_schedule, "suffix": q_schedule})
    failure_dir = output / "failures"
    prefix_states, junctions = {}, {}
    controls = []
    overhead = []
    for direction in ("ab", "ba"):
        adapter.reset_components(["all"])
        restore_rng(initial_rng)
        history = panel.history_ab if direction == "ab" else panel.history_ba
        _, trace, sec = forward_sequence(adapter, history, loader, device, False,
            rng_schedule=h_schedules[direction], failure_dir=failure_dir,
            context={**metadata, "method":adapter.implementation, "direction":direction, "phase":"history"})
        prefix_states[direction] = (adapter.snapshot(), rng_snapshot())
        overhead.append({"direction":direction,"phase":"history","seconds":sec,"images":sum(map(len,history))})
        write_json(output / "traces" / f"{stem}_{direction}_history.json", trace)
        for w in washout_lengths:
            adapter.restore(prefix_states[direction][0])
            restore_rng(prefix_states[direction][1])
            # LAST k batches ensure W4 shares its most recent content with W16.
            tail = panel.washout[-w:] if w else ()
            _, trace, sec = forward_sequence(adapter, tail, loader, device, False,
                rng_schedule=w_schedule[-w:] if w else [], failure_dir=failure_dir,
                context={**metadata, "method":adapter.implementation, "direction":direction,
                         "phase":"washout", "washout_batches":w})
            junctions[(direction,w)] = adapter.snapshot()
            if save_junctions:
                save_junction_checkpoint(output / "junctions" / f"{stem}_{direction}_w{w}.pt",
                    adapter, junctions[(direction,w)], metadata, manifest["sha256"],
                    source_checkpoint=source_checkpoint,
                    context={"direction": direction, "washout_batches": w})
            overhead.append({"direction":direction,"phase":f"washout_{w}","seconds":sec,"images":sum(map(len,tail))})
            write_json(output / "traces" / f"{stem}_{direction}_w{w}.json", trace)

    # Q has its own per-batch schedule, distinct from H and W. The boundary state
    # remains explicit for empty phases/checkpoint accounting; first Q reseeds.
    q_rng = deepcopy(initial_rng)
    suffix_labels = torch.tensor([s.label for b in panel.suffix for s in b])
    suffix_ids = np.array([s.base_id for b in panel.suffix for s in b])
    paired_rows = []
    for w in washout_lengths:
        for intervention in interventions:
            direction_outputs, states = {}, {}
            for direction in ("ab", "ba"):
                adapter.restore(junctions[(direction,w)])
                adapter.reset_components(INTERVENTIONS[intervention])
                restore_rng(q_rng)
                before = deepcopy(adapter.aux)
                run_context = {**metadata, "method":adapter.implementation, "direction":direction,
                               "washout_batches":w, "intervention":intervention}
                logits, trace, elapsed = forward_sequence(adapter, panel.suffix, loader, device,
                    rng_schedule=q_schedule, failure_dir=failure_dir, context={**run_context,"phase":"suffix"})
                state = adapter.snapshot()
                states[direction] = state
                direction_outputs[direction] = logits
                metrics = prediction_metrics(logits, suffix_labels)
                run_id = f"{stem}_w{w}_{intervention}_{direction}"
                prediction_file = Path("predictions") / f"{run_id}.npz"
                target = output / prediction_file
                target.parent.mkdir(exist_ok=True)
                payload = {"logits":logits.numpy(), "labels":suffix_labels.numpy(), "ids":suffix_ids}
                if save_images and intervention == "none":
                    saved_rng = rng_snapshot()
                    images = []
                    try:
                        for batch, seed in zip(panel.suffix, q_schedule):
                            _seed_batch(seed)
                            images.extend(loader(s) for s in batch)
                    finally:
                        restore_rng(saved_rng)
                    payload["images"] = torch.stack(images).numpy().astype(np.float16)
                np.savez_compressed(target, **payload)
                write_json(output / "traces" / f"{run_id}.json", trace)
                row = {**metadata,"method":adapter.implementation,"intervention":intervention,
                       "washout_batches":w,"direction":direction,
                       **{k:metrics[k] for k in ("n","accuracy","nll","brier","ece15")},
                       "seconds":elapsed,"updates":adapter.aux["updates"]-before["updates"],
                       "skipped":adapter.aux["skipped"]-before["skipped"],
                       "recoveries":adapter.aux["recoveries"]-before["recoveries"],
                       "prediction_file":prediction_file.as_posix()}
                append_csv(output / "runs.csv", row)

                if intervention == "all":
                    adapter.reset_components(["all"])
                    restore_rng(q_rng)
                    cold, _, _ = forward_sequence(adapter, panel.suffix, loader, device,
                        rng_schedule=q_schedule, failure_dir=failure_dir,
                        context={**run_context,"phase":"cold_replay"})
                    equal = torch.equal(logits, cold) and tree_equal(state, adapter.snapshot())
                    controls.append({"id":f"{run_id}_cold_reset","passed":equal,
                                     "max_logit_diff":float((logits-cold).abs().max())})
                    if not equal:
                        write_json(output / "failed_controls.json", controls)
                        raise AssertionError("Full reset does not match cold adapter replay")
                if verify_replay and w == washout_lengths[0] and intervention == "none":
                    adapter.restore(junctions[(direction,w)])
                    restore_rng(q_rng)
                    again, _, _ = forward_sequence(adapter, panel.suffix, loader, device,
                        rng_schedule=q_schedule, failure_dir=failure_dir,
                        context={**run_context,"phase":"snapshot_replay"})
                    equal = torch.equal(logits, again) and tree_equal(state, adapter.snapshot())
                    controls.append({"id":f"{run_id}_snapshot_replay","passed":equal,
                                     "max_logit_diff":float((logits-again).abs().max())})
                    if not equal:
                        raise AssertionError("Same-history checkpoint replay failed")
                    adapter.reset_components(["all"])
                    restore_rng(initial_rng)
                    history = panel.history_ab if direction == "ab" else panel.history_ba
                    forward_sequence(adapter, history, loader, device, False,
                        rng_schedule=h_schedules[direction], failure_dir=failure_dir,
                        context={**run_context,"phase":"full_replay_history"})
                    if w:
                        forward_sequence(adapter, panel.washout[-w:], loader, device, False,
                            rng_schedule=w_schedule[-w:], failure_dir=failure_dir,
                            context={**run_context,"phase":"full_replay_washout"})
                    restore_rng(q_rng)
                    again, _, _ = forward_sequence(adapter, panel.suffix, loader, device,
                        rng_schedule=q_schedule, failure_dir=failure_dir,
                        context={**run_context,"phase":"full_replay_suffix"})
                    equal = torch.equal(logits, again) and tree_equal(state, adapter.snapshot())
                    controls.append({"id":f"{run_id}_full_replay","passed":equal,
                                     "max_logit_diff":float((logits-again).abs().max())})
                    if not equal:
                        raise AssertionError("Fresh entire-history replay failed")

            a,b = direction_outputs["ab"],direction_outputs["ba"]
            am,bm = prediction_metrics(a,suffix_labels),prediction_metrics(b,suffix_labels)
            gap = bm["accuracy"] - am["accuracy"]  # error_AB - error_BA
            first_diff = float((a[:len(panel.suffix[0])]-b[:len(panel.suffix[0])]).abs().max())
            paired = {**metadata,"method":adapter.implementation,"intervention":intervention,"washout_batches":w,
                      "n":len(suffix_labels),"disagreement":float(a.argmax(1).ne(b.argmax(1)).float().mean()),
                      "accuracy_ab":am["accuracy"],"accuracy_ba":bm["accuracy"],
                      "signed_error_gap":gap,"absolute_error_gap":abs(gap),
                      "nll_gap":am["nll"]-bm["nll"],"brier_gap":am["brier"]-bm["brier"],
                      "first_batch_max_logit_diff":first_diff}
            append_csv(output / "paired.csv", paired)
            paired_rows.append(paired)
            if adapter.method in {"source","norm"} or intervention == "all":
                equal = torch.equal(a,b)
                controls.append({"id":f"{stem}_w{w}_{intervention}_history_invariance","passed":equal,
                                 "max_logit_diff":float((a-b).abs().max())})
                if not equal:
                    raise AssertionError("Expected order-invariant control differs")
            if "parameters" in INTERVENTIONS[intervention] or intervention == "all":
                # For current BN/LN adapters forward buffers are identical by design.
                controls.append({"id":f"{stem}_w{w}_{intervention}_first_batch","passed":first_diff == 0.0,
                                 "max_logit_diff":first_diff})
                if first_diff != 0:
                    raise AssertionError("Parameter-reset first batch differs: hidden forward state or RNG")
    write_json(output / "controls" / f"{stem}.json", controls)
    write_json(output / "timing" / f"{stem}.json", overhead)
    return paired_rows, controls
