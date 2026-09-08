# Third-party reference code

`sar_reference/` contains unmodified reference files from mr-eggplant/SAR at
`20f6e24b17525f34503510afccedc0629b67b7c4`, under its retained BSD-3-Clause LICENSE.
See its manifest for exact URLs and file checksums. These are used for tests and
the explicitly labeled CPU optimizer audit, not imported by production adapters.

SAR acknowledges TENT and credits davda54/sam for its SAM optimizer. Original
license texts from those repositories are also retained with pinned provenance.
`src/historytta/adapters.py` is a local implementation following these algorithms
with the documented changes in `research/baseline_implementation.md`.

`sar_reference/audit_result.json` is locally generated experimental output, not
an upstream file. It is excluded from the upstream source manifest.
