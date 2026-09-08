"""Plan or reproduce the free Stage A workflow. Never launches a cloud stage."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import subprocess
import sys

import yaml
import _bootstrap
from historytta.utils import object_sha256


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, default=Path("configs/sanity_v2.yaml"))
    parser.add_argument("--run", action="store_true")
    parser.add_argument("--reuse-existing", action="store_true")
    args = parser.parse_args()
    cfg = yaml.safe_load(args.config.read_text(encoding="utf-8"))
    if cfg.get("stage") != "A" or cfg.get("device") != "cpu":
        raise ValueError("This entry point only executes the free CPU sanity stage")
    output = Path(cfg["output"])
    commands = [["scripts/download_data.py", "uci-train"],
                ["scripts/run_sanity.py", "--config", str(args.config)],
                ["scripts/evaluate.py", "--results", str(output)],
                ["scripts/generate_tables.py", "--results", str(output), "--stage", "A"],
                ["scripts/generate_figures.py", "--results", str(output), "--stage", "A"],
                ["scripts/build_paper.py", "--results", str(output)]]
    if args.reuse_existing:
        status = json.loads((output / "run_status.json").read_text())
        metadata = json.loads((output / "provenance.json").read_text())
        if status["status"] != "complete" or metadata["config_sha256"] != object_sha256(cfg):
            raise ValueError("Existing run is not a complete matching configuration")
        commands = commands[2:]
    if not args.run:
        print(json.dumps({"mode": "plan_only", "commands": [[sys.executable, *c] for c in commands]}, indent=2))
        return
    for command in commands:
        subprocess.run([sys.executable, *command], check=True)


if __name__ == "__main__":
    main()
