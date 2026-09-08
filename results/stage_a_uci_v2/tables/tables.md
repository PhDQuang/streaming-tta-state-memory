# Recorded results: stage_a_uci_v2

Stage A: descriptive correctness/sanity results only. Scenarios are averaged within each seed/panel, then repeated seeds within panel_id; each panel receives equal weight. SD and 95% t intervals describe variation across the supplied panel IDs, conditional on this dataset, model, and stream construction. Tiny local samples and three seeds cannot establish population generalization. Shared-image scenarios, suffix batches, and repeated seeds are not counted as independent panels. No p-values or statistical-superiority claims are generated. Metrics remain in raw units: accuracy/error fractions, NLL in nats/example; absolute gaps are finite-panel magnitudes, not unbiased absolute population effects.

Performance-reference tables pair the exact seed, panel, scenario, W, and direction before aggregation. source_reference compares with source/no reset; norm_reference compares with normalization-only/no reset; performance_reset_effects compares each reset with the same method/no reset. Positive error_change, nll_change, brier_change, or ece15_change means worse recorded performance than that reference; positive accuracy_change means better accuracy. These are distinct from AB/BA history disagreement.

## paired

| method | intervention | washout_batches | metric | n_panels | mean | sd | ci95_low | ci95_high | n_seeds_min | n_seeds_max | individual_panels |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Normalization only | Reset all declared state | 0 | disagreement | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Normalization only | Reset all declared state | 0 | accuracy_ab | 1 | 0.861328 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.861328125} |
| Normalization only | Reset all declared state | 0 | accuracy_ba | 1 | 0.861328 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.861328125} |
| Normalization only | Reset all declared state | 0 | signed_error_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Normalization only | Reset all declared state | 0 | absolute_error_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Normalization only | Reset all declared state | 0 | nll_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Normalization only | Reset all declared state | 0 | brier_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Normalization only | Reset all declared state | 0 | first_batch_max_logit_diff | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Normalization only | Reset all declared state | 4 | disagreement | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Normalization only | Reset all declared state | 4 | accuracy_ab | 1 | 0.861328 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.861328125} |
| Normalization only | Reset all declared state | 4 | accuracy_ba | 1 | 0.861328 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.861328125} |
| Normalization only | Reset all declared state | 4 | signed_error_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Normalization only | Reset all declared state | 4 | absolute_error_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Normalization only | Reset all declared state | 4 | nll_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Normalization only | Reset all declared state | 4 | brier_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Normalization only | Reset all declared state | 4 | first_batch_max_logit_diff | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Normalization only | No external reset | 0 | disagreement | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Normalization only | No external reset | 0 | accuracy_ab | 1 | 0.861328 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.861328125} |
| Normalization only | No external reset | 0 | accuracy_ba | 1 | 0.861328 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.861328125} |
| Normalization only | No external reset | 0 | signed_error_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Normalization only | No external reset | 0 | absolute_error_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Normalization only | No external reset | 0 | nll_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Normalization only | No external reset | 0 | brier_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Normalization only | No external reset | 0 | first_batch_max_logit_diff | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Normalization only | No external reset | 4 | disagreement | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Normalization only | No external reset | 4 | accuracy_ab | 1 | 0.861328 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.861328125} |
| Normalization only | No external reset | 4 | accuracy_ba | 1 | 0.861328 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.861328125} |
| Normalization only | No external reset | 4 | signed_error_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Normalization only | No external reset | 4 | absolute_error_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Normalization only | No external reset | 4 | nll_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Normalization only | No external reset | 4 | brier_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Normalization only | No external reset | 4 | first_batch_max_logit_diff | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset all declared state | 0 | disagreement | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset all declared state | 0 | accuracy_ab | 1 | 0.861654 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8616536458333334} |
| SAR (complete-state implementation) | Reset all declared state | 0 | accuracy_ba | 1 | 0.861654 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8616536458333334} |
| SAR (complete-state implementation) | Reset all declared state | 0 | signed_error_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset all declared state | 0 | absolute_error_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset all declared state | 0 | nll_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset all declared state | 0 | brier_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset all declared state | 0 | first_batch_max_logit_diff | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset all declared state | 4 | disagreement | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset all declared state | 4 | accuracy_ab | 1 | 0.861654 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8616536458333334} |
| SAR (complete-state implementation) | Reset all declared state | 4 | accuracy_ba | 1 | 0.861654 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8616536458333334} |
| SAR (complete-state implementation) | Reset all declared state | 4 | signed_error_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset all declared state | 4 | absolute_error_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset all declared state | 4 | nll_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset all declared state | 4 | brier_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset all declared state | 4 | first_batch_max_logit_diff | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | disagreement | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | accuracy_ab | 1 | 0.861654 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8616536458333334} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | accuracy_ba | 1 | 0.861654 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8616536458333334} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | signed_error_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | absolute_error_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | nll_gap | 1 | -7.78265e-07 | — | — | — | 3 | 3 | {"uci_internal_fixed": -7.782654969761457e-07} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | brier_gap | 1 | -1.37256e-07 | — | — | — | 3 | 3 | {"uci_internal_fixed": -1.3725552089280854e-07} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | first_batch_max_logit_diff | 1 | 0.0120468 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0120467742284139} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | disagreement | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | accuracy_ab | 1 | 0.861654 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8616536458333334} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | accuracy_ba | 1 | 0.861654 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8616536458333334} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | signed_error_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | absolute_error_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | nll_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | brier_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | first_batch_max_logit_diff | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | No external reset | 0 | disagreement | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | No external reset | 0 | accuracy_ab | 1 | 0.861328 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.861328125} |
| SAR (complete-state implementation) | No external reset | 0 | accuracy_ba | 1 | 0.861328 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.861328125} |
| SAR (complete-state implementation) | No external reset | 0 | signed_error_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | No external reset | 0 | absolute_error_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | No external reset | 0 | nll_gap | 1 | 5.04814e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": 5.0481432768175876e-05} |
| SAR (complete-state implementation) | No external reset | 0 | brier_gap | 1 | 1.31498e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": 1.3149844326745588e-05} |
| SAR (complete-state implementation) | No external reset | 0 | first_batch_max_logit_diff | 1 | 0.0120468 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0120467742284139} |
| SAR (complete-state implementation) | No external reset | 4 | disagreement | 1 | 0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0003255208333333333} |
| SAR (complete-state implementation) | No external reset | 4 | accuracy_ab | 1 | 0.861328 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.861328125} |
| SAR (complete-state implementation) | No external reset | 4 | accuracy_ba | 1 | 0.861654 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8616536458333334} |
| SAR (complete-state implementation) | No external reset | 4 | signed_error_gap | 1 | 0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0003255208333333333} |
| SAR (complete-state implementation) | No external reset | 4 | absolute_error_gap | 1 | 0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0003255208333333333} |
| SAR (complete-state implementation) | No external reset | 4 | nll_gap | 1 | -2.92067e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": -2.920671777545e-05} |
| SAR (complete-state implementation) | No external reset | 4 | brier_gap | 1 | -4.94772e-06 | — | — | — | 3 | 3 | {"uci_internal_fixed": -4.947722413421267e-06} |
| SAR (complete-state implementation) | No external reset | 4 | first_batch_max_logit_diff | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | disagreement | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | accuracy_ab | 1 | 0.861328 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.861328125} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | accuracy_ba | 1 | 0.861328 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.861328125} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | signed_error_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | absolute_error_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | nll_gap | 1 | 5.04631e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": 5.0463086314296627e-05} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | brier_gap | 1 | 1.31388e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": 1.313880977528957e-05} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | first_batch_max_logit_diff | 1 | 0.0120468 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0120467742284139} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | disagreement | 1 | 0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0003255208333333333} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | accuracy_ab | 1 | 0.861328 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.861328125} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | accuracy_ba | 1 | 0.861654 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8616536458333334} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | signed_error_gap | 1 | 0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0003255208333333333} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | absolute_error_gap | 1 | 0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0003255208333333333} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | nll_gap | 1 | -2.92067e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": -2.920671777545e-05} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | brier_gap | 1 | -4.94772e-06 | — | — | — | 3 | 3 | {"uci_internal_fixed": -4.947722413421267e-06} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | first_batch_max_logit_diff | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | disagreement | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | accuracy_ab | 1 | 0.861654 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8616536458333334} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | accuracy_ba | 1 | 0.861654 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8616536458333334} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | signed_error_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | absolute_error_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | nll_gap | 1 | -7.78265e-07 | — | — | — | 3 | 3 | {"uci_internal_fixed": -7.782654969761457e-07} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | brier_gap | 1 | -1.37256e-07 | — | — | — | 3 | 3 | {"uci_internal_fixed": -1.3725552089280854e-07} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | first_batch_max_logit_diff | 1 | 0.0120468 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0120467742284139} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | disagreement | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | accuracy_ab | 1 | 0.861654 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8616536458333334} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | accuracy_ba | 1 | 0.861654 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8616536458333334} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | signed_error_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | absolute_error_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | nll_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | brier_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | first_batch_max_logit_diff | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset parameters only | 0 | disagreement | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset parameters only | 0 | accuracy_ab | 1 | 0.861328 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.861328125} |
| SAR (complete-state implementation) | Reset parameters only | 0 | accuracy_ba | 1 | 0.861328 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.861328125} |
| SAR (complete-state implementation) | Reset parameters only | 0 | signed_error_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset parameters only | 0 | absolute_error_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset parameters only | 0 | nll_gap | 1 | 5.1069e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": 5.106900193368092e-05} |
| SAR (complete-state implementation) | Reset parameters only | 0 | brier_gap | 1 | 1.31883e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": 1.3188260466219398e-05} |
| SAR (complete-state implementation) | Reset parameters only | 0 | first_batch_max_logit_diff | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset parameters only | 4 | disagreement | 1 | 0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0003255208333333333} |
| SAR (complete-state implementation) | Reset parameters only | 4 | accuracy_ab | 1 | 0.861328 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.861328125} |
| SAR (complete-state implementation) | Reset parameters only | 4 | accuracy_ba | 1 | 0.861654 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8616536458333334} |
| SAR (complete-state implementation) | Reset parameters only | 4 | signed_error_gap | 1 | 0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0003255208333333333} |
| SAR (complete-state implementation) | Reset parameters only | 4 | absolute_error_gap | 1 | 0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0003255208333333333} |
| SAR (complete-state implementation) | Reset parameters only | 4 | nll_gap | 1 | -2.92067e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": -2.920671777545e-05} |
| SAR (complete-state implementation) | Reset parameters only | 4 | brier_gap | 1 | -4.94772e-06 | — | — | — | 3 | 3 | {"uci_internal_fixed": -4.947722413421267e-06} |
| SAR (complete-state implementation) | Reset parameters only | 4 | first_batch_max_logit_diff | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | disagreement | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | accuracy_ab | 1 | 0.861654 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8616536458333334} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | accuracy_ba | 1 | 0.861654 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8616536458333334} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | signed_error_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | absolute_error_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | nll_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | brier_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | first_batch_max_logit_diff | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | disagreement | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | accuracy_ab | 1 | 0.861654 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8616536458333334} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | accuracy_ba | 1 | 0.861654 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8616536458333334} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | signed_error_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | absolute_error_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | nll_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | brier_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | first_batch_max_logit_diff | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | disagreement | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | accuracy_ab | 1 | 0.861328 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.861328125} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | accuracy_ba | 1 | 0.861328 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.861328125} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | signed_error_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | absolute_error_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | nll_gap | 1 | 5.10492e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": 5.1049229228724935e-05} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | brier_gap | 1 | 1.31764e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": 1.31763798841301e-05} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | first_batch_max_logit_diff | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | disagreement | 1 | 0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0003255208333333333} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | accuracy_ab | 1 | 0.861328 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.861328125} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | accuracy_ba | 1 | 0.861654 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8616536458333334} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | signed_error_gap | 1 | 0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0003255208333333333} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | absolute_error_gap | 1 | 0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0003255208333333333} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | nll_gap | 1 | -2.92067e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": -2.920671777545e-05} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | brier_gap | 1 | -4.94772e-06 | — | — | — | 3 | 3 | {"uci_internal_fixed": -4.947722413421267e-06} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | first_batch_max_logit_diff | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | disagreement | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | accuracy_ab | 1 | 0.861654 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8616536458333334} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | accuracy_ba | 1 | 0.861654 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8616536458333334} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | signed_error_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | absolute_error_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | nll_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | brier_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | first_batch_max_logit_diff | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | disagreement | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | accuracy_ab | 1 | 0.861654 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8616536458333334} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | accuracy_ba | 1 | 0.861654 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8616536458333334} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | signed_error_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | absolute_error_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | nll_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | brier_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | first_batch_max_logit_diff | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Source | Reset all declared state | 0 | disagreement | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Source | Reset all declared state | 0 | accuracy_ab | 1 | 0.814128 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8141276041666666} |
| Source | Reset all declared state | 0 | accuracy_ba | 1 | 0.814128 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8141276041666666} |
| Source | Reset all declared state | 0 | signed_error_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Source | Reset all declared state | 0 | absolute_error_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Source | Reset all declared state | 0 | nll_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Source | Reset all declared state | 0 | brier_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Source | Reset all declared state | 0 | first_batch_max_logit_diff | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Source | Reset all declared state | 4 | disagreement | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Source | Reset all declared state | 4 | accuracy_ab | 1 | 0.814128 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8141276041666666} |
| Source | Reset all declared state | 4 | accuracy_ba | 1 | 0.814128 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8141276041666666} |
| Source | Reset all declared state | 4 | signed_error_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Source | Reset all declared state | 4 | absolute_error_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Source | Reset all declared state | 4 | nll_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Source | Reset all declared state | 4 | brier_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Source | Reset all declared state | 4 | first_batch_max_logit_diff | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Source | No external reset | 0 | disagreement | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Source | No external reset | 0 | accuracy_ab | 1 | 0.814128 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8141276041666666} |
| Source | No external reset | 0 | accuracy_ba | 1 | 0.814128 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8141276041666666} |
| Source | No external reset | 0 | signed_error_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Source | No external reset | 0 | absolute_error_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Source | No external reset | 0 | nll_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Source | No external reset | 0 | brier_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Source | No external reset | 0 | first_batch_max_logit_diff | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Source | No external reset | 4 | disagreement | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Source | No external reset | 4 | accuracy_ab | 1 | 0.814128 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8141276041666666} |
| Source | No external reset | 4 | accuracy_ba | 1 | 0.814128 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8141276041666666} |
| Source | No external reset | 4 | signed_error_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Source | No external reset | 4 | absolute_error_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Source | No external reset | 4 | nll_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Source | No external reset | 4 | brier_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Source | No external reset | 4 | first_batch_max_logit_diff | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset all declared state | 0 | disagreement | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset all declared state | 0 | accuracy_ab | 1 | 0.861654 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8616536458333334} |
| Tent | Reset all declared state | 0 | accuracy_ba | 1 | 0.861654 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8616536458333334} |
| Tent | Reset all declared state | 0 | signed_error_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset all declared state | 0 | absolute_error_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset all declared state | 0 | nll_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset all declared state | 0 | brier_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset all declared state | 0 | first_batch_max_logit_diff | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset all declared state | 4 | disagreement | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset all declared state | 4 | accuracy_ab | 1 | 0.861654 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8616536458333334} |
| Tent | Reset all declared state | 4 | accuracy_ba | 1 | 0.861654 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8616536458333334} |
| Tent | Reset all declared state | 4 | signed_error_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset all declared state | 4 | absolute_error_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset all declared state | 4 | nll_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset all declared state | 4 | brier_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset all declared state | 4 | first_batch_max_logit_diff | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset auxiliary state only | 0 | disagreement | 1 | 0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0003255208333333333} |
| Tent | Reset auxiliary state only | 0 | accuracy_ab | 1 | 0.861979 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8619791666666666} |
| Tent | Reset auxiliary state only | 0 | accuracy_ba | 1 | 0.861654 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8616536458333334} |
| Tent | Reset auxiliary state only | 0 | signed_error_gap | 1 | -0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0003255208333333333} |
| Tent | Reset auxiliary state only | 0 | absolute_error_gap | 1 | 0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0003255208333333333} |
| Tent | Reset auxiliary state only | 0 | nll_gap | 1 | 2.61611e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": 2.6161054073633804e-05} |
| Tent | Reset auxiliary state only | 0 | brier_gap | 1 | 2.23542e-06 | — | — | — | 3 | 3 | {"uci_internal_fixed": 2.235415372002734e-06} |
| Tent | Reset auxiliary state only | 0 | first_batch_max_logit_diff | 1 | 0.00903153 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.00903153419494625} |
| Tent | Reset auxiliary state only | 4 | disagreement | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset auxiliary state only | 4 | accuracy_ab | 1 | 0.862305 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8623046875} |
| Tent | Reset auxiliary state only | 4 | accuracy_ba | 1 | 0.862305 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8623046875} |
| Tent | Reset auxiliary state only | 4 | signed_error_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset auxiliary state only | 4 | absolute_error_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset auxiliary state only | 4 | nll_gap | 1 | 1.7286e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": 1.7285966563115378e-05} |
| Tent | Reset auxiliary state only | 4 | brier_gap | 1 | 1.58798e-06 | — | — | — | 3 | 3 | {"uci_internal_fixed": 1.5879808014113844e-06} |
| Tent | Reset auxiliary state only | 4 | first_batch_max_logit_diff | 1 | 0.00592633 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.005926330884297633} |
| Tent | No external reset | 0 | disagreement | 1 | 0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0003255208333333333} |
| Tent | No external reset | 0 | accuracy_ab | 1 | 0.861979 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8619791666666666} |
| Tent | No external reset | 0 | accuracy_ba | 1 | 0.861654 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8616536458333334} |
| Tent | No external reset | 0 | signed_error_gap | 1 | -0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0003255208333333333} |
| Tent | No external reset | 0 | absolute_error_gap | 1 | 0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0003255208333333333} |
| Tent | No external reset | 0 | nll_gap | 1 | 2.61611e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": 2.6161054073633804e-05} |
| Tent | No external reset | 0 | brier_gap | 1 | 2.23542e-06 | — | — | — | 3 | 3 | {"uci_internal_fixed": 2.235415372002734e-06} |
| Tent | No external reset | 0 | first_batch_max_logit_diff | 1 | 0.00903153 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.00903153419494625} |
| Tent | No external reset | 4 | disagreement | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | No external reset | 4 | accuracy_ab | 1 | 0.862305 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8623046875} |
| Tent | No external reset | 4 | accuracy_ba | 1 | 0.862305 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8623046875} |
| Tent | No external reset | 4 | signed_error_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | No external reset | 4 | absolute_error_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | No external reset | 4 | nll_gap | 1 | 1.7286e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": 1.7285966563115378e-05} |
| Tent | No external reset | 4 | brier_gap | 1 | 1.58798e-06 | — | — | — | 3 | 3 | {"uci_internal_fixed": 1.5879808014113844e-06} |
| Tent | No external reset | 4 | first_batch_max_logit_diff | 1 | 0.00592633 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.005926330884297633} |
| Tent | Reset optimizer only | 0 | disagreement | 1 | 0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0003255208333333333} |
| Tent | Reset optimizer only | 0 | accuracy_ab | 1 | 0.861979 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8619791666666666} |
| Tent | Reset optimizer only | 0 | accuracy_ba | 1 | 0.861654 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8616536458333334} |
| Tent | Reset optimizer only | 0 | signed_error_gap | 1 | -0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0003255208333333333} |
| Tent | Reset optimizer only | 0 | absolute_error_gap | 1 | 0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0003255208333333333} |
| Tent | Reset optimizer only | 0 | nll_gap | 1 | 6.28539e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": 6.285385285298318e-05} |
| Tent | Reset optimizer only | 0 | brier_gap | 1 | 4.59213e-06 | — | — | — | 3 | 3 | {"uci_internal_fixed": 4.592129666939351e-06} |
| Tent | Reset optimizer only | 0 | first_batch_max_logit_diff | 1 | 0.00903153 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.00903153419494625} |
| Tent | Reset optimizer only | 4 | disagreement | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset optimizer only | 4 | accuracy_ab | 1 | 0.862305 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8623046875} |
| Tent | Reset optimizer only | 4 | accuracy_ba | 1 | 0.862305 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8623046875} |
| Tent | Reset optimizer only | 4 | signed_error_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset optimizer only | 4 | absolute_error_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset optimizer only | 4 | nll_gap | 1 | 4.17469e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": 4.1746933812486805e-05} |
| Tent | Reset optimizer only | 4 | brier_gap | 1 | 3.30081e-06 | — | — | — | 3 | 3 | {"uci_internal_fixed": 3.300805621079169e-06} |
| Tent | Reset optimizer only | 4 | first_batch_max_logit_diff | 1 | 0.00592633 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.005926330884297633} |
| Tent | Reset optimizer + auxiliary state | 0 | disagreement | 1 | 0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0003255208333333333} |
| Tent | Reset optimizer + auxiliary state | 0 | accuracy_ab | 1 | 0.861979 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8619791666666666} |
| Tent | Reset optimizer + auxiliary state | 0 | accuracy_ba | 1 | 0.861654 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8616536458333334} |
| Tent | Reset optimizer + auxiliary state | 0 | signed_error_gap | 1 | -0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0003255208333333333} |
| Tent | Reset optimizer + auxiliary state | 0 | absolute_error_gap | 1 | 0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0003255208333333333} |
| Tent | Reset optimizer + auxiliary state | 0 | nll_gap | 1 | 6.28539e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": 6.285385285298318e-05} |
| Tent | Reset optimizer + auxiliary state | 0 | brier_gap | 1 | 4.59213e-06 | — | — | — | 3 | 3 | {"uci_internal_fixed": 4.592129666939351e-06} |
| Tent | Reset optimizer + auxiliary state | 0 | first_batch_max_logit_diff | 1 | 0.00903153 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.00903153419494625} |
| Tent | Reset optimizer + auxiliary state | 4 | disagreement | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset optimizer + auxiliary state | 4 | accuracy_ab | 1 | 0.862305 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8623046875} |
| Tent | Reset optimizer + auxiliary state | 4 | accuracy_ba | 1 | 0.862305 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8623046875} |
| Tent | Reset optimizer + auxiliary state | 4 | signed_error_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset optimizer + auxiliary state | 4 | absolute_error_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset optimizer + auxiliary state | 4 | nll_gap | 1 | 4.17469e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": 4.1746933812486805e-05} |
| Tent | Reset optimizer + auxiliary state | 4 | brier_gap | 1 | 3.30081e-06 | — | — | — | 3 | 3 | {"uci_internal_fixed": 3.300805621079169e-06} |
| Tent | Reset optimizer + auxiliary state | 4 | first_batch_max_logit_diff | 1 | 0.00592633 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.005926330884297633} |
| Tent | Reset parameters only | 0 | disagreement | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset parameters only | 0 | accuracy_ab | 1 | 0.861654 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8616536458333334} |
| Tent | Reset parameters only | 0 | accuracy_ba | 1 | 0.861654 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8616536458333334} |
| Tent | Reset parameters only | 0 | signed_error_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset parameters only | 0 | absolute_error_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset parameters only | 0 | nll_gap | 1 | -3.66149e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": -3.661486678529051e-05} |
| Tent | Reset parameters only | 0 | brier_gap | 1 | -2.34558e-06 | — | — | — | 3 | 3 | {"uci_internal_fixed": -2.345581919303494e-06} |
| Tent | Reset parameters only | 0 | first_batch_max_logit_diff | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset parameters only | 4 | disagreement | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset parameters only | 4 | accuracy_ab | 1 | 0.861654 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8616536458333334} |
| Tent | Reset parameters only | 4 | accuracy_ba | 1 | 0.861654 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8616536458333334} |
| Tent | Reset parameters only | 4 | signed_error_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset parameters only | 4 | absolute_error_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset parameters only | 4 | nll_gap | 1 | -2.37046e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": -2.3704563783675183e-05} |
| Tent | Reset parameters only | 4 | brier_gap | 1 | -1.38028e-06 | — | — | — | 3 | 3 | {"uci_internal_fixed": -1.3802790382935286e-06} |
| Tent | Reset parameters only | 4 | first_batch_max_logit_diff | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset parameters + auxiliary state | 0 | disagreement | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset parameters + auxiliary state | 0 | accuracy_ab | 1 | 0.861654 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8616536458333334} |
| Tent | Reset parameters + auxiliary state | 0 | accuracy_ba | 1 | 0.861654 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8616536458333334} |
| Tent | Reset parameters + auxiliary state | 0 | signed_error_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset parameters + auxiliary state | 0 | absolute_error_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset parameters + auxiliary state | 0 | nll_gap | 1 | -3.66149e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": -3.661486678529051e-05} |
| Tent | Reset parameters + auxiliary state | 0 | brier_gap | 1 | -2.34558e-06 | — | — | — | 3 | 3 | {"uci_internal_fixed": -2.345581919303494e-06} |
| Tent | Reset parameters + auxiliary state | 0 | first_batch_max_logit_diff | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset parameters + auxiliary state | 4 | disagreement | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset parameters + auxiliary state | 4 | accuracy_ab | 1 | 0.861654 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8616536458333334} |
| Tent | Reset parameters + auxiliary state | 4 | accuracy_ba | 1 | 0.861654 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8616536458333334} |
| Tent | Reset parameters + auxiliary state | 4 | signed_error_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset parameters + auxiliary state | 4 | absolute_error_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset parameters + auxiliary state | 4 | nll_gap | 1 | -2.37046e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": -2.3704563783675183e-05} |
| Tent | Reset parameters + auxiliary state | 4 | brier_gap | 1 | -1.38028e-06 | — | — | — | 3 | 3 | {"uci_internal_fixed": -1.3802790382935286e-06} |
| Tent | Reset parameters + auxiliary state | 4 | first_batch_max_logit_diff | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset parameters + optimizer | 0 | disagreement | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset parameters + optimizer | 0 | accuracy_ab | 1 | 0.861654 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8616536458333334} |
| Tent | Reset parameters + optimizer | 0 | accuracy_ba | 1 | 0.861654 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8616536458333334} |
| Tent | Reset parameters + optimizer | 0 | signed_error_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset parameters + optimizer | 0 | absolute_error_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset parameters + optimizer | 0 | nll_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset parameters + optimizer | 0 | brier_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset parameters + optimizer | 0 | first_batch_max_logit_diff | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset parameters + optimizer | 4 | disagreement | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset parameters + optimizer | 4 | accuracy_ab | 1 | 0.861654 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8616536458333334} |
| Tent | Reset parameters + optimizer | 4 | accuracy_ba | 1 | 0.861654 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8616536458333334} |
| Tent | Reset parameters + optimizer | 4 | signed_error_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset parameters + optimizer | 4 | absolute_error_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset parameters + optimizer | 4 | nll_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset parameters + optimizer | 4 | brier_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset parameters + optimizer | 4 | first_batch_max_logit_diff | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | disagreement | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | accuracy_ab | 1 | 0.861654 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8616536458333334} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | accuracy_ba | 1 | 0.861654 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8616536458333334} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | signed_error_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | absolute_error_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | nll_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | brier_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | first_batch_max_logit_diff | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | disagreement | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | accuracy_ab | 1 | 0.861654 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8616536458333334} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | accuracy_ba | 1 | 0.861654 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8616536458333334} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | signed_error_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | absolute_error_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | nll_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | brier_gap | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | first_batch_max_logit_diff | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |


### paired: descriptive seed repetitions

The same image panel is reused across seeds. These standard deviations describe seed variability only; no confidence interval is justified from treating seeds as new image panels.

| method | intervention | washout_batches | panel_id | metric | n_seeds | mean | seed_sd_descriptive | individual_seeds |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Normalization only | Reset all declared state | 0 | uci_internal_fixed | disagreement | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Normalization only | Reset all declared state | 0 | uci_internal_fixed | accuracy_ab | 3 | 0.861328 | 0.0182437 | {"17": 0.8583984375, "29": 0.8447265625, "43": 0.880859375} |
| Normalization only | Reset all declared state | 0 | uci_internal_fixed | accuracy_ba | 3 | 0.861328 | 0.0182437 | {"17": 0.8583984375, "29": 0.8447265625, "43": 0.880859375} |
| Normalization only | Reset all declared state | 0 | uci_internal_fixed | signed_error_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Normalization only | Reset all declared state | 0 | uci_internal_fixed | absolute_error_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Normalization only | Reset all declared state | 0 | uci_internal_fixed | nll_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Normalization only | Reset all declared state | 0 | uci_internal_fixed | brier_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Normalization only | Reset all declared state | 0 | uci_internal_fixed | first_batch_max_logit_diff | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Normalization only | Reset all declared state | 4 | uci_internal_fixed | disagreement | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Normalization only | Reset all declared state | 4 | uci_internal_fixed | accuracy_ab | 3 | 0.861328 | 0.0182437 | {"17": 0.8583984375, "29": 0.8447265625, "43": 0.880859375} |
| Normalization only | Reset all declared state | 4 | uci_internal_fixed | accuracy_ba | 3 | 0.861328 | 0.0182437 | {"17": 0.8583984375, "29": 0.8447265625, "43": 0.880859375} |
| Normalization only | Reset all declared state | 4 | uci_internal_fixed | signed_error_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Normalization only | Reset all declared state | 4 | uci_internal_fixed | absolute_error_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Normalization only | Reset all declared state | 4 | uci_internal_fixed | nll_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Normalization only | Reset all declared state | 4 | uci_internal_fixed | brier_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Normalization only | Reset all declared state | 4 | uci_internal_fixed | first_batch_max_logit_diff | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Normalization only | No external reset | 0 | uci_internal_fixed | disagreement | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Normalization only | No external reset | 0 | uci_internal_fixed | accuracy_ab | 3 | 0.861328 | 0.0182437 | {"17": 0.8583984375, "29": 0.8447265625, "43": 0.880859375} |
| Normalization only | No external reset | 0 | uci_internal_fixed | accuracy_ba | 3 | 0.861328 | 0.0182437 | {"17": 0.8583984375, "29": 0.8447265625, "43": 0.880859375} |
| Normalization only | No external reset | 0 | uci_internal_fixed | signed_error_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Normalization only | No external reset | 0 | uci_internal_fixed | absolute_error_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Normalization only | No external reset | 0 | uci_internal_fixed | nll_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Normalization only | No external reset | 0 | uci_internal_fixed | brier_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Normalization only | No external reset | 0 | uci_internal_fixed | first_batch_max_logit_diff | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Normalization only | No external reset | 4 | uci_internal_fixed | disagreement | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Normalization only | No external reset | 4 | uci_internal_fixed | accuracy_ab | 3 | 0.861328 | 0.0182437 | {"17": 0.8583984375, "29": 0.8447265625, "43": 0.880859375} |
| Normalization only | No external reset | 4 | uci_internal_fixed | accuracy_ba | 3 | 0.861328 | 0.0182437 | {"17": 0.8583984375, "29": 0.8447265625, "43": 0.880859375} |
| Normalization only | No external reset | 4 | uci_internal_fixed | signed_error_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Normalization only | No external reset | 4 | uci_internal_fixed | absolute_error_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Normalization only | No external reset | 4 | uci_internal_fixed | nll_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Normalization only | No external reset | 4 | uci_internal_fixed | brier_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Normalization only | No external reset | 4 | uci_internal_fixed | first_batch_max_logit_diff | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset all declared state | 0 | uci_internal_fixed | disagreement | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset all declared state | 0 | uci_internal_fixed | accuracy_ab | 3 | 0.861654 | 0.0181739 | {"17": 0.859375, "29": 0.8447265625, "43": 0.880859375} |
| SAR (complete-state implementation) | Reset all declared state | 0 | uci_internal_fixed | accuracy_ba | 3 | 0.861654 | 0.0181739 | {"17": 0.859375, "29": 0.8447265625, "43": 0.880859375} |
| SAR (complete-state implementation) | Reset all declared state | 0 | uci_internal_fixed | signed_error_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset all declared state | 0 | uci_internal_fixed | absolute_error_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset all declared state | 0 | uci_internal_fixed | nll_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset all declared state | 0 | uci_internal_fixed | brier_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset all declared state | 0 | uci_internal_fixed | first_batch_max_logit_diff | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset all declared state | 4 | uci_internal_fixed | disagreement | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset all declared state | 4 | uci_internal_fixed | accuracy_ab | 3 | 0.861654 | 0.0181739 | {"17": 0.859375, "29": 0.8447265625, "43": 0.880859375} |
| SAR (complete-state implementation) | Reset all declared state | 4 | uci_internal_fixed | accuracy_ba | 3 | 0.861654 | 0.0181739 | {"17": 0.859375, "29": 0.8447265625, "43": 0.880859375} |
| SAR (complete-state implementation) | Reset all declared state | 4 | uci_internal_fixed | signed_error_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset all declared state | 4 | uci_internal_fixed | absolute_error_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset all declared state | 4 | uci_internal_fixed | nll_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset all declared state | 4 | uci_internal_fixed | brier_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset all declared state | 4 | uci_internal_fixed | first_batch_max_logit_diff | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | uci_internal_fixed | disagreement | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | uci_internal_fixed | accuracy_ab | 3 | 0.861654 | 0.0181739 | {"17": 0.859375, "29": 0.8447265625, "43": 0.880859375} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | uci_internal_fixed | accuracy_ba | 3 | 0.861654 | 0.0181739 | {"17": 0.859375, "29": 0.8447265625, "43": 0.880859375} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | uci_internal_fixed | signed_error_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | uci_internal_fixed | absolute_error_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | uci_internal_fixed | nll_gap | 3 | -7.78265e-07 | 9.12369e-07 | {"17": -7.389067389722282e-07, "29": 1.1378687791649412e-07, "43": -1.7096766298727029e-06} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | uci_internal_fixed | brier_gap | 3 | -1.37256e-07 | 2.01412e-07 | {"17": -3.067409941326371e-07, "29": 8.540978117810295e-08, "43": -1.9043534972389145e-07} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | uci_internal_fixed | first_batch_max_logit_diff | 3 | 0.0120468 | 0.00206013 | {"17": 0.01055145263671875, "29": 0.01439666748046875, "43": 0.0111922025680542} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | uci_internal_fixed | disagreement | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | uci_internal_fixed | accuracy_ab | 3 | 0.861654 | 0.0181739 | {"17": 0.859375, "29": 0.8447265625, "43": 0.880859375} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | uci_internal_fixed | accuracy_ba | 3 | 0.861654 | 0.0181739 | {"17": 0.859375, "29": 0.8447265625, "43": 0.880859375} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | uci_internal_fixed | signed_error_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | uci_internal_fixed | absolute_error_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | uci_internal_fixed | nll_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | uci_internal_fixed | brier_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | uci_internal_fixed | first_batch_max_logit_diff | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | No external reset | 0 | uci_internal_fixed | disagreement | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | No external reset | 0 | uci_internal_fixed | accuracy_ab | 3 | 0.861328 | 0.0182437 | {"17": 0.8583984375, "29": 0.8447265625, "43": 0.880859375} |
| SAR (complete-state implementation) | No external reset | 0 | uci_internal_fixed | accuracy_ba | 3 | 0.861328 | 0.0182437 | {"17": 0.8583984375, "29": 0.8447265625, "43": 0.880859375} |
| SAR (complete-state implementation) | No external reset | 0 | uci_internal_fixed | signed_error_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | No external reset | 0 | uci_internal_fixed | absolute_error_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | No external reset | 0 | uci_internal_fixed | nll_gap | 3 | 5.04814e-05 | 9.31129e-05 | {"17": 0.0001579838026641614, "29": -4.829827729761066e-06, "43": -1.7096766298727029e-06} |
| SAR (complete-state implementation) | No external reset | 0 | uci_internal_fixed | brier_gap | 3 | 1.31498e-05 | 2.3767e-05 | {"17": 4.0590077020863716e-05, "29": -9.50108690903062e-07, "43": -1.9043534972389145e-07} |
| SAR (complete-state implementation) | No external reset | 0 | uci_internal_fixed | first_batch_max_logit_diff | 3 | 0.0120468 | 0.00206013 | {"17": 0.01055145263671875, "29": 0.01439666748046875, "43": 0.0111922025680542} |
| SAR (complete-state implementation) | No external reset | 4 | uci_internal_fixed | disagreement | 3 | 0.000325521 | 0.000563819 | {"17": 0.0009765625, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | No external reset | 4 | uci_internal_fixed | accuracy_ab | 3 | 0.861328 | 0.0182437 | {"17": 0.8583984375, "29": 0.8447265625, "43": 0.880859375} |
| SAR (complete-state implementation) | No external reset | 4 | uci_internal_fixed | accuracy_ba | 3 | 0.861654 | 0.0181739 | {"17": 0.859375, "29": 0.8447265625, "43": 0.880859375} |
| SAR (complete-state implementation) | No external reset | 4 | uci_internal_fixed | signed_error_gap | 3 | 0.000325521 | 0.000563819 | {"17": 0.0009765625, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | No external reset | 4 | uci_internal_fixed | absolute_error_gap | 3 | 0.000325521 | 0.000563819 | {"17": 0.0009765625, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | No external reset | 4 | uci_internal_fixed | nll_gap | 3 | -2.92067e-05 | 5.05875e-05 | {"17": -8.762015332635e-05, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | No external reset | 4 | uci_internal_fixed | brier_gap | 3 | -4.94772e-06 | 8.56971e-06 | {"17": -1.48431672402638e-05, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | No external reset | 4 | uci_internal_fixed | first_batch_max_logit_diff | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | uci_internal_fixed | disagreement | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | uci_internal_fixed | accuracy_ab | 3 | 0.861328 | 0.0182437 | {"17": 0.8583984375, "29": 0.8447265625, "43": 0.880859375} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | uci_internal_fixed | accuracy_ba | 3 | 0.861328 | 0.0182437 | {"17": 0.8583984375, "29": 0.8447265625, "43": 0.880859375} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | uci_internal_fixed | signed_error_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | uci_internal_fixed | absolute_error_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | uci_internal_fixed | nll_gap | 3 | 5.04631e-05 | 9.30811e-05 | {"17": 0.00015792876330252364, "29": -4.829827729761066e-06, "43": -1.7096766298727029e-06} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | uci_internal_fixed | brier_gap | 3 | 1.31388e-05 | 2.37479e-05 | {"17": 4.055697336649566e-05, "29": -9.50108690903062e-07, "43": -1.9043534972389145e-07} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | uci_internal_fixed | first_batch_max_logit_diff | 3 | 0.0120468 | 0.00206013 | {"17": 0.01055145263671875, "29": 0.01439666748046875, "43": 0.0111922025680542} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | uci_internal_fixed | disagreement | 3 | 0.000325521 | 0.000563819 | {"17": 0.0009765625, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | uci_internal_fixed | accuracy_ab | 3 | 0.861328 | 0.0182437 | {"17": 0.8583984375, "29": 0.8447265625, "43": 0.880859375} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | uci_internal_fixed | accuracy_ba | 3 | 0.861654 | 0.0181739 | {"17": 0.859375, "29": 0.8447265625, "43": 0.880859375} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | uci_internal_fixed | signed_error_gap | 3 | 0.000325521 | 0.000563819 | {"17": 0.0009765625, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | uci_internal_fixed | absolute_error_gap | 3 | 0.000325521 | 0.000563819 | {"17": 0.0009765625, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | uci_internal_fixed | nll_gap | 3 | -2.92067e-05 | 5.05875e-05 | {"17": -8.762015332635e-05, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | uci_internal_fixed | brier_gap | 3 | -4.94772e-06 | 8.56971e-06 | {"17": -1.48431672402638e-05, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | uci_internal_fixed | first_batch_max_logit_diff | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | uci_internal_fixed | disagreement | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | uci_internal_fixed | accuracy_ab | 3 | 0.861654 | 0.0181739 | {"17": 0.859375, "29": 0.8447265625, "43": 0.880859375} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | uci_internal_fixed | accuracy_ba | 3 | 0.861654 | 0.0181739 | {"17": 0.859375, "29": 0.8447265625, "43": 0.880859375} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | uci_internal_fixed | signed_error_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | uci_internal_fixed | absolute_error_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | uci_internal_fixed | nll_gap | 3 | -7.78265e-07 | 9.12369e-07 | {"17": -7.389067389722282e-07, "29": 1.1378687791649412e-07, "43": -1.7096766298727029e-06} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | uci_internal_fixed | brier_gap | 3 | -1.37256e-07 | 2.01412e-07 | {"17": -3.067409941326371e-07, "29": 8.540978117810295e-08, "43": -1.9043534972389145e-07} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | uci_internal_fixed | first_batch_max_logit_diff | 3 | 0.0120468 | 0.00206013 | {"17": 0.01055145263671875, "29": 0.01439666748046875, "43": 0.0111922025680542} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | uci_internal_fixed | disagreement | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | uci_internal_fixed | accuracy_ab | 3 | 0.861654 | 0.0181739 | {"17": 0.859375, "29": 0.8447265625, "43": 0.880859375} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | uci_internal_fixed | accuracy_ba | 3 | 0.861654 | 0.0181739 | {"17": 0.859375, "29": 0.8447265625, "43": 0.880859375} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | uci_internal_fixed | signed_error_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | uci_internal_fixed | absolute_error_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | uci_internal_fixed | nll_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | uci_internal_fixed | brier_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | uci_internal_fixed | first_batch_max_logit_diff | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters only | 0 | uci_internal_fixed | disagreement | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters only | 0 | uci_internal_fixed | accuracy_ab | 3 | 0.861328 | 0.0182437 | {"17": 0.8583984375, "29": 0.8447265625, "43": 0.880859375} |
| SAR (complete-state implementation) | Reset parameters only | 0 | uci_internal_fixed | accuracy_ba | 3 | 0.861328 | 0.0182437 | {"17": 0.8583984375, "29": 0.8447265625, "43": 0.880859375} |
| SAR (complete-state implementation) | Reset parameters only | 0 | uci_internal_fixed | signed_error_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters only | 0 | uci_internal_fixed | absolute_error_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters only | 0 | uci_internal_fixed | nll_gap | 3 | 5.1069e-05 | 9.27683e-05 | {"17": 0.00015815062040872032, "29": -4.94361460767756e-06, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters only | 0 | uci_internal_fixed | brier_gap | 3 | 1.31883e-05 | 2.37452e-05 | {"17": 4.060029987073936e-05, "29": -1.035518472081165e-06, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters only | 0 | uci_internal_fixed | first_batch_max_logit_diff | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters only | 4 | uci_internal_fixed | disagreement | 3 | 0.000325521 | 0.000563819 | {"17": 0.0009765625, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters only | 4 | uci_internal_fixed | accuracy_ab | 3 | 0.861328 | 0.0182437 | {"17": 0.8583984375, "29": 0.8447265625, "43": 0.880859375} |
| SAR (complete-state implementation) | Reset parameters only | 4 | uci_internal_fixed | accuracy_ba | 3 | 0.861654 | 0.0181739 | {"17": 0.859375, "29": 0.8447265625, "43": 0.880859375} |
| SAR (complete-state implementation) | Reset parameters only | 4 | uci_internal_fixed | signed_error_gap | 3 | 0.000325521 | 0.000563819 | {"17": 0.0009765625, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters only | 4 | uci_internal_fixed | absolute_error_gap | 3 | 0.000325521 | 0.000563819 | {"17": 0.0009765625, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters only | 4 | uci_internal_fixed | nll_gap | 3 | -2.92067e-05 | 5.05875e-05 | {"17": -8.762015332635e-05, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters only | 4 | uci_internal_fixed | brier_gap | 3 | -4.94772e-06 | 8.56971e-06 | {"17": -1.48431672402638e-05, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters only | 4 | uci_internal_fixed | first_batch_max_logit_diff | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | uci_internal_fixed | disagreement | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | uci_internal_fixed | accuracy_ab | 3 | 0.861654 | 0.0181739 | {"17": 0.859375, "29": 0.8447265625, "43": 0.880859375} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | uci_internal_fixed | accuracy_ba | 3 | 0.861654 | 0.0181739 | {"17": 0.859375, "29": 0.8447265625, "43": 0.880859375} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | uci_internal_fixed | signed_error_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | uci_internal_fixed | absolute_error_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | uci_internal_fixed | nll_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | uci_internal_fixed | brier_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | uci_internal_fixed | first_batch_max_logit_diff | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | uci_internal_fixed | disagreement | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | uci_internal_fixed | accuracy_ab | 3 | 0.861654 | 0.0181739 | {"17": 0.859375, "29": 0.8447265625, "43": 0.880859375} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | uci_internal_fixed | accuracy_ba | 3 | 0.861654 | 0.0181739 | {"17": 0.859375, "29": 0.8447265625, "43": 0.880859375} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | uci_internal_fixed | signed_error_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | uci_internal_fixed | absolute_error_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | uci_internal_fixed | nll_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | uci_internal_fixed | brier_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | uci_internal_fixed | first_batch_max_logit_diff | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | uci_internal_fixed | disagreement | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | uci_internal_fixed | accuracy_ab | 3 | 0.861328 | 0.0182437 | {"17": 0.8583984375, "29": 0.8447265625, "43": 0.880859375} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | uci_internal_fixed | accuracy_ba | 3 | 0.861328 | 0.0182437 | {"17": 0.8583984375, "29": 0.8447265625, "43": 0.880859375} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | uci_internal_fixed | signed_error_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | uci_internal_fixed | absolute_error_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | uci_internal_fixed | nll_gap | 3 | 5.10492e-05 | 9.27341e-05 | {"17": 0.00015809130229385237, "29": -4.94361460767756e-06, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | uci_internal_fixed | brier_gap | 3 | 1.31764e-05 | 2.37246e-05 | {"17": 4.0564658124471464e-05, "29": -1.035518472081165e-06, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | uci_internal_fixed | first_batch_max_logit_diff | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | uci_internal_fixed | disagreement | 3 | 0.000325521 | 0.000563819 | {"17": 0.0009765625, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | uci_internal_fixed | accuracy_ab | 3 | 0.861328 | 0.0182437 | {"17": 0.8583984375, "29": 0.8447265625, "43": 0.880859375} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | uci_internal_fixed | accuracy_ba | 3 | 0.861654 | 0.0181739 | {"17": 0.859375, "29": 0.8447265625, "43": 0.880859375} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | uci_internal_fixed | signed_error_gap | 3 | 0.000325521 | 0.000563819 | {"17": 0.0009765625, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | uci_internal_fixed | absolute_error_gap | 3 | 0.000325521 | 0.000563819 | {"17": 0.0009765625, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | uci_internal_fixed | nll_gap | 3 | -2.92067e-05 | 5.05875e-05 | {"17": -8.762015332635e-05, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | uci_internal_fixed | brier_gap | 3 | -4.94772e-06 | 8.56971e-06 | {"17": -1.48431672402638e-05, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | uci_internal_fixed | first_batch_max_logit_diff | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | uci_internal_fixed | disagreement | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | uci_internal_fixed | accuracy_ab | 3 | 0.861654 | 0.0181739 | {"17": 0.859375, "29": 0.8447265625, "43": 0.880859375} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | uci_internal_fixed | accuracy_ba | 3 | 0.861654 | 0.0181739 | {"17": 0.859375, "29": 0.8447265625, "43": 0.880859375} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | uci_internal_fixed | signed_error_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | uci_internal_fixed | absolute_error_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | uci_internal_fixed | nll_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | uci_internal_fixed | brier_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | uci_internal_fixed | first_batch_max_logit_diff | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | uci_internal_fixed | disagreement | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | uci_internal_fixed | accuracy_ab | 3 | 0.861654 | 0.0181739 | {"17": 0.859375, "29": 0.8447265625, "43": 0.880859375} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | uci_internal_fixed | accuracy_ba | 3 | 0.861654 | 0.0181739 | {"17": 0.859375, "29": 0.8447265625, "43": 0.880859375} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | uci_internal_fixed | signed_error_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | uci_internal_fixed | absolute_error_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | uci_internal_fixed | nll_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | uci_internal_fixed | brier_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | uci_internal_fixed | first_batch_max_logit_diff | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Source | Reset all declared state | 0 | uci_internal_fixed | disagreement | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Source | Reset all declared state | 0 | uci_internal_fixed | accuracy_ab | 3 | 0.814128 | 0.0734719 | {"17": 0.8681640625, "29": 0.84375, "43": 0.73046875} |
| Source | Reset all declared state | 0 | uci_internal_fixed | accuracy_ba | 3 | 0.814128 | 0.0734719 | {"17": 0.8681640625, "29": 0.84375, "43": 0.73046875} |
| Source | Reset all declared state | 0 | uci_internal_fixed | signed_error_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Source | Reset all declared state | 0 | uci_internal_fixed | absolute_error_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Source | Reset all declared state | 0 | uci_internal_fixed | nll_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Source | Reset all declared state | 0 | uci_internal_fixed | brier_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Source | Reset all declared state | 0 | uci_internal_fixed | first_batch_max_logit_diff | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Source | Reset all declared state | 4 | uci_internal_fixed | disagreement | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Source | Reset all declared state | 4 | uci_internal_fixed | accuracy_ab | 3 | 0.814128 | 0.0734719 | {"17": 0.8681640625, "29": 0.84375, "43": 0.73046875} |
| Source | Reset all declared state | 4 | uci_internal_fixed | accuracy_ba | 3 | 0.814128 | 0.0734719 | {"17": 0.8681640625, "29": 0.84375, "43": 0.73046875} |
| Source | Reset all declared state | 4 | uci_internal_fixed | signed_error_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Source | Reset all declared state | 4 | uci_internal_fixed | absolute_error_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Source | Reset all declared state | 4 | uci_internal_fixed | nll_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Source | Reset all declared state | 4 | uci_internal_fixed | brier_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Source | Reset all declared state | 4 | uci_internal_fixed | first_batch_max_logit_diff | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Source | No external reset | 0 | uci_internal_fixed | disagreement | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Source | No external reset | 0 | uci_internal_fixed | accuracy_ab | 3 | 0.814128 | 0.0734719 | {"17": 0.8681640625, "29": 0.84375, "43": 0.73046875} |
| Source | No external reset | 0 | uci_internal_fixed | accuracy_ba | 3 | 0.814128 | 0.0734719 | {"17": 0.8681640625, "29": 0.84375, "43": 0.73046875} |
| Source | No external reset | 0 | uci_internal_fixed | signed_error_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Source | No external reset | 0 | uci_internal_fixed | absolute_error_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Source | No external reset | 0 | uci_internal_fixed | nll_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Source | No external reset | 0 | uci_internal_fixed | brier_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Source | No external reset | 0 | uci_internal_fixed | first_batch_max_logit_diff | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Source | No external reset | 4 | uci_internal_fixed | disagreement | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Source | No external reset | 4 | uci_internal_fixed | accuracy_ab | 3 | 0.814128 | 0.0734719 | {"17": 0.8681640625, "29": 0.84375, "43": 0.73046875} |
| Source | No external reset | 4 | uci_internal_fixed | accuracy_ba | 3 | 0.814128 | 0.0734719 | {"17": 0.8681640625, "29": 0.84375, "43": 0.73046875} |
| Source | No external reset | 4 | uci_internal_fixed | signed_error_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Source | No external reset | 4 | uci_internal_fixed | absolute_error_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Source | No external reset | 4 | uci_internal_fixed | nll_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Source | No external reset | 4 | uci_internal_fixed | brier_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Source | No external reset | 4 | uci_internal_fixed | first_batch_max_logit_diff | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset all declared state | 0 | uci_internal_fixed | disagreement | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset all declared state | 0 | uci_internal_fixed | accuracy_ab | 3 | 0.861654 | 0.0181739 | {"17": 0.859375, "29": 0.8447265625, "43": 0.880859375} |
| Tent | Reset all declared state | 0 | uci_internal_fixed | accuracy_ba | 3 | 0.861654 | 0.0181739 | {"17": 0.859375, "29": 0.8447265625, "43": 0.880859375} |
| Tent | Reset all declared state | 0 | uci_internal_fixed | signed_error_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset all declared state | 0 | uci_internal_fixed | absolute_error_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset all declared state | 0 | uci_internal_fixed | nll_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset all declared state | 0 | uci_internal_fixed | brier_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset all declared state | 0 | uci_internal_fixed | first_batch_max_logit_diff | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset all declared state | 4 | uci_internal_fixed | disagreement | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset all declared state | 4 | uci_internal_fixed | accuracy_ab | 3 | 0.861654 | 0.0181739 | {"17": 0.859375, "29": 0.8447265625, "43": 0.880859375} |
| Tent | Reset all declared state | 4 | uci_internal_fixed | accuracy_ba | 3 | 0.861654 | 0.0181739 | {"17": 0.859375, "29": 0.8447265625, "43": 0.880859375} |
| Tent | Reset all declared state | 4 | uci_internal_fixed | signed_error_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset all declared state | 4 | uci_internal_fixed | absolute_error_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset all declared state | 4 | uci_internal_fixed | nll_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset all declared state | 4 | uci_internal_fixed | brier_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset all declared state | 4 | uci_internal_fixed | first_batch_max_logit_diff | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset auxiliary state only | 0 | uci_internal_fixed | disagreement | 3 | 0.000325521 | 0.000563819 | {"17": 0.0009765625, "29": 0.0, "43": 0.0} |
| Tent | Reset auxiliary state only | 0 | uci_internal_fixed | accuracy_ab | 3 | 0.861979 | 0.0181213 | {"17": 0.8603515625, "29": 0.8447265625, "43": 0.880859375} |
| Tent | Reset auxiliary state only | 0 | uci_internal_fixed | accuracy_ba | 3 | 0.861654 | 0.0181739 | {"17": 0.859375, "29": 0.8447265625, "43": 0.880859375} |
| Tent | Reset auxiliary state only | 0 | uci_internal_fixed | signed_error_gap | 3 | -0.000325521 | 0.000563819 | {"17": -0.0009765625, "29": 0.0, "43": 0.0} |
| Tent | Reset auxiliary state only | 0 | uci_internal_fixed | absolute_error_gap | 3 | 0.000325521 | 0.000563819 | {"17": 0.0009765625, "29": 0.0, "43": 0.0} |
| Tent | Reset auxiliary state only | 0 | uci_internal_fixed | nll_gap | 3 | 2.61611e-05 | 5.37812e-05 | {"17": -2.2949739964178012e-05, "29": 1.7799686981245094e-05, "43": 8.363321520383433e-05} |
| Tent | Reset auxiliary state only | 0 | uci_internal_fixed | brier_gap | 3 | 2.23542e-06 | 1.90805e-05 | {"17": -1.3939091297097623e-05, "29": -2.633228041880667e-06, "43": 2.3278565454986494e-05} |
| Tent | Reset auxiliary state only | 0 | uci_internal_fixed | first_batch_max_logit_diff | 3 | 0.00903153 | 0.00173838 | {"17": 0.007641315460205, "29": 0.010980606079101549, "43": 0.0084726810455322} |
| Tent | Reset auxiliary state only | 4 | uci_internal_fixed | disagreement | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset auxiliary state only | 4 | uci_internal_fixed | accuracy_ab | 3 | 0.862305 | 0.0180862 | {"17": 0.861328125, "29": 0.8447265625, "43": 0.880859375} |
| Tent | Reset auxiliary state only | 4 | uci_internal_fixed | accuracy_ba | 3 | 0.862305 | 0.0180862 | {"17": 0.861328125, "29": 0.8447265625, "43": 0.880859375} |
| Tent | Reset auxiliary state only | 4 | uci_internal_fixed | signed_error_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset auxiliary state only | 4 | uci_internal_fixed | absolute_error_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset auxiliary state only | 4 | uci_internal_fixed | nll_gap | 3 | 1.7286e-05 | 3.57076e-05 | {"17": -1.6961185307570736e-05, "29": 1.452539129353711e-05, "43": 5.429369370337976e-05} |
| Tent | Reset auxiliary state only | 4 | uci_internal_fixed | brier_gap | 3 | 1.58798e-06 | 1.24235e-05 | {"17": -9.55651940180366e-06, "29": -6.623748391408613e-07, "43": 1.4982836645178674e-05} |
| Tent | Reset auxiliary state only | 4 | uci_internal_fixed | first_batch_max_logit_diff | 3 | 0.00592633 | 0.00116192 | {"17": 0.0050022602081298, "29": 0.00723075866699215, "43": 0.005545973777770949} |
| Tent | No external reset | 0 | uci_internal_fixed | disagreement | 3 | 0.000325521 | 0.000563819 | {"17": 0.0009765625, "29": 0.0, "43": 0.0} |
| Tent | No external reset | 0 | uci_internal_fixed | accuracy_ab | 3 | 0.861979 | 0.0181213 | {"17": 0.8603515625, "29": 0.8447265625, "43": 0.880859375} |
| Tent | No external reset | 0 | uci_internal_fixed | accuracy_ba | 3 | 0.861654 | 0.0181739 | {"17": 0.859375, "29": 0.8447265625, "43": 0.880859375} |
| Tent | No external reset | 0 | uci_internal_fixed | signed_error_gap | 3 | -0.000325521 | 0.000563819 | {"17": -0.0009765625, "29": 0.0, "43": 0.0} |
| Tent | No external reset | 0 | uci_internal_fixed | absolute_error_gap | 3 | 0.000325521 | 0.000563819 | {"17": 0.0009765625, "29": 0.0, "43": 0.0} |
| Tent | No external reset | 0 | uci_internal_fixed | nll_gap | 3 | 2.61611e-05 | 5.37812e-05 | {"17": -2.2949739964178012e-05, "29": 1.7799686981245094e-05, "43": 8.363321520383433e-05} |
| Tent | No external reset | 0 | uci_internal_fixed | brier_gap | 3 | 2.23542e-06 | 1.90805e-05 | {"17": -1.3939091297097623e-05, "29": -2.633228041880667e-06, "43": 2.3278565454986494e-05} |
| Tent | No external reset | 0 | uci_internal_fixed | first_batch_max_logit_diff | 3 | 0.00903153 | 0.00173838 | {"17": 0.007641315460205, "29": 0.010980606079101549, "43": 0.0084726810455322} |
| Tent | No external reset | 4 | uci_internal_fixed | disagreement | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | No external reset | 4 | uci_internal_fixed | accuracy_ab | 3 | 0.862305 | 0.0180862 | {"17": 0.861328125, "29": 0.8447265625, "43": 0.880859375} |
| Tent | No external reset | 4 | uci_internal_fixed | accuracy_ba | 3 | 0.862305 | 0.0180862 | {"17": 0.861328125, "29": 0.8447265625, "43": 0.880859375} |
| Tent | No external reset | 4 | uci_internal_fixed | signed_error_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | No external reset | 4 | uci_internal_fixed | absolute_error_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | No external reset | 4 | uci_internal_fixed | nll_gap | 3 | 1.7286e-05 | 3.57076e-05 | {"17": -1.6961185307570736e-05, "29": 1.452539129353711e-05, "43": 5.429369370337976e-05} |
| Tent | No external reset | 4 | uci_internal_fixed | brier_gap | 3 | 1.58798e-06 | 1.24235e-05 | {"17": -9.55651940180366e-06, "29": -6.623748391408613e-07, "43": 1.4982836645178674e-05} |
| Tent | No external reset | 4 | uci_internal_fixed | first_batch_max_logit_diff | 3 | 0.00592633 | 0.00116192 | {"17": 0.0050022602081298, "29": 0.00723075866699215, "43": 0.005545973777770949} |
| Tent | Reset optimizer only | 0 | uci_internal_fixed | disagreement | 3 | 0.000325521 | 0.000563819 | {"17": 0.0009765625, "29": 0.0, "43": 0.0} |
| Tent | Reset optimizer only | 0 | uci_internal_fixed | accuracy_ab | 3 | 0.861979 | 0.0181213 | {"17": 0.8603515625, "29": 0.8447265625, "43": 0.880859375} |
| Tent | Reset optimizer only | 0 | uci_internal_fixed | accuracy_ba | 3 | 0.861654 | 0.0181739 | {"17": 0.859375, "29": 0.8447265625, "43": 0.880859375} |
| Tent | Reset optimizer only | 0 | uci_internal_fixed | signed_error_gap | 3 | -0.000325521 | 0.000563819 | {"17": -0.0009765625, "29": 0.0, "43": 0.0} |
| Tent | Reset optimizer only | 0 | uci_internal_fixed | absolute_error_gap | 3 | 0.000325521 | 0.000563819 | {"17": 0.0009765625, "29": 0.0, "43": 0.0} |
| Tent | Reset optimizer only | 0 | uci_internal_fixed | nll_gap | 3 | 6.28539e-05 | 0.000118324 | {"17": -3.9568284936772335e-05, "29": 3.575313481859674e-05, "43": 0.00019237670867712514} |
| Tent | Reset optimizer only | 0 | uci_internal_fixed | brier_gap | 3 | 4.59213e-06 | 3.71559e-05 | {"17": -2.7743242864652212e-05, "29": -3.6610564236299447e-06, "43": 4.518068828910021e-05} |
| Tent | Reset optimizer only | 0 | uci_internal_fixed | first_batch_max_logit_diff | 3 | 0.00903153 | 0.00173838 | {"17": 0.007641315460205, "29": 0.010980606079101549, "43": 0.0084726810455322} |
| Tent | Reset optimizer only | 4 | uci_internal_fixed | disagreement | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset optimizer only | 4 | uci_internal_fixed | accuracy_ab | 3 | 0.862305 | 0.0180862 | {"17": 0.861328125, "29": 0.8447265625, "43": 0.880859375} |
| Tent | Reset optimizer only | 4 | uci_internal_fixed | accuracy_ba | 3 | 0.862305 | 0.0180862 | {"17": 0.861328125, "29": 0.8447265625, "43": 0.880859375} |
| Tent | Reset optimizer only | 4 | uci_internal_fixed | signed_error_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset optimizer only | 4 | uci_internal_fixed | absolute_error_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset optimizer only | 4 | uci_internal_fixed | nll_gap | 3 | 4.17469e-05 | 7.79505e-05 | {"17": -2.57843377544989e-05, "29": 2.397684046474835e-05, "43": 0.00012704829872721096} |
| Tent | Reset optimizer only | 4 | uci_internal_fixed | brier_gap | 3 | 3.30081e-06 | 2.43957e-05 | {"17": -1.800580725420768e-05, "29": -2.0042984909679493e-06, "43": 2.9912522608413136e-05} |
| Tent | Reset optimizer only | 4 | uci_internal_fixed | first_batch_max_logit_diff | 3 | 0.00592633 | 0.00116192 | {"17": 0.0050022602081298, "29": 0.00723075866699215, "43": 0.005545973777770949} |
| Tent | Reset optimizer + auxiliary state | 0 | uci_internal_fixed | disagreement | 3 | 0.000325521 | 0.000563819 | {"17": 0.0009765625, "29": 0.0, "43": 0.0} |
| Tent | Reset optimizer + auxiliary state | 0 | uci_internal_fixed | accuracy_ab | 3 | 0.861979 | 0.0181213 | {"17": 0.8603515625, "29": 0.8447265625, "43": 0.880859375} |
| Tent | Reset optimizer + auxiliary state | 0 | uci_internal_fixed | accuracy_ba | 3 | 0.861654 | 0.0181739 | {"17": 0.859375, "29": 0.8447265625, "43": 0.880859375} |
| Tent | Reset optimizer + auxiliary state | 0 | uci_internal_fixed | signed_error_gap | 3 | -0.000325521 | 0.000563819 | {"17": -0.0009765625, "29": 0.0, "43": 0.0} |
| Tent | Reset optimizer + auxiliary state | 0 | uci_internal_fixed | absolute_error_gap | 3 | 0.000325521 | 0.000563819 | {"17": 0.0009765625, "29": 0.0, "43": 0.0} |
| Tent | Reset optimizer + auxiliary state | 0 | uci_internal_fixed | nll_gap | 3 | 6.28539e-05 | 0.000118324 | {"17": -3.9568284936772335e-05, "29": 3.575313481859674e-05, "43": 0.00019237670867712514} |
| Tent | Reset optimizer + auxiliary state | 0 | uci_internal_fixed | brier_gap | 3 | 4.59213e-06 | 3.71559e-05 | {"17": -2.7743242864652212e-05, "29": -3.6610564236299447e-06, "43": 4.518068828910021e-05} |
| Tent | Reset optimizer + auxiliary state | 0 | uci_internal_fixed | first_batch_max_logit_diff | 3 | 0.00903153 | 0.00173838 | {"17": 0.007641315460205, "29": 0.010980606079101549, "43": 0.0084726810455322} |
| Tent | Reset optimizer + auxiliary state | 4 | uci_internal_fixed | disagreement | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset optimizer + auxiliary state | 4 | uci_internal_fixed | accuracy_ab | 3 | 0.862305 | 0.0180862 | {"17": 0.861328125, "29": 0.8447265625, "43": 0.880859375} |
| Tent | Reset optimizer + auxiliary state | 4 | uci_internal_fixed | accuracy_ba | 3 | 0.862305 | 0.0180862 | {"17": 0.861328125, "29": 0.8447265625, "43": 0.880859375} |
| Tent | Reset optimizer + auxiliary state | 4 | uci_internal_fixed | signed_error_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset optimizer + auxiliary state | 4 | uci_internal_fixed | absolute_error_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset optimizer + auxiliary state | 4 | uci_internal_fixed | nll_gap | 3 | 4.17469e-05 | 7.79505e-05 | {"17": -2.57843377544989e-05, "29": 2.397684046474835e-05, "43": 0.00012704829872721096} |
| Tent | Reset optimizer + auxiliary state | 4 | uci_internal_fixed | brier_gap | 3 | 3.30081e-06 | 2.43957e-05 | {"17": -1.800580725420768e-05, "29": -2.0042984909679493e-06, "43": 2.9912522608413136e-05} |
| Tent | Reset optimizer + auxiliary state | 4 | uci_internal_fixed | first_batch_max_logit_diff | 3 | 0.00592633 | 0.00116192 | {"17": 0.0050022602081298, "29": 0.00723075866699215, "43": 0.005545973777770949} |
| Tent | Reset parameters only | 0 | uci_internal_fixed | disagreement | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters only | 0 | uci_internal_fixed | accuracy_ab | 3 | 0.861654 | 0.0181739 | {"17": 0.859375, "29": 0.8447265625, "43": 0.880859375} |
| Tent | Reset parameters only | 0 | uci_internal_fixed | accuracy_ba | 3 | 0.861654 | 0.0181739 | {"17": 0.859375, "29": 0.8447265625, "43": 0.880859375} |
| Tent | Reset parameters only | 0 | uci_internal_fixed | signed_error_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters only | 0 | uci_internal_fixed | absolute_error_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters only | 0 | uci_internal_fixed | nll_gap | 3 | -3.66149e-05 | 6.30309e-05 | {"17": 1.3484938090006088e-05, "29": -1.5943871696944695e-05, "43": -0.00010738566674893292} |
| Tent | Reset parameters only | 0 | uci_internal_fixed | brier_gap | 3 | -2.34558e-06 | 1.74687e-05 | {"17": 1.2942197803490763e-05, "29": 1.4065828303679731e-06, "43": -2.1385526391769216e-05} |
| Tent | Reset parameters only | 0 | uci_internal_fixed | first_batch_max_logit_diff | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters only | 4 | uci_internal_fixed | disagreement | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters only | 4 | uci_internal_fixed | accuracy_ab | 3 | 0.861654 | 0.0181739 | {"17": 0.859375, "29": 0.8447265625, "43": 0.880859375} |
| Tent | Reset parameters only | 4 | uci_internal_fixed | accuracy_ba | 3 | 0.861654 | 0.0181739 | {"17": 0.859375, "29": 0.8447265625, "43": 0.880859375} |
| Tent | Reset parameters only | 4 | uci_internal_fixed | signed_error_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters only | 4 | uci_internal_fixed | absolute_error_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters only | 4 | uci_internal_fixed | nll_gap | 3 | -2.37046e-05 | 4.23065e-05 | {"17": 8.050189924457135e-06, "29": -7.432785928698782e-06, "43": -7.17310953467839e-05} |
| Tent | Reset parameters only | 4 | uci_internal_fixed | brier_gap | 3 | -1.38028e-06 | 1.17904e-05 | {"17": 8.352170139992038e-06, "29": 1.9980773558400666e-06, "43": -1.449108461071269e-05} |
| Tent | Reset parameters only | 4 | uci_internal_fixed | first_batch_max_logit_diff | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + auxiliary state | 0 | uci_internal_fixed | disagreement | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + auxiliary state | 0 | uci_internal_fixed | accuracy_ab | 3 | 0.861654 | 0.0181739 | {"17": 0.859375, "29": 0.8447265625, "43": 0.880859375} |
| Tent | Reset parameters + auxiliary state | 0 | uci_internal_fixed | accuracy_ba | 3 | 0.861654 | 0.0181739 | {"17": 0.859375, "29": 0.8447265625, "43": 0.880859375} |
| Tent | Reset parameters + auxiliary state | 0 | uci_internal_fixed | signed_error_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + auxiliary state | 0 | uci_internal_fixed | absolute_error_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + auxiliary state | 0 | uci_internal_fixed | nll_gap | 3 | -3.66149e-05 | 6.30309e-05 | {"17": 1.3484938090006088e-05, "29": -1.5943871696944695e-05, "43": -0.00010738566674893292} |
| Tent | Reset parameters + auxiliary state | 0 | uci_internal_fixed | brier_gap | 3 | -2.34558e-06 | 1.74687e-05 | {"17": 1.2942197803490763e-05, "29": 1.4065828303679731e-06, "43": -2.1385526391769216e-05} |
| Tent | Reset parameters + auxiliary state | 0 | uci_internal_fixed | first_batch_max_logit_diff | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + auxiliary state | 4 | uci_internal_fixed | disagreement | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + auxiliary state | 4 | uci_internal_fixed | accuracy_ab | 3 | 0.861654 | 0.0181739 | {"17": 0.859375, "29": 0.8447265625, "43": 0.880859375} |
| Tent | Reset parameters + auxiliary state | 4 | uci_internal_fixed | accuracy_ba | 3 | 0.861654 | 0.0181739 | {"17": 0.859375, "29": 0.8447265625, "43": 0.880859375} |
| Tent | Reset parameters + auxiliary state | 4 | uci_internal_fixed | signed_error_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + auxiliary state | 4 | uci_internal_fixed | absolute_error_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + auxiliary state | 4 | uci_internal_fixed | nll_gap | 3 | -2.37046e-05 | 4.23065e-05 | {"17": 8.050189924457135e-06, "29": -7.432785928698782e-06, "43": -7.17310953467839e-05} |
| Tent | Reset parameters + auxiliary state | 4 | uci_internal_fixed | brier_gap | 3 | -1.38028e-06 | 1.17904e-05 | {"17": 8.352170139992038e-06, "29": 1.9980773558400666e-06, "43": -1.449108461071269e-05} |
| Tent | Reset parameters + auxiliary state | 4 | uci_internal_fixed | first_batch_max_logit_diff | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + optimizer | 0 | uci_internal_fixed | disagreement | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + optimizer | 0 | uci_internal_fixed | accuracy_ab | 3 | 0.861654 | 0.0181739 | {"17": 0.859375, "29": 0.8447265625, "43": 0.880859375} |
| Tent | Reset parameters + optimizer | 0 | uci_internal_fixed | accuracy_ba | 3 | 0.861654 | 0.0181739 | {"17": 0.859375, "29": 0.8447265625, "43": 0.880859375} |
| Tent | Reset parameters + optimizer | 0 | uci_internal_fixed | signed_error_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + optimizer | 0 | uci_internal_fixed | absolute_error_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + optimizer | 0 | uci_internal_fixed | nll_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + optimizer | 0 | uci_internal_fixed | brier_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + optimizer | 0 | uci_internal_fixed | first_batch_max_logit_diff | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + optimizer | 4 | uci_internal_fixed | disagreement | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + optimizer | 4 | uci_internal_fixed | accuracy_ab | 3 | 0.861654 | 0.0181739 | {"17": 0.859375, "29": 0.8447265625, "43": 0.880859375} |
| Tent | Reset parameters + optimizer | 4 | uci_internal_fixed | accuracy_ba | 3 | 0.861654 | 0.0181739 | {"17": 0.859375, "29": 0.8447265625, "43": 0.880859375} |
| Tent | Reset parameters + optimizer | 4 | uci_internal_fixed | signed_error_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + optimizer | 4 | uci_internal_fixed | absolute_error_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + optimizer | 4 | uci_internal_fixed | nll_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + optimizer | 4 | uci_internal_fixed | brier_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + optimizer | 4 | uci_internal_fixed | first_batch_max_logit_diff | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | uci_internal_fixed | disagreement | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | uci_internal_fixed | accuracy_ab | 3 | 0.861654 | 0.0181739 | {"17": 0.859375, "29": 0.8447265625, "43": 0.880859375} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | uci_internal_fixed | accuracy_ba | 3 | 0.861654 | 0.0181739 | {"17": 0.859375, "29": 0.8447265625, "43": 0.880859375} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | uci_internal_fixed | signed_error_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | uci_internal_fixed | absolute_error_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | uci_internal_fixed | nll_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | uci_internal_fixed | brier_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | uci_internal_fixed | first_batch_max_logit_diff | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | uci_internal_fixed | disagreement | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | uci_internal_fixed | accuracy_ab | 3 | 0.861654 | 0.0181739 | {"17": 0.859375, "29": 0.8447265625, "43": 0.880859375} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | uci_internal_fixed | accuracy_ba | 3 | 0.861654 | 0.0181739 | {"17": 0.859375, "29": 0.8447265625, "43": 0.880859375} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | uci_internal_fixed | signed_error_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | uci_internal_fixed | absolute_error_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | uci_internal_fixed | nll_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | uci_internal_fixed | brier_gap | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | uci_internal_fixed | first_batch_max_logit_diff | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |


## runs

| method | intervention | washout_batches | direction | metric | n_panels | mean | sd | ci95_low | ci95_high | n_seeds_min | n_seeds_max | individual_panels |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Normalization only | Reset all declared state | 0 | ab | accuracy | 1 | 0.861328 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.861328125} |
| Normalization only | Reset all declared state | 0 | ab | nll | 1 | 0.513794 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.51379354555466} |
| Normalization only | Reset all declared state | 0 | ab | brier | 1 | 0.21413 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.21413016188688805} |
| Normalization only | Reset all declared state | 0 | ab | ece15 | 1 | 0.0792477 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.07924768291116553} |
| Normalization only | Reset all declared state | 0 | ab | seconds | 1 | 0.0594806 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.059480566664812266} |
| Normalization only | Reset all declared state | 0 | ab | updates | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Normalization only | Reset all declared state | 0 | ab | skipped | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Normalization only | Reset all declared state | 0 | ab | recoveries | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Normalization only | Reset all declared state | 0 | ba | accuracy | 1 | 0.861328 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.861328125} |
| Normalization only | Reset all declared state | 0 | ba | nll | 1 | 0.513794 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.51379354555466} |
| Normalization only | Reset all declared state | 0 | ba | brier | 1 | 0.21413 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.21413016188688805} |
| Normalization only | Reset all declared state | 0 | ba | ece15 | 1 | 0.0792477 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.07924768291116553} |
| Normalization only | Reset all declared state | 0 | ba | seconds | 1 | 0.0586038 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.05860381666813428} |
| Normalization only | Reset all declared state | 0 | ba | updates | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Normalization only | Reset all declared state | 0 | ba | skipped | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Normalization only | Reset all declared state | 0 | ba | recoveries | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Normalization only | Reset all declared state | 4 | ab | accuracy | 1 | 0.861328 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.861328125} |
| Normalization only | Reset all declared state | 4 | ab | nll | 1 | 0.513794 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.51379354555466} |
| Normalization only | Reset all declared state | 4 | ab | brier | 1 | 0.21413 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.21413016188688805} |
| Normalization only | Reset all declared state | 4 | ab | ece15 | 1 | 0.0792477 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.07924768291116553} |
| Normalization only | Reset all declared state | 4 | ab | seconds | 1 | 0.0636672 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.06366720000126706} |
| Normalization only | Reset all declared state | 4 | ab | updates | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Normalization only | Reset all declared state | 4 | ab | skipped | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Normalization only | Reset all declared state | 4 | ab | recoveries | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Normalization only | Reset all declared state | 4 | ba | accuracy | 1 | 0.861328 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.861328125} |
| Normalization only | Reset all declared state | 4 | ba | nll | 1 | 0.513794 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.51379354555466} |
| Normalization only | Reset all declared state | 4 | ba | brier | 1 | 0.21413 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.21413016188688805} |
| Normalization only | Reset all declared state | 4 | ba | ece15 | 1 | 0.0792477 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.07924768291116553} |
| Normalization only | Reset all declared state | 4 | ba | seconds | 1 | 0.06602 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.06602003333440125} |
| Normalization only | Reset all declared state | 4 | ba | updates | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Normalization only | Reset all declared state | 4 | ba | skipped | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Normalization only | Reset all declared state | 4 | ba | recoveries | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Normalization only | No external reset | 0 | ab | accuracy | 1 | 0.861328 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.861328125} |
| Normalization only | No external reset | 0 | ab | nll | 1 | 0.513794 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.51379354555466} |
| Normalization only | No external reset | 0 | ab | brier | 1 | 0.21413 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.21413016188688805} |
| Normalization only | No external reset | 0 | ab | ece15 | 1 | 0.0792477 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.07924768291116553} |
| Normalization only | No external reset | 0 | ab | seconds | 1 | 0.0609484 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.06094839999665657} |
| Normalization only | No external reset | 0 | ab | updates | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Normalization only | No external reset | 0 | ab | skipped | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Normalization only | No external reset | 0 | ab | recoveries | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Normalization only | No external reset | 0 | ba | accuracy | 1 | 0.861328 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.861328125} |
| Normalization only | No external reset | 0 | ba | nll | 1 | 0.513794 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.51379354555466} |
| Normalization only | No external reset | 0 | ba | brier | 1 | 0.21413 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.21413016188688805} |
| Normalization only | No external reset | 0 | ba | ece15 | 1 | 0.0792477 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.07924768291116553} |
| Normalization only | No external reset | 0 | ba | seconds | 1 | 0.0607845 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.06078448333573757} |
| Normalization only | No external reset | 0 | ba | updates | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Normalization only | No external reset | 0 | ba | skipped | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Normalization only | No external reset | 0 | ba | recoveries | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Normalization only | No external reset | 4 | ab | accuracy | 1 | 0.861328 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.861328125} |
| Normalization only | No external reset | 4 | ab | nll | 1 | 0.513794 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.51379354555466} |
| Normalization only | No external reset | 4 | ab | brier | 1 | 0.21413 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.21413016188688805} |
| Normalization only | No external reset | 4 | ab | ece15 | 1 | 0.0792477 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.07924768291116553} |
| Normalization only | No external reset | 4 | ab | seconds | 1 | 0.0606167 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.060616650000156314} |
| Normalization only | No external reset | 4 | ab | updates | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Normalization only | No external reset | 4 | ab | skipped | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Normalization only | No external reset | 4 | ab | recoveries | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Normalization only | No external reset | 4 | ba | accuracy | 1 | 0.861328 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.861328125} |
| Normalization only | No external reset | 4 | ba | nll | 1 | 0.513794 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.51379354555466} |
| Normalization only | No external reset | 4 | ba | brier | 1 | 0.21413 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.21413016188688805} |
| Normalization only | No external reset | 4 | ba | ece15 | 1 | 0.0792477 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.07924768291116553} |
| Normalization only | No external reset | 4 | ba | seconds | 1 | 0.060981 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.060980983328287615} |
| Normalization only | No external reset | 4 | ba | updates | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Normalization only | No external reset | 4 | ba | skipped | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Normalization only | No external reset | 4 | ba | recoveries | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset all declared state | 0 | ab | accuracy | 1 | 0.861654 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8616536458333334} |
| SAR (complete-state implementation) | Reset all declared state | 0 | ab | nll | 1 | 0.513692 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.5136921476014341} |
| SAR (complete-state implementation) | Reset all declared state | 0 | ab | brier | 1 | 0.214038 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.21403785842504322} |
| SAR (complete-state implementation) | Reset all declared state | 0 | ab | ece15 | 1 | 0.0789817 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.07898169428309054} |
| SAR (complete-state implementation) | Reset all declared state | 0 | ab | seconds | 1 | 0.22183 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.2218297833339117} |
| SAR (complete-state implementation) | Reset all declared state | 0 | ab | updates | 1 | 16 | — | — | — | 3 | 3 | {"uci_internal_fixed": 16.0} |
| SAR (complete-state implementation) | Reset all declared state | 0 | ab | skipped | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset all declared state | 0 | ab | recoveries | 1 | 8.5 | — | — | — | 3 | 3 | {"uci_internal_fixed": 8.5} |
| SAR (complete-state implementation) | Reset all declared state | 0 | ba | accuracy | 1 | 0.861654 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8616536458333334} |
| SAR (complete-state implementation) | Reset all declared state | 0 | ba | nll | 1 | 0.513692 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.5136921476014341} |
| SAR (complete-state implementation) | Reset all declared state | 0 | ba | brier | 1 | 0.214038 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.21403785842504322} |
| SAR (complete-state implementation) | Reset all declared state | 0 | ba | ece15 | 1 | 0.0789817 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.07898169428309054} |
| SAR (complete-state implementation) | Reset all declared state | 0 | ba | seconds | 1 | 0.219881 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.21988063333265015} |
| SAR (complete-state implementation) | Reset all declared state | 0 | ba | updates | 1 | 16 | — | — | — | 3 | 3 | {"uci_internal_fixed": 16.0} |
| SAR (complete-state implementation) | Reset all declared state | 0 | ba | skipped | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset all declared state | 0 | ba | recoveries | 1 | 8.5 | — | — | — | 3 | 3 | {"uci_internal_fixed": 8.5} |
| SAR (complete-state implementation) | Reset all declared state | 4 | ab | accuracy | 1 | 0.861654 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8616536458333334} |
| SAR (complete-state implementation) | Reset all declared state | 4 | ab | nll | 1 | 0.513692 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.5136921476014341} |
| SAR (complete-state implementation) | Reset all declared state | 4 | ab | brier | 1 | 0.214038 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.21403785842504322} |
| SAR (complete-state implementation) | Reset all declared state | 4 | ab | ece15 | 1 | 0.0789817 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.07898169428309054} |
| SAR (complete-state implementation) | Reset all declared state | 4 | ab | seconds | 1 | 0.20738 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.207379633335222} |
| SAR (complete-state implementation) | Reset all declared state | 4 | ab | updates | 1 | 16 | — | — | — | 3 | 3 | {"uci_internal_fixed": 16.0} |
| SAR (complete-state implementation) | Reset all declared state | 4 | ab | skipped | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset all declared state | 4 | ab | recoveries | 1 | 8.5 | — | — | — | 3 | 3 | {"uci_internal_fixed": 8.5} |
| SAR (complete-state implementation) | Reset all declared state | 4 | ba | accuracy | 1 | 0.861654 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8616536458333334} |
| SAR (complete-state implementation) | Reset all declared state | 4 | ba | nll | 1 | 0.513692 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.5136921476014341} |
| SAR (complete-state implementation) | Reset all declared state | 4 | ba | brier | 1 | 0.214038 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.21403785842504322} |
| SAR (complete-state implementation) | Reset all declared state | 4 | ba | ece15 | 1 | 0.0789817 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.07898169428309054} |
| SAR (complete-state implementation) | Reset all declared state | 4 | ba | seconds | 1 | 0.199697 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.19969678333533614} |
| SAR (complete-state implementation) | Reset all declared state | 4 | ba | updates | 1 | 16 | — | — | — | 3 | 3 | {"uci_internal_fixed": 16.0} |
| SAR (complete-state implementation) | Reset all declared state | 4 | ba | skipped | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset all declared state | 4 | ba | recoveries | 1 | 8.5 | — | — | — | 3 | 3 | {"uci_internal_fixed": 8.5} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | ab | accuracy | 1 | 0.861654 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8616536458333334} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | ab | nll | 1 | 0.513691 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.5136911208914686} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | ab | brier | 1 | 0.214038 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.21403761550077616} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | ab | ece15 | 1 | 0.0789826 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.07898263321143657} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | ab | seconds | 1 | 0.28652 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.2865196000008533} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | ab | updates | 1 | 16 | — | — | — | 3 | 3 | {"uci_internal_fixed": 16.0} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | ab | skipped | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | ab | recoveries | 1 | 8.5 | — | — | — | 3 | 3 | {"uci_internal_fixed": 8.5} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | ba | accuracy | 1 | 0.861654 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8616536458333334} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | ba | nll | 1 | 0.513692 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.5136918991569656} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | ba | brier | 1 | 0.214038 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.21403775275629702} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | ba | ece15 | 1 | 0.0789819 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.07898188026443755} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | ba | seconds | 1 | 0.216309 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.21630903333182983} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | ba | updates | 1 | 16 | — | — | — | 3 | 3 | {"uci_internal_fixed": 16.0} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | ba | skipped | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | ba | recoveries | 1 | 8.5 | — | — | — | 3 | 3 | {"uci_internal_fixed": 8.5} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | ab | accuracy | 1 | 0.861654 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8616536458333334} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | ab | nll | 1 | 0.513692 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.5136921476014341} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | ab | brier | 1 | 0.214038 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.21403785842504322} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | ab | ece15 | 1 | 0.0789817 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.07898169428309054} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | ab | seconds | 1 | 0.208781 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.2087808000020838} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | ab | updates | 1 | 16 | — | — | — | 3 | 3 | {"uci_internal_fixed": 16.0} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | ab | skipped | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | ab | recoveries | 1 | 8.5 | — | — | — | 3 | 3 | {"uci_internal_fixed": 8.5} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | ba | accuracy | 1 | 0.861654 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8616536458333334} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | ba | nll | 1 | 0.513692 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.5136921476014341} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | ba | brier | 1 | 0.214038 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.21403785842504322} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | ba | ece15 | 1 | 0.0789817 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.07898169428309054} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | ba | seconds | 1 | 0.23173 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.23172958333210167} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | ba | updates | 1 | 16 | — | — | — | 3 | 3 | {"uci_internal_fixed": 16.0} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | ba | skipped | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | ba | recoveries | 1 | 8.5 | — | — | — | 3 | 3 | {"uci_internal_fixed": 8.5} |
| SAR (complete-state implementation) | No external reset | 0 | ab | accuracy | 1 | 0.861328 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.861328125} |
| SAR (complete-state implementation) | No external reset | 0 | ab | nll | 1 | 0.513886 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.5138863357021054} |
| SAR (complete-state implementation) | No external reset | 0 | ab | brier | 1 | 0.214144 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.21414417125556526} |
| SAR (complete-state implementation) | No external reset | 0 | ab | ece15 | 1 | 0.079253 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.07925299168666443} |
| SAR (complete-state implementation) | No external reset | 0 | ab | seconds | 1 | 0.200229 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.2002287333331575} |
| SAR (complete-state implementation) | No external reset | 0 | ab | updates | 1 | 16 | — | — | — | 3 | 3 | {"uci_internal_fixed": 16.0} |
| SAR (complete-state implementation) | No external reset | 0 | ab | skipped | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | No external reset | 0 | ab | recoveries | 1 | 12.8333 | — | — | — | 3 | 3 | {"uci_internal_fixed": 12.833333333333334} |
| SAR (complete-state implementation) | No external reset | 0 | ba | accuracy | 1 | 0.861328 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.861328125} |
| SAR (complete-state implementation) | No external reset | 0 | ba | nll | 1 | 0.513836 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.5138358542693372} |
| SAR (complete-state implementation) | No external reset | 0 | ba | brier | 1 | 0.214131 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.21413102141123852} |
| SAR (complete-state implementation) | No external reset | 0 | ba | ece15 | 1 | 0.0792531 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0792531270536798} |
| SAR (complete-state implementation) | No external reset | 0 | ba | seconds | 1 | 0.208672 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.20867161666925915} |
| SAR (complete-state implementation) | No external reset | 0 | ba | updates | 1 | 16 | — | — | — | 3 | 3 | {"uci_internal_fixed": 16.0} |
| SAR (complete-state implementation) | No external reset | 0 | ba | skipped | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | No external reset | 0 | ba | recoveries | 1 | 12.3333 | — | — | — | 3 | 3 | {"uci_internal_fixed": 12.333333333333334} |
| SAR (complete-state implementation) | No external reset | 4 | ab | accuracy | 1 | 0.861328 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.861328125} |
| SAR (complete-state implementation) | No external reset | 4 | ab | nll | 1 | 0.514106 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.5141057965680674} |
| SAR (complete-state implementation) | No external reset | 4 | ab | brier | 1 | 0.214172 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.21417164845120007} |
| SAR (complete-state implementation) | No external reset | 4 | ab | ece15 | 1 | 0.0792869 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.07928688614591352} |
| SAR (complete-state implementation) | No external reset | 4 | ab | seconds | 1 | 0.205495 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.20549475000249606} |
| SAR (complete-state implementation) | No external reset | 4 | ab | updates | 1 | 16 | — | — | — | 3 | 3 | {"uci_internal_fixed": 16.0} |
| SAR (complete-state implementation) | No external reset | 4 | ab | skipped | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | No external reset | 4 | ab | recoveries | 1 | 10.1667 | — | — | — | 3 | 3 | {"uci_internal_fixed": 10.166666666666666} |
| SAR (complete-state implementation) | No external reset | 4 | ba | accuracy | 1 | 0.861654 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8616536458333334} |
| SAR (complete-state implementation) | No external reset | 4 | ba | nll | 1 | 0.514135 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.5141350032858429} |
| SAR (complete-state implementation) | No external reset | 4 | ba | brier | 1 | 0.214177 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.2141765961736135} |
| SAR (complete-state implementation) | No external reset | 4 | ba | ece15 | 1 | 0.0789634 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.07896337537981624} |
| SAR (complete-state implementation) | No external reset | 4 | ba | seconds | 1 | 0.205179 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.20517908333325366} |
| SAR (complete-state implementation) | No external reset | 4 | ba | updates | 1 | 16 | — | — | — | 3 | 3 | {"uci_internal_fixed": 16.0} |
| SAR (complete-state implementation) | No external reset | 4 | ba | skipped | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | No external reset | 4 | ba | recoveries | 1 | 10 | — | — | — | 3 | 3 | {"uci_internal_fixed": 10.0} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | ab | accuracy | 1 | 0.861328 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.861328125} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | ab | nll | 1 | 0.513886 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.5138863386224921} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | ab | brier | 1 | 0.214144 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.21414417126145927} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | ab | ece15 | 1 | 0.079253 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.07925298877045095} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | ab | seconds | 1 | 0.225919 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.2259194000022641} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | ab | updates | 1 | 16 | — | — | — | 3 | 3 | {"uci_internal_fixed": 16.0} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | ab | skipped | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | ab | recoveries | 1 | 12.8333 | — | — | — | 3 | 3 | {"uci_internal_fixed": 12.833333333333334} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | ba | accuracy | 1 | 0.861328 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.861328125} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | ba | nll | 1 | 0.513836 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.5138358755361777} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | ba | brier | 1 | 0.214131 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.214131032451684} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | ba | ece15 | 1 | 0.0792531 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.07925311549218288} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | ba | seconds | 1 | 0.2298 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.22979956666677026} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | ba | updates | 1 | 16 | — | — | — | 3 | 3 | {"uci_internal_fixed": 16.0} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | ba | skipped | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | ba | recoveries | 1 | 12.3333 | — | — | — | 3 | 3 | {"uci_internal_fixed": 12.333333333333334} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | ab | accuracy | 1 | 0.861328 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.861328125} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | ab | nll | 1 | 0.514106 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.5141057965680674} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | ab | brier | 1 | 0.214172 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.21417164845120007} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | ab | ece15 | 1 | 0.0792869 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.07928688614591352} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | ab | seconds | 1 | 0.228741 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.22874101666820926} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | ab | updates | 1 | 16 | — | — | — | 3 | 3 | {"uci_internal_fixed": 16.0} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | ab | skipped | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | ab | recoveries | 1 | 10.1667 | — | — | — | 3 | 3 | {"uci_internal_fixed": 10.166666666666666} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | ba | accuracy | 1 | 0.861654 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8616536458333334} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | ba | nll | 1 | 0.514135 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.5141350032858429} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | ba | brier | 1 | 0.214177 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.2141765961736135} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | ba | ece15 | 1 | 0.0789634 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.07896337537981624} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | ba | seconds | 1 | 0.217519 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.2175190999987535} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | ba | updates | 1 | 16 | — | — | — | 3 | 3 | {"uci_internal_fixed": 16.0} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | ba | skipped | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | ba | recoveries | 1 | 10 | — | — | — | 3 | 3 | {"uci_internal_fixed": 10.0} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | ab | accuracy | 1 | 0.861654 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8616536458333334} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | ab | nll | 1 | 0.513691 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.5136911208914686} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | ab | brier | 1 | 0.214038 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.21403761550077616} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | ab | ece15 | 1 | 0.0789826 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.07898263321143657} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | ab | seconds | 1 | 0.212361 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.21236051666589142} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | ab | updates | 1 | 16 | — | — | — | 3 | 3 | {"uci_internal_fixed": 16.0} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | ab | skipped | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | ab | recoveries | 1 | 8.5 | — | — | — | 3 | 3 | {"uci_internal_fixed": 8.5} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | ba | accuracy | 1 | 0.861654 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8616536458333334} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | ba | nll | 1 | 0.513692 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.5136918991569656} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | ba | brier | 1 | 0.214038 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.21403775275629702} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | ba | ece15 | 1 | 0.0789819 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.07898188026443755} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | ba | seconds | 1 | 0.222985 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.22298455000175935} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | ba | updates | 1 | 16 | — | — | — | 3 | 3 | {"uci_internal_fixed": 16.0} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | ba | skipped | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | ba | recoveries | 1 | 8.5 | — | — | — | 3 | 3 | {"uci_internal_fixed": 8.5} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | ab | accuracy | 1 | 0.861654 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8616536458333334} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | ab | nll | 1 | 0.513692 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.5136921476014341} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | ab | brier | 1 | 0.214038 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.21403785842504322} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | ab | ece15 | 1 | 0.0789817 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.07898169428309054} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | ab | seconds | 1 | 0.240638 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.24063780000142287} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | ab | updates | 1 | 16 | — | — | — | 3 | 3 | {"uci_internal_fixed": 16.0} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | ab | skipped | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | ab | recoveries | 1 | 8.5 | — | — | — | 3 | 3 | {"uci_internal_fixed": 8.5} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | ba | accuracy | 1 | 0.861654 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8616536458333334} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | ba | nll | 1 | 0.513692 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.5136921476014341} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | ba | brier | 1 | 0.214038 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.21403785842504322} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | ba | ece15 | 1 | 0.0789817 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.07898169428309054} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | ba | seconds | 1 | 0.193516 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.1935158000002654} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | ba | updates | 1 | 16 | — | — | — | 3 | 3 | {"uci_internal_fixed": 16.0} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | ba | skipped | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | ba | recoveries | 1 | 8.5 | — | — | — | 3 | 3 | {"uci_internal_fixed": 8.5} |
| SAR (complete-state implementation) | Reset parameters only | 0 | ab | accuracy | 1 | 0.861328 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.861328125} |
| SAR (complete-state implementation) | Reset parameters only | 0 | ab | nll | 1 | 0.513887 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.5138873977194044} |
| SAR (complete-state implementation) | Reset parameters only | 0 | ab | brier | 1 | 0.214144 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.21414441399914164} |
| SAR (complete-state implementation) | Reset parameters only | 0 | ab | ece15 | 1 | 0.079252 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.07925201735986052} |
| SAR (complete-state implementation) | Reset parameters only | 0 | ab | seconds | 1 | 0.217864 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.21786438332977318} |
| SAR (complete-state implementation) | Reset parameters only | 0 | ab | updates | 1 | 16 | — | — | — | 3 | 3 | {"uci_internal_fixed": 16.0} |
| SAR (complete-state implementation) | Reset parameters only | 0 | ab | skipped | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset parameters only | 0 | ab | recoveries | 1 | 12.8333 | — | — | — | 3 | 3 | {"uci_internal_fixed": 12.833333333333334} |
| SAR (complete-state implementation) | Reset parameters only | 0 | ba | accuracy | 1 | 0.861328 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.861328125} |
| SAR (complete-state implementation) | Reset parameters only | 0 | ba | nll | 1 | 0.513836 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.5138363287174706} |
| SAR (complete-state implementation) | Reset parameters only | 0 | ba | brier | 1 | 0.214131 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.2141312257386754} |
| SAR (complete-state implementation) | Reset parameters only | 0 | ba | ece15 | 1 | 0.0792528 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.07925276788446722} |
| SAR (complete-state implementation) | Reset parameters only | 0 | ba | seconds | 1 | 0.214944 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.21494396666579027} |
| SAR (complete-state implementation) | Reset parameters only | 0 | ba | updates | 1 | 16 | — | — | — | 3 | 3 | {"uci_internal_fixed": 16.0} |
| SAR (complete-state implementation) | Reset parameters only | 0 | ba | skipped | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset parameters only | 0 | ba | recoveries | 1 | 12.3333 | — | — | — | 3 | 3 | {"uci_internal_fixed": 12.333333333333334} |
| SAR (complete-state implementation) | Reset parameters only | 4 | ab | accuracy | 1 | 0.861328 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.861328125} |
| SAR (complete-state implementation) | Reset parameters only | 4 | ab | nll | 1 | 0.514106 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.5141057965680674} |
| SAR (complete-state implementation) | Reset parameters only | 4 | ab | brier | 1 | 0.214172 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.21417164845120007} |
| SAR (complete-state implementation) | Reset parameters only | 4 | ab | ece15 | 1 | 0.0792869 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.07928688614591352} |
| SAR (complete-state implementation) | Reset parameters only | 4 | ab | seconds | 1 | 0.225991 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.22599078333102318} |
| SAR (complete-state implementation) | Reset parameters only | 4 | ab | updates | 1 | 16 | — | — | — | 3 | 3 | {"uci_internal_fixed": 16.0} |
| SAR (complete-state implementation) | Reset parameters only | 4 | ab | skipped | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset parameters only | 4 | ab | recoveries | 1 | 10.1667 | — | — | — | 3 | 3 | {"uci_internal_fixed": 10.166666666666666} |
| SAR (complete-state implementation) | Reset parameters only | 4 | ba | accuracy | 1 | 0.861654 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8616536458333334} |
| SAR (complete-state implementation) | Reset parameters only | 4 | ba | nll | 1 | 0.514135 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.5141350032858429} |
| SAR (complete-state implementation) | Reset parameters only | 4 | ba | brier | 1 | 0.214177 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.2141765961736135} |
| SAR (complete-state implementation) | Reset parameters only | 4 | ba | ece15 | 1 | 0.0789634 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.07896337537981624} |
| SAR (complete-state implementation) | Reset parameters only | 4 | ba | seconds | 1 | 0.254651 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.254651350005588} |
| SAR (complete-state implementation) | Reset parameters only | 4 | ba | updates | 1 | 16 | — | — | — | 3 | 3 | {"uci_internal_fixed": 16.0} |
| SAR (complete-state implementation) | Reset parameters only | 4 | ba | skipped | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset parameters only | 4 | ba | recoveries | 1 | 10 | — | — | — | 3 | 3 | {"uci_internal_fixed": 10.0} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | ab | accuracy | 1 | 0.861654 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8616536458333334} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | ab | nll | 1 | 0.513692 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.5136921476014341} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | ab | brier | 1 | 0.214038 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.21403785842504322} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | ab | ece15 | 1 | 0.0789817 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.07898169428309054} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | ab | seconds | 1 | 0.212891 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.21289105000081077} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | ab | updates | 1 | 16 | — | — | — | 3 | 3 | {"uci_internal_fixed": 16.0} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | ab | skipped | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | ab | recoveries | 1 | 8.5 | — | — | — | 3 | 3 | {"uci_internal_fixed": 8.5} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | ba | accuracy | 1 | 0.861654 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8616536458333334} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | ba | nll | 1 | 0.513692 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.5136921476014341} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | ba | brier | 1 | 0.214038 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.21403785842504322} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | ba | ece15 | 1 | 0.0789817 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.07898169428309054} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | ba | seconds | 1 | 0.221195 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.2211948666639121} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | ba | updates | 1 | 16 | — | — | — | 3 | 3 | {"uci_internal_fixed": 16.0} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | ba | skipped | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | ba | recoveries | 1 | 8.5 | — | — | — | 3 | 3 | {"uci_internal_fixed": 8.5} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | ab | accuracy | 1 | 0.861654 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8616536458333334} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | ab | nll | 1 | 0.513692 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.5136921476014341} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | ab | brier | 1 | 0.214038 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.21403785842504322} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | ab | ece15 | 1 | 0.0789817 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.07898169428309054} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | ab | seconds | 1 | 0.229526 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.22952589999961978} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | ab | updates | 1 | 16 | — | — | — | 3 | 3 | {"uci_internal_fixed": 16.0} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | ab | skipped | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | ab | recoveries | 1 | 8.5 | — | — | — | 3 | 3 | {"uci_internal_fixed": 8.5} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | ba | accuracy | 1 | 0.861654 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8616536458333334} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | ba | nll | 1 | 0.513692 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.5136921476014341} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | ba | brier | 1 | 0.214038 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.21403785842504322} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | ba | ece15 | 1 | 0.0789817 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.07898169428309054} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | ba | seconds | 1 | 0.234399 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.2343990000008489} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | ba | updates | 1 | 16 | — | — | — | 3 | 3 | {"uci_internal_fixed": 16.0} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | ba | skipped | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | ba | recoveries | 1 | 8.5 | — | — | — | 3 | 3 | {"uci_internal_fixed": 8.5} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | ab | accuracy | 1 | 0.861328 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.861328125} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | ab | nll | 1 | 0.513887 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.5138874008871673} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | ab | brier | 1 | 0.214144 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.21414441401160808} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | ab | ece15 | 1 | 0.079252 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.07925201419837379} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | ab | seconds | 1 | 0.221881 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.22188090000175476} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | ab | updates | 1 | 16 | — | — | — | 3 | 3 | {"uci_internal_fixed": 16.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | ab | skipped | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | ab | recoveries | 1 | 12.8333 | — | — | — | 3 | 3 | {"uci_internal_fixed": 12.833333333333334} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | ba | accuracy | 1 | 0.861328 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.861328125} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | ba | nll | 1 | 0.513836 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.5138363516579386} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | ba | brier | 1 | 0.214131 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.21413123763172395} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | ba | ece15 | 1 | 0.0792528 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.07925275504696892} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | ba | seconds | 1 | 0.299368 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.29936818333226256} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | ba | updates | 1 | 16 | — | — | — | 3 | 3 | {"uci_internal_fixed": 16.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | ba | skipped | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | ba | recoveries | 1 | 12.3333 | — | — | — | 3 | 3 | {"uci_internal_fixed": 12.333333333333334} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | ab | accuracy | 1 | 0.861328 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.861328125} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | ab | nll | 1 | 0.514106 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.5141057965680674} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | ab | brier | 1 | 0.214172 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.21417164845120007} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | ab | ece15 | 1 | 0.0792869 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.07928688614591352} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | ab | seconds | 1 | 0.226051 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.22605118333255328} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | ab | updates | 1 | 16 | — | — | — | 3 | 3 | {"uci_internal_fixed": 16.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | ab | skipped | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | ab | recoveries | 1 | 10.1667 | — | — | — | 3 | 3 | {"uci_internal_fixed": 10.166666666666666} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | ba | accuracy | 1 | 0.861654 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8616536458333334} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | ba | nll | 1 | 0.514135 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.5141350032858429} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | ba | brier | 1 | 0.214177 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.2141765961736135} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | ba | ece15 | 1 | 0.0789634 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.07896337537981624} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | ba | seconds | 1 | 0.231818 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.23181801666699656} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | ba | updates | 1 | 16 | — | — | — | 3 | 3 | {"uci_internal_fixed": 16.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | ba | skipped | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | ba | recoveries | 1 | 10 | — | — | — | 3 | 3 | {"uci_internal_fixed": 10.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | ab | accuracy | 1 | 0.861654 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8616536458333334} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | ab | nll | 1 | 0.513692 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.5136921476014341} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | ab | brier | 1 | 0.214038 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.21403785842504322} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | ab | ece15 | 1 | 0.0789817 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.07898169428309054} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | ab | seconds | 1 | 0.204937 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.20493660000162583} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | ab | updates | 1 | 16 | — | — | — | 3 | 3 | {"uci_internal_fixed": 16.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | ab | skipped | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | ab | recoveries | 1 | 8.5 | — | — | — | 3 | 3 | {"uci_internal_fixed": 8.5} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | ba | accuracy | 1 | 0.861654 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8616536458333334} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | ba | nll | 1 | 0.513692 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.5136921476014341} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | ba | brier | 1 | 0.214038 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.21403785842504322} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | ba | ece15 | 1 | 0.0789817 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.07898169428309054} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | ba | seconds | 1 | 0.203826 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.2038256999973479} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | ba | updates | 1 | 16 | — | — | — | 3 | 3 | {"uci_internal_fixed": 16.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | ba | skipped | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | ba | recoveries | 1 | 8.5 | — | — | — | 3 | 3 | {"uci_internal_fixed": 8.5} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | ab | accuracy | 1 | 0.861654 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8616536458333334} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | ab | nll | 1 | 0.513692 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.5136921476014341} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | ab | brier | 1 | 0.214038 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.21403785842504322} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | ab | ece15 | 1 | 0.0789817 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.07898169428309054} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | ab | seconds | 1 | 0.196087 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.1960873499968632} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | ab | updates | 1 | 16 | — | — | — | 3 | 3 | {"uci_internal_fixed": 16.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | ab | skipped | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | ab | recoveries | 1 | 8.5 | — | — | — | 3 | 3 | {"uci_internal_fixed": 8.5} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | ba | accuracy | 1 | 0.861654 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8616536458333334} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | ba | nll | 1 | 0.513692 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.5136921476014341} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | ba | brier | 1 | 0.214038 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.21403785842504322} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | ba | ece15 | 1 | 0.0789817 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.07898169428309054} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | ba | seconds | 1 | 0.212119 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.21211941666600373} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | ba | updates | 1 | 16 | — | — | — | 3 | 3 | {"uci_internal_fixed": 16.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | ba | skipped | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | ba | recoveries | 1 | 8.5 | — | — | — | 3 | 3 | {"uci_internal_fixed": 8.5} |
| Source | Reset all declared state | 0 | ab | accuracy | 1 | 0.814128 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8141276041666666} |
| Source | Reset all declared state | 0 | ab | nll | 1 | 0.551879 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.5518788783477077} |
| Source | Reset all declared state | 0 | ab | brier | 1 | 0.272854 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.2728537124476949} |
| Source | Reset all declared state | 0 | ab | ece15 | 1 | 0.0770746 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.07707458931621847} |
| Source | Reset all declared state | 0 | ab | seconds | 1 | 0.052373 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.05237303333221153} |
| Source | Reset all declared state | 0 | ab | updates | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Source | Reset all declared state | 0 | ab | skipped | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Source | Reset all declared state | 0 | ab | recoveries | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Source | Reset all declared state | 0 | ba | accuracy | 1 | 0.814128 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8141276041666666} |
| Source | Reset all declared state | 0 | ba | nll | 1 | 0.551879 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.5518788783477077} |
| Source | Reset all declared state | 0 | ba | brier | 1 | 0.272854 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.2728537124476949} |
| Source | Reset all declared state | 0 | ba | ece15 | 1 | 0.0770746 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.07707458931621847} |
| Source | Reset all declared state | 0 | ba | seconds | 1 | 0.0575942 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.05759424999754018} |
| Source | Reset all declared state | 0 | ba | updates | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Source | Reset all declared state | 0 | ba | skipped | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Source | Reset all declared state | 0 | ba | recoveries | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Source | Reset all declared state | 4 | ab | accuracy | 1 | 0.814128 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8141276041666666} |
| Source | Reset all declared state | 4 | ab | nll | 1 | 0.551879 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.5518788783477077} |
| Source | Reset all declared state | 4 | ab | brier | 1 | 0.272854 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.2728537124476949} |
| Source | Reset all declared state | 4 | ab | ece15 | 1 | 0.0770746 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.07707458931621847} |
| Source | Reset all declared state | 4 | ab | seconds | 1 | 0.0600619 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.06006191666529042} |
| Source | Reset all declared state | 4 | ab | updates | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Source | Reset all declared state | 4 | ab | skipped | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Source | Reset all declared state | 4 | ab | recoveries | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Source | Reset all declared state | 4 | ba | accuracy | 1 | 0.814128 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8141276041666666} |
| Source | Reset all declared state | 4 | ba | nll | 1 | 0.551879 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.5518788783477077} |
| Source | Reset all declared state | 4 | ba | brier | 1 | 0.272854 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.2728537124476949} |
| Source | Reset all declared state | 4 | ba | ece15 | 1 | 0.0770746 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.07707458931621847} |
| Source | Reset all declared state | 4 | ba | seconds | 1 | 0.0554751 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.05547513333294768} |
| Source | Reset all declared state | 4 | ba | updates | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Source | Reset all declared state | 4 | ba | skipped | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Source | Reset all declared state | 4 | ba | recoveries | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Source | No external reset | 0 | ab | accuracy | 1 | 0.814128 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8141276041666666} |
| Source | No external reset | 0 | ab | nll | 1 | 0.551879 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.5518788783477077} |
| Source | No external reset | 0 | ab | brier | 1 | 0.272854 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.2728537124476949} |
| Source | No external reset | 0 | ab | ece15 | 1 | 0.0770746 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.07707458931621847} |
| Source | No external reset | 0 | ab | seconds | 1 | 0.0741483 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.07414828333518617} |
| Source | No external reset | 0 | ab | updates | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Source | No external reset | 0 | ab | skipped | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Source | No external reset | 0 | ab | recoveries | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Source | No external reset | 0 | ba | accuracy | 1 | 0.814128 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8141276041666666} |
| Source | No external reset | 0 | ba | nll | 1 | 0.551879 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.5518788783477077} |
| Source | No external reset | 0 | ba | brier | 1 | 0.272854 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.2728537124476949} |
| Source | No external reset | 0 | ba | ece15 | 1 | 0.0770746 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.07707458931621847} |
| Source | No external reset | 0 | ba | seconds | 1 | 0.049766 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0497660499992586} |
| Source | No external reset | 0 | ba | updates | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Source | No external reset | 0 | ba | skipped | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Source | No external reset | 0 | ba | recoveries | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Source | No external reset | 4 | ab | accuracy | 1 | 0.814128 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8141276041666666} |
| Source | No external reset | 4 | ab | nll | 1 | 0.551879 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.5518788783477077} |
| Source | No external reset | 4 | ab | brier | 1 | 0.272854 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.2728537124476949} |
| Source | No external reset | 4 | ab | ece15 | 1 | 0.0770746 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.07707458931621847} |
| Source | No external reset | 4 | ab | seconds | 1 | 0.0633344 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.06333443333278407} |
| Source | No external reset | 4 | ab | updates | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Source | No external reset | 4 | ab | skipped | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Source | No external reset | 4 | ab | recoveries | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Source | No external reset | 4 | ba | accuracy | 1 | 0.814128 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8141276041666666} |
| Source | No external reset | 4 | ba | nll | 1 | 0.551879 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.5518788783477077} |
| Source | No external reset | 4 | ba | brier | 1 | 0.272854 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.2728537124476949} |
| Source | No external reset | 4 | ba | ece15 | 1 | 0.0770746 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.07707458931621847} |
| Source | No external reset | 4 | ba | seconds | 1 | 0.0551323 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.055132299998755685} |
| Source | No external reset | 4 | ba | updates | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Source | No external reset | 4 | ba | skipped | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Source | No external reset | 4 | ba | recoveries | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset all declared state | 0 | ab | accuracy | 1 | 0.861654 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8616536458333334} |
| Tent | Reset all declared state | 0 | ab | nll | 1 | 0.514146 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.5141457317600596} |
| Tent | Reset all declared state | 0 | ab | brier | 1 | 0.214142 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.21414177940910126} |
| Tent | Reset all declared state | 0 | ab | ece15 | 1 | 0.0789993 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.07899930300355357} |
| Tent | Reset all declared state | 0 | ab | seconds | 1 | 0.126562 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.12656206667209816} |
| Tent | Reset all declared state | 0 | ab | updates | 1 | 16 | — | — | — | 3 | 3 | {"uci_internal_fixed": 16.0} |
| Tent | Reset all declared state | 0 | ab | skipped | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset all declared state | 0 | ab | recoveries | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset all declared state | 0 | ba | accuracy | 1 | 0.861654 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8616536458333334} |
| Tent | Reset all declared state | 0 | ba | nll | 1 | 0.514146 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.5141457317600596} |
| Tent | Reset all declared state | 0 | ba | brier | 1 | 0.214142 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.21414177940910126} |
| Tent | Reset all declared state | 0 | ba | ece15 | 1 | 0.0789993 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.07899930300355357} |
| Tent | Reset all declared state | 0 | ba | seconds | 1 | 0.11737 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.11736998333314352} |
| Tent | Reset all declared state | 0 | ba | updates | 1 | 16 | — | — | — | 3 | 3 | {"uci_internal_fixed": 16.0} |
| Tent | Reset all declared state | 0 | ba | skipped | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset all declared state | 0 | ba | recoveries | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset all declared state | 4 | ab | accuracy | 1 | 0.861654 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8616536458333334} |
| Tent | Reset all declared state | 4 | ab | nll | 1 | 0.514146 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.5141457317600596} |
| Tent | Reset all declared state | 4 | ab | brier | 1 | 0.214142 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.21414177940910126} |
| Tent | Reset all declared state | 4 | ab | ece15 | 1 | 0.0789993 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.07899930300355357} |
| Tent | Reset all declared state | 4 | ab | seconds | 1 | 0.110205 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.11020466666862673} |
| Tent | Reset all declared state | 4 | ab | updates | 1 | 16 | — | — | — | 3 | 3 | {"uci_internal_fixed": 16.0} |
| Tent | Reset all declared state | 4 | ab | skipped | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset all declared state | 4 | ab | recoveries | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset all declared state | 4 | ba | accuracy | 1 | 0.861654 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8616536458333334} |
| Tent | Reset all declared state | 4 | ba | nll | 1 | 0.514146 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.5141457317600596} |
| Tent | Reset all declared state | 4 | ba | brier | 1 | 0.214142 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.21414177940910126} |
| Tent | Reset all declared state | 4 | ba | ece15 | 1 | 0.0789993 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.07899930300355357} |
| Tent | Reset all declared state | 4 | ba | seconds | 1 | 0.106372 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.10637166666613966} |
| Tent | Reset all declared state | 4 | ba | updates | 1 | 16 | — | — | — | 3 | 3 | {"uci_internal_fixed": 16.0} |
| Tent | Reset all declared state | 4 | ba | skipped | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset all declared state | 4 | ba | recoveries | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset auxiliary state only | 0 | ab | accuracy | 1 | 0.861979 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8619791666666666} |
| Tent | Reset auxiliary state only | 0 | ab | nll | 1 | 0.513931 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.513930715797977} |
| Tent | Reset auxiliary state only | 0 | ab | brier | 1 | 0.214068 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.21406790651952343} |
| Tent | Reset auxiliary state only | 0 | ab | ece15 | 1 | 0.079346 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.07934603479537093} |
| Tent | Reset auxiliary state only | 0 | ab | seconds | 1 | 0.132635 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.13263548333391856} |
| Tent | Reset auxiliary state only | 0 | ab | updates | 1 | 16 | — | — | — | 3 | 3 | {"uci_internal_fixed": 16.0} |
| Tent | Reset auxiliary state only | 0 | ab | skipped | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset auxiliary state only | 0 | ab | recoveries | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset auxiliary state only | 0 | ba | accuracy | 1 | 0.861654 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8616536458333334} |
| Tent | Reset auxiliary state only | 0 | ba | nll | 1 | 0.513905 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.5139045547439033} |
| Tent | Reset auxiliary state only | 0 | ba | brier | 1 | 0.214066 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.2140656711041514} |
| Tent | Reset auxiliary state only | 0 | ba | ece15 | 1 | 0.0794973 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.07949729254838155} |
| Tent | Reset auxiliary state only | 0 | ba | seconds | 1 | 0.126695 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.1266945499955909} |
| Tent | Reset auxiliary state only | 0 | ba | updates | 1 | 16 | — | — | — | 3 | 3 | {"uci_internal_fixed": 16.0} |
| Tent | Reset auxiliary state only | 0 | ba | skipped | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset auxiliary state only | 0 | ba | recoveries | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset auxiliary state only | 4 | ab | accuracy | 1 | 0.862305 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8623046875} |
| Tent | Reset auxiliary state only | 4 | ab | nll | 1 | 0.514415 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.5144152186027519} |
| Tent | Reset auxiliary state only | 4 | ab | brier | 1 | 0.214122 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.21412238750003545} |
| Tent | Reset auxiliary state only | 4 | ab | ece15 | 1 | 0.0791961 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0791961374745065} |
| Tent | Reset auxiliary state only | 4 | ab | seconds | 1 | 0.114857 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.11485696666447132} |
| Tent | Reset auxiliary state only | 4 | ab | updates | 1 | 16 | — | — | — | 3 | 3 | {"uci_internal_fixed": 16.0} |
| Tent | Reset auxiliary state only | 4 | ab | skipped | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset auxiliary state only | 4 | ab | recoveries | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset auxiliary state only | 4 | ba | accuracy | 1 | 0.862305 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8623046875} |
| Tent | Reset auxiliary state only | 4 | ba | nll | 1 | 0.514398 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.5143979326361886} |
| Tent | Reset auxiliary state only | 4 | ba | brier | 1 | 0.214121 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.2141207995192341} |
| Tent | Reset auxiliary state only | 4 | ba | ece15 | 1 | 0.0791877 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0791877265102701} |
| Tent | Reset auxiliary state only | 4 | ba | seconds | 1 | 0.111634 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.11163350000182005} |
| Tent | Reset auxiliary state only | 4 | ba | updates | 1 | 16 | — | — | — | 3 | 3 | {"uci_internal_fixed": 16.0} |
| Tent | Reset auxiliary state only | 4 | ba | skipped | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset auxiliary state only | 4 | ba | recoveries | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | No external reset | 0 | ab | accuracy | 1 | 0.861979 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8619791666666666} |
| Tent | No external reset | 0 | ab | nll | 1 | 0.513931 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.513930715797977} |
| Tent | No external reset | 0 | ab | brier | 1 | 0.214068 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.21406790651952343} |
| Tent | No external reset | 0 | ab | ece15 | 1 | 0.079346 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.07934603479537093} |
| Tent | No external reset | 0 | ab | seconds | 1 | 0.147505 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.14750526666466607} |
| Tent | No external reset | 0 | ab | updates | 1 | 16 | — | — | — | 3 | 3 | {"uci_internal_fixed": 16.0} |
| Tent | No external reset | 0 | ab | skipped | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | No external reset | 0 | ab | recoveries | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | No external reset | 0 | ba | accuracy | 1 | 0.861654 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8616536458333334} |
| Tent | No external reset | 0 | ba | nll | 1 | 0.513905 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.5139045547439033} |
| Tent | No external reset | 0 | ba | brier | 1 | 0.214066 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.2140656711041514} |
| Tent | No external reset | 0 | ba | ece15 | 1 | 0.0794973 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.07949729254838155} |
| Tent | No external reset | 0 | ba | seconds | 1 | 0.125341 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.12534088333389562} |
| Tent | No external reset | 0 | ba | updates | 1 | 16 | — | — | — | 3 | 3 | {"uci_internal_fixed": 16.0} |
| Tent | No external reset | 0 | ba | skipped | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | No external reset | 0 | ba | recoveries | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | No external reset | 4 | ab | accuracy | 1 | 0.862305 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8623046875} |
| Tent | No external reset | 4 | ab | nll | 1 | 0.514415 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.5144152186027519} |
| Tent | No external reset | 4 | ab | brier | 1 | 0.214122 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.21412238750003545} |
| Tent | No external reset | 4 | ab | ece15 | 1 | 0.0791961 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0791961374745065} |
| Tent | No external reset | 4 | ab | seconds | 1 | 0.124795 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.12479485000221753} |
| Tent | No external reset | 4 | ab | updates | 1 | 16 | — | — | — | 3 | 3 | {"uci_internal_fixed": 16.0} |
| Tent | No external reset | 4 | ab | skipped | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | No external reset | 4 | ab | recoveries | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | No external reset | 4 | ba | accuracy | 1 | 0.862305 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8623046875} |
| Tent | No external reset | 4 | ba | nll | 1 | 0.514398 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.5143979326361886} |
| Tent | No external reset | 4 | ba | brier | 1 | 0.214121 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.2141207995192341} |
| Tent | No external reset | 4 | ba | ece15 | 1 | 0.0791877 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0791877265102701} |
| Tent | No external reset | 4 | ba | seconds | 1 | 0.147506 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.14750643333294033} |
| Tent | No external reset | 4 | ba | updates | 1 | 16 | — | — | — | 3 | 3 | {"uci_internal_fixed": 16.0} |
| Tent | No external reset | 4 | ba | skipped | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | No external reset | 4 | ba | recoveries | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset optimizer only | 0 | ab | accuracy | 1 | 0.861979 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8619791666666666} |
| Tent | Reset optimizer only | 0 | ab | nll | 1 | 0.514021 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.5140207636254323} |
| Tent | Reset optimizer only | 0 | ab | brier | 1 | 0.214088 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.21408797244272207} |
| Tent | Reset optimizer only | 0 | ab | ece15 | 1 | 0.0791166 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.07911659185227622} |
| Tent | Reset optimizer only | 0 | ab | seconds | 1 | 0.127872 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.12787220000366986} |
| Tent | Reset optimizer only | 0 | ab | updates | 1 | 16 | — | — | — | 3 | 3 | {"uci_internal_fixed": 16.0} |
| Tent | Reset optimizer only | 0 | ab | skipped | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset optimizer only | 0 | ab | recoveries | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset optimizer only | 0 | ba | accuracy | 1 | 0.861654 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8616536458333334} |
| Tent | Reset optimizer only | 0 | ba | nll | 1 | 0.513958 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.5139579097725794} |
| Tent | Reset optimizer only | 0 | ba | brier | 1 | 0.214083 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.21408338031305515} |
| Tent | Reset optimizer only | 0 | ba | ece15 | 1 | 0.0792563 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.07925634676265982} |
| Tent | Reset optimizer only | 0 | ba | seconds | 1 | 0.120687 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.12068738333133895} |
| Tent | Reset optimizer only | 0 | ba | updates | 1 | 16 | — | — | — | 3 | 3 | {"uci_internal_fixed": 16.0} |
| Tent | Reset optimizer only | 0 | ba | skipped | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset optimizer only | 0 | ba | recoveries | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset optimizer only | 4 | ab | accuracy | 1 | 0.862305 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8623046875} |
| Tent | Reset optimizer only | 4 | ab | nll | 1 | 0.514056 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.5140561009357576} |
| Tent | Reset optimizer only | 4 | ab | brier | 1 | 0.214076 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.21407586250579394} |
| Tent | Reset optimizer only | 4 | ab | ece15 | 1 | 0.0789856 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.07898562420616104} |
| Tent | Reset optimizer only | 4 | ab | seconds | 1 | 0.134044 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.13404435000120427} |
| Tent | Reset optimizer only | 4 | ab | updates | 1 | 16 | — | — | — | 3 | 3 | {"uci_internal_fixed": 16.0} |
| Tent | Reset optimizer only | 4 | ab | skipped | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset optimizer only | 4 | ab | recoveries | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset optimizer only | 4 | ba | accuracy | 1 | 0.862305 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8623046875} |
| Tent | Reset optimizer only | 4 | ba | nll | 1 | 0.514014 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.5140143540019452} |
| Tent | Reset optimizer only | 4 | ba | brier | 1 | 0.214073 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.21407256170017286} |
| Tent | Reset optimizer only | 4 | ba | ece15 | 1 | 0.0791894 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.07918942193259021} |
| Tent | Reset optimizer only | 4 | ba | seconds | 1 | 0.123175 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.12317511666333299} |
| Tent | Reset optimizer only | 4 | ba | updates | 1 | 16 | — | — | — | 3 | 3 | {"uci_internal_fixed": 16.0} |
| Tent | Reset optimizer only | 4 | ba | skipped | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset optimizer only | 4 | ba | recoveries | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset optimizer + auxiliary state | 0 | ab | accuracy | 1 | 0.861979 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8619791666666666} |
| Tent | Reset optimizer + auxiliary state | 0 | ab | nll | 1 | 0.514021 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.5140207636254323} |
| Tent | Reset optimizer + auxiliary state | 0 | ab | brier | 1 | 0.214088 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.21408797244272207} |
| Tent | Reset optimizer + auxiliary state | 0 | ab | ece15 | 1 | 0.0791166 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.07911659185227622} |
| Tent | Reset optimizer + auxiliary state | 0 | ab | seconds | 1 | 0.147242 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.14724173333282423} |
| Tent | Reset optimizer + auxiliary state | 0 | ab | updates | 1 | 16 | — | — | — | 3 | 3 | {"uci_internal_fixed": 16.0} |
| Tent | Reset optimizer + auxiliary state | 0 | ab | skipped | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset optimizer + auxiliary state | 0 | ab | recoveries | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset optimizer + auxiliary state | 0 | ba | accuracy | 1 | 0.861654 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8616536458333334} |
| Tent | Reset optimizer + auxiliary state | 0 | ba | nll | 1 | 0.513958 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.5139579097725794} |
| Tent | Reset optimizer + auxiliary state | 0 | ba | brier | 1 | 0.214083 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.21408338031305515} |
| Tent | Reset optimizer + auxiliary state | 0 | ba | ece15 | 1 | 0.0792563 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.07925634676265982} |
| Tent | Reset optimizer + auxiliary state | 0 | ba | seconds | 1 | 0.116762 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.11676235000292456} |
| Tent | Reset optimizer + auxiliary state | 0 | ba | updates | 1 | 16 | — | — | — | 3 | 3 | {"uci_internal_fixed": 16.0} |
| Tent | Reset optimizer + auxiliary state | 0 | ba | skipped | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset optimizer + auxiliary state | 0 | ba | recoveries | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset optimizer + auxiliary state | 4 | ab | accuracy | 1 | 0.862305 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8623046875} |
| Tent | Reset optimizer + auxiliary state | 4 | ab | nll | 1 | 0.514056 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.5140561009357576} |
| Tent | Reset optimizer + auxiliary state | 4 | ab | brier | 1 | 0.214076 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.21407586250579394} |
| Tent | Reset optimizer + auxiliary state | 4 | ab | ece15 | 1 | 0.0789856 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.07898562420616104} |
| Tent | Reset optimizer + auxiliary state | 4 | ab | seconds | 1 | 0.109525 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.1095247500003703} |
| Tent | Reset optimizer + auxiliary state | 4 | ab | updates | 1 | 16 | — | — | — | 3 | 3 | {"uci_internal_fixed": 16.0} |
| Tent | Reset optimizer + auxiliary state | 4 | ab | skipped | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset optimizer + auxiliary state | 4 | ab | recoveries | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset optimizer + auxiliary state | 4 | ba | accuracy | 1 | 0.862305 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8623046875} |
| Tent | Reset optimizer + auxiliary state | 4 | ba | nll | 1 | 0.514014 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.5140143540019452} |
| Tent | Reset optimizer + auxiliary state | 4 | ba | brier | 1 | 0.214073 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.21407256170017286} |
| Tent | Reset optimizer + auxiliary state | 4 | ba | ece15 | 1 | 0.0791894 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.07918942193259021} |
| Tent | Reset optimizer + auxiliary state | 4 | ba | seconds | 1 | 0.106365 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.10636508333360928} |
| Tent | Reset optimizer + auxiliary state | 4 | ba | updates | 1 | 16 | — | — | — | 3 | 3 | {"uci_internal_fixed": 16.0} |
| Tent | Reset optimizer + auxiliary state | 4 | ba | skipped | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset optimizer + auxiliary state | 4 | ba | recoveries | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset parameters only | 0 | ab | accuracy | 1 | 0.861654 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8616536458333334} |
| Tent | Reset parameters only | 0 | ab | nll | 1 | 0.514055 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.51405495626297} |
| Tent | Reset parameters only | 0 | ab | brier | 1 | 0.214121 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.2141212596574894} |
| Tent | Reset parameters only | 0 | ab | ece15 | 1 | 0.0790121 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.07901208171909709} |
| Tent | Reset parameters only | 0 | ab | seconds | 1 | 0.128546 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.12854586666799148} |
| Tent | Reset parameters only | 0 | ab | updates | 1 | 16 | — | — | — | 3 | 3 | {"uci_internal_fixed": 16.0} |
| Tent | Reset parameters only | 0 | ab | skipped | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset parameters only | 0 | ab | recoveries | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset parameters only | 0 | ba | accuracy | 1 | 0.861654 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8616536458333334} |
| Tent | Reset parameters only | 0 | ba | nll | 1 | 0.514092 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.5140915711297555} |
| Tent | Reset parameters only | 0 | ba | brier | 1 | 0.214124 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.21412360523940868} |
| Tent | Reset parameters only | 0 | ba | ece15 | 1 | 0.0790231 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.07902311552166603} |
| Tent | Reset parameters only | 0 | ba | seconds | 1 | 0.144112 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.1441115500007678} |
| Tent | Reset parameters only | 0 | ba | updates | 1 | 16 | — | — | — | 3 | 3 | {"uci_internal_fixed": 16.0} |
| Tent | Reset parameters only | 0 | ba | skipped | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset parameters only | 0 | ba | recoveries | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset parameters only | 4 | ab | accuracy | 1 | 0.861654 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8616536458333334} |
| Tent | Reset parameters only | 4 | ab | nll | 1 | 0.514502 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.5145020303060358} |
| Tent | Reset parameters only | 4 | ab | brier | 1 | 0.214187 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.21418720471350258} |
| Tent | Reset parameters only | 4 | ab | ece15 | 1 | 0.0790531 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.07905311101615513} |
| Tent | Reset parameters only | 4 | ab | seconds | 1 | 0.126126 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.1261260833368093} |
| Tent | Reset parameters only | 4 | ab | updates | 1 | 16 | — | — | — | 3 | 3 | {"uci_internal_fixed": 16.0} |
| Tent | Reset parameters only | 4 | ab | skipped | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset parameters only | 4 | ab | recoveries | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset parameters only | 4 | ba | accuracy | 1 | 0.861654 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8616536458333334} |
| Tent | Reset parameters only | 4 | ba | nll | 1 | 0.514526 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.5145257348698196} |
| Tent | Reset parameters only | 4 | ba | brier | 1 | 0.214189 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.2141885849925409} |
| Tent | Reset parameters only | 4 | ba | ece15 | 1 | 0.0788868 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.07888675211553235} |
| Tent | Reset parameters only | 4 | ba | seconds | 1 | 0.125484 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.1254844833310926} |
| Tent | Reset parameters only | 4 | ba | updates | 1 | 16 | — | — | — | 3 | 3 | {"uci_internal_fixed": 16.0} |
| Tent | Reset parameters only | 4 | ba | skipped | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset parameters only | 4 | ba | recoveries | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset parameters + auxiliary state | 0 | ab | accuracy | 1 | 0.861654 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8616536458333334} |
| Tent | Reset parameters + auxiliary state | 0 | ab | nll | 1 | 0.514055 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.51405495626297} |
| Tent | Reset parameters + auxiliary state | 0 | ab | brier | 1 | 0.214121 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.2141212596574894} |
| Tent | Reset parameters + auxiliary state | 0 | ab | ece15 | 1 | 0.0790121 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.07901208171909709} |
| Tent | Reset parameters + auxiliary state | 0 | ab | seconds | 1 | 0.11818 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.11817981666293535} |
| Tent | Reset parameters + auxiliary state | 0 | ab | updates | 1 | 16 | — | — | — | 3 | 3 | {"uci_internal_fixed": 16.0} |
| Tent | Reset parameters + auxiliary state | 0 | ab | skipped | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset parameters + auxiliary state | 0 | ab | recoveries | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset parameters + auxiliary state | 0 | ba | accuracy | 1 | 0.861654 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8616536458333334} |
| Tent | Reset parameters + auxiliary state | 0 | ba | nll | 1 | 0.514092 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.5140915711297555} |
| Tent | Reset parameters + auxiliary state | 0 | ba | brier | 1 | 0.214124 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.21412360523940868} |
| Tent | Reset parameters + auxiliary state | 0 | ba | ece15 | 1 | 0.0790231 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.07902311552166603} |
| Tent | Reset parameters + auxiliary state | 0 | ba | seconds | 1 | 0.113979 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.11397948333372669} |
| Tent | Reset parameters + auxiliary state | 0 | ba | updates | 1 | 16 | — | — | — | 3 | 3 | {"uci_internal_fixed": 16.0} |
| Tent | Reset parameters + auxiliary state | 0 | ba | skipped | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset parameters + auxiliary state | 0 | ba | recoveries | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset parameters + auxiliary state | 4 | ab | accuracy | 1 | 0.861654 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8616536458333334} |
| Tent | Reset parameters + auxiliary state | 4 | ab | nll | 1 | 0.514502 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.5145020303060358} |
| Tent | Reset parameters + auxiliary state | 4 | ab | brier | 1 | 0.214187 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.21418720471350258} |
| Tent | Reset parameters + auxiliary state | 4 | ab | ece15 | 1 | 0.0790531 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.07905311101615513} |
| Tent | Reset parameters + auxiliary state | 4 | ab | seconds | 1 | 0.111117 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.111116883335247} |
| Tent | Reset parameters + auxiliary state | 4 | ab | updates | 1 | 16 | — | — | — | 3 | 3 | {"uci_internal_fixed": 16.0} |
| Tent | Reset parameters + auxiliary state | 4 | ab | skipped | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset parameters + auxiliary state | 4 | ab | recoveries | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset parameters + auxiliary state | 4 | ba | accuracy | 1 | 0.861654 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8616536458333334} |
| Tent | Reset parameters + auxiliary state | 4 | ba | nll | 1 | 0.514526 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.5145257348698196} |
| Tent | Reset parameters + auxiliary state | 4 | ba | brier | 1 | 0.214189 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.2141885849925409} |
| Tent | Reset parameters + auxiliary state | 4 | ba | ece15 | 1 | 0.0788868 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.07888675211553235} |
| Tent | Reset parameters + auxiliary state | 4 | ba | seconds | 1 | 0.111848 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.1118477333366172} |
| Tent | Reset parameters + auxiliary state | 4 | ba | updates | 1 | 16 | — | — | — | 3 | 3 | {"uci_internal_fixed": 16.0} |
| Tent | Reset parameters + auxiliary state | 4 | ba | skipped | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset parameters + auxiliary state | 4 | ba | recoveries | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset parameters + optimizer | 0 | ab | accuracy | 1 | 0.861654 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8616536458333334} |
| Tent | Reset parameters + optimizer | 0 | ab | nll | 1 | 0.514146 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.5141457317600596} |
| Tent | Reset parameters + optimizer | 0 | ab | brier | 1 | 0.214142 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.21414177940910126} |
| Tent | Reset parameters + optimizer | 0 | ab | ece15 | 1 | 0.0789993 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.07899930300355357} |
| Tent | Reset parameters + optimizer | 0 | ab | seconds | 1 | 0.121998 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.12199816666786013} |
| Tent | Reset parameters + optimizer | 0 | ab | updates | 1 | 16 | — | — | — | 3 | 3 | {"uci_internal_fixed": 16.0} |
| Tent | Reset parameters + optimizer | 0 | ab | skipped | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset parameters + optimizer | 0 | ab | recoveries | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset parameters + optimizer | 0 | ba | accuracy | 1 | 0.861654 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8616536458333334} |
| Tent | Reset parameters + optimizer | 0 | ba | nll | 1 | 0.514146 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.5141457317600596} |
| Tent | Reset parameters + optimizer | 0 | ba | brier | 1 | 0.214142 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.21414177940910126} |
| Tent | Reset parameters + optimizer | 0 | ba | ece15 | 1 | 0.0789993 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.07899930300355357} |
| Tent | Reset parameters + optimizer | 0 | ba | seconds | 1 | 0.126743 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.12674271666764977} |
| Tent | Reset parameters + optimizer | 0 | ba | updates | 1 | 16 | — | — | — | 3 | 3 | {"uci_internal_fixed": 16.0} |
| Tent | Reset parameters + optimizer | 0 | ba | skipped | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset parameters + optimizer | 0 | ba | recoveries | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset parameters + optimizer | 4 | ab | accuracy | 1 | 0.861654 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8616536458333334} |
| Tent | Reset parameters + optimizer | 4 | ab | nll | 1 | 0.514146 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.5141457317600596} |
| Tent | Reset parameters + optimizer | 4 | ab | brier | 1 | 0.214142 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.21414177940910126} |
| Tent | Reset parameters + optimizer | 4 | ab | ece15 | 1 | 0.0789993 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.07899930300355357} |
| Tent | Reset parameters + optimizer | 4 | ab | seconds | 1 | 0.127586 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.12758623333259797} |
| Tent | Reset parameters + optimizer | 4 | ab | updates | 1 | 16 | — | — | — | 3 | 3 | {"uci_internal_fixed": 16.0} |
| Tent | Reset parameters + optimizer | 4 | ab | skipped | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset parameters + optimizer | 4 | ab | recoveries | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset parameters + optimizer | 4 | ba | accuracy | 1 | 0.861654 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8616536458333334} |
| Tent | Reset parameters + optimizer | 4 | ba | nll | 1 | 0.514146 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.5141457317600596} |
| Tent | Reset parameters + optimizer | 4 | ba | brier | 1 | 0.214142 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.21414177940910126} |
| Tent | Reset parameters + optimizer | 4 | ba | ece15 | 1 | 0.0789993 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.07899930300355357} |
| Tent | Reset parameters + optimizer | 4 | ba | seconds | 1 | 0.121735 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.12173470000076725} |
| Tent | Reset parameters + optimizer | 4 | ba | updates | 1 | 16 | — | — | — | 3 | 3 | {"uci_internal_fixed": 16.0} |
| Tent | Reset parameters + optimizer | 4 | ba | skipped | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset parameters + optimizer | 4 | ba | recoveries | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | ab | accuracy | 1 | 0.861654 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8616536458333334} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | ab | nll | 1 | 0.514146 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.5141457317600596} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | ab | brier | 1 | 0.214142 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.21414177940910126} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | ab | ece15 | 1 | 0.0789993 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.07899930300355357} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | ab | seconds | 1 | 0.123524 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.12352408333633012} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | ab | updates | 1 | 16 | — | — | — | 3 | 3 | {"uci_internal_fixed": 16.0} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | ab | skipped | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | ab | recoveries | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | ba | accuracy | 1 | 0.861654 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8616536458333334} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | ba | nll | 1 | 0.514146 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.5141457317600596} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | ba | brier | 1 | 0.214142 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.21414177940910126} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | ba | ece15 | 1 | 0.0789993 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.07899930300355357} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | ba | seconds | 1 | 0.139554 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.13955404999918145} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | ba | updates | 1 | 16 | — | — | — | 3 | 3 | {"uci_internal_fixed": 16.0} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | ba | skipped | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | ba | recoveries | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | ab | accuracy | 1 | 0.861654 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8616536458333334} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | ab | nll | 1 | 0.514146 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.5141457317600596} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | ab | brier | 1 | 0.214142 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.21414177940910126} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | ab | ece15 | 1 | 0.0789993 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.07899930300355357} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | ab | seconds | 1 | 0.103757 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.10375738332610727} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | ab | updates | 1 | 16 | — | — | — | 3 | 3 | {"uci_internal_fixed": 16.0} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | ab | skipped | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | ab | recoveries | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | ba | accuracy | 1 | 0.861654 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.8616536458333334} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | ba | nll | 1 | 0.514146 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.5141457317600596} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | ba | brier | 1 | 0.214142 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.21414177940910126} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | ba | ece15 | 1 | 0.0789993 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.07899930300355357} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | ba | seconds | 1 | 0.121078 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.12107786666456373} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | ba | updates | 1 | 16 | — | — | — | 3 | 3 | {"uci_internal_fixed": 16.0} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | ba | skipped | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | ba | recoveries | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |


### runs: descriptive seed repetitions

The same image panel is reused across seeds. These standard deviations describe seed variability only; no confidence interval is justified from treating seeds as new image panels.

| method | intervention | washout_batches | direction | panel_id | metric | n_seeds | mean | seed_sd_descriptive | individual_seeds |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Normalization only | Reset all declared state | 0 | ab | uci_internal_fixed | accuracy | 3 | 0.861328 | 0.0182437 | {"17": 0.8583984375, "29": 0.8447265625, "43": 0.880859375} |
| Normalization only | Reset all declared state | 0 | ab | uci_internal_fixed | nll | 3 | 0.513794 | 0.112562 | {"17": 0.5040305544153383, "29": 0.6309192931941356, "43": 0.4064307890545059} |
| Normalization only | Reset all declared state | 0 | ab | uci_internal_fixed | brier | 3 | 0.21413 | 0.0323275 | {"17": 0.2166566601112965, "29": 0.2451202662056445, "43": 0.18061355934372308} |
| Normalization only | Reset all declared state | 0 | ab | uci_internal_fixed | ece15 | 3 | 0.0792477 | 0.0154153 | {"17": 0.08152206528958006, "29": 0.09339940262777335, "43": 0.0628215808161432} |
| Normalization only | Reset all declared state | 0 | ab | uci_internal_fixed | seconds | 3 | 0.0594806 | 0.0145395 | {"17": 0.05302849999861785, "29": 0.07612949999747795, "43": 0.049283699998341} |
| Normalization only | Reset all declared state | 0 | ab | uci_internal_fixed | updates | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Normalization only | Reset all declared state | 0 | ab | uci_internal_fixed | skipped | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Normalization only | Reset all declared state | 0 | ab | uci_internal_fixed | recoveries | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Normalization only | Reset all declared state | 0 | ba | uci_internal_fixed | accuracy | 3 | 0.861328 | 0.0182437 | {"17": 0.8583984375, "29": 0.8447265625, "43": 0.880859375} |
| Normalization only | Reset all declared state | 0 | ba | uci_internal_fixed | nll | 3 | 0.513794 | 0.112562 | {"17": 0.5040305544153383, "29": 0.6309192931941356, "43": 0.4064307890545059} |
| Normalization only | Reset all declared state | 0 | ba | uci_internal_fixed | brier | 3 | 0.21413 | 0.0323275 | {"17": 0.2166566601112965, "29": 0.2451202662056445, "43": 0.18061355934372308} |
| Normalization only | Reset all declared state | 0 | ba | uci_internal_fixed | ece15 | 3 | 0.0792477 | 0.0154153 | {"17": 0.08152206528958006, "29": 0.09339940262777335, "43": 0.0628215808161432} |
| Normalization only | Reset all declared state | 0 | ba | uci_internal_fixed | seconds | 3 | 0.0586038 | 0.0145874 | {"17": 0.0503061999988858, "29": 0.07544725000479949, "43": 0.05005800000071755} |
| Normalization only | Reset all declared state | 0 | ba | uci_internal_fixed | updates | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Normalization only | Reset all declared state | 0 | ba | uci_internal_fixed | skipped | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Normalization only | Reset all declared state | 0 | ba | uci_internal_fixed | recoveries | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Normalization only | Reset all declared state | 4 | ab | uci_internal_fixed | accuracy | 3 | 0.861328 | 0.0182437 | {"17": 0.8583984375, "29": 0.8447265625, "43": 0.880859375} |
| Normalization only | Reset all declared state | 4 | ab | uci_internal_fixed | nll | 3 | 0.513794 | 0.112562 | {"17": 0.5040305544153383, "29": 0.6309192931941356, "43": 0.4064307890545059} |
| Normalization only | Reset all declared state | 4 | ab | uci_internal_fixed | brier | 3 | 0.21413 | 0.0323275 | {"17": 0.2166566601112965, "29": 0.2451202662056445, "43": 0.18061355934372308} |
| Normalization only | Reset all declared state | 4 | ab | uci_internal_fixed | ece15 | 3 | 0.0792477 | 0.0154153 | {"17": 0.08152206528958006, "29": 0.09339940262777335, "43": 0.0628215808161432} |
| Normalization only | Reset all declared state | 4 | ab | uci_internal_fixed | seconds | 3 | 0.0636672 | 0.0119186 | {"17": 0.07110039999679425, "29": 0.0699812000020756, "43": 0.04992000000493135} |
| Normalization only | Reset all declared state | 4 | ab | uci_internal_fixed | updates | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Normalization only | Reset all declared state | 4 | ab | uci_internal_fixed | skipped | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Normalization only | Reset all declared state | 4 | ab | uci_internal_fixed | recoveries | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Normalization only | Reset all declared state | 4 | ba | uci_internal_fixed | accuracy | 3 | 0.861328 | 0.0182437 | {"17": 0.8583984375, "29": 0.8447265625, "43": 0.880859375} |
| Normalization only | Reset all declared state | 4 | ba | uci_internal_fixed | nll | 3 | 0.513794 | 0.112562 | {"17": 0.5040305544153383, "29": 0.6309192931941356, "43": 0.4064307890545059} |
| Normalization only | Reset all declared state | 4 | ba | uci_internal_fixed | brier | 3 | 0.21413 | 0.0323275 | {"17": 0.2166566601112965, "29": 0.2451202662056445, "43": 0.18061355934372308} |
| Normalization only | Reset all declared state | 4 | ba | uci_internal_fixed | ece15 | 3 | 0.0792477 | 0.0154153 | {"17": 0.08152206528958006, "29": 0.09339940262777335, "43": 0.0628215808161432} |
| Normalization only | Reset all declared state | 4 | ba | uci_internal_fixed | seconds | 3 | 0.06602 | 0.0193437 | {"17": 0.06515564999426715, "29": 0.0857814000046346, "43": 0.047123050004302} |
| Normalization only | Reset all declared state | 4 | ba | uci_internal_fixed | updates | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Normalization only | Reset all declared state | 4 | ba | uci_internal_fixed | skipped | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Normalization only | Reset all declared state | 4 | ba | uci_internal_fixed | recoveries | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Normalization only | No external reset | 0 | ab | uci_internal_fixed | accuracy | 3 | 0.861328 | 0.0182437 | {"17": 0.8583984375, "29": 0.8447265625, "43": 0.880859375} |
| Normalization only | No external reset | 0 | ab | uci_internal_fixed | nll | 3 | 0.513794 | 0.112562 | {"17": 0.5040305544153383, "29": 0.6309192931941356, "43": 0.4064307890545059} |
| Normalization only | No external reset | 0 | ab | uci_internal_fixed | brier | 3 | 0.21413 | 0.0323275 | {"17": 0.2166566601112965, "29": 0.2451202662056445, "43": 0.18061355934372308} |
| Normalization only | No external reset | 0 | ab | uci_internal_fixed | ece15 | 3 | 0.0792477 | 0.0154153 | {"17": 0.08152206528958006, "29": 0.09339940262777335, "43": 0.0628215808161432} |
| Normalization only | No external reset | 0 | ab | uci_internal_fixed | seconds | 3 | 0.0609484 | 0.0132722 | {"17": 0.0553335999939008, "29": 0.07610514999396395, "43": 0.05140645000210495} |
| Normalization only | No external reset | 0 | ab | uci_internal_fixed | updates | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Normalization only | No external reset | 0 | ab | uci_internal_fixed | skipped | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Normalization only | No external reset | 0 | ab | uci_internal_fixed | recoveries | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Normalization only | No external reset | 0 | ba | uci_internal_fixed | accuracy | 3 | 0.861328 | 0.0182437 | {"17": 0.8583984375, "29": 0.8447265625, "43": 0.880859375} |
| Normalization only | No external reset | 0 | ba | uci_internal_fixed | nll | 3 | 0.513794 | 0.112562 | {"17": 0.5040305544153383, "29": 0.6309192931941356, "43": 0.4064307890545059} |
| Normalization only | No external reset | 0 | ba | uci_internal_fixed | brier | 3 | 0.21413 | 0.0323275 | {"17": 0.2166566601112965, "29": 0.2451202662056445, "43": 0.18061355934372308} |
| Normalization only | No external reset | 0 | ba | uci_internal_fixed | ece15 | 3 | 0.0792477 | 0.0154153 | {"17": 0.08152206528958006, "29": 0.09339940262777335, "43": 0.0628215808161432} |
| Normalization only | No external reset | 0 | ba | uci_internal_fixed | seconds | 3 | 0.0607845 | 0.0143761 | {"17": 0.05510035000042985, "29": 0.0771335500030545, "43": 0.05011955000372835} |
| Normalization only | No external reset | 0 | ba | uci_internal_fixed | updates | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Normalization only | No external reset | 0 | ba | uci_internal_fixed | skipped | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Normalization only | No external reset | 0 | ba | uci_internal_fixed | recoveries | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Normalization only | No external reset | 4 | ab | uci_internal_fixed | accuracy | 3 | 0.861328 | 0.0182437 | {"17": 0.8583984375, "29": 0.8447265625, "43": 0.880859375} |
| Normalization only | No external reset | 4 | ab | uci_internal_fixed | nll | 3 | 0.513794 | 0.112562 | {"17": 0.5040305544153383, "29": 0.6309192931941356, "43": 0.4064307890545059} |
| Normalization only | No external reset | 4 | ab | uci_internal_fixed | brier | 3 | 0.21413 | 0.0323275 | {"17": 0.2166566601112965, "29": 0.2451202662056445, "43": 0.18061355934372308} |
| Normalization only | No external reset | 4 | ab | uci_internal_fixed | ece15 | 3 | 0.0792477 | 0.0154153 | {"17": 0.08152206528958006, "29": 0.09339940262777335, "43": 0.0628215808161432} |
| Normalization only | No external reset | 4 | ab | uci_internal_fixed | seconds | 3 | 0.0606167 | 0.00982481 | {"17": 0.05452570000488775, "29": 0.0719507999965571, "43": 0.0553734499990241} |
| Normalization only | No external reset | 4 | ab | uci_internal_fixed | updates | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Normalization only | No external reset | 4 | ab | uci_internal_fixed | skipped | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Normalization only | No external reset | 4 | ab | uci_internal_fixed | recoveries | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Normalization only | No external reset | 4 | ba | uci_internal_fixed | accuracy | 3 | 0.861328 | 0.0182437 | {"17": 0.8583984375, "29": 0.8447265625, "43": 0.880859375} |
| Normalization only | No external reset | 4 | ba | uci_internal_fixed | nll | 3 | 0.513794 | 0.112562 | {"17": 0.5040305544153383, "29": 0.6309192931941356, "43": 0.4064307890545059} |
| Normalization only | No external reset | 4 | ba | uci_internal_fixed | brier | 3 | 0.21413 | 0.0323275 | {"17": 0.2166566601112965, "29": 0.2451202662056445, "43": 0.18061355934372308} |
| Normalization only | No external reset | 4 | ba | uci_internal_fixed | ece15 | 3 | 0.0792477 | 0.0154153 | {"17": 0.08152206528958006, "29": 0.09339940262777335, "43": 0.0628215808161432} |
| Normalization only | No external reset | 4 | ba | uci_internal_fixed | seconds | 3 | 0.060981 | 0.0128257 | {"17": 0.0669201999917277, "29": 0.0697605499954079, "43": 0.04626219999772725} |
| Normalization only | No external reset | 4 | ba | uci_internal_fixed | updates | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Normalization only | No external reset | 4 | ba | uci_internal_fixed | skipped | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Normalization only | No external reset | 4 | ba | uci_internal_fixed | recoveries | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset all declared state | 0 | ab | uci_internal_fixed | accuracy | 3 | 0.861654 | 0.0181739 | {"17": 0.859375, "29": 0.8447265625, "43": 0.880859375} |
| SAR (complete-state implementation) | Reset all declared state | 0 | ab | uci_internal_fixed | nll | 3 | 0.513692 | 0.113486 | {"17": 0.5037000013167998, "29": 0.6318433801107537, "43": 0.4055330613767488} |
| SAR (complete-state implementation) | Reset all declared state | 0 | ab | uci_internal_fixed | brier | 3 | 0.214038 | 0.0325401 | {"17": 0.21654437269545612, "29": 0.2452522483772659, "43": 0.18031695420240773} |
| SAR (complete-state implementation) | Reset all declared state | 0 | ab | uci_internal_fixed | ece15 | 3 | 0.0789817 | 0.0153697 | {"17": 0.08057571605142086, "29": 0.0934922971484249, "43": 0.06287706964942585} |
| SAR (complete-state implementation) | Reset all declared state | 0 | ab | uci_internal_fixed | seconds | 3 | 0.22183 | 0.012739 | {"17": 0.21075705000112066, "29": 0.23575235000316752, "43": 0.21897994999744697} |
| SAR (complete-state implementation) | Reset all declared state | 0 | ab | uci_internal_fixed | updates | 3 | 16 | 0 | {"17": 16.0, "29": 16.0, "43": 16.0} |
| SAR (complete-state implementation) | Reset all declared state | 0 | ab | uci_internal_fixed | skipped | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset all declared state | 0 | ab | uci_internal_fixed | recoveries | 3 | 8.5 | 0.5 | {"17": 9.0, "29": 8.5, "43": 8.0} |
| SAR (complete-state implementation) | Reset all declared state | 0 | ba | uci_internal_fixed | accuracy | 3 | 0.861654 | 0.0181739 | {"17": 0.859375, "29": 0.8447265625, "43": 0.880859375} |
| SAR (complete-state implementation) | Reset all declared state | 0 | ba | uci_internal_fixed | nll | 3 | 0.513692 | 0.113486 | {"17": 0.5037000013167998, "29": 0.6318433801107537, "43": 0.4055330613767488} |
| SAR (complete-state implementation) | Reset all declared state | 0 | ba | uci_internal_fixed | brier | 3 | 0.214038 | 0.0325401 | {"17": 0.21654437269545612, "29": 0.2452522483772659, "43": 0.18031695420240773} |
| SAR (complete-state implementation) | Reset all declared state | 0 | ba | uci_internal_fixed | ece15 | 3 | 0.0789817 | 0.0153697 | {"17": 0.08057571605142086, "29": 0.0934922971484249, "43": 0.06287706964942585} |
| SAR (complete-state implementation) | Reset all declared state | 0 | ba | uci_internal_fixed | seconds | 3 | 0.219881 | 0.0158829 | {"17": 0.2276359499956015, "29": 0.2016100000037113, "43": 0.2303959499986376} |
| SAR (complete-state implementation) | Reset all declared state | 0 | ba | uci_internal_fixed | updates | 3 | 16 | 0 | {"17": 16.0, "29": 16.0, "43": 16.0} |
| SAR (complete-state implementation) | Reset all declared state | 0 | ba | uci_internal_fixed | skipped | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset all declared state | 0 | ba | uci_internal_fixed | recoveries | 3 | 8.5 | 0.5 | {"17": 9.0, "29": 8.5, "43": 8.0} |
| SAR (complete-state implementation) | Reset all declared state | 4 | ab | uci_internal_fixed | accuracy | 3 | 0.861654 | 0.0181739 | {"17": 0.859375, "29": 0.8447265625, "43": 0.880859375} |
| SAR (complete-state implementation) | Reset all declared state | 4 | ab | uci_internal_fixed | nll | 3 | 0.513692 | 0.113486 | {"17": 0.5037000013167998, "29": 0.6318433801107537, "43": 0.4055330613767488} |
| SAR (complete-state implementation) | Reset all declared state | 4 | ab | uci_internal_fixed | brier | 3 | 0.214038 | 0.0325401 | {"17": 0.21654437269545612, "29": 0.2452522483772659, "43": 0.18031695420240773} |
| SAR (complete-state implementation) | Reset all declared state | 4 | ab | uci_internal_fixed | ece15 | 3 | 0.0789817 | 0.0153697 | {"17": 0.08057571605142086, "29": 0.0934922971484249, "43": 0.06287706964942585} |
| SAR (complete-state implementation) | Reset all declared state | 4 | ab | uci_internal_fixed | seconds | 3 | 0.20738 | 0.0202242 | {"17": 0.223784900001192, "29": 0.1847837000022991, "43": 0.2135703000021749} |
| SAR (complete-state implementation) | Reset all declared state | 4 | ab | uci_internal_fixed | updates | 3 | 16 | 0 | {"17": 16.0, "29": 16.0, "43": 16.0} |
| SAR (complete-state implementation) | Reset all declared state | 4 | ab | uci_internal_fixed | skipped | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset all declared state | 4 | ab | uci_internal_fixed | recoveries | 3 | 8.5 | 0.5 | {"17": 9.0, "29": 8.5, "43": 8.0} |
| SAR (complete-state implementation) | Reset all declared state | 4 | ba | uci_internal_fixed | accuracy | 3 | 0.861654 | 0.0181739 | {"17": 0.859375, "29": 0.8447265625, "43": 0.880859375} |
| SAR (complete-state implementation) | Reset all declared state | 4 | ba | uci_internal_fixed | nll | 3 | 0.513692 | 0.113486 | {"17": 0.5037000013167998, "29": 0.6318433801107537, "43": 0.4055330613767488} |
| SAR (complete-state implementation) | Reset all declared state | 4 | ba | uci_internal_fixed | brier | 3 | 0.214038 | 0.0325401 | {"17": 0.21654437269545612, "29": 0.2452522483772659, "43": 0.18031695420240773} |
| SAR (complete-state implementation) | Reset all declared state | 4 | ba | uci_internal_fixed | ece15 | 3 | 0.0789817 | 0.0153697 | {"17": 0.08057571605142086, "29": 0.0934922971484249, "43": 0.06287706964942585} |
| SAR (complete-state implementation) | Reset all declared state | 4 | ba | uci_internal_fixed | seconds | 3 | 0.199697 | 0.0263448 | {"17": 0.2173579500013147, "29": 0.21231640000041804, "43": 0.16941600000427565} |
| SAR (complete-state implementation) | Reset all declared state | 4 | ba | uci_internal_fixed | updates | 3 | 16 | 0 | {"17": 16.0, "29": 16.0, "43": 16.0} |
| SAR (complete-state implementation) | Reset all declared state | 4 | ba | uci_internal_fixed | skipped | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset all declared state | 4 | ba | uci_internal_fixed | recoveries | 3 | 8.5 | 0.5 | {"17": 9.0, "29": 8.5, "43": 8.0} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | ab | uci_internal_fixed | accuracy | 3 | 0.861654 | 0.0181739 | {"17": 0.859375, "29": 0.8447265625, "43": 0.880859375} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | ab | uci_internal_fixed | nll | 3 | 0.513691 | 0.113487 | {"17": 0.503698549903575, "29": 0.6318435146653553, "43": 0.40553129810547567} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | ab | uci_internal_fixed | brier | 3 | 0.214038 | 0.0325403 | {"17": 0.21654373566293117, "29": 0.24525235301770004, "43": 0.1803167578216972} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | ab | uci_internal_fixed | ece15 | 3 | 0.0789826 | 0.0153689 | {"17": 0.08057687450120081, "29": 0.09349226239343, "43": 0.06287876273967889} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | ab | uci_internal_fixed | seconds | 3 | 0.28652 | 0.0799823 | {"17": 0.3775595999977667, "29": 0.2544517000060295, "43": 0.22754749999876367} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | ab | uci_internal_fixed | updates | 3 | 16 | 0 | {"17": 16.0, "29": 16.0, "43": 16.0} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | ab | uci_internal_fixed | skipped | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | ab | uci_internal_fixed | recoveries | 3 | 8.5 | 0.5 | {"17": 9.0, "29": 8.5, "43": 8.0} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | ba | uci_internal_fixed | accuracy | 3 | 0.861654 | 0.0181739 | {"17": 0.859375, "29": 0.8447265625, "43": 0.880859375} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | ba | uci_internal_fixed | nll | 3 | 0.513692 | 0.113486 | {"17": 0.503699288810314, "29": 0.6318434008784773, "43": 0.40553300778210555} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | ba | uci_internal_fixed | brier | 3 | 0.214038 | 0.0325401 | {"17": 0.2165440424039253, "29": 0.2452522676079189, "43": 0.18031694825704694} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | ba | uci_internal_fixed | ece15 | 3 | 0.0789819 | 0.0153697 | {"17": 0.08057627214565251, "29": 0.09349224752339405, "43": 0.06287712112426609} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | ba | uci_internal_fixed | seconds | 3 | 0.216309 | 0.0429823 | {"17": 0.25623359999735834, "29": 0.22188109999842703, "43": 0.17081239999970416} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | ba | uci_internal_fixed | updates | 3 | 16 | 0 | {"17": 16.0, "29": 16.0, "43": 16.0} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | ba | uci_internal_fixed | skipped | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | ba | uci_internal_fixed | recoveries | 3 | 8.5 | 0.5 | {"17": 9.0, "29": 8.5, "43": 8.0} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | ab | uci_internal_fixed | accuracy | 3 | 0.861654 | 0.0181739 | {"17": 0.859375, "29": 0.8447265625, "43": 0.880859375} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | ab | uci_internal_fixed | nll | 3 | 0.513692 | 0.113486 | {"17": 0.5037000013167998, "29": 0.6318433801107537, "43": 0.4055330613767488} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | ab | uci_internal_fixed | brier | 3 | 0.214038 | 0.0325401 | {"17": 0.21654437269545612, "29": 0.2452522483772659, "43": 0.18031695420240773} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | ab | uci_internal_fixed | ece15 | 3 | 0.0789817 | 0.0153697 | {"17": 0.08057571605142086, "29": 0.0934922971484249, "43": 0.06287706964942585} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | ab | uci_internal_fixed | seconds | 3 | 0.208781 | 0.0160414 | {"17": 0.21777950000250712, "29": 0.19026030000532046, "43": 0.21830259999842383} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | ab | uci_internal_fixed | updates | 3 | 16 | 0 | {"17": 16.0, "29": 16.0, "43": 16.0} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | ab | uci_internal_fixed | skipped | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | ab | uci_internal_fixed | recoveries | 3 | 8.5 | 0.5 | {"17": 9.0, "29": 8.5, "43": 8.0} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | ba | uci_internal_fixed | accuracy | 3 | 0.861654 | 0.0181739 | {"17": 0.859375, "29": 0.8447265625, "43": 0.880859375} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | ba | uci_internal_fixed | nll | 3 | 0.513692 | 0.113486 | {"17": 0.5037000013167998, "29": 0.6318433801107537, "43": 0.4055330613767488} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | ba | uci_internal_fixed | brier | 3 | 0.214038 | 0.0325401 | {"17": 0.21654437269545612, "29": 0.2452522483772659, "43": 0.18031695420240773} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | ba | uci_internal_fixed | ece15 | 3 | 0.0789817 | 0.0153697 | {"17": 0.08057571605142086, "29": 0.0934922971484249, "43": 0.06287706964942585} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | ba | uci_internal_fixed | seconds | 3 | 0.23173 | 0.0504905 | {"17": 0.23075884999707336, "29": 0.18173139999998966, "43": 0.2826984999992419} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | ba | uci_internal_fixed | updates | 3 | 16 | 0 | {"17": 16.0, "29": 16.0, "43": 16.0} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | ba | uci_internal_fixed | skipped | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | ba | uci_internal_fixed | recoveries | 3 | 8.5 | 0.5 | {"17": 9.0, "29": 8.5, "43": 8.0} |
| SAR (complete-state implementation) | No external reset | 0 | ab | uci_internal_fixed | accuracy | 3 | 0.861328 | 0.0182437 | {"17": 0.8583984375, "29": 0.8447265625, "43": 0.880859375} |
| SAR (complete-state implementation) | No external reset | 0 | ab | uci_internal_fixed | nll | 3 | 0.513886 | 0.11262 | {"17": 0.5041910631568645, "29": 0.6310401962076096, "43": 0.40642774774184215} |
| SAR (complete-state implementation) | No external reset | 0 | ab | uci_internal_fixed | brier | 3 | 0.214144 | 0.0323372 | {"17": 0.21668658788135536, "29": 0.24513507703834234, "43": 0.18061084884699802} |
| SAR (complete-state implementation) | No external reset | 0 | ab | uci_internal_fixed | ece15 | 3 | 0.079253 | 0.0154188 | {"17": 0.0815274040682121, "29": 0.0934082419371765, "43": 0.06282332905460469} |
| SAR (complete-state implementation) | No external reset | 0 | ab | uci_internal_fixed | seconds | 3 | 0.200229 | 0.0362621 | {"17": 0.1967870499938726, "29": 0.2380889999985811, "43": 0.1658101500070188} |
| SAR (complete-state implementation) | No external reset | 0 | ab | uci_internal_fixed | updates | 3 | 16 | 0 | {"17": 16.0, "29": 16.0, "43": 16.0} |
| SAR (complete-state implementation) | No external reset | 0 | ab | uci_internal_fixed | skipped | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | No external reset | 0 | ab | uci_internal_fixed | recoveries | 3 | 12.8333 | 1.1547 | {"17": 11.5, "29": 13.5, "43": 13.5} |
| SAR (complete-state implementation) | No external reset | 0 | ba | uci_internal_fixed | accuracy | 3 | 0.861328 | 0.0182437 | {"17": 0.8583984375, "29": 0.8447265625, "43": 0.880859375} |
| SAR (complete-state implementation) | No external reset | 0 | ba | uci_internal_fixed | nll | 3 | 0.513836 | 0.112628 | {"17": 0.5040330793542003, "29": 0.6310450260353394, "43": 0.40642945741847203} |
| SAR (complete-state implementation) | No external reset | 0 | ba | uci_internal_fixed | brier | 3 | 0.214131 | 0.0323359 | {"17": 0.21664599780433452, "29": 0.2451360271470333, "43": 0.18061103928234776} |
| SAR (complete-state implementation) | No external reset | 0 | ba | uci_internal_fixed | ece15 | 3 | 0.0792531 | 0.0154196 | {"17": 0.08152989594354004, "29": 0.09340779777830745, "43": 0.06282168743919189} |
| SAR (complete-state implementation) | No external reset | 0 | ba | uci_internal_fixed | seconds | 3 | 0.208672 | 0.0333439 | {"17": 0.19875740000134096, "29": 0.24584825000056296, "43": 0.18140920000587354} |
| SAR (complete-state implementation) | No external reset | 0 | ba | uci_internal_fixed | updates | 3 | 16 | 0 | {"17": 16.0, "29": 16.0, "43": 16.0} |
| SAR (complete-state implementation) | No external reset | 0 | ba | uci_internal_fixed | skipped | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | No external reset | 0 | ba | uci_internal_fixed | recoveries | 3 | 12.3333 | 1.60728 | {"17": 10.5, "29": 13.0, "43": 13.5} |
| SAR (complete-state implementation) | No external reset | 4 | ab | uci_internal_fixed | accuracy | 3 | 0.861328 | 0.0182437 | {"17": 0.8583984375, "29": 0.8447265625, "43": 0.880859375} |
| SAR (complete-state implementation) | No external reset | 4 | ab | uci_internal_fixed | nll | 3 | 0.514106 | 0.113123 | {"17": 0.5037641486303785, "29": 0.6320447481779414, "43": 0.4065084928958825} |
| SAR (complete-state implementation) | No external reset | 4 | ab | uci_internal_fixed | brier | 3 | 0.214172 | 0.0324058 | {"17": 0.21657729182921606, "29": 0.24530756036666548, "43": 0.1806300931577187} |
| SAR (complete-state implementation) | No external reset | 4 | ab | uci_internal_fixed | ece15 | 3 | 0.0792869 | 0.015458 | {"17": 0.08153867859604605, "29": 0.0934954526290433, "43": 0.0628265272126512} |
| SAR (complete-state implementation) | No external reset | 4 | ab | uci_internal_fixed | seconds | 3 | 0.205495 | 0.0126714 | {"17": 0.2200679000015952, "29": 0.1993402500011143, "43": 0.19707610000477865} |
| SAR (complete-state implementation) | No external reset | 4 | ab | uci_internal_fixed | updates | 3 | 16 | 0 | {"17": 16.0, "29": 16.0, "43": 16.0} |
| SAR (complete-state implementation) | No external reset | 4 | ab | uci_internal_fixed | skipped | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | No external reset | 4 | ab | uci_internal_fixed | recoveries | 3 | 10.1667 | 1.25831 | {"17": 10.0, "29": 9.0, "43": 11.5} |
| SAR (complete-state implementation) | No external reset | 4 | ba | uci_internal_fixed | accuracy | 3 | 0.861654 | 0.0181739 | {"17": 0.859375, "29": 0.8447265625, "43": 0.880859375} |
| SAR (complete-state implementation) | No external reset | 4 | ba | uci_internal_fixed | nll | 3 | 0.514135 | 0.113119 | {"17": 0.5038517687837049, "29": 0.6320447481779414, "43": 0.4065084928958825} |
| SAR (complete-state implementation) | No external reset | 4 | ba | uci_internal_fixed | brier | 3 | 0.214177 | 0.0324063 | {"17": 0.21659213499645635, "29": 0.24530756036666548, "43": 0.1806300931577187} |
| SAR (complete-state implementation) | No external reset | 4 | ba | uci_internal_fixed | ece15 | 3 | 0.0789634 | 0.0153973 | {"17": 0.0805681462977542, "29": 0.0934954526290433, "43": 0.0628265272126512} |
| SAR (complete-state implementation) | No external reset | 4 | ba | uci_internal_fixed | seconds | 3 | 0.205179 | 0.00402797 | {"17": 0.2092369500023778, "29": 0.20118170000205282, "43": 0.2051185999953304} |
| SAR (complete-state implementation) | No external reset | 4 | ba | uci_internal_fixed | updates | 3 | 16 | 0 | {"17": 16.0, "29": 16.0, "43": 16.0} |
| SAR (complete-state implementation) | No external reset | 4 | ba | uci_internal_fixed | skipped | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | No external reset | 4 | ba | uci_internal_fixed | recoveries | 3 | 10 | 1.32288 | {"17": 9.5, "29": 9.0, "43": 11.5} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | ab | uci_internal_fixed | accuracy | 3 | 0.861328 | 0.0182437 | {"17": 0.8583984375, "29": 0.8447265625, "43": 0.880859375} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | ab | uci_internal_fixed | nll | 3 | 0.513886 | 0.11262 | {"17": 0.5041910719180245, "29": 0.6310401962076096, "43": 0.40642774774184215} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | ab | uci_internal_fixed | brier | 3 | 0.214144 | 0.0323372 | {"17": 0.21668658789903744, "29": 0.24513507703834234, "43": 0.18061084884699802} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | ab | uci_internal_fixed | ece15 | 3 | 0.079253 | 0.0154188 | {"17": 0.08152739531957165, "29": 0.0934082419371765, "43": 0.06282332905460469} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | ab | uci_internal_fixed | seconds | 3 | 0.225919 | 0.0421477 | {"17": 0.22882580000441521, "29": 0.2665387000015471, "43": 0.18239370000082994} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | ab | uci_internal_fixed | updates | 3 | 16 | 0 | {"17": 16.0, "29": 16.0, "43": 16.0} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | ab | uci_internal_fixed | skipped | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | ab | uci_internal_fixed | recoveries | 3 | 12.8333 | 1.1547 | {"17": 11.5, "29": 13.5, "43": 13.5} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | ba | uci_internal_fixed | accuracy | 3 | 0.861328 | 0.0182437 | {"17": 0.8583984375, "29": 0.8447265625, "43": 0.880859375} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | ba | uci_internal_fixed | nll | 3 | 0.513836 | 0.112628 | {"17": 0.5040331431547219, "29": 0.6310450260353394, "43": 0.40642945741847203} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | ba | uci_internal_fixed | brier | 3 | 0.214131 | 0.0323359 | {"17": 0.216646030925671, "29": 0.2451360271470333, "43": 0.18061103928234776} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | ba | uci_internal_fixed | ece15 | 3 | 0.0792531 | 0.0154196 | {"17": 0.08152986125904929, "29": 0.09340779777830745, "43": 0.06282168743919189} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | ba | uci_internal_fixed | seconds | 3 | 0.2298 | 0.0242058 | {"17": 0.2215925499986042, "29": 0.25704190000396915, "43": 0.21076424999773735} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | ba | uci_internal_fixed | updates | 3 | 16 | 0 | {"17": 16.0, "29": 16.0, "43": 16.0} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | ba | uci_internal_fixed | skipped | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | ba | uci_internal_fixed | recoveries | 3 | 12.3333 | 1.60728 | {"17": 10.5, "29": 13.0, "43": 13.5} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | ab | uci_internal_fixed | accuracy | 3 | 0.861328 | 0.0182437 | {"17": 0.8583984375, "29": 0.8447265625, "43": 0.880859375} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | ab | uci_internal_fixed | nll | 3 | 0.514106 | 0.113123 | {"17": 0.5037641486303785, "29": 0.6320447481779414, "43": 0.4065084928958825} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | ab | uci_internal_fixed | brier | 3 | 0.214172 | 0.0324058 | {"17": 0.21657729182921606, "29": 0.24530756036666548, "43": 0.1806300931577187} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | ab | uci_internal_fixed | ece15 | 3 | 0.0792869 | 0.015458 | {"17": 0.08153867859604605, "29": 0.0934954526290433, "43": 0.0628265272126512} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | ab | uci_internal_fixed | seconds | 3 | 0.228741 | 0.0461326 | {"17": 0.2811496499998611, "29": 0.19427745000575664, "43": 0.21079594999901013} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | ab | uci_internal_fixed | updates | 3 | 16 | 0 | {"17": 16.0, "29": 16.0, "43": 16.0} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | ab | uci_internal_fixed | skipped | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | ab | uci_internal_fixed | recoveries | 3 | 10.1667 | 1.25831 | {"17": 10.0, "29": 9.0, "43": 11.5} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | ba | uci_internal_fixed | accuracy | 3 | 0.861654 | 0.0181739 | {"17": 0.859375, "29": 0.8447265625, "43": 0.880859375} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | ba | uci_internal_fixed | nll | 3 | 0.514135 | 0.113119 | {"17": 0.5038517687837049, "29": 0.6320447481779414, "43": 0.4065084928958825} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | ba | uci_internal_fixed | brier | 3 | 0.214177 | 0.0324063 | {"17": 0.21659213499645635, "29": 0.24530756036666548, "43": 0.1806300931577187} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | ba | uci_internal_fixed | ece15 | 3 | 0.0789634 | 0.0153973 | {"17": 0.0805681462977542, "29": 0.0934954526290433, "43": 0.0628265272126512} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | ba | uci_internal_fixed | seconds | 3 | 0.217519 | 0.0188299 | {"17": 0.22432885000307573, "29": 0.1962316999924951, "43": 0.2319967500006896} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | ba | uci_internal_fixed | updates | 3 | 16 | 0 | {"17": 16.0, "29": 16.0, "43": 16.0} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | ba | uci_internal_fixed | skipped | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | ba | uci_internal_fixed | recoveries | 3 | 10 | 1.32288 | {"17": 9.5, "29": 9.0, "43": 11.5} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | ab | uci_internal_fixed | accuracy | 3 | 0.861654 | 0.0181739 | {"17": 0.859375, "29": 0.8447265625, "43": 0.880859375} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | ab | uci_internal_fixed | nll | 3 | 0.513691 | 0.113487 | {"17": 0.503698549903575, "29": 0.6318435146653553, "43": 0.40553129810547567} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | ab | uci_internal_fixed | brier | 3 | 0.214038 | 0.0325403 | {"17": 0.21654373566293117, "29": 0.24525235301770004, "43": 0.1803167578216972} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | ab | uci_internal_fixed | ece15 | 3 | 0.0789826 | 0.0153689 | {"17": 0.08057687450120081, "29": 0.09349226239343, "43": 0.06287876273967889} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | ab | uci_internal_fixed | seconds | 3 | 0.212361 | 0.0260951 | {"17": 0.23331755000253904, "29": 0.18313219999254216, "43": 0.22063180000259305} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | ab | uci_internal_fixed | updates | 3 | 16 | 0 | {"17": 16.0, "29": 16.0, "43": 16.0} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | ab | uci_internal_fixed | skipped | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | ab | uci_internal_fixed | recoveries | 3 | 8.5 | 0.5 | {"17": 9.0, "29": 8.5, "43": 8.0} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | ba | uci_internal_fixed | accuracy | 3 | 0.861654 | 0.0181739 | {"17": 0.859375, "29": 0.8447265625, "43": 0.880859375} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | ba | uci_internal_fixed | nll | 3 | 0.513692 | 0.113486 | {"17": 0.503699288810314, "29": 0.6318434008784773, "43": 0.40553300778210555} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | ba | uci_internal_fixed | brier | 3 | 0.214038 | 0.0325401 | {"17": 0.2165440424039253, "29": 0.2452522676079189, "43": 0.18031694825704694} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | ba | uci_internal_fixed | ece15 | 3 | 0.0789819 | 0.0153697 | {"17": 0.08057627214565251, "29": 0.09349224752339405, "43": 0.06287712112426609} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | ba | uci_internal_fixed | seconds | 3 | 0.222985 | 0.0316182 | {"17": 0.25171080000291113, "29": 0.1891069999983301, "43": 0.22813585000403686} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | ba | uci_internal_fixed | updates | 3 | 16 | 0 | {"17": 16.0, "29": 16.0, "43": 16.0} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | ba | uci_internal_fixed | skipped | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | ba | uci_internal_fixed | recoveries | 3 | 8.5 | 0.5 | {"17": 9.0, "29": 8.5, "43": 8.0} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | ab | uci_internal_fixed | accuracy | 3 | 0.861654 | 0.0181739 | {"17": 0.859375, "29": 0.8447265625, "43": 0.880859375} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | ab | uci_internal_fixed | nll | 3 | 0.513692 | 0.113486 | {"17": 0.5037000013167998, "29": 0.6318433801107537, "43": 0.4055330613767488} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | ab | uci_internal_fixed | brier | 3 | 0.214038 | 0.0325401 | {"17": 0.21654437269545612, "29": 0.2452522483772659, "43": 0.18031695420240773} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | ab | uci_internal_fixed | ece15 | 3 | 0.0789817 | 0.0153697 | {"17": 0.08057571605142086, "29": 0.0934922971484249, "43": 0.06287706964942585} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | ab | uci_internal_fixed | seconds | 3 | 0.240638 | 0.0536854 | {"17": 0.2190887000033399, "29": 0.301749700003711, "43": 0.20107499999721767} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | ab | uci_internal_fixed | updates | 3 | 16 | 0 | {"17": 16.0, "29": 16.0, "43": 16.0} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | ab | uci_internal_fixed | skipped | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | ab | uci_internal_fixed | recoveries | 3 | 8.5 | 0.5 | {"17": 9.0, "29": 8.5, "43": 8.0} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | ba | uci_internal_fixed | accuracy | 3 | 0.861654 | 0.0181739 | {"17": 0.859375, "29": 0.8447265625, "43": 0.880859375} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | ba | uci_internal_fixed | nll | 3 | 0.513692 | 0.113486 | {"17": 0.5037000013167998, "29": 0.6318433801107537, "43": 0.4055330613767488} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | ba | uci_internal_fixed | brier | 3 | 0.214038 | 0.0325401 | {"17": 0.21654437269545612, "29": 0.2452522483772659, "43": 0.18031695420240773} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | ba | uci_internal_fixed | ece15 | 3 | 0.0789817 | 0.0153697 | {"17": 0.08057571605142086, "29": 0.0934922971484249, "43": 0.06287706964942585} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | ba | uci_internal_fixed | seconds | 3 | 0.193516 | 0.0184235 | {"17": 0.1992647500010207, "29": 0.20837939999910304, "43": 0.17290325000067241} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | ba | uci_internal_fixed | updates | 3 | 16 | 0 | {"17": 16.0, "29": 16.0, "43": 16.0} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | ba | uci_internal_fixed | skipped | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | ba | uci_internal_fixed | recoveries | 3 | 8.5 | 0.5 | {"17": 9.0, "29": 8.5, "43": 8.0} |
| SAR (complete-state implementation) | Reset parameters only | 0 | ab | uci_internal_fixed | accuracy | 3 | 0.861328 | 0.0182437 | {"17": 0.8583984375, "29": 0.8447265625, "43": 0.880859375} |
| SAR (complete-state implementation) | Reset parameters only | 0 | ab | uci_internal_fixed | nll | 3 | 0.513887 | 0.112619 | {"17": 0.5041926204920896, "29": 0.6310400616530081, "43": 0.4064295110131153} |
| SAR (complete-state implementation) | Reset parameters only | 0 | ab | uci_internal_fixed | brier | 3 | 0.214144 | 0.032337 | {"17": 0.21668722437180815, "29": 0.24513497239790819, "43": 0.18061104522770854} |
| SAR (complete-state implementation) | Reset parameters only | 0 | ab | uci_internal_fixed | ece15 | 3 | 0.079252 | 0.0154196 | {"17": 0.08152613942305854, "29": 0.0934082766921714, "43": 0.06282163596435164} |
| SAR (complete-state implementation) | Reset parameters only | 0 | ab | uci_internal_fixed | seconds | 3 | 0.217864 | 0.0265619 | {"17": 0.2083394000001135, "29": 0.2478754999974626, "43": 0.19737824999174336} |
| SAR (complete-state implementation) | Reset parameters only | 0 | ab | uci_internal_fixed | updates | 3 | 16 | 0 | {"17": 16.0, "29": 16.0, "43": 16.0} |
| SAR (complete-state implementation) | Reset parameters only | 0 | ab | uci_internal_fixed | skipped | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters only | 0 | ab | uci_internal_fixed | recoveries | 3 | 12.8333 | 1.1547 | {"17": 11.5, "29": 13.5, "43": 13.5} |
| SAR (complete-state implementation) | Reset parameters only | 0 | ba | uci_internal_fixed | accuracy | 3 | 0.861328 | 0.0182437 | {"17": 0.8583984375, "29": 0.8447265625, "43": 0.880859375} |
| SAR (complete-state implementation) | Reset parameters only | 0 | ba | uci_internal_fixed | nll | 3 | 0.513836 | 0.112628 | {"17": 0.5040344698716808, "29": 0.6310450052676158, "43": 0.4064295110131153} |
| SAR (complete-state implementation) | Reset parameters only | 0 | ba | uci_internal_fixed | brier | 3 | 0.214131 | 0.0323359 | {"17": 0.2166466240719374, "29": 0.2451360079163803, "43": 0.18061104522770854} |
| SAR (complete-state implementation) | Reset parameters only | 0 | ba | uci_internal_fixed | ece15 | 3 | 0.0792528 | 0.0154196 | {"17": 0.08152882028571175, "29": 0.0934078474033383, "43": 0.06282163596435164} |
| SAR (complete-state implementation) | Reset parameters only | 0 | ba | uci_internal_fixed | seconds | 3 | 0.214944 | 0.0315505 | {"17": 0.20841294999991075, "29": 0.24924889999965671, "43": 0.18717004999780326} |
| SAR (complete-state implementation) | Reset parameters only | 0 | ba | uci_internal_fixed | updates | 3 | 16 | 0 | {"17": 16.0, "29": 16.0, "43": 16.0} |
| SAR (complete-state implementation) | Reset parameters only | 0 | ba | uci_internal_fixed | skipped | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters only | 0 | ba | uci_internal_fixed | recoveries | 3 | 12.3333 | 1.60728 | {"17": 10.5, "29": 13.0, "43": 13.5} |
| SAR (complete-state implementation) | Reset parameters only | 4 | ab | uci_internal_fixed | accuracy | 3 | 0.861328 | 0.0182437 | {"17": 0.8583984375, "29": 0.8447265625, "43": 0.880859375} |
| SAR (complete-state implementation) | Reset parameters only | 4 | ab | uci_internal_fixed | nll | 3 | 0.514106 | 0.113123 | {"17": 0.5037641486303785, "29": 0.6320447481779414, "43": 0.4065084928958825} |
| SAR (complete-state implementation) | Reset parameters only | 4 | ab | uci_internal_fixed | brier | 3 | 0.214172 | 0.0324058 | {"17": 0.21657729182921606, "29": 0.24530756036666548, "43": 0.1806300931577187} |
| SAR (complete-state implementation) | Reset parameters only | 4 | ab | uci_internal_fixed | ece15 | 3 | 0.0792869 | 0.015458 | {"17": 0.08153867859604605, "29": 0.0934954526290433, "43": 0.0628265272126512} |
| SAR (complete-state implementation) | Reset parameters only | 4 | ab | uci_internal_fixed | seconds | 3 | 0.225991 | 0.0562976 | {"17": 0.28991219999443274, "29": 0.20427494999603363, "43": 0.18378520000260318} |
| SAR (complete-state implementation) | Reset parameters only | 4 | ab | uci_internal_fixed | updates | 3 | 16 | 0 | {"17": 16.0, "29": 16.0, "43": 16.0} |
| SAR (complete-state implementation) | Reset parameters only | 4 | ab | uci_internal_fixed | skipped | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters only | 4 | ab | uci_internal_fixed | recoveries | 3 | 10.1667 | 1.25831 | {"17": 10.0, "29": 9.0, "43": 11.5} |
| SAR (complete-state implementation) | Reset parameters only | 4 | ba | uci_internal_fixed | accuracy | 3 | 0.861654 | 0.0181739 | {"17": 0.859375, "29": 0.8447265625, "43": 0.880859375} |
| SAR (complete-state implementation) | Reset parameters only | 4 | ba | uci_internal_fixed | nll | 3 | 0.514135 | 0.113119 | {"17": 0.5038517687837049, "29": 0.6320447481779414, "43": 0.4065084928958825} |
| SAR (complete-state implementation) | Reset parameters only | 4 | ba | uci_internal_fixed | brier | 3 | 0.214177 | 0.0324063 | {"17": 0.21659213499645635, "29": 0.24530756036666548, "43": 0.1806300931577187} |
| SAR (complete-state implementation) | Reset parameters only | 4 | ba | uci_internal_fixed | ece15 | 3 | 0.0789634 | 0.0153973 | {"17": 0.0805681462977542, "29": 0.0934954526290433, "43": 0.0628265272126512} |
| SAR (complete-state implementation) | Reset parameters only | 4 | ba | uci_internal_fixed | seconds | 3 | 0.254651 | 0.0450082 | {"17": 0.27780965000420105, "29": 0.20277945000998435, "43": 0.28336495000257855} |
| SAR (complete-state implementation) | Reset parameters only | 4 | ba | uci_internal_fixed | updates | 3 | 16 | 0 | {"17": 16.0, "29": 16.0, "43": 16.0} |
| SAR (complete-state implementation) | Reset parameters only | 4 | ba | uci_internal_fixed | skipped | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters only | 4 | ba | uci_internal_fixed | recoveries | 3 | 10 | 1.32288 | {"17": 9.5, "29": 9.0, "43": 11.5} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | ab | uci_internal_fixed | accuracy | 3 | 0.861654 | 0.0181739 | {"17": 0.859375, "29": 0.8447265625, "43": 0.880859375} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | ab | uci_internal_fixed | nll | 3 | 0.513692 | 0.113486 | {"17": 0.5037000013167998, "29": 0.6318433801107537, "43": 0.4055330613767488} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | ab | uci_internal_fixed | brier | 3 | 0.214038 | 0.0325401 | {"17": 0.21654437269545612, "29": 0.2452522483772659, "43": 0.18031695420240773} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | ab | uci_internal_fixed | ece15 | 3 | 0.0789817 | 0.0153697 | {"17": 0.08057571605142086, "29": 0.0934922971484249, "43": 0.06287706964942585} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | ab | uci_internal_fixed | seconds | 3 | 0.212891 | 0.0270337 | {"17": 0.24406815000111232, "29": 0.195955999995931, "43": 0.19864900000538904} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | ab | uci_internal_fixed | updates | 3 | 16 | 0 | {"17": 16.0, "29": 16.0, "43": 16.0} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | ab | uci_internal_fixed | skipped | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | ab | uci_internal_fixed | recoveries | 3 | 8.5 | 0.5 | {"17": 9.0, "29": 8.5, "43": 8.0} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | ba | uci_internal_fixed | accuracy | 3 | 0.861654 | 0.0181739 | {"17": 0.859375, "29": 0.8447265625, "43": 0.880859375} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | ba | uci_internal_fixed | nll | 3 | 0.513692 | 0.113486 | {"17": 0.5037000013167998, "29": 0.6318433801107537, "43": 0.4055330613767488} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | ba | uci_internal_fixed | brier | 3 | 0.214038 | 0.0325401 | {"17": 0.21654437269545612, "29": 0.2452522483772659, "43": 0.18031695420240773} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | ba | uci_internal_fixed | ece15 | 3 | 0.0789817 | 0.0153697 | {"17": 0.08057571605142086, "29": 0.0934922971484249, "43": 0.06287706964942585} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | ba | uci_internal_fixed | seconds | 3 | 0.221195 | 0.0365611 | {"17": 0.26326514999527717, "29": 0.19711314999585733, "43": 0.20320630000060186} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | ba | uci_internal_fixed | updates | 3 | 16 | 0 | {"17": 16.0, "29": 16.0, "43": 16.0} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | ba | uci_internal_fixed | skipped | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | ba | uci_internal_fixed | recoveries | 3 | 8.5 | 0.5 | {"17": 9.0, "29": 8.5, "43": 8.0} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | ab | uci_internal_fixed | accuracy | 3 | 0.861654 | 0.0181739 | {"17": 0.859375, "29": 0.8447265625, "43": 0.880859375} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | ab | uci_internal_fixed | nll | 3 | 0.513692 | 0.113486 | {"17": 0.5037000013167998, "29": 0.6318433801107537, "43": 0.4055330613767488} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | ab | uci_internal_fixed | brier | 3 | 0.214038 | 0.0325401 | {"17": 0.21654437269545612, "29": 0.2452522483772659, "43": 0.18031695420240773} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | ab | uci_internal_fixed | ece15 | 3 | 0.0789817 | 0.0153697 | {"17": 0.08057571605142086, "29": 0.0934922971484249, "43": 0.06287706964942585} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | ab | uci_internal_fixed | seconds | 3 | 0.229526 | 0.0444106 | {"17": 0.22257830000307874, "29": 0.2770008000006782, "43": 0.18899859999510227} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | ab | uci_internal_fixed | updates | 3 | 16 | 0 | {"17": 16.0, "29": 16.0, "43": 16.0} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | ab | uci_internal_fixed | skipped | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | ab | uci_internal_fixed | recoveries | 3 | 8.5 | 0.5 | {"17": 9.0, "29": 8.5, "43": 8.0} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | ba | uci_internal_fixed | accuracy | 3 | 0.861654 | 0.0181739 | {"17": 0.859375, "29": 0.8447265625, "43": 0.880859375} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | ba | uci_internal_fixed | nll | 3 | 0.513692 | 0.113486 | {"17": 0.5037000013167998, "29": 0.6318433801107537, "43": 0.4055330613767488} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | ba | uci_internal_fixed | brier | 3 | 0.214038 | 0.0325401 | {"17": 0.21654437269545612, "29": 0.2452522483772659, "43": 0.18031695420240773} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | ba | uci_internal_fixed | ece15 | 3 | 0.0789817 | 0.0153697 | {"17": 0.08057571605142086, "29": 0.0934922971484249, "43": 0.06287706964942585} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | ba | uci_internal_fixed | seconds | 3 | 0.234399 | 0.0264404 | {"17": 0.22099930000695167, "29": 0.264856649991998, "43": 0.217341050003597} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | ba | uci_internal_fixed | updates | 3 | 16 | 0 | {"17": 16.0, "29": 16.0, "43": 16.0} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | ba | uci_internal_fixed | skipped | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | ba | uci_internal_fixed | recoveries | 3 | 8.5 | 0.5 | {"17": 9.0, "29": 8.5, "43": 8.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | ab | uci_internal_fixed | accuracy | 3 | 0.861328 | 0.0182437 | {"17": 0.8583984375, "29": 0.8447265625, "43": 0.880859375} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | ab | uci_internal_fixed | nll | 3 | 0.513887 | 0.112619 | {"17": 0.5041926299953787, "29": 0.6310400616530081, "43": 0.4064295110131153} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | ab | uci_internal_fixed | brier | 3 | 0.214144 | 0.032337 | {"17": 0.21668722440920746, "29": 0.24513497239790819, "43": 0.18061104522770854} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | ab | uci_internal_fixed | ece15 | 3 | 0.079252 | 0.0154196 | {"17": 0.0815261299385983, "29": 0.0934082766921714, "43": 0.06282163596435164} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | ab | uci_internal_fixed | seconds | 3 | 0.221881 | 0.0157394 | {"17": 0.21212780000496415, "29": 0.2400385000000824, "43": 0.21347640000021778} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | ab | uci_internal_fixed | updates | 3 | 16 | 0 | {"17": 16.0, "29": 16.0, "43": 16.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | ab | uci_internal_fixed | skipped | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | ab | uci_internal_fixed | recoveries | 3 | 12.8333 | 1.1547 | {"17": 11.5, "29": 13.5, "43": 13.5} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | ba | uci_internal_fixed | accuracy | 3 | 0.861328 | 0.0182437 | {"17": 0.8583984375, "29": 0.8447265625, "43": 0.880859375} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | ba | uci_internal_fixed | nll | 3 | 0.513836 | 0.112628 | {"17": 0.5040345386930848, "29": 0.6310450052676158, "43": 0.4064295110131153} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | ba | uci_internal_fixed | brier | 3 | 0.214131 | 0.0323359 | {"17": 0.21664665975108302, "29": 0.2451360079163803, "43": 0.18061104522770854} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | ba | uci_internal_fixed | ece15 | 3 | 0.0792528 | 0.0154196 | {"17": 0.08152878177321685, "29": 0.0934078474033383, "43": 0.06282163596435164} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | ba | uci_internal_fixed | seconds | 3 | 0.299368 | 0.0414021 | {"17": 0.3218889999989187, "29": 0.25158729999384377, "43": 0.3246282500040252} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | ba | uci_internal_fixed | updates | 3 | 16 | 0 | {"17": 16.0, "29": 16.0, "43": 16.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | ba | uci_internal_fixed | skipped | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | ba | uci_internal_fixed | recoveries | 3 | 12.3333 | 1.60728 | {"17": 10.5, "29": 13.0, "43": 13.5} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | ab | uci_internal_fixed | accuracy | 3 | 0.861328 | 0.0182437 | {"17": 0.8583984375, "29": 0.8447265625, "43": 0.880859375} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | ab | uci_internal_fixed | nll | 3 | 0.514106 | 0.113123 | {"17": 0.5037641486303785, "29": 0.6320447481779414, "43": 0.4065084928958825} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | ab | uci_internal_fixed | brier | 3 | 0.214172 | 0.0324058 | {"17": 0.21657729182921606, "29": 0.24530756036666548, "43": 0.1806300931577187} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | ab | uci_internal_fixed | ece15 | 3 | 0.0792869 | 0.015458 | {"17": 0.08153867859604605, "29": 0.0934954526290433, "43": 0.0628265272126512} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | ab | uci_internal_fixed | seconds | 3 | 0.226051 | 0.0440921 | {"17": 0.22911124999518506, "29": 0.18050880000373576, "43": 0.268533499998739} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | ab | uci_internal_fixed | updates | 3 | 16 | 0 | {"17": 16.0, "29": 16.0, "43": 16.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | ab | uci_internal_fixed | skipped | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | ab | uci_internal_fixed | recoveries | 3 | 10.1667 | 1.25831 | {"17": 10.0, "29": 9.0, "43": 11.5} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | ba | uci_internal_fixed | accuracy | 3 | 0.861654 | 0.0181739 | {"17": 0.859375, "29": 0.8447265625, "43": 0.880859375} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | ba | uci_internal_fixed | nll | 3 | 0.514135 | 0.113119 | {"17": 0.5038517687837049, "29": 0.6320447481779414, "43": 0.4065084928958825} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | ba | uci_internal_fixed | brier | 3 | 0.214177 | 0.0324063 | {"17": 0.21659213499645635, "29": 0.24530756036666548, "43": 0.1806300931577187} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | ba | uci_internal_fixed | ece15 | 3 | 0.0789634 | 0.0153973 | {"17": 0.0805681462977542, "29": 0.0934954526290433, "43": 0.0628265272126512} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | ba | uci_internal_fixed | seconds | 3 | 0.231818 | 0.0616042 | {"17": 0.21239335000427664, "29": 0.18226745000720251, "43": 0.3007932499895105} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | ba | uci_internal_fixed | updates | 3 | 16 | 0 | {"17": 16.0, "29": 16.0, "43": 16.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | ba | uci_internal_fixed | skipped | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | ba | uci_internal_fixed | recoveries | 3 | 10 | 1.32288 | {"17": 9.5, "29": 9.0, "43": 11.5} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | ab | uci_internal_fixed | accuracy | 3 | 0.861654 | 0.0181739 | {"17": 0.859375, "29": 0.8447265625, "43": 0.880859375} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | ab | uci_internal_fixed | nll | 3 | 0.513692 | 0.113486 | {"17": 0.5037000013167998, "29": 0.6318433801107537, "43": 0.4055330613767488} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | ab | uci_internal_fixed | brier | 3 | 0.214038 | 0.0325401 | {"17": 0.21654437269545612, "29": 0.2452522483772659, "43": 0.18031695420240773} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | ab | uci_internal_fixed | ece15 | 3 | 0.0789817 | 0.0153697 | {"17": 0.08057571605142086, "29": 0.0934922971484249, "43": 0.06287706964942585} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | ab | uci_internal_fixed | seconds | 3 | 0.204937 | 0.0252238 | {"17": 0.22926900000311434, "29": 0.2066336999996565, "43": 0.1789071000021067} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | ab | uci_internal_fixed | updates | 3 | 16 | 0 | {"17": 16.0, "29": 16.0, "43": 16.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | ab | uci_internal_fixed | skipped | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | ab | uci_internal_fixed | recoveries | 3 | 8.5 | 0.5 | {"17": 9.0, "29": 8.5, "43": 8.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | ba | uci_internal_fixed | accuracy | 3 | 0.861654 | 0.0181739 | {"17": 0.859375, "29": 0.8447265625, "43": 0.880859375} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | ba | uci_internal_fixed | nll | 3 | 0.513692 | 0.113486 | {"17": 0.5037000013167998, "29": 0.6318433801107537, "43": 0.4055330613767488} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | ba | uci_internal_fixed | brier | 3 | 0.214038 | 0.0325401 | {"17": 0.21654437269545612, "29": 0.2452522483772659, "43": 0.18031695420240773} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | ba | uci_internal_fixed | ece15 | 3 | 0.0789817 | 0.0153697 | {"17": 0.08057571605142086, "29": 0.0934922971484249, "43": 0.06287706964942585} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | ba | uci_internal_fixed | seconds | 3 | 0.203826 | 0.0177836 | {"17": 0.22041619999072276, "29": 0.206010050002078, "43": 0.1850508499992429} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | ba | uci_internal_fixed | updates | 3 | 16 | 0 | {"17": 16.0, "29": 16.0, "43": 16.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | ba | uci_internal_fixed | skipped | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | ba | uci_internal_fixed | recoveries | 3 | 8.5 | 0.5 | {"17": 9.0, "29": 8.5, "43": 8.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | ab | uci_internal_fixed | accuracy | 3 | 0.861654 | 0.0181739 | {"17": 0.859375, "29": 0.8447265625, "43": 0.880859375} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | ab | uci_internal_fixed | nll | 3 | 0.513692 | 0.113486 | {"17": 0.5037000013167998, "29": 0.6318433801107537, "43": 0.4055330613767488} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | ab | uci_internal_fixed | brier | 3 | 0.214038 | 0.0325401 | {"17": 0.21654437269545612, "29": 0.2452522483772659, "43": 0.18031695420240773} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | ab | uci_internal_fixed | ece15 | 3 | 0.0789817 | 0.0153697 | {"17": 0.08057571605142086, "29": 0.0934922971484249, "43": 0.06287706964942585} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | ab | uci_internal_fixed | seconds | 3 | 0.196087 | 0.0305571 | {"17": 0.2239207999882637, "29": 0.2009511500000371, "43": 0.1633901000022888} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | ab | uci_internal_fixed | updates | 3 | 16 | 0 | {"17": 16.0, "29": 16.0, "43": 16.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | ab | uci_internal_fixed | skipped | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | ab | uci_internal_fixed | recoveries | 3 | 8.5 | 0.5 | {"17": 9.0, "29": 8.5, "43": 8.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | ba | uci_internal_fixed | accuracy | 3 | 0.861654 | 0.0181739 | {"17": 0.859375, "29": 0.8447265625, "43": 0.880859375} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | ba | uci_internal_fixed | nll | 3 | 0.513692 | 0.113486 | {"17": 0.5037000013167998, "29": 0.6318433801107537, "43": 0.4055330613767488} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | ba | uci_internal_fixed | brier | 3 | 0.214038 | 0.0325401 | {"17": 0.21654437269545612, "29": 0.2452522483772659, "43": 0.18031695420240773} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | ba | uci_internal_fixed | ece15 | 3 | 0.0789817 | 0.0153697 | {"17": 0.08057571605142086, "29": 0.0934922971484249, "43": 0.06287706964942585} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | ba | uci_internal_fixed | seconds | 3 | 0.212119 | 0.0257838 | {"17": 0.23274769999989076, "29": 0.1832133499992778, "43": 0.22039719999884255} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | ba | uci_internal_fixed | updates | 3 | 16 | 0 | {"17": 16.0, "29": 16.0, "43": 16.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | ba | uci_internal_fixed | skipped | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | ba | uci_internal_fixed | recoveries | 3 | 8.5 | 0.5 | {"17": 9.0, "29": 8.5, "43": 8.0} |
| Source | Reset all declared state | 0 | ab | uci_internal_fixed | accuracy | 3 | 0.814128 | 0.0734719 | {"17": 0.8681640625, "29": 0.84375, "43": 0.73046875} |
| Source | Reset all declared state | 0 | ab | uci_internal_fixed | nll | 3 | 0.551879 | 0.189768 | {"17": 0.39369090117525873, "29": 0.49965523580356414, "43": 0.7622904980643} |
| Source | Reset all declared state | 0 | ab | uci_internal_fixed | brier | 3 | 0.272854 | 0.103787 | {"17": 0.19237211218524314, "29": 0.2361934600178015, "43": 0.3899955651400401} |
| Source | Reset all declared state | 0 | ab | uci_internal_fixed | ece15 | 3 | 0.0770746 | 0.0634826 | {"17": 0.04125574814589005, "29": 0.03959627423661675, "43": 0.1503717455661486} |
| Source | Reset all declared state | 0 | ab | uci_internal_fixed | seconds | 3 | 0.052373 | 0.00857983 | {"17": 0.04916629999934225, "29": 0.062094350003462695, "43": 0.04585844999382965} |
| Source | Reset all declared state | 0 | ab | uci_internal_fixed | updates | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Source | Reset all declared state | 0 | ab | uci_internal_fixed | skipped | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Source | Reset all declared state | 0 | ab | uci_internal_fixed | recoveries | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Source | Reset all declared state | 0 | ba | uci_internal_fixed | accuracy | 3 | 0.814128 | 0.0734719 | {"17": 0.8681640625, "29": 0.84375, "43": 0.73046875} |
| Source | Reset all declared state | 0 | ba | uci_internal_fixed | nll | 3 | 0.551879 | 0.189768 | {"17": 0.39369090117525873, "29": 0.49965523580356414, "43": 0.7622904980643} |
| Source | Reset all declared state | 0 | ba | uci_internal_fixed | brier | 3 | 0.272854 | 0.103787 | {"17": 0.19237211218524314, "29": 0.2361934600178015, "43": 0.3899955651400401} |
| Source | Reset all declared state | 0 | ba | uci_internal_fixed | ece15 | 3 | 0.0770746 | 0.0634826 | {"17": 0.04125574814589005, "29": 0.03959627423661675, "43": 0.1503717455661486} |
| Source | Reset all declared state | 0 | ba | uci_internal_fixed | seconds | 3 | 0.0575942 | 0.00932443 | {"17": 0.0635900499983108, "29": 0.062341199998627396, "43": 0.04685149999568235} |
| Source | Reset all declared state | 0 | ba | uci_internal_fixed | updates | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Source | Reset all declared state | 0 | ba | uci_internal_fixed | skipped | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Source | Reset all declared state | 0 | ba | uci_internal_fixed | recoveries | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Source | Reset all declared state | 4 | ab | uci_internal_fixed | accuracy | 3 | 0.814128 | 0.0734719 | {"17": 0.8681640625, "29": 0.84375, "43": 0.73046875} |
| Source | Reset all declared state | 4 | ab | uci_internal_fixed | nll | 3 | 0.551879 | 0.189768 | {"17": 0.39369090117525873, "29": 0.49965523580356414, "43": 0.7622904980643} |
| Source | Reset all declared state | 4 | ab | uci_internal_fixed | brier | 3 | 0.272854 | 0.103787 | {"17": 0.19237211218524314, "29": 0.2361934600178015, "43": 0.3899955651400401} |
| Source | Reset all declared state | 4 | ab | uci_internal_fixed | ece15 | 3 | 0.0770746 | 0.0634826 | {"17": 0.04125574814589005, "29": 0.03959627423661675, "43": 0.1503717455661486} |
| Source | Reset all declared state | 4 | ab | uci_internal_fixed | seconds | 3 | 0.0600619 | 0.0197511 | {"17": 0.049646749997918904, "29": 0.082840799994301, "43": 0.04769820000365135} |
| Source | Reset all declared state | 4 | ab | uci_internal_fixed | updates | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Source | Reset all declared state | 4 | ab | uci_internal_fixed | skipped | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Source | Reset all declared state | 4 | ab | uci_internal_fixed | recoveries | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Source | Reset all declared state | 4 | ba | uci_internal_fixed | accuracy | 3 | 0.814128 | 0.0734719 | {"17": 0.8681640625, "29": 0.84375, "43": 0.73046875} |
| Source | Reset all declared state | 4 | ba | uci_internal_fixed | nll | 3 | 0.551879 | 0.189768 | {"17": 0.39369090117525873, "29": 0.49965523580356414, "43": 0.7622904980643} |
| Source | Reset all declared state | 4 | ba | uci_internal_fixed | brier | 3 | 0.272854 | 0.103787 | {"17": 0.19237211218524314, "29": 0.2361934600178015, "43": 0.3899955651400401} |
| Source | Reset all declared state | 4 | ba | uci_internal_fixed | ece15 | 3 | 0.0770746 | 0.0634826 | {"17": 0.04125574814589005, "29": 0.03959627423661675, "43": 0.1503717455661486} |
| Source | Reset all declared state | 4 | ba | uci_internal_fixed | seconds | 3 | 0.0554751 | 0.0149866 | {"17": 0.047000749997096095, "29": 0.0727789999946253, "43": 0.04664565000712165} |
| Source | Reset all declared state | 4 | ba | uci_internal_fixed | updates | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Source | Reset all declared state | 4 | ba | uci_internal_fixed | skipped | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Source | Reset all declared state | 4 | ba | uci_internal_fixed | recoveries | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Source | No external reset | 0 | ab | uci_internal_fixed | accuracy | 3 | 0.814128 | 0.0734719 | {"17": 0.8681640625, "29": 0.84375, "43": 0.73046875} |
| Source | No external reset | 0 | ab | uci_internal_fixed | nll | 3 | 0.551879 | 0.189768 | {"17": 0.39369090117525873, "29": 0.49965523580356414, "43": 0.7622904980643} |
| Source | No external reset | 0 | ab | uci_internal_fixed | brier | 3 | 0.272854 | 0.103787 | {"17": 0.19237211218524314, "29": 0.2361934600178015, "43": 0.3899955651400401} |
| Source | No external reset | 0 | ab | uci_internal_fixed | ece15 | 3 | 0.0770746 | 0.0634826 | {"17": 0.04125574814589005, "29": 0.03959627423661675, "43": 0.1503717455661486} |
| Source | No external reset | 0 | ab | uci_internal_fixed | seconds | 3 | 0.0741483 | 0.00808119 | {"17": 0.0771564000024227, "29": 0.0802940000066882, "43": 0.0649944499964476} |
| Source | No external reset | 0 | ab | uci_internal_fixed | updates | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Source | No external reset | 0 | ab | uci_internal_fixed | skipped | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Source | No external reset | 0 | ab | uci_internal_fixed | recoveries | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Source | No external reset | 0 | ba | uci_internal_fixed | accuracy | 3 | 0.814128 | 0.0734719 | {"17": 0.8681640625, "29": 0.84375, "43": 0.73046875} |
| Source | No external reset | 0 | ba | uci_internal_fixed | nll | 3 | 0.551879 | 0.189768 | {"17": 0.39369090117525873, "29": 0.49965523580356414, "43": 0.7622904980643} |
| Source | No external reset | 0 | ba | uci_internal_fixed | brier | 3 | 0.272854 | 0.103787 | {"17": 0.19237211218524314, "29": 0.2361934600178015, "43": 0.3899955651400401} |
| Source | No external reset | 0 | ba | uci_internal_fixed | ece15 | 3 | 0.0770746 | 0.0634826 | {"17": 0.04125574814589005, "29": 0.03959627423661675, "43": 0.1503717455661486} |
| Source | No external reset | 0 | ba | uci_internal_fixed | seconds | 3 | 0.049766 | 0.00398169 | {"17": 0.049471350001112996, "29": 0.053886899993813096, "43": 0.0459399000028497} |
| Source | No external reset | 0 | ba | uci_internal_fixed | updates | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Source | No external reset | 0 | ba | uci_internal_fixed | skipped | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Source | No external reset | 0 | ba | uci_internal_fixed | recoveries | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Source | No external reset | 4 | ab | uci_internal_fixed | accuracy | 3 | 0.814128 | 0.0734719 | {"17": 0.8681640625, "29": 0.84375, "43": 0.73046875} |
| Source | No external reset | 4 | ab | uci_internal_fixed | nll | 3 | 0.551879 | 0.189768 | {"17": 0.39369090117525873, "29": 0.49965523580356414, "43": 0.7622904980643} |
| Source | No external reset | 4 | ab | uci_internal_fixed | brier | 3 | 0.272854 | 0.103787 | {"17": 0.19237211218524314, "29": 0.2361934600178015, "43": 0.3899955651400401} |
| Source | No external reset | 4 | ab | uci_internal_fixed | ece15 | 3 | 0.0770746 | 0.0634826 | {"17": 0.04125574814589005, "29": 0.03959627423661675, "43": 0.1503717455661486} |
| Source | No external reset | 4 | ab | uci_internal_fixed | seconds | 3 | 0.0633344 | 0.0130864 | {"17": 0.05032984999706965, "29": 0.06317239999771115, "43": 0.07650105000357141} |
| Source | No external reset | 4 | ab | uci_internal_fixed | updates | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Source | No external reset | 4 | ab | uci_internal_fixed | skipped | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Source | No external reset | 4 | ab | uci_internal_fixed | recoveries | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Source | No external reset | 4 | ba | uci_internal_fixed | accuracy | 3 | 0.814128 | 0.0734719 | {"17": 0.8681640625, "29": 0.84375, "43": 0.73046875} |
| Source | No external reset | 4 | ba | uci_internal_fixed | nll | 3 | 0.551879 | 0.189768 | {"17": 0.39369090117525873, "29": 0.49965523580356414, "43": 0.7622904980643} |
| Source | No external reset | 4 | ba | uci_internal_fixed | brier | 3 | 0.272854 | 0.103787 | {"17": 0.19237211218524314, "29": 0.2361934600178015, "43": 0.3899955651400401} |
| Source | No external reset | 4 | ba | uci_internal_fixed | ece15 | 3 | 0.0770746 | 0.0634826 | {"17": 0.04125574814589005, "29": 0.03959627423661675, "43": 0.1503717455661486} |
| Source | No external reset | 4 | ba | uci_internal_fixed | seconds | 3 | 0.0551323 | 0.0135134 | {"17": 0.04844634999608385, "29": 0.07068535000144036, "43": 0.046265199998742845} |
| Source | No external reset | 4 | ba | uci_internal_fixed | updates | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Source | No external reset | 4 | ba | uci_internal_fixed | skipped | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Source | No external reset | 4 | ba | uci_internal_fixed | recoveries | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset all declared state | 0 | ab | uci_internal_fixed | accuracy | 3 | 0.861654 | 0.0181739 | {"17": 0.859375, "29": 0.8447265625, "43": 0.880859375} |
| Tent | Reset all declared state | 0 | ab | uci_internal_fixed | nll | 3 | 0.514146 | 0.114013 | {"17": 0.5038094188406126, "29": 0.6329752572847591, "43": 0.4056525191548072} |
| Tent | Reset all declared state | 0 | ab | uci_internal_fixed | brier | 3 | 0.214142 | 0.0326466 | {"17": 0.21656771148689508, "29": 0.24550775070835953, "43": 0.1803498760320491} |
| Tent | Reset all declared state | 0 | ab | uci_internal_fixed | ece15 | 3 | 0.0789993 | 0.01539 | {"17": 0.08059263206845049, "29": 0.09353063621526654, "43": 0.06287464072694365} |
| Tent | Reset all declared state | 0 | ab | uci_internal_fixed | seconds | 3 | 0.126562 | 0.0311771 | {"17": 0.11462760000722474, "29": 0.16194340000947705, "43": 0.1031151999995927} |
| Tent | Reset all declared state | 0 | ab | uci_internal_fixed | updates | 3 | 16 | 0 | {"17": 16.0, "29": 16.0, "43": 16.0} |
| Tent | Reset all declared state | 0 | ab | uci_internal_fixed | skipped | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset all declared state | 0 | ab | uci_internal_fixed | recoveries | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset all declared state | 0 | ba | uci_internal_fixed | accuracy | 3 | 0.861654 | 0.0181739 | {"17": 0.859375, "29": 0.8447265625, "43": 0.880859375} |
| Tent | Reset all declared state | 0 | ba | uci_internal_fixed | nll | 3 | 0.514146 | 0.114013 | {"17": 0.5038094188406126, "29": 0.6329752572847591, "43": 0.4056525191548072} |
| Tent | Reset all declared state | 0 | ba | uci_internal_fixed | brier | 3 | 0.214142 | 0.0326466 | {"17": 0.21656771148689508, "29": 0.24550775070835953, "43": 0.1803498760320491} |
| Tent | Reset all declared state | 0 | ba | uci_internal_fixed | ece15 | 3 | 0.0789993 | 0.01539 | {"17": 0.08059263206845049, "29": 0.09353063621526654, "43": 0.06287464072694365} |
| Tent | Reset all declared state | 0 | ba | uci_internal_fixed | seconds | 3 | 0.11737 | 0.0238673 | {"17": 0.10802210000110785, "29": 0.1444962999958079, "43": 0.0995915500025148} |
| Tent | Reset all declared state | 0 | ba | uci_internal_fixed | updates | 3 | 16 | 0 | {"17": 16.0, "29": 16.0, "43": 16.0} |
| Tent | Reset all declared state | 0 | ba | uci_internal_fixed | skipped | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset all declared state | 0 | ba | uci_internal_fixed | recoveries | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset all declared state | 4 | ab | uci_internal_fixed | accuracy | 3 | 0.861654 | 0.0181739 | {"17": 0.859375, "29": 0.8447265625, "43": 0.880859375} |
| Tent | Reset all declared state | 4 | ab | uci_internal_fixed | nll | 3 | 0.514146 | 0.114013 | {"17": 0.5038094188406126, "29": 0.6329752572847591, "43": 0.4056525191548072} |
| Tent | Reset all declared state | 4 | ab | uci_internal_fixed | brier | 3 | 0.214142 | 0.0326466 | {"17": 0.21656771148689508, "29": 0.24550775070835953, "43": 0.1803498760320491} |
| Tent | Reset all declared state | 4 | ab | uci_internal_fixed | ece15 | 3 | 0.0789993 | 0.01539 | {"17": 0.08059263206845049, "29": 0.09353063621526654, "43": 0.06287464072694365} |
| Tent | Reset all declared state | 4 | ab | uci_internal_fixed | seconds | 3 | 0.110205 | 0.014093 | {"17": 0.10785905000375345, "29": 0.1253233500028727, "43": 0.09743159999925405} |
| Tent | Reset all declared state | 4 | ab | uci_internal_fixed | updates | 3 | 16 | 0 | {"17": 16.0, "29": 16.0, "43": 16.0} |
| Tent | Reset all declared state | 4 | ab | uci_internal_fixed | skipped | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset all declared state | 4 | ab | uci_internal_fixed | recoveries | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset all declared state | 4 | ba | uci_internal_fixed | accuracy | 3 | 0.861654 | 0.0181739 | {"17": 0.859375, "29": 0.8447265625, "43": 0.880859375} |
| Tent | Reset all declared state | 4 | ba | uci_internal_fixed | nll | 3 | 0.514146 | 0.114013 | {"17": 0.5038094188406126, "29": 0.6329752572847591, "43": 0.4056525191548072} |
| Tent | Reset all declared state | 4 | ba | uci_internal_fixed | brier | 3 | 0.214142 | 0.0326466 | {"17": 0.21656771148689508, "29": 0.24550775070835953, "43": 0.1803498760320491} |
| Tent | Reset all declared state | 4 | ba | uci_internal_fixed | ece15 | 3 | 0.0789993 | 0.01539 | {"17": 0.08059263206845049, "29": 0.09353063621526654, "43": 0.06287464072694365} |
| Tent | Reset all declared state | 4 | ba | uci_internal_fixed | seconds | 3 | 0.106372 | 0.0114428 | {"17": 0.10677725000277855, "29": 0.1176062999948044, "43": 0.09473145000083605} |
| Tent | Reset all declared state | 4 | ba | uci_internal_fixed | updates | 3 | 16 | 0 | {"17": 16.0, "29": 16.0, "43": 16.0} |
| Tent | Reset all declared state | 4 | ba | uci_internal_fixed | skipped | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset all declared state | 4 | ba | uci_internal_fixed | recoveries | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset auxiliary state only | 0 | ab | uci_internal_fixed | accuracy | 3 | 0.861979 | 0.0181213 | {"17": 0.8603515625, "29": 0.8447265625, "43": 0.880859375} |
| Tent | Reset auxiliary state only | 0 | ab | uci_internal_fixed | nll | 3 | 0.513931 | 0.113576 | {"17": 0.5033290309695039, "29": 0.6324358882615164, "43": 0.4060272281629106} |
| Tent | Reset auxiliary state only | 0 | ab | uci_internal_fixed | brier | 3 | 0.214068 | 0.0325313 | {"17": 0.2164064086256196, "29": 0.24536689332633063, "43": 0.18043041760661999} |
| Tent | Reset auxiliary state only | 0 | ab | uci_internal_fixed | ece15 | 3 | 0.079346 | 0.0153072 | {"17": 0.08018694152575101, "29": 0.0942154772202387, "43": 0.0636356856401231} |
| Tent | Reset auxiliary state only | 0 | ab | uci_internal_fixed | seconds | 3 | 0.132635 | 0.038592 | {"17": 0.12681834999966665, "29": 0.17380579999735346, "43": 0.09728230000473556} |
| Tent | Reset auxiliary state only | 0 | ab | uci_internal_fixed | updates | 3 | 16 | 0 | {"17": 16.0, "29": 16.0, "43": 16.0} |
| Tent | Reset auxiliary state only | 0 | ab | uci_internal_fixed | skipped | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset auxiliary state only | 0 | ab | uci_internal_fixed | recoveries | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset auxiliary state only | 0 | ba | uci_internal_fixed | accuracy | 3 | 0.861654 | 0.0181739 | {"17": 0.859375, "29": 0.8447265625, "43": 0.880859375} |
| Tent | Reset auxiliary state only | 0 | ba | uci_internal_fixed | nll | 3 | 0.513905 | 0.113605 | {"17": 0.5033519807094681, "29": 0.6324180885745352, "43": 0.4059435949477067} |
| Tent | Reset auxiliary state only | 0 | ba | uci_internal_fixed | brier | 3 | 0.214066 | 0.0325451 | {"17": 0.2164203477169167, "29": 0.2453695265543725, "43": 0.180407139041165} |
| Tent | Reset auxiliary state only | 0 | ba | uci_internal_fixed | ece15 | 3 | 0.0794973 | 0.0153302 | {"17": 0.08066415532717605, "29": 0.09421069390531489, "43": 0.06361702841265371} |
| Tent | Reset auxiliary state only | 0 | ba | uci_internal_fixed | seconds | 3 | 0.126695 | 0.0441129 | {"17": 0.11892699998861644, "29": 0.17417534999549383, "43": 0.08698130000266241} |
| Tent | Reset auxiliary state only | 0 | ba | uci_internal_fixed | updates | 3 | 16 | 0 | {"17": 16.0, "29": 16.0, "43": 16.0} |
| Tent | Reset auxiliary state only | 0 | ba | uci_internal_fixed | skipped | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset auxiliary state only | 0 | ba | uci_internal_fixed | recoveries | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset auxiliary state only | 4 | ab | uci_internal_fixed | accuracy | 3 | 0.862305 | 0.0180862 | {"17": 0.861328125, "29": 0.8447265625, "43": 0.880859375} |
| Tent | Reset auxiliary state only | 4 | ab | uci_internal_fixed | nll | 3 | 0.514415 | 0.115328 | {"17": 0.5031103634542742, "29": 0.6349798384941314, "43": 0.4051554538598498} |
| Tent | Reset auxiliary state only | 4 | ab | uci_internal_fixed | brier | 3 | 0.214122 | 0.0329429 | {"17": 0.21632614900073266, "29": 0.24590809641769834, "43": 0.18013291708167545} |
| Tent | Reset auxiliary state only | 4 | ab | uci_internal_fixed | ece15 | 3 | 0.0791961 | 0.0146778 | {"17": 0.08104205295830551, "29": 0.09286363632924885, "43": 0.06368272313596515} |
| Tent | Reset auxiliary state only | 4 | ab | uci_internal_fixed | seconds | 3 | 0.114857 | 0.0150962 | {"17": 0.12714155000139724, "29": 0.1194250499902409, "43": 0.09800430000177585} |
| Tent | Reset auxiliary state only | 4 | ab | uci_internal_fixed | updates | 3 | 16 | 0 | {"17": 16.0, "29": 16.0, "43": 16.0} |
| Tent | Reset auxiliary state only | 4 | ab | uci_internal_fixed | skipped | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset auxiliary state only | 4 | ab | uci_internal_fixed | recoveries | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset auxiliary state only | 4 | ba | uci_internal_fixed | accuracy | 3 | 0.862305 | 0.0180862 | {"17": 0.861328125, "29": 0.8447265625, "43": 0.880859375} |
| Tent | Reset auxiliary state only | 4 | ba | uci_internal_fixed | nll | 3 | 0.514398 | 0.115346 | {"17": 0.5031273246395818, "29": 0.6349653131028378, "43": 0.4051011601661464} |
| Tent | Reset auxiliary state only | 4 | ba | uci_internal_fixed | brier | 3 | 0.214121 | 0.0329513 | {"17": 0.21633570552013445, "29": 0.24590875879253754, "43": 0.1801179342450303} |
| Tent | Reset auxiliary state only | 4 | ba | uci_internal_fixed | ece15 | 3 | 0.0791877 | 0.0146805 | {"17": 0.0810362302589976, "29": 0.09285647973037535, "43": 0.06367046954143735} |
| Tent | Reset auxiliary state only | 4 | ba | uci_internal_fixed | seconds | 3 | 0.111634 | 0.0122592 | {"17": 0.12067484999715809, "29": 0.11654570000246164, "43": 0.09767995000584045} |
| Tent | Reset auxiliary state only | 4 | ba | uci_internal_fixed | updates | 3 | 16 | 0 | {"17": 16.0, "29": 16.0, "43": 16.0} |
| Tent | Reset auxiliary state only | 4 | ba | uci_internal_fixed | skipped | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset auxiliary state only | 4 | ba | uci_internal_fixed | recoveries | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | No external reset | 0 | ab | uci_internal_fixed | accuracy | 3 | 0.861979 | 0.0181213 | {"17": 0.8603515625, "29": 0.8447265625, "43": 0.880859375} |
| Tent | No external reset | 0 | ab | uci_internal_fixed | nll | 3 | 0.513931 | 0.113576 | {"17": 0.5033290309695039, "29": 0.6324358882615164, "43": 0.4060272281629106} |
| Tent | No external reset | 0 | ab | uci_internal_fixed | brier | 3 | 0.214068 | 0.0325313 | {"17": 0.2164064086256196, "29": 0.24536689332633063, "43": 0.18043041760661999} |
| Tent | No external reset | 0 | ab | uci_internal_fixed | ece15 | 3 | 0.079346 | 0.0153072 | {"17": 0.08018694152575101, "29": 0.0942154772202387, "43": 0.0636356856401231} |
| Tent | No external reset | 0 | ab | uci_internal_fixed | seconds | 3 | 0.147505 | 0.0417999 | {"17": 0.17896225000004046, "29": 0.1634796500002266, "43": 0.10007389999373115} |
| Tent | No external reset | 0 | ab | uci_internal_fixed | updates | 3 | 16 | 0 | {"17": 16.0, "29": 16.0, "43": 16.0} |
| Tent | No external reset | 0 | ab | uci_internal_fixed | skipped | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | No external reset | 0 | ab | uci_internal_fixed | recoveries | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | No external reset | 0 | ba | uci_internal_fixed | accuracy | 3 | 0.861654 | 0.0181739 | {"17": 0.859375, "29": 0.8447265625, "43": 0.880859375} |
| Tent | No external reset | 0 | ba | uci_internal_fixed | nll | 3 | 0.513905 | 0.113605 | {"17": 0.5033519807094681, "29": 0.6324180885745352, "43": 0.4059435949477067} |
| Tent | No external reset | 0 | ba | uci_internal_fixed | brier | 3 | 0.214066 | 0.0325451 | {"17": 0.2164203477169167, "29": 0.2453695265543725, "43": 0.180407139041165} |
| Tent | No external reset | 0 | ba | uci_internal_fixed | ece15 | 3 | 0.0794973 | 0.0153302 | {"17": 0.08066415532717605, "29": 0.09421069390531489, "43": 0.06361702841265371} |
| Tent | No external reset | 0 | ba | uci_internal_fixed | seconds | 3 | 0.125341 | 0.0330946 | {"17": 0.1248303000029409, "29": 0.15868780000164404, "43": 0.09250454999710195} |
| Tent | No external reset | 0 | ba | uci_internal_fixed | updates | 3 | 16 | 0 | {"17": 16.0, "29": 16.0, "43": 16.0} |
| Tent | No external reset | 0 | ba | uci_internal_fixed | skipped | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | No external reset | 0 | ba | uci_internal_fixed | recoveries | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | No external reset | 4 | ab | uci_internal_fixed | accuracy | 3 | 0.862305 | 0.0180862 | {"17": 0.861328125, "29": 0.8447265625, "43": 0.880859375} |
| Tent | No external reset | 4 | ab | uci_internal_fixed | nll | 3 | 0.514415 | 0.115328 | {"17": 0.5031103634542742, "29": 0.6349798384941314, "43": 0.4051554538598498} |
| Tent | No external reset | 4 | ab | uci_internal_fixed | brier | 3 | 0.214122 | 0.0329429 | {"17": 0.21632614900073266, "29": 0.24590809641769834, "43": 0.18013291708167545} |
| Tent | No external reset | 4 | ab | uci_internal_fixed | ece15 | 3 | 0.0791961 | 0.0146778 | {"17": 0.08104205295830551, "29": 0.09286363632924885, "43": 0.06368272313596515} |
| Tent | No external reset | 4 | ab | uci_internal_fixed | seconds | 3 | 0.124795 | 0.0213656 | {"17": 0.11124435000238006, "29": 0.14942444999905996, "43": 0.11371575000521256} |
| Tent | No external reset | 4 | ab | uci_internal_fixed | updates | 3 | 16 | 0 | {"17": 16.0, "29": 16.0, "43": 16.0} |
| Tent | No external reset | 4 | ab | uci_internal_fixed | skipped | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | No external reset | 4 | ab | uci_internal_fixed | recoveries | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | No external reset | 4 | ba | uci_internal_fixed | accuracy | 3 | 0.862305 | 0.0180862 | {"17": 0.861328125, "29": 0.8447265625, "43": 0.880859375} |
| Tent | No external reset | 4 | ba | uci_internal_fixed | nll | 3 | 0.514398 | 0.115346 | {"17": 0.5031273246395818, "29": 0.6349653131028378, "43": 0.4051011601661464} |
| Tent | No external reset | 4 | ba | uci_internal_fixed | brier | 3 | 0.214121 | 0.0329513 | {"17": 0.21633570552013445, "29": 0.24590875879253754, "43": 0.1801179342450303} |
| Tent | No external reset | 4 | ba | uci_internal_fixed | ece15 | 3 | 0.0791877 | 0.0146805 | {"17": 0.0810362302589976, "29": 0.09285647973037535, "43": 0.06367046954143735} |
| Tent | No external reset | 4 | ba | uci_internal_fixed | seconds | 3 | 0.147506 | 0.0416958 | {"17": 0.1098671500003547, "29": 0.14032600000064116, "43": 0.19232614999782519} |
| Tent | No external reset | 4 | ba | uci_internal_fixed | updates | 3 | 16 | 0 | {"17": 16.0, "29": 16.0, "43": 16.0} |
| Tent | No external reset | 4 | ba | uci_internal_fixed | skipped | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | No external reset | 4 | ba | uci_internal_fixed | recoveries | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset optimizer only | 0 | ab | uci_internal_fixed | accuracy | 3 | 0.861979 | 0.0181213 | {"17": 0.8603515625, "29": 0.8447265625, "43": 0.880859375} |
| Tent | Reset optimizer only | 0 | ab | uci_internal_fixed | nll | 3 | 0.514021 | 0.113748 | {"17": 0.5034037528019594, "29": 0.6327053429929421, "43": 0.4059531950813955} |
| Tent | Reset optimizer only | 0 | ab | uci_internal_fixed | brier | 3 | 0.214088 | 0.0325677 | {"17": 0.2164270884034694, "29": 0.2454230394064824, "43": 0.1804137895182144} |
| Tent | Reset optimizer only | 0 | ab | uci_internal_fixed | ece15 | 3 | 0.0791166 | 0.01565 | {"17": 0.08017419272469095, "29": 0.09421101263479015, "43": 0.0629645701973476} |
| Tent | Reset optimizer only | 0 | ab | uci_internal_fixed | seconds | 3 | 0.127872 | 0.0420394 | {"17": 0.10725935000664316, "29": 0.17623965000530006, "43": 0.1001175999990664} |
| Tent | Reset optimizer only | 0 | ab | uci_internal_fixed | updates | 3 | 16 | 0 | {"17": 16.0, "29": 16.0, "43": 16.0} |
| Tent | Reset optimizer only | 0 | ab | uci_internal_fixed | skipped | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset optimizer only | 0 | ab | uci_internal_fixed | recoveries | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset optimizer only | 0 | ba | uci_internal_fixed | accuracy | 3 | 0.861654 | 0.0181739 | {"17": 0.859375, "29": 0.8447265625, "43": 0.880859375} |
| Tent | Reset optimizer only | 0 | ba | uci_internal_fixed | nll | 3 | 0.513958 | 0.113819 | {"17": 0.5034433210868962, "29": 0.6326695898581236, "43": 0.4057608183727183} |
| Tent | Reset optimizer only | 0 | ba | uci_internal_fixed | brier | 3 | 0.214083 | 0.0325938 | {"17": 0.2164548316463341, "29": 0.24542670046290604, "43": 0.1803686088299253} |
| Tent | Reset optimizer only | 0 | ba | uci_internal_fixed | ece15 | 3 | 0.0792563 | 0.0150344 | {"17": 0.0806380824998738, "29": 0.0935521895726693, "43": 0.06357876821543634} |
| Tent | Reset optimizer only | 0 | ba | uci_internal_fixed | seconds | 3 | 0.120687 | 0.029431 | {"17": 0.1122306500037666, "29": 0.153420949995052, "43": 0.0964105499951983} |
| Tent | Reset optimizer only | 0 | ba | uci_internal_fixed | updates | 3 | 16 | 0 | {"17": 16.0, "29": 16.0, "43": 16.0} |
| Tent | Reset optimizer only | 0 | ba | uci_internal_fixed | skipped | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset optimizer only | 0 | ba | uci_internal_fixed | recoveries | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset optimizer only | 4 | ab | uci_internal_fixed | accuracy | 3 | 0.862305 | 0.0180862 | {"17": 0.861328125, "29": 0.8447265625, "43": 0.880859375} |
| Tent | Reset optimizer only | 4 | ab | uci_internal_fixed | nll | 3 | 0.514056 | 0.1142 | {"17": 0.5032504527299361, "29": 0.6332747089410309, "43": 0.4056431411363059} |
| Tent | Reset optimizer only | 4 | ab | uci_internal_fixed | brier | 3 | 0.214076 | 0.03268 | {"17": 0.21637771653046245, "29": 0.24554409056628054, "43": 0.18030578042063886} |
| Tent | Reset optimizer only | 4 | ab | uci_internal_fixed | ece15 | 3 | 0.0789856 | 0.015079 | {"17": 0.0810193130455, "29": 0.09294454274194876, "43": 0.06299301683103435} |
| Tent | Reset optimizer only | 4 | ab | uci_internal_fixed | seconds | 3 | 0.134044 | 0.0313724 | {"17": 0.1645694999970146, "29": 0.13567520000651712, "43": 0.10188835000008105} |
| Tent | Reset optimizer only | 4 | ab | uci_internal_fixed | updates | 3 | 16 | 0 | {"17": 16.0, "29": 16.0, "43": 16.0} |
| Tent | Reset optimizer only | 4 | ab | uci_internal_fixed | skipped | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset optimizer only | 4 | ab | uci_internal_fixed | recoveries | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset optimizer only | 4 | ba | uci_internal_fixed | accuracy | 3 | 0.862305 | 0.0180862 | {"17": 0.861328125, "29": 0.8447265625, "43": 0.880859375} |
| Tent | Reset optimizer only | 4 | ba | uci_internal_fixed | nll | 3 | 0.514014 | 0.114246 | {"17": 0.5032762370676905, "29": 0.6332507321005663, "43": 0.40551609283757867} |
| Tent | Reset optimizer only | 4 | ba | uci_internal_fixed | brier | 3 | 0.214073 | 0.0326971 | {"17": 0.2163957223377167, "29": 0.24554609486477147, "43": 0.18027586789803043} |
| Tent | Reset optimizer only | 4 | ba | uci_internal_fixed | ece15 | 3 | 0.0791894 | 0.0147442 | {"17": 0.08100778344309605, "29": 0.0929401153655665, "43": 0.0636203669891081} |
| Tent | Reset optimizer only | 4 | ba | uci_internal_fixed | seconds | 3 | 0.123175 | 0.0248282 | {"17": 0.1432622499996796, "29": 0.1308464999965508, "43": 0.0954165999937686} |
| Tent | Reset optimizer only | 4 | ba | uci_internal_fixed | updates | 3 | 16 | 0 | {"17": 16.0, "29": 16.0, "43": 16.0} |
| Tent | Reset optimizer only | 4 | ba | uci_internal_fixed | skipped | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset optimizer only | 4 | ba | uci_internal_fixed | recoveries | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset optimizer + auxiliary state | 0 | ab | uci_internal_fixed | accuracy | 3 | 0.861979 | 0.0181213 | {"17": 0.8603515625, "29": 0.8447265625, "43": 0.880859375} |
| Tent | Reset optimizer + auxiliary state | 0 | ab | uci_internal_fixed | nll | 3 | 0.514021 | 0.113748 | {"17": 0.5034037528019594, "29": 0.6327053429929421, "43": 0.4059531950813955} |
| Tent | Reset optimizer + auxiliary state | 0 | ab | uci_internal_fixed | brier | 3 | 0.214088 | 0.0325677 | {"17": 0.2164270884034694, "29": 0.2454230394064824, "43": 0.1804137895182144} |
| Tent | Reset optimizer + auxiliary state | 0 | ab | uci_internal_fixed | ece15 | 3 | 0.0791166 | 0.01565 | {"17": 0.08017419272469095, "29": 0.09421101263479015, "43": 0.0629645701973476} |
| Tent | Reset optimizer + auxiliary state | 0 | ab | uci_internal_fixed | seconds | 3 | 0.147242 | 0.0398146 | {"17": 0.14443249999749241, "29": 0.1883865999989211, "43": 0.10890610000205919} |
| Tent | Reset optimizer + auxiliary state | 0 | ab | uci_internal_fixed | updates | 3 | 16 | 0 | {"17": 16.0, "29": 16.0, "43": 16.0} |
| Tent | Reset optimizer + auxiliary state | 0 | ab | uci_internal_fixed | skipped | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset optimizer + auxiliary state | 0 | ab | uci_internal_fixed | recoveries | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset optimizer + auxiliary state | 0 | ba | uci_internal_fixed | accuracy | 3 | 0.861654 | 0.0181739 | {"17": 0.859375, "29": 0.8447265625, "43": 0.880859375} |
| Tent | Reset optimizer + auxiliary state | 0 | ba | uci_internal_fixed | nll | 3 | 0.513958 | 0.113819 | {"17": 0.5034433210868962, "29": 0.6326695898581236, "43": 0.4057608183727183} |
| Tent | Reset optimizer + auxiliary state | 0 | ba | uci_internal_fixed | brier | 3 | 0.214083 | 0.0325938 | {"17": 0.2164548316463341, "29": 0.24542670046290604, "43": 0.1803686088299253} |
| Tent | Reset optimizer + auxiliary state | 0 | ba | uci_internal_fixed | ece15 | 3 | 0.0792563 | 0.0150344 | {"17": 0.0806380824998738, "29": 0.0935521895726693, "43": 0.06357876821543634} |
| Tent | Reset optimizer + auxiliary state | 0 | ba | uci_internal_fixed | seconds | 3 | 0.116762 | 0.0257361 | {"17": 0.10916369999904416, "29": 0.1454422500028158, "43": 0.09568110000691374} |
| Tent | Reset optimizer + auxiliary state | 0 | ba | uci_internal_fixed | updates | 3 | 16 | 0 | {"17": 16.0, "29": 16.0, "43": 16.0} |
| Tent | Reset optimizer + auxiliary state | 0 | ba | uci_internal_fixed | skipped | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset optimizer + auxiliary state | 0 | ba | uci_internal_fixed | recoveries | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset optimizer + auxiliary state | 4 | ab | uci_internal_fixed | accuracy | 3 | 0.862305 | 0.0180862 | {"17": 0.861328125, "29": 0.8447265625, "43": 0.880859375} |
| Tent | Reset optimizer + auxiliary state | 4 | ab | uci_internal_fixed | nll | 3 | 0.514056 | 0.1142 | {"17": 0.5032504527299361, "29": 0.6332747089410309, "43": 0.4056431411363059} |
| Tent | Reset optimizer + auxiliary state | 4 | ab | uci_internal_fixed | brier | 3 | 0.214076 | 0.03268 | {"17": 0.21637771653046245, "29": 0.24554409056628054, "43": 0.18030578042063886} |
| Tent | Reset optimizer + auxiliary state | 4 | ab | uci_internal_fixed | ece15 | 3 | 0.0789856 | 0.015079 | {"17": 0.0810193130455, "29": 0.09294454274194876, "43": 0.06299301683103435} |
| Tent | Reset optimizer + auxiliary state | 4 | ab | uci_internal_fixed | seconds | 3 | 0.109525 | 0.00375295 | {"17": 0.10730494999734215, "29": 0.11385785000311435, "43": 0.1074114500006544} |
| Tent | Reset optimizer + auxiliary state | 4 | ab | uci_internal_fixed | updates | 3 | 16 | 0 | {"17": 16.0, "29": 16.0, "43": 16.0} |
| Tent | Reset optimizer + auxiliary state | 4 | ab | uci_internal_fixed | skipped | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset optimizer + auxiliary state | 4 | ab | uci_internal_fixed | recoveries | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset optimizer + auxiliary state | 4 | ba | uci_internal_fixed | accuracy | 3 | 0.862305 | 0.0180862 | {"17": 0.861328125, "29": 0.8447265625, "43": 0.880859375} |
| Tent | Reset optimizer + auxiliary state | 4 | ba | uci_internal_fixed | nll | 3 | 0.514014 | 0.114246 | {"17": 0.5032762370676905, "29": 0.6332507321005663, "43": 0.40551609283757867} |
| Tent | Reset optimizer + auxiliary state | 4 | ba | uci_internal_fixed | brier | 3 | 0.214073 | 0.0326971 | {"17": 0.2163957223377167, "29": 0.24554609486477147, "43": 0.18027586789803043} |
| Tent | Reset optimizer + auxiliary state | 4 | ba | uci_internal_fixed | ece15 | 3 | 0.0791894 | 0.0147442 | {"17": 0.08100778344309605, "29": 0.0929401153655665, "43": 0.0636203669891081} |
| Tent | Reset optimizer + auxiliary state | 4 | ba | uci_internal_fixed | seconds | 3 | 0.106365 | 0.0107283 | {"17": 0.1129652999952668, "29": 0.11214374999690335, "43": 0.0939862000086577} |
| Tent | Reset optimizer + auxiliary state | 4 | ba | uci_internal_fixed | updates | 3 | 16 | 0 | {"17": 16.0, "29": 16.0, "43": 16.0} |
| Tent | Reset optimizer + auxiliary state | 4 | ba | uci_internal_fixed | skipped | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset optimizer + auxiliary state | 4 | ba | uci_internal_fixed | recoveries | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters only | 0 | ab | uci_internal_fixed | accuracy | 3 | 0.861654 | 0.0181739 | {"17": 0.859375, "29": 0.8447265625, "43": 0.880859375} |
| Tent | Reset parameters only | 0 | ab | uci_internal_fixed | nll | 3 | 0.514055 | 0.11384 | {"17": 0.5037357180248052, "29": 0.6327035834352337, "43": 0.4057255673288713} |
| Tent | Reset parameters only | 0 | ab | uci_internal_fixed | brier | 3 | 0.214121 | 0.03261 | {"17": 0.21654701220291023, "29": 0.24545066349121644, "43": 0.18036610327834152} |
| Tent | Reset parameters only | 0 | ab | uci_internal_fixed | ece15 | 3 | 0.0790121 | 0.0153827 | {"17": 0.0806069918029438, "29": 0.0935352071896381, "43": 0.06289404616470935} |
| Tent | Reset parameters only | 0 | ab | uci_internal_fixed | seconds | 3 | 0.128546 | 0.0357309 | {"17": 0.1087472500003059, "29": 0.16979335000360152, "43": 0.107097000000067} |
| Tent | Reset parameters only | 0 | ab | uci_internal_fixed | updates | 3 | 16 | 0 | {"17": 16.0, "29": 16.0, "43": 16.0} |
| Tent | Reset parameters only | 0 | ab | uci_internal_fixed | skipped | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters only | 0 | ab | uci_internal_fixed | recoveries | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters only | 0 | ba | uci_internal_fixed | accuracy | 3 | 0.861654 | 0.0181739 | {"17": 0.859375, "29": 0.8447265625, "43": 0.880859375} |
| Tent | Reset parameters only | 0 | ba | uci_internal_fixed | nll | 3 | 0.514092 | 0.113798 | {"17": 0.5037222330867153, "29": 0.6327195273069306, "43": 0.4058329529956203} |
| Tent | Reset parameters only | 0 | ba | uci_internal_fixed | brier | 3 | 0.214124 | 0.0325978 | {"17": 0.21653407000510672, "29": 0.2454492569083861, "43": 0.1803874888047333} |
| Tent | Reset parameters only | 0 | ba | uci_internal_fixed | ece15 | 3 | 0.0790231 | 0.0153754 | {"17": 0.08061911659979434, "29": 0.09353822668981421, "43": 0.06291200327538955} |
| Tent | Reset parameters only | 0 | ba | uci_internal_fixed | seconds | 3 | 0.144112 | 0.0661192 | {"17": 0.11347540000133445, "29": 0.2199920999992173, "43": 0.0988671500017517} |
| Tent | Reset parameters only | 0 | ba | uci_internal_fixed | updates | 3 | 16 | 0 | {"17": 16.0, "29": 16.0, "43": 16.0} |
| Tent | Reset parameters only | 0 | ba | uci_internal_fixed | skipped | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters only | 0 | ba | uci_internal_fixed | recoveries | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters only | 4 | ab | uci_internal_fixed | accuracy | 3 | 0.861654 | 0.0181739 | {"17": 0.859375, "29": 0.8447265625, "43": 0.880859375} |
| Tent | Reset parameters only | 4 | ab | uci_internal_fixed | nll | 3 | 0.514502 | 0.11514 | {"17": 0.5036687420458444, "29": 0.634676043723535, "43": 0.40516130514872817} |
| Tent | Reset parameters only | 4 | ab | uci_internal_fixed | brier | 3 | 0.214187 | 0.0329092 | {"17": 0.2165156663145436, "29": 0.245870312242852, "43": 0.1801756355831121} |
| Tent | Reset parameters only | 4 | ab | uci_internal_fixed | ece15 | 3 | 0.0790531 | 0.0154126 | {"17": 0.0806275751283608, "29": 0.09361801146404845, "43": 0.0629137464560561} |
| Tent | Reset parameters only | 4 | ab | uci_internal_fixed | seconds | 3 | 0.126126 | 0.0139947 | {"17": 0.11570700000447684, "29": 0.14203305000410177, "43": 0.1206382000018493} |
| Tent | Reset parameters only | 4 | ab | uci_internal_fixed | updates | 3 | 16 | 0 | {"17": 16.0, "29": 16.0, "43": 16.0} |
| Tent | Reset parameters only | 4 | ab | uci_internal_fixed | skipped | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters only | 4 | ab | uci_internal_fixed | recoveries | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters only | 4 | ba | uci_internal_fixed | accuracy | 3 | 0.861654 | 0.0181739 | {"17": 0.859375, "29": 0.8447265625, "43": 0.880859375} |
| Tent | Reset parameters only | 4 | ba | uci_internal_fixed | nll | 3 | 0.514526 | 0.11511 | {"17": 0.5036606918559201, "29": 0.6346834765094637, "43": 0.40523303624407503} |
| Tent | Reset parameters only | 4 | ba | uci_internal_fixed | brier | 3 | 0.214189 | 0.0329004 | {"17": 0.2165073141444036, "29": 0.2458683141654962, "43": 0.18019012666772286} |
| Tent | Reset parameters only | 4 | ba | uci_internal_fixed | ece15 | 3 | 0.0788868 | 0.0151626 | {"17": 0.08063557464399465, "29": 0.0930991063041811, "43": 0.0629255753984213} |
| Tent | Reset parameters only | 4 | ba | uci_internal_fixed | seconds | 3 | 0.125484 | 0.0248021 | {"17": 0.11933699999644884, "29": 0.15278219999891005, "43": 0.10433424999791896} |
| Tent | Reset parameters only | 4 | ba | uci_internal_fixed | updates | 3 | 16 | 0 | {"17": 16.0, "29": 16.0, "43": 16.0} |
| Tent | Reset parameters only | 4 | ba | uci_internal_fixed | skipped | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters only | 4 | ba | uci_internal_fixed | recoveries | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + auxiliary state | 0 | ab | uci_internal_fixed | accuracy | 3 | 0.861654 | 0.0181739 | {"17": 0.859375, "29": 0.8447265625, "43": 0.880859375} |
| Tent | Reset parameters + auxiliary state | 0 | ab | uci_internal_fixed | nll | 3 | 0.514055 | 0.11384 | {"17": 0.5037357180248052, "29": 0.6327035834352337, "43": 0.4057255673288713} |
| Tent | Reset parameters + auxiliary state | 0 | ab | uci_internal_fixed | brier | 3 | 0.214121 | 0.03261 | {"17": 0.21654701220291023, "29": 0.24545066349121644, "43": 0.18036610327834152} |
| Tent | Reset parameters + auxiliary state | 0 | ab | uci_internal_fixed | ece15 | 3 | 0.0790121 | 0.0153827 | {"17": 0.0806069918029438, "29": 0.0935352071896381, "43": 0.06289404616470935} |
| Tent | Reset parameters + auxiliary state | 0 | ab | uci_internal_fixed | seconds | 3 | 0.11818 | 0.0338246 | {"17": 0.10889734999364005, "29": 0.15567649999866262, "43": 0.0899655999965034} |
| Tent | Reset parameters + auxiliary state | 0 | ab | uci_internal_fixed | updates | 3 | 16 | 0 | {"17": 16.0, "29": 16.0, "43": 16.0} |
| Tent | Reset parameters + auxiliary state | 0 | ab | uci_internal_fixed | skipped | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + auxiliary state | 0 | ab | uci_internal_fixed | recoveries | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + auxiliary state | 0 | ba | uci_internal_fixed | accuracy | 3 | 0.861654 | 0.0181739 | {"17": 0.859375, "29": 0.8447265625, "43": 0.880859375} |
| Tent | Reset parameters + auxiliary state | 0 | ba | uci_internal_fixed | nll | 3 | 0.514092 | 0.113798 | {"17": 0.5037222330867153, "29": 0.6327195273069306, "43": 0.4058329529956203} |
| Tent | Reset parameters + auxiliary state | 0 | ba | uci_internal_fixed | brier | 3 | 0.214124 | 0.0325978 | {"17": 0.21653407000510672, "29": 0.2454492569083861, "43": 0.1803874888047333} |
| Tent | Reset parameters + auxiliary state | 0 | ba | uci_internal_fixed | ece15 | 3 | 0.0790231 | 0.0153754 | {"17": 0.08061911659979434, "29": 0.09353822668981421, "43": 0.06291200327538955} |
| Tent | Reset parameters + auxiliary state | 0 | ba | uci_internal_fixed | seconds | 3 | 0.113979 | 0.0186889 | {"17": 0.11083554999640904, "29": 0.1340409500044188, "43": 0.0970619500003522} |
| Tent | Reset parameters + auxiliary state | 0 | ba | uci_internal_fixed | updates | 3 | 16 | 0 | {"17": 16.0, "29": 16.0, "43": 16.0} |
| Tent | Reset parameters + auxiliary state | 0 | ba | uci_internal_fixed | skipped | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + auxiliary state | 0 | ba | uci_internal_fixed | recoveries | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + auxiliary state | 4 | ab | uci_internal_fixed | accuracy | 3 | 0.861654 | 0.0181739 | {"17": 0.859375, "29": 0.8447265625, "43": 0.880859375} |
| Tent | Reset parameters + auxiliary state | 4 | ab | uci_internal_fixed | nll | 3 | 0.514502 | 0.11514 | {"17": 0.5036687420458444, "29": 0.634676043723535, "43": 0.40516130514872817} |
| Tent | Reset parameters + auxiliary state | 4 | ab | uci_internal_fixed | brier | 3 | 0.214187 | 0.0329092 | {"17": 0.2165156663145436, "29": 0.245870312242852, "43": 0.1801756355831121} |
| Tent | Reset parameters + auxiliary state | 4 | ab | uci_internal_fixed | ece15 | 3 | 0.0790531 | 0.0154126 | {"17": 0.0806275751283608, "29": 0.09361801146404845, "43": 0.0629137464560561} |
| Tent | Reset parameters + auxiliary state | 4 | ab | uci_internal_fixed | seconds | 3 | 0.111117 | 0.0119441 | {"17": 0.11331169999903065, "29": 0.121811400000297, "43": 0.09822755000641334} |
| Tent | Reset parameters + auxiliary state | 4 | ab | uci_internal_fixed | updates | 3 | 16 | 0 | {"17": 16.0, "29": 16.0, "43": 16.0} |
| Tent | Reset parameters + auxiliary state | 4 | ab | uci_internal_fixed | skipped | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + auxiliary state | 4 | ab | uci_internal_fixed | recoveries | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + auxiliary state | 4 | ba | uci_internal_fixed | accuracy | 3 | 0.861654 | 0.0181739 | {"17": 0.859375, "29": 0.8447265625, "43": 0.880859375} |
| Tent | Reset parameters + auxiliary state | 4 | ba | uci_internal_fixed | nll | 3 | 0.514526 | 0.11511 | {"17": 0.5036606918559201, "29": 0.6346834765094637, "43": 0.40523303624407503} |
| Tent | Reset parameters + auxiliary state | 4 | ba | uci_internal_fixed | brier | 3 | 0.214189 | 0.0329004 | {"17": 0.2165073141444036, "29": 0.2458683141654962, "43": 0.18019012666772286} |
| Tent | Reset parameters + auxiliary state | 4 | ba | uci_internal_fixed | ece15 | 3 | 0.0788868 | 0.0151626 | {"17": 0.08063557464399465, "29": 0.0930991063041811, "43": 0.0629255753984213} |
| Tent | Reset parameters + auxiliary state | 4 | ba | uci_internal_fixed | seconds | 3 | 0.111848 | 0.00934086 | {"17": 0.11297070000728125, "29": 0.12057634999655414, "43": 0.1019961500060162} |
| Tent | Reset parameters + auxiliary state | 4 | ba | uci_internal_fixed | updates | 3 | 16 | 0 | {"17": 16.0, "29": 16.0, "43": 16.0} |
| Tent | Reset parameters + auxiliary state | 4 | ba | uci_internal_fixed | skipped | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + auxiliary state | 4 | ba | uci_internal_fixed | recoveries | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + optimizer | 0 | ab | uci_internal_fixed | accuracy | 3 | 0.861654 | 0.0181739 | {"17": 0.859375, "29": 0.8447265625, "43": 0.880859375} |
| Tent | Reset parameters + optimizer | 0 | ab | uci_internal_fixed | nll | 3 | 0.514146 | 0.114013 | {"17": 0.5038094188406126, "29": 0.6329752572847591, "43": 0.4056525191548072} |
| Tent | Reset parameters + optimizer | 0 | ab | uci_internal_fixed | brier | 3 | 0.214142 | 0.0326466 | {"17": 0.21656771148689508, "29": 0.24550775070835953, "43": 0.1803498760320491} |
| Tent | Reset parameters + optimizer | 0 | ab | uci_internal_fixed | ece15 | 3 | 0.0789993 | 0.01539 | {"17": 0.08059263206845049, "29": 0.09353063621526654, "43": 0.06287464072694365} |
| Tent | Reset parameters + optimizer | 0 | ab | uci_internal_fixed | seconds | 3 | 0.121998 | 0.0304031 | {"17": 0.10981870000250635, "29": 0.1566026500004227, "43": 0.09957315000065135} |
| Tent | Reset parameters + optimizer | 0 | ab | uci_internal_fixed | updates | 3 | 16 | 0 | {"17": 16.0, "29": 16.0, "43": 16.0} |
| Tent | Reset parameters + optimizer | 0 | ab | uci_internal_fixed | skipped | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + optimizer | 0 | ab | uci_internal_fixed | recoveries | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + optimizer | 0 | ba | uci_internal_fixed | accuracy | 3 | 0.861654 | 0.0181739 | {"17": 0.859375, "29": 0.8447265625, "43": 0.880859375} |
| Tent | Reset parameters + optimizer | 0 | ba | uci_internal_fixed | nll | 3 | 0.514146 | 0.114013 | {"17": 0.5038094188406126, "29": 0.6329752572847591, "43": 0.4056525191548072} |
| Tent | Reset parameters + optimizer | 0 | ba | uci_internal_fixed | brier | 3 | 0.214142 | 0.0326466 | {"17": 0.21656771148689508, "29": 0.24550775070835953, "43": 0.1803498760320491} |
| Tent | Reset parameters + optimizer | 0 | ba | uci_internal_fixed | ece15 | 3 | 0.0789993 | 0.01539 | {"17": 0.08059263206845049, "29": 0.09353063621526654, "43": 0.06287464072694365} |
| Tent | Reset parameters + optimizer | 0 | ba | uci_internal_fixed | seconds | 3 | 0.126743 | 0.0348428 | {"17": 0.1228798500014818, "29": 0.16335594999691236, "43": 0.09399235000455515} |
| Tent | Reset parameters + optimizer | 0 | ba | uci_internal_fixed | updates | 3 | 16 | 0 | {"17": 16.0, "29": 16.0, "43": 16.0} |
| Tent | Reset parameters + optimizer | 0 | ba | uci_internal_fixed | skipped | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + optimizer | 0 | ba | uci_internal_fixed | recoveries | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + optimizer | 4 | ab | uci_internal_fixed | accuracy | 3 | 0.861654 | 0.0181739 | {"17": 0.859375, "29": 0.8447265625, "43": 0.880859375} |
| Tent | Reset parameters + optimizer | 4 | ab | uci_internal_fixed | nll | 3 | 0.514146 | 0.114013 | {"17": 0.5038094188406126, "29": 0.6329752572847591, "43": 0.4056525191548072} |
| Tent | Reset parameters + optimizer | 4 | ab | uci_internal_fixed | brier | 3 | 0.214142 | 0.0326466 | {"17": 0.21656771148689508, "29": 0.24550775070835953, "43": 0.1803498760320491} |
| Tent | Reset parameters + optimizer | 4 | ab | uci_internal_fixed | ece15 | 3 | 0.0789993 | 0.01539 | {"17": 0.08059263206845049, "29": 0.09353063621526654, "43": 0.06287464072694365} |
| Tent | Reset parameters + optimizer | 4 | ab | uci_internal_fixed | seconds | 3 | 0.127586 | 0.0192749 | {"17": 0.13200009999854956, "29": 0.14427140000043434, "43": 0.10648719999880996} |
| Tent | Reset parameters + optimizer | 4 | ab | uci_internal_fixed | updates | 3 | 16 | 0 | {"17": 16.0, "29": 16.0, "43": 16.0} |
| Tent | Reset parameters + optimizer | 4 | ab | uci_internal_fixed | skipped | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + optimizer | 4 | ab | uci_internal_fixed | recoveries | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + optimizer | 4 | ba | uci_internal_fixed | accuracy | 3 | 0.861654 | 0.0181739 | {"17": 0.859375, "29": 0.8447265625, "43": 0.880859375} |
| Tent | Reset parameters + optimizer | 4 | ba | uci_internal_fixed | nll | 3 | 0.514146 | 0.114013 | {"17": 0.5038094188406126, "29": 0.6329752572847591, "43": 0.4056525191548072} |
| Tent | Reset parameters + optimizer | 4 | ba | uci_internal_fixed | brier | 3 | 0.214142 | 0.0326466 | {"17": 0.21656771148689508, "29": 0.24550775070835953, "43": 0.1803498760320491} |
| Tent | Reset parameters + optimizer | 4 | ba | uci_internal_fixed | ece15 | 3 | 0.0789993 | 0.01539 | {"17": 0.08059263206845049, "29": 0.09353063621526654, "43": 0.06287464072694365} |
| Tent | Reset parameters + optimizer | 4 | ba | uci_internal_fixed | seconds | 3 | 0.121735 | 0.0160413 | {"17": 0.1261373999950592, "29": 0.13511495000420837, "43": 0.1039517500030342} |
| Tent | Reset parameters + optimizer | 4 | ba | uci_internal_fixed | updates | 3 | 16 | 0 | {"17": 16.0, "29": 16.0, "43": 16.0} |
| Tent | Reset parameters + optimizer | 4 | ba | uci_internal_fixed | skipped | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + optimizer | 4 | ba | uci_internal_fixed | recoveries | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | ab | uci_internal_fixed | accuracy | 3 | 0.861654 | 0.0181739 | {"17": 0.859375, "29": 0.8447265625, "43": 0.880859375} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | ab | uci_internal_fixed | nll | 3 | 0.514146 | 0.114013 | {"17": 0.5038094188406126, "29": 0.6329752572847591, "43": 0.4056525191548072} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | ab | uci_internal_fixed | brier | 3 | 0.214142 | 0.0326466 | {"17": 0.21656771148689508, "29": 0.24550775070835953, "43": 0.1803498760320491} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | ab | uci_internal_fixed | ece15 | 3 | 0.0789993 | 0.01539 | {"17": 0.08059263206845049, "29": 0.09353063621526654, "43": 0.06287464072694365} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | ab | uci_internal_fixed | seconds | 3 | 0.123524 | 0.019753 | {"17": 0.1240865000072517, "29": 0.14298985000641545, "43": 0.1034958999953232} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | ab | uci_internal_fixed | updates | 3 | 16 | 0 | {"17": 16.0, "29": 16.0, "43": 16.0} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | ab | uci_internal_fixed | skipped | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | ab | uci_internal_fixed | recoveries | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | ba | uci_internal_fixed | accuracy | 3 | 0.861654 | 0.0181739 | {"17": 0.859375, "29": 0.8447265625, "43": 0.880859375} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | ba | uci_internal_fixed | nll | 3 | 0.514146 | 0.114013 | {"17": 0.5038094188406126, "29": 0.6329752572847591, "43": 0.4056525191548072} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | ba | uci_internal_fixed | brier | 3 | 0.214142 | 0.0326466 | {"17": 0.21656771148689508, "29": 0.24550775070835953, "43": 0.1803498760320491} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | ba | uci_internal_fixed | ece15 | 3 | 0.0789993 | 0.01539 | {"17": 0.08059263206845049, "29": 0.09353063621526654, "43": 0.06287464072694365} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | ba | uci_internal_fixed | seconds | 3 | 0.139554 | 0.0472147 | {"17": 0.11135479999938974, "29": 0.19406195000192378, "43": 0.1132453999962308} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | ba | uci_internal_fixed | updates | 3 | 16 | 0 | {"17": 16.0, "29": 16.0, "43": 16.0} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | ba | uci_internal_fixed | skipped | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | ba | uci_internal_fixed | recoveries | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | ab | uci_internal_fixed | accuracy | 3 | 0.861654 | 0.0181739 | {"17": 0.859375, "29": 0.8447265625, "43": 0.880859375} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | ab | uci_internal_fixed | nll | 3 | 0.514146 | 0.114013 | {"17": 0.5038094188406126, "29": 0.6329752572847591, "43": 0.4056525191548072} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | ab | uci_internal_fixed | brier | 3 | 0.214142 | 0.0326466 | {"17": 0.21656771148689508, "29": 0.24550775070835953, "43": 0.1803498760320491} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | ab | uci_internal_fixed | ece15 | 3 | 0.0789993 | 0.01539 | {"17": 0.08059263206845049, "29": 0.09353063621526654, "43": 0.06287464072694365} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | ab | uci_internal_fixed | seconds | 3 | 0.103757 | 0.014124 | {"17": 0.11535884999466355, "29": 0.10788344999309624, "43": 0.08802984999056204} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | ab | uci_internal_fixed | updates | 3 | 16 | 0 | {"17": 16.0, "29": 16.0, "43": 16.0} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | ab | uci_internal_fixed | skipped | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | ab | uci_internal_fixed | recoveries | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | ba | uci_internal_fixed | accuracy | 3 | 0.861654 | 0.0181739 | {"17": 0.859375, "29": 0.8447265625, "43": 0.880859375} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | ba | uci_internal_fixed | nll | 3 | 0.514146 | 0.114013 | {"17": 0.5038094188406126, "29": 0.6329752572847591, "43": 0.4056525191548072} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | ba | uci_internal_fixed | brier | 3 | 0.214142 | 0.0326466 | {"17": 0.21656771148689508, "29": 0.24550775070835953, "43": 0.1803498760320491} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | ba | uci_internal_fixed | ece15 | 3 | 0.0789993 | 0.01539 | {"17": 0.08059263206845049, "29": 0.09353063621526654, "43": 0.06287464072694365} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | ba | uci_internal_fixed | seconds | 3 | 0.121078 | 0.0307729 | {"17": 0.1514337999979034, "29": 0.12189550000039155, "43": 0.08990429999539626} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | ba | uci_internal_fixed | updates | 3 | 16 | 0 | {"17": 16.0, "29": 16.0, "43": 16.0} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | ba | uci_internal_fixed | skipped | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | ba | uci_internal_fixed | recoveries | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |


## reset_effects

| method | intervention | washout_batches | metric | n_panels | mean | sd | ci95_low | ci95_high | n_seeds_min | n_seeds_max | individual_panels |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Normalization only | Reset all declared state | 0 | disagreement_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Normalization only | Reset all declared state | 0 | absolute_error_gap_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Normalization only | Reset all declared state | 0 | nll_gap_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Normalization only | Reset all declared state | 0 | brier_gap_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Normalization only | Reset all declared state | 4 | disagreement_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Normalization only | Reset all declared state | 4 | absolute_error_gap_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Normalization only | Reset all declared state | 4 | nll_gap_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Normalization only | Reset all declared state | 4 | brier_gap_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset all declared state | 0 | disagreement_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset all declared state | 0 | absolute_error_gap_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset all declared state | 0 | nll_gap_change | 1 | -5.04814e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": -5.0481432768175876e-05} |
| SAR (complete-state implementation) | Reset all declared state | 0 | brier_gap_change | 1 | -1.31498e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": -1.3149844326745588e-05} |
| SAR (complete-state implementation) | Reset all declared state | 4 | disagreement_change | 1 | -0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0003255208333333333} |
| SAR (complete-state implementation) | Reset all declared state | 4 | absolute_error_gap_change | 1 | -0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0003255208333333333} |
| SAR (complete-state implementation) | Reset all declared state | 4 | nll_gap_change | 1 | 2.92067e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": 2.920671777545e-05} |
| SAR (complete-state implementation) | Reset all declared state | 4 | brier_gap_change | 1 | 4.94772e-06 | — | — | — | 3 | 3 | {"uci_internal_fixed": 4.947722413421267e-06} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | disagreement_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | absolute_error_gap_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | nll_gap_change | 1 | -5.12597e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": -5.1259698265152024e-05} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | brier_gap_change | 1 | -1.32871e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": -1.3287099847638395e-05} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | disagreement_change | 1 | -0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0003255208333333333} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | absolute_error_gap_change | 1 | -0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0003255208333333333} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | nll_gap_change | 1 | 2.92067e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": 2.920671777545e-05} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | brier_gap_change | 1 | 4.94772e-06 | — | — | — | 3 | 3 | {"uci_internal_fixed": 4.947722413421267e-06} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | disagreement_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | absolute_error_gap_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | nll_gap_change | 1 | -1.83465e-08 | — | — | — | 3 | 3 | {"uci_internal_fixed": -1.8346453879251407e-08} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | brier_gap_change | 1 | -1.10346e-08 | — | — | — | 3 | 3 | {"uci_internal_fixed": -1.1034551456017469e-08} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | disagreement_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | absolute_error_gap_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | nll_gap_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | brier_gap_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | disagreement_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | absolute_error_gap_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | nll_gap_change | 1 | -5.12597e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": -5.1259698265152024e-05} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | brier_gap_change | 1 | -1.32871e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": -1.3287099847638395e-05} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | disagreement_change | 1 | -0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0003255208333333333} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | absolute_error_gap_change | 1 | -0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0003255208333333333} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | nll_gap_change | 1 | 2.92067e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": 2.920671777545e-05} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | brier_gap_change | 1 | 4.94772e-06 | — | — | — | 3 | 3 | {"uci_internal_fixed": 4.947722413421267e-06} |
| SAR (complete-state implementation) | Reset parameters only | 0 | disagreement_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset parameters only | 0 | absolute_error_gap_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset parameters only | 0 | nll_gap_change | 1 | 5.87569e-07 | — | — | — | 3 | 3 | {"uci_internal_fixed": 5.875691655050456e-07} |
| SAR (complete-state implementation) | Reset parameters only | 0 | brier_gap_change | 1 | 3.84161e-08 | — | — | — | 3 | 3 | {"uci_internal_fixed": 3.841613947381158e-08} |
| SAR (complete-state implementation) | Reset parameters only | 4 | disagreement_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset parameters only | 4 | absolute_error_gap_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset parameters only | 4 | nll_gap_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset parameters only | 4 | brier_gap_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | disagreement_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | absolute_error_gap_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | nll_gap_change | 1 | -5.04814e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": -5.0481432768175876e-05} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | brier_gap_change | 1 | -1.31498e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": -1.3149844326745588e-05} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | disagreement_change | 1 | -0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0003255208333333333} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | absolute_error_gap_change | 1 | -0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0003255208333333333} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | nll_gap_change | 1 | 2.92067e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": 2.920671777545e-05} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | brier_gap_change | 1 | 4.94772e-06 | — | — | — | 3 | 3 | {"uci_internal_fixed": 4.947722413421267e-06} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | disagreement_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | absolute_error_gap_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | nll_gap_change | 1 | 5.67796e-07 | — | — | — | 3 | 3 | {"uci_internal_fixed": 5.677964605490619e-07} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | brier_gap_change | 1 | 2.65356e-08 | — | — | — | 3 | 3 | {"uci_internal_fixed": 2.6535557384512378e-08} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | disagreement_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | absolute_error_gap_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | nll_gap_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | brier_gap_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | disagreement_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | absolute_error_gap_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | nll_gap_change | 1 | -5.04814e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": -5.0481432768175876e-05} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | brier_gap_change | 1 | -1.31498e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": -1.3149844326745588e-05} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | disagreement_change | 1 | -0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0003255208333333333} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | absolute_error_gap_change | 1 | -0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0003255208333333333} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | nll_gap_change | 1 | 2.92067e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": 2.920671777545e-05} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | brier_gap_change | 1 | 4.94772e-06 | — | — | — | 3 | 3 | {"uci_internal_fixed": 4.947722413421267e-06} |
| Source | Reset all declared state | 0 | disagreement_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Source | Reset all declared state | 0 | absolute_error_gap_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Source | Reset all declared state | 0 | nll_gap_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Source | Reset all declared state | 0 | brier_gap_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Source | Reset all declared state | 4 | disagreement_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Source | Reset all declared state | 4 | absolute_error_gap_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Source | Reset all declared state | 4 | nll_gap_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Source | Reset all declared state | 4 | brier_gap_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset all declared state | 0 | disagreement_change | 1 | -0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0003255208333333333} |
| Tent | Reset all declared state | 0 | absolute_error_gap_change | 1 | -0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0003255208333333333} |
| Tent | Reset all declared state | 0 | nll_gap_change | 1 | -2.61611e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": -2.6161054073633804e-05} |
| Tent | Reset all declared state | 0 | brier_gap_change | 1 | -2.23542e-06 | — | — | — | 3 | 3 | {"uci_internal_fixed": -2.235415372002734e-06} |
| Tent | Reset all declared state | 4 | disagreement_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset all declared state | 4 | absolute_error_gap_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset all declared state | 4 | nll_gap_change | 1 | -1.7286e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": -1.7285966563115378e-05} |
| Tent | Reset all declared state | 4 | brier_gap_change | 1 | -1.58798e-06 | — | — | — | 3 | 3 | {"uci_internal_fixed": -1.5879808014113844e-06} |
| Tent | Reset auxiliary state only | 0 | disagreement_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset auxiliary state only | 0 | absolute_error_gap_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset auxiliary state only | 0 | nll_gap_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset auxiliary state only | 0 | brier_gap_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset auxiliary state only | 4 | disagreement_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset auxiliary state only | 4 | absolute_error_gap_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset auxiliary state only | 4 | nll_gap_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset auxiliary state only | 4 | brier_gap_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset optimizer only | 0 | disagreement_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset optimizer only | 0 | absolute_error_gap_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset optimizer only | 0 | nll_gap_change | 1 | 3.66928e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": 3.6692798779349373e-05} |
| Tent | Reset optimizer only | 0 | brier_gap_change | 1 | 2.35671e-06 | — | — | — | 3 | 3 | {"uci_internal_fixed": 2.3567142949366175e-06} |
| Tent | Reset optimizer only | 4 | disagreement_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset optimizer only | 4 | absolute_error_gap_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset optimizer only | 4 | nll_gap_change | 1 | 2.4461e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": 2.4460967249371428e-05} |
| Tent | Reset optimizer only | 4 | brier_gap_change | 1 | 1.71282e-06 | — | — | — | 3 | 3 | {"uci_internal_fixed": 1.7128248196677843e-06} |
| Tent | Reset optimizer + auxiliary state | 0 | disagreement_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset optimizer + auxiliary state | 0 | absolute_error_gap_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset optimizer + auxiliary state | 0 | nll_gap_change | 1 | 3.66928e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": 3.6692798779349373e-05} |
| Tent | Reset optimizer + auxiliary state | 0 | brier_gap_change | 1 | 2.35671e-06 | — | — | — | 3 | 3 | {"uci_internal_fixed": 2.3567142949366175e-06} |
| Tent | Reset optimizer + auxiliary state | 4 | disagreement_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset optimizer + auxiliary state | 4 | absolute_error_gap_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset optimizer + auxiliary state | 4 | nll_gap_change | 1 | 2.4461e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": 2.4460967249371428e-05} |
| Tent | Reset optimizer + auxiliary state | 4 | brier_gap_change | 1 | 1.71282e-06 | — | — | — | 3 | 3 | {"uci_internal_fixed": 1.7128248196677843e-06} |
| Tent | Reset parameters only | 0 | disagreement_change | 1 | -0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0003255208333333333} |
| Tent | Reset parameters only | 0 | absolute_error_gap_change | 1 | -0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0003255208333333333} |
| Tent | Reset parameters only | 0 | nll_gap_change | 1 | -6.27759e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": -6.277592085892432e-05} |
| Tent | Reset parameters only | 0 | brier_gap_change | 1 | -4.581e-06 | — | — | — | 3 | 3 | {"uci_internal_fixed": -4.580997291306228e-06} |
| Tent | Reset parameters only | 4 | disagreement_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset parameters only | 4 | absolute_error_gap_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset parameters only | 4 | nll_gap_change | 1 | -4.09905e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": -4.0990530346790564e-05} |
| Tent | Reset parameters only | 4 | brier_gap_change | 1 | -2.96826e-06 | — | — | — | 3 | 3 | {"uci_internal_fixed": -2.968259839704913e-06} |
| Tent | Reset parameters + auxiliary state | 0 | disagreement_change | 1 | -0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0003255208333333333} |
| Tent | Reset parameters + auxiliary state | 0 | absolute_error_gap_change | 1 | -0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0003255208333333333} |
| Tent | Reset parameters + auxiliary state | 0 | nll_gap_change | 1 | -6.27759e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": -6.277592085892432e-05} |
| Tent | Reset parameters + auxiliary state | 0 | brier_gap_change | 1 | -4.581e-06 | — | — | — | 3 | 3 | {"uci_internal_fixed": -4.580997291306228e-06} |
| Tent | Reset parameters + auxiliary state | 4 | disagreement_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset parameters + auxiliary state | 4 | absolute_error_gap_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset parameters + auxiliary state | 4 | nll_gap_change | 1 | -4.09905e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": -4.0990530346790564e-05} |
| Tent | Reset parameters + auxiliary state | 4 | brier_gap_change | 1 | -2.96826e-06 | — | — | — | 3 | 3 | {"uci_internal_fixed": -2.968259839704913e-06} |
| Tent | Reset parameters + optimizer | 0 | disagreement_change | 1 | -0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0003255208333333333} |
| Tent | Reset parameters + optimizer | 0 | absolute_error_gap_change | 1 | -0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0003255208333333333} |
| Tent | Reset parameters + optimizer | 0 | nll_gap_change | 1 | -2.61611e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": -2.6161054073633804e-05} |
| Tent | Reset parameters + optimizer | 0 | brier_gap_change | 1 | -2.23542e-06 | — | — | — | 3 | 3 | {"uci_internal_fixed": -2.235415372002734e-06} |
| Tent | Reset parameters + optimizer | 4 | disagreement_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset parameters + optimizer | 4 | absolute_error_gap_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset parameters + optimizer | 4 | nll_gap_change | 1 | -1.7286e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": -1.7285966563115378e-05} |
| Tent | Reset parameters + optimizer | 4 | brier_gap_change | 1 | -1.58798e-06 | — | — | — | 3 | 3 | {"uci_internal_fixed": -1.5879808014113844e-06} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | disagreement_change | 1 | -0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0003255208333333333} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | absolute_error_gap_change | 1 | -0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0003255208333333333} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | nll_gap_change | 1 | -2.61611e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": -2.6161054073633804e-05} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | brier_gap_change | 1 | -2.23542e-06 | — | — | — | 3 | 3 | {"uci_internal_fixed": -2.235415372002734e-06} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | disagreement_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | absolute_error_gap_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | nll_gap_change | 1 | -1.7286e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": -1.7285966563115378e-05} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | brier_gap_change | 1 | -1.58798e-06 | — | — | — | 3 | 3 | {"uci_internal_fixed": -1.5879808014113844e-06} |


### reset_effects: descriptive seed repetitions

The same image panel is reused across seeds. These standard deviations describe seed variability only; no confidence interval is justified from treating seeds as new image panels.

| method | intervention | washout_batches | panel_id | metric | n_seeds | mean | seed_sd_descriptive | individual_seeds |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Normalization only | Reset all declared state | 0 | uci_internal_fixed | disagreement_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Normalization only | Reset all declared state | 0 | uci_internal_fixed | absolute_error_gap_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Normalization only | Reset all declared state | 0 | uci_internal_fixed | nll_gap_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Normalization only | Reset all declared state | 0 | uci_internal_fixed | brier_gap_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Normalization only | Reset all declared state | 4 | uci_internal_fixed | disagreement_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Normalization only | Reset all declared state | 4 | uci_internal_fixed | absolute_error_gap_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Normalization only | Reset all declared state | 4 | uci_internal_fixed | nll_gap_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Normalization only | Reset all declared state | 4 | uci_internal_fixed | brier_gap_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset all declared state | 0 | uci_internal_fixed | disagreement_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset all declared state | 0 | uci_internal_fixed | absolute_error_gap_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset all declared state | 0 | uci_internal_fixed | nll_gap_change | 3 | -5.04814e-05 | 9.31129e-05 | {"17": -0.0001579838026641614, "29": 4.829827729761066e-06, "43": 1.7096766298727029e-06} |
| SAR (complete-state implementation) | Reset all declared state | 0 | uci_internal_fixed | brier_gap_change | 3 | -1.31498e-05 | 2.3767e-05 | {"17": -4.0590077020863716e-05, "29": 9.50108690903062e-07, "43": 1.9043534972389145e-07} |
| SAR (complete-state implementation) | Reset all declared state | 4 | uci_internal_fixed | disagreement_change | 3 | -0.000325521 | 0.000563819 | {"17": -0.0009765625, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset all declared state | 4 | uci_internal_fixed | absolute_error_gap_change | 3 | -0.000325521 | 0.000563819 | {"17": -0.0009765625, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset all declared state | 4 | uci_internal_fixed | nll_gap_change | 3 | 2.92067e-05 | 5.05875e-05 | {"17": 8.762015332635e-05, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset all declared state | 4 | uci_internal_fixed | brier_gap_change | 3 | 4.94772e-06 | 8.56971e-06 | {"17": 1.48431672402638e-05, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | uci_internal_fixed | disagreement_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | uci_internal_fixed | absolute_error_gap_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | uci_internal_fixed | nll_gap_change | 3 | -5.12597e-05 | 9.30985e-05 | {"17": -0.00015872270940313362, "29": 4.94361460767756e-06, "43": 0.0} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | uci_internal_fixed | brier_gap_change | 3 | -1.32871e-05 | 2.39163e-05 | {"17": -4.089681801499635e-05, "29": 1.035518472081165e-06, "43": 0.0} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | uci_internal_fixed | disagreement_change | 3 | -0.000325521 | 0.000563819 | {"17": -0.0009765625, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | uci_internal_fixed | absolute_error_gap_change | 3 | -0.000325521 | 0.000563819 | {"17": -0.0009765625, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | uci_internal_fixed | nll_gap_change | 3 | 2.92067e-05 | 5.05875e-05 | {"17": 8.762015332635e-05, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | uci_internal_fixed | brier_gap_change | 3 | 4.94772e-06 | 8.56971e-06 | {"17": 1.48431672402638e-05, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | uci_internal_fixed | disagreement_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | uci_internal_fixed | absolute_error_gap_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | uci_internal_fixed | nll_gap_change | 3 | -1.83465e-08 | 3.1777e-08 | {"17": -5.503936163775422e-08, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | uci_internal_fixed | brier_gap_change | 3 | -1.10346e-08 | 1.91124e-08 | {"17": -3.3103654368052404e-08, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | uci_internal_fixed | disagreement_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | uci_internal_fixed | absolute_error_gap_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | uci_internal_fixed | nll_gap_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | uci_internal_fixed | brier_gap_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | uci_internal_fixed | disagreement_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | uci_internal_fixed | absolute_error_gap_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | uci_internal_fixed | nll_gap_change | 3 | -5.12597e-05 | 9.30985e-05 | {"17": -0.00015872270940313362, "29": 4.94361460767756e-06, "43": 0.0} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | uci_internal_fixed | brier_gap_change | 3 | -1.32871e-05 | 2.39163e-05 | {"17": -4.089681801499635e-05, "29": 1.035518472081165e-06, "43": 0.0} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | uci_internal_fixed | disagreement_change | 3 | -0.000325521 | 0.000563819 | {"17": -0.0009765625, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | uci_internal_fixed | absolute_error_gap_change | 3 | -0.000325521 | 0.000563819 | {"17": -0.0009765625, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | uci_internal_fixed | nll_gap_change | 3 | 2.92067e-05 | 5.05875e-05 | {"17": 8.762015332635e-05, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | uci_internal_fixed | brier_gap_change | 3 | 4.94772e-06 | 8.56971e-06 | {"17": 1.48431672402638e-05, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters only | 0 | uci_internal_fixed | disagreement_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters only | 0 | uci_internal_fixed | absolute_error_gap_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters only | 0 | uci_internal_fixed | nll_gap_change | 3 | 5.87569e-07 | 9.8185e-07 | {"17": 1.6681774455892806e-07, "29": -1.1378687791649412e-07, "43": 1.7096766298727029e-06} |
| SAR (complete-state implementation) | Reset parameters only | 0 | uci_internal_fixed | brier_gap_change | 3 | 3.84161e-08 | 1.40067e-07 | {"17": 1.0222849875646253e-08, "29": -8.540978117810295e-08, "43": 1.9043534972389145e-07} |
| SAR (complete-state implementation) | Reset parameters only | 4 | uci_internal_fixed | disagreement_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters only | 4 | uci_internal_fixed | absolute_error_gap_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters only | 4 | uci_internal_fixed | nll_gap_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters only | 4 | uci_internal_fixed | brier_gap_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | uci_internal_fixed | disagreement_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | uci_internal_fixed | absolute_error_gap_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | uci_internal_fixed | nll_gap_change | 3 | -5.04814e-05 | 9.31129e-05 | {"17": -0.0001579838026641614, "29": 4.829827729761066e-06, "43": 1.7096766298727029e-06} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | uci_internal_fixed | brier_gap_change | 3 | -1.31498e-05 | 2.3767e-05 | {"17": -4.0590077020863716e-05, "29": 9.50108690903062e-07, "43": 1.9043534972389145e-07} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | uci_internal_fixed | disagreement_change | 3 | -0.000325521 | 0.000563819 | {"17": -0.0009765625, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | uci_internal_fixed | absolute_error_gap_change | 3 | -0.000325521 | 0.000563819 | {"17": -0.0009765625, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | uci_internal_fixed | nll_gap_change | 3 | 2.92067e-05 | 5.05875e-05 | {"17": 8.762015332635e-05, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | uci_internal_fixed | brier_gap_change | 3 | 4.94772e-06 | 8.56971e-06 | {"17": 1.48431672402638e-05, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | uci_internal_fixed | disagreement_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | uci_internal_fixed | absolute_error_gap_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | uci_internal_fixed | nll_gap_change | 3 | 5.67796e-07 | 9.95068e-07 | {"17": 1.0749962969097693e-07, "29": -1.1378687791649412e-07, "43": 1.7096766298727029e-06} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | uci_internal_fixed | brier_gap_change | 3 | 2.65356e-08 | 1.45076e-07 | {"17": -2.5418896392251367e-08, "29": -8.540978117810295e-08, "43": 1.9043534972389145e-07} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | uci_internal_fixed | disagreement_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | uci_internal_fixed | absolute_error_gap_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | uci_internal_fixed | nll_gap_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | uci_internal_fixed | brier_gap_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | uci_internal_fixed | disagreement_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | uci_internal_fixed | absolute_error_gap_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | uci_internal_fixed | nll_gap_change | 3 | -5.04814e-05 | 9.31129e-05 | {"17": -0.0001579838026641614, "29": 4.829827729761066e-06, "43": 1.7096766298727029e-06} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | uci_internal_fixed | brier_gap_change | 3 | -1.31498e-05 | 2.3767e-05 | {"17": -4.0590077020863716e-05, "29": 9.50108690903062e-07, "43": 1.9043534972389145e-07} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | uci_internal_fixed | disagreement_change | 3 | -0.000325521 | 0.000563819 | {"17": -0.0009765625, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | uci_internal_fixed | absolute_error_gap_change | 3 | -0.000325521 | 0.000563819 | {"17": -0.0009765625, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | uci_internal_fixed | nll_gap_change | 3 | 2.92067e-05 | 5.05875e-05 | {"17": 8.762015332635e-05, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | uci_internal_fixed | brier_gap_change | 3 | 4.94772e-06 | 8.56971e-06 | {"17": 1.48431672402638e-05, "29": 0.0, "43": 0.0} |
| Source | Reset all declared state | 0 | uci_internal_fixed | disagreement_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Source | Reset all declared state | 0 | uci_internal_fixed | absolute_error_gap_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Source | Reset all declared state | 0 | uci_internal_fixed | nll_gap_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Source | Reset all declared state | 0 | uci_internal_fixed | brier_gap_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Source | Reset all declared state | 4 | uci_internal_fixed | disagreement_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Source | Reset all declared state | 4 | uci_internal_fixed | absolute_error_gap_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Source | Reset all declared state | 4 | uci_internal_fixed | nll_gap_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Source | Reset all declared state | 4 | uci_internal_fixed | brier_gap_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset all declared state | 0 | uci_internal_fixed | disagreement_change | 3 | -0.000325521 | 0.000563819 | {"17": -0.0009765625, "29": 0.0, "43": 0.0} |
| Tent | Reset all declared state | 0 | uci_internal_fixed | absolute_error_gap_change | 3 | -0.000325521 | 0.000563819 | {"17": -0.0009765625, "29": 0.0, "43": 0.0} |
| Tent | Reset all declared state | 0 | uci_internal_fixed | nll_gap_change | 3 | -2.61611e-05 | 5.37812e-05 | {"17": 2.2949739964178012e-05, "29": -1.7799686981245094e-05, "43": -8.363321520383433e-05} |
| Tent | Reset all declared state | 0 | uci_internal_fixed | brier_gap_change | 3 | -2.23542e-06 | 1.90805e-05 | {"17": 1.3939091297097623e-05, "29": 2.633228041880667e-06, "43": -2.3278565454986494e-05} |
| Tent | Reset all declared state | 4 | uci_internal_fixed | disagreement_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset all declared state | 4 | uci_internal_fixed | absolute_error_gap_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset all declared state | 4 | uci_internal_fixed | nll_gap_change | 3 | -1.7286e-05 | 3.57076e-05 | {"17": 1.6961185307570736e-05, "29": -1.452539129353711e-05, "43": -5.429369370337976e-05} |
| Tent | Reset all declared state | 4 | uci_internal_fixed | brier_gap_change | 3 | -1.58798e-06 | 1.24235e-05 | {"17": 9.55651940180366e-06, "29": 6.623748391408613e-07, "43": -1.4982836645178674e-05} |
| Tent | Reset auxiliary state only | 0 | uci_internal_fixed | disagreement_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset auxiliary state only | 0 | uci_internal_fixed | absolute_error_gap_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset auxiliary state only | 0 | uci_internal_fixed | nll_gap_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset auxiliary state only | 0 | uci_internal_fixed | brier_gap_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset auxiliary state only | 4 | uci_internal_fixed | disagreement_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset auxiliary state only | 4 | uci_internal_fixed | absolute_error_gap_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset auxiliary state only | 4 | uci_internal_fixed | nll_gap_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset auxiliary state only | 4 | uci_internal_fixed | brier_gap_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset optimizer only | 0 | uci_internal_fixed | disagreement_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset optimizer only | 0 | uci_internal_fixed | absolute_error_gap_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset optimizer only | 0 | uci_internal_fixed | nll_gap_change | 3 | 3.66928e-05 | 6.47478e-05 | {"17": -1.6618544972594324e-05, "29": 1.7953447837351644e-05, "43": 0.00010874349347329081} |
| Tent | Reset optimizer only | 0 | uci_internal_fixed | brier_gap_change | 3 | 2.35671e-06 | 1.80921e-05 | {"17": -1.3804151567554587e-05, "29": -1.0278283817492778e-06, "43": 2.1902122834113718e-05} |
| Tent | Reset optimizer only | 4 | uci_internal_fixed | disagreement_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset optimizer only | 4 | uci_internal_fixed | absolute_error_gap_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset optimizer only | 4 | uci_internal_fixed | nll_gap_change | 3 | 2.4461e-05 | 4.281e-05 | {"17": -8.823152446928162e-06, "29": 9.45144917121124e-06, "43": 7.275460502383121e-05} |
| Tent | Reset optimizer only | 4 | uci_internal_fixed | brier_gap_change | 3 | 1.71282e-06 | 1.19851e-05 | {"17": -8.449287852404022e-06, "29": -1.341923651827088e-06, "43": 1.4929685963234463e-05} |
| Tent | Reset optimizer + auxiliary state | 0 | uci_internal_fixed | disagreement_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset optimizer + auxiliary state | 0 | uci_internal_fixed | absolute_error_gap_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset optimizer + auxiliary state | 0 | uci_internal_fixed | nll_gap_change | 3 | 3.66928e-05 | 6.47478e-05 | {"17": -1.6618544972594324e-05, "29": 1.7953447837351644e-05, "43": 0.00010874349347329081} |
| Tent | Reset optimizer + auxiliary state | 0 | uci_internal_fixed | brier_gap_change | 3 | 2.35671e-06 | 1.80921e-05 | {"17": -1.3804151567554587e-05, "29": -1.0278283817492778e-06, "43": 2.1902122834113718e-05} |
| Tent | Reset optimizer + auxiliary state | 4 | uci_internal_fixed | disagreement_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset optimizer + auxiliary state | 4 | uci_internal_fixed | absolute_error_gap_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset optimizer + auxiliary state | 4 | uci_internal_fixed | nll_gap_change | 3 | 2.4461e-05 | 4.281e-05 | {"17": -8.823152446928162e-06, "29": 9.45144917121124e-06, "43": 7.275460502383121e-05} |
| Tent | Reset optimizer + auxiliary state | 4 | uci_internal_fixed | brier_gap_change | 3 | 1.71282e-06 | 1.19851e-05 | {"17": -8.449287852404022e-06, "29": -1.341923651827088e-06, "43": 1.4929685963234463e-05} |
| Tent | Reset parameters only | 0 | uci_internal_fixed | disagreement_change | 3 | -0.000325521 | 0.000563819 | {"17": -0.0009765625, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters only | 0 | uci_internal_fixed | absolute_error_gap_change | 3 | -0.000325521 | 0.000563819 | {"17": -0.0009765625, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters only | 0 | uci_internal_fixed | nll_gap_change | 3 | -6.27759e-05 | 0.000116473 | {"17": 3.64346780541841e-05, "29": -3.374355867818979e-05, "43": -0.00019101888195276727} |
| Tent | Reset parameters only | 0 | uci_internal_fixed | brier_gap_change | 3 | -4.581e-06 | 3.65435e-05 | {"17": 2.6881289100588387e-05, "29": 4.039810872248639e-06, "43": -4.466409184675571e-05} |
| Tent | Reset parameters only | 4 | uci_internal_fixed | disagreement_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters only | 4 | uci_internal_fixed | absolute_error_gap_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters only | 4 | uci_internal_fixed | nll_gap_change | 3 | -4.09905e-05 | 7.72959e-05 | {"17": 2.501137523202787e-05, "29": -2.1958177222235892e-05, "43": -0.00012602478905016367} |
| Tent | Reset parameters only | 4 | uci_internal_fixed | brier_gap_change | 3 | -2.96826e-06 | 2.41876e-05 | {"17": 1.7908689541795697e-05, "29": 2.660452194980928e-06, "43": -2.9473921255891364e-05} |
| Tent | Reset parameters + auxiliary state | 0 | uci_internal_fixed | disagreement_change | 3 | -0.000325521 | 0.000563819 | {"17": -0.0009765625, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + auxiliary state | 0 | uci_internal_fixed | absolute_error_gap_change | 3 | -0.000325521 | 0.000563819 | {"17": -0.0009765625, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + auxiliary state | 0 | uci_internal_fixed | nll_gap_change | 3 | -6.27759e-05 | 0.000116473 | {"17": 3.64346780541841e-05, "29": -3.374355867818979e-05, "43": -0.00019101888195276727} |
| Tent | Reset parameters + auxiliary state | 0 | uci_internal_fixed | brier_gap_change | 3 | -4.581e-06 | 3.65435e-05 | {"17": 2.6881289100588387e-05, "29": 4.039810872248639e-06, "43": -4.466409184675571e-05} |
| Tent | Reset parameters + auxiliary state | 4 | uci_internal_fixed | disagreement_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + auxiliary state | 4 | uci_internal_fixed | absolute_error_gap_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + auxiliary state | 4 | uci_internal_fixed | nll_gap_change | 3 | -4.09905e-05 | 7.72959e-05 | {"17": 2.501137523202787e-05, "29": -2.1958177222235892e-05, "43": -0.00012602478905016367} |
| Tent | Reset parameters + auxiliary state | 4 | uci_internal_fixed | brier_gap_change | 3 | -2.96826e-06 | 2.41876e-05 | {"17": 1.7908689541795697e-05, "29": 2.660452194980928e-06, "43": -2.9473921255891364e-05} |
| Tent | Reset parameters + optimizer | 0 | uci_internal_fixed | disagreement_change | 3 | -0.000325521 | 0.000563819 | {"17": -0.0009765625, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + optimizer | 0 | uci_internal_fixed | absolute_error_gap_change | 3 | -0.000325521 | 0.000563819 | {"17": -0.0009765625, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + optimizer | 0 | uci_internal_fixed | nll_gap_change | 3 | -2.61611e-05 | 5.37812e-05 | {"17": 2.2949739964178012e-05, "29": -1.7799686981245094e-05, "43": -8.363321520383433e-05} |
| Tent | Reset parameters + optimizer | 0 | uci_internal_fixed | brier_gap_change | 3 | -2.23542e-06 | 1.90805e-05 | {"17": 1.3939091297097623e-05, "29": 2.633228041880667e-06, "43": -2.3278565454986494e-05} |
| Tent | Reset parameters + optimizer | 4 | uci_internal_fixed | disagreement_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + optimizer | 4 | uci_internal_fixed | absolute_error_gap_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + optimizer | 4 | uci_internal_fixed | nll_gap_change | 3 | -1.7286e-05 | 3.57076e-05 | {"17": 1.6961185307570736e-05, "29": -1.452539129353711e-05, "43": -5.429369370337976e-05} |
| Tent | Reset parameters + optimizer | 4 | uci_internal_fixed | brier_gap_change | 3 | -1.58798e-06 | 1.24235e-05 | {"17": 9.55651940180366e-06, "29": 6.623748391408613e-07, "43": -1.4982836645178674e-05} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | uci_internal_fixed | disagreement_change | 3 | -0.000325521 | 0.000563819 | {"17": -0.0009765625, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | uci_internal_fixed | absolute_error_gap_change | 3 | -0.000325521 | 0.000563819 | {"17": -0.0009765625, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | uci_internal_fixed | nll_gap_change | 3 | -2.61611e-05 | 5.37812e-05 | {"17": 2.2949739964178012e-05, "29": -1.7799686981245094e-05, "43": -8.363321520383433e-05} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | uci_internal_fixed | brier_gap_change | 3 | -2.23542e-06 | 1.90805e-05 | {"17": 1.3939091297097623e-05, "29": 2.633228041880667e-06, "43": -2.3278565454986494e-05} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | uci_internal_fixed | disagreement_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | uci_internal_fixed | absolute_error_gap_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | uci_internal_fixed | nll_gap_change | 3 | -1.7286e-05 | 3.57076e-05 | {"17": 1.6961185307570736e-05, "29": -1.452539129353711e-05, "43": -5.429369370337976e-05} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | uci_internal_fixed | brier_gap_change | 3 | -1.58798e-06 | 1.24235e-05 | {"17": 9.55651940180366e-06, "29": 6.623748391408613e-07, "43": -1.4982836645178674e-05} |


## factorial

| method | intervention | washout_batches | metric | n_panels | mean | sd | ci95_low | ci95_high | n_seeds_min | n_seeds_max | individual_panels |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SAR (complete-state implementation) | Auxiliary: marginal reset effect | 0 | disagreement_factorial | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Auxiliary: marginal reset effect | 0 | absolute_error_gap_factorial | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Auxiliary: marginal reset effect | 0 | nll_gap_factorial | 1 | -5.11548e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": -5.1154820309707665e-05} |
| SAR (complete-state implementation) | Auxiliary: marginal reset effect | 0 | brier_gap_factorial | 1 | -1.3232e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": -1.3231951373542569e-05} |
| SAR (complete-state implementation) | Auxiliary: marginal reset effect | 4 | disagreement_factorial | 1 | -0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0003255208333333333} |
| SAR (complete-state implementation) | Auxiliary: marginal reset effect | 4 | absolute_error_gap_factorial | 1 | -0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0003255208333333333} |
| SAR (complete-state implementation) | Auxiliary: marginal reset effect | 4 | nll_gap_factorial | 1 | 2.92067e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": 2.920671777545e-05} |
| SAR (complete-state implementation) | Auxiliary: marginal reset effect | 4 | brier_gap_factorial | 1 | 4.94772e-06 | — | — | — | 3 | 3 | {"uci_internal_fixed": 4.947722413421267e-06} |
| SAR (complete-state implementation) | Optimizer: marginal reset effect | 0 | disagreement_factorial | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Optimizer: marginal reset effect | 0 | absolute_error_gap_factorial | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Optimizer: marginal reset effect | 0 | nll_gap_factorial | 1 | -9.52979e-09 | — | — | — | 3 | 3 | {"uci_internal_fixed": -9.529789708808781e-09} |
| SAR (complete-state implementation) | Optimizer: marginal reset effect | 0 | brier_gap_factorial | 1 | -5.72878e-09 | — | — | — | 3 | 3 | {"uci_internal_fixed": -5.728783386329169e-09} |
| SAR (complete-state implementation) | Optimizer: marginal reset effect | 4 | disagreement_factorial | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Optimizer: marginal reset effect | 4 | absolute_error_gap_factorial | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Optimizer: marginal reset effect | 4 | nll_gap_factorial | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Optimizer: marginal reset effect | 4 | brier_gap_factorial | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Optimizer × auxiliary interaction | 0 | disagreement_factorial | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Optimizer × auxiliary interaction | 0 | absolute_error_gap_factorial | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Optimizer × auxiliary interaction | 0 | nll_gap_factorial | 1 | 1.90596e-08 | — | — | — | 3 | 3 | {"uci_internal_fixed": 1.9059579417617562e-08} |
| SAR (complete-state implementation) | Optimizer × auxiliary interaction | 0 | brier_gap_factorial | 1 | 1.14576e-08 | — | — | — | 3 | 3 | {"uci_internal_fixed": 1.1457566772658337e-08} |
| SAR (complete-state implementation) | Optimizer × auxiliary interaction | 4 | disagreement_factorial | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Optimizer × auxiliary interaction | 4 | absolute_error_gap_factorial | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Optimizer × auxiliary interaction | 4 | nll_gap_factorial | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Optimizer × auxiliary interaction | 4 | brier_gap_factorial | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Parameters: marginal reset effect | 0 | disagreement_factorial | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Parameters: marginal reset effect | 0 | absolute_error_gap_factorial | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Parameters: marginal reset effect | 0 | nll_gap_factorial | 1 | 6.82561e-07 | — | — | — | 3 | 3 | {"uci_internal_fixed": 6.825607684714125e-07} |
| SAR (complete-state implementation) | Parameters: marginal reset effect | 0 | brier_gap_factorial | 1 | 8.76243e-08 | — | — | — | 3 | 3 | {"uci_internal_fixed": 8.762432252498963e-08} |
| SAR (complete-state implementation) | Parameters: marginal reset effect | 4 | disagreement_factorial | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Parameters: marginal reset effect | 4 | absolute_error_gap_factorial | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Parameters: marginal reset effect | 4 | nll_gap_factorial | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Parameters: marginal reset effect | 4 | brier_gap_factorial | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Parameters × auxiliary interaction | 0 | disagreement_factorial | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Parameters × auxiliary interaction | 0 | absolute_error_gap_factorial | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Parameters × auxiliary interaction | 0 | nll_gap_factorial | 1 | 1.91409e-07 | — | — | — | 3 | 3 | {"uci_internal_fixed": 1.914094570094662e-07} |
| SAR (complete-state implementation) | Parameters × auxiliary interaction | 0 | brier_gap_factorial | 1 | 9.92624e-08 | — | — | — | 3 | 3 | {"uci_internal_fixed": 9.926239673563782e-08} |
| SAR (complete-state implementation) | Parameters × auxiliary interaction | 4 | disagreement_factorial | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Parameters × auxiliary interaction | 4 | absolute_error_gap_factorial | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Parameters × auxiliary interaction | 4 | nll_gap_factorial | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Parameters × auxiliary interaction | 4 | brier_gap_factorial | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Parameters × optimizer interaction | 0 | disagreement_factorial | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Parameters × optimizer interaction | 0 | absolute_error_gap_factorial | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Parameters × optimizer interaction | 0 | nll_gap_factorial | 1 | -7.13126e-10 | — | — | — | 3 | 3 | {"uci_internal_fixed": -7.131255383661476e-10} |
| SAR (complete-state implementation) | Parameters × optimizer interaction | 0 | brier_gap_factorial | 1 | -4.23015e-10 | — | — | — | 3 | 3 | {"uci_internal_fixed": -4.230153166408697e-10} |
| SAR (complete-state implementation) | Parameters × optimizer interaction | 4 | disagreement_factorial | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Parameters × optimizer interaction | 4 | absolute_error_gap_factorial | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Parameters × optimizer interaction | 4 | nll_gap_factorial | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Parameters × optimizer interaction | 4 | brier_gap_factorial | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Three-state interaction | 0 | disagreement_factorial | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Three-state interaction | 0 | absolute_error_gap_factorial | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Three-state interaction | 0 | nll_gap_factorial | 1 | 1.42625e-09 | — | — | — | 3 | 3 | {"uci_internal_fixed": 1.4262510767322951e-09} |
| SAR (complete-state implementation) | Three-state interaction | 0 | brier_gap_factorial | 1 | 8.46031e-10 | — | — | — | 3 | 3 | {"uci_internal_fixed": 8.460306332817394e-10} |
| SAR (complete-state implementation) | Three-state interaction | 4 | disagreement_factorial | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Three-state interaction | 4 | absolute_error_gap_factorial | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Three-state interaction | 4 | nll_gap_factorial | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Three-state interaction | 4 | brier_gap_factorial | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Auxiliary: marginal reset effect | 0 | disagreement_factorial | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Auxiliary: marginal reset effect | 0 | absolute_error_gap_factorial | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Auxiliary: marginal reset effect | 0 | nll_gap_factorial | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Auxiliary: marginal reset effect | 0 | brier_gap_factorial | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Auxiliary: marginal reset effect | 4 | disagreement_factorial | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Auxiliary: marginal reset effect | 4 | absolute_error_gap_factorial | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Auxiliary: marginal reset effect | 4 | nll_gap_factorial | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Auxiliary: marginal reset effect | 4 | brier_gap_factorial | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Optimizer: marginal reset effect | 0 | disagreement_factorial | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Optimizer: marginal reset effect | 0 | absolute_error_gap_factorial | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Optimizer: marginal reset effect | 0 | nll_gap_factorial | 1 | 3.66538e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": 3.665383278231995e-05} |
| Tent | Optimizer: marginal reset effect | 0 | brier_gap_factorial | 1 | 2.35115e-06 | — | — | — | 3 | 3 | {"uci_internal_fixed": 2.3511481071200554e-06} |
| Tent | Optimizer: marginal reset effect | 4 | disagreement_factorial | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Optimizer: marginal reset effect | 4 | absolute_error_gap_factorial | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Optimizer: marginal reset effect | 4 | nll_gap_factorial | 1 | 2.40828e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": 2.4082765516523304e-05} |
| Tent | Optimizer: marginal reset effect | 4 | brier_gap_factorial | 1 | 1.54655e-06 | — | — | — | 3 | 3 | {"uci_internal_fixed": 1.5465519289806565e-06} |
| Tent | Optimizer × auxiliary interaction | 0 | disagreement_factorial | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Optimizer × auxiliary interaction | 0 | absolute_error_gap_factorial | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Optimizer × auxiliary interaction | 0 | nll_gap_factorial | 1 | -1.41172e-22 | — | — | — | 3 | 3 | {"uci_internal_fixed": -1.4117215787571672e-22} |
| Tent | Optimizer × auxiliary interaction | 0 | brier_gap_factorial | 1 | -8.47033e-22 | — | — | — | 3 | 3 | {"uci_internal_fixed": -8.470329472543003e-22} |
| Tent | Optimizer × auxiliary interaction | 4 | disagreement_factorial | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Optimizer × auxiliary interaction | 4 | absolute_error_gap_factorial | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Optimizer × auxiliary interaction | 4 | nll_gap_factorial | 1 | 4.51751e-21 | — | — | — | 3 | 3 | {"uci_internal_fixed": 4.517509052022935e-21} |
| Tent | Optimizer × auxiliary interaction | 4 | brier_gap_factorial | 1 | -1.41172e-22 | — | — | — | 3 | 3 | {"uci_internal_fixed": -1.4117215787571672e-22} |
| Tent | Parameters: marginal reset effect | 0 | disagreement_factorial | 1 | -0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0003255208333333333} |
| Tent | Parameters: marginal reset effect | 0 | absolute_error_gap_factorial | 1 | -0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0003255208333333333} |
| Tent | Parameters: marginal reset effect | 0 | nll_gap_factorial | 1 | -6.28149e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": -6.281488685595376e-05} |
| Tent | Parameters: marginal reset effect | 0 | brier_gap_factorial | 1 | -4.58656e-06 | — | — | — | 3 | 3 | {"uci_internal_fixed": -4.586563479122791e-06} |
| Tent | Parameters: marginal reset effect | 4 | disagreement_factorial | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Parameters: marginal reset effect | 4 | absolute_error_gap_factorial | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Parameters: marginal reset effect | 4 | nll_gap_factorial | 1 | -4.13687e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": -4.136873207963868e-05} |
| Tent | Parameters: marginal reset effect | 4 | brier_gap_factorial | 1 | -3.13453e-06 | — | — | — | 3 | 3 | {"uci_internal_fixed": -3.134532730392041e-06} |
| Tent | Parameters × auxiliary interaction | 0 | disagreement_factorial | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Parameters × auxiliary interaction | 0 | absolute_error_gap_factorial | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Parameters × auxiliary interaction | 0 | nll_gap_factorial | 1 | 1.41172e-22 | — | — | — | 3 | 3 | {"uci_internal_fixed": 1.4117215787571672e-22} |
| Tent | Parameters × auxiliary interaction | 0 | brier_gap_factorial | 1 | 8.47033e-22 | — | — | — | 3 | 3 | {"uci_internal_fixed": 8.470329472543003e-22} |
| Tent | Parameters × auxiliary interaction | 4 | disagreement_factorial | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Parameters × auxiliary interaction | 4 | absolute_error_gap_factorial | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Parameters × auxiliary interaction | 4 | nll_gap_factorial | 1 | -4.51751e-21 | — | — | — | 3 | 3 | {"uci_internal_fixed": -4.517509052022935e-21} |
| Tent | Parameters × auxiliary interaction | 4 | brier_gap_factorial | 1 | 1.41172e-22 | — | — | — | 3 | 3 | {"uci_internal_fixed": 1.4117215787571672e-22} |
| Tent | Parameters × optimizer interaction | 0 | disagreement_factorial | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Parameters × optimizer interaction | 0 | absolute_error_gap_factorial | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Parameters × optimizer interaction | 0 | nll_gap_factorial | 1 | -7.7932e-08 | — | — | — | 3 | 3 | {"uci_internal_fixed": -7.793199405886096e-08} |
| Tent | Parameters × optimizer interaction | 0 | brier_gap_factorial | 1 | -1.11324e-08 | — | — | — | 3 | 3 | {"uci_internal_fixed": -1.1132375633123818e-08} |
| Tent | Parameters × optimizer interaction | 4 | disagreement_factorial | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Parameters × optimizer interaction | 4 | absolute_error_gap_factorial | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Parameters × optimizer interaction | 4 | nll_gap_factorial | 1 | -7.56403e-07 | — | — | — | 3 | 3 | {"uci_internal_fixed": -7.56403465696241e-07} |
| Tent | Parameters × optimizer interaction | 4 | brier_gap_factorial | 1 | -3.32546e-07 | — | — | — | 3 | 3 | {"uci_internal_fixed": -3.3254578137425557e-07} |
| Tent | Three-state interaction | 0 | disagreement_factorial | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Three-state interaction | 0 | absolute_error_gap_factorial | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Three-state interaction | 0 | nll_gap_factorial | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Three-state interaction | 0 | brier_gap_factorial | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Three-state interaction | 4 | disagreement_factorial | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Three-state interaction | 4 | absolute_error_gap_factorial | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Three-state interaction | 4 | nll_gap_factorial | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Three-state interaction | 4 | brier_gap_factorial | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |


### factorial: descriptive seed repetitions

The same image panel is reused across seeds. These standard deviations describe seed variability only; no confidence interval is justified from treating seeds as new image panels.

| method | intervention | washout_batches | panel_id | metric | n_seeds | mean | seed_sd_descriptive | individual_seeds |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SAR (complete-state implementation) | Auxiliary: marginal reset effect | 0 | uci_internal_fixed | disagreement_factorial | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Auxiliary: marginal reset effect | 0 | uci_internal_fixed | absolute_error_gap_factorial | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Auxiliary: marginal reset effect | 0 | uci_internal_fixed | nll_gap_factorial | 3 | -5.11548e-05 | 9.29169e-05 | {"17": -0.00015840807553680055, "29": 4.94361460767756e-06, "43": 0.0} |
| SAR (complete-state implementation) | Auxiliary: marginal reset effect | 0 | uci_internal_fixed | brier_gap_factorial | 3 | -1.3232e-05 | 2.38208e-05 | {"17": -4.073137259270887e-05, "29": 1.035518472081165e-06, "43": 0.0} |
| SAR (complete-state implementation) | Auxiliary: marginal reset effect | 4 | uci_internal_fixed | disagreement_factorial | 3 | -0.000325521 | 0.000563819 | {"17": -0.0009765625, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Auxiliary: marginal reset effect | 4 | uci_internal_fixed | absolute_error_gap_factorial | 3 | -0.000325521 | 0.000563819 | {"17": -0.0009765625, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Auxiliary: marginal reset effect | 4 | uci_internal_fixed | nll_gap_factorial | 3 | 2.92067e-05 | 5.05875e-05 | {"17": 8.762015332635e-05, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Auxiliary: marginal reset effect | 4 | uci_internal_fixed | brier_gap_factorial | 3 | 4.94772e-06 | 8.56971e-06 | {"17": 1.48431672402638e-05, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Optimizer: marginal reset effect | 0 | uci_internal_fixed | disagreement_factorial | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Optimizer: marginal reset effect | 0 | uci_internal_fixed | absolute_error_gap_factorial | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Optimizer: marginal reset effect | 0 | uci_internal_fixed | nll_gap_factorial | 3 | -9.52979e-09 | 1.65061e-08 | {"17": -2.8589369126426345e-08, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Optimizer: marginal reset effect | 0 | uci_internal_fixed | brier_gap_factorial | 3 | -5.72878e-09 | 9.92254e-09 | {"17": -1.7186350158987507e-08, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Optimizer: marginal reset effect | 4 | uci_internal_fixed | disagreement_factorial | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Optimizer: marginal reset effect | 4 | uci_internal_fixed | absolute_error_gap_factorial | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Optimizer: marginal reset effect | 4 | uci_internal_fixed | nll_gap_factorial | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Optimizer: marginal reset effect | 4 | uci_internal_fixed | brier_gap_factorial | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Optimizer × auxiliary interaction | 0 | uci_internal_fixed | disagreement_factorial | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Optimizer × auxiliary interaction | 0 | uci_internal_fixed | absolute_error_gap_factorial | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Optimizer × auxiliary interaction | 0 | uci_internal_fixed | nll_gap_factorial | 3 | 1.90596e-08 | 3.30122e-08 | {"17": 5.717873825285269e-08, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Optimizer × auxiliary interaction | 0 | uci_internal_fixed | brier_gap_factorial | 3 | 1.14576e-08 | 1.98451e-08 | {"17": 3.4372700317975013e-08, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Optimizer × auxiliary interaction | 4 | uci_internal_fixed | disagreement_factorial | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Optimizer × auxiliary interaction | 4 | uci_internal_fixed | absolute_error_gap_factorial | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Optimizer × auxiliary interaction | 4 | uci_internal_fixed | nll_gap_factorial | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Optimizer × auxiliary interaction | 4 | uci_internal_fixed | brier_gap_factorial | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Parameters: marginal reset effect | 0 | uci_internal_fixed | disagreement_factorial | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Parameters: marginal reset effect | 0 | uci_internal_fixed | absolute_error_gap_factorial | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Parameters: marginal reset effect | 0 | uci_internal_fixed | nll_gap_factorial | 3 | 6.82561e-07 | 9.33378e-07 | {"17": 4.517925534580289e-07, "29": -1.1378687791649412e-07, "43": 1.7096766298727029e-06} |
| SAR (complete-state implementation) | Parameters: marginal reset effect | 0 | uci_internal_fixed | brier_gap_factorial | 3 | 8.76243e-08 | 1.50735e-07 | {"17": 1.5784739902918038e-07, "29": -8.540978117810295e-08, "43": 1.9043534972389145e-07} |
| SAR (complete-state implementation) | Parameters: marginal reset effect | 4 | uci_internal_fixed | disagreement_factorial | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Parameters: marginal reset effect | 4 | uci_internal_fixed | absolute_error_gap_factorial | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Parameters: marginal reset effect | 4 | uci_internal_fixed | nll_gap_factorial | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Parameters: marginal reset effect | 4 | uci_internal_fixed | brier_gap_factorial | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Parameters × auxiliary interaction | 0 | uci_internal_fixed | disagreement_factorial | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Parameters × auxiliary interaction | 0 | uci_internal_fixed | absolute_error_gap_factorial | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Parameters × auxiliary interaction | 0 | uci_internal_fixed | nll_gap_factorial | 3 | 1.91409e-07 | 3.31531e-07 | {"17": 5.742283710283986e-07, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Parameters × auxiliary interaction | 0 | uci_internal_fixed | brier_gap_factorial | 3 | 9.92624e-08 | 1.71928e-07 | {"17": 2.9778719020691347e-07, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Parameters × auxiliary interaction | 4 | uci_internal_fixed | disagreement_factorial | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Parameters × auxiliary interaction | 4 | uci_internal_fixed | absolute_error_gap_factorial | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Parameters × auxiliary interaction | 4 | uci_internal_fixed | nll_gap_factorial | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Parameters × auxiliary interaction | 4 | uci_internal_fixed | brier_gap_factorial | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Parameters × optimizer interaction | 0 | uci_internal_fixed | disagreement_factorial | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Parameters × optimizer interaction | 0 | uci_internal_fixed | absolute_error_gap_factorial | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Parameters × optimizer interaction | 0 | uci_internal_fixed | nll_gap_factorial | 3 | -7.13126e-10 | 1.23517e-09 | {"17": -2.1393766150984428e-09, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Parameters × optimizer interaction | 0 | uci_internal_fixed | brier_gap_factorial | 3 | -4.23015e-10 | 7.32684e-10 | {"17": -1.2690459499226092e-09, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Parameters × optimizer interaction | 4 | uci_internal_fixed | disagreement_factorial | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Parameters × optimizer interaction | 4 | uci_internal_fixed | absolute_error_gap_factorial | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Parameters × optimizer interaction | 4 | uci_internal_fixed | nll_gap_factorial | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Parameters × optimizer interaction | 4 | uci_internal_fixed | brier_gap_factorial | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Three-state interaction | 0 | uci_internal_fixed | disagreement_factorial | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Three-state interaction | 0 | uci_internal_fixed | absolute_error_gap_factorial | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Three-state interaction | 0 | uci_internal_fixed | nll_gap_factorial | 3 | 1.42625e-09 | 2.47034e-09 | {"17": 4.2787532301968856e-09, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Three-state interaction | 0 | uci_internal_fixed | brier_gap_factorial | 3 | 8.46031e-10 | 1.46537e-09 | {"17": 2.5380918998452184e-09, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Three-state interaction | 4 | uci_internal_fixed | disagreement_factorial | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Three-state interaction | 4 | uci_internal_fixed | absolute_error_gap_factorial | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Three-state interaction | 4 | uci_internal_fixed | nll_gap_factorial | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Three-state interaction | 4 | uci_internal_fixed | brier_gap_factorial | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Auxiliary: marginal reset effect | 0 | uci_internal_fixed | disagreement_factorial | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Auxiliary: marginal reset effect | 0 | uci_internal_fixed | absolute_error_gap_factorial | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Auxiliary: marginal reset effect | 0 | uci_internal_fixed | nll_gap_factorial | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Auxiliary: marginal reset effect | 0 | uci_internal_fixed | brier_gap_factorial | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Auxiliary: marginal reset effect | 4 | uci_internal_fixed | disagreement_factorial | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Auxiliary: marginal reset effect | 4 | uci_internal_fixed | absolute_error_gap_factorial | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Auxiliary: marginal reset effect | 4 | uci_internal_fixed | nll_gap_factorial | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Auxiliary: marginal reset effect | 4 | uci_internal_fixed | brier_gap_factorial | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Optimizer: marginal reset effect | 0 | uci_internal_fixed | disagreement_factorial | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Optimizer: marginal reset effect | 0 | uci_internal_fixed | absolute_error_gap_factorial | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Optimizer: marginal reset effect | 0 | uci_internal_fixed | nll_gap_factorial | 3 | 3.66538e-05 | 6.38798e-05 | {"17": -1.5051741531300206e-05, "29": 1.694865976714817e-05, "43": 0.00010806458011111187} |
| Tent | Optimizer: marginal reset effect | 0 | uci_internal_fixed | brier_gap_factorial | 3 | 2.35115e-06 | 1.77791e-05 | {"17": -1.3373174685522675e-05, "29": -1.2172056060586259e-06, "43": 2.1643824612941467e-05} |
| Tent | Optimizer: marginal reset effect | 4 | uci_internal_fixed | disagreement_factorial | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Optimizer: marginal reset effect | 4 | uci_internal_fixed | absolute_error_gap_factorial | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Optimizer: marginal reset effect | 4 | uci_internal_fixed | nll_gap_factorial | 3 | 2.40828e-05 | 4.25531e-05 | {"17": -8.436671185692649e-06, "29": 8.442117549955011e-06, "43": 7.224285018530755e-05} |
| Tent | Optimizer: marginal reset effect | 4 | uci_internal_fixed | brier_gap_factorial | 3 | 1.54655e-06 | 1.18866e-05 | {"17": -8.40072899619803e-06, "29": -1.670000503833577e-06, "43": 1.4710385286973576e-05} |
| Tent | Optimizer × auxiliary interaction | 0 | uci_internal_fixed | disagreement_factorial | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Optimizer × auxiliary interaction | 0 | uci_internal_fixed | absolute_error_gap_factorial | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Optimizer × auxiliary interaction | 0 | uci_internal_fixed | nll_gap_factorial | 3 | -1.41172e-22 | 2.44517e-22 | {"17": 0.0, "29": 0.0, "43": -4.235164736271502e-22} |
| Tent | Optimizer × auxiliary interaction | 0 | uci_internal_fixed | brier_gap_factorial | 3 | -8.47033e-22 | 2.24104e-21 | {"17": 0.0, "29": 8.470329472543003e-22, "43": -3.3881317890172014e-21} |
| Tent | Optimizer × auxiliary interaction | 4 | uci_internal_fixed | disagreement_factorial | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Optimizer × auxiliary interaction | 4 | uci_internal_fixed | absolute_error_gap_factorial | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Optimizer × auxiliary interaction | 4 | uci_internal_fixed | nll_gap_factorial | 3 | 4.51751e-21 | 7.82456e-21 | {"17": 0.0, "29": 0.0, "43": 1.3552527156068805e-20} |
| Tent | Optimizer × auxiliary interaction | 4 | uci_internal_fixed | brier_gap_factorial | 3 | -1.41172e-22 | 2.44517e-22 | {"17": 0.0, "29": -4.235164736271502e-22, "43": 0.0} |
| Tent | Parameters: marginal reset effect | 0 | uci_internal_fixed | disagreement_factorial | 3 | -0.000325521 | 0.000563819 | {"17": -0.0009765625, "29": 0.0, "43": 0.0} |
| Tent | Parameters: marginal reset effect | 0 | uci_internal_fixed | absolute_error_gap_factorial | 3 | -0.000325521 | 0.000563819 | {"17": -0.0009765625, "29": 0.0, "43": 0.0} |
| Tent | Parameters: marginal reset effect | 0 | uci_internal_fixed | nll_gap_factorial | 3 | -6.28149e-05 | 0.000117394 | {"17": 3.800148149547822e-05, "29": -3.4748346748393263e-05, "43": -0.00019169779531494623} |
| Tent | Parameters: marginal reset effect | 0 | uci_internal_fixed | brier_gap_factorial | 3 | -4.58656e-06 | 3.6849e-05 | {"17": 2.73122659826203e-05, "29": 3.850433647939293e-06, "43": -4.4922390067927964e-05} |
| Tent | Parameters: marginal reset effect | 4 | uci_internal_fixed | disagreement_factorial | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Parameters: marginal reset effect | 4 | uci_internal_fixed | absolute_error_gap_factorial | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Parameters: marginal reset effect | 4 | uci_internal_fixed | nll_gap_factorial | 3 | -4.13687e-05 | 7.76207e-05 | {"17": 2.5397856493263385e-05, "29": -2.296750884349212e-05, "43": -0.0001265365438886873} |
| Tent | Parameters: marginal reset effect | 4 | uci_internal_fixed | brier_gap_factorial | 3 | -3.13453e-06 | 2.42911e-05 | {"17": 1.795724839800169e-05, "29": 2.332375342974438e-06, "43": -2.969322193215225e-05} |
| Tent | Parameters × auxiliary interaction | 0 | uci_internal_fixed | disagreement_factorial | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Parameters × auxiliary interaction | 0 | uci_internal_fixed | absolute_error_gap_factorial | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Parameters × auxiliary interaction | 0 | uci_internal_fixed | nll_gap_factorial | 3 | 1.41172e-22 | 2.44517e-22 | {"17": 0.0, "29": 0.0, "43": 4.235164736271502e-22} |
| Tent | Parameters × auxiliary interaction | 0 | uci_internal_fixed | brier_gap_factorial | 3 | 8.47033e-22 | 2.24104e-21 | {"17": 0.0, "29": -8.470329472543003e-22, "43": 3.3881317890172014e-21} |
| Tent | Parameters × auxiliary interaction | 4 | uci_internal_fixed | disagreement_factorial | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Parameters × auxiliary interaction | 4 | uci_internal_fixed | absolute_error_gap_factorial | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Parameters × auxiliary interaction | 4 | uci_internal_fixed | nll_gap_factorial | 3 | -4.51751e-21 | 7.82456e-21 | {"17": 0.0, "29": 0.0, "43": -1.3552527156068805e-20} |
| Tent | Parameters × auxiliary interaction | 4 | uci_internal_fixed | brier_gap_factorial | 3 | 1.41172e-22 | 2.44517e-22 | {"17": 0.0, "29": 4.235164736271502e-22, "43": 0.0} |
| Tent | Parameters × optimizer interaction | 0 | uci_internal_fixed | disagreement_factorial | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Parameters × optimizer interaction | 0 | uci_internal_fixed | absolute_error_gap_factorial | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Parameters × optimizer interaction | 0 | uci_internal_fixed | nll_gap_factorial | 3 | -7.7932e-08 | 2.8003e-06 | {"17": 3.1336068825882357e-06, "29": -2.009576140406949e-06, "43": -1.3578267243578696e-06} |
| Tent | Parameters × optimizer interaction | 0 | uci_internal_fixed | brier_gap_factorial | 3 | -1.11324e-08 | 7.59249e-07 | {"17": 8.619537640638247e-07, "29": -3.787544486186945e-07, "43": -5.165964423445017e-07} |
| Tent | Parameters × optimizer interaction | 4 | uci_internal_fixed | disagreement_factorial | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Parameters × optimizer interaction | 4 | uci_internal_fixed | absolute_error_gap_factorial | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Parameters × optimizer interaction | 4 | uci_internal_fixed | nll_gap_factorial | 3 | -7.56403e-07 | 1.41485e-06 | {"17": 7.729625224710268e-07, "29": -2.0186632425124584e-06, "43": -1.0235096770472914e-06} |
| Tent | Parameters × optimizer interaction | 4 | uci_internal_fixed | brier_gap_factorial | 3 | -3.32546e-07 | 3.87673e-07 | {"17": 9.71177124119843e-08, "29": -6.561537040129786e-07, "43": -4.3860135252177246e-07} |
| Tent | Three-state interaction | 0 | uci_internal_fixed | disagreement_factorial | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Three-state interaction | 0 | uci_internal_fixed | absolute_error_gap_factorial | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Three-state interaction | 0 | uci_internal_fixed | nll_gap_factorial | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Three-state interaction | 0 | uci_internal_fixed | brier_gap_factorial | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Three-state interaction | 4 | uci_internal_fixed | disagreement_factorial | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Three-state interaction | 4 | uci_internal_fixed | absolute_error_gap_factorial | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Three-state interaction | 4 | uci_internal_fixed | nll_gap_factorial | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Three-state interaction | 4 | uci_internal_fixed | brier_gap_factorial | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |


## source_reference

| method | intervention | washout_batches | direction | metric | n_panels | mean | sd | ci95_low | ci95_high | n_seeds_min | n_seeds_max | individual_panels |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Normalization only | Reset all declared state | 0 | ab | accuracy_change | 1 | 0.0472005 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.047200520833333336} |
| Normalization only | Reset all declared state | 0 | ab | error_change | 1 | -0.0472005 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.047200520833333336} |
| Normalization only | Reset all declared state | 0 | ab | nll_change | 1 | -0.0380853 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.03808533279304773} |
| Normalization only | Reset all declared state | 0 | ab | brier_change | 1 | -0.0587236 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.058723550560806866} |
| Normalization only | Reset all declared state | 0 | ab | ece15_change | 1 | 0.00217309 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.002173093594947074} |
| Normalization only | Reset all declared state | 0 | ba | accuracy_change | 1 | 0.0472005 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.047200520833333336} |
| Normalization only | Reset all declared state | 0 | ba | error_change | 1 | -0.0472005 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.047200520833333336} |
| Normalization only | Reset all declared state | 0 | ba | nll_change | 1 | -0.0380853 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.03808533279304773} |
| Normalization only | Reset all declared state | 0 | ba | brier_change | 1 | -0.0587236 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.058723550560806866} |
| Normalization only | Reset all declared state | 0 | ba | ece15_change | 1 | 0.00217309 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.002173093594947074} |
| Normalization only | Reset all declared state | 4 | ab | accuracy_change | 1 | 0.0472005 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.047200520833333336} |
| Normalization only | Reset all declared state | 4 | ab | error_change | 1 | -0.0472005 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.047200520833333336} |
| Normalization only | Reset all declared state | 4 | ab | nll_change | 1 | -0.0380853 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.03808533279304773} |
| Normalization only | Reset all declared state | 4 | ab | brier_change | 1 | -0.0587236 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.058723550560806866} |
| Normalization only | Reset all declared state | 4 | ab | ece15_change | 1 | 0.00217309 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.002173093594947074} |
| Normalization only | Reset all declared state | 4 | ba | accuracy_change | 1 | 0.0472005 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.047200520833333336} |
| Normalization only | Reset all declared state | 4 | ba | error_change | 1 | -0.0472005 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.047200520833333336} |
| Normalization only | Reset all declared state | 4 | ba | nll_change | 1 | -0.0380853 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.03808533279304773} |
| Normalization only | Reset all declared state | 4 | ba | brier_change | 1 | -0.0587236 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.058723550560806866} |
| Normalization only | Reset all declared state | 4 | ba | ece15_change | 1 | 0.00217309 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.002173093594947074} |
| Normalization only | No external reset | 0 | ab | accuracy_change | 1 | 0.0472005 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.047200520833333336} |
| Normalization only | No external reset | 0 | ab | error_change | 1 | -0.0472005 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.047200520833333336} |
| Normalization only | No external reset | 0 | ab | nll_change | 1 | -0.0380853 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.03808533279304773} |
| Normalization only | No external reset | 0 | ab | brier_change | 1 | -0.0587236 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.058723550560806866} |
| Normalization only | No external reset | 0 | ab | ece15_change | 1 | 0.00217309 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.002173093594947074} |
| Normalization only | No external reset | 0 | ba | accuracy_change | 1 | 0.0472005 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.047200520833333336} |
| Normalization only | No external reset | 0 | ba | error_change | 1 | -0.0472005 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.047200520833333336} |
| Normalization only | No external reset | 0 | ba | nll_change | 1 | -0.0380853 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.03808533279304773} |
| Normalization only | No external reset | 0 | ba | brier_change | 1 | -0.0587236 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.058723550560806866} |
| Normalization only | No external reset | 0 | ba | ece15_change | 1 | 0.00217309 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.002173093594947074} |
| Normalization only | No external reset | 4 | ab | accuracy_change | 1 | 0.0472005 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.047200520833333336} |
| Normalization only | No external reset | 4 | ab | error_change | 1 | -0.0472005 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.047200520833333336} |
| Normalization only | No external reset | 4 | ab | nll_change | 1 | -0.0380853 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.03808533279304773} |
| Normalization only | No external reset | 4 | ab | brier_change | 1 | -0.0587236 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.058723550560806866} |
| Normalization only | No external reset | 4 | ab | ece15_change | 1 | 0.00217309 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.002173093594947074} |
| Normalization only | No external reset | 4 | ba | accuracy_change | 1 | 0.0472005 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.047200520833333336} |
| Normalization only | No external reset | 4 | ba | error_change | 1 | -0.0472005 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.047200520833333336} |
| Normalization only | No external reset | 4 | ba | nll_change | 1 | -0.0380853 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.03808533279304773} |
| Normalization only | No external reset | 4 | ba | brier_change | 1 | -0.0587236 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.058723550560806866} |
| Normalization only | No external reset | 4 | ba | ece15_change | 1 | 0.00217309 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.002173093594947074} |
| SAR (complete-state implementation) | Reset all declared state | 0 | ab | accuracy_change | 1 | 0.047526 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.047526041666666664} |
| SAR (complete-state implementation) | Reset all declared state | 0 | ab | error_change | 1 | -0.047526 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.047526041666666664} |
| SAR (complete-state implementation) | Reset all declared state | 0 | ab | nll_change | 1 | -0.0381867 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.038186730746273545} |
| SAR (complete-state implementation) | Reset all declared state | 0 | ab | brier_change | 1 | -0.0588159 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.05881585402265165} |
| SAR (complete-state implementation) | Reset all declared state | 0 | ab | ece15_change | 1 | 0.0019071 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0019071049668720706} |
| SAR (complete-state implementation) | Reset all declared state | 0 | ba | accuracy_change | 1 | 0.047526 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.047526041666666664} |
| SAR (complete-state implementation) | Reset all declared state | 0 | ba | error_change | 1 | -0.047526 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.047526041666666664} |
| SAR (complete-state implementation) | Reset all declared state | 0 | ba | nll_change | 1 | -0.0381867 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.038186730746273545} |
| SAR (complete-state implementation) | Reset all declared state | 0 | ba | brier_change | 1 | -0.0588159 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.05881585402265165} |
| SAR (complete-state implementation) | Reset all declared state | 0 | ba | ece15_change | 1 | 0.0019071 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0019071049668720706} |
| SAR (complete-state implementation) | Reset all declared state | 4 | ab | accuracy_change | 1 | 0.047526 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.047526041666666664} |
| SAR (complete-state implementation) | Reset all declared state | 4 | ab | error_change | 1 | -0.047526 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.047526041666666664} |
| SAR (complete-state implementation) | Reset all declared state | 4 | ab | nll_change | 1 | -0.0381867 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.038186730746273545} |
| SAR (complete-state implementation) | Reset all declared state | 4 | ab | brier_change | 1 | -0.0588159 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.05881585402265165} |
| SAR (complete-state implementation) | Reset all declared state | 4 | ab | ece15_change | 1 | 0.0019071 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0019071049668720706} |
| SAR (complete-state implementation) | Reset all declared state | 4 | ba | accuracy_change | 1 | 0.047526 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.047526041666666664} |
| SAR (complete-state implementation) | Reset all declared state | 4 | ba | error_change | 1 | -0.047526 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.047526041666666664} |
| SAR (complete-state implementation) | Reset all declared state | 4 | ba | nll_change | 1 | -0.0381867 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.038186730746273545} |
| SAR (complete-state implementation) | Reset all declared state | 4 | ba | brier_change | 1 | -0.0588159 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.05881585402265165} |
| SAR (complete-state implementation) | Reset all declared state | 4 | ba | ece15_change | 1 | 0.0019071 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0019071049668720706} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | ab | accuracy_change | 1 | 0.047526 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.047526041666666664} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | ab | error_change | 1 | -0.047526 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.047526041666666664} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | ab | nll_change | 1 | -0.0381878 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.038187757456239} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | ab | brier_change | 1 | -0.0588161 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.05881609694691877} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | ab | ece15_change | 1 | 0.00190804 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0019080438952181016} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | ba | accuracy_change | 1 | 0.047526 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.047526041666666664} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | ba | error_change | 1 | -0.047526 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.047526041666666664} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | ba | nll_change | 1 | -0.038187 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.03818697919074202} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | ba | brier_change | 1 | -0.058816 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.05881595969139786} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | ba | ece15_change | 1 | 0.00190729 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0019072909482190832} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | ab | accuracy_change | 1 | 0.047526 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.047526041666666664} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | ab | error_change | 1 | -0.047526 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.047526041666666664} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | ab | nll_change | 1 | -0.0381867 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.038186730746273545} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | ab | brier_change | 1 | -0.0588159 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.05881585402265165} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | ab | ece15_change | 1 | 0.0019071 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0019071049668720706} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | ba | accuracy_change | 1 | 0.047526 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.047526041666666664} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | ba | error_change | 1 | -0.047526 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.047526041666666664} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | ba | nll_change | 1 | -0.0381867 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.038186730746273545} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | ba | brier_change | 1 | -0.0588159 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.05881585402265165} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | ba | ece15_change | 1 | 0.0019071 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0019071049668720706} |
| SAR (complete-state implementation) | No external reset | 0 | ab | accuracy_change | 1 | 0.0472005 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.047200520833333336} |
| SAR (complete-state implementation) | No external reset | 0 | ab | error_change | 1 | -0.0472005 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.047200520833333336} |
| SAR (complete-state implementation) | No external reset | 0 | ab | nll_change | 1 | -0.0379925 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.037992542645602236} |
| SAR (complete-state implementation) | No external reset | 0 | ab | brier_change | 1 | -0.0587095 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.05870954119212967} |
| SAR (complete-state implementation) | No external reset | 0 | ab | ece15_change | 1 | 0.0021784 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0021784023704459663} |
| SAR (complete-state implementation) | No external reset | 0 | ba | accuracy_change | 1 | 0.0472005 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.047200520833333336} |
| SAR (complete-state implementation) | No external reset | 0 | ba | error_change | 1 | -0.0472005 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.047200520833333336} |
| SAR (complete-state implementation) | No external reset | 0 | ba | nll_change | 1 | -0.038043 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.03804302407837043} |
| SAR (complete-state implementation) | No external reset | 0 | ba | brier_change | 1 | -0.0587227 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.05872269103645639} |
| SAR (complete-state implementation) | No external reset | 0 | ba | ece15_change | 1 | 0.00217854 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.002178537737461327} |
| SAR (complete-state implementation) | No external reset | 4 | ab | accuracy_change | 1 | 0.0472005 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.047200520833333336} |
| SAR (complete-state implementation) | No external reset | 4 | ab | error_change | 1 | -0.0472005 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.047200520833333336} |
| SAR (complete-state implementation) | No external reset | 4 | ab | nll_change | 1 | -0.0377731 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.03777308177964017} |
| SAR (complete-state implementation) | No external reset | 4 | ab | brier_change | 1 | -0.0586821 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.05868206399649482} |
| SAR (complete-state implementation) | No external reset | 4 | ab | ece15_change | 1 | 0.0022123 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0022122968296950513} |
| SAR (complete-state implementation) | No external reset | 4 | ba | accuracy_change | 1 | 0.047526 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.047526041666666664} |
| SAR (complete-state implementation) | No external reset | 4 | ba | error_change | 1 | -0.047526 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.047526041666666664} |
| SAR (complete-state implementation) | No external reset | 4 | ba | nll_change | 1 | -0.0377439 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.03774387506186472} |
| SAR (complete-state implementation) | No external reset | 4 | ba | brier_change | 1 | -0.0586771 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.05867711627408139} |
| SAR (complete-state implementation) | No external reset | 4 | ba | ece15_change | 1 | 0.00188879 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0018887860635977693} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | ab | accuracy_change | 1 | 0.0472005 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.047200520833333336} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | ab | error_change | 1 | -0.0472005 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.047200520833333336} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | ab | nll_change | 1 | -0.0379925 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.03799253972521555} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | ab | brier_change | 1 | -0.0587095 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.058709541186235635} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | ab | ece15_change | 1 | 0.0021784 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0021783994542324825} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | ba | accuracy_change | 1 | 0.0472005 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.047200520833333336} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | ba | error_change | 1 | -0.0472005 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.047200520833333336} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | ba | nll_change | 1 | -0.038043 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.038043002811529864} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | ba | brier_change | 1 | -0.0587227 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.058722679996010885} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | ba | ece15_change | 1 | 0.00217853 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.00217852617596441} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | ab | accuracy_change | 1 | 0.0472005 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.047200520833333336} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | ab | error_change | 1 | -0.0472005 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.047200520833333336} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | ab | nll_change | 1 | -0.0377731 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.03777308177964017} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | ab | brier_change | 1 | -0.0586821 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.05868206399649482} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | ab | ece15_change | 1 | 0.0022123 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0022122968296950513} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | ba | accuracy_change | 1 | 0.047526 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.047526041666666664} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | ba | error_change | 1 | -0.047526 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.047526041666666664} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | ba | nll_change | 1 | -0.0377439 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.03774387506186472} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | ba | brier_change | 1 | -0.0586771 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.05867711627408139} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | ba | ece15_change | 1 | 0.00188879 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0018887860635977693} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | ab | accuracy_change | 1 | 0.047526 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.047526041666666664} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | ab | error_change | 1 | -0.047526 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.047526041666666664} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | ab | nll_change | 1 | -0.0381878 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.038187757456239} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | ab | brier_change | 1 | -0.0588161 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.05881609694691877} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | ab | ece15_change | 1 | 0.00190804 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0019080438952181016} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | ba | accuracy_change | 1 | 0.047526 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.047526041666666664} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | ba | error_change | 1 | -0.047526 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.047526041666666664} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | ba | nll_change | 1 | -0.038187 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.03818697919074202} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | ba | brier_change | 1 | -0.058816 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.05881595969139786} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | ba | ece15_change | 1 | 0.00190729 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0019072909482190832} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | ab | accuracy_change | 1 | 0.047526 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.047526041666666664} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | ab | error_change | 1 | -0.047526 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.047526041666666664} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | ab | nll_change | 1 | -0.0381867 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.038186730746273545} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | ab | brier_change | 1 | -0.0588159 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.05881585402265165} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | ab | ece15_change | 1 | 0.0019071 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0019071049668720706} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | ba | accuracy_change | 1 | 0.047526 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.047526041666666664} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | ba | error_change | 1 | -0.047526 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.047526041666666664} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | ba | nll_change | 1 | -0.0381867 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.038186730746273545} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | ba | brier_change | 1 | -0.0588159 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.05881585402265165} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | ba | ece15_change | 1 | 0.0019071 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0019071049668720706} |
| SAR (complete-state implementation) | Reset parameters only | 0 | ab | accuracy_change | 1 | 0.0472005 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.047200520833333336} |
| SAR (complete-state implementation) | Reset parameters only | 0 | ab | error_change | 1 | -0.0472005 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.047200520833333336} |
| SAR (complete-state implementation) | Reset parameters only | 0 | ab | nll_change | 1 | -0.0379915 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.03799148062830334} |
| SAR (complete-state implementation) | Reset parameters only | 0 | ab | brier_change | 1 | -0.0587093 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.05870929844855327} |
| SAR (complete-state implementation) | Reset parameters only | 0 | ab | ece15_change | 1 | 0.00217743 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.002177428043642071} |
| SAR (complete-state implementation) | Reset parameters only | 0 | ba | accuracy_change | 1 | 0.0472005 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.047200520833333336} |
| SAR (complete-state implementation) | Reset parameters only | 0 | ba | error_change | 1 | -0.0472005 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.047200520833333336} |
| SAR (complete-state implementation) | Reset parameters only | 0 | ba | nll_change | 1 | -0.0380425 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.03804254963023704} |
| SAR (complete-state implementation) | Reset parameters only | 0 | ba | brier_change | 1 | -0.0587225 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.05872248670901948} |
| SAR (complete-state implementation) | Reset parameters only | 0 | ba | ece15_change | 1 | 0.00217818 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0021781785682487655} |
| SAR (complete-state implementation) | Reset parameters only | 4 | ab | accuracy_change | 1 | 0.0472005 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.047200520833333336} |
| SAR (complete-state implementation) | Reset parameters only | 4 | ab | error_change | 1 | -0.0472005 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.047200520833333336} |
| SAR (complete-state implementation) | Reset parameters only | 4 | ab | nll_change | 1 | -0.0377731 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.03777308177964017} |
| SAR (complete-state implementation) | Reset parameters only | 4 | ab | brier_change | 1 | -0.0586821 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.05868206399649482} |
| SAR (complete-state implementation) | Reset parameters only | 4 | ab | ece15_change | 1 | 0.0022123 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0022122968296950513} |
| SAR (complete-state implementation) | Reset parameters only | 4 | ba | accuracy_change | 1 | 0.047526 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.047526041666666664} |
| SAR (complete-state implementation) | Reset parameters only | 4 | ba | error_change | 1 | -0.047526 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.047526041666666664} |
| SAR (complete-state implementation) | Reset parameters only | 4 | ba | nll_change | 1 | -0.0377439 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.03774387506186472} |
| SAR (complete-state implementation) | Reset parameters only | 4 | ba | brier_change | 1 | -0.0586771 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.05867711627408139} |
| SAR (complete-state implementation) | Reset parameters only | 4 | ba | ece15_change | 1 | 0.00188879 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0018887860635977693} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | ab | accuracy_change | 1 | 0.047526 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.047526041666666664} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | ab | error_change | 1 | -0.047526 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.047526041666666664} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | ab | nll_change | 1 | -0.0381867 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.038186730746273545} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | ab | brier_change | 1 | -0.0588159 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.05881585402265165} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | ab | ece15_change | 1 | 0.0019071 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0019071049668720706} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | ba | accuracy_change | 1 | 0.047526 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.047526041666666664} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | ba | error_change | 1 | -0.047526 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.047526041666666664} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | ba | nll_change | 1 | -0.0381867 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.038186730746273545} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | ba | brier_change | 1 | -0.0588159 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.05881585402265165} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | ba | ece15_change | 1 | 0.0019071 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0019071049668720706} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | ab | accuracy_change | 1 | 0.047526 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.047526041666666664} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | ab | error_change | 1 | -0.047526 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.047526041666666664} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | ab | nll_change | 1 | -0.0381867 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.038186730746273545} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | ab | brier_change | 1 | -0.0588159 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.05881585402265165} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | ab | ece15_change | 1 | 0.0019071 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0019071049668720706} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | ba | accuracy_change | 1 | 0.047526 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.047526041666666664} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | ba | error_change | 1 | -0.047526 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.047526041666666664} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | ba | nll_change | 1 | -0.0381867 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.038186730746273545} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | ba | brier_change | 1 | -0.0588159 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.05881585402265165} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | ba | ece15_change | 1 | 0.0019071 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0019071049668720706} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | ab | accuracy_change | 1 | 0.0472005 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.047200520833333336} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | ab | error_change | 1 | -0.0472005 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.047200520833333336} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | ab | nll_change | 1 | -0.0379915 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.03799147746054029} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | ab | brier_change | 1 | -0.0587093 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.05870929843608683} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | ab | ece15_change | 1 | 0.00217742 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.002177424882155323} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | ba | accuracy_change | 1 | 0.0472005 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.047200520833333336} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | ba | error_change | 1 | -0.0472005 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.047200520833333336} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | ba | nll_change | 1 | -0.0380425 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.03804252668976902} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | ba | brier_change | 1 | -0.0587225 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.05872247481597095} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | ba | ece15_change | 1 | 0.00217817 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.002178165730750465} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | ab | accuracy_change | 1 | 0.0472005 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.047200520833333336} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | ab | error_change | 1 | -0.0472005 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.047200520833333336} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | ab | nll_change | 1 | -0.0377731 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.03777308177964017} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | ab | brier_change | 1 | -0.0586821 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.05868206399649482} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | ab | ece15_change | 1 | 0.0022123 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0022122968296950513} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | ba | accuracy_change | 1 | 0.047526 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.047526041666666664} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | ba | error_change | 1 | -0.047526 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.047526041666666664} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | ba | nll_change | 1 | -0.0377439 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.03774387506186472} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | ba | brier_change | 1 | -0.0586771 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.05867711627408139} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | ba | ece15_change | 1 | 0.00188879 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0018887860635977693} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | ab | accuracy_change | 1 | 0.047526 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.047526041666666664} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | ab | error_change | 1 | -0.047526 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.047526041666666664} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | ab | nll_change | 1 | -0.0381867 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.038186730746273545} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | ab | brier_change | 1 | -0.0588159 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.05881585402265165} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | ab | ece15_change | 1 | 0.0019071 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0019071049668720706} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | ba | accuracy_change | 1 | 0.047526 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.047526041666666664} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | ba | error_change | 1 | -0.047526 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.047526041666666664} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | ba | nll_change | 1 | -0.0381867 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.038186730746273545} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | ba | brier_change | 1 | -0.0588159 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.05881585402265165} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | ba | ece15_change | 1 | 0.0019071 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0019071049668720706} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | ab | accuracy_change | 1 | 0.047526 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.047526041666666664} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | ab | error_change | 1 | -0.047526 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.047526041666666664} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | ab | nll_change | 1 | -0.0381867 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.038186730746273545} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | ab | brier_change | 1 | -0.0588159 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.05881585402265165} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | ab | ece15_change | 1 | 0.0019071 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0019071049668720706} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | ba | accuracy_change | 1 | 0.047526 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.047526041666666664} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | ba | error_change | 1 | -0.047526 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.047526041666666664} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | ba | nll_change | 1 | -0.0381867 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.038186730746273545} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | ba | brier_change | 1 | -0.0588159 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.05881585402265165} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | ba | ece15_change | 1 | 0.0019071 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0019071049668720706} |
| Tent | Reset all declared state | 0 | ab | accuracy_change | 1 | 0.047526 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.047526041666666664} |
| Tent | Reset all declared state | 0 | ab | error_change | 1 | -0.047526 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.047526041666666664} |
| Tent | Reset all declared state | 0 | ab | nll_change | 1 | -0.0377331 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.037733146587648} |
| Tent | Reset all declared state | 0 | ab | brier_change | 1 | -0.0587119 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.05871193303859365} |
| Tent | Reset all declared state | 0 | ab | ece15_change | 1 | 0.00192471 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0019247136873351} |
| Tent | Reset all declared state | 0 | ba | accuracy_change | 1 | 0.047526 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.047526041666666664} |
| Tent | Reset all declared state | 0 | ba | error_change | 1 | -0.047526 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.047526041666666664} |
| Tent | Reset all declared state | 0 | ba | nll_change | 1 | -0.0377331 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.037733146587648} |
| Tent | Reset all declared state | 0 | ba | brier_change | 1 | -0.0587119 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.05871193303859365} |
| Tent | Reset all declared state | 0 | ba | ece15_change | 1 | 0.00192471 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0019247136873351} |
| Tent | Reset all declared state | 4 | ab | accuracy_change | 1 | 0.047526 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.047526041666666664} |
| Tent | Reset all declared state | 4 | ab | error_change | 1 | -0.047526 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.047526041666666664} |
| Tent | Reset all declared state | 4 | ab | nll_change | 1 | -0.0377331 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.037733146587648} |
| Tent | Reset all declared state | 4 | ab | brier_change | 1 | -0.0587119 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.05871193303859365} |
| Tent | Reset all declared state | 4 | ab | ece15_change | 1 | 0.00192471 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0019247136873351} |
| Tent | Reset all declared state | 4 | ba | accuracy_change | 1 | 0.047526 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.047526041666666664} |
| Tent | Reset all declared state | 4 | ba | error_change | 1 | -0.047526 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.047526041666666664} |
| Tent | Reset all declared state | 4 | ba | nll_change | 1 | -0.0377331 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.037733146587648} |
| Tent | Reset all declared state | 4 | ba | brier_change | 1 | -0.0587119 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.05871193303859365} |
| Tent | Reset all declared state | 4 | ba | ece15_change | 1 | 0.00192471 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0019247136873351} |
| Tent | Reset auxiliary state only | 0 | ab | accuracy_change | 1 | 0.0478516 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0478515625} |
| Tent | Reset auxiliary state only | 0 | ab | error_change | 1 | -0.0478516 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0478515625} |
| Tent | Reset auxiliary state only | 0 | ab | nll_change | 1 | -0.0379482 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.037948162549730706} |
| Tent | Reset auxiliary state only | 0 | ab | brier_change | 1 | -0.0587858 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.05878580592817149} |
| Tent | Reset auxiliary state only | 0 | ab | ece15_change | 1 | 0.00227145 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0022714454791524646} |
| Tent | Reset auxiliary state only | 0 | ba | accuracy_change | 1 | 0.047526 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.047526041666666664} |
| Tent | Reset auxiliary state only | 0 | ba | error_change | 1 | -0.047526 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.047526041666666664} |
| Tent | Reset auxiliary state only | 0 | ba | nll_change | 1 | -0.0379743 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.037974323603804316} |
| Tent | Reset auxiliary state only | 0 | ba | brier_change | 1 | -0.058788 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.058788041343543505} |
| Tent | Reset auxiliary state only | 0 | ba | ece15_change | 1 | 0.0024227 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0024227032321630835} |
| Tent | Reset auxiliary state only | 4 | ab | accuracy_change | 1 | 0.0481771 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.048177083333333336} |
| Tent | Reset auxiliary state only | 4 | ab | error_change | 1 | -0.0481771 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.048177083333333336} |
| Tent | Reset auxiliary state only | 4 | ab | nll_change | 1 | -0.0374637 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.037463659744955864} |
| Tent | Reset auxiliary state only | 4 | ab | brier_change | 1 | -0.0587313 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.05873132494765942} |
| Tent | Reset auxiliary state only | 4 | ab | ece15_change | 1 | 0.00212155 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0021215481582880316} |
| Tent | Reset auxiliary state only | 4 | ba | accuracy_change | 1 | 0.0481771 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.048177083333333336} |
| Tent | Reset auxiliary state only | 4 | ba | error_change | 1 | -0.0481771 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.048177083333333336} |
| Tent | Reset auxiliary state only | 4 | ba | nll_change | 1 | -0.0374809 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.037480945711519026} |
| Tent | Reset auxiliary state only | 4 | ba | brier_change | 1 | -0.0587329 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.058732912928460806} |
| Tent | Reset auxiliary state only | 4 | ba | ece15_change | 1 | 0.00211314 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.002113137194051632} |
| Tent | No external reset | 0 | ab | accuracy_change | 1 | 0.0478516 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0478515625} |
| Tent | No external reset | 0 | ab | error_change | 1 | -0.0478516 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0478515625} |
| Tent | No external reset | 0 | ab | nll_change | 1 | -0.0379482 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.037948162549730706} |
| Tent | No external reset | 0 | ab | brier_change | 1 | -0.0587858 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.05878580592817149} |
| Tent | No external reset | 0 | ab | ece15_change | 1 | 0.00227145 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0022714454791524646} |
| Tent | No external reset | 0 | ba | accuracy_change | 1 | 0.047526 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.047526041666666664} |
| Tent | No external reset | 0 | ba | error_change | 1 | -0.047526 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.047526041666666664} |
| Tent | No external reset | 0 | ba | nll_change | 1 | -0.0379743 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.037974323603804316} |
| Tent | No external reset | 0 | ba | brier_change | 1 | -0.058788 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.058788041343543505} |
| Tent | No external reset | 0 | ba | ece15_change | 1 | 0.0024227 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0024227032321630835} |
| Tent | No external reset | 4 | ab | accuracy_change | 1 | 0.0481771 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.048177083333333336} |
| Tent | No external reset | 4 | ab | error_change | 1 | -0.0481771 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.048177083333333336} |
| Tent | No external reset | 4 | ab | nll_change | 1 | -0.0374637 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.037463659744955864} |
| Tent | No external reset | 4 | ab | brier_change | 1 | -0.0587313 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.05873132494765942} |
| Tent | No external reset | 4 | ab | ece15_change | 1 | 0.00212155 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0021215481582880316} |
| Tent | No external reset | 4 | ba | accuracy_change | 1 | 0.0481771 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.048177083333333336} |
| Tent | No external reset | 4 | ba | error_change | 1 | -0.0481771 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.048177083333333336} |
| Tent | No external reset | 4 | ba | nll_change | 1 | -0.0374809 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.037480945711519026} |
| Tent | No external reset | 4 | ba | brier_change | 1 | -0.0587329 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.058732912928460806} |
| Tent | No external reset | 4 | ba | ece15_change | 1 | 0.00211314 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.002113137194051632} |
| Tent | Reset optimizer only | 0 | ab | accuracy_change | 1 | 0.0478516 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0478515625} |
| Tent | Reset optimizer only | 0 | ab | error_change | 1 | -0.0478516 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0478515625} |
| Tent | Reset optimizer only | 0 | ab | nll_change | 1 | -0.0378581 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.03785811472227534} |
| Tent | Reset optimizer only | 0 | ab | brier_change | 1 | -0.0587657 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.05876574000497284} |
| Tent | Reset optimizer only | 0 | ab | ece15_change | 1 | 0.002042 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0020420025360577687} |
| Tent | Reset optimizer only | 0 | ba | accuracy_change | 1 | 0.047526 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.047526041666666664} |
| Tent | Reset optimizer only | 0 | ba | error_change | 1 | -0.047526 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.047526041666666664} |
| Tent | Reset optimizer only | 0 | ba | nll_change | 1 | -0.037921 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.037920968575128326} |
| Tent | Reset optimizer only | 0 | ba | brier_change | 1 | -0.0587703 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.05877033213463975} |
| Tent | Reset optimizer only | 0 | ba | ece15_change | 1 | 0.00218176 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0021817574464413534} |
| Tent | Reset optimizer only | 4 | ab | accuracy_change | 1 | 0.0481771 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.048177083333333336} |
| Tent | Reset optimizer only | 4 | ab | error_change | 1 | -0.0481771 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.048177083333333336} |
| Tent | Reset optimizer only | 4 | ab | nll_change | 1 | -0.0378228 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.03782277741195004} |
| Tent | Reset optimizer only | 4 | ab | brier_change | 1 | -0.0587778 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.05877784994190096} |
| Tent | Reset optimizer only | 4 | ab | ece15_change | 1 | 0.00191103 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0019110348899425654} |
| Tent | Reset optimizer only | 4 | ba | accuracy_change | 1 | 0.0481771 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.048177083333333336} |
| Tent | Reset optimizer only | 4 | ba | error_change | 1 | -0.0481771 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.048177083333333336} |
| Tent | Reset optimizer only | 4 | ba | nll_change | 1 | -0.0378645 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.03786452434576252} |
| Tent | Reset optimizer only | 4 | ba | brier_change | 1 | -0.0587812 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.05878115074752203} |
| Tent | Reset optimizer only | 4 | ba | ece15_change | 1 | 0.00211483 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0021148326163717515} |
| Tent | Reset optimizer + auxiliary state | 0 | ab | accuracy_change | 1 | 0.0478516 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0478515625} |
| Tent | Reset optimizer + auxiliary state | 0 | ab | error_change | 1 | -0.0478516 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0478515625} |
| Tent | Reset optimizer + auxiliary state | 0 | ab | nll_change | 1 | -0.0378581 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.03785811472227534} |
| Tent | Reset optimizer + auxiliary state | 0 | ab | brier_change | 1 | -0.0587657 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.05876574000497284} |
| Tent | Reset optimizer + auxiliary state | 0 | ab | ece15_change | 1 | 0.002042 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0020420025360577687} |
| Tent | Reset optimizer + auxiliary state | 0 | ba | accuracy_change | 1 | 0.047526 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.047526041666666664} |
| Tent | Reset optimizer + auxiliary state | 0 | ba | error_change | 1 | -0.047526 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.047526041666666664} |
| Tent | Reset optimizer + auxiliary state | 0 | ba | nll_change | 1 | -0.037921 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.037920968575128326} |
| Tent | Reset optimizer + auxiliary state | 0 | ba | brier_change | 1 | -0.0587703 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.05877033213463975} |
| Tent | Reset optimizer + auxiliary state | 0 | ba | ece15_change | 1 | 0.00218176 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0021817574464413534} |
| Tent | Reset optimizer + auxiliary state | 4 | ab | accuracy_change | 1 | 0.0481771 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.048177083333333336} |
| Tent | Reset optimizer + auxiliary state | 4 | ab | error_change | 1 | -0.0481771 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.048177083333333336} |
| Tent | Reset optimizer + auxiliary state | 4 | ab | nll_change | 1 | -0.0378228 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.03782277741195004} |
| Tent | Reset optimizer + auxiliary state | 4 | ab | brier_change | 1 | -0.0587778 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.05877784994190096} |
| Tent | Reset optimizer + auxiliary state | 4 | ab | ece15_change | 1 | 0.00191103 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0019110348899425654} |
| Tent | Reset optimizer + auxiliary state | 4 | ba | accuracy_change | 1 | 0.0481771 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.048177083333333336} |
| Tent | Reset optimizer + auxiliary state | 4 | ba | error_change | 1 | -0.0481771 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.048177083333333336} |
| Tent | Reset optimizer + auxiliary state | 4 | ba | nll_change | 1 | -0.0378645 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.03786452434576252} |
| Tent | Reset optimizer + auxiliary state | 4 | ba | brier_change | 1 | -0.0587812 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.05878115074752203} |
| Tent | Reset optimizer + auxiliary state | 4 | ba | ece15_change | 1 | 0.00211483 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0021148326163717515} |
| Tent | Reset parameters only | 0 | ab | accuracy_change | 1 | 0.047526 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.047526041666666664} |
| Tent | Reset parameters only | 0 | ab | error_change | 1 | -0.047526 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.047526041666666664} |
| Tent | Reset parameters only | 0 | ab | nll_change | 1 | -0.0378239 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.037823922084737616} |
| Tent | Reset parameters only | 0 | ab | brier_change | 1 | -0.0587325 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.05873245279020551} |
| Tent | Reset parameters only | 0 | ab | ece15_change | 1 | 0.00193749 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0019374924028786138} |
| Tent | Reset parameters only | 0 | ba | accuracy_change | 1 | 0.047526 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.047526041666666664} |
| Tent | Reset parameters only | 0 | ba | error_change | 1 | -0.047526 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.047526041666666664} |
| Tent | Reset parameters only | 0 | ba | nll_change | 1 | -0.0377873 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.037787307217952266} |
| Tent | Reset parameters only | 0 | ba | brier_change | 1 | -0.0587301 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0587301072082862} |
| Tent | Reset parameters only | 0 | ba | ece15_change | 1 | 0.00194853 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0019485262054475723} |
| Tent | Reset parameters only | 4 | ab | accuracy_change | 1 | 0.047526 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.047526041666666664} |
| Tent | Reset parameters only | 4 | ab | error_change | 1 | -0.047526 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.047526041666666664} |
| Tent | Reset parameters only | 4 | ab | nll_change | 1 | -0.0373768 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.03737684804167177} |
| Tent | Reset parameters only | 4 | ab | brier_change | 1 | -0.0586665 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.05866650773419233} |
| Tent | Reset parameters only | 4 | ab | ece15_change | 1 | 0.00197852 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0019785216999366473} |
| Tent | Reset parameters only | 4 | ba | accuracy_change | 1 | 0.047526 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.047526041666666664} |
| Tent | Reset parameters only | 4 | ba | error_change | 1 | -0.047526 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.047526041666666664} |
| Tent | Reset parameters only | 4 | ba | nll_change | 1 | -0.0373531 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.03735314347788806} |
| Tent | Reset parameters only | 4 | ba | brier_change | 1 | -0.0586651 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.05866512745515401} |
| Tent | Reset parameters only | 4 | ba | ece15_change | 1 | 0.00181216 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0018121627993138805} |
| Tent | Reset parameters + auxiliary state | 0 | ab | accuracy_change | 1 | 0.047526 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.047526041666666664} |
| Tent | Reset parameters + auxiliary state | 0 | ab | error_change | 1 | -0.047526 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.047526041666666664} |
| Tent | Reset parameters + auxiliary state | 0 | ab | nll_change | 1 | -0.0378239 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.037823922084737616} |
| Tent | Reset parameters + auxiliary state | 0 | ab | brier_change | 1 | -0.0587325 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.05873245279020551} |
| Tent | Reset parameters + auxiliary state | 0 | ab | ece15_change | 1 | 0.00193749 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0019374924028786138} |
| Tent | Reset parameters + auxiliary state | 0 | ba | accuracy_change | 1 | 0.047526 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.047526041666666664} |
| Tent | Reset parameters + auxiliary state | 0 | ba | error_change | 1 | -0.047526 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.047526041666666664} |
| Tent | Reset parameters + auxiliary state | 0 | ba | nll_change | 1 | -0.0377873 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.037787307217952266} |
| Tent | Reset parameters + auxiliary state | 0 | ba | brier_change | 1 | -0.0587301 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0587301072082862} |
| Tent | Reset parameters + auxiliary state | 0 | ba | ece15_change | 1 | 0.00194853 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0019485262054475723} |
| Tent | Reset parameters + auxiliary state | 4 | ab | accuracy_change | 1 | 0.047526 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.047526041666666664} |
| Tent | Reset parameters + auxiliary state | 4 | ab | error_change | 1 | -0.047526 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.047526041666666664} |
| Tent | Reset parameters + auxiliary state | 4 | ab | nll_change | 1 | -0.0373768 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.03737684804167177} |
| Tent | Reset parameters + auxiliary state | 4 | ab | brier_change | 1 | -0.0586665 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.05866650773419233} |
| Tent | Reset parameters + auxiliary state | 4 | ab | ece15_change | 1 | 0.00197852 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0019785216999366473} |
| Tent | Reset parameters + auxiliary state | 4 | ba | accuracy_change | 1 | 0.047526 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.047526041666666664} |
| Tent | Reset parameters + auxiliary state | 4 | ba | error_change | 1 | -0.047526 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.047526041666666664} |
| Tent | Reset parameters + auxiliary state | 4 | ba | nll_change | 1 | -0.0373531 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.03735314347788806} |
| Tent | Reset parameters + auxiliary state | 4 | ba | brier_change | 1 | -0.0586651 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.05866512745515401} |
| Tent | Reset parameters + auxiliary state | 4 | ba | ece15_change | 1 | 0.00181216 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0018121627993138805} |
| Tent | Reset parameters + optimizer | 0 | ab | accuracy_change | 1 | 0.047526 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.047526041666666664} |
| Tent | Reset parameters + optimizer | 0 | ab | error_change | 1 | -0.047526 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.047526041666666664} |
| Tent | Reset parameters + optimizer | 0 | ab | nll_change | 1 | -0.0377331 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.037733146587648} |
| Tent | Reset parameters + optimizer | 0 | ab | brier_change | 1 | -0.0587119 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.05871193303859365} |
| Tent | Reset parameters + optimizer | 0 | ab | ece15_change | 1 | 0.00192471 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0019247136873351} |
| Tent | Reset parameters + optimizer | 0 | ba | accuracy_change | 1 | 0.047526 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.047526041666666664} |
| Tent | Reset parameters + optimizer | 0 | ba | error_change | 1 | -0.047526 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.047526041666666664} |
| Tent | Reset parameters + optimizer | 0 | ba | nll_change | 1 | -0.0377331 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.037733146587648} |
| Tent | Reset parameters + optimizer | 0 | ba | brier_change | 1 | -0.0587119 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.05871193303859365} |
| Tent | Reset parameters + optimizer | 0 | ba | ece15_change | 1 | 0.00192471 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0019247136873351} |
| Tent | Reset parameters + optimizer | 4 | ab | accuracy_change | 1 | 0.047526 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.047526041666666664} |
| Tent | Reset parameters + optimizer | 4 | ab | error_change | 1 | -0.047526 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.047526041666666664} |
| Tent | Reset parameters + optimizer | 4 | ab | nll_change | 1 | -0.0377331 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.037733146587648} |
| Tent | Reset parameters + optimizer | 4 | ab | brier_change | 1 | -0.0587119 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.05871193303859365} |
| Tent | Reset parameters + optimizer | 4 | ab | ece15_change | 1 | 0.00192471 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0019247136873351} |
| Tent | Reset parameters + optimizer | 4 | ba | accuracy_change | 1 | 0.047526 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.047526041666666664} |
| Tent | Reset parameters + optimizer | 4 | ba | error_change | 1 | -0.047526 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.047526041666666664} |
| Tent | Reset parameters + optimizer | 4 | ba | nll_change | 1 | -0.0377331 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.037733146587648} |
| Tent | Reset parameters + optimizer | 4 | ba | brier_change | 1 | -0.0587119 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.05871193303859365} |
| Tent | Reset parameters + optimizer | 4 | ba | ece15_change | 1 | 0.00192471 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0019247136873351} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | ab | accuracy_change | 1 | 0.047526 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.047526041666666664} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | ab | error_change | 1 | -0.047526 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.047526041666666664} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | ab | nll_change | 1 | -0.0377331 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.037733146587648} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | ab | brier_change | 1 | -0.0587119 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.05871193303859365} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | ab | ece15_change | 1 | 0.00192471 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0019247136873351} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | ba | accuracy_change | 1 | 0.047526 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.047526041666666664} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | ba | error_change | 1 | -0.047526 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.047526041666666664} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | ba | nll_change | 1 | -0.0377331 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.037733146587648} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | ba | brier_change | 1 | -0.0587119 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.05871193303859365} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | ba | ece15_change | 1 | 0.00192471 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0019247136873351} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | ab | accuracy_change | 1 | 0.047526 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.047526041666666664} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | ab | error_change | 1 | -0.047526 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.047526041666666664} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | ab | nll_change | 1 | -0.0377331 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.037733146587648} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | ab | brier_change | 1 | -0.0587119 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.05871193303859365} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | ab | ece15_change | 1 | 0.00192471 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0019247136873351} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | ba | accuracy_change | 1 | 0.047526 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.047526041666666664} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | ba | error_change | 1 | -0.047526 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.047526041666666664} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | ba | nll_change | 1 | -0.0377331 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.037733146587648} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | ba | brier_change | 1 | -0.0587119 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.05871193303859365} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | ba | ece15_change | 1 | 0.00192471 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0019247136873351} |


### source_reference: descriptive seed repetitions

The same image panel is reused across seeds. These standard deviations describe seed variability only; no confidence interval is justified from treating seeds as new image panels.

| method | intervention | washout_batches | direction | panel_id | metric | n_seeds | mean | seed_sd_descriptive | individual_seeds |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Normalization only | Reset all declared state | 0 | ab | uci_internal_fixed | accuracy_change | 3 | 0.0472005 | 0.0895265 | {"17": -0.009765625, "29": 0.0009765625, "43": 0.150390625} |
| Normalization only | Reset all declared state | 0 | ab | uci_internal_fixed | error_change | 3 | -0.0472005 | 0.0895265 | {"17": 0.009765625, "29": -0.0009765625, "43": -0.150390625} |
| Normalization only | Reset all declared state | 0 | ab | uci_internal_fixed | nll_change | 3 | -0.0380853 | 0.275399 | {"17": 0.11033965324007958, "29": 0.13126405739057143, "43": -0.3558597090097942} |
| Normalization only | Reset all declared state | 0 | ab | uci_internal_fixed | brier_change | 3 | -0.0587236 | 0.1307 | {"17": 0.02428454792605335, "29": 0.008926806187843006, "43": -0.20938200579631697} |
| Normalization only | Reset all declared state | 0 | ab | uci_internal_fixed | ece15_change | 3 | 0.00217309 | 0.0779969 | {"17": 0.04026631714369, "29": 0.05380312839115661, "43": -0.08755016475000539} |
| Normalization only | Reset all declared state | 0 | ba | uci_internal_fixed | accuracy_change | 3 | 0.0472005 | 0.0895265 | {"17": -0.009765625, "29": 0.0009765625, "43": 0.150390625} |
| Normalization only | Reset all declared state | 0 | ba | uci_internal_fixed | error_change | 3 | -0.0472005 | 0.0895265 | {"17": 0.009765625, "29": -0.0009765625, "43": -0.150390625} |
| Normalization only | Reset all declared state | 0 | ba | uci_internal_fixed | nll_change | 3 | -0.0380853 | 0.275399 | {"17": 0.11033965324007958, "29": 0.13126405739057143, "43": -0.3558597090097942} |
| Normalization only | Reset all declared state | 0 | ba | uci_internal_fixed | brier_change | 3 | -0.0587236 | 0.1307 | {"17": 0.02428454792605335, "29": 0.008926806187843006, "43": -0.20938200579631697} |
| Normalization only | Reset all declared state | 0 | ba | uci_internal_fixed | ece15_change | 3 | 0.00217309 | 0.0779969 | {"17": 0.04026631714369, "29": 0.05380312839115661, "43": -0.08755016475000539} |
| Normalization only | Reset all declared state | 4 | ab | uci_internal_fixed | accuracy_change | 3 | 0.0472005 | 0.0895265 | {"17": -0.009765625, "29": 0.0009765625, "43": 0.150390625} |
| Normalization only | Reset all declared state | 4 | ab | uci_internal_fixed | error_change | 3 | -0.0472005 | 0.0895265 | {"17": 0.009765625, "29": -0.0009765625, "43": -0.150390625} |
| Normalization only | Reset all declared state | 4 | ab | uci_internal_fixed | nll_change | 3 | -0.0380853 | 0.275399 | {"17": 0.11033965324007958, "29": 0.13126405739057143, "43": -0.3558597090097942} |
| Normalization only | Reset all declared state | 4 | ab | uci_internal_fixed | brier_change | 3 | -0.0587236 | 0.1307 | {"17": 0.02428454792605335, "29": 0.008926806187843006, "43": -0.20938200579631697} |
| Normalization only | Reset all declared state | 4 | ab | uci_internal_fixed | ece15_change | 3 | 0.00217309 | 0.0779969 | {"17": 0.04026631714369, "29": 0.05380312839115661, "43": -0.08755016475000539} |
| Normalization only | Reset all declared state | 4 | ba | uci_internal_fixed | accuracy_change | 3 | 0.0472005 | 0.0895265 | {"17": -0.009765625, "29": 0.0009765625, "43": 0.150390625} |
| Normalization only | Reset all declared state | 4 | ba | uci_internal_fixed | error_change | 3 | -0.0472005 | 0.0895265 | {"17": 0.009765625, "29": -0.0009765625, "43": -0.150390625} |
| Normalization only | Reset all declared state | 4 | ba | uci_internal_fixed | nll_change | 3 | -0.0380853 | 0.275399 | {"17": 0.11033965324007958, "29": 0.13126405739057143, "43": -0.3558597090097942} |
| Normalization only | Reset all declared state | 4 | ba | uci_internal_fixed | brier_change | 3 | -0.0587236 | 0.1307 | {"17": 0.02428454792605335, "29": 0.008926806187843006, "43": -0.20938200579631697} |
| Normalization only | Reset all declared state | 4 | ba | uci_internal_fixed | ece15_change | 3 | 0.00217309 | 0.0779969 | {"17": 0.04026631714369, "29": 0.05380312839115661, "43": -0.08755016475000539} |
| Normalization only | No external reset | 0 | ab | uci_internal_fixed | accuracy_change | 3 | 0.0472005 | 0.0895265 | {"17": -0.009765625, "29": 0.0009765625, "43": 0.150390625} |
| Normalization only | No external reset | 0 | ab | uci_internal_fixed | error_change | 3 | -0.0472005 | 0.0895265 | {"17": 0.009765625, "29": -0.0009765625, "43": -0.150390625} |
| Normalization only | No external reset | 0 | ab | uci_internal_fixed | nll_change | 3 | -0.0380853 | 0.275399 | {"17": 0.11033965324007958, "29": 0.13126405739057143, "43": -0.3558597090097942} |
| Normalization only | No external reset | 0 | ab | uci_internal_fixed | brier_change | 3 | -0.0587236 | 0.1307 | {"17": 0.02428454792605335, "29": 0.008926806187843006, "43": -0.20938200579631697} |
| Normalization only | No external reset | 0 | ab | uci_internal_fixed | ece15_change | 3 | 0.00217309 | 0.0779969 | {"17": 0.04026631714369, "29": 0.05380312839115661, "43": -0.08755016475000539} |
| Normalization only | No external reset | 0 | ba | uci_internal_fixed | accuracy_change | 3 | 0.0472005 | 0.0895265 | {"17": -0.009765625, "29": 0.0009765625, "43": 0.150390625} |
| Normalization only | No external reset | 0 | ba | uci_internal_fixed | error_change | 3 | -0.0472005 | 0.0895265 | {"17": 0.009765625, "29": -0.0009765625, "43": -0.150390625} |
| Normalization only | No external reset | 0 | ba | uci_internal_fixed | nll_change | 3 | -0.0380853 | 0.275399 | {"17": 0.11033965324007958, "29": 0.13126405739057143, "43": -0.3558597090097942} |
| Normalization only | No external reset | 0 | ba | uci_internal_fixed | brier_change | 3 | -0.0587236 | 0.1307 | {"17": 0.02428454792605335, "29": 0.008926806187843006, "43": -0.20938200579631697} |
| Normalization only | No external reset | 0 | ba | uci_internal_fixed | ece15_change | 3 | 0.00217309 | 0.0779969 | {"17": 0.04026631714369, "29": 0.05380312839115661, "43": -0.08755016475000539} |
| Normalization only | No external reset | 4 | ab | uci_internal_fixed | accuracy_change | 3 | 0.0472005 | 0.0895265 | {"17": -0.009765625, "29": 0.0009765625, "43": 0.150390625} |
| Normalization only | No external reset | 4 | ab | uci_internal_fixed | error_change | 3 | -0.0472005 | 0.0895265 | {"17": 0.009765625, "29": -0.0009765625, "43": -0.150390625} |
| Normalization only | No external reset | 4 | ab | uci_internal_fixed | nll_change | 3 | -0.0380853 | 0.275399 | {"17": 0.11033965324007958, "29": 0.13126405739057143, "43": -0.3558597090097942} |
| Normalization only | No external reset | 4 | ab | uci_internal_fixed | brier_change | 3 | -0.0587236 | 0.1307 | {"17": 0.02428454792605335, "29": 0.008926806187843006, "43": -0.20938200579631697} |
| Normalization only | No external reset | 4 | ab | uci_internal_fixed | ece15_change | 3 | 0.00217309 | 0.0779969 | {"17": 0.04026631714369, "29": 0.05380312839115661, "43": -0.08755016475000539} |
| Normalization only | No external reset | 4 | ba | uci_internal_fixed | accuracy_change | 3 | 0.0472005 | 0.0895265 | {"17": -0.009765625, "29": 0.0009765625, "43": 0.150390625} |
| Normalization only | No external reset | 4 | ba | uci_internal_fixed | error_change | 3 | -0.0472005 | 0.0895265 | {"17": 0.009765625, "29": -0.0009765625, "43": -0.150390625} |
| Normalization only | No external reset | 4 | ba | uci_internal_fixed | nll_change | 3 | -0.0380853 | 0.275399 | {"17": 0.11033965324007958, "29": 0.13126405739057143, "43": -0.3558597090097942} |
| Normalization only | No external reset | 4 | ba | uci_internal_fixed | brier_change | 3 | -0.0587236 | 0.1307 | {"17": 0.02428454792605335, "29": 0.008926806187843006, "43": -0.20938200579631697} |
| Normalization only | No external reset | 4 | ba | uci_internal_fixed | ece15_change | 3 | 0.00217309 | 0.0779969 | {"17": 0.04026631714369, "29": 0.05380312839115661, "43": -0.08755016475000539} |
| SAR (complete-state implementation) | Reset all declared state | 0 | ab | uci_internal_fixed | accuracy_change | 3 | 0.047526 | 0.0892171 | {"17": -0.0087890625, "29": 0.0009765625, "43": 0.150390625} |
| SAR (complete-state implementation) | Reset all declared state | 0 | ab | uci_internal_fixed | error_change | 3 | -0.047526 | 0.0892171 | {"17": 0.0087890625, "29": -0.0009765625, "43": -0.150390625} |
| SAR (complete-state implementation) | Reset all declared state | 0 | ab | uci_internal_fixed | nll_change | 3 | -0.0381867 | 0.276113 | {"17": 0.11000910014154106, "29": 0.1321881443071896, "43": -0.3567574366875513} |
| SAR (complete-state implementation) | Reset all declared state | 0 | ab | uci_internal_fixed | brier_change | 3 | -0.0588159 | 0.130869 | {"17": 0.02417226051021297, "29": 0.009058788359464392, "43": -0.20967861093763232} |
| SAR (complete-state implementation) | Reset all declared state | 0 | ab | uci_internal_fixed | ece15_change | 3 | 0.0019071 | 0.0777665 | {"17": 0.0393199679055308, "29": 0.05389602291180816, "43": -0.08749467591672275} |
| SAR (complete-state implementation) | Reset all declared state | 0 | ba | uci_internal_fixed | accuracy_change | 3 | 0.047526 | 0.0892171 | {"17": -0.0087890625, "29": 0.0009765625, "43": 0.150390625} |
| SAR (complete-state implementation) | Reset all declared state | 0 | ba | uci_internal_fixed | error_change | 3 | -0.047526 | 0.0892171 | {"17": 0.0087890625, "29": -0.0009765625, "43": -0.150390625} |
| SAR (complete-state implementation) | Reset all declared state | 0 | ba | uci_internal_fixed | nll_change | 3 | -0.0381867 | 0.276113 | {"17": 0.11000910014154106, "29": 0.1321881443071896, "43": -0.3567574366875513} |
| SAR (complete-state implementation) | Reset all declared state | 0 | ba | uci_internal_fixed | brier_change | 3 | -0.0588159 | 0.130869 | {"17": 0.02417226051021297, "29": 0.009058788359464392, "43": -0.20967861093763232} |
| SAR (complete-state implementation) | Reset all declared state | 0 | ba | uci_internal_fixed | ece15_change | 3 | 0.0019071 | 0.0777665 | {"17": 0.0393199679055308, "29": 0.05389602291180816, "43": -0.08749467591672275} |
| SAR (complete-state implementation) | Reset all declared state | 4 | ab | uci_internal_fixed | accuracy_change | 3 | 0.047526 | 0.0892171 | {"17": -0.0087890625, "29": 0.0009765625, "43": 0.150390625} |
| SAR (complete-state implementation) | Reset all declared state | 4 | ab | uci_internal_fixed | error_change | 3 | -0.047526 | 0.0892171 | {"17": 0.0087890625, "29": -0.0009765625, "43": -0.150390625} |
| SAR (complete-state implementation) | Reset all declared state | 4 | ab | uci_internal_fixed | nll_change | 3 | -0.0381867 | 0.276113 | {"17": 0.11000910014154106, "29": 0.1321881443071896, "43": -0.3567574366875513} |
| SAR (complete-state implementation) | Reset all declared state | 4 | ab | uci_internal_fixed | brier_change | 3 | -0.0588159 | 0.130869 | {"17": 0.02417226051021297, "29": 0.009058788359464392, "43": -0.20967861093763232} |
| SAR (complete-state implementation) | Reset all declared state | 4 | ab | uci_internal_fixed | ece15_change | 3 | 0.0019071 | 0.0777665 | {"17": 0.0393199679055308, "29": 0.05389602291180816, "43": -0.08749467591672275} |
| SAR (complete-state implementation) | Reset all declared state | 4 | ba | uci_internal_fixed | accuracy_change | 3 | 0.047526 | 0.0892171 | {"17": -0.0087890625, "29": 0.0009765625, "43": 0.150390625} |
| SAR (complete-state implementation) | Reset all declared state | 4 | ba | uci_internal_fixed | error_change | 3 | -0.047526 | 0.0892171 | {"17": 0.0087890625, "29": -0.0009765625, "43": -0.150390625} |
| SAR (complete-state implementation) | Reset all declared state | 4 | ba | uci_internal_fixed | nll_change | 3 | -0.0381867 | 0.276113 | {"17": 0.11000910014154106, "29": 0.1321881443071896, "43": -0.3567574366875513} |
| SAR (complete-state implementation) | Reset all declared state | 4 | ba | uci_internal_fixed | brier_change | 3 | -0.0588159 | 0.130869 | {"17": 0.02417226051021297, "29": 0.009058788359464392, "43": -0.20967861093763232} |
| SAR (complete-state implementation) | Reset all declared state | 4 | ba | uci_internal_fixed | ece15_change | 3 | 0.0019071 | 0.0777665 | {"17": 0.0393199679055308, "29": 0.05389602291180816, "43": -0.08749467591672275} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | ab | uci_internal_fixed | accuracy_change | 3 | 0.047526 | 0.0892171 | {"17": -0.0087890625, "29": 0.0009765625, "43": 0.150390625} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | ab | uci_internal_fixed | error_change | 3 | -0.047526 | 0.0892171 | {"17": 0.0087890625, "29": -0.0009765625, "43": -0.150390625} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | ab | uci_internal_fixed | nll_change | 3 | -0.0381878 | 0.276114 | {"17": 0.11000764872831631, "29": 0.13218827886179113, "43": -0.35675919995882444} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | ab | uci_internal_fixed | brier_change | 3 | -0.0588161 | 0.130869 | {"17": 0.024171623477688017, "29": 0.009058892999898543, "43": -0.20967880731834287} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | ab | uci_internal_fixed | ece15_change | 3 | 0.00190804 | 0.0777658 | {"17": 0.03932112635531075, "29": 0.053895988156813256, "43": -0.08749298282646971} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | ba | uci_internal_fixed | accuracy_change | 3 | 0.047526 | 0.0892171 | {"17": -0.0087890625, "29": 0.0009765625, "43": 0.150390625} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | ba | uci_internal_fixed | error_change | 3 | -0.047526 | 0.0892171 | {"17": 0.0087890625, "29": -0.0009765625, "43": -0.150390625} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | ba | uci_internal_fixed | nll_change | 3 | -0.038187 | 0.276113 | {"17": 0.1100083876350553, "29": 0.13218816507491318, "43": -0.35675749028219456} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | ba | uci_internal_fixed | brier_change | 3 | -0.058816 | 0.130869 | {"17": 0.02417193021868217, "29": 0.009058807590117393, "43": -0.20967861688299314} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | ba | uci_internal_fixed | ece15_change | 3 | 0.00190729 | 0.0777666 | {"17": 0.03932052399976245, "29": 0.0538959732867773, "43": -0.0874946244418825} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | ab | uci_internal_fixed | accuracy_change | 3 | 0.047526 | 0.0892171 | {"17": -0.0087890625, "29": 0.0009765625, "43": 0.150390625} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | ab | uci_internal_fixed | error_change | 3 | -0.047526 | 0.0892171 | {"17": 0.0087890625, "29": -0.0009765625, "43": -0.150390625} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | ab | uci_internal_fixed | nll_change | 3 | -0.0381867 | 0.276113 | {"17": 0.11000910014154106, "29": 0.1321881443071896, "43": -0.3567574366875513} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | ab | uci_internal_fixed | brier_change | 3 | -0.0588159 | 0.130869 | {"17": 0.02417226051021297, "29": 0.009058788359464392, "43": -0.20967861093763232} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | ab | uci_internal_fixed | ece15_change | 3 | 0.0019071 | 0.0777665 | {"17": 0.0393199679055308, "29": 0.05389602291180816, "43": -0.08749467591672275} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | ba | uci_internal_fixed | accuracy_change | 3 | 0.047526 | 0.0892171 | {"17": -0.0087890625, "29": 0.0009765625, "43": 0.150390625} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | ba | uci_internal_fixed | error_change | 3 | -0.047526 | 0.0892171 | {"17": 0.0087890625, "29": -0.0009765625, "43": -0.150390625} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | ba | uci_internal_fixed | nll_change | 3 | -0.0381867 | 0.276113 | {"17": 0.11000910014154106, "29": 0.1321881443071896, "43": -0.3567574366875513} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | ba | uci_internal_fixed | brier_change | 3 | -0.0588159 | 0.130869 | {"17": 0.02417226051021297, "29": 0.009058788359464392, "43": -0.20967861093763232} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | ba | uci_internal_fixed | ece15_change | 3 | 0.0019071 | 0.0777665 | {"17": 0.0393199679055308, "29": 0.05389602291180816, "43": -0.08749467591672275} |
| SAR (complete-state implementation) | No external reset | 0 | ab | uci_internal_fixed | accuracy_change | 3 | 0.0472005 | 0.0895265 | {"17": -0.009765625, "29": 0.0009765625, "43": 0.150390625} |
| SAR (complete-state implementation) | No external reset | 0 | ab | uci_internal_fixed | error_change | 3 | -0.0472005 | 0.0895265 | {"17": 0.009765625, "29": -0.0009765625, "43": -0.150390625} |
| SAR (complete-state implementation) | No external reset | 0 | ab | uci_internal_fixed | nll_change | 3 | -0.0379925 | 0.275482 | {"17": 0.11050016198160573, "29": 0.13138496040404551, "43": -0.35586275032245795} |
| SAR (complete-state implementation) | No external reset | 0 | ab | uci_internal_fixed | brier_change | 3 | -0.0587095 | 0.130715 | {"17": 0.02431447569611221, "29": 0.008941617020540837, "43": -0.20938471629304206} |
| SAR (complete-state implementation) | No external reset | 0 | ab | uci_internal_fixed | ece15_change | 3 | 0.0021784 | 0.0780001 | {"17": 0.04027165592232204, "29": 0.05381196770055976, "43": -0.08754841651154391} |
| SAR (complete-state implementation) | No external reset | 0 | ba | uci_internal_fixed | accuracy_change | 3 | 0.0472005 | 0.0895265 | {"17": -0.009765625, "29": 0.0009765625, "43": 0.150390625} |
| SAR (complete-state implementation) | No external reset | 0 | ba | uci_internal_fixed | error_change | 3 | -0.0472005 | 0.0895265 | {"17": 0.009765625, "29": -0.0009765625, "43": -0.150390625} |
| SAR (complete-state implementation) | No external reset | 0 | ba | uci_internal_fixed | nll_change | 3 | -0.038043 | 0.27544 | {"17": 0.11034217817894154, "29": 0.13138979023177524, "43": -0.3558610406458281} |
| SAR (complete-state implementation) | No external reset | 0 | ba | uci_internal_fixed | brier_change | 3 | -0.0587227 | 0.130702 | {"17": 0.02427388561909137, "29": 0.008942567129231796, "43": -0.20938452585769232} |
| SAR (complete-state implementation) | No external reset | 0 | ba | uci_internal_fixed | ece15_change | 3 | 0.00217854 | 0.0780015 | {"17": 0.04027414779764999, "29": 0.0538115235416907, "43": -0.08755005812695671} |
| SAR (complete-state implementation) | No external reset | 4 | ab | uci_internal_fixed | accuracy_change | 3 | 0.0472005 | 0.0895265 | {"17": -0.009765625, "29": 0.0009765625, "43": 0.150390625} |
| SAR (complete-state implementation) | No external reset | 4 | ab | uci_internal_fixed | error_change | 3 | -0.0472005 | 0.0895265 | {"17": 0.009765625, "29": -0.0009765625, "43": -0.150390625} |
| SAR (complete-state implementation) | No external reset | 4 | ab | uci_internal_fixed | nll_change | 3 | -0.0377731 | 0.27563 | {"17": 0.11007324745511979, "29": 0.13238951237437732, "43": -0.3557820051684176} |
| SAR (complete-state implementation) | No external reset | 4 | ab | uci_internal_fixed | brier_change | 3 | -0.0586821 | 0.130714 | {"17": 0.02420517964397291, "29": 0.009114100348863985, "43": -0.20936547198232136} |
| SAR (complete-state implementation) | No external reset | 4 | ab | uci_internal_fixed | ece15_change | 3 | 0.0022123 | 0.0780299 | {"17": 0.04028293045015599, "29": 0.053899178392426556, "43": -0.08754521835349739} |
| SAR (complete-state implementation) | No external reset | 4 | ba | uci_internal_fixed | accuracy_change | 3 | 0.047526 | 0.0892171 | {"17": -0.0087890625, "29": 0.0009765625, "43": 0.150390625} |
| SAR (complete-state implementation) | No external reset | 4 | ba | uci_internal_fixed | error_change | 3 | -0.047526 | 0.0892171 | {"17": 0.0087890625, "29": -0.0009765625, "43": -0.150390625} |
| SAR (complete-state implementation) | No external reset | 4 | ba | uci_internal_fixed | nll_change | 3 | -0.0377439 | 0.275653 | {"17": 0.11016086760844615, "29": 0.13238951237437732, "43": -0.3557820051684176} |
| SAR (complete-state implementation) | No external reset | 4 | ba | uci_internal_fixed | brier_change | 3 | -0.0586771 | 0.130718 | {"17": 0.0242200228112132, "29": 0.009114100348863985, "43": -0.20936547198232136} |
| SAR (complete-state implementation) | No external reset | 4 | ba | uci_internal_fixed | ece15_change | 3 | 0.00188879 | 0.0777948 | {"17": 0.039312398151864145, "29": 0.053899178392426556, "43": -0.08754521835349739} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | ab | uci_internal_fixed | accuracy_change | 3 | 0.0472005 | 0.0895265 | {"17": -0.009765625, "29": 0.0009765625, "43": 0.150390625} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | ab | uci_internal_fixed | error_change | 3 | -0.0472005 | 0.0895265 | {"17": 0.009765625, "29": -0.0009765625, "43": -0.150390625} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | ab | uci_internal_fixed | nll_change | 3 | -0.0379925 | 0.275482 | {"17": 0.11050017074276577, "29": 0.13138496040404551, "43": -0.35586275032245795} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | ab | uci_internal_fixed | brier_change | 3 | -0.0587095 | 0.130715 | {"17": 0.02431447571379431, "29": 0.008941617020540837, "43": -0.20938471629304206} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | ab | uci_internal_fixed | ece15_change | 3 | 0.0021784 | 0.0780001 | {"17": 0.0402716471736816, "29": 0.05381196770055976, "43": -0.08754841651154391} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | ba | uci_internal_fixed | accuracy_change | 3 | 0.0472005 | 0.0895265 | {"17": -0.009765625, "29": 0.0009765625, "43": 0.150390625} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | ba | uci_internal_fixed | error_change | 3 | -0.0472005 | 0.0895265 | {"17": 0.009765625, "29": -0.0009765625, "43": -0.150390625} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | ba | uci_internal_fixed | nll_change | 3 | -0.038043 | 0.27544 | {"17": 0.11034224197946324, "29": 0.13138979023177524, "43": -0.3558610406458281} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | ba | uci_internal_fixed | brier_change | 3 | -0.0587227 | 0.130702 | {"17": 0.02427391874042787, "29": 0.008942567129231796, "43": -0.20938452585769232} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | ba | uci_internal_fixed | ece15_change | 3 | 0.00217853 | 0.0780015 | {"17": 0.04027411311315924, "29": 0.0538115235416907, "43": -0.08755005812695671} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | ab | uci_internal_fixed | accuracy_change | 3 | 0.0472005 | 0.0895265 | {"17": -0.009765625, "29": 0.0009765625, "43": 0.150390625} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | ab | uci_internal_fixed | error_change | 3 | -0.0472005 | 0.0895265 | {"17": 0.009765625, "29": -0.0009765625, "43": -0.150390625} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | ab | uci_internal_fixed | nll_change | 3 | -0.0377731 | 0.27563 | {"17": 0.11007324745511979, "29": 0.13238951237437732, "43": -0.3557820051684176} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | ab | uci_internal_fixed | brier_change | 3 | -0.0586821 | 0.130714 | {"17": 0.02420517964397291, "29": 0.009114100348863985, "43": -0.20936547198232136} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | ab | uci_internal_fixed | ece15_change | 3 | 0.0022123 | 0.0780299 | {"17": 0.04028293045015599, "29": 0.053899178392426556, "43": -0.08754521835349739} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | ba | uci_internal_fixed | accuracy_change | 3 | 0.047526 | 0.0892171 | {"17": -0.0087890625, "29": 0.0009765625, "43": 0.150390625} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | ba | uci_internal_fixed | error_change | 3 | -0.047526 | 0.0892171 | {"17": 0.0087890625, "29": -0.0009765625, "43": -0.150390625} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | ba | uci_internal_fixed | nll_change | 3 | -0.0377439 | 0.275653 | {"17": 0.11016086760844615, "29": 0.13238951237437732, "43": -0.3557820051684176} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | ba | uci_internal_fixed | brier_change | 3 | -0.0586771 | 0.130718 | {"17": 0.0242200228112132, "29": 0.009114100348863985, "43": -0.20936547198232136} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | ba | uci_internal_fixed | ece15_change | 3 | 0.00188879 | 0.0777948 | {"17": 0.039312398151864145, "29": 0.053899178392426556, "43": -0.08754521835349739} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | ab | uci_internal_fixed | accuracy_change | 3 | 0.047526 | 0.0892171 | {"17": -0.0087890625, "29": 0.0009765625, "43": 0.150390625} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | ab | uci_internal_fixed | error_change | 3 | -0.047526 | 0.0892171 | {"17": 0.0087890625, "29": -0.0009765625, "43": -0.150390625} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | ab | uci_internal_fixed | nll_change | 3 | -0.0381878 | 0.276114 | {"17": 0.11000764872831631, "29": 0.13218827886179113, "43": -0.35675919995882444} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | ab | uci_internal_fixed | brier_change | 3 | -0.0588161 | 0.130869 | {"17": 0.024171623477688017, "29": 0.009058892999898543, "43": -0.20967880731834287} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | ab | uci_internal_fixed | ece15_change | 3 | 0.00190804 | 0.0777658 | {"17": 0.03932112635531075, "29": 0.053895988156813256, "43": -0.08749298282646971} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | ba | uci_internal_fixed | accuracy_change | 3 | 0.047526 | 0.0892171 | {"17": -0.0087890625, "29": 0.0009765625, "43": 0.150390625} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | ba | uci_internal_fixed | error_change | 3 | -0.047526 | 0.0892171 | {"17": 0.0087890625, "29": -0.0009765625, "43": -0.150390625} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | ba | uci_internal_fixed | nll_change | 3 | -0.038187 | 0.276113 | {"17": 0.1100083876350553, "29": 0.13218816507491318, "43": -0.35675749028219456} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | ba | uci_internal_fixed | brier_change | 3 | -0.058816 | 0.130869 | {"17": 0.02417193021868217, "29": 0.009058807590117393, "43": -0.20967861688299314} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | ba | uci_internal_fixed | ece15_change | 3 | 0.00190729 | 0.0777666 | {"17": 0.03932052399976245, "29": 0.0538959732867773, "43": -0.0874946244418825} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | ab | uci_internal_fixed | accuracy_change | 3 | 0.047526 | 0.0892171 | {"17": -0.0087890625, "29": 0.0009765625, "43": 0.150390625} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | ab | uci_internal_fixed | error_change | 3 | -0.047526 | 0.0892171 | {"17": 0.0087890625, "29": -0.0009765625, "43": -0.150390625} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | ab | uci_internal_fixed | nll_change | 3 | -0.0381867 | 0.276113 | {"17": 0.11000910014154106, "29": 0.1321881443071896, "43": -0.3567574366875513} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | ab | uci_internal_fixed | brier_change | 3 | -0.0588159 | 0.130869 | {"17": 0.02417226051021297, "29": 0.009058788359464392, "43": -0.20967861093763232} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | ab | uci_internal_fixed | ece15_change | 3 | 0.0019071 | 0.0777665 | {"17": 0.0393199679055308, "29": 0.05389602291180816, "43": -0.08749467591672275} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | ba | uci_internal_fixed | accuracy_change | 3 | 0.047526 | 0.0892171 | {"17": -0.0087890625, "29": 0.0009765625, "43": 0.150390625} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | ba | uci_internal_fixed | error_change | 3 | -0.047526 | 0.0892171 | {"17": 0.0087890625, "29": -0.0009765625, "43": -0.150390625} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | ba | uci_internal_fixed | nll_change | 3 | -0.0381867 | 0.276113 | {"17": 0.11000910014154106, "29": 0.1321881443071896, "43": -0.3567574366875513} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | ba | uci_internal_fixed | brier_change | 3 | -0.0588159 | 0.130869 | {"17": 0.02417226051021297, "29": 0.009058788359464392, "43": -0.20967861093763232} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | ba | uci_internal_fixed | ece15_change | 3 | 0.0019071 | 0.0777665 | {"17": 0.0393199679055308, "29": 0.05389602291180816, "43": -0.08749467591672275} |
| SAR (complete-state implementation) | Reset parameters only | 0 | ab | uci_internal_fixed | accuracy_change | 3 | 0.0472005 | 0.0895265 | {"17": -0.009765625, "29": 0.0009765625, "43": 0.150390625} |
| SAR (complete-state implementation) | Reset parameters only | 0 | ab | uci_internal_fixed | error_change | 3 | -0.0472005 | 0.0895265 | {"17": 0.009765625, "29": -0.0009765625, "43": -0.150390625} |
| SAR (complete-state implementation) | Reset parameters only | 0 | ab | uci_internal_fixed | nll_change | 3 | -0.0379915 | 0.275481 | {"17": 0.11050171931683081, "29": 0.13138482584944397, "43": -0.3558609870511848} |
| SAR (complete-state implementation) | Reset parameters only | 0 | ab | uci_internal_fixed | brier_change | 3 | -0.0587093 | 0.130715 | {"17": 0.024315112186565013, "29": 0.008941512380106686, "43": -0.2093845199123315} |
| SAR (complete-state implementation) | Reset parameters only | 0 | ab | uci_internal_fixed | ece15_change | 3 | 0.00217743 | 0.0780008 | {"17": 0.04027039127716849, "29": 0.05381200245555466, "43": -0.08755010960179695} |
| SAR (complete-state implementation) | Reset parameters only | 0 | ba | uci_internal_fixed | accuracy_change | 3 | 0.0472005 | 0.0895265 | {"17": -0.009765625, "29": 0.0009765625, "43": 0.150390625} |
| SAR (complete-state implementation) | Reset parameters only | 0 | ba | uci_internal_fixed | error_change | 3 | -0.0472005 | 0.0895265 | {"17": 0.009765625, "29": -0.0009765625, "43": -0.150390625} |
| SAR (complete-state implementation) | Reset parameters only | 0 | ba | uci_internal_fixed | nll_change | 3 | -0.0380425 | 0.27544 | {"17": 0.11034356869642203, "29": 0.13138976946405165, "43": -0.3558609870511848} |
| SAR (complete-state implementation) | Reset parameters only | 0 | ba | uci_internal_fixed | brier_change | 3 | -0.0587225 | 0.130702 | {"17": 0.02427451188669427, "29": 0.008942547898578795, "43": -0.2093845199123315} |
| SAR (complete-state implementation) | Reset parameters only | 0 | ba | uci_internal_fixed | ece15_change | 3 | 0.00217818 | 0.0780013 | {"17": 0.04027307213982169, "29": 0.053811573166721555, "43": -0.08755010960179695} |
| SAR (complete-state implementation) | Reset parameters only | 4 | ab | uci_internal_fixed | accuracy_change | 3 | 0.0472005 | 0.0895265 | {"17": -0.009765625, "29": 0.0009765625, "43": 0.150390625} |
| SAR (complete-state implementation) | Reset parameters only | 4 | ab | uci_internal_fixed | error_change | 3 | -0.0472005 | 0.0895265 | {"17": 0.009765625, "29": -0.0009765625, "43": -0.150390625} |
| SAR (complete-state implementation) | Reset parameters only | 4 | ab | uci_internal_fixed | nll_change | 3 | -0.0377731 | 0.27563 | {"17": 0.11007324745511979, "29": 0.13238951237437732, "43": -0.3557820051684176} |
| SAR (complete-state implementation) | Reset parameters only | 4 | ab | uci_internal_fixed | brier_change | 3 | -0.0586821 | 0.130714 | {"17": 0.02420517964397291, "29": 0.009114100348863985, "43": -0.20936547198232136} |
| SAR (complete-state implementation) | Reset parameters only | 4 | ab | uci_internal_fixed | ece15_change | 3 | 0.0022123 | 0.0780299 | {"17": 0.04028293045015599, "29": 0.053899178392426556, "43": -0.08754521835349739} |
| SAR (complete-state implementation) | Reset parameters only | 4 | ba | uci_internal_fixed | accuracy_change | 3 | 0.047526 | 0.0892171 | {"17": -0.0087890625, "29": 0.0009765625, "43": 0.150390625} |
| SAR (complete-state implementation) | Reset parameters only | 4 | ba | uci_internal_fixed | error_change | 3 | -0.047526 | 0.0892171 | {"17": 0.0087890625, "29": -0.0009765625, "43": -0.150390625} |
| SAR (complete-state implementation) | Reset parameters only | 4 | ba | uci_internal_fixed | nll_change | 3 | -0.0377439 | 0.275653 | {"17": 0.11016086760844615, "29": 0.13238951237437732, "43": -0.3557820051684176} |
| SAR (complete-state implementation) | Reset parameters only | 4 | ba | uci_internal_fixed | brier_change | 3 | -0.0586771 | 0.130718 | {"17": 0.0242200228112132, "29": 0.009114100348863985, "43": -0.20936547198232136} |
| SAR (complete-state implementation) | Reset parameters only | 4 | ba | uci_internal_fixed | ece15_change | 3 | 0.00188879 | 0.0777948 | {"17": 0.039312398151864145, "29": 0.053899178392426556, "43": -0.08754521835349739} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | ab | uci_internal_fixed | accuracy_change | 3 | 0.047526 | 0.0892171 | {"17": -0.0087890625, "29": 0.0009765625, "43": 0.150390625} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | ab | uci_internal_fixed | error_change | 3 | -0.047526 | 0.0892171 | {"17": 0.0087890625, "29": -0.0009765625, "43": -0.150390625} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | ab | uci_internal_fixed | nll_change | 3 | -0.0381867 | 0.276113 | {"17": 0.11000910014154106, "29": 0.1321881443071896, "43": -0.3567574366875513} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | ab | uci_internal_fixed | brier_change | 3 | -0.0588159 | 0.130869 | {"17": 0.02417226051021297, "29": 0.009058788359464392, "43": -0.20967861093763232} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | ab | uci_internal_fixed | ece15_change | 3 | 0.0019071 | 0.0777665 | {"17": 0.0393199679055308, "29": 0.05389602291180816, "43": -0.08749467591672275} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | ba | uci_internal_fixed | accuracy_change | 3 | 0.047526 | 0.0892171 | {"17": -0.0087890625, "29": 0.0009765625, "43": 0.150390625} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | ba | uci_internal_fixed | error_change | 3 | -0.047526 | 0.0892171 | {"17": 0.0087890625, "29": -0.0009765625, "43": -0.150390625} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | ba | uci_internal_fixed | nll_change | 3 | -0.0381867 | 0.276113 | {"17": 0.11000910014154106, "29": 0.1321881443071896, "43": -0.3567574366875513} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | ba | uci_internal_fixed | brier_change | 3 | -0.0588159 | 0.130869 | {"17": 0.02417226051021297, "29": 0.009058788359464392, "43": -0.20967861093763232} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | ba | uci_internal_fixed | ece15_change | 3 | 0.0019071 | 0.0777665 | {"17": 0.0393199679055308, "29": 0.05389602291180816, "43": -0.08749467591672275} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | ab | uci_internal_fixed | accuracy_change | 3 | 0.047526 | 0.0892171 | {"17": -0.0087890625, "29": 0.0009765625, "43": 0.150390625} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | ab | uci_internal_fixed | error_change | 3 | -0.047526 | 0.0892171 | {"17": 0.0087890625, "29": -0.0009765625, "43": -0.150390625} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | ab | uci_internal_fixed | nll_change | 3 | -0.0381867 | 0.276113 | {"17": 0.11000910014154106, "29": 0.1321881443071896, "43": -0.3567574366875513} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | ab | uci_internal_fixed | brier_change | 3 | -0.0588159 | 0.130869 | {"17": 0.02417226051021297, "29": 0.009058788359464392, "43": -0.20967861093763232} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | ab | uci_internal_fixed | ece15_change | 3 | 0.0019071 | 0.0777665 | {"17": 0.0393199679055308, "29": 0.05389602291180816, "43": -0.08749467591672275} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | ba | uci_internal_fixed | accuracy_change | 3 | 0.047526 | 0.0892171 | {"17": -0.0087890625, "29": 0.0009765625, "43": 0.150390625} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | ba | uci_internal_fixed | error_change | 3 | -0.047526 | 0.0892171 | {"17": 0.0087890625, "29": -0.0009765625, "43": -0.150390625} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | ba | uci_internal_fixed | nll_change | 3 | -0.0381867 | 0.276113 | {"17": 0.11000910014154106, "29": 0.1321881443071896, "43": -0.3567574366875513} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | ba | uci_internal_fixed | brier_change | 3 | -0.0588159 | 0.130869 | {"17": 0.02417226051021297, "29": 0.009058788359464392, "43": -0.20967861093763232} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | ba | uci_internal_fixed | ece15_change | 3 | 0.0019071 | 0.0777665 | {"17": 0.0393199679055308, "29": 0.05389602291180816, "43": -0.08749467591672275} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | ab | uci_internal_fixed | accuracy_change | 3 | 0.0472005 | 0.0895265 | {"17": -0.009765625, "29": 0.0009765625, "43": 0.150390625} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | ab | uci_internal_fixed | error_change | 3 | -0.0472005 | 0.0895265 | {"17": 0.009765625, "29": -0.0009765625, "43": -0.150390625} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | ab | uci_internal_fixed | nll_change | 3 | -0.0379915 | 0.275481 | {"17": 0.11050172882011997, "29": 0.13138482584944397, "43": -0.3558609870511848} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | ab | uci_internal_fixed | brier_change | 3 | -0.0587093 | 0.130715 | {"17": 0.024315112223964312, "29": 0.008941512380106686, "43": -0.2093845199123315} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | ab | uci_internal_fixed | ece15_change | 3 | 0.00217742 | 0.0780007 | {"17": 0.04027038179270825, "29": 0.05381200245555466, "43": -0.08755010960179695} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | ba | uci_internal_fixed | accuracy_change | 3 | 0.0472005 | 0.0895265 | {"17": -0.009765625, "29": 0.0009765625, "43": 0.150390625} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | ba | uci_internal_fixed | error_change | 3 | -0.0472005 | 0.0895265 | {"17": 0.009765625, "29": -0.0009765625, "43": -0.150390625} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | ba | uci_internal_fixed | nll_change | 3 | -0.0380425 | 0.27544 | {"17": 0.11034363751782608, "29": 0.13138976946405165, "43": -0.3558609870511848} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | ba | uci_internal_fixed | brier_change | 3 | -0.0587225 | 0.130702 | {"17": 0.02427454756583987, "29": 0.008942547898578795, "43": -0.2093845199123315} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | ba | uci_internal_fixed | ece15_change | 3 | 0.00217817 | 0.0780013 | {"17": 0.04027303362732679, "29": 0.053811573166721555, "43": -0.08755010960179695} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | ab | uci_internal_fixed | accuracy_change | 3 | 0.0472005 | 0.0895265 | {"17": -0.009765625, "29": 0.0009765625, "43": 0.150390625} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | ab | uci_internal_fixed | error_change | 3 | -0.0472005 | 0.0895265 | {"17": 0.009765625, "29": -0.0009765625, "43": -0.150390625} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | ab | uci_internal_fixed | nll_change | 3 | -0.0377731 | 0.27563 | {"17": 0.11007324745511979, "29": 0.13238951237437732, "43": -0.3557820051684176} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | ab | uci_internal_fixed | brier_change | 3 | -0.0586821 | 0.130714 | {"17": 0.02420517964397291, "29": 0.009114100348863985, "43": -0.20936547198232136} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | ab | uci_internal_fixed | ece15_change | 3 | 0.0022123 | 0.0780299 | {"17": 0.04028293045015599, "29": 0.053899178392426556, "43": -0.08754521835349739} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | ba | uci_internal_fixed | accuracy_change | 3 | 0.047526 | 0.0892171 | {"17": -0.0087890625, "29": 0.0009765625, "43": 0.150390625} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | ba | uci_internal_fixed | error_change | 3 | -0.047526 | 0.0892171 | {"17": 0.0087890625, "29": -0.0009765625, "43": -0.150390625} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | ba | uci_internal_fixed | nll_change | 3 | -0.0377439 | 0.275653 | {"17": 0.11016086760844615, "29": 0.13238951237437732, "43": -0.3557820051684176} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | ba | uci_internal_fixed | brier_change | 3 | -0.0586771 | 0.130718 | {"17": 0.0242200228112132, "29": 0.009114100348863985, "43": -0.20936547198232136} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | ba | uci_internal_fixed | ece15_change | 3 | 0.00188879 | 0.0777948 | {"17": 0.039312398151864145, "29": 0.053899178392426556, "43": -0.08754521835349739} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | ab | uci_internal_fixed | accuracy_change | 3 | 0.047526 | 0.0892171 | {"17": -0.0087890625, "29": 0.0009765625, "43": 0.150390625} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | ab | uci_internal_fixed | error_change | 3 | -0.047526 | 0.0892171 | {"17": 0.0087890625, "29": -0.0009765625, "43": -0.150390625} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | ab | uci_internal_fixed | nll_change | 3 | -0.0381867 | 0.276113 | {"17": 0.11000910014154106, "29": 0.1321881443071896, "43": -0.3567574366875513} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | ab | uci_internal_fixed | brier_change | 3 | -0.0588159 | 0.130869 | {"17": 0.02417226051021297, "29": 0.009058788359464392, "43": -0.20967861093763232} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | ab | uci_internal_fixed | ece15_change | 3 | 0.0019071 | 0.0777665 | {"17": 0.0393199679055308, "29": 0.05389602291180816, "43": -0.08749467591672275} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | ba | uci_internal_fixed | accuracy_change | 3 | 0.047526 | 0.0892171 | {"17": -0.0087890625, "29": 0.0009765625, "43": 0.150390625} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | ba | uci_internal_fixed | error_change | 3 | -0.047526 | 0.0892171 | {"17": 0.0087890625, "29": -0.0009765625, "43": -0.150390625} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | ba | uci_internal_fixed | nll_change | 3 | -0.0381867 | 0.276113 | {"17": 0.11000910014154106, "29": 0.1321881443071896, "43": -0.3567574366875513} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | ba | uci_internal_fixed | brier_change | 3 | -0.0588159 | 0.130869 | {"17": 0.02417226051021297, "29": 0.009058788359464392, "43": -0.20967861093763232} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | ba | uci_internal_fixed | ece15_change | 3 | 0.0019071 | 0.0777665 | {"17": 0.0393199679055308, "29": 0.05389602291180816, "43": -0.08749467591672275} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | ab | uci_internal_fixed | accuracy_change | 3 | 0.047526 | 0.0892171 | {"17": -0.0087890625, "29": 0.0009765625, "43": 0.150390625} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | ab | uci_internal_fixed | error_change | 3 | -0.047526 | 0.0892171 | {"17": 0.0087890625, "29": -0.0009765625, "43": -0.150390625} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | ab | uci_internal_fixed | nll_change | 3 | -0.0381867 | 0.276113 | {"17": 0.11000910014154106, "29": 0.1321881443071896, "43": -0.3567574366875513} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | ab | uci_internal_fixed | brier_change | 3 | -0.0588159 | 0.130869 | {"17": 0.02417226051021297, "29": 0.009058788359464392, "43": -0.20967861093763232} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | ab | uci_internal_fixed | ece15_change | 3 | 0.0019071 | 0.0777665 | {"17": 0.0393199679055308, "29": 0.05389602291180816, "43": -0.08749467591672275} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | ba | uci_internal_fixed | accuracy_change | 3 | 0.047526 | 0.0892171 | {"17": -0.0087890625, "29": 0.0009765625, "43": 0.150390625} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | ba | uci_internal_fixed | error_change | 3 | -0.047526 | 0.0892171 | {"17": 0.0087890625, "29": -0.0009765625, "43": -0.150390625} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | ba | uci_internal_fixed | nll_change | 3 | -0.0381867 | 0.276113 | {"17": 0.11000910014154106, "29": 0.1321881443071896, "43": -0.3567574366875513} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | ba | uci_internal_fixed | brier_change | 3 | -0.0588159 | 0.130869 | {"17": 0.02417226051021297, "29": 0.009058788359464392, "43": -0.20967861093763232} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | ba | uci_internal_fixed | ece15_change | 3 | 0.0019071 | 0.0777665 | {"17": 0.0393199679055308, "29": 0.05389602291180816, "43": -0.08749467591672275} |
| Tent | Reset all declared state | 0 | ab | uci_internal_fixed | accuracy_change | 3 | 0.047526 | 0.0892171 | {"17": -0.0087890625, "29": 0.0009765625, "43": 0.150390625} |
| Tent | Reset all declared state | 0 | ab | uci_internal_fixed | error_change | 3 | -0.047526 | 0.0892171 | {"17": 0.0087890625, "29": -0.0009765625, "43": -0.150390625} |
| Tent | Reset all declared state | 0 | ab | uci_internal_fixed | nll_change | 3 | -0.0377331 | 0.276423 | {"17": 0.11011851766535391, "29": 0.13332002148119498, "43": -0.3566379789094929} |
| Tent | Reset all declared state | 0 | ab | uci_internal_fixed | brier_change | 3 | -0.0587119 | 0.130924 | {"17": 0.024195599301651945, "29": 0.009314290690558046, "43": -0.20964568910799095} |
| Tent | Reset all declared state | 0 | ab | uci_internal_fixed | ece15_change | 3 | 0.00192471 | 0.0777848 | {"17": 0.03933688392256045, "29": 0.0539343619786498, "43": -0.08749710483920495} |
| Tent | Reset all declared state | 0 | ba | uci_internal_fixed | accuracy_change | 3 | 0.047526 | 0.0892171 | {"17": -0.0087890625, "29": 0.0009765625, "43": 0.150390625} |
| Tent | Reset all declared state | 0 | ba | uci_internal_fixed | error_change | 3 | -0.047526 | 0.0892171 | {"17": 0.0087890625, "29": -0.0009765625, "43": -0.150390625} |
| Tent | Reset all declared state | 0 | ba | uci_internal_fixed | nll_change | 3 | -0.0377331 | 0.276423 | {"17": 0.11011851766535391, "29": 0.13332002148119498, "43": -0.3566379789094929} |
| Tent | Reset all declared state | 0 | ba | uci_internal_fixed | brier_change | 3 | -0.0587119 | 0.130924 | {"17": 0.024195599301651945, "29": 0.009314290690558046, "43": -0.20964568910799095} |
| Tent | Reset all declared state | 0 | ba | uci_internal_fixed | ece15_change | 3 | 0.00192471 | 0.0777848 | {"17": 0.03933688392256045, "29": 0.0539343619786498, "43": -0.08749710483920495} |
| Tent | Reset all declared state | 4 | ab | uci_internal_fixed | accuracy_change | 3 | 0.047526 | 0.0892171 | {"17": -0.0087890625, "29": 0.0009765625, "43": 0.150390625} |
| Tent | Reset all declared state | 4 | ab | uci_internal_fixed | error_change | 3 | -0.047526 | 0.0892171 | {"17": 0.0087890625, "29": -0.0009765625, "43": -0.150390625} |
| Tent | Reset all declared state | 4 | ab | uci_internal_fixed | nll_change | 3 | -0.0377331 | 0.276423 | {"17": 0.11011851766535391, "29": 0.13332002148119498, "43": -0.3566379789094929} |
| Tent | Reset all declared state | 4 | ab | uci_internal_fixed | brier_change | 3 | -0.0587119 | 0.130924 | {"17": 0.024195599301651945, "29": 0.009314290690558046, "43": -0.20964568910799095} |
| Tent | Reset all declared state | 4 | ab | uci_internal_fixed | ece15_change | 3 | 0.00192471 | 0.0777848 | {"17": 0.03933688392256045, "29": 0.0539343619786498, "43": -0.08749710483920495} |
| Tent | Reset all declared state | 4 | ba | uci_internal_fixed | accuracy_change | 3 | 0.047526 | 0.0892171 | {"17": -0.0087890625, "29": 0.0009765625, "43": 0.150390625} |
| Tent | Reset all declared state | 4 | ba | uci_internal_fixed | error_change | 3 | -0.047526 | 0.0892171 | {"17": 0.0087890625, "29": -0.0009765625, "43": -0.150390625} |
| Tent | Reset all declared state | 4 | ba | uci_internal_fixed | nll_change | 3 | -0.0377331 | 0.276423 | {"17": 0.11011851766535391, "29": 0.13332002148119498, "43": -0.3566379789094929} |
| Tent | Reset all declared state | 4 | ba | uci_internal_fixed | brier_change | 3 | -0.0587119 | 0.130924 | {"17": 0.024195599301651945, "29": 0.009314290690558046, "43": -0.20964568910799095} |
| Tent | Reset all declared state | 4 | ba | uci_internal_fixed | ece15_change | 3 | 0.00192471 | 0.0777848 | {"17": 0.03933688392256045, "29": 0.0539343619786498, "43": -0.08749710483920495} |
| Tent | Reset auxiliary state only | 0 | ab | uci_internal_fixed | accuracy_change | 3 | 0.0478516 | 0.0889101 | {"17": -0.0078125, "29": 0.0009765625, "43": 0.150390625} |
| Tent | Reset auxiliary state only | 0 | ab | uci_internal_fixed | error_change | 3 | -0.0478516 | 0.0889101 | {"17": 0.0078125, "29": -0.0009765625, "43": -0.150390625} |
| Tent | Reset auxiliary state only | 0 | ab | uci_internal_fixed | nll_change | 3 | -0.0379482 | 0.275912 | {"17": 0.10963812979424517, "29": 0.13278065245795223, "43": -0.3562632699013895} |
| Tent | Reset auxiliary state only | 0 | ab | uci_internal_fixed | brier_change | 3 | -0.0587858 | 0.13079 | {"17": 0.024034296440376454, "29": 0.009173433308529141, "43": -0.20956514753342007} |
| Tent | Reset auxiliary state only | 0 | ab | uci_internal_fixed | ece15_change | 3 | 0.00227145 | 0.0774808 | {"17": 0.03893119337986095, "29": 0.05461920298362195, "43": -0.08673605992602551} |
| Tent | Reset auxiliary state only | 0 | ba | uci_internal_fixed | accuracy_change | 3 | 0.047526 | 0.0892171 | {"17": -0.0087890625, "29": 0.0009765625, "43": 0.150390625} |
| Tent | Reset auxiliary state only | 0 | ba | uci_internal_fixed | error_change | 3 | -0.047526 | 0.0892171 | {"17": 0.0087890625, "29": -0.0009765625, "43": -0.150390625} |
| Tent | Reset auxiliary state only | 0 | ba | uci_internal_fixed | nll_change | 3 | -0.0379743 | 0.275961 | {"17": 0.10966107953420932, "29": 0.13276285277097108, "43": -0.3563469031165934} |
| Tent | Reset auxiliary state only | 0 | ba | uci_internal_fixed | brier_change | 3 | -0.058788 | 0.130808 | {"17": 0.02404823553167357, "29": 0.00917606653657099, "43": -0.20958842609887507} |
| Tent | Reset auxiliary state only | 0 | ba | uci_internal_fixed | ece15_change | 3 | 0.0024227 | 0.0776033 | {"17": 0.039408407181286, "29": 0.05461441966869815, "43": -0.08675471715349489} |
| Tent | Reset auxiliary state only | 4 | ab | uci_internal_fixed | accuracy_change | 3 | 0.0481771 | 0.0886057 | {"17": -0.0068359375, "29": 0.0009765625, "43": 0.150390625} |
| Tent | Reset auxiliary state only | 4 | ab | uci_internal_fixed | error_change | 3 | -0.0481771 | 0.0886057 | {"17": 0.0068359375, "29": -0.0009765625, "43": -0.150390625} |
| Tent | Reset auxiliary state only | 4 | ab | uci_internal_fixed | nll_change | 3 | -0.0374637 | 0.277146 | {"17": 0.10941946227901544, "29": 0.13532460269056726, "43": -0.3571350442044503} |
| Tent | Reset auxiliary state only | 4 | ab | uci_internal_fixed | brier_change | 3 | -0.0587313 | 0.131077 | {"17": 0.023954036815489507, "29": 0.009714636399896849, "43": -0.2098626480583646} |
| Tent | Reset auxiliary state only | 4 | ab | uci_internal_fixed | ece15_change | 3 | 0.00212155 | 0.077207 | {"17": 0.039786304812415456, "29": 0.053267362092632095, "43": -0.08668902243018345} |
| Tent | Reset auxiliary state only | 4 | ba | uci_internal_fixed | accuracy_change | 3 | 0.0481771 | 0.0886057 | {"17": -0.0068359375, "29": 0.0009765625, "43": 0.150390625} |
| Tent | Reset auxiliary state only | 4 | ba | uci_internal_fixed | error_change | 3 | -0.0481771 | 0.0886057 | {"17": 0.0068359375, "29": -0.0009765625, "43": -0.150390625} |
| Tent | Reset auxiliary state only | 4 | ba | uci_internal_fixed | nll_change | 3 | -0.0374809 | 0.277178 | {"17": 0.109436423464323, "29": 0.13531007729927363, "43": -0.3571893378981537} |
| Tent | Reset auxiliary state only | 4 | ba | uci_internal_fixed | brier_change | 3 | -0.0587329 | 0.131089 | {"17": 0.0239635933348913, "29": 0.009715298774736054, "43": -0.20987763089500977} |
| Tent | Reset auxiliary state only | 4 | ba | uci_internal_fixed | ece15_change | 3 | 0.00211314 | 0.0772103 | {"17": 0.03978048211310755, "29": 0.05326020549375861, "43": -0.08670127602471125} |
| Tent | No external reset | 0 | ab | uci_internal_fixed | accuracy_change | 3 | 0.0478516 | 0.0889101 | {"17": -0.0078125, "29": 0.0009765625, "43": 0.150390625} |
| Tent | No external reset | 0 | ab | uci_internal_fixed | error_change | 3 | -0.0478516 | 0.0889101 | {"17": 0.0078125, "29": -0.0009765625, "43": -0.150390625} |
| Tent | No external reset | 0 | ab | uci_internal_fixed | nll_change | 3 | -0.0379482 | 0.275912 | {"17": 0.10963812979424517, "29": 0.13278065245795223, "43": -0.3562632699013895} |
| Tent | No external reset | 0 | ab | uci_internal_fixed | brier_change | 3 | -0.0587858 | 0.13079 | {"17": 0.024034296440376454, "29": 0.009173433308529141, "43": -0.20956514753342007} |
| Tent | No external reset | 0 | ab | uci_internal_fixed | ece15_change | 3 | 0.00227145 | 0.0774808 | {"17": 0.03893119337986095, "29": 0.05461920298362195, "43": -0.08673605992602551} |
| Tent | No external reset | 0 | ba | uci_internal_fixed | accuracy_change | 3 | 0.047526 | 0.0892171 | {"17": -0.0087890625, "29": 0.0009765625, "43": 0.150390625} |
| Tent | No external reset | 0 | ba | uci_internal_fixed | error_change | 3 | -0.047526 | 0.0892171 | {"17": 0.0087890625, "29": -0.0009765625, "43": -0.150390625} |
| Tent | No external reset | 0 | ba | uci_internal_fixed | nll_change | 3 | -0.0379743 | 0.275961 | {"17": 0.10966107953420932, "29": 0.13276285277097108, "43": -0.3563469031165934} |
| Tent | No external reset | 0 | ba | uci_internal_fixed | brier_change | 3 | -0.058788 | 0.130808 | {"17": 0.02404823553167357, "29": 0.00917606653657099, "43": -0.20958842609887507} |
| Tent | No external reset | 0 | ba | uci_internal_fixed | ece15_change | 3 | 0.0024227 | 0.0776033 | {"17": 0.039408407181286, "29": 0.05461441966869815, "43": -0.08675471715349489} |
| Tent | No external reset | 4 | ab | uci_internal_fixed | accuracy_change | 3 | 0.0481771 | 0.0886057 | {"17": -0.0068359375, "29": 0.0009765625, "43": 0.150390625} |
| Tent | No external reset | 4 | ab | uci_internal_fixed | error_change | 3 | -0.0481771 | 0.0886057 | {"17": 0.0068359375, "29": -0.0009765625, "43": -0.150390625} |
| Tent | No external reset | 4 | ab | uci_internal_fixed | nll_change | 3 | -0.0374637 | 0.277146 | {"17": 0.10941946227901544, "29": 0.13532460269056726, "43": -0.3571350442044503} |
| Tent | No external reset | 4 | ab | uci_internal_fixed | brier_change | 3 | -0.0587313 | 0.131077 | {"17": 0.023954036815489507, "29": 0.009714636399896849, "43": -0.2098626480583646} |
| Tent | No external reset | 4 | ab | uci_internal_fixed | ece15_change | 3 | 0.00212155 | 0.077207 | {"17": 0.039786304812415456, "29": 0.053267362092632095, "43": -0.08668902243018345} |
| Tent | No external reset | 4 | ba | uci_internal_fixed | accuracy_change | 3 | 0.0481771 | 0.0886057 | {"17": -0.0068359375, "29": 0.0009765625, "43": 0.150390625} |
| Tent | No external reset | 4 | ba | uci_internal_fixed | error_change | 3 | -0.0481771 | 0.0886057 | {"17": 0.0068359375, "29": -0.0009765625, "43": -0.150390625} |
| Tent | No external reset | 4 | ba | uci_internal_fixed | nll_change | 3 | -0.0374809 | 0.277178 | {"17": 0.109436423464323, "29": 0.13531007729927363, "43": -0.3571893378981537} |
| Tent | No external reset | 4 | ba | uci_internal_fixed | brier_change | 3 | -0.0587329 | 0.131089 | {"17": 0.0239635933348913, "29": 0.009715298774736054, "43": -0.20987763089500977} |
| Tent | No external reset | 4 | ba | uci_internal_fixed | ece15_change | 3 | 0.00211314 | 0.0772103 | {"17": 0.03978048211310755, "29": 0.05326020549375861, "43": -0.08670127602471125} |
| Tent | Reset optimizer only | 0 | ab | uci_internal_fixed | accuracy_change | 3 | 0.0478516 | 0.0889101 | {"17": -0.0078125, "29": 0.0009765625, "43": 0.150390625} |
| Tent | Reset optimizer only | 0 | ab | uci_internal_fixed | error_change | 3 | -0.0478516 | 0.0889101 | {"17": 0.0078125, "29": -0.0009765625, "43": -0.150390625} |
| Tent | Reset optimizer only | 0 | ab | uci_internal_fixed | nll_change | 3 | -0.0378581 | 0.276058 | {"17": 0.10971285162670061, "29": 0.133050107189378, "43": -0.3563373029829046} |
| Tent | Reset optimizer only | 0 | ab | uci_internal_fixed | brier_change | 3 | -0.0587657 | 0.130821 | {"17": 0.02405497621822625, "29": 0.009229579388680902, "43": -0.20958177562182567} |
| Tent | Reset optimizer only | 0 | ab | uci_internal_fixed | ece15_change | 3 | 0.002042 | 0.0778618 | {"17": 0.0389184445788009, "29": 0.05461473839817341, "43": -0.087407175368801} |
| Tent | Reset optimizer only | 0 | ba | uci_internal_fixed | accuracy_change | 3 | 0.047526 | 0.0892171 | {"17": -0.0087890625, "29": 0.0009765625, "43": 0.150390625} |
| Tent | Reset optimizer only | 0 | ba | uci_internal_fixed | error_change | 3 | -0.047526 | 0.0892171 | {"17": 0.0087890625, "29": -0.0009765625, "43": -0.150390625} |
| Tent | Reset optimizer only | 0 | ba | uci_internal_fixed | nll_change | 3 | -0.037921 | 0.276168 | {"17": 0.1097524199116374, "29": 0.1330143540545594, "43": -0.3565296796915818} |
| Tent | Reset optimizer only | 0 | ba | uci_internal_fixed | brier_change | 3 | -0.0587703 | 0.130856 | {"17": 0.024082719461090966, "29": 0.00923324044510455, "43": -0.20962695631011477} |
| Tent | Reset optimizer only | 0 | ba | uci_internal_fixed | ece15_change | 3 | 0.00218176 | 0.0773982 | {"17": 0.03938233435398375, "29": 0.05395591533605255, "43": -0.08679297735071224} |
| Tent | Reset optimizer only | 4 | ab | uci_internal_fixed | accuracy_change | 3 | 0.0481771 | 0.0886057 | {"17": -0.0068359375, "29": 0.0009765625, "43": 0.150390625} |
| Tent | Reset optimizer only | 4 | ab | uci_internal_fixed | error_change | 3 | -0.0481771 | 0.0886057 | {"17": 0.0068359375, "29": -0.0009765625, "43": -0.150390625} |
| Tent | Reset optimizer only | 4 | ab | uci_internal_fixed | nll_change | 3 | -0.0378228 | 0.276372 | {"17": 0.10955955155467736, "29": 0.13361947313746672, "43": -0.3566473569279942} |
| Tent | Reset optimizer only | 4 | ab | uci_internal_fixed | brier_change | 3 | -0.0587778 | 0.130899 | {"17": 0.024005604345219304, "29": 0.009350630548479049, "43": -0.20968978471940122} |
| Tent | Reset optimizer only | 4 | ab | uci_internal_fixed | ece15_change | 3 | 0.00191103 | 0.0776249 | {"17": 0.03976356489960994, "29": 0.053348268505332, "43": -0.08737872873511425} |
| Tent | Reset optimizer only | 4 | ba | uci_internal_fixed | accuracy_change | 3 | 0.0481771 | 0.0886057 | {"17": -0.0068359375, "29": 0.0009765625, "43": 0.150390625} |
| Tent | Reset optimizer only | 4 | ba | uci_internal_fixed | error_change | 3 | -0.0481771 | 0.0886057 | {"17": 0.0068359375, "29": -0.0009765625, "43": -0.150390625} |
| Tent | Reset optimizer only | 4 | ba | uci_internal_fixed | nll_change | 3 | -0.0378645 | 0.276445 | {"17": 0.1095853358924318, "29": 0.13359549629700207, "43": -0.35677440522672144} |
| Tent | Reset optimizer only | 4 | ba | uci_internal_fixed | brier_change | 3 | -0.0587812 | 0.130922 | {"17": 0.024023610152473562, "29": 0.009352634846969955, "43": -0.20971969724200962} |
| Tent | Reset optimizer only | 4 | ba | uci_internal_fixed | ece15_change | 3 | 0.00211483 | 0.0772599 | {"17": 0.039752035297205994, "29": 0.05334384112894976, "43": -0.0867513785770405} |
| Tent | Reset optimizer + auxiliary state | 0 | ab | uci_internal_fixed | accuracy_change | 3 | 0.0478516 | 0.0889101 | {"17": -0.0078125, "29": 0.0009765625, "43": 0.150390625} |
| Tent | Reset optimizer + auxiliary state | 0 | ab | uci_internal_fixed | error_change | 3 | -0.0478516 | 0.0889101 | {"17": 0.0078125, "29": -0.0009765625, "43": -0.150390625} |
| Tent | Reset optimizer + auxiliary state | 0 | ab | uci_internal_fixed | nll_change | 3 | -0.0378581 | 0.276058 | {"17": 0.10971285162670061, "29": 0.133050107189378, "43": -0.3563373029829046} |
| Tent | Reset optimizer + auxiliary state | 0 | ab | uci_internal_fixed | brier_change | 3 | -0.0587657 | 0.130821 | {"17": 0.02405497621822625, "29": 0.009229579388680902, "43": -0.20958177562182567} |
| Tent | Reset optimizer + auxiliary state | 0 | ab | uci_internal_fixed | ece15_change | 3 | 0.002042 | 0.0778618 | {"17": 0.0389184445788009, "29": 0.05461473839817341, "43": -0.087407175368801} |
| Tent | Reset optimizer + auxiliary state | 0 | ba | uci_internal_fixed | accuracy_change | 3 | 0.047526 | 0.0892171 | {"17": -0.0087890625, "29": 0.0009765625, "43": 0.150390625} |
| Tent | Reset optimizer + auxiliary state | 0 | ba | uci_internal_fixed | error_change | 3 | -0.047526 | 0.0892171 | {"17": 0.0087890625, "29": -0.0009765625, "43": -0.150390625} |
| Tent | Reset optimizer + auxiliary state | 0 | ba | uci_internal_fixed | nll_change | 3 | -0.037921 | 0.276168 | {"17": 0.1097524199116374, "29": 0.1330143540545594, "43": -0.3565296796915818} |
| Tent | Reset optimizer + auxiliary state | 0 | ba | uci_internal_fixed | brier_change | 3 | -0.0587703 | 0.130856 | {"17": 0.024082719461090966, "29": 0.00923324044510455, "43": -0.20962695631011477} |
| Tent | Reset optimizer + auxiliary state | 0 | ba | uci_internal_fixed | ece15_change | 3 | 0.00218176 | 0.0773982 | {"17": 0.03938233435398375, "29": 0.05395591533605255, "43": -0.08679297735071224} |
| Tent | Reset optimizer + auxiliary state | 4 | ab | uci_internal_fixed | accuracy_change | 3 | 0.0481771 | 0.0886057 | {"17": -0.0068359375, "29": 0.0009765625, "43": 0.150390625} |
| Tent | Reset optimizer + auxiliary state | 4 | ab | uci_internal_fixed | error_change | 3 | -0.0481771 | 0.0886057 | {"17": 0.0068359375, "29": -0.0009765625, "43": -0.150390625} |
| Tent | Reset optimizer + auxiliary state | 4 | ab | uci_internal_fixed | nll_change | 3 | -0.0378228 | 0.276372 | {"17": 0.10955955155467736, "29": 0.13361947313746672, "43": -0.3566473569279942} |
| Tent | Reset optimizer + auxiliary state | 4 | ab | uci_internal_fixed | brier_change | 3 | -0.0587778 | 0.130899 | {"17": 0.024005604345219304, "29": 0.009350630548479049, "43": -0.20968978471940122} |
| Tent | Reset optimizer + auxiliary state | 4 | ab | uci_internal_fixed | ece15_change | 3 | 0.00191103 | 0.0776249 | {"17": 0.03976356489960994, "29": 0.053348268505332, "43": -0.08737872873511425} |
| Tent | Reset optimizer + auxiliary state | 4 | ba | uci_internal_fixed | accuracy_change | 3 | 0.0481771 | 0.0886057 | {"17": -0.0068359375, "29": 0.0009765625, "43": 0.150390625} |
| Tent | Reset optimizer + auxiliary state | 4 | ba | uci_internal_fixed | error_change | 3 | -0.0481771 | 0.0886057 | {"17": 0.0068359375, "29": -0.0009765625, "43": -0.150390625} |
| Tent | Reset optimizer + auxiliary state | 4 | ba | uci_internal_fixed | nll_change | 3 | -0.0378645 | 0.276445 | {"17": 0.1095853358924318, "29": 0.13359549629700207, "43": -0.35677440522672144} |
| Tent | Reset optimizer + auxiliary state | 4 | ba | uci_internal_fixed | brier_change | 3 | -0.0587812 | 0.130922 | {"17": 0.024023610152473562, "29": 0.009352634846969955, "43": -0.20971969724200962} |
| Tent | Reset optimizer + auxiliary state | 4 | ba | uci_internal_fixed | ece15_change | 3 | 0.00211483 | 0.0772599 | {"17": 0.039752035297205994, "29": 0.05334384112894976, "43": -0.0867513785770405} |
| Tent | Reset parameters only | 0 | ab | uci_internal_fixed | accuracy_change | 3 | 0.047526 | 0.0892171 | {"17": -0.0087890625, "29": 0.0009765625, "43": 0.150390625} |
| Tent | Reset parameters only | 0 | ab | uci_internal_fixed | error_change | 3 | -0.047526 | 0.0892171 | {"17": 0.0087890625, "29": -0.0009765625, "43": -0.150390625} |
| Tent | Reset parameters only | 0 | ab | uci_internal_fixed | nll_change | 3 | -0.0378239 | 0.276277 | {"17": 0.11004481684954648, "29": 0.1330483476316695, "43": -0.35656493073542883} |
| Tent | Reset parameters only | 0 | ab | uci_internal_fixed | brier_change | 3 | -0.0587325 | 0.130893 | {"17": 0.0241749000176671, "29": 0.009257203473414936, "43": -0.20962946186169856} |
| Tent | Reset parameters only | 0 | ab | uci_internal_fixed | ece15_change | 3 | 0.00193749 | 0.0777786 | {"17": 0.03935124365705374, "29": 0.05393893295302136, "43": -0.08747769940143925} |
| Tent | Reset parameters only | 0 | ba | uci_internal_fixed | accuracy_change | 3 | 0.047526 | 0.0892171 | {"17": -0.0087890625, "29": 0.0009765625, "43": 0.150390625} |
| Tent | Reset parameters only | 0 | ba | uci_internal_fixed | error_change | 3 | -0.047526 | 0.0892171 | {"17": 0.0087890625, "29": -0.0009765625, "43": -0.150390625} |
| Tent | Reset parameters only | 0 | ba | uci_internal_fixed | nll_change | 3 | -0.0377873 | 0.276217 | {"17": 0.11003133191145656, "29": 0.13306429150336646, "43": -0.3564575450686798} |
| Tent | Reset parameters only | 0 | ba | uci_internal_fixed | brier_change | 3 | -0.0587301 | 0.130877 | {"17": 0.024161957819863564, "29": 0.009255796890584603, "43": -0.20960807633530676} |
| Tent | Reset parameters only | 0 | ba | uci_internal_fixed | ece15_change | 3 | 0.00194853 | 0.0777722 | {"17": 0.0393633684539043, "29": 0.05394195245319745, "43": -0.08745974229075903} |
| Tent | Reset parameters only | 4 | ab | uci_internal_fixed | accuracy_change | 3 | 0.047526 | 0.0892171 | {"17": -0.0087890625, "29": 0.0009765625, "43": 0.150390625} |
| Tent | Reset parameters only | 4 | ab | uci_internal_fixed | error_change | 3 | -0.047526 | 0.0892171 | {"17": 0.0087890625, "29": -0.0009765625, "43": -0.150390625} |
| Tent | Reset parameters only | 4 | ab | uci_internal_fixed | nll_change | 3 | -0.0373768 | 0.277197 | {"17": 0.10997784087058576, "29": 0.13502080791997087, "43": -0.35712919291557194} |
| Tent | Reset parameters only | 4 | ab | uci_internal_fixed | brier_change | 3 | -0.0586665 | 0.131102 | {"17": 0.024143554129300467, "29": 0.009676852225050507, "43": -0.20981992955692796} |
| Tent | Reset parameters only | 4 | ab | uci_internal_fixed | ece15_change | 3 | 0.00197852 | 0.0777999 | {"17": 0.03937182698247074, "29": 0.0540217372274317, "43": -0.0874579991100925} |
| Tent | Reset parameters only | 4 | ba | uci_internal_fixed | accuracy_change | 3 | 0.047526 | 0.0892171 | {"17": -0.0087890625, "29": 0.0009765625, "43": 0.150390625} |
| Tent | Reset parameters only | 4 | ba | uci_internal_fixed | error_change | 3 | -0.047526 | 0.0892171 | {"17": 0.0087890625, "29": -0.0009765625, "43": -0.150390625} |
| Tent | Reset parameters only | 4 | ba | uci_internal_fixed | nll_change | 3 | -0.0373531 | 0.277155 | {"17": 0.10996979068066136, "29": 0.1350282407058995, "43": -0.3570574618202251} |
| Tent | Reset parameters only | 4 | ba | uci_internal_fixed | brier_change | 3 | -0.0586651 | 0.131091 | {"17": 0.024135201959160472, "29": 0.009674854147694707, "43": -0.20980543847231722} |
| Tent | Reset parameters only | 4 | ba | uci_internal_fixed | ece15_change | 3 | 0.00181216 | 0.0776219 | {"17": 0.03937982649810459, "29": 0.05350283206756434, "43": -0.0874461701677273} |
| Tent | Reset parameters + auxiliary state | 0 | ab | uci_internal_fixed | accuracy_change | 3 | 0.047526 | 0.0892171 | {"17": -0.0087890625, "29": 0.0009765625, "43": 0.150390625} |
| Tent | Reset parameters + auxiliary state | 0 | ab | uci_internal_fixed | error_change | 3 | -0.047526 | 0.0892171 | {"17": 0.0087890625, "29": -0.0009765625, "43": -0.150390625} |
| Tent | Reset parameters + auxiliary state | 0 | ab | uci_internal_fixed | nll_change | 3 | -0.0378239 | 0.276277 | {"17": 0.11004481684954648, "29": 0.1330483476316695, "43": -0.35656493073542883} |
| Tent | Reset parameters + auxiliary state | 0 | ab | uci_internal_fixed | brier_change | 3 | -0.0587325 | 0.130893 | {"17": 0.0241749000176671, "29": 0.009257203473414936, "43": -0.20962946186169856} |
| Tent | Reset parameters + auxiliary state | 0 | ab | uci_internal_fixed | ece15_change | 3 | 0.00193749 | 0.0777786 | {"17": 0.03935124365705374, "29": 0.05393893295302136, "43": -0.08747769940143925} |
| Tent | Reset parameters + auxiliary state | 0 | ba | uci_internal_fixed | accuracy_change | 3 | 0.047526 | 0.0892171 | {"17": -0.0087890625, "29": 0.0009765625, "43": 0.150390625} |
| Tent | Reset parameters + auxiliary state | 0 | ba | uci_internal_fixed | error_change | 3 | -0.047526 | 0.0892171 | {"17": 0.0087890625, "29": -0.0009765625, "43": -0.150390625} |
| Tent | Reset parameters + auxiliary state | 0 | ba | uci_internal_fixed | nll_change | 3 | -0.0377873 | 0.276217 | {"17": 0.11003133191145656, "29": 0.13306429150336646, "43": -0.3564575450686798} |
| Tent | Reset parameters + auxiliary state | 0 | ba | uci_internal_fixed | brier_change | 3 | -0.0587301 | 0.130877 | {"17": 0.024161957819863564, "29": 0.009255796890584603, "43": -0.20960807633530676} |
| Tent | Reset parameters + auxiliary state | 0 | ba | uci_internal_fixed | ece15_change | 3 | 0.00194853 | 0.0777722 | {"17": 0.0393633684539043, "29": 0.05394195245319745, "43": -0.08745974229075903} |
| Tent | Reset parameters + auxiliary state | 4 | ab | uci_internal_fixed | accuracy_change | 3 | 0.047526 | 0.0892171 | {"17": -0.0087890625, "29": 0.0009765625, "43": 0.150390625} |
| Tent | Reset parameters + auxiliary state | 4 | ab | uci_internal_fixed | error_change | 3 | -0.047526 | 0.0892171 | {"17": 0.0087890625, "29": -0.0009765625, "43": -0.150390625} |
| Tent | Reset parameters + auxiliary state | 4 | ab | uci_internal_fixed | nll_change | 3 | -0.0373768 | 0.277197 | {"17": 0.10997784087058576, "29": 0.13502080791997087, "43": -0.35712919291557194} |
| Tent | Reset parameters + auxiliary state | 4 | ab | uci_internal_fixed | brier_change | 3 | -0.0586665 | 0.131102 | {"17": 0.024143554129300467, "29": 0.009676852225050507, "43": -0.20981992955692796} |
| Tent | Reset parameters + auxiliary state | 4 | ab | uci_internal_fixed | ece15_change | 3 | 0.00197852 | 0.0777999 | {"17": 0.03937182698247074, "29": 0.0540217372274317, "43": -0.0874579991100925} |
| Tent | Reset parameters + auxiliary state | 4 | ba | uci_internal_fixed | accuracy_change | 3 | 0.047526 | 0.0892171 | {"17": -0.0087890625, "29": 0.0009765625, "43": 0.150390625} |
| Tent | Reset parameters + auxiliary state | 4 | ba | uci_internal_fixed | error_change | 3 | -0.047526 | 0.0892171 | {"17": 0.0087890625, "29": -0.0009765625, "43": -0.150390625} |
| Tent | Reset parameters + auxiliary state | 4 | ba | uci_internal_fixed | nll_change | 3 | -0.0373531 | 0.277155 | {"17": 0.10996979068066136, "29": 0.1350282407058995, "43": -0.3570574618202251} |
| Tent | Reset parameters + auxiliary state | 4 | ba | uci_internal_fixed | brier_change | 3 | -0.0586651 | 0.131091 | {"17": 0.024135201959160472, "29": 0.009674854147694707, "43": -0.20980543847231722} |
| Tent | Reset parameters + auxiliary state | 4 | ba | uci_internal_fixed | ece15_change | 3 | 0.00181216 | 0.0776219 | {"17": 0.03937982649810459, "29": 0.05350283206756434, "43": -0.0874461701677273} |
| Tent | Reset parameters + optimizer | 0 | ab | uci_internal_fixed | accuracy_change | 3 | 0.047526 | 0.0892171 | {"17": -0.0087890625, "29": 0.0009765625, "43": 0.150390625} |
| Tent | Reset parameters + optimizer | 0 | ab | uci_internal_fixed | error_change | 3 | -0.047526 | 0.0892171 | {"17": 0.0087890625, "29": -0.0009765625, "43": -0.150390625} |
| Tent | Reset parameters + optimizer | 0 | ab | uci_internal_fixed | nll_change | 3 | -0.0377331 | 0.276423 | {"17": 0.11011851766535391, "29": 0.13332002148119498, "43": -0.3566379789094929} |
| Tent | Reset parameters + optimizer | 0 | ab | uci_internal_fixed | brier_change | 3 | -0.0587119 | 0.130924 | {"17": 0.024195599301651945, "29": 0.009314290690558046, "43": -0.20964568910799095} |
| Tent | Reset parameters + optimizer | 0 | ab | uci_internal_fixed | ece15_change | 3 | 0.00192471 | 0.0777848 | {"17": 0.03933688392256045, "29": 0.0539343619786498, "43": -0.08749710483920495} |
| Tent | Reset parameters + optimizer | 0 | ba | uci_internal_fixed | accuracy_change | 3 | 0.047526 | 0.0892171 | {"17": -0.0087890625, "29": 0.0009765625, "43": 0.150390625} |
| Tent | Reset parameters + optimizer | 0 | ba | uci_internal_fixed | error_change | 3 | -0.047526 | 0.0892171 | {"17": 0.0087890625, "29": -0.0009765625, "43": -0.150390625} |
| Tent | Reset parameters + optimizer | 0 | ba | uci_internal_fixed | nll_change | 3 | -0.0377331 | 0.276423 | {"17": 0.11011851766535391, "29": 0.13332002148119498, "43": -0.3566379789094929} |
| Tent | Reset parameters + optimizer | 0 | ba | uci_internal_fixed | brier_change | 3 | -0.0587119 | 0.130924 | {"17": 0.024195599301651945, "29": 0.009314290690558046, "43": -0.20964568910799095} |
| Tent | Reset parameters + optimizer | 0 | ba | uci_internal_fixed | ece15_change | 3 | 0.00192471 | 0.0777848 | {"17": 0.03933688392256045, "29": 0.0539343619786498, "43": -0.08749710483920495} |
| Tent | Reset parameters + optimizer | 4 | ab | uci_internal_fixed | accuracy_change | 3 | 0.047526 | 0.0892171 | {"17": -0.0087890625, "29": 0.0009765625, "43": 0.150390625} |
| Tent | Reset parameters + optimizer | 4 | ab | uci_internal_fixed | error_change | 3 | -0.047526 | 0.0892171 | {"17": 0.0087890625, "29": -0.0009765625, "43": -0.150390625} |
| Tent | Reset parameters + optimizer | 4 | ab | uci_internal_fixed | nll_change | 3 | -0.0377331 | 0.276423 | {"17": 0.11011851766535391, "29": 0.13332002148119498, "43": -0.3566379789094929} |
| Tent | Reset parameters + optimizer | 4 | ab | uci_internal_fixed | brier_change | 3 | -0.0587119 | 0.130924 | {"17": 0.024195599301651945, "29": 0.009314290690558046, "43": -0.20964568910799095} |
| Tent | Reset parameters + optimizer | 4 | ab | uci_internal_fixed | ece15_change | 3 | 0.00192471 | 0.0777848 | {"17": 0.03933688392256045, "29": 0.0539343619786498, "43": -0.08749710483920495} |
| Tent | Reset parameters + optimizer | 4 | ba | uci_internal_fixed | accuracy_change | 3 | 0.047526 | 0.0892171 | {"17": -0.0087890625, "29": 0.0009765625, "43": 0.150390625} |
| Tent | Reset parameters + optimizer | 4 | ba | uci_internal_fixed | error_change | 3 | -0.047526 | 0.0892171 | {"17": 0.0087890625, "29": -0.0009765625, "43": -0.150390625} |
| Tent | Reset parameters + optimizer | 4 | ba | uci_internal_fixed | nll_change | 3 | -0.0377331 | 0.276423 | {"17": 0.11011851766535391, "29": 0.13332002148119498, "43": -0.3566379789094929} |
| Tent | Reset parameters + optimizer | 4 | ba | uci_internal_fixed | brier_change | 3 | -0.0587119 | 0.130924 | {"17": 0.024195599301651945, "29": 0.009314290690558046, "43": -0.20964568910799095} |
| Tent | Reset parameters + optimizer | 4 | ba | uci_internal_fixed | ece15_change | 3 | 0.00192471 | 0.0777848 | {"17": 0.03933688392256045, "29": 0.0539343619786498, "43": -0.08749710483920495} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | ab | uci_internal_fixed | accuracy_change | 3 | 0.047526 | 0.0892171 | {"17": -0.0087890625, "29": 0.0009765625, "43": 0.150390625} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | ab | uci_internal_fixed | error_change | 3 | -0.047526 | 0.0892171 | {"17": 0.0087890625, "29": -0.0009765625, "43": -0.150390625} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | ab | uci_internal_fixed | nll_change | 3 | -0.0377331 | 0.276423 | {"17": 0.11011851766535391, "29": 0.13332002148119498, "43": -0.3566379789094929} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | ab | uci_internal_fixed | brier_change | 3 | -0.0587119 | 0.130924 | {"17": 0.024195599301651945, "29": 0.009314290690558046, "43": -0.20964568910799095} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | ab | uci_internal_fixed | ece15_change | 3 | 0.00192471 | 0.0777848 | {"17": 0.03933688392256045, "29": 0.0539343619786498, "43": -0.08749710483920495} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | ba | uci_internal_fixed | accuracy_change | 3 | 0.047526 | 0.0892171 | {"17": -0.0087890625, "29": 0.0009765625, "43": 0.150390625} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | ba | uci_internal_fixed | error_change | 3 | -0.047526 | 0.0892171 | {"17": 0.0087890625, "29": -0.0009765625, "43": -0.150390625} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | ba | uci_internal_fixed | nll_change | 3 | -0.0377331 | 0.276423 | {"17": 0.11011851766535391, "29": 0.13332002148119498, "43": -0.3566379789094929} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | ba | uci_internal_fixed | brier_change | 3 | -0.0587119 | 0.130924 | {"17": 0.024195599301651945, "29": 0.009314290690558046, "43": -0.20964568910799095} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | ba | uci_internal_fixed | ece15_change | 3 | 0.00192471 | 0.0777848 | {"17": 0.03933688392256045, "29": 0.0539343619786498, "43": -0.08749710483920495} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | ab | uci_internal_fixed | accuracy_change | 3 | 0.047526 | 0.0892171 | {"17": -0.0087890625, "29": 0.0009765625, "43": 0.150390625} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | ab | uci_internal_fixed | error_change | 3 | -0.047526 | 0.0892171 | {"17": 0.0087890625, "29": -0.0009765625, "43": -0.150390625} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | ab | uci_internal_fixed | nll_change | 3 | -0.0377331 | 0.276423 | {"17": 0.11011851766535391, "29": 0.13332002148119498, "43": -0.3566379789094929} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | ab | uci_internal_fixed | brier_change | 3 | -0.0587119 | 0.130924 | {"17": 0.024195599301651945, "29": 0.009314290690558046, "43": -0.20964568910799095} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | ab | uci_internal_fixed | ece15_change | 3 | 0.00192471 | 0.0777848 | {"17": 0.03933688392256045, "29": 0.0539343619786498, "43": -0.08749710483920495} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | ba | uci_internal_fixed | accuracy_change | 3 | 0.047526 | 0.0892171 | {"17": -0.0087890625, "29": 0.0009765625, "43": 0.150390625} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | ba | uci_internal_fixed | error_change | 3 | -0.047526 | 0.0892171 | {"17": 0.0087890625, "29": -0.0009765625, "43": -0.150390625} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | ba | uci_internal_fixed | nll_change | 3 | -0.0377331 | 0.276423 | {"17": 0.11011851766535391, "29": 0.13332002148119498, "43": -0.3566379789094929} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | ba | uci_internal_fixed | brier_change | 3 | -0.0587119 | 0.130924 | {"17": 0.024195599301651945, "29": 0.009314290690558046, "43": -0.20964568910799095} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | ba | uci_internal_fixed | ece15_change | 3 | 0.00192471 | 0.0777848 | {"17": 0.03933688392256045, "29": 0.0539343619786498, "43": -0.08749710483920495} |


## norm_reference

| method | intervention | washout_batches | direction | metric | n_panels | mean | sd | ci95_low | ci95_high | n_seeds_min | n_seeds_max | individual_panels |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SAR (complete-state implementation) | Reset all declared state | 0 | ab | accuracy_change | 1 | 0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0003255208333333333} |
| SAR (complete-state implementation) | Reset all declared state | 0 | ab | error_change | 1 | -0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0003255208333333333} |
| SAR (complete-state implementation) | Reset all declared state | 0 | ab | nll_change | 1 | -0.000101398 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.00010139795322581617} |
| SAR (complete-state implementation) | Reset all declared state | 0 | ab | brier_change | 1 | -9.23035e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": -9.230346184478193e-05} |
| SAR (complete-state implementation) | Reset all declared state | 0 | ab | ece15_change | 1 | -0.000265989 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0002659886280750011} |
| SAR (complete-state implementation) | Reset all declared state | 0 | ba | accuracy_change | 1 | 0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0003255208333333333} |
| SAR (complete-state implementation) | Reset all declared state | 0 | ba | error_change | 1 | -0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0003255208333333333} |
| SAR (complete-state implementation) | Reset all declared state | 0 | ba | nll_change | 1 | -0.000101398 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.00010139795322581617} |
| SAR (complete-state implementation) | Reset all declared state | 0 | ba | brier_change | 1 | -9.23035e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": -9.230346184478193e-05} |
| SAR (complete-state implementation) | Reset all declared state | 0 | ba | ece15_change | 1 | -0.000265989 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0002659886280750011} |
| SAR (complete-state implementation) | Reset all declared state | 4 | ab | accuracy_change | 1 | 0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0003255208333333333} |
| SAR (complete-state implementation) | Reset all declared state | 4 | ab | error_change | 1 | -0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0003255208333333333} |
| SAR (complete-state implementation) | Reset all declared state | 4 | ab | nll_change | 1 | -0.000101398 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.00010139795322581617} |
| SAR (complete-state implementation) | Reset all declared state | 4 | ab | brier_change | 1 | -9.23035e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": -9.230346184478193e-05} |
| SAR (complete-state implementation) | Reset all declared state | 4 | ab | ece15_change | 1 | -0.000265989 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0002659886280750011} |
| SAR (complete-state implementation) | Reset all declared state | 4 | ba | accuracy_change | 1 | 0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0003255208333333333} |
| SAR (complete-state implementation) | Reset all declared state | 4 | ba | error_change | 1 | -0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0003255208333333333} |
| SAR (complete-state implementation) | Reset all declared state | 4 | ba | nll_change | 1 | -0.000101398 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.00010139795322581617} |
| SAR (complete-state implementation) | Reset all declared state | 4 | ba | brier_change | 1 | -9.23035e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": -9.230346184478193e-05} |
| SAR (complete-state implementation) | Reset all declared state | 4 | ba | ece15_change | 1 | -0.000265989 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0002659886280750011} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | ab | accuracy_change | 1 | 0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0003255208333333333} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | ab | error_change | 1 | -0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0003255208333333333} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | ab | nll_change | 1 | -0.000102425 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.00010242466319126721} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | ab | brier_change | 1 | -9.25464e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": -9.254638611189772e-05} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | ab | ece15_change | 1 | -0.00026505 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0002650496997289679} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | ba | accuracy_change | 1 | 0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0003255208333333333} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | ba | error_change | 1 | -0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0003255208333333333} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | ba | nll_change | 1 | -0.000101646 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.00010164639769429916} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | ba | brier_change | 1 | -9.24091e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": -9.240913059098121e-05} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | ba | ece15_change | 1 | -0.000265803 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0002658026467279844} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | ab | accuracy_change | 1 | 0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0003255208333333333} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | ab | error_change | 1 | -0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0003255208333333333} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | ab | nll_change | 1 | -0.000101398 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.00010139795322581617} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | ab | brier_change | 1 | -9.23035e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": -9.230346184478193e-05} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | ab | ece15_change | 1 | -0.000265989 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0002659886280750011} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | ba | accuracy_change | 1 | 0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0003255208333333333} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | ba | error_change | 1 | -0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0003255208333333333} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | ba | nll_change | 1 | -0.000101398 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.00010139795322581617} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | ba | brier_change | 1 | -9.23035e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": -9.230346184478193e-05} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | ba | ece15_change | 1 | -0.000265989 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0002659886280750011} |
| SAR (complete-state implementation) | No external reset | 0 | ab | accuracy_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | No external reset | 0 | ab | error_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | No external reset | 0 | ab | nll_change | 1 | 9.27901e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": 9.279014744549216e-05} |
| SAR (complete-state implementation) | No external reset | 0 | ab | brier_change | 1 | 1.40094e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": 1.4009368677202205e-05} |
| SAR (complete-state implementation) | No external reset | 0 | ab | ece15_change | 1 | 5.30878e-06 | — | — | — | 3 | 3 | {"uci_internal_fixed": 5.3087754988973236e-06} |
| SAR (complete-state implementation) | No external reset | 0 | ba | accuracy_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | No external reset | 0 | ba | error_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | No external reset | 0 | ba | nll_change | 1 | 4.23087e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": 4.23087146772932e-05} |
| SAR (complete-state implementation) | No external reset | 0 | ba | brier_change | 1 | 8.59524e-07 | — | — | — | 3 | 3 | {"uci_internal_fixed": 8.595243504907341e-07} |
| SAR (complete-state implementation) | No external reset | 0 | ba | ece15_change | 1 | 5.44414e-06 | — | — | — | 3 | 3 | {"uci_internal_fixed": 5.4441425142605126e-06} |
| SAR (complete-state implementation) | No external reset | 4 | ab | accuracy_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | No external reset | 4 | ab | error_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | No external reset | 4 | ab | nll_change | 1 | 0.000312251 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.00031225101340755695} |
| SAR (complete-state implementation) | No external reset | 4 | ab | brier_change | 1 | 4.14866e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": 4.148656431204878e-05} |
| SAR (complete-state implementation) | No external reset | 4 | ab | ece15_change | 1 | 3.92032e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": 3.920323474797954e-05} |
| SAR (complete-state implementation) | No external reset | 4 | ba | accuracy_change | 1 | 0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0003255208333333333} |
| SAR (complete-state implementation) | No external reset | 4 | ba | error_change | 1 | -0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0003255208333333333} |
| SAR (complete-state implementation) | No external reset | 4 | ba | nll_change | 1 | 0.000341458 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.000341457731183011} |
| SAR (complete-state implementation) | No external reset | 4 | ba | brier_change | 1 | 4.64343e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": 4.64342867254793e-05} |
| SAR (complete-state implementation) | No external reset | 4 | ba | ece15_change | 1 | -0.000284308 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.00028430753134930237} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | ab | accuracy_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | ab | error_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | ab | nll_change | 1 | 9.27931e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": 9.279306783217464e-05} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | ab | brier_change | 1 | 1.40094e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": 1.400937457123573e-05} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | ab | ece15_change | 1 | 5.30586e-06 | — | — | — | 3 | 3 | {"uci_internal_fixed": 5.305859285413955e-06} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | ba | accuracy_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | ba | error_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | ba | nll_change | 1 | 4.233e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": 4.2329981517859557e-05} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | ba | brier_change | 1 | 8.70565e-07 | — | — | — | 3 | 3 | {"uci_internal_fixed": 8.70564795990685e-07} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | ba | ece15_change | 1 | 5.43258e-06 | — | — | — | 3 | 3 | {"uci_internal_fixed": 5.43258101734385e-06} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | ab | accuracy_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | ab | error_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | ab | nll_change | 1 | 0.000312251 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.00031225101340755695} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | ab | brier_change | 1 | 4.14866e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": 4.148656431204878e-05} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | ab | ece15_change | 1 | 3.92032e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": 3.920323474797954e-05} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | ba | accuracy_change | 1 | 0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0003255208333333333} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | ba | error_change | 1 | -0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0003255208333333333} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | ba | nll_change | 1 | 0.000341458 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.000341457731183011} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | ba | brier_change | 1 | 4.64343e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": 4.64342867254793e-05} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | ba | ece15_change | 1 | -0.000284308 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.00028430753134930237} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | ab | accuracy_change | 1 | 0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0003255208333333333} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | ab | error_change | 1 | -0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0003255208333333333} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | ab | nll_change | 1 | -0.000102425 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.00010242466319126721} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | ab | brier_change | 1 | -9.25464e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": -9.254638611189772e-05} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | ab | ece15_change | 1 | -0.00026505 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0002650496997289679} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | ba | accuracy_change | 1 | 0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0003255208333333333} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | ba | error_change | 1 | -0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0003255208333333333} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | ba | nll_change | 1 | -0.000101646 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.00010164639769429916} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | ba | brier_change | 1 | -9.24091e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": -9.240913059098121e-05} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | ba | ece15_change | 1 | -0.000265803 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0002658026467279844} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | ab | accuracy_change | 1 | 0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0003255208333333333} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | ab | error_change | 1 | -0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0003255208333333333} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | ab | nll_change | 1 | -0.000101398 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.00010139795322581617} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | ab | brier_change | 1 | -9.23035e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": -9.230346184478193e-05} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | ab | ece15_change | 1 | -0.000265989 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0002659886280750011} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | ba | accuracy_change | 1 | 0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0003255208333333333} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | ba | error_change | 1 | -0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0003255208333333333} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | ba | nll_change | 1 | -0.000101398 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.00010139795322581617} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | ba | brier_change | 1 | -9.23035e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": -9.230346184478193e-05} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | ba | ece15_change | 1 | -0.000265989 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0002659886280750011} |
| SAR (complete-state implementation) | Reset parameters only | 0 | ab | accuracy_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset parameters only | 0 | ab | error_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset parameters only | 0 | ab | nll_change | 1 | 9.38522e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": 9.38521647443925e-05} |
| SAR (complete-state implementation) | Reset parameters only | 0 | ab | brier_change | 1 | 1.42521e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": 1.4252112253601568e-05} |
| SAR (complete-state implementation) | Reset parameters only | 0 | ab | ece15_change | 1 | 4.33445e-06 | — | — | — | 3 | 3 | {"uci_internal_fixed": 4.33444869499718e-06} |
| SAR (complete-state implementation) | Reset parameters only | 0 | ba | accuracy_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset parameters only | 0 | ba | error_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset parameters only | 0 | ba | nll_change | 1 | 4.27832e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": 4.278316281069311e-05} |
| SAR (complete-state implementation) | Reset parameters only | 0 | ba | brier_change | 1 | 1.06385e-06 | — | — | — | 3 | 3 | {"uci_internal_fixed": 1.063851787390264e-06} |
| SAR (complete-state implementation) | Reset parameters only | 0 | ba | ece15_change | 1 | 5.08497e-06 | — | — | — | 3 | 3 | {"uci_internal_fixed": 5.0849733016939775e-06} |
| SAR (complete-state implementation) | Reset parameters only | 4 | ab | accuracy_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset parameters only | 4 | ab | error_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset parameters only | 4 | ab | nll_change | 1 | 0.000312251 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.00031225101340755695} |
| SAR (complete-state implementation) | Reset parameters only | 4 | ab | brier_change | 1 | 4.14866e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": 4.148656431204878e-05} |
| SAR (complete-state implementation) | Reset parameters only | 4 | ab | ece15_change | 1 | 3.92032e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": 3.920323474797954e-05} |
| SAR (complete-state implementation) | Reset parameters only | 4 | ba | accuracy_change | 1 | 0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0003255208333333333} |
| SAR (complete-state implementation) | Reset parameters only | 4 | ba | error_change | 1 | -0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0003255208333333333} |
| SAR (complete-state implementation) | Reset parameters only | 4 | ba | nll_change | 1 | 0.000341458 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.000341457731183011} |
| SAR (complete-state implementation) | Reset parameters only | 4 | ba | brier_change | 1 | 4.64343e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": 4.64342867254793e-05} |
| SAR (complete-state implementation) | Reset parameters only | 4 | ba | ece15_change | 1 | -0.000284308 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.00028430753134930237} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | ab | accuracy_change | 1 | 0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0003255208333333333} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | ab | error_change | 1 | -0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0003255208333333333} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | ab | nll_change | 1 | -0.000101398 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.00010139795322581617} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | ab | brier_change | 1 | -9.23035e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": -9.230346184478193e-05} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | ab | ece15_change | 1 | -0.000265989 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0002659886280750011} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | ba | accuracy_change | 1 | 0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0003255208333333333} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | ba | error_change | 1 | -0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0003255208333333333} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | ba | nll_change | 1 | -0.000101398 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.00010139795322581617} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | ba | brier_change | 1 | -9.23035e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": -9.230346184478193e-05} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | ba | ece15_change | 1 | -0.000265989 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0002659886280750011} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | ab | accuracy_change | 1 | 0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0003255208333333333} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | ab | error_change | 1 | -0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0003255208333333333} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | ab | nll_change | 1 | -0.000101398 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.00010139795322581617} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | ab | brier_change | 1 | -9.23035e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": -9.230346184478193e-05} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | ab | ece15_change | 1 | -0.000265989 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0002659886280750011} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | ba | accuracy_change | 1 | 0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0003255208333333333} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | ba | error_change | 1 | -0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0003255208333333333} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | ba | nll_change | 1 | -0.000101398 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.00010139795322581617} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | ba | brier_change | 1 | -9.23035e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": -9.230346184478193e-05} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | ba | ece15_change | 1 | -0.000265989 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0002659886280750011} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | ab | accuracy_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | ab | error_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | ab | nll_change | 1 | 9.38553e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": 9.38553325074432e-05} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | ab | brier_change | 1 | 1.42521e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": 1.4252124720035125e-05} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | ab | ece15_change | 1 | 4.33129e-06 | — | — | — | 3 | 3 | {"uci_internal_fixed": 4.331287208247127e-06} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | ba | accuracy_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | ba | error_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | ba | nll_change | 1 | 4.28061e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": 4.280610327870906e-05} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | ba | brier_change | 1 | 1.07574e-06 | — | — | — | 3 | 3 | {"uci_internal_fixed": 1.0757448359235283e-06} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | ba | ece15_change | 1 | 5.07214e-06 | — | — | — | 3 | 3 | {"uci_internal_fixed": 5.072135803393767e-06} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | ab | accuracy_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | ab | error_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | ab | nll_change | 1 | 0.000312251 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.00031225101340755695} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | ab | brier_change | 1 | 4.14866e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": 4.148656431204878e-05} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | ab | ece15_change | 1 | 3.92032e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": 3.920323474797954e-05} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | ba | accuracy_change | 1 | 0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0003255208333333333} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | ba | error_change | 1 | -0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0003255208333333333} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | ba | nll_change | 1 | 0.000341458 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.000341457731183011} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | ba | brier_change | 1 | 4.64343e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": 4.64342867254793e-05} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | ba | ece15_change | 1 | -0.000284308 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.00028430753134930237} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | ab | accuracy_change | 1 | 0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0003255208333333333} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | ab | error_change | 1 | -0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0003255208333333333} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | ab | nll_change | 1 | -0.000101398 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.00010139795322581617} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | ab | brier_change | 1 | -9.23035e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": -9.230346184478193e-05} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | ab | ece15_change | 1 | -0.000265989 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0002659886280750011} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | ba | accuracy_change | 1 | 0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0003255208333333333} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | ba | error_change | 1 | -0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0003255208333333333} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | ba | nll_change | 1 | -0.000101398 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.00010139795322581617} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | ba | brier_change | 1 | -9.23035e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": -9.230346184478193e-05} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | ba | ece15_change | 1 | -0.000265989 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0002659886280750011} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | ab | accuracy_change | 1 | 0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0003255208333333333} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | ab | error_change | 1 | -0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0003255208333333333} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | ab | nll_change | 1 | -0.000101398 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.00010139795322581617} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | ab | brier_change | 1 | -9.23035e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": -9.230346184478193e-05} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | ab | ece15_change | 1 | -0.000265989 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0002659886280750011} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | ba | accuracy_change | 1 | 0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0003255208333333333} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | ba | error_change | 1 | -0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0003255208333333333} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | ba | nll_change | 1 | -0.000101398 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.00010139795322581617} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | ba | brier_change | 1 | -9.23035e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": -9.230346184478193e-05} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | ba | ece15_change | 1 | -0.000265989 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0002659886280750011} |
| Source | Reset all declared state | 0 | ab | accuracy_change | 1 | -0.0472005 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.047200520833333336} |
| Source | Reset all declared state | 0 | ab | error_change | 1 | 0.0472005 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.047200520833333336} |
| Source | Reset all declared state | 0 | ab | nll_change | 1 | 0.0380853 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.03808533279304773} |
| Source | Reset all declared state | 0 | ab | brier_change | 1 | 0.0587236 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.058723550560806866} |
| Source | Reset all declared state | 0 | ab | ece15_change | 1 | -0.00217309 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.002173093594947074} |
| Source | Reset all declared state | 0 | ba | accuracy_change | 1 | -0.0472005 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.047200520833333336} |
| Source | Reset all declared state | 0 | ba | error_change | 1 | 0.0472005 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.047200520833333336} |
| Source | Reset all declared state | 0 | ba | nll_change | 1 | 0.0380853 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.03808533279304773} |
| Source | Reset all declared state | 0 | ba | brier_change | 1 | 0.0587236 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.058723550560806866} |
| Source | Reset all declared state | 0 | ba | ece15_change | 1 | -0.00217309 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.002173093594947074} |
| Source | Reset all declared state | 4 | ab | accuracy_change | 1 | -0.0472005 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.047200520833333336} |
| Source | Reset all declared state | 4 | ab | error_change | 1 | 0.0472005 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.047200520833333336} |
| Source | Reset all declared state | 4 | ab | nll_change | 1 | 0.0380853 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.03808533279304773} |
| Source | Reset all declared state | 4 | ab | brier_change | 1 | 0.0587236 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.058723550560806866} |
| Source | Reset all declared state | 4 | ab | ece15_change | 1 | -0.00217309 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.002173093594947074} |
| Source | Reset all declared state | 4 | ba | accuracy_change | 1 | -0.0472005 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.047200520833333336} |
| Source | Reset all declared state | 4 | ba | error_change | 1 | 0.0472005 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.047200520833333336} |
| Source | Reset all declared state | 4 | ba | nll_change | 1 | 0.0380853 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.03808533279304773} |
| Source | Reset all declared state | 4 | ba | brier_change | 1 | 0.0587236 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.058723550560806866} |
| Source | Reset all declared state | 4 | ba | ece15_change | 1 | -0.00217309 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.002173093594947074} |
| Source | No external reset | 0 | ab | accuracy_change | 1 | -0.0472005 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.047200520833333336} |
| Source | No external reset | 0 | ab | error_change | 1 | 0.0472005 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.047200520833333336} |
| Source | No external reset | 0 | ab | nll_change | 1 | 0.0380853 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.03808533279304773} |
| Source | No external reset | 0 | ab | brier_change | 1 | 0.0587236 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.058723550560806866} |
| Source | No external reset | 0 | ab | ece15_change | 1 | -0.00217309 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.002173093594947074} |
| Source | No external reset | 0 | ba | accuracy_change | 1 | -0.0472005 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.047200520833333336} |
| Source | No external reset | 0 | ba | error_change | 1 | 0.0472005 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.047200520833333336} |
| Source | No external reset | 0 | ba | nll_change | 1 | 0.0380853 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.03808533279304773} |
| Source | No external reset | 0 | ba | brier_change | 1 | 0.0587236 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.058723550560806866} |
| Source | No external reset | 0 | ba | ece15_change | 1 | -0.00217309 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.002173093594947074} |
| Source | No external reset | 4 | ab | accuracy_change | 1 | -0.0472005 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.047200520833333336} |
| Source | No external reset | 4 | ab | error_change | 1 | 0.0472005 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.047200520833333336} |
| Source | No external reset | 4 | ab | nll_change | 1 | 0.0380853 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.03808533279304773} |
| Source | No external reset | 4 | ab | brier_change | 1 | 0.0587236 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.058723550560806866} |
| Source | No external reset | 4 | ab | ece15_change | 1 | -0.00217309 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.002173093594947074} |
| Source | No external reset | 4 | ba | accuracy_change | 1 | -0.0472005 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.047200520833333336} |
| Source | No external reset | 4 | ba | error_change | 1 | 0.0472005 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.047200520833333336} |
| Source | No external reset | 4 | ba | nll_change | 1 | 0.0380853 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.03808533279304773} |
| Source | No external reset | 4 | ba | brier_change | 1 | 0.0587236 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.058723550560806866} |
| Source | No external reset | 4 | ba | ece15_change | 1 | -0.00217309 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.002173093594947074} |
| Tent | Reset all declared state | 0 | ab | accuracy_change | 1 | 0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0003255208333333333} |
| Tent | Reset all declared state | 0 | ab | error_change | 1 | -0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0003255208333333333} |
| Tent | Reset all declared state | 0 | ab | nll_change | 1 | 0.000352186 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0003521862053997224} |
| Tent | Reset all declared state | 0 | ab | brier_change | 1 | 1.16175e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": 1.1617522213218495e-05} |
| Tent | Reset all declared state | 0 | ab | ece15_change | 1 | -0.00024838 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.00024837990761197105} |
| Tent | Reset all declared state | 0 | ba | accuracy_change | 1 | 0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0003255208333333333} |
| Tent | Reset all declared state | 0 | ba | error_change | 1 | -0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0003255208333333333} |
| Tent | Reset all declared state | 0 | ba | nll_change | 1 | 0.000352186 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0003521862053997224} |
| Tent | Reset all declared state | 0 | ba | brier_change | 1 | 1.16175e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": 1.1617522213218495e-05} |
| Tent | Reset all declared state | 0 | ba | ece15_change | 1 | -0.00024838 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.00024837990761197105} |
| Tent | Reset all declared state | 4 | ab | accuracy_change | 1 | 0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0003255208333333333} |
| Tent | Reset all declared state | 4 | ab | error_change | 1 | -0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0003255208333333333} |
| Tent | Reset all declared state | 4 | ab | nll_change | 1 | 0.000352186 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0003521862053997224} |
| Tent | Reset all declared state | 4 | ab | brier_change | 1 | 1.16175e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": 1.1617522213218495e-05} |
| Tent | Reset all declared state | 4 | ab | ece15_change | 1 | -0.00024838 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.00024837990761197105} |
| Tent | Reset all declared state | 4 | ba | accuracy_change | 1 | 0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0003255208333333333} |
| Tent | Reset all declared state | 4 | ba | error_change | 1 | -0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0003255208333333333} |
| Tent | Reset all declared state | 4 | ba | nll_change | 1 | 0.000352186 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0003521862053997224} |
| Tent | Reset all declared state | 4 | ba | brier_change | 1 | 1.16175e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": 1.1617522213218495e-05} |
| Tent | Reset all declared state | 4 | ba | ece15_change | 1 | -0.00024838 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.00024837990761197105} |
| Tent | Reset auxiliary state only | 0 | ab | accuracy_change | 1 | 0.000651042 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0006510416666666666} |
| Tent | Reset auxiliary state only | 0 | ab | error_change | 1 | -0.000651042 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0006510416666666666} |
| Tent | Reset auxiliary state only | 0 | ab | nll_change | 1 | 0.00013717 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.00013717024331701133} |
| Tent | Reset auxiliary state only | 0 | ab | brier_change | 1 | -6.22554e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": -6.225536736462085e-05} |
| Tent | Reset auxiliary state only | 0 | ab | ece15_change | 1 | 9.83519e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": 9.835188420539813e-05} |
| Tent | Reset auxiliary state only | 0 | ba | accuracy_change | 1 | 0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0003255208333333333} |
| Tent | Reset auxiliary state only | 0 | ba | error_change | 1 | -0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0003255208333333333} |
| Tent | Reset auxiliary state only | 0 | ba | nll_change | 1 | 0.000111009 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.00011100918924340324} |
| Tent | Reset auxiliary state only | 0 | ba | brier_change | 1 | -6.44908e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": -6.449078273662531e-05} |
| Tent | Reset auxiliary state only | 0 | ba | ece15_change | 1 | 0.00024961 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0002496096372160139} |
| Tent | Reset auxiliary state only | 4 | ab | accuracy_change | 1 | 0.000976562 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0009765625} |
| Tent | Reset auxiliary state only | 4 | ab | error_change | 1 | -0.000976562 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0009765625} |
| Tent | Reset auxiliary state only | 4 | ab | nll_change | 1 | 0.000621673 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0006216730480918543} |
| Tent | Reset auxiliary state only | 4 | ab | brier_change | 1 | -7.77439e-06 | — | — | — | 3 | 3 | {"uci_internal_fixed": -7.774386852545112e-06} |
| Tent | Reset auxiliary state only | 4 | ab | ece15_change | 1 | -5.15454e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": -5.154543665903509e-05} |
| Tent | Reset auxiliary state only | 4 | ba | accuracy_change | 1 | 0.000976562 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0009765625} |
| Tent | Reset auxiliary state only | 4 | ba | error_change | 1 | -0.000976562 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0009765625} |
| Tent | Reset auxiliary state only | 4 | ba | nll_change | 1 | 0.000604387 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0006043870815287053} |
| Tent | Reset auxiliary state only | 4 | ba | brier_change | 1 | -9.36237e-06 | — | — | — | 3 | 3 | {"uci_internal_fixed": -9.362367653929319e-06} |
| Tent | Reset auxiliary state only | 4 | ba | ece15_change | 1 | -5.99564e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": -5.9956400895433935e-05} |
| Tent | No external reset | 0 | ab | accuracy_change | 1 | 0.000651042 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0006510416666666666} |
| Tent | No external reset | 0 | ab | error_change | 1 | -0.000651042 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0006510416666666666} |
| Tent | No external reset | 0 | ab | nll_change | 1 | 0.00013717 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.00013717024331701133} |
| Tent | No external reset | 0 | ab | brier_change | 1 | -6.22554e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": -6.225536736462085e-05} |
| Tent | No external reset | 0 | ab | ece15_change | 1 | 9.83519e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": 9.835188420539813e-05} |
| Tent | No external reset | 0 | ba | accuracy_change | 1 | 0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0003255208333333333} |
| Tent | No external reset | 0 | ba | error_change | 1 | -0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0003255208333333333} |
| Tent | No external reset | 0 | ba | nll_change | 1 | 0.000111009 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.00011100918924340324} |
| Tent | No external reset | 0 | ba | brier_change | 1 | -6.44908e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": -6.449078273662531e-05} |
| Tent | No external reset | 0 | ba | ece15_change | 1 | 0.00024961 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0002496096372160139} |
| Tent | No external reset | 4 | ab | accuracy_change | 1 | 0.000976562 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0009765625} |
| Tent | No external reset | 4 | ab | error_change | 1 | -0.000976562 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0009765625} |
| Tent | No external reset | 4 | ab | nll_change | 1 | 0.000621673 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0006216730480918543} |
| Tent | No external reset | 4 | ab | brier_change | 1 | -7.77439e-06 | — | — | — | 3 | 3 | {"uci_internal_fixed": -7.774386852545112e-06} |
| Tent | No external reset | 4 | ab | ece15_change | 1 | -5.15454e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": -5.154543665903509e-05} |
| Tent | No external reset | 4 | ba | accuracy_change | 1 | 0.000976562 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0009765625} |
| Tent | No external reset | 4 | ba | error_change | 1 | -0.000976562 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0009765625} |
| Tent | No external reset | 4 | ba | nll_change | 1 | 0.000604387 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0006043870815287053} |
| Tent | No external reset | 4 | ba | brier_change | 1 | -9.36237e-06 | — | — | — | 3 | 3 | {"uci_internal_fixed": -9.362367653929319e-06} |
| Tent | No external reset | 4 | ba | ece15_change | 1 | -5.99564e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": -5.9956400895433935e-05} |
| Tent | Reset optimizer only | 0 | ab | accuracy_change | 1 | 0.000651042 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0006510416666666666} |
| Tent | Reset optimizer only | 0 | ab | error_change | 1 | -0.000651042 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0006510416666666666} |
| Tent | Reset optimizer only | 0 | ab | nll_change | 1 | 0.000227218 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.00022721807077238573} |
| Tent | Reset optimizer only | 0 | ab | brier_change | 1 | -4.21894e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": -4.218944416596477e-05} |
| Tent | Reset optimizer only | 0 | ab | ece15_change | 1 | -0.000131091 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.00013109105888930097} |
| Tent | Reset optimizer only | 0 | ba | accuracy_change | 1 | 0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0003255208333333333} |
| Tent | Reset optimizer only | 0 | ba | error_change | 1 | -0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0003255208333333333} |
| Tent | Reset optimizer only | 0 | ba | nll_change | 1 | 0.000164364 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.00016436421791938988} |
| Tent | Reset optimizer only | 0 | ba | brier_change | 1 | -4.67816e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": -4.678157383287742e-05} |
| Tent | Reset optimizer only | 0 | ba | ece15_change | 1 | 8.66385e-06 | — | — | — | 3 | 3 | {"uci_internal_fixed": 8.663851494277475e-06} |
| Tent | Reset optimizer only | 4 | ab | accuracy_change | 1 | 0.000976562 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0009765625} |
| Tent | Reset optimizer only | 4 | ab | error_change | 1 | -0.000976562 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0009765625} |
| Tent | Reset optimizer only | 4 | ab | nll_change | 1 | 0.000262555 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.00026255538109768925} |
| Tent | Reset optimizer only | 4 | ab | brier_change | 1 | -5.42994e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": -5.4299381094083506e-05} |
| Tent | Reset optimizer only | 4 | ab | ece15_change | 1 | -0.000262059 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0002620587050045029} |
| Tent | Reset optimizer only | 4 | ba | accuracy_change | 1 | 0.000976562 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0009765625} |
| Tent | Reset optimizer only | 4 | ba | error_change | 1 | -0.000976562 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0009765625} |
| Tent | Reset optimizer only | 4 | ba | nll_change | 1 | 0.000220808 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.00022080844728520366} |
| Tent | Reset optimizer only | 4 | ba | brier_change | 1 | -5.76002e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": -5.760018671516383e-05} |
| Tent | Reset optimizer only | 4 | ba | ece15_change | 1 | -5.8261e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": -5.826097857532126e-05} |
| Tent | Reset optimizer + auxiliary state | 0 | ab | accuracy_change | 1 | 0.000651042 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0006510416666666666} |
| Tent | Reset optimizer + auxiliary state | 0 | ab | error_change | 1 | -0.000651042 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0006510416666666666} |
| Tent | Reset optimizer + auxiliary state | 0 | ab | nll_change | 1 | 0.000227218 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.00022721807077238573} |
| Tent | Reset optimizer + auxiliary state | 0 | ab | brier_change | 1 | -4.21894e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": -4.218944416596477e-05} |
| Tent | Reset optimizer + auxiliary state | 0 | ab | ece15_change | 1 | -0.000131091 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.00013109105888930097} |
| Tent | Reset optimizer + auxiliary state | 0 | ba | accuracy_change | 1 | 0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0003255208333333333} |
| Tent | Reset optimizer + auxiliary state | 0 | ba | error_change | 1 | -0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0003255208333333333} |
| Tent | Reset optimizer + auxiliary state | 0 | ba | nll_change | 1 | 0.000164364 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.00016436421791938988} |
| Tent | Reset optimizer + auxiliary state | 0 | ba | brier_change | 1 | -4.67816e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": -4.678157383287742e-05} |
| Tent | Reset optimizer + auxiliary state | 0 | ba | ece15_change | 1 | 8.66385e-06 | — | — | — | 3 | 3 | {"uci_internal_fixed": 8.663851494277475e-06} |
| Tent | Reset optimizer + auxiliary state | 4 | ab | accuracy_change | 1 | 0.000976562 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0009765625} |
| Tent | Reset optimizer + auxiliary state | 4 | ab | error_change | 1 | -0.000976562 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0009765625} |
| Tent | Reset optimizer + auxiliary state | 4 | ab | nll_change | 1 | 0.000262555 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.00026255538109768925} |
| Tent | Reset optimizer + auxiliary state | 4 | ab | brier_change | 1 | -5.42994e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": -5.4299381094083506e-05} |
| Tent | Reset optimizer + auxiliary state | 4 | ab | ece15_change | 1 | -0.000262059 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0002620587050045029} |
| Tent | Reset optimizer + auxiliary state | 4 | ba | accuracy_change | 1 | 0.000976562 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0009765625} |
| Tent | Reset optimizer + auxiliary state | 4 | ba | error_change | 1 | -0.000976562 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0009765625} |
| Tent | Reset optimizer + auxiliary state | 4 | ba | nll_change | 1 | 0.000220808 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.00022080844728520366} |
| Tent | Reset optimizer + auxiliary state | 4 | ba | brier_change | 1 | -5.76002e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": -5.760018671516383e-05} |
| Tent | Reset optimizer + auxiliary state | 4 | ba | ece15_change | 1 | -5.8261e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": -5.826097857532126e-05} |
| Tent | Reset parameters only | 0 | ab | accuracy_change | 1 | 0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0003255208333333333} |
| Tent | Reset parameters only | 0 | ab | error_change | 1 | -0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0003255208333333333} |
| Tent | Reset parameters only | 0 | ab | nll_change | 1 | 0.000261411 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.00026141070831011207} |
| Tent | Reset parameters only | 0 | ab | brier_change | 1 | -8.90223e-06 | — | — | — | 3 | 3 | {"uci_internal_fixed": -8.902229398634795e-06} |
| Tent | Reset parameters only | 0 | ab | ece15_change | 1 | -0.000235601 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.00023560119206845424} |
| Tent | Reset parameters only | 0 | ba | accuracy_change | 1 | 0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0003255208333333333} |
| Tent | Reset parameters only | 0 | ba | error_change | 1 | -0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0003255208333333333} |
| Tent | Reset parameters only | 0 | ba | nll_change | 1 | 0.000298026 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.00029802557509545313} |
| Tent | Reset parameters only | 0 | ba | brier_change | 1 | -6.55665e-06 | — | — | — | 3 | 3 | {"uci_internal_fixed": -6.556647479326096e-06} |
| Tent | Reset parameters only | 0 | ba | ece15_change | 1 | -0.000224567 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0002245673894995011} |
| Tent | Reset parameters only | 4 | ab | accuracy_change | 1 | 0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0003255208333333333} |
| Tent | Reset parameters only | 4 | ab | error_change | 1 | -0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0003255208333333333} |
| Tent | Reset parameters only | 4 | ab | nll_change | 1 | 0.000708485 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0007084847513759625} |
| Tent | Reset parameters only | 4 | ab | brier_change | 1 | 5.70428e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": 5.704282661454091e-05} |
| Tent | Reset parameters only | 4 | ab | ece15_change | 1 | -0.000194572 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.00019457189501042067} |
| Tent | Reset parameters only | 4 | ba | accuracy_change | 1 | 0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0003255208333333333} |
| Tent | Reset parameters only | 4 | ba | error_change | 1 | -0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0003255208333333333} |
| Tent | Reset parameters only | 4 | ba | nll_change | 1 | 0.000732189 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0007321893151596403} |
| Tent | Reset parameters only | 4 | ba | brier_change | 1 | 5.84231e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": 5.842310565286104e-05} |
| Tent | Reset parameters only | 4 | ba | ece15_change | 1 | -0.000360931 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.00036093079563319076} |
| Tent | Reset parameters + auxiliary state | 0 | ab | accuracy_change | 1 | 0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0003255208333333333} |
| Tent | Reset parameters + auxiliary state | 0 | ab | error_change | 1 | -0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0003255208333333333} |
| Tent | Reset parameters + auxiliary state | 0 | ab | nll_change | 1 | 0.000261411 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.00026141070831011207} |
| Tent | Reset parameters + auxiliary state | 0 | ab | brier_change | 1 | -8.90223e-06 | — | — | — | 3 | 3 | {"uci_internal_fixed": -8.902229398634795e-06} |
| Tent | Reset parameters + auxiliary state | 0 | ab | ece15_change | 1 | -0.000235601 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.00023560119206845424} |
| Tent | Reset parameters + auxiliary state | 0 | ba | accuracy_change | 1 | 0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0003255208333333333} |
| Tent | Reset parameters + auxiliary state | 0 | ba | error_change | 1 | -0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0003255208333333333} |
| Tent | Reset parameters + auxiliary state | 0 | ba | nll_change | 1 | 0.000298026 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.00029802557509545313} |
| Tent | Reset parameters + auxiliary state | 0 | ba | brier_change | 1 | -6.55665e-06 | — | — | — | 3 | 3 | {"uci_internal_fixed": -6.556647479326096e-06} |
| Tent | Reset parameters + auxiliary state | 0 | ba | ece15_change | 1 | -0.000224567 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0002245673894995011} |
| Tent | Reset parameters + auxiliary state | 4 | ab | accuracy_change | 1 | 0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0003255208333333333} |
| Tent | Reset parameters + auxiliary state | 4 | ab | error_change | 1 | -0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0003255208333333333} |
| Tent | Reset parameters + auxiliary state | 4 | ab | nll_change | 1 | 0.000708485 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0007084847513759625} |
| Tent | Reset parameters + auxiliary state | 4 | ab | brier_change | 1 | 5.70428e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": 5.704282661454091e-05} |
| Tent | Reset parameters + auxiliary state | 4 | ab | ece15_change | 1 | -0.000194572 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.00019457189501042067} |
| Tent | Reset parameters + auxiliary state | 4 | ba | accuracy_change | 1 | 0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0003255208333333333} |
| Tent | Reset parameters + auxiliary state | 4 | ba | error_change | 1 | -0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0003255208333333333} |
| Tent | Reset parameters + auxiliary state | 4 | ba | nll_change | 1 | 0.000732189 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0007321893151596403} |
| Tent | Reset parameters + auxiliary state | 4 | ba | brier_change | 1 | 5.84231e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": 5.842310565286104e-05} |
| Tent | Reset parameters + auxiliary state | 4 | ba | ece15_change | 1 | -0.000360931 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.00036093079563319076} |
| Tent | Reset parameters + optimizer | 0 | ab | accuracy_change | 1 | 0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0003255208333333333} |
| Tent | Reset parameters + optimizer | 0 | ab | error_change | 1 | -0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0003255208333333333} |
| Tent | Reset parameters + optimizer | 0 | ab | nll_change | 1 | 0.000352186 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0003521862053997224} |
| Tent | Reset parameters + optimizer | 0 | ab | brier_change | 1 | 1.16175e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": 1.1617522213218495e-05} |
| Tent | Reset parameters + optimizer | 0 | ab | ece15_change | 1 | -0.00024838 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.00024837990761197105} |
| Tent | Reset parameters + optimizer | 0 | ba | accuracy_change | 1 | 0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0003255208333333333} |
| Tent | Reset parameters + optimizer | 0 | ba | error_change | 1 | -0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0003255208333333333} |
| Tent | Reset parameters + optimizer | 0 | ba | nll_change | 1 | 0.000352186 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0003521862053997224} |
| Tent | Reset parameters + optimizer | 0 | ba | brier_change | 1 | 1.16175e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": 1.1617522213218495e-05} |
| Tent | Reset parameters + optimizer | 0 | ba | ece15_change | 1 | -0.00024838 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.00024837990761197105} |
| Tent | Reset parameters + optimizer | 4 | ab | accuracy_change | 1 | 0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0003255208333333333} |
| Tent | Reset parameters + optimizer | 4 | ab | error_change | 1 | -0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0003255208333333333} |
| Tent | Reset parameters + optimizer | 4 | ab | nll_change | 1 | 0.000352186 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0003521862053997224} |
| Tent | Reset parameters + optimizer | 4 | ab | brier_change | 1 | 1.16175e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": 1.1617522213218495e-05} |
| Tent | Reset parameters + optimizer | 4 | ab | ece15_change | 1 | -0.00024838 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.00024837990761197105} |
| Tent | Reset parameters + optimizer | 4 | ba | accuracy_change | 1 | 0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0003255208333333333} |
| Tent | Reset parameters + optimizer | 4 | ba | error_change | 1 | -0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0003255208333333333} |
| Tent | Reset parameters + optimizer | 4 | ba | nll_change | 1 | 0.000352186 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0003521862053997224} |
| Tent | Reset parameters + optimizer | 4 | ba | brier_change | 1 | 1.16175e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": 1.1617522213218495e-05} |
| Tent | Reset parameters + optimizer | 4 | ba | ece15_change | 1 | -0.00024838 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.00024837990761197105} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | ab | accuracy_change | 1 | 0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0003255208333333333} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | ab | error_change | 1 | -0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0003255208333333333} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | ab | nll_change | 1 | 0.000352186 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0003521862053997224} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | ab | brier_change | 1 | 1.16175e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": 1.1617522213218495e-05} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | ab | ece15_change | 1 | -0.00024838 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.00024837990761197105} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | ba | accuracy_change | 1 | 0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0003255208333333333} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | ba | error_change | 1 | -0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0003255208333333333} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | ba | nll_change | 1 | 0.000352186 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0003521862053997224} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | ba | brier_change | 1 | 1.16175e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": 1.1617522213218495e-05} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | ba | ece15_change | 1 | -0.00024838 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.00024837990761197105} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | ab | accuracy_change | 1 | 0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0003255208333333333} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | ab | error_change | 1 | -0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0003255208333333333} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | ab | nll_change | 1 | 0.000352186 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0003521862053997224} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | ab | brier_change | 1 | 1.16175e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": 1.1617522213218495e-05} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | ab | ece15_change | 1 | -0.00024838 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.00024837990761197105} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | ba | accuracy_change | 1 | 0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0003255208333333333} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | ba | error_change | 1 | -0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0003255208333333333} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | ba | nll_change | 1 | 0.000352186 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0003521862053997224} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | ba | brier_change | 1 | 1.16175e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": 1.1617522213218495e-05} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | ba | ece15_change | 1 | -0.00024838 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.00024837990761197105} |


### norm_reference: descriptive seed repetitions

The same image panel is reused across seeds. These standard deviations describe seed variability only; no confidence interval is justified from treating seeds as new image panels.

| method | intervention | washout_batches | direction | panel_id | metric | n_seeds | mean | seed_sd_descriptive | individual_seeds |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SAR (complete-state implementation) | Reset all declared state | 0 | ab | uci_internal_fixed | accuracy_change | 3 | 0.000325521 | 0.000563819 | {"17": 0.0009765625, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset all declared state | 0 | ab | uci_internal_fixed | error_change | 3 | -0.000325521 | 0.000563819 | {"17": -0.0009765625, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset all declared state | 0 | ab | uci_internal_fixed | nll_change | 3 | -0.000101398 | 0.000932275 | {"17": -0.0003305530985385219, "29": 0.0009240869166181609, "43": -0.0008977276777570875} |
| SAR (complete-state implementation) | Reset all declared state | 0 | ab | uci_internal_fixed | brier_change | 3 | -9.23035e-05 | 0.000214991 | {"17": -0.0001122874158403786, "29": 0.00013198217162138648, "43": -0.00029660514131535365} |
| SAR (complete-state implementation) | Reset all declared state | 0 | ab | uci_internal_fixed | ece15_change | 3 | -0.000265989 | 0.000589506 | {"17": -0.0009463492381591998, "29": 9.28945206515458e-05, "43": 5.5488833282650585e-05} |
| SAR (complete-state implementation) | Reset all declared state | 0 | ba | uci_internal_fixed | accuracy_change | 3 | 0.000325521 | 0.000563819 | {"17": 0.0009765625, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset all declared state | 0 | ba | uci_internal_fixed | error_change | 3 | -0.000325521 | 0.000563819 | {"17": -0.0009765625, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset all declared state | 0 | ba | uci_internal_fixed | nll_change | 3 | -0.000101398 | 0.000932275 | {"17": -0.0003305530985385219, "29": 0.0009240869166181609, "43": -0.0008977276777570875} |
| SAR (complete-state implementation) | Reset all declared state | 0 | ba | uci_internal_fixed | brier_change | 3 | -9.23035e-05 | 0.000214991 | {"17": -0.0001122874158403786, "29": 0.00013198217162138648, "43": -0.00029660514131535365} |
| SAR (complete-state implementation) | Reset all declared state | 0 | ba | uci_internal_fixed | ece15_change | 3 | -0.000265989 | 0.000589506 | {"17": -0.0009463492381591998, "29": 9.28945206515458e-05, "43": 5.5488833282650585e-05} |
| SAR (complete-state implementation) | Reset all declared state | 4 | ab | uci_internal_fixed | accuracy_change | 3 | 0.000325521 | 0.000563819 | {"17": 0.0009765625, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset all declared state | 4 | ab | uci_internal_fixed | error_change | 3 | -0.000325521 | 0.000563819 | {"17": -0.0009765625, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset all declared state | 4 | ab | uci_internal_fixed | nll_change | 3 | -0.000101398 | 0.000932275 | {"17": -0.0003305530985385219, "29": 0.0009240869166181609, "43": -0.0008977276777570875} |
| SAR (complete-state implementation) | Reset all declared state | 4 | ab | uci_internal_fixed | brier_change | 3 | -9.23035e-05 | 0.000214991 | {"17": -0.0001122874158403786, "29": 0.00013198217162138648, "43": -0.00029660514131535365} |
| SAR (complete-state implementation) | Reset all declared state | 4 | ab | uci_internal_fixed | ece15_change | 3 | -0.000265989 | 0.000589506 | {"17": -0.0009463492381591998, "29": 9.28945206515458e-05, "43": 5.5488833282650585e-05} |
| SAR (complete-state implementation) | Reset all declared state | 4 | ba | uci_internal_fixed | accuracy_change | 3 | 0.000325521 | 0.000563819 | {"17": 0.0009765625, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset all declared state | 4 | ba | uci_internal_fixed | error_change | 3 | -0.000325521 | 0.000563819 | {"17": -0.0009765625, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset all declared state | 4 | ba | uci_internal_fixed | nll_change | 3 | -0.000101398 | 0.000932275 | {"17": -0.0003305530985385219, "29": 0.0009240869166181609, "43": -0.0008977276777570875} |
| SAR (complete-state implementation) | Reset all declared state | 4 | ba | uci_internal_fixed | brier_change | 3 | -9.23035e-05 | 0.000214991 | {"17": -0.0001122874158403786, "29": 0.00013198217162138648, "43": -0.00029660514131535365} |
| SAR (complete-state implementation) | Reset all declared state | 4 | ba | uci_internal_fixed | ece15_change | 3 | -0.000265989 | 0.000589506 | {"17": -0.0009463492381591998, "29": 9.28945206515458e-05, "43": 5.5488833282650585e-05} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | ab | uci_internal_fixed | accuracy_change | 3 | 0.000325521 | 0.000563819 | {"17": 0.0009765625, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | ab | uci_internal_fixed | error_change | 3 | -0.000325521 | 0.000563819 | {"17": -0.0009765625, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | ab | uci_internal_fixed | nll_change | 3 | -0.000102425 | 0.00093328 | {"17": -0.000332004511763271, "29": 0.0009242214712197085, "43": -0.0008994909490302391} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | ab | uci_internal_fixed | brier_change | 3 | -9.25464e-05 | 0.000215169 | {"17": -0.00011292444836532786, "29": 0.0001320868120555374, "43": -0.0002968015220259027} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | ab | uci_internal_fixed | ece15_change | 3 | -0.00026505 | 0.00058929 | {"17": -0.0009451907883792502, "29": 9.285976565664555e-05, "43": 5.718192353570094e-05} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | ba | uci_internal_fixed | accuracy_change | 3 | 0.000325521 | 0.000563819 | {"17": 0.0009765625, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | ba | uci_internal_fixed | error_change | 3 | -0.000325521 | 0.000563819 | {"17": -0.0009765625, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | ba | uci_internal_fixed | nll_change | 3 | -0.000101646 | 0.000932397 | {"17": -0.000331265605024271, "29": 0.0009241076843417607, "43": -0.0008977812724003872} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | ba | uci_internal_fixed | brier_change | 3 | -9.24091e-05 | 0.00021502 | {"17": -0.00011261770737117788, "29": 0.00013200140227438706, "43": -0.0002966110866761528} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | ba | uci_internal_fixed | ece15_change | 3 | -0.000265803 | 0.000589184 | {"17": -0.0009457931439275499, "29": 9.284489562069558e-05, "43": 5.554030812290108e-05} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | ab | uci_internal_fixed | accuracy_change | 3 | 0.000325521 | 0.000563819 | {"17": 0.0009765625, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | ab | uci_internal_fixed | error_change | 3 | -0.000325521 | 0.000563819 | {"17": -0.0009765625, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | ab | uci_internal_fixed | nll_change | 3 | -0.000101398 | 0.000932275 | {"17": -0.0003305530985385219, "29": 0.0009240869166181609, "43": -0.0008977276777570875} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | ab | uci_internal_fixed | brier_change | 3 | -9.23035e-05 | 0.000214991 | {"17": -0.0001122874158403786, "29": 0.00013198217162138648, "43": -0.00029660514131535365} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | ab | uci_internal_fixed | ece15_change | 3 | -0.000265989 | 0.000589506 | {"17": -0.0009463492381591998, "29": 9.28945206515458e-05, "43": 5.5488833282650585e-05} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | ba | uci_internal_fixed | accuracy_change | 3 | 0.000325521 | 0.000563819 | {"17": 0.0009765625, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | ba | uci_internal_fixed | error_change | 3 | -0.000325521 | 0.000563819 | {"17": -0.0009765625, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | ba | uci_internal_fixed | nll_change | 3 | -0.000101398 | 0.000932275 | {"17": -0.0003305530985385219, "29": 0.0009240869166181609, "43": -0.0008977276777570875} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | ba | uci_internal_fixed | brier_change | 3 | -9.23035e-05 | 0.000214991 | {"17": -0.0001122874158403786, "29": 0.00013198217162138648, "43": -0.00029660514131535365} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | ba | uci_internal_fixed | ece15_change | 3 | -0.000265989 | 0.000589506 | {"17": -0.0009463492381591998, "29": 9.28945206515458e-05, "43": 5.5488833282650585e-05} |
| SAR (complete-state implementation) | No external reset | 0 | ab | uci_internal_fixed | accuracy_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | No external reset | 0 | ab | uci_internal_fixed | error_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | No external reset | 0 | ab | uci_internal_fixed | nll_change | 3 | 9.27901e-05 | 8.53224e-05 | {"17": 0.00016050874152614275, "29": 0.00012090301347409196, "43": -3.0413126637582333e-06} |
| SAR (complete-state implementation) | No external reset | 0 | ab | uci_internal_fixed | brier_change | 3 | 1.40094e-05 | 1.63339e-05 | {"17": 2.992777005886467e-05, "29": 1.4810832697831344e-05, "43": -2.710496725089398e-06} |
| SAR (complete-state implementation) | No external reset | 0 | ab | uci_internal_fixed | ece15_change | 3 | 5.30878e-06 | 3.54563e-06 | {"17": 5.3387786320422195e-06, "29": 8.839309403148136e-06, "43": 1.7482384615016139e-06} |
| SAR (complete-state implementation) | No external reset | 0 | ba | uci_internal_fixed | accuracy_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | No external reset | 0 | ba | uci_internal_fixed | error_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | No external reset | 0 | ba | uci_internal_fixed | nll_change | 3 | 4.23087e-05 | 7.22731e-05 | {"17": 2.5249388619641433e-06, "29": 0.0001257328412038218, "43": -1.331636033906347e-06} |
| SAR (complete-state implementation) | No external reset | 0 | ba | uci_internal_fixed | brier_change | 3 | 8.59524e-07 | 1.35319e-05 | {"17": -1.066230696197823e-05, "29": 1.5760941388789917e-05, "43": -2.5200613753394857e-06} |
| SAR (complete-state implementation) | No external reset | 0 | ba | uci_internal_fixed | ece15_change | 3 | 5.44414e-06 | 4.63104e-06 | {"17": 7.830653959988061e-06, "29": 8.39515053409172e-06, "43": 1.0662304870175804e-07} |
| SAR (complete-state implementation) | No external reset | 4 | ab | uci_internal_fixed | accuracy_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | No external reset | 4 | ab | uci_internal_fixed | error_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | No external reset | 4 | ab | uci_internal_fixed | nll_change | 3 | 0.000312251 | 0.000724968 | {"17": -0.00026640578495978895, "29": 0.0011254549838058958, "43": 7.770384137656405e-05} |
| SAR (complete-state implementation) | No external reset | 4 | ab | uci_internal_fixed | brier_change | 3 | 4.14866e-05 | 0.000135071 | {"17": -7.936828208043867e-05, "29": 0.00018729416102097884, "43": 1.653381399560616e-05} |
| SAR (complete-state implementation) | No external reset | 4 | ab | uci_internal_fixed | ece15_change | 3 | 3.92032e-05 | 4.95751e-05 | {"17": 1.661330646599013e-05, "29": 9.605000126994279e-05, "43": 4.946396508005713e-06} |
| SAR (complete-state implementation) | No external reset | 4 | ba | uci_internal_fixed | accuracy_change | 3 | 0.000325521 | 0.000563819 | {"17": 0.0009765625, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | No external reset | 4 | ba | uci_internal_fixed | error_change | 3 | -0.000325521 | 0.000563819 | {"17": -0.0009765625, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | No external reset | 4 | ba | uci_internal_fixed | nll_change | 3 | 0.000341458 | 0.000690967 | {"17": -0.00017878563163342687, "29": 0.0011254549838058958, "43": 7.770384137656405e-05} |
| SAR (complete-state implementation) | No external reset | 4 | ba | uci_internal_fixed | brier_change | 3 | 4.64343e-05 | 0.000128545 | {"17": -6.452511484014711e-05, "29": 0.00018729416102097884, "43": 1.653381399560616e-05} |
| SAR (complete-state implementation) | No external reset | 4 | ba | uci_internal_fixed | ece15_change | 3 | -0.000284308 | 0.000581687 | {"17": -0.0009539189918258556, "29": 9.605000126994279e-05, "43": 4.946396508005713e-06} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | ab | uci_internal_fixed | accuracy_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | ab | uci_internal_fixed | error_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | ab | uci_internal_fixed | nll_change | 3 | 9.27931e-05 | 8.53258e-05 | {"17": 0.0001605175026861902, "29": 0.00012090301347409196, "43": -3.0413126637582333e-06} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | ab | uci_internal_fixed | brier_change | 3 | 1.40094e-05 | 1.63339e-05 | {"17": 2.9927787740965245e-05, "29": 1.4810832697831344e-05, "43": -2.710496725089398e-06} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | ab | uci_internal_fixed | ece15_change | 3 | 5.30586e-06 | 3.5456e-06 | {"17": 5.330029991592114e-06, "29": 8.839309403148136e-06, "43": 1.7482384615016139e-06} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | ba | uci_internal_fixed | accuracy_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | ba | uci_internal_fixed | error_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | ba | uci_internal_fixed | nll_change | 3 | 4.233e-05 | 7.22556e-05 | {"17": 2.588739383663219e-06, "29": 0.0001257328412038218, "43": -1.331636033906347e-06} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | ba | uci_internal_fixed | brier_change | 3 | 8.70565e-07 | 1.35178e-05 | {"17": -1.0629185625478377e-05, "29": 1.5760941388789917e-05, "43": -2.5200613753394857e-06} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | ba | uci_internal_fixed | ece15_change | 3 | 5.43258e-06 | 4.62213e-06 | {"17": 7.795969469238072e-06, "29": 8.39515053409172e-06, "43": 1.0662304870175804e-07} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | ab | uci_internal_fixed | accuracy_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | ab | uci_internal_fixed | error_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | ab | uci_internal_fixed | nll_change | 3 | 0.000312251 | 0.000724968 | {"17": -0.00026640578495978895, "29": 0.0011254549838058958, "43": 7.770384137656405e-05} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | ab | uci_internal_fixed | brier_change | 3 | 4.14866e-05 | 0.000135071 | {"17": -7.936828208043867e-05, "29": 0.00018729416102097884, "43": 1.653381399560616e-05} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | ab | uci_internal_fixed | ece15_change | 3 | 3.92032e-05 | 4.95751e-05 | {"17": 1.661330646599013e-05, "29": 9.605000126994279e-05, "43": 4.946396508005713e-06} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | ba | uci_internal_fixed | accuracy_change | 3 | 0.000325521 | 0.000563819 | {"17": 0.0009765625, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | ba | uci_internal_fixed | error_change | 3 | -0.000325521 | 0.000563819 | {"17": -0.0009765625, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | ba | uci_internal_fixed | nll_change | 3 | 0.000341458 | 0.000690967 | {"17": -0.00017878563163342687, "29": 0.0011254549838058958, "43": 7.770384137656405e-05} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | ba | uci_internal_fixed | brier_change | 3 | 4.64343e-05 | 0.000128545 | {"17": -6.452511484014711e-05, "29": 0.00018729416102097884, "43": 1.653381399560616e-05} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | ba | uci_internal_fixed | ece15_change | 3 | -0.000284308 | 0.000581687 | {"17": -0.0009539189918258556, "29": 9.605000126994279e-05, "43": 4.946396508005713e-06} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | ab | uci_internal_fixed | accuracy_change | 3 | 0.000325521 | 0.000563819 | {"17": 0.0009765625, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | ab | uci_internal_fixed | error_change | 3 | -0.000325521 | 0.000563819 | {"17": -0.0009765625, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | ab | uci_internal_fixed | nll_change | 3 | -0.000102425 | 0.00093328 | {"17": -0.000332004511763271, "29": 0.0009242214712197085, "43": -0.0008994909490302391} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | ab | uci_internal_fixed | brier_change | 3 | -9.25464e-05 | 0.000215169 | {"17": -0.00011292444836532786, "29": 0.0001320868120555374, "43": -0.0002968015220259027} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | ab | uci_internal_fixed | ece15_change | 3 | -0.00026505 | 0.00058929 | {"17": -0.0009451907883792502, "29": 9.285976565664555e-05, "43": 5.718192353570094e-05} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | ba | uci_internal_fixed | accuracy_change | 3 | 0.000325521 | 0.000563819 | {"17": 0.0009765625, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | ba | uci_internal_fixed | error_change | 3 | -0.000325521 | 0.000563819 | {"17": -0.0009765625, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | ba | uci_internal_fixed | nll_change | 3 | -0.000101646 | 0.000932397 | {"17": -0.000331265605024271, "29": 0.0009241076843417607, "43": -0.0008977812724003872} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | ba | uci_internal_fixed | brier_change | 3 | -9.24091e-05 | 0.00021502 | {"17": -0.00011261770737117788, "29": 0.00013200140227438706, "43": -0.0002966110866761528} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | ba | uci_internal_fixed | ece15_change | 3 | -0.000265803 | 0.000589184 | {"17": -0.0009457931439275499, "29": 9.284489562069558e-05, "43": 5.554030812290108e-05} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | ab | uci_internal_fixed | accuracy_change | 3 | 0.000325521 | 0.000563819 | {"17": 0.0009765625, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | ab | uci_internal_fixed | error_change | 3 | -0.000325521 | 0.000563819 | {"17": -0.0009765625, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | ab | uci_internal_fixed | nll_change | 3 | -0.000101398 | 0.000932275 | {"17": -0.0003305530985385219, "29": 0.0009240869166181609, "43": -0.0008977276777570875} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | ab | uci_internal_fixed | brier_change | 3 | -9.23035e-05 | 0.000214991 | {"17": -0.0001122874158403786, "29": 0.00013198217162138648, "43": -0.00029660514131535365} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | ab | uci_internal_fixed | ece15_change | 3 | -0.000265989 | 0.000589506 | {"17": -0.0009463492381591998, "29": 9.28945206515458e-05, "43": 5.5488833282650585e-05} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | ba | uci_internal_fixed | accuracy_change | 3 | 0.000325521 | 0.000563819 | {"17": 0.0009765625, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | ba | uci_internal_fixed | error_change | 3 | -0.000325521 | 0.000563819 | {"17": -0.0009765625, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | ba | uci_internal_fixed | nll_change | 3 | -0.000101398 | 0.000932275 | {"17": -0.0003305530985385219, "29": 0.0009240869166181609, "43": -0.0008977276777570875} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | ba | uci_internal_fixed | brier_change | 3 | -9.23035e-05 | 0.000214991 | {"17": -0.0001122874158403786, "29": 0.00013198217162138648, "43": -0.00029660514131535365} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | ba | uci_internal_fixed | ece15_change | 3 | -0.000265989 | 0.000589506 | {"17": -0.0009463492381591998, "29": 9.28945206515458e-05, "43": 5.5488833282650585e-05} |
| SAR (complete-state implementation) | Reset parameters only | 0 | ab | uci_internal_fixed | accuracy_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters only | 0 | ab | uci_internal_fixed | error_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters only | 0 | ab | uci_internal_fixed | nll_change | 3 | 9.38522e-05 | 8.49334e-05 | {"17": 0.00016206607675123968, "29": 0.00012076845887254439, "43": -1.2780413906066102e-06} |
| SAR (complete-state implementation) | Reset parameters only | 0 | ab | uci_internal_fixed | brier_change | 3 | 1.42521e-05 | 1.65439e-05 | {"17": 3.056426051166461e-05, "29": 1.4706192263680418e-05, "43": -2.514116014540324e-06} |
| SAR (complete-state implementation) | Reset parameters only | 0 | ab | uci_internal_fixed | ece15_change | 3 | 4.33445e-06 | 4.41522e-06 | {"17": 4.0741334784918926e-06, "29": 8.874064398048387e-06, "43": 5.5148208451261116e-08} |
| SAR (complete-state implementation) | Reset parameters only | 0 | ba | uci_internal_fixed | accuracy_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters only | 0 | ba | uci_internal_fixed | error_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters only | 0 | ba | uci_internal_fixed | nll_change | 3 | 4.27832e-05 | 7.18655e-05 | {"17": 3.9154563424639854e-06, "29": 0.00012571207348022195, "43": -1.2780413906066102e-06} |
| SAR (complete-state implementation) | Reset parameters only | 0 | ba | uci_internal_fixed | brier_change | 3 | 1.06385e-06 | 1.32561e-05 | {"17": -1.0036039359078222e-05, "29": 1.5741710735789338e-05, "43": -2.514116014540324e-06} |
| SAR (complete-state implementation) | Reset parameters only | 0 | ba | uci_internal_fixed | ece15_change | 3 | 5.08497e-06 | 4.43714e-06 | {"17": 6.754996131688729e-06, "29": 8.444775564941942e-06, "43": 5.5148208451261116e-08} |
| SAR (complete-state implementation) | Reset parameters only | 4 | ab | uci_internal_fixed | accuracy_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters only | 4 | ab | uci_internal_fixed | error_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters only | 4 | ab | uci_internal_fixed | nll_change | 3 | 0.000312251 | 0.000724968 | {"17": -0.00026640578495978895, "29": 0.0011254549838058958, "43": 7.770384137656405e-05} |
| SAR (complete-state implementation) | Reset parameters only | 4 | ab | uci_internal_fixed | brier_change | 3 | 4.14866e-05 | 0.000135071 | {"17": -7.936828208043867e-05, "29": 0.00018729416102097884, "43": 1.653381399560616e-05} |
| SAR (complete-state implementation) | Reset parameters only | 4 | ab | uci_internal_fixed | ece15_change | 3 | 3.92032e-05 | 4.95751e-05 | {"17": 1.661330646599013e-05, "29": 9.605000126994279e-05, "43": 4.946396508005713e-06} |
| SAR (complete-state implementation) | Reset parameters only | 4 | ba | uci_internal_fixed | accuracy_change | 3 | 0.000325521 | 0.000563819 | {"17": 0.0009765625, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters only | 4 | ba | uci_internal_fixed | error_change | 3 | -0.000325521 | 0.000563819 | {"17": -0.0009765625, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters only | 4 | ba | uci_internal_fixed | nll_change | 3 | 0.000341458 | 0.000690967 | {"17": -0.00017878563163342687, "29": 0.0011254549838058958, "43": 7.770384137656405e-05} |
| SAR (complete-state implementation) | Reset parameters only | 4 | ba | uci_internal_fixed | brier_change | 3 | 4.64343e-05 | 0.000128545 | {"17": -6.452511484014711e-05, "29": 0.00018729416102097884, "43": 1.653381399560616e-05} |
| SAR (complete-state implementation) | Reset parameters only | 4 | ba | uci_internal_fixed | ece15_change | 3 | -0.000284308 | 0.000581687 | {"17": -0.0009539189918258556, "29": 9.605000126994279e-05, "43": 4.946396508005713e-06} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | ab | uci_internal_fixed | accuracy_change | 3 | 0.000325521 | 0.000563819 | {"17": 0.0009765625, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | ab | uci_internal_fixed | error_change | 3 | -0.000325521 | 0.000563819 | {"17": -0.0009765625, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | ab | uci_internal_fixed | nll_change | 3 | -0.000101398 | 0.000932275 | {"17": -0.0003305530985385219, "29": 0.0009240869166181609, "43": -0.0008977276777570875} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | ab | uci_internal_fixed | brier_change | 3 | -9.23035e-05 | 0.000214991 | {"17": -0.0001122874158403786, "29": 0.00013198217162138648, "43": -0.00029660514131535365} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | ab | uci_internal_fixed | ece15_change | 3 | -0.000265989 | 0.000589506 | {"17": -0.0009463492381591998, "29": 9.28945206515458e-05, "43": 5.5488833282650585e-05} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | ba | uci_internal_fixed | accuracy_change | 3 | 0.000325521 | 0.000563819 | {"17": 0.0009765625, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | ba | uci_internal_fixed | error_change | 3 | -0.000325521 | 0.000563819 | {"17": -0.0009765625, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | ba | uci_internal_fixed | nll_change | 3 | -0.000101398 | 0.000932275 | {"17": -0.0003305530985385219, "29": 0.0009240869166181609, "43": -0.0008977276777570875} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | ba | uci_internal_fixed | brier_change | 3 | -9.23035e-05 | 0.000214991 | {"17": -0.0001122874158403786, "29": 0.00013198217162138648, "43": -0.00029660514131535365} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | ba | uci_internal_fixed | ece15_change | 3 | -0.000265989 | 0.000589506 | {"17": -0.0009463492381591998, "29": 9.28945206515458e-05, "43": 5.5488833282650585e-05} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | ab | uci_internal_fixed | accuracy_change | 3 | 0.000325521 | 0.000563819 | {"17": 0.0009765625, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | ab | uci_internal_fixed | error_change | 3 | -0.000325521 | 0.000563819 | {"17": -0.0009765625, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | ab | uci_internal_fixed | nll_change | 3 | -0.000101398 | 0.000932275 | {"17": -0.0003305530985385219, "29": 0.0009240869166181609, "43": -0.0008977276777570875} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | ab | uci_internal_fixed | brier_change | 3 | -9.23035e-05 | 0.000214991 | {"17": -0.0001122874158403786, "29": 0.00013198217162138648, "43": -0.00029660514131535365} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | ab | uci_internal_fixed | ece15_change | 3 | -0.000265989 | 0.000589506 | {"17": -0.0009463492381591998, "29": 9.28945206515458e-05, "43": 5.5488833282650585e-05} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | ba | uci_internal_fixed | accuracy_change | 3 | 0.000325521 | 0.000563819 | {"17": 0.0009765625, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | ba | uci_internal_fixed | error_change | 3 | -0.000325521 | 0.000563819 | {"17": -0.0009765625, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | ba | uci_internal_fixed | nll_change | 3 | -0.000101398 | 0.000932275 | {"17": -0.0003305530985385219, "29": 0.0009240869166181609, "43": -0.0008977276777570875} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | ba | uci_internal_fixed | brier_change | 3 | -9.23035e-05 | 0.000214991 | {"17": -0.0001122874158403786, "29": 0.00013198217162138648, "43": -0.00029660514131535365} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | ba | uci_internal_fixed | ece15_change | 3 | -0.000265989 | 0.000589506 | {"17": -0.0009463492381591998, "29": 9.28945206515458e-05, "43": 5.5488833282650585e-05} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | ab | uci_internal_fixed | accuracy_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | ab | uci_internal_fixed | error_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | ab | uci_internal_fixed | nll_change | 3 | 9.38553e-05 | 8.49373e-05 | {"17": 0.00016207558004039183, "29": 0.00012076845887254439, "43": -1.2780413906066102e-06} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | ab | uci_internal_fixed | brier_change | 3 | 1.42521e-05 | 1.65439e-05 | {"17": 3.056429791096528e-05, "29": 1.4706192263680418e-05, "43": -2.514116014540324e-06} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | ab | uci_internal_fixed | ece15_change | 3 | 4.33129e-06 | 4.4155e-06 | {"17": 4.064649018241731e-06, "29": 8.874064398048387e-06, "43": 5.5148208451261116e-08} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | ba | uci_internal_fixed | accuracy_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | ba | uci_internal_fixed | error_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | ba | uci_internal_fixed | nll_change | 3 | 4.28061e-05 | 7.18469e-05 | {"17": 3.984277746511833e-06, "29": 0.00012571207348022195, "43": -1.2780413906066102e-06} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | ba | uci_internal_fixed | brier_change | 3 | 1.07574e-06 | 1.32412e-05 | {"17": -1.000036021347843e-05, "29": 1.5741710735789338e-05, "43": -2.514116014540324e-06} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | ba | uci_internal_fixed | ece15_change | 3 | 5.07214e-06 | 4.42994e-06 | {"17": 6.716483636788097e-06, "29": 8.444775564941942e-06, "43": 5.5148208451261116e-08} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | ab | uci_internal_fixed | accuracy_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | ab | uci_internal_fixed | error_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | ab | uci_internal_fixed | nll_change | 3 | 0.000312251 | 0.000724968 | {"17": -0.00026640578495978895, "29": 0.0011254549838058958, "43": 7.770384137656405e-05} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | ab | uci_internal_fixed | brier_change | 3 | 4.14866e-05 | 0.000135071 | {"17": -7.936828208043867e-05, "29": 0.00018729416102097884, "43": 1.653381399560616e-05} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | ab | uci_internal_fixed | ece15_change | 3 | 3.92032e-05 | 4.95751e-05 | {"17": 1.661330646599013e-05, "29": 9.605000126994279e-05, "43": 4.946396508005713e-06} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | ba | uci_internal_fixed | accuracy_change | 3 | 0.000325521 | 0.000563819 | {"17": 0.0009765625, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | ba | uci_internal_fixed | error_change | 3 | -0.000325521 | 0.000563819 | {"17": -0.0009765625, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | ba | uci_internal_fixed | nll_change | 3 | 0.000341458 | 0.000690967 | {"17": -0.00017878563163342687, "29": 0.0011254549838058958, "43": 7.770384137656405e-05} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | ba | uci_internal_fixed | brier_change | 3 | 4.64343e-05 | 0.000128545 | {"17": -6.452511484014711e-05, "29": 0.00018729416102097884, "43": 1.653381399560616e-05} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | ba | uci_internal_fixed | ece15_change | 3 | -0.000284308 | 0.000581687 | {"17": -0.0009539189918258556, "29": 9.605000126994279e-05, "43": 4.946396508005713e-06} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | ab | uci_internal_fixed | accuracy_change | 3 | 0.000325521 | 0.000563819 | {"17": 0.0009765625, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | ab | uci_internal_fixed | error_change | 3 | -0.000325521 | 0.000563819 | {"17": -0.0009765625, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | ab | uci_internal_fixed | nll_change | 3 | -0.000101398 | 0.000932275 | {"17": -0.0003305530985385219, "29": 0.0009240869166181609, "43": -0.0008977276777570875} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | ab | uci_internal_fixed | brier_change | 3 | -9.23035e-05 | 0.000214991 | {"17": -0.0001122874158403786, "29": 0.00013198217162138648, "43": -0.00029660514131535365} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | ab | uci_internal_fixed | ece15_change | 3 | -0.000265989 | 0.000589506 | {"17": -0.0009463492381591998, "29": 9.28945206515458e-05, "43": 5.5488833282650585e-05} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | ba | uci_internal_fixed | accuracy_change | 3 | 0.000325521 | 0.000563819 | {"17": 0.0009765625, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | ba | uci_internal_fixed | error_change | 3 | -0.000325521 | 0.000563819 | {"17": -0.0009765625, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | ba | uci_internal_fixed | nll_change | 3 | -0.000101398 | 0.000932275 | {"17": -0.0003305530985385219, "29": 0.0009240869166181609, "43": -0.0008977276777570875} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | ba | uci_internal_fixed | brier_change | 3 | -9.23035e-05 | 0.000214991 | {"17": -0.0001122874158403786, "29": 0.00013198217162138648, "43": -0.00029660514131535365} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | ba | uci_internal_fixed | ece15_change | 3 | -0.000265989 | 0.000589506 | {"17": -0.0009463492381591998, "29": 9.28945206515458e-05, "43": 5.5488833282650585e-05} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | ab | uci_internal_fixed | accuracy_change | 3 | 0.000325521 | 0.000563819 | {"17": 0.0009765625, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | ab | uci_internal_fixed | error_change | 3 | -0.000325521 | 0.000563819 | {"17": -0.0009765625, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | ab | uci_internal_fixed | nll_change | 3 | -0.000101398 | 0.000932275 | {"17": -0.0003305530985385219, "29": 0.0009240869166181609, "43": -0.0008977276777570875} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | ab | uci_internal_fixed | brier_change | 3 | -9.23035e-05 | 0.000214991 | {"17": -0.0001122874158403786, "29": 0.00013198217162138648, "43": -0.00029660514131535365} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | ab | uci_internal_fixed | ece15_change | 3 | -0.000265989 | 0.000589506 | {"17": -0.0009463492381591998, "29": 9.28945206515458e-05, "43": 5.5488833282650585e-05} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | ba | uci_internal_fixed | accuracy_change | 3 | 0.000325521 | 0.000563819 | {"17": 0.0009765625, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | ba | uci_internal_fixed | error_change | 3 | -0.000325521 | 0.000563819 | {"17": -0.0009765625, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | ba | uci_internal_fixed | nll_change | 3 | -0.000101398 | 0.000932275 | {"17": -0.0003305530985385219, "29": 0.0009240869166181609, "43": -0.0008977276777570875} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | ba | uci_internal_fixed | brier_change | 3 | -9.23035e-05 | 0.000214991 | {"17": -0.0001122874158403786, "29": 0.00013198217162138648, "43": -0.00029660514131535365} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | ba | uci_internal_fixed | ece15_change | 3 | -0.000265989 | 0.000589506 | {"17": -0.0009463492381591998, "29": 9.28945206515458e-05, "43": 5.5488833282650585e-05} |
| Source | Reset all declared state | 0 | ab | uci_internal_fixed | accuracy_change | 3 | -0.0472005 | 0.0895265 | {"17": 0.009765625, "29": -0.0009765625, "43": -0.150390625} |
| Source | Reset all declared state | 0 | ab | uci_internal_fixed | error_change | 3 | 0.0472005 | 0.0895265 | {"17": -0.009765625, "29": 0.0009765625, "43": 0.150390625} |
| Source | Reset all declared state | 0 | ab | uci_internal_fixed | nll_change | 3 | 0.0380853 | 0.275399 | {"17": -0.11033965324007958, "29": -0.13126405739057143, "43": 0.3558597090097942} |
| Source | Reset all declared state | 0 | ab | uci_internal_fixed | brier_change | 3 | 0.0587236 | 0.1307 | {"17": -0.02428454792605335, "29": -0.008926806187843006, "43": 0.20938200579631697} |
| Source | Reset all declared state | 0 | ab | uci_internal_fixed | ece15_change | 3 | -0.00217309 | 0.0779969 | {"17": -0.04026631714369, "29": -0.05380312839115661, "43": 0.08755016475000539} |
| Source | Reset all declared state | 0 | ba | uci_internal_fixed | accuracy_change | 3 | -0.0472005 | 0.0895265 | {"17": 0.009765625, "29": -0.0009765625, "43": -0.150390625} |
| Source | Reset all declared state | 0 | ba | uci_internal_fixed | error_change | 3 | 0.0472005 | 0.0895265 | {"17": -0.009765625, "29": 0.0009765625, "43": 0.150390625} |
| Source | Reset all declared state | 0 | ba | uci_internal_fixed | nll_change | 3 | 0.0380853 | 0.275399 | {"17": -0.11033965324007958, "29": -0.13126405739057143, "43": 0.3558597090097942} |
| Source | Reset all declared state | 0 | ba | uci_internal_fixed | brier_change | 3 | 0.0587236 | 0.1307 | {"17": -0.02428454792605335, "29": -0.008926806187843006, "43": 0.20938200579631697} |
| Source | Reset all declared state | 0 | ba | uci_internal_fixed | ece15_change | 3 | -0.00217309 | 0.0779969 | {"17": -0.04026631714369, "29": -0.05380312839115661, "43": 0.08755016475000539} |
| Source | Reset all declared state | 4 | ab | uci_internal_fixed | accuracy_change | 3 | -0.0472005 | 0.0895265 | {"17": 0.009765625, "29": -0.0009765625, "43": -0.150390625} |
| Source | Reset all declared state | 4 | ab | uci_internal_fixed | error_change | 3 | 0.0472005 | 0.0895265 | {"17": -0.009765625, "29": 0.0009765625, "43": 0.150390625} |
| Source | Reset all declared state | 4 | ab | uci_internal_fixed | nll_change | 3 | 0.0380853 | 0.275399 | {"17": -0.11033965324007958, "29": -0.13126405739057143, "43": 0.3558597090097942} |
| Source | Reset all declared state | 4 | ab | uci_internal_fixed | brier_change | 3 | 0.0587236 | 0.1307 | {"17": -0.02428454792605335, "29": -0.008926806187843006, "43": 0.20938200579631697} |
| Source | Reset all declared state | 4 | ab | uci_internal_fixed | ece15_change | 3 | -0.00217309 | 0.0779969 | {"17": -0.04026631714369, "29": -0.05380312839115661, "43": 0.08755016475000539} |
| Source | Reset all declared state | 4 | ba | uci_internal_fixed | accuracy_change | 3 | -0.0472005 | 0.0895265 | {"17": 0.009765625, "29": -0.0009765625, "43": -0.150390625} |
| Source | Reset all declared state | 4 | ba | uci_internal_fixed | error_change | 3 | 0.0472005 | 0.0895265 | {"17": -0.009765625, "29": 0.0009765625, "43": 0.150390625} |
| Source | Reset all declared state | 4 | ba | uci_internal_fixed | nll_change | 3 | 0.0380853 | 0.275399 | {"17": -0.11033965324007958, "29": -0.13126405739057143, "43": 0.3558597090097942} |
| Source | Reset all declared state | 4 | ba | uci_internal_fixed | brier_change | 3 | 0.0587236 | 0.1307 | {"17": -0.02428454792605335, "29": -0.008926806187843006, "43": 0.20938200579631697} |
| Source | Reset all declared state | 4 | ba | uci_internal_fixed | ece15_change | 3 | -0.00217309 | 0.0779969 | {"17": -0.04026631714369, "29": -0.05380312839115661, "43": 0.08755016475000539} |
| Source | No external reset | 0 | ab | uci_internal_fixed | accuracy_change | 3 | -0.0472005 | 0.0895265 | {"17": 0.009765625, "29": -0.0009765625, "43": -0.150390625} |
| Source | No external reset | 0 | ab | uci_internal_fixed | error_change | 3 | 0.0472005 | 0.0895265 | {"17": -0.009765625, "29": 0.0009765625, "43": 0.150390625} |
| Source | No external reset | 0 | ab | uci_internal_fixed | nll_change | 3 | 0.0380853 | 0.275399 | {"17": -0.11033965324007958, "29": -0.13126405739057143, "43": 0.3558597090097942} |
| Source | No external reset | 0 | ab | uci_internal_fixed | brier_change | 3 | 0.0587236 | 0.1307 | {"17": -0.02428454792605335, "29": -0.008926806187843006, "43": 0.20938200579631697} |
| Source | No external reset | 0 | ab | uci_internal_fixed | ece15_change | 3 | -0.00217309 | 0.0779969 | {"17": -0.04026631714369, "29": -0.05380312839115661, "43": 0.08755016475000539} |
| Source | No external reset | 0 | ba | uci_internal_fixed | accuracy_change | 3 | -0.0472005 | 0.0895265 | {"17": 0.009765625, "29": -0.0009765625, "43": -0.150390625} |
| Source | No external reset | 0 | ba | uci_internal_fixed | error_change | 3 | 0.0472005 | 0.0895265 | {"17": -0.009765625, "29": 0.0009765625, "43": 0.150390625} |
| Source | No external reset | 0 | ba | uci_internal_fixed | nll_change | 3 | 0.0380853 | 0.275399 | {"17": -0.11033965324007958, "29": -0.13126405739057143, "43": 0.3558597090097942} |
| Source | No external reset | 0 | ba | uci_internal_fixed | brier_change | 3 | 0.0587236 | 0.1307 | {"17": -0.02428454792605335, "29": -0.008926806187843006, "43": 0.20938200579631697} |
| Source | No external reset | 0 | ba | uci_internal_fixed | ece15_change | 3 | -0.00217309 | 0.0779969 | {"17": -0.04026631714369, "29": -0.05380312839115661, "43": 0.08755016475000539} |
| Source | No external reset | 4 | ab | uci_internal_fixed | accuracy_change | 3 | -0.0472005 | 0.0895265 | {"17": 0.009765625, "29": -0.0009765625, "43": -0.150390625} |
| Source | No external reset | 4 | ab | uci_internal_fixed | error_change | 3 | 0.0472005 | 0.0895265 | {"17": -0.009765625, "29": 0.0009765625, "43": 0.150390625} |
| Source | No external reset | 4 | ab | uci_internal_fixed | nll_change | 3 | 0.0380853 | 0.275399 | {"17": -0.11033965324007958, "29": -0.13126405739057143, "43": 0.3558597090097942} |
| Source | No external reset | 4 | ab | uci_internal_fixed | brier_change | 3 | 0.0587236 | 0.1307 | {"17": -0.02428454792605335, "29": -0.008926806187843006, "43": 0.20938200579631697} |
| Source | No external reset | 4 | ab | uci_internal_fixed | ece15_change | 3 | -0.00217309 | 0.0779969 | {"17": -0.04026631714369, "29": -0.05380312839115661, "43": 0.08755016475000539} |
| Source | No external reset | 4 | ba | uci_internal_fixed | accuracy_change | 3 | -0.0472005 | 0.0895265 | {"17": 0.009765625, "29": -0.0009765625, "43": -0.150390625} |
| Source | No external reset | 4 | ba | uci_internal_fixed | error_change | 3 | 0.0472005 | 0.0895265 | {"17": -0.009765625, "29": 0.0009765625, "43": 0.150390625} |
| Source | No external reset | 4 | ba | uci_internal_fixed | nll_change | 3 | 0.0380853 | 0.275399 | {"17": -0.11033965324007958, "29": -0.13126405739057143, "43": 0.3558597090097942} |
| Source | No external reset | 4 | ba | uci_internal_fixed | brier_change | 3 | 0.0587236 | 0.1307 | {"17": -0.02428454792605335, "29": -0.008926806187843006, "43": 0.20938200579631697} |
| Source | No external reset | 4 | ba | uci_internal_fixed | ece15_change | 3 | -0.00217309 | 0.0779969 | {"17": -0.04026631714369, "29": -0.05380312839115661, "43": 0.08755016475000539} |
| Tent | Reset all declared state | 0 | ab | uci_internal_fixed | accuracy_change | 3 | 0.000325521 | 0.000563819 | {"17": 0.0009765625, "29": 0.0, "43": 0.0} |
| Tent | Reset all declared state | 0 | ab | uci_internal_fixed | error_change | 3 | -0.000325521 | 0.000563819 | {"17": -0.0009765625, "29": 0.0, "43": 0.0} |
| Tent | Reset all declared state | 0 | ab | uci_internal_fixed | nll_change | 3 | 0.000352186 | 0.00150158 | {"17": -0.00022113557472566367, "29": 0.0020559640906235473, "43": -0.0007782698996987164} |
| Tent | Reset all declared state | 0 | ab | uci_internal_fixed | brier_change | 3 | 1.16175e-05 | 0.000337031 | {"17": -8.894862440140226e-05, "29": 0.0003874845027150402, "43": -0.00026368331167398243} |
| Tent | Reset all declared state | 0 | ab | uci_internal_fixed | ece15_change | 3 | -0.00024838 | 0.000591103 | {"17": -0.000929433221129556, "29": 0.00013123358749319095, "43": 5.305991080045182e-05} |
| Tent | Reset all declared state | 0 | ba | uci_internal_fixed | accuracy_change | 3 | 0.000325521 | 0.000563819 | {"17": 0.0009765625, "29": 0.0, "43": 0.0} |
| Tent | Reset all declared state | 0 | ba | uci_internal_fixed | error_change | 3 | -0.000325521 | 0.000563819 | {"17": -0.0009765625, "29": 0.0, "43": 0.0} |
| Tent | Reset all declared state | 0 | ba | uci_internal_fixed | nll_change | 3 | 0.000352186 | 0.00150158 | {"17": -0.00022113557472566367, "29": 0.0020559640906235473, "43": -0.0007782698996987164} |
| Tent | Reset all declared state | 0 | ba | uci_internal_fixed | brier_change | 3 | 1.16175e-05 | 0.000337031 | {"17": -8.894862440140226e-05, "29": 0.0003874845027150402, "43": -0.00026368331167398243} |
| Tent | Reset all declared state | 0 | ba | uci_internal_fixed | ece15_change | 3 | -0.00024838 | 0.000591103 | {"17": -0.000929433221129556, "29": 0.00013123358749319095, "43": 5.305991080045182e-05} |
| Tent | Reset all declared state | 4 | ab | uci_internal_fixed | accuracy_change | 3 | 0.000325521 | 0.000563819 | {"17": 0.0009765625, "29": 0.0, "43": 0.0} |
| Tent | Reset all declared state | 4 | ab | uci_internal_fixed | error_change | 3 | -0.000325521 | 0.000563819 | {"17": -0.0009765625, "29": 0.0, "43": 0.0} |
| Tent | Reset all declared state | 4 | ab | uci_internal_fixed | nll_change | 3 | 0.000352186 | 0.00150158 | {"17": -0.00022113557472566367, "29": 0.0020559640906235473, "43": -0.0007782698996987164} |
| Tent | Reset all declared state | 4 | ab | uci_internal_fixed | brier_change | 3 | 1.16175e-05 | 0.000337031 | {"17": -8.894862440140226e-05, "29": 0.0003874845027150402, "43": -0.00026368331167398243} |
| Tent | Reset all declared state | 4 | ab | uci_internal_fixed | ece15_change | 3 | -0.00024838 | 0.000591103 | {"17": -0.000929433221129556, "29": 0.00013123358749319095, "43": 5.305991080045182e-05} |
| Tent | Reset all declared state | 4 | ba | uci_internal_fixed | accuracy_change | 3 | 0.000325521 | 0.000563819 | {"17": 0.0009765625, "29": 0.0, "43": 0.0} |
| Tent | Reset all declared state | 4 | ba | uci_internal_fixed | error_change | 3 | -0.000325521 | 0.000563819 | {"17": -0.0009765625, "29": 0.0, "43": 0.0} |
| Tent | Reset all declared state | 4 | ba | uci_internal_fixed | nll_change | 3 | 0.000352186 | 0.00150158 | {"17": -0.00022113557472566367, "29": 0.0020559640906235473, "43": -0.0007782698996987164} |
| Tent | Reset all declared state | 4 | ba | uci_internal_fixed | brier_change | 3 | 1.16175e-05 | 0.000337031 | {"17": -8.894862440140226e-05, "29": 0.0003874845027150402, "43": -0.00026368331167398243} |
| Tent | Reset all declared state | 4 | ba | uci_internal_fixed | ece15_change | 3 | -0.00024838 | 0.000591103 | {"17": -0.000929433221129556, "29": 0.00013123358749319095, "43": 5.305991080045182e-05} |
| Tent | Reset auxiliary state only | 0 | ab | uci_internal_fixed | accuracy_change | 3 | 0.000651042 | 0.00112764 | {"17": 0.001953125, "29": 0.0, "43": 0.0} |
| Tent | Reset auxiliary state only | 0 | ab | uci_internal_fixed | error_change | 3 | -0.000651042 | 0.00112764 | {"17": -0.001953125, "29": 0.0, "43": 0.0} |
| Tent | Reset auxiliary state only | 0 | ab | uci_internal_fixed | nll_change | 3 | 0.00013717 | 0.00120387 | {"17": -0.0007015234458344032, "29": 0.001516595067380791, "43": -0.0004035608915953538} |
| Tent | Reset auxiliary state only | 0 | ab | uci_internal_fixed | brier_change | 3 | -6.22554e-05 | 0.000269596 | {"17": -0.0002502514856768945, "29": 0.0002466271206861357, "43": -0.00018314173710310376} |
| Tent | Reset auxiliary state only | 0 | ab | uci_internal_fixed | ece15_change | 3 | 9.83519e-05 | 0.00124143 | {"17": -0.0013351237638290492, "29": 0.0008160745924653406, "43": 0.0008141048239799029} |
| Tent | Reset auxiliary state only | 0 | ba | uci_internal_fixed | accuracy_change | 3 | 0.000325521 | 0.000563819 | {"17": 0.0009765625, "29": 0.0, "43": 0.0} |
| Tent | Reset auxiliary state only | 0 | ba | uci_internal_fixed | error_change | 3 | -0.000325521 | 0.000563819 | {"17": -0.0009765625, "29": 0.0, "43": 0.0} |
| Tent | Reset auxiliary state only | 0 | ba | uci_internal_fixed | nll_change | 3 | 0.000111009 | 0.00120566 | {"17": -0.0006785737058702529, "29": 0.0014987953803996534, "43": -0.00048719410679919084} |
| Tent | Reset auxiliary state only | 0 | ba | uci_internal_fixed | brier_change | 3 | -6.44908e-05 | 0.000272127 | {"17": -0.00023631239437977604, "29": 0.00024926034872798514, "43": -0.00020642030255808505} |
| Tent | Reset auxiliary state only | 0 | ba | uci_internal_fixed | ece15_change | 3 | 0.00024961 | 0.000959173 | {"17": -0.0008579099624040059, "29": 0.0008112912775415414, "43": 0.0007954475965105063} |
| Tent | Reset auxiliary state only | 4 | ab | uci_internal_fixed | accuracy_change | 3 | 0.000976562 | 0.00169146 | {"17": 0.0029296875, "29": 0.0, "43": 0.0} |
| Tent | Reset auxiliary state only | 4 | ab | uci_internal_fixed | error_change | 3 | -0.000976562 | 0.00169146 | {"17": -0.0029296875, "29": 0.0, "43": 0.0} |
| Tent | Reset auxiliary state only | 4 | ab | uci_internal_fixed | nll_change | 3 | 0.000621673 | 0.00298344 | {"17": -0.0009201909610641358, "29": 0.004060545299995815, "43": -0.0012753351946561166} |
| Tent | Reset auxiliary state only | 4 | ab | uci_internal_fixed | brier_change | 3 | -7.77439e-06 | 0.000693091 | {"17": -0.00033051111056383795, "29": 0.000787830212053843, "43": -0.0004806422620476404} |
| Tent | Reset auxiliary state only | 4 | ab | uci_internal_fixed | ece15_change | 3 | -5.15454e-05 | 0.000790902 | {"17": -0.0004800123312745496, "29": -0.0005357662985245116, "43": 0.0008611423198219559} |
| Tent | Reset auxiliary state only | 4 | ba | uci_internal_fixed | accuracy_change | 3 | 0.000976562 | 0.00169146 | {"17": 0.0029296875, "29": 0.0, "43": 0.0} |
| Tent | Reset auxiliary state only | 4 | ba | uci_internal_fixed | error_change | 3 | -0.000976562 | 0.00169146 | {"17": -0.0029296875, "29": 0.0, "43": 0.0} |
| Tent | Reset auxiliary state only | 4 | ba | uci_internal_fixed | nll_change | 3 | 0.000604387 | 0.00298816 | {"17": -0.0009032297757565685, "29": 0.004046019908702195, "43": -0.0013296288883595103} |
| Tent | Reset auxiliary state only | 4 | ba | uci_internal_fixed | brier_change | 3 | -9.36237e-06 | 0.00069646 | {"17": -0.00032095459116204643, "29": 0.0007884925868930481, "43": -0.0004956250986927896} |
| Tent | Reset auxiliary state only | 4 | ba | uci_internal_fixed | ece15_change | 3 | -5.99564e-05 | 0.0007876 | {"17": -0.0004858350305824554, "29": -0.0005429228973980026, "43": 0.0008488887252941562} |
| Tent | No external reset | 0 | ab | uci_internal_fixed | accuracy_change | 3 | 0.000651042 | 0.00112764 | {"17": 0.001953125, "29": 0.0, "43": 0.0} |
| Tent | No external reset | 0 | ab | uci_internal_fixed | error_change | 3 | -0.000651042 | 0.00112764 | {"17": -0.001953125, "29": 0.0, "43": 0.0} |
| Tent | No external reset | 0 | ab | uci_internal_fixed | nll_change | 3 | 0.00013717 | 0.00120387 | {"17": -0.0007015234458344032, "29": 0.001516595067380791, "43": -0.0004035608915953538} |
| Tent | No external reset | 0 | ab | uci_internal_fixed | brier_change | 3 | -6.22554e-05 | 0.000269596 | {"17": -0.0002502514856768945, "29": 0.0002466271206861357, "43": -0.00018314173710310376} |
| Tent | No external reset | 0 | ab | uci_internal_fixed | ece15_change | 3 | 9.83519e-05 | 0.00124143 | {"17": -0.0013351237638290492, "29": 0.0008160745924653406, "43": 0.0008141048239799029} |
| Tent | No external reset | 0 | ba | uci_internal_fixed | accuracy_change | 3 | 0.000325521 | 0.000563819 | {"17": 0.0009765625, "29": 0.0, "43": 0.0} |
| Tent | No external reset | 0 | ba | uci_internal_fixed | error_change | 3 | -0.000325521 | 0.000563819 | {"17": -0.0009765625, "29": 0.0, "43": 0.0} |
| Tent | No external reset | 0 | ba | uci_internal_fixed | nll_change | 3 | 0.000111009 | 0.00120566 | {"17": -0.0006785737058702529, "29": 0.0014987953803996534, "43": -0.00048719410679919084} |
| Tent | No external reset | 0 | ba | uci_internal_fixed | brier_change | 3 | -6.44908e-05 | 0.000272127 | {"17": -0.00023631239437977604, "29": 0.00024926034872798514, "43": -0.00020642030255808505} |
| Tent | No external reset | 0 | ba | uci_internal_fixed | ece15_change | 3 | 0.00024961 | 0.000959173 | {"17": -0.0008579099624040059, "29": 0.0008112912775415414, "43": 0.0007954475965105063} |
| Tent | No external reset | 4 | ab | uci_internal_fixed | accuracy_change | 3 | 0.000976562 | 0.00169146 | {"17": 0.0029296875, "29": 0.0, "43": 0.0} |
| Tent | No external reset | 4 | ab | uci_internal_fixed | error_change | 3 | -0.000976562 | 0.00169146 | {"17": -0.0029296875, "29": 0.0, "43": 0.0} |
| Tent | No external reset | 4 | ab | uci_internal_fixed | nll_change | 3 | 0.000621673 | 0.00298344 | {"17": -0.0009201909610641358, "29": 0.004060545299995815, "43": -0.0012753351946561166} |
| Tent | No external reset | 4 | ab | uci_internal_fixed | brier_change | 3 | -7.77439e-06 | 0.000693091 | {"17": -0.00033051111056383795, "29": 0.000787830212053843, "43": -0.0004806422620476404} |
| Tent | No external reset | 4 | ab | uci_internal_fixed | ece15_change | 3 | -5.15454e-05 | 0.000790902 | {"17": -0.0004800123312745496, "29": -0.0005357662985245116, "43": 0.0008611423198219559} |
| Tent | No external reset | 4 | ba | uci_internal_fixed | accuracy_change | 3 | 0.000976562 | 0.00169146 | {"17": 0.0029296875, "29": 0.0, "43": 0.0} |
| Tent | No external reset | 4 | ba | uci_internal_fixed | error_change | 3 | -0.000976562 | 0.00169146 | {"17": -0.0029296875, "29": 0.0, "43": 0.0} |
| Tent | No external reset | 4 | ba | uci_internal_fixed | nll_change | 3 | 0.000604387 | 0.00298816 | {"17": -0.0009032297757565685, "29": 0.004046019908702195, "43": -0.0013296288883595103} |
| Tent | No external reset | 4 | ba | uci_internal_fixed | brier_change | 3 | -9.36237e-06 | 0.00069646 | {"17": -0.00032095459116204643, "29": 0.0007884925868930481, "43": -0.0004956250986927896} |
| Tent | No external reset | 4 | ba | uci_internal_fixed | ece15_change | 3 | -5.99564e-05 | 0.0007876 | {"17": -0.0004858350305824554, "29": -0.0005429228973980026, "43": 0.0008488887252941562} |
| Tent | Reset optimizer only | 0 | ab | uci_internal_fixed | accuracy_change | 3 | 0.000651042 | 0.00112764 | {"17": 0.001953125, "29": 0.0, "43": 0.0} |
| Tent | Reset optimizer only | 0 | ab | uci_internal_fixed | error_change | 3 | -0.000651042 | 0.00112764 | {"17": -0.001953125, "29": 0.0, "43": 0.0} |
| Tent | Reset optimizer only | 0 | ab | uci_internal_fixed | nll_change | 3 | 0.000227218 | 0.00135205 | {"17": -0.0006268016133789654, "29": 0.0017860497988065605, "43": -0.00047759397311043783} |
| Tent | Reset optimizer only | 0 | ab | uci_internal_fixed | brier_change | 3 | -4.21894e-05 | 0.000299118 | {"17": -0.00022957170782710035, "29": 0.0003027732008378959, "43": -0.00019976982550868987} |
| Tent | Reset optimizer only | 0 | ab | uci_internal_fixed | ece15_change | 3 | -0.000131091 | 0.00110552 | {"17": -0.0013478725648891016, "29": 0.0008116100070167959, "43": 0.00014298938120440273} |
| Tent | Reset optimizer only | 0 | ba | uci_internal_fixed | accuracy_change | 3 | 0.000325521 | 0.000563819 | {"17": 0.0009765625, "29": 0.0, "43": 0.0} |
| Tent | Reset optimizer only | 0 | ba | uci_internal_fixed | error_change | 3 | -0.000325521 | 0.000563819 | {"17": -0.0009765625, "29": 0.0, "43": 0.0} |
| Tent | Reset optimizer only | 0 | ba | uci_internal_fixed | nll_change | 3 | 0.000164364 | 0.00137408 | {"17": -0.0005872333284421827, "29": 0.0017502966639879707, "43": -0.0006699706817876183} |
| Tent | Reset optimizer only | 0 | ba | uci_internal_fixed | brier_change | 3 | -4.67816e-05 | 0.000306653 | {"17": -0.00020182846496237875, "29": 0.0003064342572615449, "43": -0.00024495051379779843} |
| Tent | Reset optimizer only | 0 | ba | uci_internal_fixed | ece15_change | 3 | 8.66385e-06 | 0.000830023 | {"17": -0.0008839827897062563, "29": 0.00015278694489593778, "43": 0.0007571873992931509} |
| Tent | Reset optimizer only | 4 | ab | uci_internal_fixed | accuracy_change | 3 | 0.000976562 | 0.00169146 | {"17": 0.0029296875, "29": 0.0, "43": 0.0} |
| Tent | Reset optimizer only | 4 | ab | uci_internal_fixed | error_change | 3 | -0.000976562 | 0.00169146 | {"17": -0.0029296875, "29": 0.0, "43": 0.0} |
| Tent | Reset optimizer only | 4 | ab | uci_internal_fixed | nll_change | 3 | 0.000262555 | 0.00181247 | {"17": -0.0007801016854022125, "29": 0.002355415746895295, "43": -0.000787647918200015} |
| Tent | Reset optimizer only | 4 | ab | uci_internal_fixed | brier_change | 3 | -5.42994e-05 | 0.000414318 | {"17": -0.0002789435808340443, "29": 0.0004238243606360433, "43": -0.00030777892308424953} |
| Tent | Reset optimizer only | 4 | ab | uci_internal_fixed | ece15_change | 3 | -0.000262059 | 0.00037618 | {"17": -0.000502752244080056, "29": -0.00045485988582460394, "43": 0.00017143601489115132} |
| Tent | Reset optimizer only | 4 | ba | uci_internal_fixed | accuracy_change | 3 | 0.000976562 | 0.00169146 | {"17": 0.0029296875, "29": 0.0, "43": 0.0} |
| Tent | Reset optimizer only | 4 | ba | uci_internal_fixed | error_change | 3 | -0.000976562 | 0.00169146 | {"17": -0.0029296875, "29": 0.0, "43": 0.0} |
| Tent | Reset optimizer only | 4 | ba | uci_internal_fixed | nll_change | 3 | 0.000220808 | 0.00182962 | {"17": -0.000754317347647783, "29": 0.002331438906430651, "43": -0.000914696216927257} |
| Tent | Reset optimizer only | 4 | ba | uci_internal_fixed | brier_change | 3 | -5.76002e-05 | 0.000420417 | {"17": -0.0002609377735797863, "29": 0.0004258286591269488, "43": -0.000337691445692654} |
| Tent | Reset optimizer only | 4 | ba | uci_internal_fixed | ece15_change | 3 | -5.8261e-05 | 0.000742734 | {"17": -0.0005142818464840097, "29": -0.0004592872622068561, "43": 0.0007987861729649021} |
| Tent | Reset optimizer + auxiliary state | 0 | ab | uci_internal_fixed | accuracy_change | 3 | 0.000651042 | 0.00112764 | {"17": 0.001953125, "29": 0.0, "43": 0.0} |
| Tent | Reset optimizer + auxiliary state | 0 | ab | uci_internal_fixed | error_change | 3 | -0.000651042 | 0.00112764 | {"17": -0.001953125, "29": 0.0, "43": 0.0} |
| Tent | Reset optimizer + auxiliary state | 0 | ab | uci_internal_fixed | nll_change | 3 | 0.000227218 | 0.00135205 | {"17": -0.0006268016133789654, "29": 0.0017860497988065605, "43": -0.00047759397311043783} |
| Tent | Reset optimizer + auxiliary state | 0 | ab | uci_internal_fixed | brier_change | 3 | -4.21894e-05 | 0.000299118 | {"17": -0.00022957170782710035, "29": 0.0003027732008378959, "43": -0.00019976982550868987} |
| Tent | Reset optimizer + auxiliary state | 0 | ab | uci_internal_fixed | ece15_change | 3 | -0.000131091 | 0.00110552 | {"17": -0.0013478725648891016, "29": 0.0008116100070167959, "43": 0.00014298938120440273} |
| Tent | Reset optimizer + auxiliary state | 0 | ba | uci_internal_fixed | accuracy_change | 3 | 0.000325521 | 0.000563819 | {"17": 0.0009765625, "29": 0.0, "43": 0.0} |
| Tent | Reset optimizer + auxiliary state | 0 | ba | uci_internal_fixed | error_change | 3 | -0.000325521 | 0.000563819 | {"17": -0.0009765625, "29": 0.0, "43": 0.0} |
| Tent | Reset optimizer + auxiliary state | 0 | ba | uci_internal_fixed | nll_change | 3 | 0.000164364 | 0.00137408 | {"17": -0.0005872333284421827, "29": 0.0017502966639879707, "43": -0.0006699706817876183} |
| Tent | Reset optimizer + auxiliary state | 0 | ba | uci_internal_fixed | brier_change | 3 | -4.67816e-05 | 0.000306653 | {"17": -0.00020182846496237875, "29": 0.0003064342572615449, "43": -0.00024495051379779843} |
| Tent | Reset optimizer + auxiliary state | 0 | ba | uci_internal_fixed | ece15_change | 3 | 8.66385e-06 | 0.000830023 | {"17": -0.0008839827897062563, "29": 0.00015278694489593778, "43": 0.0007571873992931509} |
| Tent | Reset optimizer + auxiliary state | 4 | ab | uci_internal_fixed | accuracy_change | 3 | 0.000976562 | 0.00169146 | {"17": 0.0029296875, "29": 0.0, "43": 0.0} |
| Tent | Reset optimizer + auxiliary state | 4 | ab | uci_internal_fixed | error_change | 3 | -0.000976562 | 0.00169146 | {"17": -0.0029296875, "29": 0.0, "43": 0.0} |
| Tent | Reset optimizer + auxiliary state | 4 | ab | uci_internal_fixed | nll_change | 3 | 0.000262555 | 0.00181247 | {"17": -0.0007801016854022125, "29": 0.002355415746895295, "43": -0.000787647918200015} |
| Tent | Reset optimizer + auxiliary state | 4 | ab | uci_internal_fixed | brier_change | 3 | -5.42994e-05 | 0.000414318 | {"17": -0.0002789435808340443, "29": 0.0004238243606360433, "43": -0.00030777892308424953} |
| Tent | Reset optimizer + auxiliary state | 4 | ab | uci_internal_fixed | ece15_change | 3 | -0.000262059 | 0.00037618 | {"17": -0.000502752244080056, "29": -0.00045485988582460394, "43": 0.00017143601489115132} |
| Tent | Reset optimizer + auxiliary state | 4 | ba | uci_internal_fixed | accuracy_change | 3 | 0.000976562 | 0.00169146 | {"17": 0.0029296875, "29": 0.0, "43": 0.0} |
| Tent | Reset optimizer + auxiliary state | 4 | ba | uci_internal_fixed | error_change | 3 | -0.000976562 | 0.00169146 | {"17": -0.0029296875, "29": 0.0, "43": 0.0} |
| Tent | Reset optimizer + auxiliary state | 4 | ba | uci_internal_fixed | nll_change | 3 | 0.000220808 | 0.00182962 | {"17": -0.000754317347647783, "29": 0.002331438906430651, "43": -0.000914696216927257} |
| Tent | Reset optimizer + auxiliary state | 4 | ba | uci_internal_fixed | brier_change | 3 | -5.76002e-05 | 0.000420417 | {"17": -0.0002609377735797863, "29": 0.0004258286591269488, "43": -0.000337691445692654} |
| Tent | Reset optimizer + auxiliary state | 4 | ba | uci_internal_fixed | ece15_change | 3 | -5.8261e-05 | 0.000742734 | {"17": -0.0005142818464840097, "29": -0.0004592872622068561, "43": 0.0007987861729649021} |
| Tent | Reset parameters only | 0 | ab | uci_internal_fixed | accuracy_change | 3 | 0.000325521 | 0.000563819 | {"17": 0.0009765625, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters only | 0 | ab | uci_internal_fixed | error_change | 3 | -0.000325521 | 0.000563819 | {"17": -0.0009765625, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters only | 0 | ab | uci_internal_fixed | nll_change | 3 | 0.000261411 | 0.00133472 | {"17": -0.0002948363905330986, "29": 0.0017842902410980799, "43": -0.000705221725634645} |
| Tent | Reset parameters only | 0 | ab | uci_internal_fixed | brier_change | 3 | -8.90223e-06 | 0.000301813 | {"17": -0.00010964790838624734, "29": 0.0003303972855719303, "43": -0.00024745606538158736} |
| Tent | Reset parameters only | 0 | ab | uci_internal_fixed | ece15_change | 3 | -0.000235601 | 0.000589292 | {"17": -0.0009150734866362606, "29": 0.0001358045618647481, "43": 7.246534856614976e-05} |
| Tent | Reset parameters only | 0 | ba | uci_internal_fixed | accuracy_change | 3 | 0.000325521 | 0.000563819 | {"17": 0.0009765625, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters only | 0 | ba | uci_internal_fixed | error_change | 3 | -0.000325521 | 0.000563819 | {"17": -0.0009765625, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters only | 0 | ba | uci_internal_fixed | nll_change | 3 | 0.000298026 | 0.00130898 | {"17": -0.000308321328623018, "29": 0.001800234112795042, "43": -0.0005978360588856646} |
| Tent | Reset parameters only | 0 | ba | uci_internal_fixed | brier_change | 3 | -6.55665e-06 | 0.000295163 | {"17": -0.00012259010618978494, "29": 0.00032899070274159704, "43": -0.0002260705389897904} |
| Tent | Reset parameters only | 0 | ba | uci_internal_fixed | ece15_change | 3 | -0.000224567 | 0.000587994 | {"17": -0.0009029486897857049, "29": 0.00013882406204084475, "43": 9.042245924635681e-05} |
| Tent | Reset parameters only | 4 | ab | uci_internal_fixed | accuracy_change | 3 | 0.000325521 | 0.000563819 | {"17": 0.0009765625, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters only | 4 | ab | uci_internal_fixed | error_change | 3 | -0.000325521 | 0.000563819 | {"17": -0.0009765625, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters only | 4 | ab | uci_internal_fixed | nll_change | 3 | 0.000708485 | 0.0026786 | {"17": -0.0003618123694938205, "29": 0.0037567505293994406, "43": -0.0012694839057777324} |
| Tent | Reset parameters only | 4 | ab | uci_internal_fixed | brier_change | 3 | 5.70428e-05 | 0.000618249 | {"17": -0.00014099379675287967, "29": 0.0007500460372075017, "43": -0.0004379237606109993} |
| Tent | Reset parameters only | 4 | ab | uci_internal_fixed | ece15_change | 3 | -0.000194572 | 0.000609435 | {"17": -0.0008944901612192597, "29": 0.00021860883627509292, "43": 9.216563991290474e-05} |
| Tent | Reset parameters only | 4 | ba | uci_internal_fixed | accuracy_change | 3 | 0.000325521 | 0.000563819 | {"17": 0.0009765625, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters only | 4 | ba | uci_internal_fixed | error_change | 3 | -0.000325521 | 0.000563819 | {"17": -0.0009765625, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters only | 4 | ba | uci_internal_fixed | nll_change | 3 | 0.000732189 | 0.00265821 | {"17": -0.00036986255941822213, "29": 0.003764183315328063, "43": -0.0011977528104309201} |
| Tent | Reset parameters only | 4 | ba | uci_internal_fixed | brier_change | 3 | 5.84231e-05 | 0.000612754 | {"17": -0.00014934596689287517, "29": 0.0007480479598517015, "43": -0.00042343267600024326} |
| Tent | Reset parameters only | 4 | ba | uci_internal_fixed | ece15_change | 3 | -0.000360931 | 0.000498019 | {"17": -0.0008864906455854108, "29": -0.0003002963235922626, "43": 0.00010399458227810122} |
| Tent | Reset parameters + auxiliary state | 0 | ab | uci_internal_fixed | accuracy_change | 3 | 0.000325521 | 0.000563819 | {"17": 0.0009765625, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + auxiliary state | 0 | ab | uci_internal_fixed | error_change | 3 | -0.000325521 | 0.000563819 | {"17": -0.0009765625, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + auxiliary state | 0 | ab | uci_internal_fixed | nll_change | 3 | 0.000261411 | 0.00133472 | {"17": -0.0002948363905330986, "29": 0.0017842902410980799, "43": -0.000705221725634645} |
| Tent | Reset parameters + auxiliary state | 0 | ab | uci_internal_fixed | brier_change | 3 | -8.90223e-06 | 0.000301813 | {"17": -0.00010964790838624734, "29": 0.0003303972855719303, "43": -0.00024745606538158736} |
| Tent | Reset parameters + auxiliary state | 0 | ab | uci_internal_fixed | ece15_change | 3 | -0.000235601 | 0.000589292 | {"17": -0.0009150734866362606, "29": 0.0001358045618647481, "43": 7.246534856614976e-05} |
| Tent | Reset parameters + auxiliary state | 0 | ba | uci_internal_fixed | accuracy_change | 3 | 0.000325521 | 0.000563819 | {"17": 0.0009765625, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + auxiliary state | 0 | ba | uci_internal_fixed | error_change | 3 | -0.000325521 | 0.000563819 | {"17": -0.0009765625, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + auxiliary state | 0 | ba | uci_internal_fixed | nll_change | 3 | 0.000298026 | 0.00130898 | {"17": -0.000308321328623018, "29": 0.001800234112795042, "43": -0.0005978360588856646} |
| Tent | Reset parameters + auxiliary state | 0 | ba | uci_internal_fixed | brier_change | 3 | -6.55665e-06 | 0.000295163 | {"17": -0.00012259010618978494, "29": 0.00032899070274159704, "43": -0.0002260705389897904} |
| Tent | Reset parameters + auxiliary state | 0 | ba | uci_internal_fixed | ece15_change | 3 | -0.000224567 | 0.000587994 | {"17": -0.0009029486897857049, "29": 0.00013882406204084475, "43": 9.042245924635681e-05} |
| Tent | Reset parameters + auxiliary state | 4 | ab | uci_internal_fixed | accuracy_change | 3 | 0.000325521 | 0.000563819 | {"17": 0.0009765625, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + auxiliary state | 4 | ab | uci_internal_fixed | error_change | 3 | -0.000325521 | 0.000563819 | {"17": -0.0009765625, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + auxiliary state | 4 | ab | uci_internal_fixed | nll_change | 3 | 0.000708485 | 0.0026786 | {"17": -0.0003618123694938205, "29": 0.0037567505293994406, "43": -0.0012694839057777324} |
| Tent | Reset parameters + auxiliary state | 4 | ab | uci_internal_fixed | brier_change | 3 | 5.70428e-05 | 0.000618249 | {"17": -0.00014099379675287967, "29": 0.0007500460372075017, "43": -0.0004379237606109993} |
| Tent | Reset parameters + auxiliary state | 4 | ab | uci_internal_fixed | ece15_change | 3 | -0.000194572 | 0.000609435 | {"17": -0.0008944901612192597, "29": 0.00021860883627509292, "43": 9.216563991290474e-05} |
| Tent | Reset parameters + auxiliary state | 4 | ba | uci_internal_fixed | accuracy_change | 3 | 0.000325521 | 0.000563819 | {"17": 0.0009765625, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + auxiliary state | 4 | ba | uci_internal_fixed | error_change | 3 | -0.000325521 | 0.000563819 | {"17": -0.0009765625, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + auxiliary state | 4 | ba | uci_internal_fixed | nll_change | 3 | 0.000732189 | 0.00265821 | {"17": -0.00036986255941822213, "29": 0.003764183315328063, "43": -0.0011977528104309201} |
| Tent | Reset parameters + auxiliary state | 4 | ba | uci_internal_fixed | brier_change | 3 | 5.84231e-05 | 0.000612754 | {"17": -0.00014934596689287517, "29": 0.0007480479598517015, "43": -0.00042343267600024326} |
| Tent | Reset parameters + auxiliary state | 4 | ba | uci_internal_fixed | ece15_change | 3 | -0.000360931 | 0.000498019 | {"17": -0.0008864906455854108, "29": -0.0003002963235922626, "43": 0.00010399458227810122} |
| Tent | Reset parameters + optimizer | 0 | ab | uci_internal_fixed | accuracy_change | 3 | 0.000325521 | 0.000563819 | {"17": 0.0009765625, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + optimizer | 0 | ab | uci_internal_fixed | error_change | 3 | -0.000325521 | 0.000563819 | {"17": -0.0009765625, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + optimizer | 0 | ab | uci_internal_fixed | nll_change | 3 | 0.000352186 | 0.00150158 | {"17": -0.00022113557472566367, "29": 0.0020559640906235473, "43": -0.0007782698996987164} |
| Tent | Reset parameters + optimizer | 0 | ab | uci_internal_fixed | brier_change | 3 | 1.16175e-05 | 0.000337031 | {"17": -8.894862440140226e-05, "29": 0.0003874845027150402, "43": -0.00026368331167398243} |
| Tent | Reset parameters + optimizer | 0 | ab | uci_internal_fixed | ece15_change | 3 | -0.00024838 | 0.000591103 | {"17": -0.000929433221129556, "29": 0.00013123358749319095, "43": 5.305991080045182e-05} |
| Tent | Reset parameters + optimizer | 0 | ba | uci_internal_fixed | accuracy_change | 3 | 0.000325521 | 0.000563819 | {"17": 0.0009765625, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + optimizer | 0 | ba | uci_internal_fixed | error_change | 3 | -0.000325521 | 0.000563819 | {"17": -0.0009765625, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + optimizer | 0 | ba | uci_internal_fixed | nll_change | 3 | 0.000352186 | 0.00150158 | {"17": -0.00022113557472566367, "29": 0.0020559640906235473, "43": -0.0007782698996987164} |
| Tent | Reset parameters + optimizer | 0 | ba | uci_internal_fixed | brier_change | 3 | 1.16175e-05 | 0.000337031 | {"17": -8.894862440140226e-05, "29": 0.0003874845027150402, "43": -0.00026368331167398243} |
| Tent | Reset parameters + optimizer | 0 | ba | uci_internal_fixed | ece15_change | 3 | -0.00024838 | 0.000591103 | {"17": -0.000929433221129556, "29": 0.00013123358749319095, "43": 5.305991080045182e-05} |
| Tent | Reset parameters + optimizer | 4 | ab | uci_internal_fixed | accuracy_change | 3 | 0.000325521 | 0.000563819 | {"17": 0.0009765625, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + optimizer | 4 | ab | uci_internal_fixed | error_change | 3 | -0.000325521 | 0.000563819 | {"17": -0.0009765625, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + optimizer | 4 | ab | uci_internal_fixed | nll_change | 3 | 0.000352186 | 0.00150158 | {"17": -0.00022113557472566367, "29": 0.0020559640906235473, "43": -0.0007782698996987164} |
| Tent | Reset parameters + optimizer | 4 | ab | uci_internal_fixed | brier_change | 3 | 1.16175e-05 | 0.000337031 | {"17": -8.894862440140226e-05, "29": 0.0003874845027150402, "43": -0.00026368331167398243} |
| Tent | Reset parameters + optimizer | 4 | ab | uci_internal_fixed | ece15_change | 3 | -0.00024838 | 0.000591103 | {"17": -0.000929433221129556, "29": 0.00013123358749319095, "43": 5.305991080045182e-05} |
| Tent | Reset parameters + optimizer | 4 | ba | uci_internal_fixed | accuracy_change | 3 | 0.000325521 | 0.000563819 | {"17": 0.0009765625, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + optimizer | 4 | ba | uci_internal_fixed | error_change | 3 | -0.000325521 | 0.000563819 | {"17": -0.0009765625, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + optimizer | 4 | ba | uci_internal_fixed | nll_change | 3 | 0.000352186 | 0.00150158 | {"17": -0.00022113557472566367, "29": 0.0020559640906235473, "43": -0.0007782698996987164} |
| Tent | Reset parameters + optimizer | 4 | ba | uci_internal_fixed | brier_change | 3 | 1.16175e-05 | 0.000337031 | {"17": -8.894862440140226e-05, "29": 0.0003874845027150402, "43": -0.00026368331167398243} |
| Tent | Reset parameters + optimizer | 4 | ba | uci_internal_fixed | ece15_change | 3 | -0.00024838 | 0.000591103 | {"17": -0.000929433221129556, "29": 0.00013123358749319095, "43": 5.305991080045182e-05} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | ab | uci_internal_fixed | accuracy_change | 3 | 0.000325521 | 0.000563819 | {"17": 0.0009765625, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | ab | uci_internal_fixed | error_change | 3 | -0.000325521 | 0.000563819 | {"17": -0.0009765625, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | ab | uci_internal_fixed | nll_change | 3 | 0.000352186 | 0.00150158 | {"17": -0.00022113557472566367, "29": 0.0020559640906235473, "43": -0.0007782698996987164} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | ab | uci_internal_fixed | brier_change | 3 | 1.16175e-05 | 0.000337031 | {"17": -8.894862440140226e-05, "29": 0.0003874845027150402, "43": -0.00026368331167398243} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | ab | uci_internal_fixed | ece15_change | 3 | -0.00024838 | 0.000591103 | {"17": -0.000929433221129556, "29": 0.00013123358749319095, "43": 5.305991080045182e-05} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | ba | uci_internal_fixed | accuracy_change | 3 | 0.000325521 | 0.000563819 | {"17": 0.0009765625, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | ba | uci_internal_fixed | error_change | 3 | -0.000325521 | 0.000563819 | {"17": -0.0009765625, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | ba | uci_internal_fixed | nll_change | 3 | 0.000352186 | 0.00150158 | {"17": -0.00022113557472566367, "29": 0.0020559640906235473, "43": -0.0007782698996987164} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | ba | uci_internal_fixed | brier_change | 3 | 1.16175e-05 | 0.000337031 | {"17": -8.894862440140226e-05, "29": 0.0003874845027150402, "43": -0.00026368331167398243} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | ba | uci_internal_fixed | ece15_change | 3 | -0.00024838 | 0.000591103 | {"17": -0.000929433221129556, "29": 0.00013123358749319095, "43": 5.305991080045182e-05} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | ab | uci_internal_fixed | accuracy_change | 3 | 0.000325521 | 0.000563819 | {"17": 0.0009765625, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | ab | uci_internal_fixed | error_change | 3 | -0.000325521 | 0.000563819 | {"17": -0.0009765625, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | ab | uci_internal_fixed | nll_change | 3 | 0.000352186 | 0.00150158 | {"17": -0.00022113557472566367, "29": 0.0020559640906235473, "43": -0.0007782698996987164} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | ab | uci_internal_fixed | brier_change | 3 | 1.16175e-05 | 0.000337031 | {"17": -8.894862440140226e-05, "29": 0.0003874845027150402, "43": -0.00026368331167398243} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | ab | uci_internal_fixed | ece15_change | 3 | -0.00024838 | 0.000591103 | {"17": -0.000929433221129556, "29": 0.00013123358749319095, "43": 5.305991080045182e-05} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | ba | uci_internal_fixed | accuracy_change | 3 | 0.000325521 | 0.000563819 | {"17": 0.0009765625, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | ba | uci_internal_fixed | error_change | 3 | -0.000325521 | 0.000563819 | {"17": -0.0009765625, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | ba | uci_internal_fixed | nll_change | 3 | 0.000352186 | 0.00150158 | {"17": -0.00022113557472566367, "29": 0.0020559640906235473, "43": -0.0007782698996987164} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | ba | uci_internal_fixed | brier_change | 3 | 1.16175e-05 | 0.000337031 | {"17": -8.894862440140226e-05, "29": 0.0003874845027150402, "43": -0.00026368331167398243} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | ba | uci_internal_fixed | ece15_change | 3 | -0.00024838 | 0.000591103 | {"17": -0.000929433221129556, "29": 0.00013123358749319095, "43": 5.305991080045182e-05} |


## performance_reset_effects

| method | intervention | washout_batches | direction | metric | n_panels | mean | sd | ci95_low | ci95_high | n_seeds_min | n_seeds_max | individual_panels |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Normalization only | Reset all declared state | 0 | ab | accuracy_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Normalization only | Reset all declared state | 0 | ab | error_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Normalization only | Reset all declared state | 0 | ab | nll_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Normalization only | Reset all declared state | 0 | ab | brier_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Normalization only | Reset all declared state | 0 | ab | ece15_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Normalization only | Reset all declared state | 0 | ba | accuracy_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Normalization only | Reset all declared state | 0 | ba | error_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Normalization only | Reset all declared state | 0 | ba | nll_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Normalization only | Reset all declared state | 0 | ba | brier_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Normalization only | Reset all declared state | 0 | ba | ece15_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Normalization only | Reset all declared state | 4 | ab | accuracy_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Normalization only | Reset all declared state | 4 | ab | error_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Normalization only | Reset all declared state | 4 | ab | nll_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Normalization only | Reset all declared state | 4 | ab | brier_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Normalization only | Reset all declared state | 4 | ab | ece15_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Normalization only | Reset all declared state | 4 | ba | accuracy_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Normalization only | Reset all declared state | 4 | ba | error_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Normalization only | Reset all declared state | 4 | ba | nll_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Normalization only | Reset all declared state | 4 | ba | brier_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Normalization only | Reset all declared state | 4 | ba | ece15_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset all declared state | 0 | ab | accuracy_change | 1 | 0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0003255208333333333} |
| SAR (complete-state implementation) | Reset all declared state | 0 | ab | error_change | 1 | -0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0003255208333333333} |
| SAR (complete-state implementation) | Reset all declared state | 0 | ab | nll_change | 1 | -0.000194188 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.00019418810067130832} |
| SAR (complete-state implementation) | Reset all declared state | 0 | ab | brier_change | 1 | -0.000106313 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.00010631283052198413} |
| SAR (complete-state implementation) | Reset all declared state | 0 | ab | ece15_change | 1 | -0.000271297 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.00027129740357389846} |
| SAR (complete-state implementation) | Reset all declared state | 0 | ba | accuracy_change | 1 | 0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0003255208333333333} |
| SAR (complete-state implementation) | Reset all declared state | 0 | ba | error_change | 1 | -0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0003255208333333333} |
| SAR (complete-state implementation) | Reset all declared state | 0 | ba | nll_change | 1 | -0.000143707 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.00014370666790310938} |
| SAR (complete-state implementation) | Reset all declared state | 0 | ba | brier_change | 1 | -9.3163e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": -9.316298619527266e-05} |
| SAR (complete-state implementation) | Reset all declared state | 0 | ba | ece15_change | 1 | -0.000271433 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.00027143277058926167} |
| SAR (complete-state implementation) | Reset all declared state | 4 | ab | accuracy_change | 1 | 0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0003255208333333333} |
| SAR (complete-state implementation) | Reset all declared state | 4 | ab | error_change | 1 | -0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0003255208333333333} |
| SAR (complete-state implementation) | Reset all declared state | 4 | ab | nll_change | 1 | -0.000413649 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.00041364896663337314} |
| SAR (complete-state implementation) | Reset all declared state | 4 | ab | brier_change | 1 | -0.00013379 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0001337900261568307} |
| SAR (complete-state implementation) | Reset all declared state | 4 | ab | ece15_change | 1 | -0.000305192 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.00030519186282298066} |
| SAR (complete-state implementation) | Reset all declared state | 4 | ba | accuracy_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset all declared state | 4 | ba | error_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset all declared state | 4 | ba | nll_change | 1 | -0.000442856 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.00044285568440882717} |
| SAR (complete-state implementation) | Reset all declared state | 4 | ba | brier_change | 1 | -0.000138738 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.00013873774857026122} |
| SAR (complete-state implementation) | Reset all declared state | 4 | ba | ece15_change | 1 | 1.83189e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": 1.831890327430123e-05} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | ab | accuracy_change | 1 | 0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0003255208333333333} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | ab | error_change | 1 | -0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0003255208333333333} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | ab | nll_change | 1 | -0.000195215 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.00019521481063675938} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | ab | brier_change | 1 | -0.000106556 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.00010655575478909993} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | ab | ece15_change | 1 | -0.000270358 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0002703584752278652} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | ba | accuracy_change | 1 | 0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0003255208333333333} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | ba | error_change | 1 | -0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0003255208333333333} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | ba | nll_change | 1 | -0.000143955 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.00014395511237159236} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | ba | brier_change | 1 | -9.32687e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": -9.326865494147195e-05} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | ba | ece15_change | 1 | -0.000271247 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0002712467892422449} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | ab | accuracy_change | 1 | 0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0003255208333333333} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | ab | error_change | 1 | -0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0003255208333333333} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | ab | nll_change | 1 | -0.000413649 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.00041364896663337314} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | ab | brier_change | 1 | -0.00013379 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0001337900261568307} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | ab | ece15_change | 1 | -0.000305192 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.00030519186282298066} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | ba | accuracy_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | ba | error_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | ba | nll_change | 1 | -0.000442856 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.00044285568440882717} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | ba | brier_change | 1 | -0.000138738 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.00013873774857026122} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | ba | ece15_change | 1 | 1.83189e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": 1.831890327430123e-05} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | ab | accuracy_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | ab | error_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | ab | nll_change | 1 | 2.92039e-09 | — | — | — | 3 | 3 | {"uci_internal_fixed": 2.9203866824811797e-09} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | ab | brier_change | 1 | 5.89403e-12 | — | — | — | 3 | 3 | {"uci_internal_fixed": 5.894033525133402e-12} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | ab | ece15_change | 1 | -2.91621e-09 | — | — | — | 3 | 3 | {"uci_internal_fixed": -2.9162134833685127e-09} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | ba | accuracy_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | ba | error_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | ba | nll_change | 1 | 2.12668e-08 | — | — | — | 3 | 3 | {"uci_internal_fixed": 2.1266840566358525e-08} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | ba | brier_change | 1 | 1.10404e-08 | — | — | — | 3 | 3 | {"uci_internal_fixed": 1.1040445499950943e-08} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | ba | ece15_change | 1 | -1.15615e-08 | — | — | — | 3 | 3 | {"uci_internal_fixed": -1.156149691666312e-08} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | ab | accuracy_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | ab | error_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | ab | nll_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | ab | brier_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | ab | ece15_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | ba | accuracy_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | ba | error_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | ba | nll_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | ba | brier_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | ba | ece15_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | ab | accuracy_change | 1 | 0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0003255208333333333} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | ab | error_change | 1 | -0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0003255208333333333} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | ab | nll_change | 1 | -0.000195215 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.00019521481063675938} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | ab | brier_change | 1 | -0.000106556 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.00010655575478909993} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | ab | ece15_change | 1 | -0.000270358 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0002703584752278652} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | ba | accuracy_change | 1 | 0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0003255208333333333} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | ba | error_change | 1 | -0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0003255208333333333} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | ba | nll_change | 1 | -0.000143955 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.00014395511237159236} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | ba | brier_change | 1 | -9.32687e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": -9.326865494147195e-05} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | ba | ece15_change | 1 | -0.000271247 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0002712467892422449} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | ab | accuracy_change | 1 | 0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0003255208333333333} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | ab | error_change | 1 | -0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0003255208333333333} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | ab | nll_change | 1 | -0.000413649 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.00041364896663337314} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | ab | brier_change | 1 | -0.00013379 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0001337900261568307} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | ab | ece15_change | 1 | -0.000305192 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.00030519186282298066} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | ba | accuracy_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | ba | error_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | ba | nll_change | 1 | -0.000442856 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.00044285568440882717} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | ba | brier_change | 1 | -0.000138738 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.00013873774857026122} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | ba | ece15_change | 1 | 1.83189e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": 1.831890327430123e-05} |
| SAR (complete-state implementation) | Reset parameters only | 0 | ab | accuracy_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset parameters only | 0 | ab | error_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset parameters only | 0 | ab | nll_change | 1 | 1.06202e-06 | — | — | — | 3 | 3 | {"uci_internal_fixed": 1.062017298900329e-06} |
| SAR (complete-state implementation) | Reset parameters only | 0 | ab | brier_change | 1 | 2.42744e-07 | — | — | — | 3 | 3 | {"uci_internal_fixed": 2.427435763993624e-07} |
| SAR (complete-state implementation) | Reset parameters only | 0 | ab | ece15_change | 1 | -9.74327e-07 | — | — | — | 3 | 3 | {"uci_internal_fixed": -9.74326803900143e-07} |
| SAR (complete-state implementation) | Reset parameters only | 0 | ba | accuracy_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset parameters only | 0 | ba | error_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset parameters only | 0 | ba | nll_change | 1 | 4.74448e-07 | — | — | — | 3 | 3 | {"uci_internal_fixed": 4.7444813339990916e-07} |
| SAR (complete-state implementation) | Reset parameters only | 0 | ba | brier_change | 1 | 2.04327e-07 | — | — | — | 3 | 3 | {"uci_internal_fixed": 2.0432743689952995e-07} |
| SAR (complete-state implementation) | Reset parameters only | 0 | ba | ece15_change | 1 | -3.59169e-07 | — | — | — | 3 | 3 | {"uci_internal_fixed": -3.591692125665356e-07} |
| SAR (complete-state implementation) | Reset parameters only | 4 | ab | accuracy_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset parameters only | 4 | ab | error_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset parameters only | 4 | ab | nll_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset parameters only | 4 | ab | brier_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset parameters only | 4 | ab | ece15_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset parameters only | 4 | ba | accuracy_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset parameters only | 4 | ba | error_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset parameters only | 4 | ba | nll_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset parameters only | 4 | ba | brier_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset parameters only | 4 | ba | ece15_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | ab | accuracy_change | 1 | 0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0003255208333333333} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | ab | error_change | 1 | -0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0003255208333333333} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | ab | nll_change | 1 | -0.000194188 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.00019418810067130832} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | ab | brier_change | 1 | -0.000106313 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.00010631283052198413} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | ab | ece15_change | 1 | -0.000271297 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.00027129740357389846} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | ba | accuracy_change | 1 | 0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0003255208333333333} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | ba | error_change | 1 | -0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0003255208333333333} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | ba | nll_change | 1 | -0.000143707 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.00014370666790310938} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | ba | brier_change | 1 | -9.3163e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": -9.316298619527266e-05} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | ba | ece15_change | 1 | -0.000271433 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.00027143277058926167} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | ab | accuracy_change | 1 | 0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0003255208333333333} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | ab | error_change | 1 | -0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0003255208333333333} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | ab | nll_change | 1 | -0.000413649 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.00041364896663337314} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | ab | brier_change | 1 | -0.00013379 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0001337900261568307} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | ab | ece15_change | 1 | -0.000305192 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.00030519186282298066} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | ba | accuracy_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | ba | error_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | ba | nll_change | 1 | -0.000442856 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.00044285568440882717} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | ba | brier_change | 1 | -0.000138738 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.00013873774857026122} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | ba | ece15_change | 1 | 1.83189e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": 1.831890327430123e-05} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | ab | accuracy_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | ab | error_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | ab | nll_change | 1 | 1.06519e-06 | — | — | — | 3 | 3 | {"uci_internal_fixed": 1.0651850619510423e-06} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | ab | brier_change | 1 | 2.42756e-07 | — | — | — | 3 | 3 | {"uci_internal_fixed": 2.4275604283291913e-07} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | ab | ece15_change | 1 | -9.77488e-07 | — | — | — | 3 | 3 | {"uci_internal_fixed": -9.77488290650197e-07} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | ba | accuracy_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | ba | error_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | ba | nll_change | 1 | 4.97389e-07 | — | — | — | 3 | 3 | {"uci_internal_fixed": 4.973886014158583e-07} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | ba | brier_change | 1 | 2.1622e-07 | — | — | — | 3 | 3 | {"uci_internal_fixed": 2.1622048543279426e-07} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | ba | ece15_change | 1 | -3.72007e-07 | — | — | — | 3 | 3 | {"uci_internal_fixed": -3.720067108667462e-07} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | ab | accuracy_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | ab | error_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | ab | nll_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | ab | brier_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | ab | ece15_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | ba | accuracy_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | ba | error_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | ba | nll_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | ba | brier_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | ba | ece15_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | ab | accuracy_change | 1 | 0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0003255208333333333} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | ab | error_change | 1 | -0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0003255208333333333} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | ab | nll_change | 1 | -0.000194188 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.00019418810067130832} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | ab | brier_change | 1 | -0.000106313 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.00010631283052198413} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | ab | ece15_change | 1 | -0.000271297 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.00027129740357389846} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | ba | accuracy_change | 1 | 0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0003255208333333333} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | ba | error_change | 1 | -0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0003255208333333333} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | ba | nll_change | 1 | -0.000143707 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.00014370666790310938} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | ba | brier_change | 1 | -9.3163e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": -9.316298619527266e-05} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | ba | ece15_change | 1 | -0.000271433 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.00027143277058926167} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | ab | accuracy_change | 1 | 0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0003255208333333333} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | ab | error_change | 1 | -0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0003255208333333333} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | ab | nll_change | 1 | -0.000413649 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.00041364896663337314} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | ab | brier_change | 1 | -0.00013379 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0001337900261568307} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | ab | ece15_change | 1 | -0.000305192 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.00030519186282298066} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | ba | accuracy_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | ba | error_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | ba | nll_change | 1 | -0.000442856 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.00044285568440882717} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | ba | brier_change | 1 | -0.000138738 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.00013873774857026122} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | ba | ece15_change | 1 | 1.83189e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": 1.831890327430123e-05} |
| Source | Reset all declared state | 0 | ab | accuracy_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Source | Reset all declared state | 0 | ab | error_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Source | Reset all declared state | 0 | ab | nll_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Source | Reset all declared state | 0 | ab | brier_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Source | Reset all declared state | 0 | ab | ece15_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Source | Reset all declared state | 0 | ba | accuracy_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Source | Reset all declared state | 0 | ba | error_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Source | Reset all declared state | 0 | ba | nll_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Source | Reset all declared state | 0 | ba | brier_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Source | Reset all declared state | 0 | ba | ece15_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Source | Reset all declared state | 4 | ab | accuracy_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Source | Reset all declared state | 4 | ab | error_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Source | Reset all declared state | 4 | ab | nll_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Source | Reset all declared state | 4 | ab | brier_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Source | Reset all declared state | 4 | ab | ece15_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Source | Reset all declared state | 4 | ba | accuracy_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Source | Reset all declared state | 4 | ba | error_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Source | Reset all declared state | 4 | ba | nll_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Source | Reset all declared state | 4 | ba | brier_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Source | Reset all declared state | 4 | ba | ece15_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset all declared state | 0 | ab | accuracy_change | 1 | -0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0003255208333333333} |
| Tent | Reset all declared state | 0 | ab | error_change | 1 | 0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0003255208333333333} |
| Tent | Reset all declared state | 0 | ab | nll_change | 1 | 0.000215016 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.00021501596208271107} |
| Tent | Reset all declared state | 0 | ab | brier_change | 1 | 7.38729e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": 7.387288957783934e-05} |
| Tent | Reset all declared state | 0 | ab | ece15_change | 1 | -0.000346732 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0003467317918173692} |
| Tent | Reset all declared state | 0 | ba | accuracy_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset all declared state | 0 | ba | error_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset all declared state | 0 | ba | nll_change | 1 | 0.000241177 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.00024117701615631917} |
| Tent | Reset all declared state | 0 | ba | brier_change | 1 | 7.61083e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": 7.610830494984382e-05} |
| Tent | Reset all declared state | 0 | ba | ece15_change | 1 | -0.00049799 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.000497989544827985} |
| Tent | Reset all declared state | 4 | ab | accuracy_change | 1 | -0.000651042 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0006510416666666666} |
| Tent | Reset all declared state | 4 | ab | error_change | 1 | 0.000651042 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0006510416666666666} |
| Tent | Reset all declared state | 4 | ab | nll_change | 1 | -0.000269487 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.00026948684269213183} |
| Tent | Reset all declared state | 4 | ab | brier_change | 1 | 1.93919e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": 1.9391909065763605e-05} |
| Tent | Reset all declared state | 4 | ab | ece15_change | 1 | -0.000196834 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.00019683447095293597} |
| Tent | Reset all declared state | 4 | ba | accuracy_change | 1 | -0.000651042 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0006510416666666666} |
| Tent | Reset all declared state | 4 | ba | error_change | 1 | 0.000651042 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0006510416666666666} |
| Tent | Reset all declared state | 4 | ba | nll_change | 1 | -0.000252201 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0002522008761289829} |
| Tent | Reset all declared state | 4 | ba | brier_change | 1 | 2.09799e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": 2.0979889867147813e-05} |
| Tent | Reset all declared state | 4 | ba | ece15_change | 1 | -0.000188424 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.00018842350671653715} |
| Tent | Reset auxiliary state only | 0 | ab | accuracy_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset auxiliary state only | 0 | ab | error_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset auxiliary state only | 0 | ab | nll_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset auxiliary state only | 0 | ab | brier_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset auxiliary state only | 0 | ab | ece15_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset auxiliary state only | 0 | ba | accuracy_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset auxiliary state only | 0 | ba | error_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset auxiliary state only | 0 | ba | nll_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset auxiliary state only | 0 | ba | brier_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset auxiliary state only | 0 | ba | ece15_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset auxiliary state only | 4 | ab | accuracy_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset auxiliary state only | 4 | ab | error_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset auxiliary state only | 4 | ab | nll_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset auxiliary state only | 4 | ab | brier_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset auxiliary state only | 4 | ab | ece15_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset auxiliary state only | 4 | ba | accuracy_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset auxiliary state only | 4 | ba | error_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset auxiliary state only | 4 | ba | nll_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset auxiliary state only | 4 | ba | brier_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset auxiliary state only | 4 | ba | ece15_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset optimizer only | 0 | ab | accuracy_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset optimizer only | 0 | ab | error_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset optimizer only | 0 | ab | nll_change | 1 | 9.00478e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": 9.00478274553744e-05} |
| Tent | Reset optimizer only | 0 | ab | brier_change | 1 | 2.00659e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": 2.0065923198656077e-05} |
| Tent | Reset optimizer only | 0 | ab | ece15_change | 1 | -0.000229443 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0002294429430946991} |
| Tent | Reset optimizer only | 0 | ba | accuracy_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset optimizer only | 0 | ba | error_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset optimizer only | 0 | ba | nll_change | 1 | 5.3355e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": 5.3355028675986654e-05} |
| Tent | Reset optimizer only | 0 | ba | brier_change | 1 | 1.77092e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": 1.77092089037479e-05} |
| Tent | Reset optimizer only | 0 | ba | ece15_change | 1 | -0.000240946 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.00024094578572173646} |
| Tent | Reset optimizer only | 4 | ab | accuracy_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset optimizer only | 4 | ab | error_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset optimizer only | 4 | ab | nll_change | 1 | -0.000359118 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.000359117666994165} |
| Tent | Reset optimizer only | 4 | ab | brier_change | 1 | -4.6525e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": -4.6524994241538393e-05} |
| Tent | Reset optimizer only | 4 | ab | ece15_change | 1 | -0.000210513 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0002105132683454678} |
| Tent | Reset optimizer only | 4 | ba | accuracy_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset optimizer only | 4 | ba | error_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset optimizer only | 4 | ba | nll_change | 1 | -0.000383579 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0003835786342435016} |
| Tent | Reset optimizer only | 4 | ba | brier_change | 1 | -4.82378e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": -4.823781906123451e-05} |
| Tent | Reset optimizer only | 4 | ba | ece15_change | 1 | 1.69542e-06 | — | — | — | 3 | 3 | {"uci_internal_fixed": 1.695422320112672e-06} |
| Tent | Reset optimizer + auxiliary state | 0 | ab | accuracy_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset optimizer + auxiliary state | 0 | ab | error_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset optimizer + auxiliary state | 0 | ab | nll_change | 1 | 9.00478e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": 9.00478274553744e-05} |
| Tent | Reset optimizer + auxiliary state | 0 | ab | brier_change | 1 | 2.00659e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": 2.0065923198656077e-05} |
| Tent | Reset optimizer + auxiliary state | 0 | ab | ece15_change | 1 | -0.000229443 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0002294429430946991} |
| Tent | Reset optimizer + auxiliary state | 0 | ba | accuracy_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset optimizer + auxiliary state | 0 | ba | error_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset optimizer + auxiliary state | 0 | ba | nll_change | 1 | 5.3355e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": 5.3355028675986654e-05} |
| Tent | Reset optimizer + auxiliary state | 0 | ba | brier_change | 1 | 1.77092e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": 1.77092089037479e-05} |
| Tent | Reset optimizer + auxiliary state | 0 | ba | ece15_change | 1 | -0.000240946 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.00024094578572173646} |
| Tent | Reset optimizer + auxiliary state | 4 | ab | accuracy_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset optimizer + auxiliary state | 4 | ab | error_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset optimizer + auxiliary state | 4 | ab | nll_change | 1 | -0.000359118 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.000359117666994165} |
| Tent | Reset optimizer + auxiliary state | 4 | ab | brier_change | 1 | -4.6525e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": -4.6524994241538393e-05} |
| Tent | Reset optimizer + auxiliary state | 4 | ab | ece15_change | 1 | -0.000210513 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0002105132683454678} |
| Tent | Reset optimizer + auxiliary state | 4 | ba | accuracy_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset optimizer + auxiliary state | 4 | ba | error_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset optimizer + auxiliary state | 4 | ba | nll_change | 1 | -0.000383579 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0003835786342435016} |
| Tent | Reset optimizer + auxiliary state | 4 | ba | brier_change | 1 | -4.82378e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": -4.823781906123451e-05} |
| Tent | Reset optimizer + auxiliary state | 4 | ba | ece15_change | 1 | 1.69542e-06 | — | — | — | 3 | 3 | {"uci_internal_fixed": 1.695422320112672e-06} |
| Tent | Reset parameters only | 0 | ab | accuracy_change | 1 | -0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0003255208333333333} |
| Tent | Reset parameters only | 0 | ab | error_change | 1 | 0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0003255208333333333} |
| Tent | Reset parameters only | 0 | ab | nll_change | 1 | 0.00012424 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.00012424046499310074} |
| Tent | Reset parameters only | 0 | ab | brier_change | 1 | 5.33531e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": 5.335313796598606e-05} |
| Tent | Reset parameters only | 0 | ab | ece15_change | 1 | -0.000333953 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.00033395307627385237} |
| Tent | Reset parameters only | 0 | ba | accuracy_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset parameters only | 0 | ba | error_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset parameters only | 0 | ba | nll_change | 1 | 0.000187016 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.00018701638585204988} |
| Tent | Reset parameters only | 0 | ba | brier_change | 1 | 5.79341e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": 5.793413525729922e-05} |
| Tent | Reset parameters only | 0 | ba | ece15_change | 1 | -0.000474177 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.00047417702671551505} |
| Tent | Reset parameters only | 4 | ab | accuracy_change | 1 | -0.000651042 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0006510416666666666} |
| Tent | Reset parameters only | 4 | ab | error_change | 1 | 0.000651042 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0006510416666666666} |
| Tent | Reset parameters only | 4 | ab | nll_change | 1 | 8.68117e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": 8.681170328410832e-05} |
| Tent | Reset parameters only | 4 | ab | brier_change | 1 | 6.48172e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": 6.481721346708602e-05} |
| Tent | Reset parameters only | 4 | ab | ece15_change | 1 | -0.000143026 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.00014302645835138558} |
| Tent | Reset parameters only | 4 | ba | accuracy_change | 1 | -0.000651042 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0006510416666666666} |
| Tent | Reset parameters only | 4 | ba | error_change | 1 | 0.000651042 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0006510416666666666} |
| Tent | Reset parameters only | 4 | ba | nll_change | 1 | 0.000127802 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.00012780223363093499} |
| Tent | Reset parameters only | 4 | ba | brier_change | 1 | 6.77855e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": 6.778547330679036e-05} |
| Tent | Reset parameters only | 4 | ba | ece15_change | 1 | -0.000300974 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0003009743947377568} |
| Tent | Reset parameters + auxiliary state | 0 | ab | accuracy_change | 1 | -0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0003255208333333333} |
| Tent | Reset parameters + auxiliary state | 0 | ab | error_change | 1 | 0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0003255208333333333} |
| Tent | Reset parameters + auxiliary state | 0 | ab | nll_change | 1 | 0.00012424 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.00012424046499310074} |
| Tent | Reset parameters + auxiliary state | 0 | ab | brier_change | 1 | 5.33531e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": 5.335313796598606e-05} |
| Tent | Reset parameters + auxiliary state | 0 | ab | ece15_change | 1 | -0.000333953 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.00033395307627385237} |
| Tent | Reset parameters + auxiliary state | 0 | ba | accuracy_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset parameters + auxiliary state | 0 | ba | error_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset parameters + auxiliary state | 0 | ba | nll_change | 1 | 0.000187016 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.00018701638585204988} |
| Tent | Reset parameters + auxiliary state | 0 | ba | brier_change | 1 | 5.79341e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": 5.793413525729922e-05} |
| Tent | Reset parameters + auxiliary state | 0 | ba | ece15_change | 1 | -0.000474177 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.00047417702671551505} |
| Tent | Reset parameters + auxiliary state | 4 | ab | accuracy_change | 1 | -0.000651042 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0006510416666666666} |
| Tent | Reset parameters + auxiliary state | 4 | ab | error_change | 1 | 0.000651042 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0006510416666666666} |
| Tent | Reset parameters + auxiliary state | 4 | ab | nll_change | 1 | 8.68117e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": 8.681170328410832e-05} |
| Tent | Reset parameters + auxiliary state | 4 | ab | brier_change | 1 | 6.48172e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": 6.481721346708602e-05} |
| Tent | Reset parameters + auxiliary state | 4 | ab | ece15_change | 1 | -0.000143026 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.00014302645835138558} |
| Tent | Reset parameters + auxiliary state | 4 | ba | accuracy_change | 1 | -0.000651042 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0006510416666666666} |
| Tent | Reset parameters + auxiliary state | 4 | ba | error_change | 1 | 0.000651042 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0006510416666666666} |
| Tent | Reset parameters + auxiliary state | 4 | ba | nll_change | 1 | 0.000127802 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.00012780223363093499} |
| Tent | Reset parameters + auxiliary state | 4 | ba | brier_change | 1 | 6.77855e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": 6.778547330679036e-05} |
| Tent | Reset parameters + auxiliary state | 4 | ba | ece15_change | 1 | -0.000300974 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0003009743947377568} |
| Tent | Reset parameters + optimizer | 0 | ab | accuracy_change | 1 | -0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0003255208333333333} |
| Tent | Reset parameters + optimizer | 0 | ab | error_change | 1 | 0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0003255208333333333} |
| Tent | Reset parameters + optimizer | 0 | ab | nll_change | 1 | 0.000215016 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.00021501596208271107} |
| Tent | Reset parameters + optimizer | 0 | ab | brier_change | 1 | 7.38729e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": 7.387288957783934e-05} |
| Tent | Reset parameters + optimizer | 0 | ab | ece15_change | 1 | -0.000346732 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0003467317918173692} |
| Tent | Reset parameters + optimizer | 0 | ba | accuracy_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset parameters + optimizer | 0 | ba | error_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset parameters + optimizer | 0 | ba | nll_change | 1 | 0.000241177 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.00024117701615631917} |
| Tent | Reset parameters + optimizer | 0 | ba | brier_change | 1 | 7.61083e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": 7.610830494984382e-05} |
| Tent | Reset parameters + optimizer | 0 | ba | ece15_change | 1 | -0.00049799 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.000497989544827985} |
| Tent | Reset parameters + optimizer | 4 | ab | accuracy_change | 1 | -0.000651042 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0006510416666666666} |
| Tent | Reset parameters + optimizer | 4 | ab | error_change | 1 | 0.000651042 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0006510416666666666} |
| Tent | Reset parameters + optimizer | 4 | ab | nll_change | 1 | -0.000269487 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.00026948684269213183} |
| Tent | Reset parameters + optimizer | 4 | ab | brier_change | 1 | 1.93919e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": 1.9391909065763605e-05} |
| Tent | Reset parameters + optimizer | 4 | ab | ece15_change | 1 | -0.000196834 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.00019683447095293597} |
| Tent | Reset parameters + optimizer | 4 | ba | accuracy_change | 1 | -0.000651042 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0006510416666666666} |
| Tent | Reset parameters + optimizer | 4 | ba | error_change | 1 | 0.000651042 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0006510416666666666} |
| Tent | Reset parameters + optimizer | 4 | ba | nll_change | 1 | -0.000252201 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0002522008761289829} |
| Tent | Reset parameters + optimizer | 4 | ba | brier_change | 1 | 2.09799e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": 2.0979889867147813e-05} |
| Tent | Reset parameters + optimizer | 4 | ba | ece15_change | 1 | -0.000188424 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.00018842350671653715} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | ab | accuracy_change | 1 | -0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0003255208333333333} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | ab | error_change | 1 | 0.000325521 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0003255208333333333} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | ab | nll_change | 1 | 0.000215016 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.00021501596208271107} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | ab | brier_change | 1 | 7.38729e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": 7.387288957783934e-05} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | ab | ece15_change | 1 | -0.000346732 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0003467317918173692} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | ba | accuracy_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | ba | error_change | 1 | 0 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | ba | nll_change | 1 | 0.000241177 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.00024117701615631917} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | ba | brier_change | 1 | 7.61083e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": 7.610830494984382e-05} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | ba | ece15_change | 1 | -0.00049799 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.000497989544827985} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | ab | accuracy_change | 1 | -0.000651042 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0006510416666666666} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | ab | error_change | 1 | 0.000651042 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0006510416666666666} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | ab | nll_change | 1 | -0.000269487 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.00026948684269213183} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | ab | brier_change | 1 | 1.93919e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": 1.9391909065763605e-05} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | ab | ece15_change | 1 | -0.000196834 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.00019683447095293597} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | ba | accuracy_change | 1 | -0.000651042 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0006510416666666666} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | ba | error_change | 1 | 0.000651042 | — | — | — | 3 | 3 | {"uci_internal_fixed": 0.0006510416666666666} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | ba | nll_change | 1 | -0.000252201 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.0002522008761289829} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | ba | brier_change | 1 | 2.09799e-05 | — | — | — | 3 | 3 | {"uci_internal_fixed": 2.0979889867147813e-05} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | ba | ece15_change | 1 | -0.000188424 | — | — | — | 3 | 3 | {"uci_internal_fixed": -0.00018842350671653715} |


### performance_reset_effects: descriptive seed repetitions

The same image panel is reused across seeds. These standard deviations describe seed variability only; no confidence interval is justified from treating seeds as new image panels.

| method | intervention | washout_batches | direction | panel_id | metric | n_seeds | mean | seed_sd_descriptive | individual_seeds |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Normalization only | Reset all declared state | 0 | ab | uci_internal_fixed | accuracy_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Normalization only | Reset all declared state | 0 | ab | uci_internal_fixed | error_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Normalization only | Reset all declared state | 0 | ab | uci_internal_fixed | nll_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Normalization only | Reset all declared state | 0 | ab | uci_internal_fixed | brier_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Normalization only | Reset all declared state | 0 | ab | uci_internal_fixed | ece15_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Normalization only | Reset all declared state | 0 | ba | uci_internal_fixed | accuracy_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Normalization only | Reset all declared state | 0 | ba | uci_internal_fixed | error_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Normalization only | Reset all declared state | 0 | ba | uci_internal_fixed | nll_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Normalization only | Reset all declared state | 0 | ba | uci_internal_fixed | brier_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Normalization only | Reset all declared state | 0 | ba | uci_internal_fixed | ece15_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Normalization only | Reset all declared state | 4 | ab | uci_internal_fixed | accuracy_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Normalization only | Reset all declared state | 4 | ab | uci_internal_fixed | error_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Normalization only | Reset all declared state | 4 | ab | uci_internal_fixed | nll_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Normalization only | Reset all declared state | 4 | ab | uci_internal_fixed | brier_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Normalization only | Reset all declared state | 4 | ab | uci_internal_fixed | ece15_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Normalization only | Reset all declared state | 4 | ba | uci_internal_fixed | accuracy_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Normalization only | Reset all declared state | 4 | ba | uci_internal_fixed | error_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Normalization only | Reset all declared state | 4 | ba | uci_internal_fixed | nll_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Normalization only | Reset all declared state | 4 | ba | uci_internal_fixed | brier_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Normalization only | Reset all declared state | 4 | ba | uci_internal_fixed | ece15_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset all declared state | 0 | ab | uci_internal_fixed | accuracy_change | 3 | 0.000325521 | 0.000563819 | {"17": 0.0009765625, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset all declared state | 0 | ab | uci_internal_fixed | error_change | 3 | -0.000325521 | 0.000563819 | {"17": -0.0009765625, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset all declared state | 0 | ab | uci_internal_fixed | nll_change | 3 | -0.000194188 | 0.000887013 | {"17": -0.0004910618400646646, "29": 0.0008031839031440689, "43": -0.0008946863650933293} |
| SAR (complete-state implementation) | Reset all declared state | 0 | ab | uci_internal_fixed | brier_change | 3 | -0.000106313 | 0.000207871 | {"17": -0.00014221518589924327, "29": 0.00011717133892355514, "43": -0.00029389464459026425} |
| SAR (complete-state implementation) | Reset all declared state | 0 | ab | uci_internal_fixed | ece15_change | 3 | -0.000271297 | 0.00058943 | {"17": -0.000951688016791242, "29": 8.405521124839766e-05, "43": 5.374059482114897e-05} |
| SAR (complete-state implementation) | Reset all declared state | 0 | ba | uci_internal_fixed | accuracy_change | 3 | 0.000325521 | 0.000563819 | {"17": 0.0009765625, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset all declared state | 0 | ba | uci_internal_fixed | error_change | 3 | -0.000325521 | 0.000563819 | {"17": -0.0009765625, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset all declared state | 0 | ba | uci_internal_fixed | nll_change | 3 | -0.000143707 | 0.000863099 | {"17": -0.000333078037400486, "29": 0.0007983540754143391, "43": -0.0008963960417231812} |
| SAR (complete-state implementation) | Reset all declared state | 0 | ba | uci_internal_fixed | brier_change | 3 | -9.3163e-05 | 0.000205284 | {"17": -0.00010162510887840037, "29": 0.00011622123023259656, "43": -0.00029408507994001416} |
| SAR (complete-state implementation) | Reset all declared state | 0 | ba | uci_internal_fixed | ece15_change | 3 | -0.000271433 | 0.000591456 | {"17": -0.0009541798921191879, "29": 8.449937011745408e-05, "43": 5.538221023394883e-05} |
| SAR (complete-state implementation) | Reset all declared state | 4 | ab | uci_internal_fixed | accuracy_change | 3 | 0.000325521 | 0.000563819 | {"17": 0.0009765625, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset all declared state | 4 | ab | uci_internal_fixed | error_change | 3 | -0.000325521 | 0.000563819 | {"17": -0.0009765625, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset all declared state | 4 | ab | uci_internal_fixed | nll_change | 3 | -0.000413649 | 0.000491332 | {"17": -6.414731357873293e-05, "29": -0.00020136806718773492, "43": -0.0009754315191336516} |
| SAR (complete-state implementation) | Reset all declared state | 4 | ab | uci_internal_fixed | brier_change | 3 | -0.00013379 | 0.000155724 | {"17": -3.2919133759939934e-05, "29": -5.5311989399592365e-05, "43": -0.0003131389553109598} |
| SAR (complete-state implementation) | Reset all declared state | 4 | ab | uci_internal_fixed | ece15_change | 3 | -0.000305192 | 0.000570279 | {"17": -0.0009629625446251899, "29": -3.1554806183969886e-06, "43": 5.054243677464487e-05} |
| SAR (complete-state implementation) | Reset all declared state | 4 | ba | uci_internal_fixed | accuracy_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset all declared state | 4 | ba | uci_internal_fixed | error_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset all declared state | 4 | ba | uci_internal_fixed | nll_change | 3 | -0.000442856 | 0.00046189 | {"17": -0.00015176746690509502, "29": -0.00020136806718773492, "43": -0.0009754315191336516} |
| SAR (complete-state implementation) | Reset all declared state | 4 | ba | uci_internal_fixed | brier_change | 3 | -0.000138738 | 0.000151083 | {"17": -4.776230100023149e-05, "29": -5.5311989399592365e-05, "43": -0.0003131389553109598} |
| SAR (complete-state implementation) | Reset all declared state | 4 | ba | uci_internal_fixed | ece15_change | 3 | 1.83189e-05 | 2.8417e-05 | {"17": 7.5697536666557985e-06, "29": -3.1554806183969886e-06, "43": 5.054243677464487e-05} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | ab | uci_internal_fixed | accuracy_change | 3 | 0.000325521 | 0.000563819 | {"17": 0.0009765625, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | ab | uci_internal_fixed | error_change | 3 | -0.000325521 | 0.000563819 | {"17": -0.0009765625, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | ab | uci_internal_fixed | nll_change | 3 | -0.000195215 | 0.000888027 | {"17": -0.0004925132532894137, "29": 0.0008033184577456165, "43": -0.0008964496363664809} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | ab | uci_internal_fixed | brier_change | 3 | -0.000106556 | 0.000208072 | {"17": -0.00014285221842419253, "29": 0.00011727597935770606, "43": -0.0002940910253008133} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | ab | uci_internal_fixed | ece15_change | 3 | -0.000270358 | 0.000589219 | {"17": -0.0009505295670112924, "29": 8.402045625349741e-05, "43": 5.5433685074199324e-05} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | ba | uci_internal_fixed | accuracy_change | 3 | 0.000325521 | 0.000563819 | {"17": 0.0009765625, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | ba | uci_internal_fixed | error_change | 3 | -0.000325521 | 0.000563819 | {"17": -0.0009765625, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | ba | uci_internal_fixed | nll_change | 3 | -0.000143955 | 0.000863212 | {"17": -0.00033379054388623514, "29": 0.0007983748431379389, "43": -0.0008964496363664809} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | ba | uci_internal_fixed | brier_change | 3 | -9.32687e-05 | 0.000205304 | {"17": -0.00010195540040919965, "29": 0.00011624046088559714, "43": -0.0002940910253008133} |
| SAR (complete-state implementation) | Reset auxiliary state only | 0 | ba | uci_internal_fixed | ece15_change | 3 | -0.000271247 | 0.000591134 | {"17": -0.000953623797887538, "29": 8.444974508660386e-05, "43": 5.5433685074199324e-05} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | ab | uci_internal_fixed | accuracy_change | 3 | 0.000325521 | 0.000563819 | {"17": 0.0009765625, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | ab | uci_internal_fixed | error_change | 3 | -0.000325521 | 0.000563819 | {"17": -0.0009765625, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | ab | uci_internal_fixed | nll_change | 3 | -0.000413649 | 0.000491332 | {"17": -6.414731357873293e-05, "29": -0.00020136806718773492, "43": -0.0009754315191336516} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | ab | uci_internal_fixed | brier_change | 3 | -0.00013379 | 0.000155724 | {"17": -3.2919133759939934e-05, "29": -5.5311989399592365e-05, "43": -0.0003131389553109598} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | ab | uci_internal_fixed | ece15_change | 3 | -0.000305192 | 0.000570279 | {"17": -0.0009629625446251899, "29": -3.1554806183969886e-06, "43": 5.054243677464487e-05} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | ba | uci_internal_fixed | accuracy_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | ba | uci_internal_fixed | error_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | ba | uci_internal_fixed | nll_change | 3 | -0.000442856 | 0.00046189 | {"17": -0.00015176746690509502, "29": -0.00020136806718773492, "43": -0.0009754315191336516} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | ba | uci_internal_fixed | brier_change | 3 | -0.000138738 | 0.000151083 | {"17": -4.776230100023149e-05, "29": -5.5311989399592365e-05, "43": -0.0003131389553109598} |
| SAR (complete-state implementation) | Reset auxiliary state only | 4 | ba | uci_internal_fixed | ece15_change | 3 | 1.83189e-05 | 2.8417e-05 | {"17": 7.5697536666557985e-06, "29": -3.1554806183969886e-06, "43": 5.054243677464487e-05} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | ab | uci_internal_fixed | accuracy_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | ab | uci_internal_fixed | error_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | ab | uci_internal_fixed | nll_change | 3 | 2.92039e-09 | 5.05826e-09 | {"17": 8.761160047443539e-09, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | ab | uci_internal_fixed | brier_change | 3 | 5.89403e-12 | 1.02088e-11 | {"17": 1.7682100575400206e-11, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | ab | uci_internal_fixed | ece15_change | 3 | -2.91621e-09 | 5.05103e-09 | {"17": -8.748640450105538e-09, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | ba | uci_internal_fixed | accuracy_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | ba | uci_internal_fixed | error_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | ba | uci_internal_fixed | nll_change | 3 | 2.12668e-08 | 3.68352e-08 | {"17": 6.380052169907557e-08, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | ba | uci_internal_fixed | brier_change | 3 | 1.10404e-08 | 1.91226e-08 | {"17": 3.312133649985283e-08, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset optimizer only | 0 | ba | uci_internal_fixed | ece15_change | 3 | -1.15615e-08 | 2.00251e-08 | {"17": -3.468449074998936e-08, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | ab | uci_internal_fixed | accuracy_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | ab | uci_internal_fixed | error_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | ab | uci_internal_fixed | nll_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | ab | uci_internal_fixed | brier_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | ab | uci_internal_fixed | ece15_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | ba | uci_internal_fixed | accuracy_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | ba | uci_internal_fixed | error_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | ba | uci_internal_fixed | nll_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | ba | uci_internal_fixed | brier_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset optimizer only | 4 | ba | uci_internal_fixed | ece15_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | ab | uci_internal_fixed | accuracy_change | 3 | 0.000325521 | 0.000563819 | {"17": 0.0009765625, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | ab | uci_internal_fixed | error_change | 3 | -0.000325521 | 0.000563819 | {"17": -0.0009765625, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | ab | uci_internal_fixed | nll_change | 3 | -0.000195215 | 0.000888027 | {"17": -0.0004925132532894137, "29": 0.0008033184577456165, "43": -0.0008964496363664809} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | ab | uci_internal_fixed | brier_change | 3 | -0.000106556 | 0.000208072 | {"17": -0.00014285221842419253, "29": 0.00011727597935770606, "43": -0.0002940910253008133} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | ab | uci_internal_fixed | ece15_change | 3 | -0.000270358 | 0.000589219 | {"17": -0.0009505295670112924, "29": 8.402045625349741e-05, "43": 5.5433685074199324e-05} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | ba | uci_internal_fixed | accuracy_change | 3 | 0.000325521 | 0.000563819 | {"17": 0.0009765625, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | ba | uci_internal_fixed | error_change | 3 | -0.000325521 | 0.000563819 | {"17": -0.0009765625, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | ba | uci_internal_fixed | nll_change | 3 | -0.000143955 | 0.000863212 | {"17": -0.00033379054388623514, "29": 0.0007983748431379389, "43": -0.0008964496363664809} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | ba | uci_internal_fixed | brier_change | 3 | -9.32687e-05 | 0.000205304 | {"17": -0.00010195540040919965, "29": 0.00011624046088559714, "43": -0.0002940910253008133} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 0 | ba | uci_internal_fixed | ece15_change | 3 | -0.000271247 | 0.000591134 | {"17": -0.000953623797887538, "29": 8.444974508660386e-05, "43": 5.5433685074199324e-05} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | ab | uci_internal_fixed | accuracy_change | 3 | 0.000325521 | 0.000563819 | {"17": 0.0009765625, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | ab | uci_internal_fixed | error_change | 3 | -0.000325521 | 0.000563819 | {"17": -0.0009765625, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | ab | uci_internal_fixed | nll_change | 3 | -0.000413649 | 0.000491332 | {"17": -6.414731357873293e-05, "29": -0.00020136806718773492, "43": -0.0009754315191336516} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | ab | uci_internal_fixed | brier_change | 3 | -0.00013379 | 0.000155724 | {"17": -3.2919133759939934e-05, "29": -5.5311989399592365e-05, "43": -0.0003131389553109598} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | ab | uci_internal_fixed | ece15_change | 3 | -0.000305192 | 0.000570279 | {"17": -0.0009629625446251899, "29": -3.1554806183969886e-06, "43": 5.054243677464487e-05} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | ba | uci_internal_fixed | accuracy_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | ba | uci_internal_fixed | error_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | ba | uci_internal_fixed | nll_change | 3 | -0.000442856 | 0.00046189 | {"17": -0.00015176746690509502, "29": -0.00020136806718773492, "43": -0.0009754315191336516} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | ba | uci_internal_fixed | brier_change | 3 | -0.000138738 | 0.000151083 | {"17": -4.776230100023149e-05, "29": -5.5311989399592365e-05, "43": -0.0003131389553109598} |
| SAR (complete-state implementation) | Reset optimizer + auxiliary state | 4 | ba | uci_internal_fixed | ece15_change | 3 | 1.83189e-05 | 2.8417e-05 | {"17": 7.5697536666557985e-06, "29": -3.1554806183969886e-06, "43": 5.054243677464487e-05} |
| SAR (complete-state implementation) | Reset parameters only | 0 | ab | uci_internal_fixed | accuracy_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters only | 0 | ab | uci_internal_fixed | error_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters only | 0 | ab | uci_internal_fixed | nll_change | 3 | 1.06202e-06 | 1.04136e-06 | {"17": 1.5573352250969341e-06, "29": -1.345546015475707e-07, "43": 1.7632712731516231e-06} |
| SAR (complete-state implementation) | Reset parameters only | 0 | ab | uci_internal_fixed | brier_change | 3 | 2.42744e-07 | 3.72734e-07 | {"17": 6.364904527999399e-07, "29": -1.0464043415092661e-07, "43": 1.963807105490739e-07} |
| SAR (complete-state implementation) | Reset parameters only | 0 | ab | uci_internal_fixed | ece15_change | 3 | -9.74327e-07 | 8.99764e-07 | {"17": -1.264645153550327e-06, "29": 3.475499490025041e-08, "43": -1.6930902530503528e-06} |
| SAR (complete-state implementation) | Reset parameters only | 0 | ba | uci_internal_fixed | accuracy_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters only | 0 | ba | uci_internal_fixed | error_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters only | 0 | ba | uci_internal_fixed | nll_change | 3 | 4.74448e-07 | 7.9421e-07 | {"17": 1.3905174804998421e-06, "29": -2.0767723599851573e-08, "43": 5.3594643299736955e-08} |
| SAR (complete-state implementation) | Reset parameters only | 0 | ba | uci_internal_fixed | brier_change | 3 | 2.04327e-07 | 3.65628e-07 | {"17": 6.262676029000075e-07, "29": -1.9230653000579245e-08, "43": 5.945360799161636e-09} |
| SAR (complete-state implementation) | Reset parameters only | 0 | ba | uci_internal_fixed | ece15_change | 3 | -3.59169e-07 | 6.22553e-07 | {"17": -1.0756578282993326e-06, "29": 4.962503085022274e-08, "43": -5.147484025049692e-08} |
| SAR (complete-state implementation) | Reset parameters only | 4 | ab | uci_internal_fixed | accuracy_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters only | 4 | ab | uci_internal_fixed | error_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters only | 4 | ab | uci_internal_fixed | nll_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters only | 4 | ab | uci_internal_fixed | brier_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters only | 4 | ab | uci_internal_fixed | ece15_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters only | 4 | ba | uci_internal_fixed | accuracy_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters only | 4 | ba | uci_internal_fixed | error_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters only | 4 | ba | uci_internal_fixed | nll_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters only | 4 | ba | uci_internal_fixed | brier_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters only | 4 | ba | uci_internal_fixed | ece15_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | ab | uci_internal_fixed | accuracy_change | 3 | 0.000325521 | 0.000563819 | {"17": 0.0009765625, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | ab | uci_internal_fixed | error_change | 3 | -0.000325521 | 0.000563819 | {"17": -0.0009765625, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | ab | uci_internal_fixed | nll_change | 3 | -0.000194188 | 0.000887013 | {"17": -0.0004910618400646646, "29": 0.0008031839031440689, "43": -0.0008946863650933293} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | ab | uci_internal_fixed | brier_change | 3 | -0.000106313 | 0.000207871 | {"17": -0.00014221518589924327, "29": 0.00011717133892355514, "43": -0.00029389464459026425} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | ab | uci_internal_fixed | ece15_change | 3 | -0.000271297 | 0.00058943 | {"17": -0.000951688016791242, "29": 8.405521124839766e-05, "43": 5.374059482114897e-05} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | ba | uci_internal_fixed | accuracy_change | 3 | 0.000325521 | 0.000563819 | {"17": 0.0009765625, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | ba | uci_internal_fixed | error_change | 3 | -0.000325521 | 0.000563819 | {"17": -0.0009765625, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | ba | uci_internal_fixed | nll_change | 3 | -0.000143707 | 0.000863099 | {"17": -0.000333078037400486, "29": 0.0007983540754143391, "43": -0.0008963960417231812} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | ba | uci_internal_fixed | brier_change | 3 | -9.3163e-05 | 0.000205284 | {"17": -0.00010162510887840037, "29": 0.00011622123023259656, "43": -0.00029408507994001416} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 0 | ba | uci_internal_fixed | ece15_change | 3 | -0.000271433 | 0.000591456 | {"17": -0.0009541798921191879, "29": 8.449937011745408e-05, "43": 5.538221023394883e-05} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | ab | uci_internal_fixed | accuracy_change | 3 | 0.000325521 | 0.000563819 | {"17": 0.0009765625, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | ab | uci_internal_fixed | error_change | 3 | -0.000325521 | 0.000563819 | {"17": -0.0009765625, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | ab | uci_internal_fixed | nll_change | 3 | -0.000413649 | 0.000491332 | {"17": -6.414731357873293e-05, "29": -0.00020136806718773492, "43": -0.0009754315191336516} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | ab | uci_internal_fixed | brier_change | 3 | -0.00013379 | 0.000155724 | {"17": -3.2919133759939934e-05, "29": -5.5311989399592365e-05, "43": -0.0003131389553109598} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | ab | uci_internal_fixed | ece15_change | 3 | -0.000305192 | 0.000570279 | {"17": -0.0009629625446251899, "29": -3.1554806183969886e-06, "43": 5.054243677464487e-05} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | ba | uci_internal_fixed | accuracy_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | ba | uci_internal_fixed | error_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | ba | uci_internal_fixed | nll_change | 3 | -0.000442856 | 0.00046189 | {"17": -0.00015176746690509502, "29": -0.00020136806718773492, "43": -0.0009754315191336516} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | ba | uci_internal_fixed | brier_change | 3 | -0.000138738 | 0.000151083 | {"17": -4.776230100023149e-05, "29": -5.5311989399592365e-05, "43": -0.0003131389553109598} |
| SAR (complete-state implementation) | Reset parameters + auxiliary state | 4 | ba | uci_internal_fixed | ece15_change | 3 | 1.83189e-05 | 2.8417e-05 | {"17": 7.5697536666557985e-06, "29": -3.1554806183969886e-06, "43": 5.054243677464487e-05} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | ab | uci_internal_fixed | accuracy_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | ab | uci_internal_fixed | error_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | ab | uci_internal_fixed | nll_change | 3 | 1.06519e-06 | 1.04364e-06 | {"17": 1.5668385142490748e-06, "29": -1.345546015475707e-07, "43": 1.7632712731516231e-06} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | ab | uci_internal_fixed | brier_change | 3 | 2.42756e-07 | 3.72754e-07 | {"17": 6.365278521006101e-07, "29": -1.0464043415092661e-07, "43": 1.963807105490739e-07} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | ab | uci_internal_fixed | ece15_change | 3 | -9.77488e-07 | 9.0131e-07 | {"17": -1.2741296138004884e-06, "29": 3.475499490025041e-08, "43": -1.6930902530503528e-06} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | ba | uci_internal_fixed | accuracy_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | ba | uci_internal_fixed | error_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | ba | uci_internal_fixed | nll_change | 3 | 4.97389e-07 | 8.33903e-07 | {"17": 1.4593388845476896e-06, "29": -2.0767723599851573e-08, "43": 5.3594643299736955e-08} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | ba | uci_internal_fixed | brier_change | 3 | 2.1622e-07 | 3.86215e-07 | {"17": 6.619467484998004e-07, "29": -1.9230653000579245e-08, "43": 5.945360799161636e-09} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 0 | ba | uci_internal_fixed | ece15_change | 3 | -3.72007e-07 | 6.44717e-07 | {"17": -1.1141703231999645e-06, "29": 4.962503085022274e-08, "43": -5.147484025049692e-08} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | ab | uci_internal_fixed | accuracy_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | ab | uci_internal_fixed | error_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | ab | uci_internal_fixed | nll_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | ab | uci_internal_fixed | brier_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | ab | uci_internal_fixed | ece15_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | ba | uci_internal_fixed | accuracy_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | ba | uci_internal_fixed | error_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | ba | uci_internal_fixed | nll_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | ba | uci_internal_fixed | brier_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer | 4 | ba | uci_internal_fixed | ece15_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | ab | uci_internal_fixed | accuracy_change | 3 | 0.000325521 | 0.000563819 | {"17": 0.0009765625, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | ab | uci_internal_fixed | error_change | 3 | -0.000325521 | 0.000563819 | {"17": -0.0009765625, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | ab | uci_internal_fixed | nll_change | 3 | -0.000194188 | 0.000887013 | {"17": -0.0004910618400646646, "29": 0.0008031839031440689, "43": -0.0008946863650933293} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | ab | uci_internal_fixed | brier_change | 3 | -0.000106313 | 0.000207871 | {"17": -0.00014221518589924327, "29": 0.00011717133892355514, "43": -0.00029389464459026425} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | ab | uci_internal_fixed | ece15_change | 3 | -0.000271297 | 0.00058943 | {"17": -0.000951688016791242, "29": 8.405521124839766e-05, "43": 5.374059482114897e-05} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | ba | uci_internal_fixed | accuracy_change | 3 | 0.000325521 | 0.000563819 | {"17": 0.0009765625, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | ba | uci_internal_fixed | error_change | 3 | -0.000325521 | 0.000563819 | {"17": -0.0009765625, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | ba | uci_internal_fixed | nll_change | 3 | -0.000143707 | 0.000863099 | {"17": -0.000333078037400486, "29": 0.0007983540754143391, "43": -0.0008963960417231812} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | ba | uci_internal_fixed | brier_change | 3 | -9.3163e-05 | 0.000205284 | {"17": -0.00010162510887840037, "29": 0.00011622123023259656, "43": -0.00029408507994001416} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 0 | ba | uci_internal_fixed | ece15_change | 3 | -0.000271433 | 0.000591456 | {"17": -0.0009541798921191879, "29": 8.449937011745408e-05, "43": 5.538221023394883e-05} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | ab | uci_internal_fixed | accuracy_change | 3 | 0.000325521 | 0.000563819 | {"17": 0.0009765625, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | ab | uci_internal_fixed | error_change | 3 | -0.000325521 | 0.000563819 | {"17": -0.0009765625, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | ab | uci_internal_fixed | nll_change | 3 | -0.000413649 | 0.000491332 | {"17": -6.414731357873293e-05, "29": -0.00020136806718773492, "43": -0.0009754315191336516} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | ab | uci_internal_fixed | brier_change | 3 | -0.00013379 | 0.000155724 | {"17": -3.2919133759939934e-05, "29": -5.5311989399592365e-05, "43": -0.0003131389553109598} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | ab | uci_internal_fixed | ece15_change | 3 | -0.000305192 | 0.000570279 | {"17": -0.0009629625446251899, "29": -3.1554806183969886e-06, "43": 5.054243677464487e-05} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | ba | uci_internal_fixed | accuracy_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | ba | uci_internal_fixed | error_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | ba | uci_internal_fixed | nll_change | 3 | -0.000442856 | 0.00046189 | {"17": -0.00015176746690509502, "29": -0.00020136806718773492, "43": -0.0009754315191336516} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | ba | uci_internal_fixed | brier_change | 3 | -0.000138738 | 0.000151083 | {"17": -4.776230100023149e-05, "29": -5.5311989399592365e-05, "43": -0.0003131389553109598} |
| SAR (complete-state implementation) | Reset parameters + optimizer + auxiliary state | 4 | ba | uci_internal_fixed | ece15_change | 3 | 1.83189e-05 | 2.8417e-05 | {"17": 7.5697536666557985e-06, "29": -3.1554806183969886e-06, "43": 5.054243677464487e-05} |
| Source | Reset all declared state | 0 | ab | uci_internal_fixed | accuracy_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Source | Reset all declared state | 0 | ab | uci_internal_fixed | error_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Source | Reset all declared state | 0 | ab | uci_internal_fixed | nll_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Source | Reset all declared state | 0 | ab | uci_internal_fixed | brier_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Source | Reset all declared state | 0 | ab | uci_internal_fixed | ece15_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Source | Reset all declared state | 0 | ba | uci_internal_fixed | accuracy_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Source | Reset all declared state | 0 | ba | uci_internal_fixed | error_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Source | Reset all declared state | 0 | ba | uci_internal_fixed | nll_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Source | Reset all declared state | 0 | ba | uci_internal_fixed | brier_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Source | Reset all declared state | 0 | ba | uci_internal_fixed | ece15_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Source | Reset all declared state | 4 | ab | uci_internal_fixed | accuracy_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Source | Reset all declared state | 4 | ab | uci_internal_fixed | error_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Source | Reset all declared state | 4 | ab | uci_internal_fixed | nll_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Source | Reset all declared state | 4 | ab | uci_internal_fixed | brier_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Source | Reset all declared state | 4 | ab | uci_internal_fixed | ece15_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Source | Reset all declared state | 4 | ba | uci_internal_fixed | accuracy_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Source | Reset all declared state | 4 | ba | uci_internal_fixed | error_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Source | Reset all declared state | 4 | ba | uci_internal_fixed | nll_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Source | Reset all declared state | 4 | ba | uci_internal_fixed | brier_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Source | Reset all declared state | 4 | ba | uci_internal_fixed | ece15_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset all declared state | 0 | ab | uci_internal_fixed | accuracy_change | 3 | -0.000325521 | 0.000563819 | {"17": -0.0009765625, "29": 0.0, "43": 0.0} |
| Tent | Reset all declared state | 0 | ab | uci_internal_fixed | error_change | 3 | 0.000325521 | 0.000563819 | {"17": 0.0009765625, "29": 0.0, "43": 0.0} |
| Tent | Reset all declared state | 0 | ab | uci_internal_fixed | nll_change | 3 | 0.000215016 | 0.000511568 | {"17": 0.0004803878711087395, "29": 0.0005393690232427563, "43": -0.0003747090081033626} |
| Tent | Reset all declared state | 0 | ab | uci_internal_fixed | brier_change | 3 | 7.38729e-05 | 0.000134117 | {"17": 0.00016130286127549222, "29": 0.00014085738202890448, "43": -8.054157457087867e-05} |
| Tent | Reset all declared state | 0 | ab | uci_internal_fixed | ece15_change | 3 | -0.000346732 | 0.00065273 | {"17": 0.0004056905426994932, "29": -0.0006848410049721497, "43": -0.0007610449131794511} |
| Tent | Reset all declared state | 0 | ba | uci_internal_fixed | accuracy_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset all declared state | 0 | ba | uci_internal_fixed | error_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset all declared state | 0 | ba | uci_internal_fixed | nll_change | 3 | 0.000241177 | 0.000463634 | {"17": 0.00045743813114458923, "29": 0.0005571687102238938, "43": -0.00029107579289952557} |
| Tent | Reset all declared state | 0 | ba | uci_internal_fixed | brier_change | 3 | 7.61083e-05 | 0.000115593 | {"17": 0.00014736376997837378, "29": 0.00013822415398705504, "43": -5.726300911589738e-05} |
| Tent | Reset all declared state | 0 | ba | uci_internal_fixed | ece15_change | 3 | -0.00049799 | 0.000370643 | {"17": -7.152325872555008e-05, "29": -0.0006800576900483505, "43": -0.0007423876857100544} |
| Tent | Reset all declared state | 4 | ab | uci_internal_fixed | accuracy_change | 3 | -0.000651042 | 0.00112764 | {"17": -0.001953125, "29": 0.0, "43": 0.0} |
| Tent | Reset all declared state | 4 | ab | uci_internal_fixed | error_change | 3 | 0.000651042 | 0.00112764 | {"17": 0.001953125, "29": 0.0, "43": 0.0} |
| Tent | Reset all declared state | 4 | ab | uci_internal_fixed | nll_change | 3 | -0.000269487 | 0.00150603 | {"17": 0.0006990553863384721, "29": -0.002004581209372268, "43": 0.0004970652949574002} |
| Tent | Reset all declared state | 4 | ab | uci_internal_fixed | brier_change | 3 | 1.93919e-05 | 0.000363712 | {"17": 0.00024156248616243568, "29": -0.00040034570933880284, "43": 0.00021695895037365798} |
| Tent | Reset all declared state | 4 | ab | uci_internal_fixed | ece15_change | 3 | -0.000196834 | 0.000769296 | {"17": -0.0004494208898550064, "29": 0.0006669998860177025, "43": -0.0008080824090215041} |
| Tent | Reset all declared state | 4 | ba | uci_internal_fixed | accuracy_change | 3 | -0.000651042 | 0.00112764 | {"17": -0.001953125, "29": 0.0, "43": 0.0} |
| Tent | Reset all declared state | 4 | ba | uci_internal_fixed | error_change | 3 | 0.000651042 | 0.00112764 | {"17": 0.001953125, "29": 0.0, "43": 0.0} |
| Tent | Reset all declared state | 4 | ba | uci_internal_fixed | nll_change | 3 | -0.000252201 | 0.00150645 | {"17": 0.0006820942010309049, "29": -0.0019900558180786475, "43": 0.0005513589886607939} |
| Tent | Reset all declared state | 4 | ba | uci_internal_fixed | brier_change | 3 | 2.09799e-05 | 0.000365452 | {"17": 0.00023200596676064417, "29": -0.0004010080841780079, "43": 0.00023194178701880716} |
| Tent | Reset all declared state | 4 | ba | uci_internal_fixed | ece15_change | 3 | -0.000188424 | 0.000767496 | {"17": -0.0004435981905471006, "29": 0.0006741564848911936, "43": -0.0007958288144937044} |
| Tent | Reset auxiliary state only | 0 | ab | uci_internal_fixed | accuracy_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset auxiliary state only | 0 | ab | uci_internal_fixed | error_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset auxiliary state only | 0 | ab | uci_internal_fixed | nll_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset auxiliary state only | 0 | ab | uci_internal_fixed | brier_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset auxiliary state only | 0 | ab | uci_internal_fixed | ece15_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset auxiliary state only | 0 | ba | uci_internal_fixed | accuracy_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset auxiliary state only | 0 | ba | uci_internal_fixed | error_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset auxiliary state only | 0 | ba | uci_internal_fixed | nll_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset auxiliary state only | 0 | ba | uci_internal_fixed | brier_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset auxiliary state only | 0 | ba | uci_internal_fixed | ece15_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset auxiliary state only | 4 | ab | uci_internal_fixed | accuracy_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset auxiliary state only | 4 | ab | uci_internal_fixed | error_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset auxiliary state only | 4 | ab | uci_internal_fixed | nll_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset auxiliary state only | 4 | ab | uci_internal_fixed | brier_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset auxiliary state only | 4 | ab | uci_internal_fixed | ece15_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset auxiliary state only | 4 | ba | uci_internal_fixed | accuracy_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset auxiliary state only | 4 | ba | uci_internal_fixed | error_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset auxiliary state only | 4 | ba | uci_internal_fixed | nll_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset auxiliary state only | 4 | ba | uci_internal_fixed | brier_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset auxiliary state only | 4 | ba | uci_internal_fixed | ece15_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset optimizer only | 0 | ab | uci_internal_fixed | accuracy_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset optimizer only | 0 | ab | uci_internal_fixed | error_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset optimizer only | 0 | ab | uci_internal_fixed | nll_change | 3 | 9.00478e-05 | 0.000172256 | {"17": 7.472183245543773e-05, "29": 0.0002694547314257695, "43": -7.4033081515084e-05} |
| Tent | Reset optimizer only | 0 | ab | uci_internal_fixed | brier_change | 3 | 2.00659e-05 | 3.6391e-05 | {"17": 2.0679777849794134e-05, "29": 5.61460801517602e-05, "43": -1.6628088405586106e-05} |
| Tent | Reset optimizer only | 0 | ab | uci_internal_fixed | ece15_change | 3 | -0.000229443 | 0.000382522 | {"17": -1.2748801060052418e-05, "29": -4.464585448544708e-06, "43": -0.0006711154427755002} |
| Tent | Reset optimizer only | 0 | ba | uci_internal_fixed | accuracy_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset optimizer only | 0 | ba | uci_internal_fixed | error_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset optimizer only | 0 | ba | uci_internal_fixed | nll_change | 3 | 5.3355e-05 | 0.000219617 | {"17": 9.134037742807022e-05, "29": 0.0002515012835883172, "43": -0.00018277657498842748} |
| Tent | Reset optimizer only | 0 | ba | uci_internal_fixed | brier_change | 3 | 1.77092e-05 | 5.00086e-05 | {"17": 3.4483929417397294e-05, "29": 5.717390853355979e-05, "43": -3.853021123971338e-05} |
| Tent | Reset optimizer only | 0 | ba | uci_internal_fixed | ece15_change | 3 | -0.000240946 | 0.000361668 | {"17": -2.607282730225039e-05, "29": -0.0006585043326456036, "43": -3.8260197217355324e-05} |
| Tent | Reset optimizer only | 4 | ab | uci_internal_fixed | accuracy_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset optimizer only | 4 | ab | uci_internal_fixed | error_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset optimizer only | 4 | ab | uci_internal_fixed | nll_change | 3 | -0.000359118 | 0.00117857 | {"17": 0.00014008927566192333, "29": -0.00170512955310052, "43": 0.0004876872764561016} |
| Tent | Reset optimizer only | 4 | ab | uci_internal_fixed | brier_change | 3 | -4.6525e-05 | 0.000281556 | {"17": 5.156752972979364e-05, "29": -0.0003640058514177997, "43": 0.00017286333896339087} |
| Tent | Reset optimizer only | 4 | ab | uci_internal_fixed | ece15_change | 3 | -0.000210513 | 0.000418217 | {"17": -2.2739912805506447e-05, "29": 8.090641269990761e-05, "43": -0.0006897063049308046} |
| Tent | Reset optimizer only | 4 | ba | uci_internal_fixed | accuracy_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset optimizer only | 4 | ba | uci_internal_fixed | error_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset optimizer only | 4 | ba | uci_internal_fixed | nll_change | 3 | -0.000383579 | 0.00116033 | {"17": 0.00014891242810878558, "29": -0.0017145810022715438, "43": 0.00041493267143225335} |
| Tent | Reset optimizer only | 4 | ba | uci_internal_fixed | brier_change | 3 | -4.82378e-05 | 0.000276667 | {"17": 6.0016817582260115e-05, "29": -0.00036266392776609924, "43": 0.0001579336530001356} |
| Tent | Reset optimizer only | 4 | ba | uci_internal_fixed | ece15_change | 3 | 1.69542e-06 | 7.17836e-05 | {"17": -2.844681590155433e-05, "29": 8.363563519114652e-05, "43": -5.010255232925417e-05} |
| Tent | Reset optimizer + auxiliary state | 0 | ab | uci_internal_fixed | accuracy_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset optimizer + auxiliary state | 0 | ab | uci_internal_fixed | error_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset optimizer + auxiliary state | 0 | ab | uci_internal_fixed | nll_change | 3 | 9.00478e-05 | 0.000172256 | {"17": 7.472183245543773e-05, "29": 0.0002694547314257695, "43": -7.4033081515084e-05} |
| Tent | Reset optimizer + auxiliary state | 0 | ab | uci_internal_fixed | brier_change | 3 | 2.00659e-05 | 3.6391e-05 | {"17": 2.0679777849794134e-05, "29": 5.61460801517602e-05, "43": -1.6628088405586106e-05} |
| Tent | Reset optimizer + auxiliary state | 0 | ab | uci_internal_fixed | ece15_change | 3 | -0.000229443 | 0.000382522 | {"17": -1.2748801060052418e-05, "29": -4.464585448544708e-06, "43": -0.0006711154427755002} |
| Tent | Reset optimizer + auxiliary state | 0 | ba | uci_internal_fixed | accuracy_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset optimizer + auxiliary state | 0 | ba | uci_internal_fixed | error_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset optimizer + auxiliary state | 0 | ba | uci_internal_fixed | nll_change | 3 | 5.3355e-05 | 0.000219617 | {"17": 9.134037742807022e-05, "29": 0.0002515012835883172, "43": -0.00018277657498842748} |
| Tent | Reset optimizer + auxiliary state | 0 | ba | uci_internal_fixed | brier_change | 3 | 1.77092e-05 | 5.00086e-05 | {"17": 3.4483929417397294e-05, "29": 5.717390853355979e-05, "43": -3.853021123971338e-05} |
| Tent | Reset optimizer + auxiliary state | 0 | ba | uci_internal_fixed | ece15_change | 3 | -0.000240946 | 0.000361668 | {"17": -2.607282730225039e-05, "29": -0.0006585043326456036, "43": -3.8260197217355324e-05} |
| Tent | Reset optimizer + auxiliary state | 4 | ab | uci_internal_fixed | accuracy_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset optimizer + auxiliary state | 4 | ab | uci_internal_fixed | error_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset optimizer + auxiliary state | 4 | ab | uci_internal_fixed | nll_change | 3 | -0.000359118 | 0.00117857 | {"17": 0.00014008927566192333, "29": -0.00170512955310052, "43": 0.0004876872764561016} |
| Tent | Reset optimizer + auxiliary state | 4 | ab | uci_internal_fixed | brier_change | 3 | -4.6525e-05 | 0.000281556 | {"17": 5.156752972979364e-05, "29": -0.0003640058514177997, "43": 0.00017286333896339087} |
| Tent | Reset optimizer + auxiliary state | 4 | ab | uci_internal_fixed | ece15_change | 3 | -0.000210513 | 0.000418217 | {"17": -2.2739912805506447e-05, "29": 8.090641269990761e-05, "43": -0.0006897063049308046} |
| Tent | Reset optimizer + auxiliary state | 4 | ba | uci_internal_fixed | accuracy_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset optimizer + auxiliary state | 4 | ba | uci_internal_fixed | error_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset optimizer + auxiliary state | 4 | ba | uci_internal_fixed | nll_change | 3 | -0.000383579 | 0.00116033 | {"17": 0.00014891242810878558, "29": -0.0017145810022715438, "43": 0.00041493267143225335} |
| Tent | Reset optimizer + auxiliary state | 4 | ba | uci_internal_fixed | brier_change | 3 | -4.82378e-05 | 0.000276667 | {"17": 6.0016817582260115e-05, "29": -0.00036266392776609924, "43": 0.0001579336530001356} |
| Tent | Reset optimizer + auxiliary state | 4 | ba | uci_internal_fixed | ece15_change | 3 | 1.69542e-06 | 7.17836e-05 | {"17": -2.844681590155433e-05, "29": 8.363563519114652e-05, "43": -5.010255232925417e-05} |
| Tent | Reset parameters only | 0 | ab | uci_internal_fixed | accuracy_change | 3 | -0.000325521 | 0.000563819 | {"17": -0.0009765625, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters only | 0 | ab | uci_internal_fixed | error_change | 3 | 0.000325521 | 0.000563819 | {"17": 0.0009765625, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters only | 0 | ab | uci_internal_fixed | nll_change | 3 | 0.00012424 | 0.000375331 | {"17": 0.00040668705530130453, "29": 0.0002676951737172889, "43": -0.0003016608340392912} |
| Tent | Reset parameters only | 0 | ab | uci_internal_fixed | brier_change | 3 | 5.33531e-05 | 0.000105791 | {"17": 0.00014060357729064714, "29": 8.377016488579463e-05, "43": -6.43143282784836e-05} |
| Tent | Reset parameters only | 0 | ab | uci_internal_fixed | ece15_change | 3 | -0.000333953 | 0.000653707 | {"17": 0.0004200502771927886, "29": -0.0006802700306005926, "43": -0.0007416394754137532} |
| Tent | Reset parameters only | 0 | ba | uci_internal_fixed | accuracy_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters only | 0 | ba | uci_internal_fixed | error_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters only | 0 | ba | uci_internal_fixed | nll_change | 3 | 0.000187016 | 0.000260066 | {"17": 0.0003702523772472349, "29": 0.0003014387323953885, "43": -0.00011064195208647376} |
| Tent | Reset parameters only | 0 | ba | uci_internal_fixed | brier_change | 3 | 5.79341e-05 | 6.93063e-05 | {"17": 0.0001137222881899911, "29": 7.97303540136119e-05, "43": -1.965023643170534e-05} |
| Tent | Reset parameters only | 0 | ba | uci_internal_fixed | ece15_change | 3 | -0.000474177 | 0.000372001 | {"17": -4.503872738169899e-05, "29": -0.0006724672155006967, "43": -0.0007050251372641494} |
| Tent | Reset parameters only | 4 | ab | uci_internal_fixed | accuracy_change | 3 | -0.000651042 | 0.00112764 | {"17": -0.001953125, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters only | 4 | ab | uci_internal_fixed | error_change | 3 | 0.000651042 | 0.00112764 | {"17": 0.001953125, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters only | 4 | ab | uci_internal_fixed | nll_change | 3 | 8.68117e-05 | 0.000436751 | {"17": 0.0005583785915703153, "29": -0.0003037947705963745, "43": 5.851288878384181e-06} |
| Tent | Reset parameters only | 4 | ab | uci_internal_fixed | brier_change | 3 | 6.48172e-05 | 0.000115251 | {"17": 0.00018951731381095828, "29": -3.7784174846341306e-05, "43": 4.271850143664109e-05} |
| Tent | Reset parameters only | 4 | ab | uci_internal_fixed | ece15_change | 3 | -0.000143026 | 0.000797129 | {"17": -0.0004144778299447101, "29": 0.0007543751347996045, "43": -0.0007689766799090511} |
| Tent | Reset parameters only | 4 | ba | uci_internal_fixed | accuracy_change | 3 | -0.000651042 | 0.00112764 | {"17": -0.001953125, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters only | 4 | ba | uci_internal_fixed | error_change | 3 | 0.000651042 | 0.00112764 | {"17": 0.001953125, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters only | 4 | ba | uci_internal_fixed | nll_change | 3 | 0.000127802 | 0.000407617 | {"17": 0.0005333672163383464, "29": -0.00028183659337413167, "43": 0.00013187607792859019} |
| Tent | Reset parameters only | 4 | ba | uci_internal_fixed | brier_change | 3 | 6.77855e-05 | 0.000106095 | {"17": 0.00017160862426917126, "29": -4.044462704134652e-05, "43": 7.219242269254633e-05} |
| Tent | Reset parameters only | 4 | ba | uci_internal_fixed | ece15_change | 3 | -0.000300974 | 0.00050125 | {"17": -0.00040065561500295544, "29": 0.00024262657380574003, "43": -0.000744894143016055} |
| Tent | Reset parameters + auxiliary state | 0 | ab | uci_internal_fixed | accuracy_change | 3 | -0.000325521 | 0.000563819 | {"17": -0.0009765625, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + auxiliary state | 0 | ab | uci_internal_fixed | error_change | 3 | 0.000325521 | 0.000563819 | {"17": 0.0009765625, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + auxiliary state | 0 | ab | uci_internal_fixed | nll_change | 3 | 0.00012424 | 0.000375331 | {"17": 0.00040668705530130453, "29": 0.0002676951737172889, "43": -0.0003016608340392912} |
| Tent | Reset parameters + auxiliary state | 0 | ab | uci_internal_fixed | brier_change | 3 | 5.33531e-05 | 0.000105791 | {"17": 0.00014060357729064714, "29": 8.377016488579463e-05, "43": -6.43143282784836e-05} |
| Tent | Reset parameters + auxiliary state | 0 | ab | uci_internal_fixed | ece15_change | 3 | -0.000333953 | 0.000653707 | {"17": 0.0004200502771927886, "29": -0.0006802700306005926, "43": -0.0007416394754137532} |
| Tent | Reset parameters + auxiliary state | 0 | ba | uci_internal_fixed | accuracy_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + auxiliary state | 0 | ba | uci_internal_fixed | error_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + auxiliary state | 0 | ba | uci_internal_fixed | nll_change | 3 | 0.000187016 | 0.000260066 | {"17": 0.0003702523772472349, "29": 0.0003014387323953885, "43": -0.00011064195208647376} |
| Tent | Reset parameters + auxiliary state | 0 | ba | uci_internal_fixed | brier_change | 3 | 5.79341e-05 | 6.93063e-05 | {"17": 0.0001137222881899911, "29": 7.97303540136119e-05, "43": -1.965023643170534e-05} |
| Tent | Reset parameters + auxiliary state | 0 | ba | uci_internal_fixed | ece15_change | 3 | -0.000474177 | 0.000372001 | {"17": -4.503872738169899e-05, "29": -0.0006724672155006967, "43": -0.0007050251372641494} |
| Tent | Reset parameters + auxiliary state | 4 | ab | uci_internal_fixed | accuracy_change | 3 | -0.000651042 | 0.00112764 | {"17": -0.001953125, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + auxiliary state | 4 | ab | uci_internal_fixed | error_change | 3 | 0.000651042 | 0.00112764 | {"17": 0.001953125, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + auxiliary state | 4 | ab | uci_internal_fixed | nll_change | 3 | 8.68117e-05 | 0.000436751 | {"17": 0.0005583785915703153, "29": -0.0003037947705963745, "43": 5.851288878384181e-06} |
| Tent | Reset parameters + auxiliary state | 4 | ab | uci_internal_fixed | brier_change | 3 | 6.48172e-05 | 0.000115251 | {"17": 0.00018951731381095828, "29": -3.7784174846341306e-05, "43": 4.271850143664109e-05} |
| Tent | Reset parameters + auxiliary state | 4 | ab | uci_internal_fixed | ece15_change | 3 | -0.000143026 | 0.000797129 | {"17": -0.0004144778299447101, "29": 0.0007543751347996045, "43": -0.0007689766799090511} |
| Tent | Reset parameters + auxiliary state | 4 | ba | uci_internal_fixed | accuracy_change | 3 | -0.000651042 | 0.00112764 | {"17": -0.001953125, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + auxiliary state | 4 | ba | uci_internal_fixed | error_change | 3 | 0.000651042 | 0.00112764 | {"17": 0.001953125, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + auxiliary state | 4 | ba | uci_internal_fixed | nll_change | 3 | 0.000127802 | 0.000407617 | {"17": 0.0005333672163383464, "29": -0.00028183659337413167, "43": 0.00013187607792859019} |
| Tent | Reset parameters + auxiliary state | 4 | ba | uci_internal_fixed | brier_change | 3 | 6.77855e-05 | 0.000106095 | {"17": 0.00017160862426917126, "29": -4.044462704134652e-05, "43": 7.219242269254633e-05} |
| Tent | Reset parameters + auxiliary state | 4 | ba | uci_internal_fixed | ece15_change | 3 | -0.000300974 | 0.00050125 | {"17": -0.00040065561500295544, "29": 0.00024262657380574003, "43": -0.000744894143016055} |
| Tent | Reset parameters + optimizer | 0 | ab | uci_internal_fixed | accuracy_change | 3 | -0.000325521 | 0.000563819 | {"17": -0.0009765625, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + optimizer | 0 | ab | uci_internal_fixed | error_change | 3 | 0.000325521 | 0.000563819 | {"17": 0.0009765625, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + optimizer | 0 | ab | uci_internal_fixed | nll_change | 3 | 0.000215016 | 0.000511568 | {"17": 0.0004803878711087395, "29": 0.0005393690232427563, "43": -0.0003747090081033626} |
| Tent | Reset parameters + optimizer | 0 | ab | uci_internal_fixed | brier_change | 3 | 7.38729e-05 | 0.000134117 | {"17": 0.00016130286127549222, "29": 0.00014085738202890448, "43": -8.054157457087867e-05} |
| Tent | Reset parameters + optimizer | 0 | ab | uci_internal_fixed | ece15_change | 3 | -0.000346732 | 0.00065273 | {"17": 0.0004056905426994932, "29": -0.0006848410049721497, "43": -0.0007610449131794511} |
| Tent | Reset parameters + optimizer | 0 | ba | uci_internal_fixed | accuracy_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + optimizer | 0 | ba | uci_internal_fixed | error_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + optimizer | 0 | ba | uci_internal_fixed | nll_change | 3 | 0.000241177 | 0.000463634 | {"17": 0.00045743813114458923, "29": 0.0005571687102238938, "43": -0.00029107579289952557} |
| Tent | Reset parameters + optimizer | 0 | ba | uci_internal_fixed | brier_change | 3 | 7.61083e-05 | 0.000115593 | {"17": 0.00014736376997837378, "29": 0.00013822415398705504, "43": -5.726300911589738e-05} |
| Tent | Reset parameters + optimizer | 0 | ba | uci_internal_fixed | ece15_change | 3 | -0.00049799 | 0.000370643 | {"17": -7.152325872555008e-05, "29": -0.0006800576900483505, "43": -0.0007423876857100544} |
| Tent | Reset parameters + optimizer | 4 | ab | uci_internal_fixed | accuracy_change | 3 | -0.000651042 | 0.00112764 | {"17": -0.001953125, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + optimizer | 4 | ab | uci_internal_fixed | error_change | 3 | 0.000651042 | 0.00112764 | {"17": 0.001953125, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + optimizer | 4 | ab | uci_internal_fixed | nll_change | 3 | -0.000269487 | 0.00150603 | {"17": 0.0006990553863384721, "29": -0.002004581209372268, "43": 0.0004970652949574002} |
| Tent | Reset parameters + optimizer | 4 | ab | uci_internal_fixed | brier_change | 3 | 1.93919e-05 | 0.000363712 | {"17": 0.00024156248616243568, "29": -0.00040034570933880284, "43": 0.00021695895037365798} |
| Tent | Reset parameters + optimizer | 4 | ab | uci_internal_fixed | ece15_change | 3 | -0.000196834 | 0.000769296 | {"17": -0.0004494208898550064, "29": 0.0006669998860177025, "43": -0.0008080824090215041} |
| Tent | Reset parameters + optimizer | 4 | ba | uci_internal_fixed | accuracy_change | 3 | -0.000651042 | 0.00112764 | {"17": -0.001953125, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + optimizer | 4 | ba | uci_internal_fixed | error_change | 3 | 0.000651042 | 0.00112764 | {"17": 0.001953125, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + optimizer | 4 | ba | uci_internal_fixed | nll_change | 3 | -0.000252201 | 0.00150645 | {"17": 0.0006820942010309049, "29": -0.0019900558180786475, "43": 0.0005513589886607939} |
| Tent | Reset parameters + optimizer | 4 | ba | uci_internal_fixed | brier_change | 3 | 2.09799e-05 | 0.000365452 | {"17": 0.00023200596676064417, "29": -0.0004010080841780079, "43": 0.00023194178701880716} |
| Tent | Reset parameters + optimizer | 4 | ba | uci_internal_fixed | ece15_change | 3 | -0.000188424 | 0.000767496 | {"17": -0.0004435981905471006, "29": 0.0006741564848911936, "43": -0.0007958288144937044} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | ab | uci_internal_fixed | accuracy_change | 3 | -0.000325521 | 0.000563819 | {"17": -0.0009765625, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | ab | uci_internal_fixed | error_change | 3 | 0.000325521 | 0.000563819 | {"17": 0.0009765625, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | ab | uci_internal_fixed | nll_change | 3 | 0.000215016 | 0.000511568 | {"17": 0.0004803878711087395, "29": 0.0005393690232427563, "43": -0.0003747090081033626} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | ab | uci_internal_fixed | brier_change | 3 | 7.38729e-05 | 0.000134117 | {"17": 0.00016130286127549222, "29": 0.00014085738202890448, "43": -8.054157457087867e-05} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | ab | uci_internal_fixed | ece15_change | 3 | -0.000346732 | 0.00065273 | {"17": 0.0004056905426994932, "29": -0.0006848410049721497, "43": -0.0007610449131794511} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | ba | uci_internal_fixed | accuracy_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | ba | uci_internal_fixed | error_change | 3 | 0 | 0 | {"17": 0.0, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | ba | uci_internal_fixed | nll_change | 3 | 0.000241177 | 0.000463634 | {"17": 0.00045743813114458923, "29": 0.0005571687102238938, "43": -0.00029107579289952557} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | ba | uci_internal_fixed | brier_change | 3 | 7.61083e-05 | 0.000115593 | {"17": 0.00014736376997837378, "29": 0.00013822415398705504, "43": -5.726300911589738e-05} |
| Tent | Reset parameters + optimizer + auxiliary state | 0 | ba | uci_internal_fixed | ece15_change | 3 | -0.00049799 | 0.000370643 | {"17": -7.152325872555008e-05, "29": -0.0006800576900483505, "43": -0.0007423876857100544} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | ab | uci_internal_fixed | accuracy_change | 3 | -0.000651042 | 0.00112764 | {"17": -0.001953125, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | ab | uci_internal_fixed | error_change | 3 | 0.000651042 | 0.00112764 | {"17": 0.001953125, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | ab | uci_internal_fixed | nll_change | 3 | -0.000269487 | 0.00150603 | {"17": 0.0006990553863384721, "29": -0.002004581209372268, "43": 0.0004970652949574002} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | ab | uci_internal_fixed | brier_change | 3 | 1.93919e-05 | 0.000363712 | {"17": 0.00024156248616243568, "29": -0.00040034570933880284, "43": 0.00021695895037365798} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | ab | uci_internal_fixed | ece15_change | 3 | -0.000196834 | 0.000769296 | {"17": -0.0004494208898550064, "29": 0.0006669998860177025, "43": -0.0008080824090215041} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | ba | uci_internal_fixed | accuracy_change | 3 | -0.000651042 | 0.00112764 | {"17": -0.001953125, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | ba | uci_internal_fixed | error_change | 3 | 0.000651042 | 0.00112764 | {"17": 0.001953125, "29": 0.0, "43": 0.0} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | ba | uci_internal_fixed | nll_change | 3 | -0.000252201 | 0.00150645 | {"17": 0.0006820942010309049, "29": -0.0019900558180786475, "43": 0.0005513589886607939} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | ba | uci_internal_fixed | brier_change | 3 | 2.09799e-05 | 0.000365452 | {"17": 0.00023200596676064417, "29": -0.0004010080841780079, "43": 0.00023194178701880716} |
| Tent | Reset parameters + optimizer + auxiliary state | 4 | ba | uci_internal_fixed | ece15_change | 3 | -0.000188424 | 0.000767496 | {"17": -0.0004435981905471006, "29": 0.0006741564848911936, "43": -0.0007958288144937044} |


## Deterministic controls

| id | passed | max_logit_diff |
| --- | --- | --- |
| 17_uci_internal_fixed_noise_brightness_to_blur_source_w0_none_ab_snapshot_replay | True | 0 |
| 17_uci_internal_fixed_noise_brightness_to_blur_source_w0_none_ab_full_replay | True | 0 |
| 17_uci_internal_fixed_noise_brightness_to_blur_source_w0_none_ba_snapshot_replay | True | 0 |
| 17_uci_internal_fixed_noise_brightness_to_blur_source_w0_none_ba_full_replay | True | 0 |
| 17_uci_internal_fixed_noise_brightness_to_blur_source_w0_none_history_invariance | True | 0 |
| 17_uci_internal_fixed_noise_brightness_to_blur_source_w0_all_ab_cold_reset | True | 0 |
| 17_uci_internal_fixed_noise_brightness_to_blur_source_w0_all_ba_cold_reset | True | 0 |
| 17_uci_internal_fixed_noise_brightness_to_blur_source_w0_all_history_invariance | True | 0 |
| 17_uci_internal_fixed_noise_brightness_to_blur_source_w0_all_first_batch | True | 0 |
| 17_uci_internal_fixed_noise_brightness_to_blur_source_w4_none_history_invariance | True | 0 |
| 17_uci_internal_fixed_noise_brightness_to_blur_source_w4_all_ab_cold_reset | True | 0 |
| 17_uci_internal_fixed_noise_brightness_to_blur_source_w4_all_ba_cold_reset | True | 0 |
| 17_uci_internal_fixed_noise_brightness_to_blur_source_w4_all_history_invariance | True | 0 |
| 17_uci_internal_fixed_noise_brightness_to_blur_source_w4_all_first_batch | True | 0 |
| 17_uci_internal_fixed_noise_brightness_to_blur_norm_w0_none_ab_snapshot_replay | True | 0 |
| 17_uci_internal_fixed_noise_brightness_to_blur_norm_w0_none_ab_full_replay | True | 0 |
| 17_uci_internal_fixed_noise_brightness_to_blur_norm_w0_none_ba_snapshot_replay | True | 0 |
| 17_uci_internal_fixed_noise_brightness_to_blur_norm_w0_none_ba_full_replay | True | 0 |
| 17_uci_internal_fixed_noise_brightness_to_blur_norm_w0_none_history_invariance | True | 0 |
| 17_uci_internal_fixed_noise_brightness_to_blur_norm_w0_all_ab_cold_reset | True | 0 |
| 17_uci_internal_fixed_noise_brightness_to_blur_norm_w0_all_ba_cold_reset | True | 0 |
| 17_uci_internal_fixed_noise_brightness_to_blur_norm_w0_all_history_invariance | True | 0 |
| 17_uci_internal_fixed_noise_brightness_to_blur_norm_w0_all_first_batch | True | 0 |
| 17_uci_internal_fixed_noise_brightness_to_blur_norm_w4_none_history_invariance | True | 0 |
| 17_uci_internal_fixed_noise_brightness_to_blur_norm_w4_all_ab_cold_reset | True | 0 |
| 17_uci_internal_fixed_noise_brightness_to_blur_norm_w4_all_ba_cold_reset | True | 0 |
| 17_uci_internal_fixed_noise_brightness_to_blur_norm_w4_all_history_invariance | True | 0 |
| 17_uci_internal_fixed_noise_brightness_to_blur_norm_w4_all_first_batch | True | 0 |
| 17_uci_internal_fixed_noise_brightness_to_blur_tent_w0_none_ab_snapshot_replay | True | 0 |
| 17_uci_internal_fixed_noise_brightness_to_blur_tent_w0_none_ab_full_replay | True | 0 |
| 17_uci_internal_fixed_noise_brightness_to_blur_tent_w0_none_ba_snapshot_replay | True | 0 |
| 17_uci_internal_fixed_noise_brightness_to_blur_tent_w0_none_ba_full_replay | True | 0 |
| 17_uci_internal_fixed_noise_brightness_to_blur_tent_w0_parameters_first_batch | True | 0 |
| 17_uci_internal_fixed_noise_brightness_to_blur_tent_w0_parameters_optimizer_first_batch | True | 0 |
| 17_uci_internal_fixed_noise_brightness_to_blur_tent_w0_parameters_aux_first_batch | True | 0 |
| 17_uci_internal_fixed_noise_brightness_to_blur_tent_w0_parameters_optimizer_aux_first_batch | True | 0 |
| 17_uci_internal_fixed_noise_brightness_to_blur_tent_w0_all_ab_cold_reset | True | 0 |
| 17_uci_internal_fixed_noise_brightness_to_blur_tent_w0_all_ba_cold_reset | True | 0 |
| 17_uci_internal_fixed_noise_brightness_to_blur_tent_w0_all_history_invariance | True | 0 |
| 17_uci_internal_fixed_noise_brightness_to_blur_tent_w0_all_first_batch | True | 0 |
| 17_uci_internal_fixed_noise_brightness_to_blur_tent_w4_parameters_first_batch | True | 0 |
| 17_uci_internal_fixed_noise_brightness_to_blur_tent_w4_parameters_optimizer_first_batch | True | 0 |
| 17_uci_internal_fixed_noise_brightness_to_blur_tent_w4_parameters_aux_first_batch | True | 0 |
| 17_uci_internal_fixed_noise_brightness_to_blur_tent_w4_parameters_optimizer_aux_first_batch | True | 0 |
| 17_uci_internal_fixed_noise_brightness_to_blur_tent_w4_all_ab_cold_reset | True | 0 |
| 17_uci_internal_fixed_noise_brightness_to_blur_tent_w4_all_ba_cold_reset | True | 0 |
| 17_uci_internal_fixed_noise_brightness_to_blur_tent_w4_all_history_invariance | True | 0 |
| 17_uci_internal_fixed_noise_brightness_to_blur_tent_w4_all_first_batch | True | 0 |
| 17_uci_internal_fixed_noise_brightness_to_blur_sar_complete_w0_none_ab_snapshot_replay | True | 0 |
| 17_uci_internal_fixed_noise_brightness_to_blur_sar_complete_w0_none_ab_full_replay | True | 0 |
| 17_uci_internal_fixed_noise_brightness_to_blur_sar_complete_w0_none_ba_snapshot_replay | True | 0 |
| 17_uci_internal_fixed_noise_brightness_to_blur_sar_complete_w0_none_ba_full_replay | True | 0 |
| 17_uci_internal_fixed_noise_brightness_to_blur_sar_complete_w0_parameters_first_batch | True | 0 |
| 17_uci_internal_fixed_noise_brightness_to_blur_sar_complete_w0_parameters_optimizer_first_batch | True | 0 |
| 17_uci_internal_fixed_noise_brightness_to_blur_sar_complete_w0_parameters_aux_first_batch | True | 0 |
| 17_uci_internal_fixed_noise_brightness_to_blur_sar_complete_w0_parameters_optimizer_aux_first_batch | True | 0 |
| 17_uci_internal_fixed_noise_brightness_to_blur_sar_complete_w0_all_ab_cold_reset | True | 0 |
| 17_uci_internal_fixed_noise_brightness_to_blur_sar_complete_w0_all_ba_cold_reset | True | 0 |
| 17_uci_internal_fixed_noise_brightness_to_blur_sar_complete_w0_all_history_invariance | True | 0 |
| 17_uci_internal_fixed_noise_brightness_to_blur_sar_complete_w0_all_first_batch | True | 0 |
| 17_uci_internal_fixed_noise_brightness_to_blur_sar_complete_w4_parameters_first_batch | True | 0 |
| 17_uci_internal_fixed_noise_brightness_to_blur_sar_complete_w4_parameters_optimizer_first_batch | True | 0 |
| 17_uci_internal_fixed_noise_brightness_to_blur_sar_complete_w4_parameters_aux_first_batch | True | 0 |
| 17_uci_internal_fixed_noise_brightness_to_blur_sar_complete_w4_parameters_optimizer_aux_first_batch | True | 0 |
| 17_uci_internal_fixed_noise_brightness_to_blur_sar_complete_w4_all_ab_cold_reset | True | 0 |
| 17_uci_internal_fixed_noise_brightness_to_blur_sar_complete_w4_all_ba_cold_reset | True | 0 |
| 17_uci_internal_fixed_noise_brightness_to_blur_sar_complete_w4_all_history_invariance | True | 0 |
| 17_uci_internal_fixed_noise_brightness_to_blur_sar_complete_w4_all_first_batch | True | 0 |
| 17_uci_internal_fixed_blur_noise_to_clean_source_w0_none_ab_snapshot_replay | True | 0 |
| 17_uci_internal_fixed_blur_noise_to_clean_source_w0_none_ab_full_replay | True | 0 |
| 17_uci_internal_fixed_blur_noise_to_clean_source_w0_none_ba_snapshot_replay | True | 0 |
| 17_uci_internal_fixed_blur_noise_to_clean_source_w0_none_ba_full_replay | True | 0 |
| 17_uci_internal_fixed_blur_noise_to_clean_source_w0_none_history_invariance | True | 0 |
| 17_uci_internal_fixed_blur_noise_to_clean_source_w0_all_ab_cold_reset | True | 0 |
| 17_uci_internal_fixed_blur_noise_to_clean_source_w0_all_ba_cold_reset | True | 0 |
| 17_uci_internal_fixed_blur_noise_to_clean_source_w0_all_history_invariance | True | 0 |
| 17_uci_internal_fixed_blur_noise_to_clean_source_w0_all_first_batch | True | 0 |
| 17_uci_internal_fixed_blur_noise_to_clean_source_w4_none_history_invariance | True | 0 |
| 17_uci_internal_fixed_blur_noise_to_clean_source_w4_all_ab_cold_reset | True | 0 |
| 17_uci_internal_fixed_blur_noise_to_clean_source_w4_all_ba_cold_reset | True | 0 |
| 17_uci_internal_fixed_blur_noise_to_clean_source_w4_all_history_invariance | True | 0 |
| 17_uci_internal_fixed_blur_noise_to_clean_source_w4_all_first_batch | True | 0 |
| 17_uci_internal_fixed_blur_noise_to_clean_norm_w0_none_ab_snapshot_replay | True | 0 |
| 17_uci_internal_fixed_blur_noise_to_clean_norm_w0_none_ab_full_replay | True | 0 |
| 17_uci_internal_fixed_blur_noise_to_clean_norm_w0_none_ba_snapshot_replay | True | 0 |
| 17_uci_internal_fixed_blur_noise_to_clean_norm_w0_none_ba_full_replay | True | 0 |
| 17_uci_internal_fixed_blur_noise_to_clean_norm_w0_none_history_invariance | True | 0 |
| 17_uci_internal_fixed_blur_noise_to_clean_norm_w0_all_ab_cold_reset | True | 0 |
| 17_uci_internal_fixed_blur_noise_to_clean_norm_w0_all_ba_cold_reset | True | 0 |
| 17_uci_internal_fixed_blur_noise_to_clean_norm_w0_all_history_invariance | True | 0 |
| 17_uci_internal_fixed_blur_noise_to_clean_norm_w0_all_first_batch | True | 0 |
| 17_uci_internal_fixed_blur_noise_to_clean_norm_w4_none_history_invariance | True | 0 |
| 17_uci_internal_fixed_blur_noise_to_clean_norm_w4_all_ab_cold_reset | True | 0 |
| 17_uci_internal_fixed_blur_noise_to_clean_norm_w4_all_ba_cold_reset | True | 0 |
| 17_uci_internal_fixed_blur_noise_to_clean_norm_w4_all_history_invariance | True | 0 |
| 17_uci_internal_fixed_blur_noise_to_clean_norm_w4_all_first_batch | True | 0 |
| 17_uci_internal_fixed_blur_noise_to_clean_tent_w0_none_ab_snapshot_replay | True | 0 |
| 17_uci_internal_fixed_blur_noise_to_clean_tent_w0_none_ab_full_replay | True | 0 |
| 17_uci_internal_fixed_blur_noise_to_clean_tent_w0_none_ba_snapshot_replay | True | 0 |
| 17_uci_internal_fixed_blur_noise_to_clean_tent_w0_none_ba_full_replay | True | 0 |
| 17_uci_internal_fixed_blur_noise_to_clean_tent_w0_parameters_first_batch | True | 0 |
| 17_uci_internal_fixed_blur_noise_to_clean_tent_w0_parameters_optimizer_first_batch | True | 0 |
| 17_uci_internal_fixed_blur_noise_to_clean_tent_w0_parameters_aux_first_batch | True | 0 |
| 17_uci_internal_fixed_blur_noise_to_clean_tent_w0_parameters_optimizer_aux_first_batch | True | 0 |
| 17_uci_internal_fixed_blur_noise_to_clean_tent_w0_all_ab_cold_reset | True | 0 |
| 17_uci_internal_fixed_blur_noise_to_clean_tent_w0_all_ba_cold_reset | True | 0 |
| 17_uci_internal_fixed_blur_noise_to_clean_tent_w0_all_history_invariance | True | 0 |
| 17_uci_internal_fixed_blur_noise_to_clean_tent_w0_all_first_batch | True | 0 |
| 17_uci_internal_fixed_blur_noise_to_clean_tent_w4_parameters_first_batch | True | 0 |
| 17_uci_internal_fixed_blur_noise_to_clean_tent_w4_parameters_optimizer_first_batch | True | 0 |
| 17_uci_internal_fixed_blur_noise_to_clean_tent_w4_parameters_aux_first_batch | True | 0 |
| 17_uci_internal_fixed_blur_noise_to_clean_tent_w4_parameters_optimizer_aux_first_batch | True | 0 |
| 17_uci_internal_fixed_blur_noise_to_clean_tent_w4_all_ab_cold_reset | True | 0 |
| 17_uci_internal_fixed_blur_noise_to_clean_tent_w4_all_ba_cold_reset | True | 0 |
| 17_uci_internal_fixed_blur_noise_to_clean_tent_w4_all_history_invariance | True | 0 |
| 17_uci_internal_fixed_blur_noise_to_clean_tent_w4_all_first_batch | True | 0 |
| 17_uci_internal_fixed_blur_noise_to_clean_sar_complete_w0_none_ab_snapshot_replay | True | 0 |
| 17_uci_internal_fixed_blur_noise_to_clean_sar_complete_w0_none_ab_full_replay | True | 0 |
| 17_uci_internal_fixed_blur_noise_to_clean_sar_complete_w0_none_ba_snapshot_replay | True | 0 |
| 17_uci_internal_fixed_blur_noise_to_clean_sar_complete_w0_none_ba_full_replay | True | 0 |
| 17_uci_internal_fixed_blur_noise_to_clean_sar_complete_w0_parameters_first_batch | True | 0 |
| 17_uci_internal_fixed_blur_noise_to_clean_sar_complete_w0_parameters_optimizer_first_batch | True | 0 |
| 17_uci_internal_fixed_blur_noise_to_clean_sar_complete_w0_parameters_aux_first_batch | True | 0 |
| 17_uci_internal_fixed_blur_noise_to_clean_sar_complete_w0_parameters_optimizer_aux_first_batch | True | 0 |
| 17_uci_internal_fixed_blur_noise_to_clean_sar_complete_w0_all_ab_cold_reset | True | 0 |
| 17_uci_internal_fixed_blur_noise_to_clean_sar_complete_w0_all_ba_cold_reset | True | 0 |
| 17_uci_internal_fixed_blur_noise_to_clean_sar_complete_w0_all_history_invariance | True | 0 |
| 17_uci_internal_fixed_blur_noise_to_clean_sar_complete_w0_all_first_batch | True | 0 |
| 17_uci_internal_fixed_blur_noise_to_clean_sar_complete_w4_parameters_first_batch | True | 0 |
| 17_uci_internal_fixed_blur_noise_to_clean_sar_complete_w4_parameters_optimizer_first_batch | True | 0 |
| 17_uci_internal_fixed_blur_noise_to_clean_sar_complete_w4_parameters_aux_first_batch | True | 0 |
| 17_uci_internal_fixed_blur_noise_to_clean_sar_complete_w4_parameters_optimizer_aux_first_batch | True | 0 |
| 17_uci_internal_fixed_blur_noise_to_clean_sar_complete_w4_all_ab_cold_reset | True | 0 |
| 17_uci_internal_fixed_blur_noise_to_clean_sar_complete_w4_all_ba_cold_reset | True | 0 |
| 17_uci_internal_fixed_blur_noise_to_clean_sar_complete_w4_all_history_invariance | True | 0 |
| 17_uci_internal_fixed_blur_noise_to_clean_sar_complete_w4_all_first_batch | True | 0 |
| 29_uci_internal_fixed_noise_brightness_to_blur_source_w0_none_ab_snapshot_replay | True | 0 |
| 29_uci_internal_fixed_noise_brightness_to_blur_source_w0_none_ab_full_replay | True | 0 |
| 29_uci_internal_fixed_noise_brightness_to_blur_source_w0_none_ba_snapshot_replay | True | 0 |
| 29_uci_internal_fixed_noise_brightness_to_blur_source_w0_none_ba_full_replay | True | 0 |
| 29_uci_internal_fixed_noise_brightness_to_blur_source_w0_none_history_invariance | True | 0 |
| 29_uci_internal_fixed_noise_brightness_to_blur_source_w0_all_ab_cold_reset | True | 0 |
| 29_uci_internal_fixed_noise_brightness_to_blur_source_w0_all_ba_cold_reset | True | 0 |
| 29_uci_internal_fixed_noise_brightness_to_blur_source_w0_all_history_invariance | True | 0 |
| 29_uci_internal_fixed_noise_brightness_to_blur_source_w0_all_first_batch | True | 0 |
| 29_uci_internal_fixed_noise_brightness_to_blur_source_w4_none_history_invariance | True | 0 |
| 29_uci_internal_fixed_noise_brightness_to_blur_source_w4_all_ab_cold_reset | True | 0 |
| 29_uci_internal_fixed_noise_brightness_to_blur_source_w4_all_ba_cold_reset | True | 0 |
| 29_uci_internal_fixed_noise_brightness_to_blur_source_w4_all_history_invariance | True | 0 |
| 29_uci_internal_fixed_noise_brightness_to_blur_source_w4_all_first_batch | True | 0 |
| 29_uci_internal_fixed_noise_brightness_to_blur_norm_w0_none_ab_snapshot_replay | True | 0 |
| 29_uci_internal_fixed_noise_brightness_to_blur_norm_w0_none_ab_full_replay | True | 0 |
| 29_uci_internal_fixed_noise_brightness_to_blur_norm_w0_none_ba_snapshot_replay | True | 0 |
| 29_uci_internal_fixed_noise_brightness_to_blur_norm_w0_none_ba_full_replay | True | 0 |
| 29_uci_internal_fixed_noise_brightness_to_blur_norm_w0_none_history_invariance | True | 0 |
| 29_uci_internal_fixed_noise_brightness_to_blur_norm_w0_all_ab_cold_reset | True | 0 |
| 29_uci_internal_fixed_noise_brightness_to_blur_norm_w0_all_ba_cold_reset | True | 0 |
| 29_uci_internal_fixed_noise_brightness_to_blur_norm_w0_all_history_invariance | True | 0 |
| 29_uci_internal_fixed_noise_brightness_to_blur_norm_w0_all_first_batch | True | 0 |
| 29_uci_internal_fixed_noise_brightness_to_blur_norm_w4_none_history_invariance | True | 0 |
| 29_uci_internal_fixed_noise_brightness_to_blur_norm_w4_all_ab_cold_reset | True | 0 |
| 29_uci_internal_fixed_noise_brightness_to_blur_norm_w4_all_ba_cold_reset | True | 0 |
| 29_uci_internal_fixed_noise_brightness_to_blur_norm_w4_all_history_invariance | True | 0 |
| 29_uci_internal_fixed_noise_brightness_to_blur_norm_w4_all_first_batch | True | 0 |
| 29_uci_internal_fixed_noise_brightness_to_blur_tent_w0_none_ab_snapshot_replay | True | 0 |
| 29_uci_internal_fixed_noise_brightness_to_blur_tent_w0_none_ab_full_replay | True | 0 |
| 29_uci_internal_fixed_noise_brightness_to_blur_tent_w0_none_ba_snapshot_replay | True | 0 |
| 29_uci_internal_fixed_noise_brightness_to_blur_tent_w0_none_ba_full_replay | True | 0 |
| 29_uci_internal_fixed_noise_brightness_to_blur_tent_w0_parameters_first_batch | True | 0 |
| 29_uci_internal_fixed_noise_brightness_to_blur_tent_w0_parameters_optimizer_first_batch | True | 0 |
| 29_uci_internal_fixed_noise_brightness_to_blur_tent_w0_parameters_aux_first_batch | True | 0 |
| 29_uci_internal_fixed_noise_brightness_to_blur_tent_w0_parameters_optimizer_aux_first_batch | True | 0 |
| 29_uci_internal_fixed_noise_brightness_to_blur_tent_w0_all_ab_cold_reset | True | 0 |
| 29_uci_internal_fixed_noise_brightness_to_blur_tent_w0_all_ba_cold_reset | True | 0 |
| 29_uci_internal_fixed_noise_brightness_to_blur_tent_w0_all_history_invariance | True | 0 |
| 29_uci_internal_fixed_noise_brightness_to_blur_tent_w0_all_first_batch | True | 0 |
| 29_uci_internal_fixed_noise_brightness_to_blur_tent_w4_parameters_first_batch | True | 0 |
| 29_uci_internal_fixed_noise_brightness_to_blur_tent_w4_parameters_optimizer_first_batch | True | 0 |
| 29_uci_internal_fixed_noise_brightness_to_blur_tent_w4_parameters_aux_first_batch | True | 0 |
| 29_uci_internal_fixed_noise_brightness_to_blur_tent_w4_parameters_optimizer_aux_first_batch | True | 0 |
| 29_uci_internal_fixed_noise_brightness_to_blur_tent_w4_all_ab_cold_reset | True | 0 |
| 29_uci_internal_fixed_noise_brightness_to_blur_tent_w4_all_ba_cold_reset | True | 0 |
| 29_uci_internal_fixed_noise_brightness_to_blur_tent_w4_all_history_invariance | True | 0 |
| 29_uci_internal_fixed_noise_brightness_to_blur_tent_w4_all_first_batch | True | 0 |
| 29_uci_internal_fixed_noise_brightness_to_blur_sar_complete_w0_none_ab_snapshot_replay | True | 0 |
| 29_uci_internal_fixed_noise_brightness_to_blur_sar_complete_w0_none_ab_full_replay | True | 0 |
| 29_uci_internal_fixed_noise_brightness_to_blur_sar_complete_w0_none_ba_snapshot_replay | True | 0 |
| 29_uci_internal_fixed_noise_brightness_to_blur_sar_complete_w0_none_ba_full_replay | True | 0 |
| 29_uci_internal_fixed_noise_brightness_to_blur_sar_complete_w0_parameters_first_batch | True | 0 |
| 29_uci_internal_fixed_noise_brightness_to_blur_sar_complete_w0_parameters_optimizer_first_batch | True | 0 |
| 29_uci_internal_fixed_noise_brightness_to_blur_sar_complete_w0_parameters_aux_first_batch | True | 0 |
| 29_uci_internal_fixed_noise_brightness_to_blur_sar_complete_w0_parameters_optimizer_aux_first_batch | True | 0 |
| 29_uci_internal_fixed_noise_brightness_to_blur_sar_complete_w0_all_ab_cold_reset | True | 0 |
| 29_uci_internal_fixed_noise_brightness_to_blur_sar_complete_w0_all_ba_cold_reset | True | 0 |
| 29_uci_internal_fixed_noise_brightness_to_blur_sar_complete_w0_all_history_invariance | True | 0 |
| 29_uci_internal_fixed_noise_brightness_to_blur_sar_complete_w0_all_first_batch | True | 0 |
| 29_uci_internal_fixed_noise_brightness_to_blur_sar_complete_w4_parameters_first_batch | True | 0 |
| 29_uci_internal_fixed_noise_brightness_to_blur_sar_complete_w4_parameters_optimizer_first_batch | True | 0 |
| 29_uci_internal_fixed_noise_brightness_to_blur_sar_complete_w4_parameters_aux_first_batch | True | 0 |
| 29_uci_internal_fixed_noise_brightness_to_blur_sar_complete_w4_parameters_optimizer_aux_first_batch | True | 0 |
| 29_uci_internal_fixed_noise_brightness_to_blur_sar_complete_w4_all_ab_cold_reset | True | 0 |
| 29_uci_internal_fixed_noise_brightness_to_blur_sar_complete_w4_all_ba_cold_reset | True | 0 |
| 29_uci_internal_fixed_noise_brightness_to_blur_sar_complete_w4_all_history_invariance | True | 0 |
| 29_uci_internal_fixed_noise_brightness_to_blur_sar_complete_w4_all_first_batch | True | 0 |
| 29_uci_internal_fixed_blur_noise_to_clean_source_w0_none_ab_snapshot_replay | True | 0 |
| 29_uci_internal_fixed_blur_noise_to_clean_source_w0_none_ab_full_replay | True | 0 |
| 29_uci_internal_fixed_blur_noise_to_clean_source_w0_none_ba_snapshot_replay | True | 0 |
| 29_uci_internal_fixed_blur_noise_to_clean_source_w0_none_ba_full_replay | True | 0 |
| 29_uci_internal_fixed_blur_noise_to_clean_source_w0_none_history_invariance | True | 0 |
| 29_uci_internal_fixed_blur_noise_to_clean_source_w0_all_ab_cold_reset | True | 0 |
| 29_uci_internal_fixed_blur_noise_to_clean_source_w0_all_ba_cold_reset | True | 0 |
| 29_uci_internal_fixed_blur_noise_to_clean_source_w0_all_history_invariance | True | 0 |
| 29_uci_internal_fixed_blur_noise_to_clean_source_w0_all_first_batch | True | 0 |
| 29_uci_internal_fixed_blur_noise_to_clean_source_w4_none_history_invariance | True | 0 |
| 29_uci_internal_fixed_blur_noise_to_clean_source_w4_all_ab_cold_reset | True | 0 |
| 29_uci_internal_fixed_blur_noise_to_clean_source_w4_all_ba_cold_reset | True | 0 |
| 29_uci_internal_fixed_blur_noise_to_clean_source_w4_all_history_invariance | True | 0 |
| 29_uci_internal_fixed_blur_noise_to_clean_source_w4_all_first_batch | True | 0 |
| 29_uci_internal_fixed_blur_noise_to_clean_norm_w0_none_ab_snapshot_replay | True | 0 |
| 29_uci_internal_fixed_blur_noise_to_clean_norm_w0_none_ab_full_replay | True | 0 |
| 29_uci_internal_fixed_blur_noise_to_clean_norm_w0_none_ba_snapshot_replay | True | 0 |
| 29_uci_internal_fixed_blur_noise_to_clean_norm_w0_none_ba_full_replay | True | 0 |
| 29_uci_internal_fixed_blur_noise_to_clean_norm_w0_none_history_invariance | True | 0 |
| 29_uci_internal_fixed_blur_noise_to_clean_norm_w0_all_ab_cold_reset | True | 0 |
| 29_uci_internal_fixed_blur_noise_to_clean_norm_w0_all_ba_cold_reset | True | 0 |
| 29_uci_internal_fixed_blur_noise_to_clean_norm_w0_all_history_invariance | True | 0 |
| 29_uci_internal_fixed_blur_noise_to_clean_norm_w0_all_first_batch | True | 0 |
| 29_uci_internal_fixed_blur_noise_to_clean_norm_w4_none_history_invariance | True | 0 |
| 29_uci_internal_fixed_blur_noise_to_clean_norm_w4_all_ab_cold_reset | True | 0 |
| 29_uci_internal_fixed_blur_noise_to_clean_norm_w4_all_ba_cold_reset | True | 0 |
| 29_uci_internal_fixed_blur_noise_to_clean_norm_w4_all_history_invariance | True | 0 |
| 29_uci_internal_fixed_blur_noise_to_clean_norm_w4_all_first_batch | True | 0 |
| 29_uci_internal_fixed_blur_noise_to_clean_tent_w0_none_ab_snapshot_replay | True | 0 |
| 29_uci_internal_fixed_blur_noise_to_clean_tent_w0_none_ab_full_replay | True | 0 |
| 29_uci_internal_fixed_blur_noise_to_clean_tent_w0_none_ba_snapshot_replay | True | 0 |
| 29_uci_internal_fixed_blur_noise_to_clean_tent_w0_none_ba_full_replay | True | 0 |
| 29_uci_internal_fixed_blur_noise_to_clean_tent_w0_parameters_first_batch | True | 0 |
| 29_uci_internal_fixed_blur_noise_to_clean_tent_w0_parameters_optimizer_first_batch | True | 0 |
| 29_uci_internal_fixed_blur_noise_to_clean_tent_w0_parameters_aux_first_batch | True | 0 |
| 29_uci_internal_fixed_blur_noise_to_clean_tent_w0_parameters_optimizer_aux_first_batch | True | 0 |
| 29_uci_internal_fixed_blur_noise_to_clean_tent_w0_all_ab_cold_reset | True | 0 |
| 29_uci_internal_fixed_blur_noise_to_clean_tent_w0_all_ba_cold_reset | True | 0 |
| 29_uci_internal_fixed_blur_noise_to_clean_tent_w0_all_history_invariance | True | 0 |
| 29_uci_internal_fixed_blur_noise_to_clean_tent_w0_all_first_batch | True | 0 |
| 29_uci_internal_fixed_blur_noise_to_clean_tent_w4_parameters_first_batch | True | 0 |
| 29_uci_internal_fixed_blur_noise_to_clean_tent_w4_parameters_optimizer_first_batch | True | 0 |
| 29_uci_internal_fixed_blur_noise_to_clean_tent_w4_parameters_aux_first_batch | True | 0 |
| 29_uci_internal_fixed_blur_noise_to_clean_tent_w4_parameters_optimizer_aux_first_batch | True | 0 |
| 29_uci_internal_fixed_blur_noise_to_clean_tent_w4_all_ab_cold_reset | True | 0 |
| 29_uci_internal_fixed_blur_noise_to_clean_tent_w4_all_ba_cold_reset | True | 0 |
| 29_uci_internal_fixed_blur_noise_to_clean_tent_w4_all_history_invariance | True | 0 |
| 29_uci_internal_fixed_blur_noise_to_clean_tent_w4_all_first_batch | True | 0 |
| 29_uci_internal_fixed_blur_noise_to_clean_sar_complete_w0_none_ab_snapshot_replay | True | 0 |
| 29_uci_internal_fixed_blur_noise_to_clean_sar_complete_w0_none_ab_full_replay | True | 0 |
| 29_uci_internal_fixed_blur_noise_to_clean_sar_complete_w0_none_ba_snapshot_replay | True | 0 |
| 29_uci_internal_fixed_blur_noise_to_clean_sar_complete_w0_none_ba_full_replay | True | 0 |
| 29_uci_internal_fixed_blur_noise_to_clean_sar_complete_w0_parameters_first_batch | True | 0 |
| 29_uci_internal_fixed_blur_noise_to_clean_sar_complete_w0_parameters_optimizer_first_batch | True | 0 |
| 29_uci_internal_fixed_blur_noise_to_clean_sar_complete_w0_parameters_aux_first_batch | True | 0 |
| 29_uci_internal_fixed_blur_noise_to_clean_sar_complete_w0_parameters_optimizer_aux_first_batch | True | 0 |
| 29_uci_internal_fixed_blur_noise_to_clean_sar_complete_w0_all_ab_cold_reset | True | 0 |
| 29_uci_internal_fixed_blur_noise_to_clean_sar_complete_w0_all_ba_cold_reset | True | 0 |
| 29_uci_internal_fixed_blur_noise_to_clean_sar_complete_w0_all_history_invariance | True | 0 |
| 29_uci_internal_fixed_blur_noise_to_clean_sar_complete_w0_all_first_batch | True | 0 |
| 29_uci_internal_fixed_blur_noise_to_clean_sar_complete_w4_parameters_first_batch | True | 0 |
| 29_uci_internal_fixed_blur_noise_to_clean_sar_complete_w4_parameters_optimizer_first_batch | True | 0 |
| 29_uci_internal_fixed_blur_noise_to_clean_sar_complete_w4_parameters_aux_first_batch | True | 0 |
| 29_uci_internal_fixed_blur_noise_to_clean_sar_complete_w4_parameters_optimizer_aux_first_batch | True | 0 |
| 29_uci_internal_fixed_blur_noise_to_clean_sar_complete_w4_all_ab_cold_reset | True | 0 |
| 29_uci_internal_fixed_blur_noise_to_clean_sar_complete_w4_all_ba_cold_reset | True | 0 |
| 29_uci_internal_fixed_blur_noise_to_clean_sar_complete_w4_all_history_invariance | True | 0 |
| 29_uci_internal_fixed_blur_noise_to_clean_sar_complete_w4_all_first_batch | True | 0 |
| 43_uci_internal_fixed_noise_brightness_to_blur_source_w0_none_ab_snapshot_replay | True | 0 |
| 43_uci_internal_fixed_noise_brightness_to_blur_source_w0_none_ab_full_replay | True | 0 |
| 43_uci_internal_fixed_noise_brightness_to_blur_source_w0_none_ba_snapshot_replay | True | 0 |
| 43_uci_internal_fixed_noise_brightness_to_blur_source_w0_none_ba_full_replay | True | 0 |
| 43_uci_internal_fixed_noise_brightness_to_blur_source_w0_none_history_invariance | True | 0 |
| 43_uci_internal_fixed_noise_brightness_to_blur_source_w0_all_ab_cold_reset | True | 0 |
| 43_uci_internal_fixed_noise_brightness_to_blur_source_w0_all_ba_cold_reset | True | 0 |
| 43_uci_internal_fixed_noise_brightness_to_blur_source_w0_all_history_invariance | True | 0 |
| 43_uci_internal_fixed_noise_brightness_to_blur_source_w0_all_first_batch | True | 0 |
| 43_uci_internal_fixed_noise_brightness_to_blur_source_w4_none_history_invariance | True | 0 |
| 43_uci_internal_fixed_noise_brightness_to_blur_source_w4_all_ab_cold_reset | True | 0 |
| 43_uci_internal_fixed_noise_brightness_to_blur_source_w4_all_ba_cold_reset | True | 0 |
| 43_uci_internal_fixed_noise_brightness_to_blur_source_w4_all_history_invariance | True | 0 |
| 43_uci_internal_fixed_noise_brightness_to_blur_source_w4_all_first_batch | True | 0 |
| 43_uci_internal_fixed_noise_brightness_to_blur_norm_w0_none_ab_snapshot_replay | True | 0 |
| 43_uci_internal_fixed_noise_brightness_to_blur_norm_w0_none_ab_full_replay | True | 0 |
| 43_uci_internal_fixed_noise_brightness_to_blur_norm_w0_none_ba_snapshot_replay | True | 0 |
| 43_uci_internal_fixed_noise_brightness_to_blur_norm_w0_none_ba_full_replay | True | 0 |
| 43_uci_internal_fixed_noise_brightness_to_blur_norm_w0_none_history_invariance | True | 0 |
| 43_uci_internal_fixed_noise_brightness_to_blur_norm_w0_all_ab_cold_reset | True | 0 |
| 43_uci_internal_fixed_noise_brightness_to_blur_norm_w0_all_ba_cold_reset | True | 0 |
| 43_uci_internal_fixed_noise_brightness_to_blur_norm_w0_all_history_invariance | True | 0 |
| 43_uci_internal_fixed_noise_brightness_to_blur_norm_w0_all_first_batch | True | 0 |
| 43_uci_internal_fixed_noise_brightness_to_blur_norm_w4_none_history_invariance | True | 0 |
| 43_uci_internal_fixed_noise_brightness_to_blur_norm_w4_all_ab_cold_reset | True | 0 |
| 43_uci_internal_fixed_noise_brightness_to_blur_norm_w4_all_ba_cold_reset | True | 0 |
| 43_uci_internal_fixed_noise_brightness_to_blur_norm_w4_all_history_invariance | True | 0 |
| 43_uci_internal_fixed_noise_brightness_to_blur_norm_w4_all_first_batch | True | 0 |
| 43_uci_internal_fixed_noise_brightness_to_blur_tent_w0_none_ab_snapshot_replay | True | 0 |
| 43_uci_internal_fixed_noise_brightness_to_blur_tent_w0_none_ab_full_replay | True | 0 |
| 43_uci_internal_fixed_noise_brightness_to_blur_tent_w0_none_ba_snapshot_replay | True | 0 |
| 43_uci_internal_fixed_noise_brightness_to_blur_tent_w0_none_ba_full_replay | True | 0 |
| 43_uci_internal_fixed_noise_brightness_to_blur_tent_w0_parameters_first_batch | True | 0 |
| 43_uci_internal_fixed_noise_brightness_to_blur_tent_w0_parameters_optimizer_first_batch | True | 0 |
| 43_uci_internal_fixed_noise_brightness_to_blur_tent_w0_parameters_aux_first_batch | True | 0 |
| 43_uci_internal_fixed_noise_brightness_to_blur_tent_w0_parameters_optimizer_aux_first_batch | True | 0 |
| 43_uci_internal_fixed_noise_brightness_to_blur_tent_w0_all_ab_cold_reset | True | 0 |
| 43_uci_internal_fixed_noise_brightness_to_blur_tent_w0_all_ba_cold_reset | True | 0 |
| 43_uci_internal_fixed_noise_brightness_to_blur_tent_w0_all_history_invariance | True | 0 |
| 43_uci_internal_fixed_noise_brightness_to_blur_tent_w0_all_first_batch | True | 0 |
| 43_uci_internal_fixed_noise_brightness_to_blur_tent_w4_parameters_first_batch | True | 0 |
| 43_uci_internal_fixed_noise_brightness_to_blur_tent_w4_parameters_optimizer_first_batch | True | 0 |
| 43_uci_internal_fixed_noise_brightness_to_blur_tent_w4_parameters_aux_first_batch | True | 0 |
| 43_uci_internal_fixed_noise_brightness_to_blur_tent_w4_parameters_optimizer_aux_first_batch | True | 0 |
| 43_uci_internal_fixed_noise_brightness_to_blur_tent_w4_all_ab_cold_reset | True | 0 |
| 43_uci_internal_fixed_noise_brightness_to_blur_tent_w4_all_ba_cold_reset | True | 0 |
| 43_uci_internal_fixed_noise_brightness_to_blur_tent_w4_all_history_invariance | True | 0 |
| 43_uci_internal_fixed_noise_brightness_to_blur_tent_w4_all_first_batch | True | 0 |
| 43_uci_internal_fixed_noise_brightness_to_blur_sar_complete_w0_none_ab_snapshot_replay | True | 0 |
| 43_uci_internal_fixed_noise_brightness_to_blur_sar_complete_w0_none_ab_full_replay | True | 0 |
| 43_uci_internal_fixed_noise_brightness_to_blur_sar_complete_w0_none_ba_snapshot_replay | True | 0 |
| 43_uci_internal_fixed_noise_brightness_to_blur_sar_complete_w0_none_ba_full_replay | True | 0 |
| 43_uci_internal_fixed_noise_brightness_to_blur_sar_complete_w0_parameters_first_batch | True | 0 |
| 43_uci_internal_fixed_noise_brightness_to_blur_sar_complete_w0_parameters_optimizer_first_batch | True | 0 |
| 43_uci_internal_fixed_noise_brightness_to_blur_sar_complete_w0_parameters_aux_first_batch | True | 0 |
| 43_uci_internal_fixed_noise_brightness_to_blur_sar_complete_w0_parameters_optimizer_aux_first_batch | True | 0 |
| 43_uci_internal_fixed_noise_brightness_to_blur_sar_complete_w0_all_ab_cold_reset | True | 0 |
| 43_uci_internal_fixed_noise_brightness_to_blur_sar_complete_w0_all_ba_cold_reset | True | 0 |
| 43_uci_internal_fixed_noise_brightness_to_blur_sar_complete_w0_all_history_invariance | True | 0 |
| 43_uci_internal_fixed_noise_brightness_to_blur_sar_complete_w0_all_first_batch | True | 0 |
| 43_uci_internal_fixed_noise_brightness_to_blur_sar_complete_w4_parameters_first_batch | True | 0 |
| 43_uci_internal_fixed_noise_brightness_to_blur_sar_complete_w4_parameters_optimizer_first_batch | True | 0 |
| 43_uci_internal_fixed_noise_brightness_to_blur_sar_complete_w4_parameters_aux_first_batch | True | 0 |
| 43_uci_internal_fixed_noise_brightness_to_blur_sar_complete_w4_parameters_optimizer_aux_first_batch | True | 0 |
| 43_uci_internal_fixed_noise_brightness_to_blur_sar_complete_w4_all_ab_cold_reset | True | 0 |
| 43_uci_internal_fixed_noise_brightness_to_blur_sar_complete_w4_all_ba_cold_reset | True | 0 |
| 43_uci_internal_fixed_noise_brightness_to_blur_sar_complete_w4_all_history_invariance | True | 0 |
| 43_uci_internal_fixed_noise_brightness_to_blur_sar_complete_w4_all_first_batch | True | 0 |
| 43_uci_internal_fixed_blur_noise_to_clean_source_w0_none_ab_snapshot_replay | True | 0 |
| 43_uci_internal_fixed_blur_noise_to_clean_source_w0_none_ab_full_replay | True | 0 |
| 43_uci_internal_fixed_blur_noise_to_clean_source_w0_none_ba_snapshot_replay | True | 0 |
| 43_uci_internal_fixed_blur_noise_to_clean_source_w0_none_ba_full_replay | True | 0 |
| 43_uci_internal_fixed_blur_noise_to_clean_source_w0_none_history_invariance | True | 0 |
| 43_uci_internal_fixed_blur_noise_to_clean_source_w0_all_ab_cold_reset | True | 0 |
| 43_uci_internal_fixed_blur_noise_to_clean_source_w0_all_ba_cold_reset | True | 0 |
| 43_uci_internal_fixed_blur_noise_to_clean_source_w0_all_history_invariance | True | 0 |
| 43_uci_internal_fixed_blur_noise_to_clean_source_w0_all_first_batch | True | 0 |
| 43_uci_internal_fixed_blur_noise_to_clean_source_w4_none_history_invariance | True | 0 |
| 43_uci_internal_fixed_blur_noise_to_clean_source_w4_all_ab_cold_reset | True | 0 |
| 43_uci_internal_fixed_blur_noise_to_clean_source_w4_all_ba_cold_reset | True | 0 |
| 43_uci_internal_fixed_blur_noise_to_clean_source_w4_all_history_invariance | True | 0 |
| 43_uci_internal_fixed_blur_noise_to_clean_source_w4_all_first_batch | True | 0 |
| 43_uci_internal_fixed_blur_noise_to_clean_norm_w0_none_ab_snapshot_replay | True | 0 |
| 43_uci_internal_fixed_blur_noise_to_clean_norm_w0_none_ab_full_replay | True | 0 |
| 43_uci_internal_fixed_blur_noise_to_clean_norm_w0_none_ba_snapshot_replay | True | 0 |
| 43_uci_internal_fixed_blur_noise_to_clean_norm_w0_none_ba_full_replay | True | 0 |
| 43_uci_internal_fixed_blur_noise_to_clean_norm_w0_none_history_invariance | True | 0 |
| 43_uci_internal_fixed_blur_noise_to_clean_norm_w0_all_ab_cold_reset | True | 0 |
| 43_uci_internal_fixed_blur_noise_to_clean_norm_w0_all_ba_cold_reset | True | 0 |
| 43_uci_internal_fixed_blur_noise_to_clean_norm_w0_all_history_invariance | True | 0 |
| 43_uci_internal_fixed_blur_noise_to_clean_norm_w0_all_first_batch | True | 0 |
| 43_uci_internal_fixed_blur_noise_to_clean_norm_w4_none_history_invariance | True | 0 |
| 43_uci_internal_fixed_blur_noise_to_clean_norm_w4_all_ab_cold_reset | True | 0 |
| 43_uci_internal_fixed_blur_noise_to_clean_norm_w4_all_ba_cold_reset | True | 0 |
| 43_uci_internal_fixed_blur_noise_to_clean_norm_w4_all_history_invariance | True | 0 |
| 43_uci_internal_fixed_blur_noise_to_clean_norm_w4_all_first_batch | True | 0 |
| 43_uci_internal_fixed_blur_noise_to_clean_tent_w0_none_ab_snapshot_replay | True | 0 |
| 43_uci_internal_fixed_blur_noise_to_clean_tent_w0_none_ab_full_replay | True | 0 |
| 43_uci_internal_fixed_blur_noise_to_clean_tent_w0_none_ba_snapshot_replay | True | 0 |
| 43_uci_internal_fixed_blur_noise_to_clean_tent_w0_none_ba_full_replay | True | 0 |
| 43_uci_internal_fixed_blur_noise_to_clean_tent_w0_parameters_first_batch | True | 0 |
| 43_uci_internal_fixed_blur_noise_to_clean_tent_w0_parameters_optimizer_first_batch | True | 0 |
| 43_uci_internal_fixed_blur_noise_to_clean_tent_w0_parameters_aux_first_batch | True | 0 |
| 43_uci_internal_fixed_blur_noise_to_clean_tent_w0_parameters_optimizer_aux_first_batch | True | 0 |
| 43_uci_internal_fixed_blur_noise_to_clean_tent_w0_all_ab_cold_reset | True | 0 |
| 43_uci_internal_fixed_blur_noise_to_clean_tent_w0_all_ba_cold_reset | True | 0 |
| 43_uci_internal_fixed_blur_noise_to_clean_tent_w0_all_history_invariance | True | 0 |
| 43_uci_internal_fixed_blur_noise_to_clean_tent_w0_all_first_batch | True | 0 |
| 43_uci_internal_fixed_blur_noise_to_clean_tent_w4_parameters_first_batch | True | 0 |
| 43_uci_internal_fixed_blur_noise_to_clean_tent_w4_parameters_optimizer_first_batch | True | 0 |
| 43_uci_internal_fixed_blur_noise_to_clean_tent_w4_parameters_aux_first_batch | True | 0 |
| 43_uci_internal_fixed_blur_noise_to_clean_tent_w4_parameters_optimizer_aux_first_batch | True | 0 |
| 43_uci_internal_fixed_blur_noise_to_clean_tent_w4_all_ab_cold_reset | True | 0 |
| 43_uci_internal_fixed_blur_noise_to_clean_tent_w4_all_ba_cold_reset | True | 0 |
| 43_uci_internal_fixed_blur_noise_to_clean_tent_w4_all_history_invariance | True | 0 |
| 43_uci_internal_fixed_blur_noise_to_clean_tent_w4_all_first_batch | True | 0 |
| 43_uci_internal_fixed_blur_noise_to_clean_sar_complete_w0_none_ab_snapshot_replay | True | 0 |
| 43_uci_internal_fixed_blur_noise_to_clean_sar_complete_w0_none_ab_full_replay | True | 0 |
| 43_uci_internal_fixed_blur_noise_to_clean_sar_complete_w0_none_ba_snapshot_replay | True | 0 |
| 43_uci_internal_fixed_blur_noise_to_clean_sar_complete_w0_none_ba_full_replay | True | 0 |
| 43_uci_internal_fixed_blur_noise_to_clean_sar_complete_w0_parameters_first_batch | True | 0 |
| 43_uci_internal_fixed_blur_noise_to_clean_sar_complete_w0_parameters_optimizer_first_batch | True | 0 |
| 43_uci_internal_fixed_blur_noise_to_clean_sar_complete_w0_parameters_aux_first_batch | True | 0 |
| 43_uci_internal_fixed_blur_noise_to_clean_sar_complete_w0_parameters_optimizer_aux_first_batch | True | 0 |
| 43_uci_internal_fixed_blur_noise_to_clean_sar_complete_w0_all_ab_cold_reset | True | 0 |
| 43_uci_internal_fixed_blur_noise_to_clean_sar_complete_w0_all_ba_cold_reset | True | 0 |
| 43_uci_internal_fixed_blur_noise_to_clean_sar_complete_w0_all_history_invariance | True | 0 |
| 43_uci_internal_fixed_blur_noise_to_clean_sar_complete_w0_all_first_batch | True | 0 |
| 43_uci_internal_fixed_blur_noise_to_clean_sar_complete_w4_parameters_first_batch | True | 0 |
| 43_uci_internal_fixed_blur_noise_to_clean_sar_complete_w4_parameters_optimizer_first_batch | True | 0 |
| 43_uci_internal_fixed_blur_noise_to_clean_sar_complete_w4_parameters_aux_first_batch | True | 0 |
| 43_uci_internal_fixed_blur_noise_to_clean_sar_complete_w4_parameters_optimizer_aux_first_batch | True | 0 |
| 43_uci_internal_fixed_blur_noise_to_clean_sar_complete_w4_all_ab_cold_reset | True | 0 |
| 43_uci_internal_fixed_blur_noise_to_clean_sar_complete_w4_all_ba_cold_reset | True | 0 |
| 43_uci_internal_fixed_blur_noise_to_clean_sar_complete_w4_all_history_invariance | True | 0 |
| 43_uci_internal_fixed_blur_noise_to_clean_sar_complete_w4_all_first_batch | True | 0 |


## Source training

Complete recorded epochs and seeds are retained in training_recorded.csv. Development accuracy is not a locked-test benchmark result.
