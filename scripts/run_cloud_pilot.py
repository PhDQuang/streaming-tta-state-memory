"""Run an already provisioned, explicitly approved cloud experiment.

Default is plan-only and does not load weights/data or use a payment API.
This script cannot rent a GPU. A provider instance must be obtained separately
after the user's explicit approval. The process has a configurable runtime cap.
"""
from __future__ import annotations

import argparse
import copy
import json
from pathlib import Path
import time
import traceback

import torch
import yaml

import _bootstrap
from prepare_data import CLASS_INDEX_SHA256
from historytta.adapters import make_adapter
from historytta.data import ImageLoader
from historytta.models import cloud_model
from historytta.runner import INTERVENTIONS, execute_panel, from_manifest
from historytta.utils import file_sha256, object_sha256, provenance, seed_all, write_json


def validate_backbone_config(config):
    """Keep saved weight provenance equal to the existing factory contract.

    Both supported historytta.models.cloud_model branches explicitly select V1;
    constructor-spy tests verify this without accessing a weight download.
    """
    if config.get("backbone") not in {"resnet50","vit_b_16"}:
        raise ValueError("Cloud model factory supports only resnet50 and vit_b_16")
    if config.get("weights")!="IMAGENET1K_V1":
        raise ValueError("Configured weights mismatch: the cloud model factory is pinned to IMAGENET1K_V1")


def load_configured_backbone(config):
    validate_backbone_config(config)
    return cloud_model(config["backbone"],pretrained=True)


def experiment_plan(config):
    validate_backbone_config(config)
    p=config["planning"]
    batch_size=config["adaptation"]["batch_size"]
    for name,value in {"batch_size":batch_size, **{k:p[k] for k in
                      ("independent_panels","scenarios_per_panel","prefix_images","suffix_images")}}.items():
        if type(value) is not int or value<=0:
            raise ValueError(f"{name} must be a positive integer")
    maximum=p["washout_images_max"]
    if type(maximum) is not int or maximum<0 or maximum%batch_size:
        raise ValueError("Maximum washout must contain whole nonnegative batches")
    if p["prefix_images"]%(2*batch_size) or p["suffix_images"]%batch_size:
        raise ValueError("Prefix must contain two equal whole-batch blocks and suffix whole batches")
    washes=config["washout_batches"]
    if not washes or len(set(washes))!=len(washes) or any(type(w) is not int or w<0 or w*batch_size>maximum for w in washes):
        raise ValueError("Washout lengths must be distinct nonnegative integers within the frozen tail")
    methods=config["methods"]
    if not methods or len(set(methods))!=len(methods) or not set(methods)<={"source","norm","tent","sar","sar_complete"}:
        raise ValueError("Methods must be distinct supported adapters")
    if "sar" in methods and "sar_complete" in methods:
        raise ValueError("sar and sar_complete name the same implementation and would overwrite outputs")
    interventions=config["interventions"]
    if not interventions or len(set(interventions))!=len(interventions) or not set(interventions)<=set(INTERVENTIONS):
        raise ValueError("Interventions must be distinct supported state resets")
    units=p["independent_panels"]*p["scenarios_per_panel"]
    arms=sum(2 if method in {"source","norm"} else len(config["interventions"]) for method in config["methods"])
    q_runs=units*len(config["washout_batches"])*2*arms
    junctions=(units*len(washes)*2*sum(method not in {"source","norm"} for method in methods)
               if config.get("save_junctions",False) else 0)
    return {"mode":"plan_only","config":config,"matrix":{
        "independent_image_panels":p["independent_panels"],"reused_scenarios_per_panel":p["scenarios_per_panel"],
        "unique_base_images":p["independent_panels"]*(p["prefix_images"]+p["washout_images_max"]+p["suffix_images"]),
        "paired_suffix_runs":q_runs//2,"directional_suffix_runs":q_runs,
        "main_suffix_image_forwards":q_runs*p["suffix_images"],
        "saved_junction_checkpoints":junctions,
        "model_state_copies_in_junctions":2*junctions,
        "junction_storage_note":"Each junction stores both current model state and the immutable source anchor, plus optimizer/auxiliary/RNG state. Budget approximately twice model-state bytes per junction, with additional serialization/state overhead.",
        "note":"Counts exclude histories, shared tails, parity/replay controls and SAR second forwards/backward computation."},
        "budget":{"gpu_hours":[p["gpu_hours_low"],p["gpu_hours_high"]],
        "gpu_cost_usd":[p["gpu_hours_low"]*p["observed_gpu_usd_per_hour"],p["gpu_hours_high"]*p["observed_gpu_usd_per_hour"]],
        "disk_gb":p["disk_gb"],"requested_ceiling_usd":p["requested_total_budget_usd"]}}


def load_index(path: Path, expected_batch_size: int, expected_planning: dict | None=None,
               *, dataset_profile="imagenet_c"):
    """Validate frozen content, statistical units, labels and all batch stages.

    Reused scenarios must retain the same H/W/Q identity pools inside a panel;
    distinct panel IDs must have disjoint original-image identities. Digests are
    checked against actual bytes even when a path was already read elsewhere.
    """
    if dataset_profile not in {"imagenet_c", "tiny_imagenet_c"}:
        raise ValueError("Unknown dataset profile")
    if type(expected_batch_size) is not int or expected_batch_size<=0:
        raise ValueError("Expected batch size must be a positive integer")
    path=Path(path)
    index=json.loads(path.read_text(encoding="utf-8"))
    body={k:v for k,v in index.items() if k!="sha256"}
    if index.get("sha256") != object_sha256(body):
        raise ValueError("Manifest index integrity mismatch")
    if index.get("schema_version")!=1 or not isinstance(index.get("panels"),list) or not index["panels"]:
        raise ValueError("Unsupported or empty manifest index schema")
    if index["metadata"].get("path_mode") != "absolute":
        raise ValueError("Cloud runner currently requires absolute paths; rebuild the manifest on the cloud machine")
    metadata=index["metadata"]
    if "batch_size" in metadata and metadata["batch_size"]!=expected_batch_size:
        raise ValueError("Index metadata batch size differs from experiment config")
    mapping=metadata.get("class_to_idx")
    if not isinstance(mapping,dict) or not mapping or (
            any(type(value) is not int for value in mapping.values()) or
            sorted(mapping.values())!=list(range(len(mapping)))):
        raise ValueError("Class mapping must contain unique contiguous zero-based indices")
    if not isinstance(metadata.get("model_class_names"),list) or len(metadata["model_class_names"])!=len(mapping):
        raise ValueError("Class mapping and model class names differ in length")
    if list(sorted(mapping,key=mapping.get))!=sorted(mapping):
        raise ValueError("Class mapping indices must follow sorted synset order")
    if "expected_classes" in metadata and metadata["expected_classes"]!=len(mapping):
        raise ValueError("Declared class count differs from the class mapping")
    if expected_planning is not None:
        tiny = dataset_profile == "tiny_imagenet_c"
        count = 200 if tiny else 1000
        if len(mapping)!=count or metadata.get("expected_classes")!=count:
            if tiny:
                raise ValueError("Tiny planning requires exactly 200 classes")
            raise ValueError("Production planning requires exactly 1000 ImageNet classes; fixture mappings are loader-only")
        if tiny and (metadata.get("dataset") != "Tiny ImageNet-C"
                     or metadata.get("dataset_profile") != dataset_profile):
            raise ValueError("Tiny planning requires an explicit Tiny dataset identity")
        if metadata.get("class_index_sha256")!=CLASS_INDEX_SHA256:
            raise ValueError("Production class mapping must declare the pinned canonical class-index digest")
    if "source_records_sha256" in metadata and metadata["source_records_sha256"]!=object_sha256(metadata.get("source_records")):
        raise ValueError("Source provenance record integrity mismatch")
    records=[]
    verified_images={}
    component_pools={}
    panel_seeds={}
    owner_by_id={}
    seen_outputs=set()
    stages=("history_ab","history_ba","washout","suffix")
    for record in index["panels"]:
        panel_id=record.get("panel_id")
        scenario=record.get("scenario")
        if not isinstance(panel_id,str) or not panel_id or not isinstance(scenario,str) or not scenario or type(record.get("seed")) is not int:
            raise ValueError("Every panel record needs a panel_id, scenario and integer seed")
        # Output filenames do not include severity; repeated conditions must use
        # an explicit new scenario/experiment instead of silently overwriting.
        output_key=(panel_id,scenario)
        if output_key in seen_outputs:
            raise ValueError("Duplicate panel/scenario output identity")
        seen_outputs.add(output_key)
        item=path.parent/record["path"]
        if file_sha256(item)!=record["file_sha256"]:
            raise ValueError("Panel file changed after manifest freeze")
        document=json.loads(item.read_text(encoding="utf-8"))
        if object_sha256({k:v for k,v in document.items() if k!="manifest_sha256"}) != document.get("manifest_sha256"):
            raise ValueError("Panel metadata integrity mismatch")
        if record.get("panel_sha256")!=document.get("sha256") or record.get("manifest_sha256")!=document.get("manifest_sha256"):
            raise ValueError("Index record and panel/manifest digest correspondence mismatch")
        panel_metadata=document.get("metadata",{})
        for name in ("panel_id","scenario","seed","severity"):
            if name in panel_metadata and panel_metadata[name]!=record.get(name):
                raise ValueError(f"Index record and document metadata {name} mismatch")
        for name in ("path_mode","batch_size","class_to_idx","model_class_names","expected_classes","class_index_sha256","source_records_sha256",
                     "dataset","dataset_profile","input_image_size","classifier","output_imagenet_indices","classifier_sha256"):
            if name in panel_metadata and panel_metadata[name]!=metadata.get(name):
                raise ValueError(f"Index and document metadata {name} mismatch")
        if "source_records_sha256" in panel_metadata and panel_metadata["source_records_sha256"]!=object_sha256(panel_metadata.get("source_records")):
            raise ValueError("Panel source provenance record integrity mismatch")
        panel=from_manifest(document)
        if any(len(batch)!=expected_batch_size for name in stages for batch in getattr(panel,name)):
            raise ValueError("Manifest batch size differs from experiment config")
        pools={name:frozenset(s.base_id for batch in getattr(panel,name) for s in batch)
               for name in ("history_ab","washout","suffix")}
        if panel_id in component_pools and pools!=component_pools[panel_id]:
            raise ValueError("Scenarios sharing a panel_id must reuse identical history/washout/suffix identity pools")
        if panel_id in panel_seeds and record["seed"]!=panel_seeds[panel_id]:
            raise ValueError("Scenarios sharing a panel_id must share the same seed")
        component_pools[panel_id]=pools
        panel_seeds[panel_id]=record["seed"]
        for base_id in set().union(*pools.values()):
            if base_id in owner_by_id and owner_by_id[base_id]!=panel_id:
                raise ValueError("Original-image overlap between distinct independent panel_ids")
            owner_by_id[base_id]=panel_id
        for key,name in (("prefix_size","history_ab"),("washout_size","washout"),("suffix_size","suffix")):
            if key in metadata and metadata[key]!=len(pools[name]):
                raise ValueError(f"Manifest {key} differs from declared index size")
        samples=[s for name in stages for batch in getattr(panel,name) for s in batch]
        sample_paths={s.path for s in samples}
        checksums=panel_metadata.get("image_sha256")
        if not isinstance(checksums,dict) or set(checksums)!=sample_paths:
            raise ValueError("Image hash coverage must exactly match all referenced sample paths")
        for sample in samples:
            if not sample.path or not Path(sample.path).is_absolute():
                raise ValueError("Every cloud sample requires an absolute image path")
            if sample.base_id!=Path(sample.path).name:
                raise ValueError("Original-image base_id must match the image basename")
            if type(sample.label) is not int or sample.label not in mapping.values():
                raise ValueError("Evaluator label is outside the declared class mapping")
            if mapping.get(Path(sample.path).parent.name)!=sample.label:
                raise ValueError("Evaluator label does not match image synset and class mapping")
        for image_path,digest in checksums.items():
            canonical=Path(image_path).resolve()
            if canonical not in verified_images:
                verified_images[canonical]=file_sha256(canonical)
            if verified_images[canonical]!=digest:
                raise ValueError("Image content changed after manifest freeze or conflicting repeated-path digest")
        records.append((record,panel,document))
    if expected_planning is not None:
        p=expected_planning
        if len(component_pools)!=p["independent_panels"]:
            raise ValueError("Independent panel count differs from experiment plan")
        condition_sets={panel_id:{scenario for ident,scenario in seen_outputs if ident==panel_id}
                        for panel_id in component_pools}
        reference_conditions=next(iter(condition_sets.values()))
        if any(len(conditions)!=p["scenarios_per_panel"] or conditions!=reference_conditions for conditions in condition_sets.values()):
            raise ValueError("Each independent panel must have the same planned scenario set")
        for pools in component_pools.values():
            for key,name in (("prefix_images","history_ab"),("washout_images_max","washout"),("suffix_images","suffix")):
                if len(pools[name])!=p[key]:
                    raise ValueError(f"Actual {key} differs from experiment plan")
    return index,records


def run_experiment(cfg, max_hours, *, index_loader=None, backbone_loader=None):
    """Shared execution; custom dataset/model loaders must verify their contract."""
    plan=experiment_plan(cfg)
    stage = cfg["stage"]
    if not torch.cuda.is_available() or cfg["device"]!="cuda":
        raise RuntimeError("Cloud execution requires a CUDA GPU; local CPU is only for sanity checks")
    if max_hours<=0 or max_hours>16:
        raise ValueError("Pilot process cap must be in (0,16] hours; larger runs need a separately approved plan")
    index_path=Path(cfg["manifest_index"])
    if index_loader is None:
        index,records=load_index(index_path,cfg["adaptation"]["batch_size"],expected_planning=cfg["planning"])
    else:
        index,records=index_loader(cfg)
    if len(records)!=cfg["planning"]["independent_panels"]*cfg["planning"]["scenarios_per_panel"]:
        raise ValueError("Unexpected pilot matrix; verify frozen manifest/config")
    output=Path(cfg["output"])
    if output.exists() and any(output.iterdir()):
        raise FileExistsError("Existing experiment retained; use an explicit new ID for another attempt")
    output.mkdir(parents=True,exist_ok=True)
    write_json(output/"provenance.json",provenance(cfg))
    write_json(output/"plan.json",plan)
    write_json(output/"manifest_index.json",index)
    started=time.perf_counter()
    write_json(output/"run_status.json",{"status":"running","stage":stage})
    controls=[]
    try:
        seed_all(20260908,cfg["threads"])
        model,transform=load_configured_backbone(cfg) if backbone_loader is None else backbone_loader(cfg,index)
        anchor=output/"source_anchor.pt"
        torch.save({"model":model.state_dict(),"backbone":cfg["backbone"],"weights":cfg["weights"],
                    "dataset":index["metadata"].get("dataset"),
                    "output_imagenet_indices":index["metadata"].get("output_imagenet_indices")},anchor)
        source_info={"path":str(anchor.resolve()),"sha256":file_sha256(anchor),"config_sha256":object_sha256(cfg)}
        loader=ImageLoader(transform)
        for record,panel,document in records:
            for method in cfg["methods"]:
                if (time.perf_counter()-started)/3600>=max_hours:
                    raise TimeoutError("Process runtime cap reached. Provider must still be stopped separately.")
                seed_all(record["seed"],cfg["threads"])
                settings={k:v for k,v in cfg["adaptation"].items() if k!="batch_size"}
                adapter=make_adapter(copy.deepcopy(model).to(cfg["device"]),method,**settings)
                torch.cuda.reset_peak_memory_stats()
                _,checks=execute_panel(adapter,panel,loader,output,
                    {"experiment_id":cfg["experiment_id"],"seed":record["seed"],"panel_id":record["panel_id"],"scenario":record["scenario"]},
                    cfg["washout_batches"], ["none","all"] if method in {"source","norm"} else cfg["interventions"],
                    device=cfg["device"],save_images=False,verify_replay=True,
                    save_junctions=cfg["save_junctions"] and method not in {"source","norm"},source_checkpoint=source_info)
                controls.extend(checks)
                write_json(output/"controls.json",controls)
                write_json(output/"memory"/f'{record["panel_id"]}_{record["scenario"]}_{method}.json',
                    {"peak_allocated_bytes":torch.cuda.max_memory_allocated(),"peak_reserved_bytes":torch.cuda.max_memory_reserved()})
                print(f'{record["panel_id"]} {record["scenario"]} {method} completed',flush=True)
                del adapter
                torch.cuda.empty_cache()
        write_json(output/"run_status.json",{"status":"complete","stage":stage,"seconds":time.perf_counter()-started,
            "controls_passed":sum(c["passed"] for c in controls),"controls_total":len(controls),
            "interpretation":cfg.get("interpretation", "Underpowered pilot; report findings and variance before any full-stage approval")})
    except Exception:
        write_json(output/"run_status.json",{"status":"failed","stage":stage,"seconds":time.perf_counter()-started,
                                           "traceback":traceback.format_exc()})
        raise


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--config",type=Path,default=Path("configs/cloud_pilot.yaml"))
    p.add_argument("--execute",action="store_true")
    p.add_argument("--max-hours",type=float,default=16.0,help="Experiment-process cap, NOT a provider billing shutdown")
    args=p.parse_args()
    cfg=yaml.safe_load(args.config.read_text(encoding="utf-8"))
    plan=experiment_plan(cfg)
    if not args.execute:
        print(json.dumps(plan,indent=2))
        return
    run_experiment(cfg,args.max_hours)


if __name__=="__main__":
    main()
