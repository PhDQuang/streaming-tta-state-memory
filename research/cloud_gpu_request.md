# Stage B GPU approval request

Prepared 2026-09-08. **Approval pending. No paid action has occurred.** The user's request, sections 0, 13, 30 and 32, requires explicit approval before incurring cost.

| Field | Concrete request |
|---|---|
| Experiment | `stage_b_imagenetc_pilot_v1`, `configs/cloud_pilot.yaml` |
| Scientific purpose | Determine whether matched-history effects survive an identical recent tail on realistic pretrained vision; validate complete-state interventions, throughput, memory and panel variance before a larger study |
| GPU / VRAM | One RTX 4090-class GPU / 24 GB |
| Estimated GPU-hours | 8–16 experiment hours; this estimate has not been GPU-profiled |
| Compute estimate | $5.92–$11.84 at an observed $0.74/hour |
| Requested ceiling | **$20 total**, including preparation/idle time, storage, tax/fees and contingency; reduce run time if the actual quote requires it |
| Storage | 120 GB temporary cloud disk, no large local dataset |
| Expected duration | Within one day including archive transfer, setup and artifact export, subject to host/network availability |
| Continue criterion | All controls pass; measurable persistent effects or enough stable pilot variance to justify a precise confirmatory bound; a distinct contribution survives comparison with known order/reset methods |
| Modify/abandon criterion | Apparent effects disappear under correct replay/reset controls; effects are negligible at feasible precision; frequent automatic recovery prevents the intended state contrast; required panel precision exceeds a justified budget; or recent baselines/prior work subsume the contribution |

## Frozen experiment

Source: torchvision ResNet-50 IMAGENET1K_V1 with its own deterministic transform. Released ImageNet-C JPEGs, severity 5, gaussian_noise, brightness, defocus_blur. Source, current-batch normalization, Tent and explicitly corrected `sar_complete`. Batch 32; SGD lr0.00025, momentum 0.9; SAR rho 0.05, entropy margin 0.4 log(1000), recovery threshold 0.2. Hyperparameters are fixed without pilot target-label tuning.

Three identity-disjoint panels each contain 1,024 prefix +512 maximum tail +1,024 suffix images: 7,680 original IDs. Three domain-pair scenarios reuse each panel and are averaged within panel. AB/BA share exactly the same preformed batches in different block order; W is0/4/16 batches; Q is identical and previously unseen. Reset P/O/A factorial and all-state controls at the W/Q junction.

The matrix contains **594 paired, 1,188 directional suffix runs and 1,216,512 main suffix-image forward evaluations**. Those counts exclude prefixes, tails, parity/replay controls, backward passes and SAR's second forward. Full junctions are saved only for adaptive methods: 9 panel/scenario units ×2 methods ×3 tails ×2 orders =108 files, approximately 22 GB for two ResNet-50 weight states each, plus small normalization optimizer state. Raw 1,000-class Q logits have an uncompressed lower-level array volume of approximately 4.87 GB. Three archive groups total 42.48 GB; selected JPEGs, environment, output, weights and headroom fit the planned 120 GB subject to verification before launch. These are estimates, not measured cloud sizes.

H1 is fixed to SAR complete / ResNet-50 / no reset / W16, equal scenario average, >1 percentage point mean Q disagreement. A full-stage positive result needs a 95% independent-panel lower bound above 1 point plus architecture/dataset replication. An upper bound below 1 point can support a bounded practical null; a wide interval is inconclusive. Three pilot panels alone cannot establish either claim. H2 primary optimizer contrast is P+A versus P+O+A; the secondary auxiliary contrast is none versus A. The proposal fixes thresholds and multiplicity requirements.

## Cost arithmetic and control

The official [Runpod GPU pricing page](https://www.runpod.io/pricing) listed RTX 4090 at $0.74/hour when checked 2026-09-08. This is a planning reference, not a reservation or guaranteed available quote. Official [Pod storage documentation](https://docs.runpod.io/pods/pricing) lists container/running-volume disk at $0.10/GB/month and stopped volume disk at $0.20/GB/month. At120 GB for 24 hours, running storage is approximately $0.40 under a 30-day convention. 16 GPU hours plus one day of that disk is approximately **$12.24**, before setup/idle time and any applicable tax/fees. A full24-hour rental at the reference rate plus that disk is approximately **$18.16**, leaving little room for fees. Quote and budget accounting determine the actual earlier stop time. Do not assume any free credit or deposit refund.

Before launch, confirm the displayed host/driver/disk quote and a provider termination procedure that keeps accrued total cost within $20. Allow for download/setup/export in the paid clock. The shell wrapper uses a 16-hour experiment timeout; Python additionally checks the cap between method units, which can overshoot internally. Neither process exit nor a stopped workload terminates the rented Pod or persistent-disk billing. Provider termination and artifact preservation remain required operational steps. No automatic provider shutdown has been tested or represented as implemented.

If the quote cannot fit the approved ceiling, do not silently buy a larger GPU, extend hours or expand the matrix. Stop at a documented partial run, retain raw failures, analyze completed prespecified units descriptively, and request a revised budget only with measured throughput/variance.

## Deliverables from the approved pilot

Immutable data/index/config hashes; pretrained source and complete junction checkpoints; all per-image predictions and scalar tables; negative controls; event/failure traces; wall time, peak GPU memory and actual billed cost; panel variance and practical effect bounds; a written proceed/modify/stop decision. Full confirmation is a separate future budget, not included in this request.
