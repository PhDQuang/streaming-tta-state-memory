"""Data-integrity controls, archive attack rejection, and pilot-ID isolation."""
import hashlib
import importlib.util
import io
import json
import sys
import tarfile
from pathlib import Path
from types import SimpleNamespace

import pytest

SCRIPT_DIR = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPT_DIR))
spec = importlib.util.spec_from_file_location("prepare_data", SCRIPT_DIR / "prepare_data.py")
prep = importlib.util.module_from_spec(spec)
spec.loader.exec_module(prep)


def make_archive(path, members):
    with tarfile.open(path, "w") as tar:
        for member, payload in members:
            if isinstance(member, str):
                info = tarfile.TarInfo(member)
                info.size = len(payload)
            else:
                info = member
            tar.addfile(info, io.BytesIO(payload) if info.isreg() else None)
    return {path.name: {"sha256": prep.file_sha256(path)}}


def image_path(domain="gaussian_noise", severity=5, index=1, synset="n00000001"):
    return f"{domain}/{severity}/{synset}/ILSVRC2012_val_{index:08d}.JPEG"


def test_extract_selects_severity_partition_and_is_idempotent(tmp_path):
    members = [(image_path(index=i, severity=s), f"JPEG{i}-{s}".encode())
               for i in range(1, 51) for s in (3, 5)]
    members.append(("harmless_readme.txt", b"do not extract"))
    archive = tmp_path / "tiny.tar"
    checksums = make_archive(archive, members)
    target = tmp_path / "images"
    options = dict(severities=(5,), partition="pilot", reserve_bytes=0, expected_checksums=checksums)
    plan = prep.extract_archives([archive], target, ["gaussian_noise"], **options)
    assert plan["executed"] is False and not target.exists()
    result = prep.extract_archives([archive], target, ["gaussian_noise"], execute=True, **options)
    paths = list(target.rglob("*.JPEG"))
    assert paths and len(paths) == result["selected_files"]
    assert all(prep.split_role(path.name) == "pilot" for path in paths)
    assert not (target / "gaussian_noise" / "3").exists()
    assert not (target / "harmless_readme.txt").exists()
    first_provenance = Path(result["provenance"]).read_bytes()
    again = prep.extract_archives([archive], target, ["gaussian_noise"], execute=True, **options)
    assert Path(again["provenance"]).read_bytes() == first_provenance
    paths[0].write_bytes(b"tampered")
    with pytest.raises(FileExistsError, match="nonidentical"):
        prep.extract_archives([archive], target, ["gaussian_noise"], execute=True, **options)
    assert paths[0].read_bytes() == b"tampered"


@pytest.mark.parametrize("badname", ["../escape", "/absolute", "C:/escape", "a\\escape", "ok/../../escape", "a/NUL"])
def test_hostile_path_rejected_before_any_extraction(tmp_path, badname):
    archive = tmp_path / "tiny.tar"
    checksums = make_archive(archive, [(image_path(), b"valid"), (badname, b"bad")])
    target = tmp_path / "images"
    with pytest.raises(ValueError):
        prep.extract_archives([archive], target, ["gaussian_noise"], execute=True,
                              reserve_bytes=0, expected_checksums=checksums)
    assert not target.exists()


@pytest.mark.parametrize("kind", [tarfile.SYMTYPE, tarfile.LNKTYPE, tarfile.CHRTYPE, tarfile.BLKTYPE, tarfile.FIFOTYPE])
def test_unselected_links_and_devices_rejected(tmp_path, kind):
    special = tarfile.TarInfo("unselected/special")
    special.type = kind
    special.linkname = "../../escape"
    archive = tmp_path / "tiny.tar"
    checksums = make_archive(archive, [(image_path(), b"valid"), (special, b"")])
    with pytest.raises(ValueError, match="special"):
        prep.extract_archives([archive], tmp_path / "out", ["gaussian_noise"], execute=True,
                              reserve_bytes=0, expected_checksums=checksums)
    assert not (tmp_path / "out").exists()


def test_duplicate_archive_member_and_checksum_failure(tmp_path):
    archive = tmp_path / "tiny.tar"
    checksums = make_archive(archive, [(image_path(), b"one"), (image_path(), b"two")])
    with pytest.raises(ValueError, match="Duplicate"):
        prep.extract_archives([archive], tmp_path / "out", ["gaussian_noise"],
                              reserve_bytes=0, expected_checksums=checksums)
    with pytest.raises(ValueError, match="sha256 mismatch"):
        prep.archive_checksum(archive, {archive.name: {"sha256": "0" * 64}})


def test_disk_check_blocks_extraction(tmp_path, monkeypatch):
    archive = tmp_path / "tiny.tar"
    checksums = make_archive(archive, [(image_path(), b"payload")])
    monkeypatch.setattr(prep.shutil, "disk_usage", lambda _: SimpleNamespace(free=1))
    with pytest.raises(OSError, match="Insufficient"):
        prep.extract_archives([archive], tmp_path / "out", ["gaussian_noise"], execute=True,
                              reserve_bytes=0, expected_checksums=checksums)
    assert not (tmp_path / "out").exists()


def fake_data(tmp_path, count=200):
    root = tmp_path / "images"
    mapping_path = tmp_path / "classes.json"
    mapping_path.write_text(json.dumps({"0": ["n00000001", "first"], "1": ["n00000002", "second"]}))
    for domain in sorted({c for scenario in prep.SCENARIOS for c in scenario}):
        for synset in ("n00000001", "n00000002"):
            (root / domain / "5" / synset).mkdir(parents=True)
        for i in range(1, count + 1):
            path = root / image_path(domain=domain, index=i, synset=f"n0000000{1 + i % 2}")
            path.write_bytes(f"jpeg fixture {i} {domain}".encode())
    source = [{"archives": [{"filename": "fixture.tar", "sha256": "1" * 64}], "partition": "all"}]
    return root, mapping_path, source


def build_tiny(tmp_path, root, mapping, source, **kwargs):
    options = dict(prefix_size=4, washout_size=2, suffix_size=4, batch_size=2,
                   expected_classes=2, source_records=source)
    options.update(kwargs)
    return prep.build_manifests(root, tmp_path / "panels", mapping, **options)


def flatten_ids(document, component):
    return [s["base_id"] for b in document[component] for s in b]


def test_pilot_panels_are_disjoint_and_immutable(tmp_path):
    root, mapping, source = fake_data(tmp_path)
    index = build_tiny(tmp_path, root, mapping, source)
    assert len(index["panels"]) == 9
    by_seed = {}
    for entry in index["panels"]:
        path = tmp_path / "panels" / entry["path"]
        assert prep.file_sha256(path) == entry["file_sha256"]
        document = json.loads(path.read_text())
        payload = {k: document[k] for k in ("history_ab", "history_ba", "washout", "suffix")}
        assert prep.object_sha256(payload) == document["sha256"]
        original_sha = document.pop("manifest_sha256")
        assert prep.object_sha256(document) == original_sha == entry["manifest_sha256"]
        parts = [set(flatten_ids(document, component)) for component in ("history_ab", "washout", "suffix")]
        assert all(parts[i].isdisjoint(parts[j]) for i in range(3) for j in range(i))
        ids = set.union(*parts)
        assert len(ids) == 10 and all(prep.split_role(base_id) == "pilot" for base_id in ids)
        if entry["seed"] in by_seed:
            assert ids == by_seed[entry["seed"]]
        by_seed[entry["seed"]] = ids
        assert document["history_ab"] == list(reversed(document["history_ba"]))
        assert all(Path(s["path"]).is_absolute() and s["label"] in (0, 1)
                   for batch in document["suffix"] for s in batch)
    seeds = list(by_seed)
    assert all(by_seed[seeds[i]].isdisjoint(by_seed[seeds[j]]) for i in range(3) for j in range(i))
    before = (tmp_path / "panels" / "index.json").read_bytes()
    build_tiny(tmp_path, root, mapping, source)
    assert (tmp_path / "panels" / "index.json").read_bytes() == before
    with pytest.raises(FileExistsError, match="Immutable"):
        build_tiny(tmp_path, root, mapping, source, seeds=(202, 101, 303))
    assert (tmp_path / "panels" / "index.json").read_bytes() == before


def test_missing_variant_image_fails_instead_of_intersecting(tmp_path):
    root, mapping, source = fake_data(tmp_path)
    next((root / "brightness" / "5").rglob("*.JPEG")).unlink()
    with pytest.raises(ValueError, match="exactly the same original"):
        build_tiny(tmp_path, root, mapping, source)


def test_wrong_class_order_is_rejected(tmp_path):
    root, mapping, source = fake_data(tmp_path)
    mapping.write_text(json.dumps({"0": ["n00000002", "second"], "1": ["n00000001", "first"]}))
    with pytest.raises(ValueError, match="lexicographically"):
        build_tiny(tmp_path, root, mapping, source)


def test_insufficient_pilot_never_draws_reserve(tmp_path):
    root, mapping, source = fake_data(tmp_path, count=40)
    with pytest.raises(ValueError, match="No fallback to reserve"):
        build_tiny(tmp_path, root, mapping, source)
    assert not (tmp_path / "panels").exists()


def test_relative_paths_and_labels_do_not_determine_id_selection(tmp_path):
    root, mapping, source = fake_data(tmp_path)
    index = build_tiny(tmp_path, root, mapping, source, relative_paths=True)
    first = json.loads((tmp_path / "panels" / index["panels"][0]["path"]).read_text())
    expected = sorted([f"ILSVRC2012_val_{i:08d}.JPEG" for i in range(1, 201)
                       if prep.split_role(f"ILSVRC2012_val_{i:08d}.JPEG") == "pilot"],
                      key=lambda name: (prep.split_hash(name), name))[:10]
    observed = [s["base_id"] for component in ("history_ab", "washout", "suffix")
                for batch in first[component] for s in batch]
    assert set(expected) == set(observed)
    assert first["metadata"]["sampler_uses_labels"] is False
    assert first["metadata"]["path_root"] == str(root.resolve())
    assert not Path(first["suffix"][0][0]["path"]).is_absolute()


def test_duplicate_basename_across_classes_rejected(tmp_path):
    root, mapping, source = fake_data(tmp_path)
    path = root / image_path(domain="brightness", index=1, synset="n00000001")
    path.write_bytes(b"duplicate")
    with pytest.raises(ValueError, match="Duplicate base ID"):
        build_tiny(tmp_path, root, mapping, source)


def test_corrupt_provenance_and_unknown_archive_rejected(tmp_path):
    root, mapping, source = fake_data(tmp_path)
    with pytest.raises(ValueError, match="No verified extraction provenance"):
        build_tiny(tmp_path, root, mapping, None)
    folder = root / "_provenance"
    folder.mkdir()
    (folder / "extract_bad.json").write_text(json.dumps({"record_sha256": "0" * 64, "archives": []}))
    with pytest.raises(ValueError, match="provenance checksum"):
        prep._source_records(root)


def test_nested_destination_symlink_rejected(tmp_path):
    archive = tmp_path / "tiny.tar"
    checksums = make_archive(archive, [(image_path(), b"payload")])
    root, outside = tmp_path / "out", tmp_path / "outside"
    root.mkdir()
    outside.mkdir()
    try:
        (root / "gaussian_noise").symlink_to(outside, target_is_directory=True)
    except OSError:
        pytest.skip("Windows symlink privilege unavailable; traversal cases remain tested")
    with pytest.raises(ValueError, match="escapes|symlink"):
        prep.extract_archives([archive], root, ["gaussian_noise"], execute=True,
                              reserve_bytes=0, expected_checksums=checksums)
    assert not list(outside.iterdir())


def test_selective_archive_to_manifest_integration(tmp_path):
    root, mapping, _ = fake_data(tmp_path)
    members = [(path.relative_to(root).as_posix(), path.read_bytes()) for path in root.rglob("*.JPEG")]
    archive = tmp_path / "fixture.tar"
    checksums = make_archive(archive, members)
    extracted = tmp_path / "extracted"
    prep.extract_archives([archive], extracted, ["gaussian_noise", "brightness", "defocus_blur"],
                          partition="pilot", execute=True, reserve_bytes=0,
                          expected_checksums=checksums)
    index = build_tiny(tmp_path, extracted, mapping, None)
    assert len(index["panels"]) == 9
    assert index["metadata"]["available_reserve_ids"] == 0
    assert index["metadata"]["source_records"][0]["archives"][0]["sha256"] == checksums[archive.name]["sha256"]
    assert not any(prep.split_role(path.name) == "reserve_confirmation" for path in extracted.rglob("*.JPEG"))


def test_mapping_download_refuses_changed_payload(tmp_path, monkeypatch):
    monkeypatch.setattr(prep.urllib.request, "urlopen", lambda *args, **kwargs: io.BytesIO(b"unexpected mapping"))
    with pytest.raises(ValueError, match="class-index changed"):
        prep.download_class_index(tmp_path / "mapping.json")
    assert not (tmp_path / "mapping.json").exists()
