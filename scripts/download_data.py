"""Download small training-only sanity data or explicit cloud ImageNet-C archives.

No service provisioning or payment APIs exist in this script. Large data defaults to
plan-only; --execute is required and free disk is checked before transfer.
"""
from __future__ import annotations

import argparse
import hashlib
import io
import shutil
import urllib.request
import zipfile
from pathlib import Path

import _bootstrap
from historytta.utils import file_sha256, write_json

UCI_URL = "https://archive.ics.uci.edu/static/public/80/optical+recognition+of+handwritten+digits.zip"
UCI_ZIP_SHA = "0d7b054fea010270e9b3f06411c654c5e59547732ad626381980baffe0a23fb0"
UCI_TRAIN_SHA = "e1b683cc211604fe8fd8c4417e6a69f31380e0c61d4af22e93cc21e9257ffedd"
ARCHIVES = {
    "noise": (22565673785, "e80562d7f6c3f8834afb1ecf27252745"),
    "blur": (7112704951, "2d8e81fdd8e07fef67b9334fa635e45c"),
    "weather": (12797438995, "33ffea4db4d93fe4a428c40a6ce0c25d"),
    "digital": (7757510705, "89157860d7b10d5797849337ca2e5c03"),
    "extra": (15789490144, "d492dfba5fc162d8ec2c3cd8ee672984"),
}


def download_uci(destination: Path) -> Path:
    destination.mkdir(parents=True, exist_ok=True)
    target = destination / "optdigits.tra"
    if target.exists():
        if file_sha256(target) != UCI_TRAIN_SHA:
            raise ValueError("Existing UCI training file checksum mismatch")
        return target
    with urllib.request.urlopen(UCI_URL, timeout=60) as response:
        payload = response.read()
    if hashlib.sha256(payload).hexdigest() != UCI_ZIP_SHA:
        raise ValueError("UCI archive checksum mismatch; investigate source version")
    # Explicit allowlist: never extract or read official test annotations.
    with zipfile.ZipFile(io.BytesIO(payload)) as archive:
        train = archive.read("optdigits.tra")
    if hashlib.sha256(train).hexdigest() != UCI_TRAIN_SHA:
        raise ValueError("UCI training checksum mismatch")
    target.write_bytes(train)
    write_json(destination / "provenance.json", {
        "url": UCI_URL, "archive_sha256": UCI_ZIP_SHA, "member": "optdigits.tra",
        "file_sha256": UCI_TRAIN_SHA, "license": "CC BY 4.0",
        "official_test_extracted": False,
    })
    return target


def download_imagenetc(destination: Path, groups: list[str], execute: bool) -> None:
    total = sum(ARCHIVES[g][0] for g in groups)
    print({"archives": groups, "archive_GB": round(total / 1e9, 2),
           "recommended_disk_GB": 120, "execute": execute})
    if not execute:
        return
    destination.mkdir(parents=True, exist_ok=True)
    if shutil.disk_usage(destination).free < total + 20 * 10**9:
        raise OSError("Insufficient free disk for selected archives plus workspace reserve")
    for group in groups:
        size, digest = ARCHIVES[group]
        target = destination / f"{group}.tar"
        if not target.exists():
            temp = target.with_suffix(".tar.part")
            with urllib.request.urlopen(f"https://zenodo.org/api/records/2235448/files/{group}.tar/content", timeout=180) as r, temp.open("wb") as f:
                shutil.copyfileobj(r, f, length=1024 * 1024)
            temp.replace(target)
        md5 = hashlib.md5()
        with target.open("rb") as f:
            for chunk in iter(lambda: f.read(1024 * 1024), b""):
                md5.update(chunk)
        if target.stat().st_size != size or md5.hexdigest() != digest:
            raise ValueError(f"Checksum/size mismatch: {target}. File retained for investigation.")
        print(f"Verified {target}")


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("dataset", choices=["uci-train", "imagenet-c"])
    p.add_argument("--destination", type=Path)
    p.add_argument("--groups", nargs="+", choices=list(ARCHIVES), default=["noise", "blur", "weather"])
    p.add_argument("--execute", action="store_true", help="Explicitly download large cloud archives")
    args = p.parse_args()
    if args.dataset == "uci-train":
        print(download_uci(args.destination or Path("datasets/raw/uci")))
    else:
        download_imagenetc(args.destination or Path("datasets/raw/archives"), args.groups, args.execute)


if __name__ == "__main__":
    main()

