"""Read-only cloud planning and integrity checks using tiny local byte fixtures."""
import copy
import importlib.util
import json
from pathlib import Path
import sys

import pytest
import yaml

from historytta.streams import Sample, make_panel
from historytta.utils import file_sha256, object_sha256

SCRIPT_DIR=Path(__file__).resolve().parents[1]/"scripts"
sys.path.insert(0,str(SCRIPT_DIR))
spec=importlib.util.spec_from_file_location("cloud_plan_under_test",SCRIPT_DIR/"run_cloud_pilot.py")
cloud=importlib.util.module_from_spec(spec)
spec.loader.exec_module(cloud)
STAGES=("history_ab","history_ba","washout","suffix")


def freeze_index(path,index):
    index["sha256"]=object_sha256({k:v for k,v in index.items() if k!="sha256"})
    path.write_text(json.dumps(index),encoding="utf-8")


def freeze_document(index_path,index,position,document):
    document["sha256"]=object_sha256({name:document[name] for name in STAGES})
    document["manifest_sha256"]=object_sha256({k:v for k,v in document.items() if k!="manifest_sha256"})
    record=index["panels"][position]
    item=index_path.parent/record["path"]
    item.write_text(json.dumps(document),encoding="utf-8")
    record.update(panel_sha256=document["sha256"],manifest_sha256=document["manifest_sha256"],file_sha256=file_sha256(item))
    freeze_index(index_path,index)


def document_at(path,index,position):
    return json.loads((path.parent/index["panels"][position]["path"]).read_text())


def make_index(tmp_path,batch_size=2,class_count=1000):
    path=tmp_path/"index.json"
    # Synthetic metadata exercises production-shape guards; no claim that these
    # artificial synsets constitute the real canonical ImageNet mapping.
    metadata={"path_mode":"absolute","batch_size":batch_size,
              "class_to_idx":{f"n{i+1:08d}":i for i in range(class_count)},
              "model_class_names":[f"fixture class {i}" for i in range(class_count)],
              "expected_classes":class_count,"class_index_sha256":cloud.CLASS_INDEX_SHA256,
              "prefix_size":2*batch_size,"washout_size":batch_size,"suffix_size":batch_size}
    index={"schema_version":1,"metadata":metadata,"panels":[]}
    for p in range(2):
        for scenario in ("noise_to_blur","brightness_to_blur"):
            def factory(i,domain):
                image=tmp_path/"images"/domain/"n00000001"/f"image_{i}.JPEG"
                image.parent.mkdir(parents=True,exist_ok=True)
                image.write_bytes(f"deterministic image bytes {i} {domain}".encode())
                return Sample(image.name,domain,5,str(image.resolve()),0)
            start=p*4*batch_size
            panel=make_panel(range(start,start+2*batch_size),range(start+2*batch_size,start+3*batch_size),
                             range(start+3*batch_size,start+4*batch_size),("a","b"),"c",batch_size,p+17,factory)
            document=panel.manifest()
            checksums={s.path:file_sha256(s.path) for name in STAGES for batch in getattr(panel,name) for s in batch}
            document["metadata"]={**metadata,"panel_id":f"panel_{p}","seed":p+17,"scenario":scenario,
                                  "severity":5,"image_sha256":checksums}
            index["panels"].append({"panel_id":f"panel_{p}","seed":p+17,"scenario":scenario,
                                    "severity":5,"path":f"panel_{p}_{scenario}.json"})
            freeze_document(path,index,len(index["panels"])-1,document)
    planning={"independent_panels":2,"scenarios_per_panel":2,"prefix_images":2*batch_size,
              "washout_images_max":batch_size,"suffix_images":batch_size}
    return path,index,planning


def test_cloud_plan_counts_and_never_loads_weights_or_images(monkeypatch):
    def forbidden(*args,**kwargs):
        raise AssertionError("Planning must not load a model or image")
    monkeypatch.setattr(cloud,"cloud_model",forbidden)
    monkeypatch.setattr(cloud,"ImageLoader",forbidden)
    config=yaml.safe_load((SCRIPT_DIR.parent/"configs"/"cloud_pilot.yaml").read_text())
    plan=cloud.experiment_plan(config)
    assert plan["mode"]=="plan_only"
    assert plan["matrix"]["unique_base_images"]==7680
    assert plan["matrix"]["directional_suffix_runs"]==1188
    assert plan["matrix"]["paired_suffix_runs"]==594
    assert plan["matrix"]["saved_junction_checkpoints"]==108
    assert plan["matrix"]["model_state_copies_in_junctions"]==216


@pytest.mark.parametrize("key,value",[("prefix_images",1000),("suffix_images",1000),("washout_images_max",500),
                                      ("independent_panels",0),("scenarios_per_panel",2.5)])
def test_plan_rejects_incoherent_matrix(key,value):
    config=yaml.safe_load((SCRIPT_DIR.parent/"configs"/"cloud_pilot.yaml").read_text())
    config["planning"][key]=value
    with pytest.raises(ValueError):
        cloud.experiment_plan(config)


def test_plan_rejects_out_of_tail_washout_and_adapter_alias_collision():
    config=yaml.safe_load((SCRIPT_DIR.parent/"configs"/"cloud_pilot.yaml").read_text())
    config["washout_batches"]=[0,4,17]
    with pytest.raises(ValueError,match="Washout"):
        cloud.experiment_plan(config)
    config["washout_batches"]=[0,4,16]
    config["methods"].append("sar")
    with pytest.raises(ValueError,match="same implementation"):
        cloud.experiment_plan(config)


def test_b32_full_index_all_stages_and_reused_scenarios(tmp_path):
    path,index,planning=make_index(tmp_path,batch_size=32)
    loaded,records=cloud.load_index(path,32,expected_planning=planning)
    assert loaded==index and len(records)==4
    assert all(len(batch)==32 for _,panel,_ in records for name in STAGES for batch in getattr(panel,name))
    document=document_at(path,index,0)
    for name in ("history_ab","history_ba"):
        document[name]=[batch[:16] for batch in document[name]]
    freeze_document(path,index,0,document)
    with pytest.raises(ValueError,match="equal-sized"):
        cloud.load_index(path,32,expected_planning=planning)


def test_manifest_builder_output_passes_cloud_validation(tmp_path):
    import prepare_data as prep
    root=tmp_path/"images"
    for domain in sorted({d for scenario in prep.SCENARIOS for d in scenario}):
        folder=root/domain/"5"/"n00000001"
        folder.mkdir(parents=True)
        for i in range(1,201):
            (folder/f"ILSVRC2012_val_{i:08d}.JPEG").write_bytes(f"fixture {domain} {i}".encode())
    classes=tmp_path/"classes.json"
    classes.write_text(json.dumps({"0":["n00000001","class fixture"]}))
    source=[{"archives":[{"filename":"fixture.tar","sha256":"1"*64}]}]
    index=prep.build_manifests(root,tmp_path/"panels",classes,seeds=(101,202),prefix_size=4,
          washout_size=2,suffix_size=2,batch_size=2,expected_classes=1,source_records=source)
    loaded,records=cloud.load_index(tmp_path/"panels"/"index.json",2)
    assert loaded==index and len(records)==6


@pytest.mark.parametrize("field,value",[("panel_sha256","0"*64),("manifest_sha256","0"*64),
                                        ("panel_id","renamed"),("scenario","other"),("seed",999),("severity",4)])
def test_index_record_must_match_document_even_after_index_is_rehashed(tmp_path,field,value):
    path,index,_=make_index(tmp_path)
    index["panels"][0][field]=value
    freeze_index(path,index)
    with pytest.raises(ValueError,match="correspondence|metadata"):
        cloud.load_index(path,2)


def test_distinct_panel_ids_cannot_hide_reused_images(tmp_path):
    path,index,_=make_index(tmp_path)
    first=document_at(path,index,0)
    other=document_at(path,index,2)
    for name in STAGES:
        other[name]=copy.deepcopy(first[name])
    other["metadata"]["image_sha256"]=first["metadata"]["image_sha256"]
    freeze_document(path,index,2,other)
    with pytest.raises(ValueError,match="overlap between distinct"):
        cloud.load_index(path,2)


def test_same_panel_scenarios_cannot_move_images_between_roles(tmp_path):
    path,index,_=make_index(tmp_path)
    document=document_at(path,index,1)
    document["washout"],document["suffix"]=document["suffix"],document["washout"]
    freeze_document(path,index,1,document)
    with pytest.raises(ValueError,match="identity pools"):
        cloud.load_index(path,2)


@pytest.mark.parametrize("mode",["missing","empty","conflicting_cached_digest"])
def test_hash_coverage_and_repeated_path_digests_are_never_skipped(tmp_path,mode):
    path,index,_=make_index(tmp_path)
    document=document_at(path,index,1)
    checksums=document["metadata"]["image_sha256"]
    image=next(iter(checksums))
    if mode=="missing":
        del checksums[image]
    elif mode=="empty":
        document["metadata"]["image_sha256"]={}
    else:
        checksums[image]="0"*64
    freeze_document(path,index,1,document)
    with pytest.raises(ValueError,match="hash coverage|conflicting repeated-path"):
        cloud.load_index(path,2)


def test_actual_image_bytes_and_document_bytes_are_verified(tmp_path):
    path,index,_=make_index(tmp_path)
    document=document_at(path,index,0)
    image=Path(next(iter(document["metadata"]["image_sha256"])))
    original=image.read_bytes()
    image.write_bytes(b"changed after freeze")
    with pytest.raises(ValueError,match="Image content"):
        cloud.load_index(path,2)
    image.write_bytes(original)
    item=path.parent/index["panels"][0]["path"]
    item.write_text(item.read_text()+" ")
    with pytest.raises(ValueError,match="Panel file changed"):
        cloud.load_index(path,2)


@pytest.mark.parametrize("key,value",[("independent_panels",3),("scenarios_per_panel",3),
                                      ("prefix_images",8),("washout_images_max",4),("suffix_images",4)])
def test_actual_matrix_must_match_planned_statistical_units_and_sizes(tmp_path,key,value):
    path,_,planning=make_index(tmp_path)
    planning[key]=value
    with pytest.raises(ValueError,match="plan|planned"):
        cloud.load_index(path,2,expected_planning=planning)


def test_duplicate_output_identity_and_invalid_class_mapping(tmp_path):
    path,index,_=make_index(tmp_path)
    index["panels"].append(copy.deepcopy(index["panels"][0]))
    freeze_index(path,index)
    with pytest.raises(ValueError,match="Duplicate"):
        cloud.load_index(path,2)
    index["panels"].pop()
    index["metadata"]["class_to_idx"]={"n00000001":1}
    freeze_index(path,index)
    with pytest.raises(ValueError,match="zero-based"):
        cloud.load_index(path,2)


def test_unsupported_schema_and_invalid_evaluator_labels(tmp_path):
    path,index,_=make_index(tmp_path)
    index["schema_version"]=2
    freeze_index(path,index)
    with pytest.raises(ValueError,match="schema"):
        cloud.load_index(path,2)
    index["schema_version"]=1
    document=document_at(path,index,0)
    document["suffix"][0][0]["label"]=3
    freeze_document(path,index,0,document)
    with pytest.raises(ValueError,match="Evaluator label"):
        cloud.load_index(path,2)


def test_tiny_class_fixture_allowed_only_without_production_planning(tmp_path):
    path,_,planning=make_index(tmp_path,class_count=2)
    _,records=cloud.load_index(path,2)
    assert len(records)==4
    with pytest.raises(ValueError,match="exactly 1000"):
        cloud.load_index(path,2,expected_planning=planning)


def test_production_rejects_unpinned_mapping_digest_and_wrong_synset_order(tmp_path):
    path,index,planning=make_index(tmp_path)
    index["metadata"]["class_index_sha256"]="0"*64
    freeze_index(path,index)
    with pytest.raises(ValueError,match="pinned canonical"):
        cloud.load_index(path,2,expected_planning=planning)
    index["metadata"]["class_index_sha256"]=cloud.CLASS_INDEX_SHA256
    mapping=index["metadata"]["class_to_idx"]
    mapping["n00000001"],mapping["n00000002"]=mapping["n00000002"],mapping["n00000001"]
    freeze_index(path,index)
    with pytest.raises(ValueError,match="sorted synset"):
        cloud.load_index(path,2,expected_planning=planning)


@pytest.mark.parametrize("backbone,enum_name",[("resnet50","ResNet50_Weights"),("vit_b_16","ViT_B_16_Weights")])
def test_actual_factory_requests_configured_weight_enum_without_download(monkeypatch,backbone,enum_name):
    from torchvision import models
    sentinel=object()
    requested=[]
    def constructor(*,weights):
        requested.append(weights)
        return sentinel
    monkeypatch.setattr(models,backbone,constructor)
    model,transform=cloud.load_configured_backbone({"backbone":backbone,"weights":"IMAGENET1K_V1"})
    assert model is sentinel
    assert requested==[getattr(models,enum_name).IMAGENET1K_V1]
    assert callable(transform)


@pytest.mark.parametrize("wrong_weights",["IMAGENET1K_V2","DEFAULT",None])
def test_weight_mismatch_fails_before_factory_or_download(monkeypatch,wrong_weights):
    def forbidden(*args,**kwargs):
        raise AssertionError("Mismatched weights reached the factory")
    monkeypatch.setattr(cloud,"cloud_model",forbidden)
    config=yaml.safe_load((SCRIPT_DIR.parent/"configs"/"cloud_pilot.yaml").read_text())
    config["weights"]=wrong_weights
    with pytest.raises(ValueError,match="Configured weights mismatch"):
        cloud.experiment_plan(config)
    with pytest.raises(ValueError,match="Configured weights mismatch"):
        cloud.load_configured_backbone(config)
