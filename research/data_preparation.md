# ImageNet-C cloud data preparation

Implemented in `scripts/prepare_data.py`; tested with tiny synthetic archives/directories only. No ImageNet-C archive was downloaded or extracted locally. The small canonical model-label JSON was fetched into memory once to verify its checksum on 2026-09-08.

## Source and usage terms

ImageNet-C is distributed in [Dan Hendrycks' Zenodo record 2235448](https://zenodo.org/records/2235448), DOI `10.5281/zenodo.2235448`, associated with Hendrycks and Dietterich's ICLR 2019 corruption benchmark. The record's API metadata returned `access_right: open` and `license.id: cc-by-4.0` on 2026-09-08. This records the derivative dataset's declared license; it does not establish separate ownership or unrestricted redistribution rights for every underlying ImageNet image. Use downloaded data for the authorized research and retain attribution/source provenance.

Archive groups relevant to the pilot, verified against the source and existing download script:

| Group | Corruptions used here | Archive bytes | Published MD5 |
|---|---|---:|---|
| noise.tar | gaussian_noise | 22,565,673,785 | e80562d7f6c3f8834afb1ecf27252745 |
| blur.tar | defocus_blur | 7,112,704,951 | 2d8e81fdd8e07fef67b9334fa635e45c |
| weather.tar | brightness | 12,797,438,995 | 33ffea4db4d93fe4a428c40a6ce0c25d |

Download these on the approved cloud machine with the existing `scripts/download_data.py`. The combined archive footprint is 42.48 GB decimal; extraction needs additional space. Preparation prints exact selected JPEG bytes after scanning the already downloaded archives and enforces a configurable 5 GB free-space reserve by default. Archive scans calculate SHA256 plus the published MD5 and check exact byte counts. `extract` therefore reads large archives even in plan mode; it never transfers them over the network.

## Pinned 1000-class mapping

The [TensorFlow-hosted ImageNet class-index mapping](https://storage.googleapis.com/download.tensorflow.org/data/imagenet_class_index.json) contains 35,363 bytes, with SHA256:

```text
a1e7a966a1f601d39e4b43e119b3e7dd4a2ad3ea08cf69847cbaf021013767bc
```

Verified: exactly indices `0..999`; values `[synset, human-readable name]`; unique synsets in lexicographic order; first `n01440764 / tench`, last `n15075141 / toilet_tissue`. `manifest --download-class-index` fetches only this pinned small mapping if absent and fails if it changes. Existing files are also checked. Production defaults require its exact SHA; `--expected-classes` exists only for synthetic tests.

Each selected corruption/severity directory must contain exactly the canonical 1000 synset directories. The numeric mapping is compatible with standard ImageNet classifiers using that class order; a nonstandard model head must be checked separately by the runner. Human-readable strings can use different synonyms in model libraries, so exact string equality to a library's display labels is not an additional assumed guarantee.

## Commands

Run these from the repository on the cloud machine after the separately approved data download. They do not provision infrastructure or initiate a paid service.

```bash
# Read and verify local tar archives, inspect every header, print exact extraction plan.
python scripts/prepare_data.py extract \
  --archives datasets/raw/archives/noise.tar datasets/raw/archives/blur.tar datasets/raw/archives/weather.tar \
  --destination datasets/processed/imagenet-c \
  --corruptions gaussian_noise brightness defocus_blur \
  --severities 5 --partition pilot

# Repeat with --execute to extract selected payloads.
python scripts/prepare_data.py extract \
  --archives datasets/raw/archives/noise.tar datasets/raw/archives/blur.tar datasets/raw/archives/weather.tar \
  --destination datasets/processed/imagenet-c \
  --corruptions gaussian_noise brightness defocus_blur \
  --severities 5 --partition pilot --execute

# Freeze all three pilot panels and their three paired scenarios.
python scripts/prepare_data.py manifest \
  --data-root datasets/processed/imagenet-c \
  --output datasets/processed/imagenet-c-pilot \
  --download-class-index
```

PowerShell users can place each command on one line or use PowerShell's continuation syntax. `--severities 3 5` extracts both levels; manifest generation needs the same list to include both. Extraction defaults to `--partition all`, which includes all original IDs for the chosen corruption/severity variants; `--partition pilot` is the storage-saving choice for this pilot. Use a distinct extraction root if changing partition, because extra existing JPEGs are never deleted. An extraction under `reserve_confirmation` does not authorize its use for development.

Archive layout is `corruption/severity/synset/ILSVRC2012_val_XXXXXXXX.JPEG`. A leading `./` is accepted; arbitrary extra directory nesting is not guessed. Selected variants must actually exist in the supplied archives. The script copies bytes without image resizing, recompression or augmentation; model-specific transforms belong in the evaluator.

## Label-blind identity split and panel construction

The original basename including its `.JPEG` extension is the canonical `base_id`. It must be globally unique across synset folders and have identical class assignment across every selected variant. Missing IDs are errors; the code never silently intersects variant sets. Different corrupted versions inherit the same original identity.

The fixed split is:

```python
h = sha256(("20260908/" + base_id).encode("utf-8")).hexdigest()
role = "pilot" if int(h, 16) % 100 < 20 else "reserve_confirmation"
```

Order pilot IDs by `(h, base_id)`, take the first 7,680 IDs, then allocate three consecutive, nonoverlapping chunks of 2,560 to seeds 101, 202 and 303. For each chunk: first 1,024 IDs are prefix; next 512 are maximum washout; last 1,024 are suffix. Batch size defaults to 32, matching the proposal and making the maximum washout 16 batches. `make_panel` shuffles only the prefix using its panel seed, forms equal A/B blocks of fixed batches, and swaps block order for AB versus BA. Prefix, washout and suffix have disjoint original IDs, and panels for different seeds have disjoint original IDs. Exhausting the pilot pool is a hard error; reserve IDs are never borrowed. Statistical panel_id is `pilot_seed101` (and analogously 202/303), shared across scenario/severity variants; unique filenames include those conditions. This prevents pseudoreplication in analysis.

For each panel, the same component identity sets are reused across the three scenarios and requested severities to create paired comparisons:

1. gaussian_noise + brightness → defocus_blur
2. defocus_blur + gaussian_noise → brightness
3. brightness + defocus_blur → gaussian_noise

Thus nine files are produced at severity 5. These nine files are not nine statistically independent image panels. Statistical analysis must account for shared panel identities across scenarios/severities. The hash split separates development from reserved confirmation examples, but all derive from standard ImageNet validation identities; this project must not describe the pilot as an untouched benchmark test result after tuning on its outcomes.

The sampler receives only original basenames and hashes. Directory synsets are translated into numeric labels when constructing evaluator metadata; no annotation file is opened, no class balancing/label-driven sampling occurs, and `adapt_batch` must never receive those labels. Reserved-image file contents are not opened or hashed by manifest generation. If all IDs were extracted, directory names are inventoried to validate source identity consistency, and only a count/digest of reserve basenames is recorded; this is not an evaluation of reserve labels or predictions. If only the pilot partition was extracted, the recorded available-reserve count is zero, meaning absent locally, not that the global reserve is empty.

## Manifest interface

The default index path is `datasets/processed/imagenet-c-pilot/index.json`:

```json
{
  "schema_version": 1,
  "metadata": {
    "dataset": "ImageNet-C",
    "path_mode": "absolute",
    "path_root": "/absolute/runtime/data/root",
    "class_to_idx": {"n01440764": 0},
    "model_class_names": ["tench"],
    "split_role": "pilot_development",
    "sampler_uses_labels": false,
    "panel_identity_disjoint": true,
    "scenario_and_severity_variants_share_panel_ids": true
  },
  "panels": [
    {
      "panel_id": "pilot_seed101",
      "seed": 101,
      "scenario": "gaussian_noise+brightness__to__defocus_blur",
      "severity": 5,
      "path": "pilot_seed101_s5_gaussian_noise+brightness__to__defocus_blur.json",
      "panel_sha256": "...",
      "manifest_sha256": "...",
      "file_sha256": "..."
    }
  ],
  "sha256": "..."
}
```

The example abbreviates metadata, arrays and the 1000-class mapping. Index entry paths are relative to the index file's parent directory. Each panel JSON preserves `history_ab`, `history_ba`, `washout`, `suffix`, and `sha256` exactly as `StreamPanel.manifest()` defines them. Additional keys are `metadata` and `manifest_sha256`. Each sample has `base_id`, `domain`, `severity`, `path`, and evaluator-only `label`. Sample paths default to absolute paths resolved at manifest creation. `--relative-paths` makes them relative to explicit `metadata.path_root`; a relocated dataset requires deliberately updating the runtime root or generating a new reviewed manifest location.

Integrity meanings:

- Panel `sha256`: `object_sha256` of only the four batch arrays, compatible with existing `StreamPanel.manifest()`.
- Panel `manifest_sha256`: `object_sha256` of the full document except that field.
- Index entry `file_sha256`: SHA256 of exact panel file bytes, including newline/formatting.
- Index `sha256`: `object_sha256` of the full index except that field.
- `metadata.image_sha256`: actual selected file-byte hashes, keyed by sample path.
- `metadata.source_records`: verified archive MD5/SHA256/byte sizes and immutable extraction records.

The runner should verify index and file hashes before reading samples; verify the panel batch-array digest, path root, class count/order, and selected image hashes before scoring a claim. Manifests are not cryptographic proof against an adversary who can replace both data and hashes; they provide reproducible identity and accidental-change detection. `write_immutable` refuses to replace different artifacts and publishes via atomic no-clobber hard links. Byte-identical reruns succeed. Changing the mapping, split parameters, paths or image bytes requires a new output directory. Local Windows/Unix filesystems supporting hard links are required; object storage should receive the completed artifacts afterward.

## Extraction safety and recovery

All tar members are checked before any selected payload is written, including unselected headers. Absolute paths, parent traversal, Windows drive/alternate-stream syntax, backslashes, reserved device names, symlinks, hard links, sparse files and device/FIFO members are rejected. Existing destination symlinks or Windows reparse points are rejected; resolved paths must remain within the extraction root. The implementation does not call `extractall`, restore archive ownership, or apply archive permissions.

Only allowed JPEG payloads are streamed to disk. Duplicate selected member paths are errors. Existing files are accepted only when their bytes match the archive; differing files are retained unchanged and raise an error. A successful extraction writes a content-addressed JSON record below `_provenance/`; a failed extraction has no success record. If an I/O failure leaves some completed images, rerun verifies and reuses them. No cleanup operation recursively deletes dataset directories.

For synthetic fixtures only, `--archive-checksums` accepts a JSON mapping from archive basename to `{"sha256": "..."}` with optional `md5` and `size_bytes`. This is recorded as a local checksummed source, not misrepresented as the published ImageNet-C archive. Standard production archive names use source-published MD5/size and compute new SHA256 without custom arguments.

## Verification

Run `python -m pytest tests/test_prepare_data.py -q`. The tests cover hostile archive paths, symlink/hardlink/device/FIFO headers, duplicate members, source checksums, disk exhaustion before extraction, idempotent extraction, changed-file refusal, exact class mapping, variant/base-ID consistency, reserve exclusion, cross-panel disjointness, immutable manifests, relative paths and end-to-end tiny archive preparation. A destination-symlink test is skipped on Windows without symlink privilege; explicit archive-link and traversal cases still run.

These are data-engineering tests with synthetic bytes, not evidence that a vision hypothesis works. Real JPEG decode, model preprocessing and published-baseline reproduction remain runner/cloud validation responsibilities.
