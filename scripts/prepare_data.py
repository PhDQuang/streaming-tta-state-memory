"""Selectively extract ImageNet-C archives and freeze label-blind pilot panels.

Run --help or see research/data_preparation.md. No cloud provisioning occurs.
Archive extraction is opt-in via --execute; manifest creation reads local files.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import tarfile
import urllib.request
import uuid
from pathlib import Path, PurePosixPath

import _bootstrap
from download_data import ARCHIVES
from historytta.streams import Sample, make_panel
from historytta.utils import file_sha256, object_sha256


CLASS_INDEX_URL = "https://storage.googleapis.com/download.tensorflow.org/data/imagenet_class_index.json"
CLASS_INDEX_SHA256 = "a1e7a966a1f601d39e4b43e119b3e7dd4a2ad3ea08cf69847cbaf021013767bc"
DATASET_URL = "https://zenodo.org/records/2235448"
SPLIT_SALT = "20260908/"
DEFAULT_SEEDS = (101, 202, 303)
SCENARIOS = (
    ("gaussian_noise", "brightness", "defocus_blur"),
    ("defocus_blur", "gaussian_noise", "brightness"),
    ("brightness", "defocus_blur", "gaussian_noise"),
)
SYNSET = re.compile(r"n[0-9]{8}\Z")
IMAGE_NAME = re.compile(r"ILSVRC2012_val_[0-9]{8}\.(?:JPEG|jpg|jpeg)\Z")


def split_hash(base_id: str) -> str:
    return hashlib.sha256((SPLIT_SALT + base_id).encode("utf-8")).hexdigest()


def split_role(base_id: str) -> str:
    return "pilot" if int(split_hash(base_id), 16) % 100 < 20 else "reserve_confirmation"


def _json_bytes(value: dict) -> bytes:
    return (json.dumps(value, sort_keys=True, indent=2, allow_nan=False) + "\n").encode("utf-8")


def write_immutable(path: Path, payload: bytes) -> None:
    """Idempotent exact-content write; never replace a different existing artifact."""
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        if path.is_symlink() or path.read_bytes() != payload:
            raise FileExistsError(f"Immutable artifact differs: {path}; use a new output directory")
        return
    temp = path.parent / ("." + path.name + "." + uuid.uuid4().hex + ".part")
    try:
        with temp.open("xb") as stream:
            stream.write(payload)
            stream.flush()
            os.fsync(stream.fileno())
        # Atomic no-clobber publication on local Windows/Unix filesystems.
        os.link(temp, path)
    finally:
        temp.unlink(missing_ok=True)


def download_class_index(path: Path) -> Path:
    """Download only the pinned 35 KB public model-label mapping."""
    if path.exists():
        if file_sha256(path) != CLASS_INDEX_SHA256:
            raise ValueError("Existing canonical class-index checksum mismatch")
        return path
    with urllib.request.urlopen(CLASS_INDEX_URL, timeout=60) as response:
        payload = response.read(1024 * 1024 + 1)
    if hashlib.sha256(payload).hexdigest() != CLASS_INDEX_SHA256:
        raise ValueError("Canonical class-index changed; inspect version before using it")
    write_immutable(path, payload)
    return path


def load_class_index(path: Path, expected_classes: int = 1000) -> tuple[dict, list[str]]:
    if expected_classes <= 0:
        raise ValueError("Expected class count must be positive")
    if expected_classes == 1000 and file_sha256(path) != CLASS_INDEX_SHA256:
        raise ValueError("Production class mapping must match the pinned canonical mapping")
    data = json.loads(path.read_text(encoding="utf-8"))
    if set(data) != {str(i) for i in range(expected_classes)}:
        raise ValueError("Class-index keys must be contiguous zero-based model indices")
    rows = [data[str(i)] for i in range(expected_classes)]
    if any(not isinstance(row, list) or len(row) != 2 or
           not isinstance(row[0], str) or not SYNSET.fullmatch(row[0]) or
           not isinstance(row[1], str) or not row[1] for row in rows):
        raise ValueError("Class-index rows must contain [synset, model class name]")
    synsets = [row[0] for row in rows]
    if len(set(synsets)) != expected_classes or synsets != sorted(synsets):
        raise ValueError("Model class order must equal lexicographically sorted unique synsets")
    return {synset: i for i, synset in enumerate(synsets)}, [row[1] for row in rows]


def _safe_parts(member: tarfile.TarInfo) -> tuple[str, ...]:
    raw = member.name
    if not raw or "\\" in raw or ":" in raw or "\x00" in raw or raw.startswith("/"):
        raise ValueError(f"Unsafe archive member path: {raw!r}")
    if ".." in raw.split("/"):
        raise ValueError(f"Archive traversal rejected: {raw!r}")
    if not (member.isdir() or member.isreg()) or member.issparse():
        raise ValueError(f"Archive link/device/special/sparse member rejected: {raw!r}")
    parts = tuple(part for part in PurePosixPath(raw).parts if part != ".")
    if any(part.endswith((" ", ".")) or part.upper().split(".")[0] in
           {"CON", "PRN", "AUX", "NUL", *[f"COM{i}" for i in range(1, 10)],
            *[f"LPT{i}" for i in range(1, 10)]} for part in parts):
        raise ValueError(f"Nonportable archive member rejected: {raw!r}")
    return parts


def _selection(parts: tuple, corruptions: set, severities: set):
    if len(parts) != 4 or parts[0] not in corruptions or parts[1] not in severities:
        return None
    domain, severity, synset, name = parts
    if not SYNSET.fullmatch(synset) or not IMAGE_NAME.fullmatch(name):
        raise ValueError(f"Unexpected selected image layout: {'/'.join(parts)}")
    return domain, severity, synset, name


def _checked_destination(root: Path, parts: tuple) -> Path:
    target = root.joinpath(*parts)
    try:
        target.resolve().relative_to(root.resolve())
    except ValueError as exc:
        raise ValueError(f"Destination escapes extraction root: {target}") from exc
    current = target
    while current != root.parent:
        if current.exists() or current.is_symlink():
            info = current.lstat()
            if current.is_symlink() or getattr(info, "st_file_attributes", 0) & 0x400:
                raise ValueError(f"Destination symlink/junction rejected: {current}")
        if current == root:
            break
        current = current.parent
    return target


def _existing_disk_parent(path: Path) -> Path:
    while not path.exists():
        path = path.parent
    return path


def archive_checksum(path: Path, expected_checksums: dict | None = None) -> dict:
    sha, md5 = hashlib.sha256(), hashlib.md5()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            sha.update(chunk)
            md5.update(chunk)
    result = {"filename": path.name, "path": str(path.resolve()), "size_bytes": path.stat().st_size,
              "sha256": sha.hexdigest(), "md5": md5.hexdigest()}
    if expected_checksums is None:
        if path.name != f"{path.stem}.tar" or path.stem not in ARCHIVES:
            raise ValueError(f"Unknown archive {path.name}; provide --archive-checksums for a local fixture")
        expected_size, expected_md5 = ARCHIVES[path.stem]
        expected = {"size_bytes": expected_size, "md5": expected_md5}
        result["source_url"] = f"https://zenodo.org/api/records/2235448/files/{path.name}/content"
    else:
        expected = expected_checksums.get(path.name, {})
        if not expected.get("sha256"):
            raise ValueError(f"Explicit SHA256 required for custom archive: {path.name}")
        result["source_url"] = "local-checksummed-archive"
    for key, value in expected.items():
        if key not in ("sha256", "md5", "size_bytes"):
            raise ValueError(f"Unknown checksum field: {key}")
        if result[key] != value:
            raise ValueError(f"Archive {key} mismatch: {path}")
    return result


def extract_archives(archives: list[Path], destination: Path, corruptions: list[str],
                     severities=(5,), partition="all", execute=False,
                     reserve_bytes=5 * 10**9, expected_checksums=None) -> dict:
    """Two-pass tar inspection/extraction; selected payloads alone reach disk.

    Every header is validated, including unselected members. Existing JPEGs are
    accepted only if content-identical; archive metadata never changes permissions.
    """
    if partition not in {"all", "pilot", "reserve_confirmation"}:
        raise ValueError("Invalid image-ID partition")
    if not archives or not corruptions or any(not re.fullmatch(r"[a-z_]+", c) for c in corruptions):
        raise ValueError("Provide archive(s) and valid corruption names")
    if not severities or any(s not in range(1, 6) for s in severities) or reserve_bytes < 0:
        raise ValueError("Severities must be 1..5 and disk reserve nonnegative")
    root = destination.absolute()
    _checked_destination(root, ())
    selected, all_dirs, seen = {}, set(), set()
    requested = {(c, str(s)) for c in corruptions for s in severities}
    found_variants = set()
    sources = []
    for archive in archives:
        sources.append(archive_checksum(archive, expected_checksums))
        with tarfile.open(archive, mode="r|*") as tar:
            for member in tar:
                parts = _safe_parts(member)
                if member.isdir():
                    continue
                item = _selection(parts, set(corruptions), {str(s) for s in severities})
                if item is None:
                    continue
                domain, severity, synset, base_id = item
                if parts in seen:
                    raise ValueError(f"Duplicate selected archive member: {parts}")
                seen.add(parts)
                found_variants.add((domain, severity))
                all_dirs.add(parts[:3])
                if partition != "all" and split_role(base_id) != partition:
                    continue
                if member.size <= 0:
                    raise ValueError(f"Empty image payload: {member.name}")
                _checked_destination(root, parts)
                selected[parts] = member.size
    if requested != found_variants:
        raise ValueError(f"Requested variants absent from archives: {sorted(requested - found_variants)}")
    if not selected:
        raise ValueError("Selected image partition is empty")
    required = sum(size for parts, size in selected.items() if not root.joinpath(*parts).exists())
    free = shutil.disk_usage(_existing_disk_parent(root)).free
    plan = {"schema_version": 1, "dataset": "ImageNet-C", "source": DATASET_URL,
            "archives": sources, "corruptions": sorted(set(corruptions)),
            "severities": sorted(set(severities)), "partition": partition,
            "split_salt": SPLIT_SALT, "selected_files": len(selected),
            "selected_bytes": sum(selected.values()), "additional_bytes": required,
            "reserve_bytes": reserve_bytes, "destination": str(root.resolve())}
    if free < required + reserve_bytes:
        raise OSError(f"Insufficient free disk: need {required + reserve_bytes}, have {free}")
    if not execute:
        return {**plan, "executed": False}
    root.mkdir(parents=True, exist_ok=True)
    for parts in sorted(all_dirs):
        _checked_destination(root, parts).mkdir(parents=True, exist_ok=True)
    for archive in archives:
        with tarfile.open(archive, mode="r|*") as tar:
            for member in tar:
                parts = _safe_parts(member)
                if parts not in selected or not member.isreg():
                    continue
                target = _checked_destination(root, parts)
                source = tar.extractfile(member)
                if source is None:
                    raise ValueError(f"Unreadable tar payload: {member.name}")
                digest = hashlib.sha256()
                temp = target.parent / ("." + target.name + "." + uuid.uuid4().hex + ".part")
                try:
                    existing = target.exists()
                    with source, (temp.open("xb") if not existing else open(os.devnull, "wb")) as stream:
                        copied = 0
                        for chunk in iter(lambda: source.read(1024 * 1024), b""):
                            copied += len(chunk)
                            digest.update(chunk)
                            stream.write(chunk)
                    if copied != selected[parts]:
                        raise ValueError(f"Truncated archive member: {member.name}")
                    if existing:
                        if not target.is_file() or file_sha256(target) != digest.hexdigest():
                            raise FileExistsError(f"Refusing to replace nonidentical image: {target}")
                    else:
                        _checked_destination(root, parts)
                        os.link(temp, target)
                finally:
                    temp.unlink(missing_ok=True)
    # The record only appears after every selected payload completed successfully.
    record = {k: v for k, v in plan.items() if k not in {"additional_bytes", "reserve_bytes"}}
    record["record_sha256"] = object_sha256(record)
    record_path = root / "_provenance" / f"extract_{record['record_sha256']}.json"
    write_immutable(record_path, _json_bytes(record))
    return {**plan, "executed": True, "provenance": str(record_path)}


def _source_records(root: Path) -> list[dict]:
    records = []
    for path in sorted((root / "_provenance").glob("extract_*.json")):
        record = json.loads(path.read_text(encoding="utf-8"))
        digest = record.pop("record_sha256", None)
        if not digest or object_sha256(record) != digest:
            raise ValueError(f"Extraction provenance checksum mismatch: {path}")
        records.append({**record, "record_sha256": digest})
    if not records:
        raise ValueError("No verified extraction provenance; run extract first")
    return records


def build_manifests(data_root: Path, output: Path, class_index: Path, severities=(5,),
                    seeds=DEFAULT_SEEDS, prefix_size=1024, washout_size=512,
                    suffix_size=1024, batch_size=32, expected_classes=1000,
                    relative_paths=False, source_records=None, allow_attached_source=False,
                    dataset_profile="imagenet_c") -> dict:
    """Freeze three disjoint pilot panels; scenario/severity variants are paired.

    Basenames alone determine partition/rank/component selection. Synsets are
    translated into evaluator labels only when constructing immutable Samples.
    """
    if len(set(seeds)) != len(seeds) or not seeds or not severities or any(s not in range(1, 6) for s in severities):
        raise ValueError("Seeds must be distinct and severities must be 1..5")
    if batch_size <= 0 or prefix_size <= 0 or suffix_size <= 0 or washout_size < 0:
        raise ValueError("Invalid panel sizes")
    if prefix_size % (2 * batch_size) or washout_size % batch_size or suffix_size % batch_size:
        raise ValueError("Panel sizes must form equal whole batches and two equal prefix blocks")
    if dataset_profile not in {"imagenet_c", "tiny_imagenet_c"}:
        raise ValueError("Unknown dataset profile")
    tiny = dataset_profile == "tiny_imagenet_c"
    root = data_root.resolve(strict=True)
    projection = None
    if tiny:
        if expected_classes != 200:
            raise ValueError("Tiny ImageNet-C requires 200 declared classes")
        source_mapping, source_names = load_class_index(class_index, 1000)
        first_variant = root / "brightness" / str(sorted(set(severities))[0])
        if not first_variant.is_dir():
            raise ValueError(f"Missing Tiny variant: {first_variant}")
        synsets = sorted(p.name for p in first_variant.iterdir() if p.is_dir())
        if len(synsets) != 200 or not set(synsets).issubset(source_mapping):
            raise ValueError("Tiny dataset must have exactly 200 synsets present in the canonical ImageNet mapping")
        mapping = {synset: i for i, synset in enumerate(synsets)}
        projection = [source_mapping[synset] for synset in synsets]
        names = [source_names[i] for i in projection]
    else:
        mapping, names = load_class_index(class_index, expected_classes)
    image_name = re.compile(r"test_[0-9]+\.(?:JPEG|jpg|jpeg)\Z") if tiny else IMAGE_NAME
    provenance = _source_records(root) if source_records is None else source_records
    def acceptable_source(record):
        if record.get("archives"):
            return True
        attached = record.get("attached_dataset", {})
        return (allow_attached_source and attached.get("source_url", "").startswith(("https://", "http://"))
                and attached.get("verification") == "selected_image_hashes_only_not_official_archive_verified")

    if not provenance or not all(acceptable_source(record) for record in provenance):
        raise ValueError("Source archive checksums are required; attached datasets need explicit exploratory opt-in and source URL")
    variants = [(domain, severity) for domain in sorted({c for scenario in SCENARIOS for c in scenario})
                for severity in sorted(set(severities))]
    inventories = {}
    reference_ids, reference_synsets = None, None
    for domain, severity in variants:
        variant = root / domain / str(severity)
        if not variant.is_dir() or variant.is_symlink():
            raise ValueError(f"Missing/unsafe variant directory: {variant}")
        dirs = {p.name for p in variant.iterdir() if p.is_dir()}
        if dirs != set(mapping):
            raise ValueError(f"Variant class directories do not match canonical mapping: {variant}")
        inventory = {}
        for synset in sorted(dirs):
            folder = _checked_destination(root, (domain, str(severity), synset))
            for path in sorted(folder.iterdir()):
                if not path.is_file() or not image_name.fullmatch(path.name):
                    raise ValueError(f"Unexpected image entry: {path}")
                _checked_destination(root, (domain, str(severity), synset, path.name))
                if path.name in inventory:
                    raise ValueError(f"Duplicate base ID across class folders: {path.name}")
                inventory[path.name] = (synset, path)
        ids = set(inventory)
        synsets = {base_id: row[0] for base_id, row in inventory.items()}
        if reference_ids is not None and (ids != reference_ids or synsets != reference_synsets):
            raise ValueError("Variants must share exactly the same original IDs and synset assignment")
        reference_ids, reference_synsets = ids, synsets
        inventories[(domain, severity)] = inventory
    # No labels influence these decisions: only the global original basename.
    ordered_ids = sorted(reference_ids, key=lambda base_id: (split_hash(base_id), base_id))
    pilot_ids = [base_id for base_id in ordered_ids if split_role(base_id) == "pilot"]
    reserve_ids = [base_id for base_id in ordered_ids if split_role(base_id) != "pilot"]
    panel_size = prefix_size + washout_size + suffix_size
    required = len(seeds) * panel_size
    if len(pilot_ids) < required:
        raise ValueError(f"Need {required} disjoint pilot IDs; only {len(pilot_ids)} available. No fallback to reserve.")
    metadata = {
        "dataset": "Tiny ImageNet-C" if tiny else "ImageNet-C",
        "source": "https://zenodo.org/records/2536630" if tiny else DATASET_URL,
        "source_records": provenance,
        "source_records_sha256": object_sha256(provenance),
        "path_mode": "relative" if relative_paths else "absolute", "path_root": str(root),
        "class_to_idx": mapping, "model_class_names": names,
        "class_index_sha256": file_sha256(class_index),
        "class_index_source": CLASS_INDEX_URL if tiny or expected_classes == 1000 else "test-fixture",
        "partition_rule": "int(sha256('20260908/' + base_id),16) % 100 < 20",
        "rank_rule": "ascending sha256('20260908/' + base_id), then base_id",
        "split_role": "pilot_development", "available_pilot_ids": len(pilot_ids),
        "available_reserve_ids": len(reserve_ids), "reserve_ids_sha256": object_sha256(reserve_ids),
        "reserve_annotations_loaded": False, "sampler_uses_labels": False,
        "seeds": list(seeds), "prefix_size": prefix_size, "washout_size": washout_size,
        "suffix_size": suffix_size, "batch_size": batch_size,
        "panel_identity_disjoint": True, "scenario_and_severity_variants_share_panel_ids": True,
        "expected_classes": expected_classes,
    }
    if tiny:
        metadata.update(dataset_profile=dataset_profile, input_image_size=[64, 64],
                        classifier="imagenet_200_class_projection", output_imagenet_indices=projection,
                        classifier_sha256=object_sha256({"synsets": sorted(mapping), "indices": projection}),
                        model_training="ImageNet-1K pretrained; no Tiny ImageNet source training",
                        transform="IMAGENET1K_V1 transforms: resize 256, center crop 224, ImageNet normalization")
    payloads, index_entries = [], []
    image_hashes = {}
    for panel_index, seed in enumerate(seeds):
        chosen = pilot_ids[panel_index * panel_size:(panel_index + 1) * panel_size]
        prefix = chosen[:prefix_size]
        washout = chosen[prefix_size:prefix_size + washout_size]
        suffix = chosen[prefix_size + washout_size:]
        for severity in sorted(set(severities)):
            for a, b, q in SCENARIOS:
                def factory(base_id, domain):
                    synset, path = inventories[(domain, severity)][base_id]
                    sample_path = path.relative_to(root).as_posix() if relative_paths else str(path.resolve())
                    return Sample(base_id, domain, severity, sample_path, mapping[synset])
                panel = make_panel(prefix, washout, suffix, (a, b), q, batch_size, seed, factory)
                document = panel.manifest()
                checksums = {}
                for batches in (panel.history_ab, panel.washout, panel.suffix):
                    for batch in batches:
                        for sample in batch:
                            path = root / sample.path if relative_paths else Path(sample.path)
                            if sample.path not in image_hashes:
                                if tiny:
                                    from PIL import Image
                                    with Image.open(path) as image:
                                        if image.size != (64, 64):
                                            raise ValueError(f"Tiny ImageNet-C requires 64x64 selected JPEGs: {path}")
                                image_hashes[sample.path] = file_sha256(path)
                            checksums[sample.path] = image_hashes[sample.path]
                scenario = f"{a}+{b}__to__{q}"
                # Statistical unit excludes repeated scenario/severity conditions.
                panel_id = f"{'tiny_' if tiny else ''}pilot_seed{seed}"
                document["metadata"] = {**metadata, "panel_id": panel_id, "panel_index": panel_index,
                                        "seed": seed, "scenario": scenario, "severity": severity,
                                        "prefix_domains": [a, b], "suffix_domain": q,
                                        "selected_ids_sha256": object_sha256(chosen),
                                        "image_sha256": checksums}
                document["manifest_sha256"] = object_sha256(document)
                filename = f"{panel_id}_s{severity}_{scenario}.json"
                payload = _json_bytes(document)
                payloads.append((output / filename, payload))
                index_entries.append({"panel_id": panel_id, "seed": seed, "scenario": scenario,
                                      "severity": severity, "path": filename,
                                      "panel_sha256": document["sha256"],
                                      "manifest_sha256": document["manifest_sha256"],
                                      "file_sha256": hashlib.sha256(payload).hexdigest()})
    index = {"schema_version": 1, "metadata": metadata, "panels": index_entries}
    index["sha256"] = object_sha256(index)
    payloads.append((output / "index.json", _json_bytes(index)))
    # Detect an incompatible rerun before publishing any new file.
    for path, payload in payloads:
        if path.exists() and (path.is_symlink() or path.read_bytes() != payload):
            raise FileExistsError(f"Immutable artifact differs: {path}; use a new output directory")
    output.mkdir(parents=True, exist_ok=True)
    if shutil.disk_usage(output).free < sum(len(payload) for _, payload in payloads) + 1024 * 1024:
        raise OSError("Insufficient disk space for manifests")
    for path, payload in payloads:
        write_immutable(path, payload)
    return index


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    extract = commands.add_parser("extract", help="Inspect or safely extract selected archive JPEGs")
    extract.add_argument("--archives", type=Path, nargs="+", required=True)
    extract.add_argument("--destination", type=Path, default=Path("datasets/processed/imagenet-c"))
    extract.add_argument("--corruptions", nargs="+", default=["gaussian_noise", "brightness", "defocus_blur"])
    extract.add_argument("--severities", nargs="+", type=int, default=[5])
    extract.add_argument("--partition", choices=["all", "pilot", "reserve_confirmation"], default="all")
    extract.add_argument("--reserve-gb", type=float, default=5.0)
    extract.add_argument("--execute", action="store_true")
    extract.add_argument("--archive-checksums", type=Path, help="Explicit SHA256 JSON for local fixture archives")
    manifest = commands.add_parser("manifest", help="Freeze pilot3 JSON panels and index")
    manifest.add_argument("--data-root", type=Path, default=Path("datasets/processed/imagenet-c"))
    manifest.add_argument("--output", type=Path, default=Path("datasets/processed/imagenet-c-pilot"))
    manifest.add_argument("--class-index", type=Path, default=Path("datasets/metadata/imagenet_class_index.json"))
    manifest.add_argument("--download-class-index", action="store_true", help="Fetch the pinned 35 KB mapping if absent")
    manifest.add_argument("--severities", nargs="+", type=int, default=[5])
    manifest.add_argument("--seeds", nargs="+", type=int, default=list(DEFAULT_SEEDS))
    manifest.add_argument("--prefix-size", type=int, default=1024)
    manifest.add_argument("--washout-size", type=int, default=512)
    manifest.add_argument("--suffix-size", type=int, default=1024)
    manifest.add_argument("--batch-size", type=int, default=32)
    manifest.add_argument("--expected-classes", type=int, default=1000, help="Override only for synthetic tests")
    manifest.add_argument("--relative-paths", action="store_true")
    args = parser.parse_args()
    if args.command == "extract":
        expected = json.loads(args.archive_checksums.read_text()) if args.archive_checksums else None
        result = extract_archives(args.archives, args.destination, args.corruptions, args.severities,
                                  args.partition, args.execute, int(args.reserve_gb * 10**9), expected)
        print(json.dumps(result, indent=2))
    else:
        if args.download_class_index:
            if args.expected_classes != 1000:
                raise ValueError("Canonical mapping download requires 1000 classes")
            download_class_index(args.class_index)
        result = build_manifests(args.data_root, args.output, args.class_index, args.severities,
                                 args.seeds, args.prefix_size, args.washout_size, args.suffix_size,
                                 args.batch_size, args.expected_classes, args.relative_paths)
        print(json.dumps({"index": str((args.output / 'index.json').resolve()),
                          "panels": len(result["panels"]), "sha256": result["sha256"]}, indent=2))


if __name__ == "__main__":
    main()
