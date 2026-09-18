"""Create a small source-only ZIP to upload as a private Kaggle Dataset."""
from pathlib import Path
import argparse
import hashlib
from zipfile import ZIP_DEFLATED, ZipFile

ROOT = Path(__file__).resolve().parents[1]


def create_bundle(output: Path):
    output.parent.mkdir(parents=True, exist_ok=True)
    folders = ["src", "scripts", "configs", "tests", "notebooks", "third_party"]
    paths = [ROOT / name for name in ["README.md", "pyproject.toml", "requirements.txt",
                                     "research/kaggle_preliminary.md", "research/data_preparation.md",
                                     "research/kaggle_tiny_preliminary.md"]]
    for folder in folders:
        paths.extend(p for p in (ROOT / folder).rglob("*")
                     if p.is_file() and "__pycache__" not in p.parts and p.suffix != ".pyc")
    with ZipFile(output, "x", compression=ZIP_DEFLATED) as archive:
        for path in sorted(p for p in paths if p.is_file()):
            archive.write(path, f"streaming-tta-state-memory/{path.relative_to(ROOT).as_posix()}")
    digest = hashlib.sha256(output.read_bytes()).hexdigest()
    output.with_suffix(".zip.sha256").write_text(f"{digest}  {output.name}\n", encoding="utf-8")
    print(f"Source bundle: {output.resolve()} ({output.stat().st_size:,} bytes)\nSHA256: {digest}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "artifacts/kaggle/streaming-tta-kaggle-source.zip")
    create_bundle(parser.parse_args().output)
