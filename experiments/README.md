# Experiment registry

| ID / stage | Status | Configuration / evidence | Interpretation |
|---|---|---|---|
| UPSTREAM_SAM_STATE_CPU_001 | Executed | `third_party/sar_reference/audit_result.json` | Deterministic optimizer-state audit, no image accuracy |
| stage_a_uci_v1 | Executed, preserved | `configs/sanity.yaml`, `results/stage_a_uci_v1` | Training-only local software sanity |
| stage_a_uci_v2 | Executed and independently audited | `configs/sanity_v2.yaml`, `results/stage_a_uci_v2` | Hardened replay, exact scientific parity with v1 |
| stage_a_sar_recovery_comparison | Executed | `scripts/compare_sar_recovery.py`, `results/stage_a_sar_recovery_comparison` | Faithful/corrected SAR on six fixed local trajectories |
| Stage B ImageNet-C pilot | Prepared, approval pending | `configs/cloud_pilot.yaml`, `research/cloud_gpu_request.md` | Engineering/variance pilot, not confirmation |
| Stages C/D | Scientific design only | `research/proposal.md` | Confirmation, stronger baselines, mandatory controls and replication still require implementation/approved compute |

All scientific settings and failed/negative outcomes belong to an immutable experiment ID. Reruns use new IDs and output directories. Do not pool overlapping local seeds, scenarios, branches or v1/v2 repeats into an inflated panel count. Do not mark a partial cloud run complete; the default analysis validates the full planned matrix. Full details and decisions are maintained in `research/research_log.md`.
