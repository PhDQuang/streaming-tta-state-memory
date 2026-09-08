"""Stage A only: real images from UCI's official training partition."""
from __future__ import annotations
import argparse
import copy
from pathlib import Path
import time
import traceback

import torch
from torch.utils.data import DataLoader, TensorDataset
import yaml

import _bootstrap
from historytta.adapters import make_adapter
from historytta.data import DigitLoader, fixed_split, load_uci_train
from historytta.models import DigitCNN
from historytta.runner import append_csv, execute_panel
from historytta.streams import Sample, make_panel
from historytta.utils import provenance, seed_all, write_json, file_sha256


def train_source(images, labels, split, seed, config, output):
    checkpoint = output / "checkpoints" / f'{config["experiment_id"]}_source_{seed}.pt'
    if checkpoint.exists():
        raise FileExistsError(f"Refusing to overwrite immutable source checkpoint: {checkpoint}")
    seed_all(seed, config["threads"])
    model = DigitCNN()
    cfg = config["training"]
    generator = torch.Generator().manual_seed(seed)
    dl = DataLoader(TensorDataset(images[split["source_train"]], labels[split["source_train"]]),
                    batch_size=cfg["batch_size"],shuffle=True,generator=generator,num_workers=0)
    optimizer = torch.optim.Adam(model.parameters(),lr=cfg["lr"])
    for epoch in range(1,cfg["epochs"]+1):
        start = time.perf_counter()
        model.train()
        loss_total = 0.0
        for x,y in dl:
            optimizer.zero_grad(set_to_none=True)
            loss = torch.nn.functional.cross_entropy(model(x),y)
            loss.backward()
            optimizer.step()
            loss_total += loss.item()*len(y)
        model.eval()
        with torch.no_grad():
            accuracy = model(images[split["source_dev"]]).argmax(1).eq(labels[split["source_dev"]]).float().mean().item()
        append_csv(output/"training.csv",{"seed":seed,"epoch":epoch,"train_loss":loss_total/len(split["source_train"]),
                                          "dev_accuracy":accuracy,"seconds":time.perf_counter()-start})
    # Fixed final epoch, no best-checkpoint or test selection.
    checkpoint.parent.mkdir(parents=True, exist_ok=True)
    torch.save({"model":model.state_dict(),"seed":seed,"config":cfg,"split":split},checkpoint)
    restored = DigitCNN()
    restored.load_state_dict(torch.load(checkpoint,map_location="cpu",weights_only=True)["model"])
    restored.eval()
    with torch.no_grad():
        if not torch.equal(model(images[:4]),restored(images[:4])):
            raise AssertionError("Source checkpoint roundtrip mismatch")
    return restored,checkpoint,accuracy


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--config",type=Path,default=Path("configs/sanity.yaml"))
    args=p.parse_args()
    config=yaml.safe_load(args.config.read_text(encoding="utf-8"))
    output=Path(config["output"])
    if output.exists() and any(output.iterdir()):
        raise FileExistsError(f"Refusing to overwrite existing experiment: {output}; choose a new experiment ID/output")
    output.mkdir(parents=True,exist_ok=True)
    write_json(output/"provenance.json",provenance(config))
    write_json(output/"run_status.json",{"status":"running","stage":"A","scientific_claims":"correctness only"})
    all_controls=[]
    start=time.perf_counter()
    try:
        images,labels=load_uci_train(config["data"])
        split=fixed_split(len(images),config["split_seed"],config["counts"])
        write_json(output/"split.json",split)
        checkpoints=[]
        for seed in config["source_seeds"]:
            model,checkpoint,dev_acc=train_source(images,labels,split,seed,config,output)
            checkpoints.append({"seed":seed,"path":checkpoint.as_posix(),"sha256":file_sha256(checkpoint),"dev_accuracy":dev_acc})
            print(f"Source seed={seed}: final clean development accuracy={dev_acc:.4f}",flush=True)
            loader=DigitLoader(images,config["split_seed"])
            for scenario in config["scenarios"]:
                factory=lambda i,d: Sample(str(i),d,label=int(labels[int(i)]))
                panel=make_panel(split["prefix"],split["washout"],split["suffix"],tuple(scenario["domains"]),
                                 scenario["suffix_domain"],config["adaptation"]["batch_size"],config["split_seed"],factory)
                for method in config["methods"]:
                    seed_all(seed,config["threads"])
                    settings={k:v for k,v in config["adaptation"].items() if k != "batch_size"}
                    adapter=make_adapter(copy.deepcopy(model),method,**settings)
                    _,controls=execute_panel(adapter,panel,loader,output,
                        {"experiment_id":config["experiment_id"],"seed":seed,"panel_id":"uci_internal_fixed","scenario":scenario["name"]},
                        config["washout_batches"], ["none","all"] if method in {"source","norm"} else config["interventions"],
                        save_images=True)
                    all_controls.extend(controls)
                    write_json(output/"controls.json",all_controls)
                    print(f"  {scenario['name']} {method}: {len(controls)} controls passed",flush=True)
        write_json(output/"checkpoints.json",checkpoints)
        write_json(output/"run_status.json",{"status":"complete","stage":"A","seconds":time.perf_counter()-start,
                   "controls_passed":sum(c["passed"] for c in all_controls),"controls_total":len(all_controls),
                   "scientific_claims":"training-only local correctness; no ImageNet generalization evidence"})
    except Exception:
        write_json(output/"run_status.json",{"status":"failed","stage":"A","seconds":time.perf_counter()-start,"traceback":traceback.format_exc()})
        raise


if __name__=="__main__":
    main()
