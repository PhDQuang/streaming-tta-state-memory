# Dataset policy

No large dataset is stored in Git or downloaded locally. Official test annotations are unavailable to adaptation code; only the evaluator reads labels. Group all corrupted versions of one original image under a single base ID before splitting.

## Local correctness data

[UCI Optical Recognition of Handwritten Digits](https://archive.ics.uci.edu/dataset/80/optical+recognition+of+handwritten+digits), E. Alpaydin and C. Kaynak, 1998; [DOI](https://doi.org/10.24432/C50P49), CC BY 4.0. Download archive is 591,292 bytes. Use **only optdigits.tra**, with 3,823 examples, for an internal source/development split. Do not load or extract optdigits.tes. The built-in sklearn load_digits dataset is the original test set, so it is deliberately not used for model development.

Images are 8×8 counts divided by 16, giving [0,1] intensity. File SHA-256: `e1b683cc211604fe8fd8c4417e6a69f31380e0c61d4af22e93cc21e9257ffedd`. Archive SHA-256: `0d7b054fea010270e9b3f06411c654c5e59547732ad626381980baffe0a23fb0`.

This small task verifies execution and controls; it supplies no evidence of ImageNet-scale generalization or publication-level novelty.

## Planned ImageNet-C cloud evaluation

[Original project](https://github.com/hendrycks/robustness), [Zenodo record](https://zenodo.org/records/2235448), DOI 10.5281/zenodo.2235448. Use released JPEGs, not newly generated approximations. Zenodo API metadata queried 2026-09-08 lists CC BY 4.0 for the record. Underlying ImageNet images have their own rights and [research access terms](https://image-net.org/accessagreement); repository code licensing does not confer ownership of the images. Intended use is non-commercial research. No redistribution of images is included in this repository.

| Archive | Bytes | Published MD5 |
|---|---:|---|
| noise.tar | 22565673785 | e80562d7f6c3f8834afb1ecf27252745 |
| blur.tar | 7112704951 | 2d8e81fdd8e07fef67b9334fa635e45c |
| weather.tar | 12797438995 | 33ffea4db4d93fe4a428c40a6ce0c25d |
| digital.tar | 7757510705 | 89157860d7b10d5797849337ca2e5c03 |
| extra.tar | 15789490144 | d492dfba5fc162d8ec2c3cd8ee672984 |

Archive sizes/checksums verified against the Zenodo API. Allocate approximately 120 GB cloud disk for pilot archives, extracted selected images, model caches and workspace; full 15-corruption evaluation needs a fresh storage estimate. Structure: `datasets/raw/imagenet-c/<corruption>/<severity>/<synset>/<original_name>.JPEG`.

The cloud preparer hashes original basenames to create disjoint prefix, common-tail, suffix and reserved-confirmation pools. Class indices follow the standard lexicographic ImageFolder synset order only after validating all 1,000 synsets. Store a frozen `class_to_idx.json` and manifests before inference. Do not infer class indices independently from a subset of classes.
