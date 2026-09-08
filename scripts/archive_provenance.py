"""Archive exact still-available producer sources without rewriting run provenance."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import zipfile

import _bootstrap
from historytta.utils import file_sha256, write_json


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--results", type=Path, required=True)
    args = p.parse_args()
    recorded = json.loads((args.results / "provenance.json").read_text(encoding="utf-8"))
    source = recorded["source_hashes"]
    matched = [name for name, digest in source.items() if Path(name).is_file() and file_sha256(name) == digest]
    changed = sorted(set(source) - set(matched))
    # All imported implementation modules and the Stage A entrypoint must survive.
    required = [name for name in source if name.startswith("src/")]
    required += ["scripts/run_sanity.py", "scripts/_bootstrap.py"]
    unavailable = sorted(set(required) - set(matched))
    if unavailable:
        raise ValueError(f"Cannot archive exact experiment-producing sources: {unavailable}")
    destination = args.results / "producer_source.zip"
    if destination.exists():
        raise FileExistsError("Existing producer archive retained")
    with zipfile.ZipFile(destination, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for name in sorted(matched):
            archive.write(name, name)
        archive.write(args.results / "provenance.json", "run_provenance.json")
    write_json(args.results / "producer_archive.json", {
        "archive": destination.name, "sha256": file_sha256(destination),
        "exact_recorded_sources_archived": sorted(matched),
        "changed_or_unavailable_nonproducer_sources": changed,
        "all_required_runtime_sources_archived": True,
        "note": "Historical git_commit remains null. This archive preserves matching producer bytes; later analysis has separate provenance. Config object is embedded in run_provenance.json."})
    print(json.dumps({"archive": str(destination), "matched": len(matched), "nonproducer_drift": changed}, indent=2))


if __name__ == "__main__":
    main()
