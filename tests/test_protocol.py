import copy
import importlib.util
from pathlib import Path

import numpy as np
import pytest
import torch

from historytta.adapters import make_adapter
from historytta.data import corrupt_digit, fixed_split
from historytta.metrics import prediction_metrics, paired_summary, holm
from historytta.models import DigitCNN
from historytta.runner import execute_panel, from_manifest
from historytta.streams import Sample, StreamPanel, make_panel
from historytta.utils import seed_all


def test_prefix_multiset_and_base_id_disjointness():
    p = make_panel(list(range(8)), list(range(8,12)), list(range(12,16)), ("noise","blur"), "clean", 2, 4)
    assert from_manifest(p.manifest()) == p
    leaked = StreamPanel(p.history_ab,p.history_ba,p.washout,p.history_ab[:2])
    with pytest.raises(ValueError,match="leakage"):
        leaked.validate()
    changed = copy.deepcopy(p.manifest())
    changed["suffix"][0][0]["domain"]="changed"
    with pytest.raises(ValueError,match="integrity"):
        from_manifest(changed)


def test_reject_rebatched_history_even_same_image_multiset():
    p = make_panel(list(range(8)), [], list(range(8,12)), ("noise","blur"), "clean", 2, 4)
    shuffled = list(p.history_ba)
    shuffled[0],shuffled[1] = ((shuffled[0][0],shuffled[1][0]),(shuffled[0][1],shuffled[1][1]))
    with pytest.raises(ValueError,match="preformed"):
        StreamPanel(p.history_ab,tuple(shuffled),p.washout,p.suffix).validate()


def test_metrics_known_probabilities_and_signed_intervals():
    probs=torch.tensor([[.75,.25],[.25,.75]],dtype=torch.double)
    m=prediction_metrics(probs.log(),torch.tensor([0,0]))
    assert m["accuracy"] == .5
    assert m["nll"] == pytest.approx(-np.log(.75*.25)/2)
    assert m["brier"] == pytest.approx(.625)
    assert m["ece15"] == pytest.approx(.25)
    assert paired_summary([0,0,0])["ci_low"] == 0
    assert paired_summary([.2])["ci_low"] is None
    assert holm([.01,.04,.03]) == pytest.approx([.03,.06,.06])


def test_split_and_corruption_reproducibility():
    split=fixed_split(30,1,{"train":10,"prefix":10,"suffix":10})
    assert len(set(sum(split.values(),[]))) == 30
    x=torch.ones(1,8,8)/2
    assert torch.equal(corrupt_digit(x,"noise",10),corrupt_digit(x,"noise",10))
    assert not torch.equal(corrupt_digit(x,"noise",10),corrupt_digit(x,"noise",11))


def test_end_to_end_label_isolation_and_complete_controls(tmp_path):
    seed_all(19)
    model=DigitCNN().eval()
    x=torch.rand(20,1,8,8)
    factory=lambda i,d:Sample(str(i),d,label=i%10)
    panel=make_panel(list(range(8)),list(range(8,12)),list(range(12,20)),("noise","brightness"),"clean",2,7,factory)
    loader=lambda s:corrupt_digit(x[int(s.base_id)],s.domain,int(s.base_id))
    adapter=make_adapter(model,"tent",lr=.001)
    rows,controls=execute_panel(adapter,panel,loader,tmp_path,
         {"experiment_id":"test","seed":1,"panel_id":"test","scenario":"s"},(0,2),["none","parameters","all"])
    assert all(c["passed"] for c in controls)
    assert len(rows)==6
    assert (tmp_path/"paired.csv").exists()
    # Swapping evaluator labels must never alter predictions or trajectory.
    label_changed=StreamPanel(**{name:tuple(tuple(Sample(s.base_id,s.domain,label=(s.label+1)%10) for s in b)
                         for b in getattr(panel,name)) for name in ("history_ab","history_ba","washout","suffix")})
    other=tmp_path/"label_swapped"
    adapter.reset_components(["all"])
    execute_panel(adapter,label_changed,loader,other,
         {"experiment_id":"test","seed":1,"panel_id":"test","scenario":"s"},(0,2),["none","parameters","all"])
    for original in (tmp_path/"predictions").glob("*.npz"):
        with np.load(original) as a,np.load(other/"predictions"/original.name) as b:
            assert np.array_equal(a["logits"],b["logits"])


def test_washout_uses_last_batches(tmp_path):
    seed_all(1)
    panel=make_panel(list(range(4)),list(range(4,10)),list(range(10,14)),("a","b"),"c",2,1,
                     lambda i,d:Sample(str(i),d,label=i%10))
    seen=[]
    def loader(s):
        seen.append(int(s.base_id))
        return torch.zeros(1,8,8)
    execute_panel(make_adapter(DigitCNN(),"source"),panel,loader,tmp_path,
           {"experiment_id":"test","seed":1,"panel_id":"test","scenario":"s"},(1,),["none"],verify_replay=False)
    # Each direction sees prefix then LAST washout batch (IDs 8/9), not first 4/5.
    assert seen[:6][-2:] == [8,9]
    assert 4 not in seen and 5 not in seen
