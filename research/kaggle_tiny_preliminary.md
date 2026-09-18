# Chạy Tiny ImageNet-C sơ bộ với Dataset hiện có

Bản riêng `tiny_imagenetc_kaggle_preliminary_v1` hỗ trợ dữ liệu bạn đã kiểm tra: 200 thư mục synset, ảnh JPEG 64×64, tên `test_4360.JPEG`… Dataset mirror hiện dùng là `husnifdu/imagenet-c`; profile thực tế được ghi là **Tiny ImageNet-C**. Không cần tải ImageNet-C 1000 lớp để chạy bản này.

## File cần đưa lên Kaggle

- Notebook: `notebooks/kaggle_tiny_imagenetc_preliminary.ipynb`.
- ZIP nguồn mới: `artifacts/kaggle/streaming-tta-kaggle-tiny-source.zip`.
- Config trong ZIP: `configs/kaggle_tiny_preliminary.yaml`.

1. Tạo private Dataset mới từ ZIP nguồn mới, ví dụ `streaming-tta-tiny-source`, hoặc upload một version mới của Dataset nguồn hiện có. ZIP không có dữ liệu ảnh, credentials, `.git` hay kết quả cũ.
2. Import **notebook Tiny mới** lên Kaggle. Notebook ImageNet-C cũ vẫn yêu cầu 1000 lớp.
3. Add Input nguồn mới và Dataset ảnh `husnifdu/imagenet-c` đang có. Nếu cập nhật version Dataset nguồn, kiểm tra notebook đã chọn đúng version mới.
4. Bật GPU + Internet. Chạy từng cell hoặc Save Version → Run All. Đường dẫn ảnh được tìm tự động; `DATA_SOURCE_URL` mặc định đã là URL mirror hiện tại.

Cell đầu copy nguồn mới vào `/kaggle/working/streaming-tta-tiny-state-memory`, tách khỏi bản ImageNet-C cũ. Nguồn được nhận diện bởi `scripts/tiny_imagenetc.py` và `configs/kaggle_tiny_preliminary.yaml`; nguồn cũ thiếu các file này sẽ bị bỏ qua. Nếu chỉ có ZIP chưa giải nén, notebook tìm tên `streaming-tta-kaggle-tiny-source.zip`.

Nếu cell đầu báo thiếu nguồn Tiny, bạn đang dùng version Dataset nguồn cũ. Add Input version mới và mở session mới. Bản đã copy trong working không tự cập nhật giữa một session. Nếu thay mirror, sửa `DATA_SOURCE_URL` thành URL thực tế của mirror đó.

## Mô hình và nhãn

Dùng ResNet50 với `IMAGENET1K_V1` pretrained từ ImageNet-1K, không huấn luyện source trên Tiny ImageNet. Giữ head 1000 logits và thêm phép chọn cố định 200 logits tương ứng các synset trong Dataset. Ví dụ nhãn Tiny thứ 1 có thể tương ứng một chỉ số ImageNet khác 1; không lấy tùy ý 200 logits đầu tiên.

Mapping ImageNet gốc là JSON 35 KB có SHA256 pinned `a1e7a966a1f601d39e4b43e119b3e7dd4a2ad3ea08cf69847cbaf021013767bc`. Mapping nhãn Tiny 0..199 theo synset đã sắp xếp; manifest lưu `output_imagenet_indices`, tên lớp và fingerprint. Runtime so phép chiếu với mapping canonical đã kiểm hash trước khi load ảnh/mô hình.

Phép chọn logits diễn ra **trước softmax, entropy, NLL, Brier, ECE và adaptation**. Accuracy vì thế là phân loại có điều kiện trong 200 lớp của Dataset, không phải accuracy head 1000 lớp đầy đủ. Tent/SAR cùng thích nghi trong không gian 200 lớp; SAR margin được đặt `0.4 × log(200) = 2.1193269466192146`.

Ảnh Input phải 64×64. Transform theo trọng số ResNet50 V1: resize cạnh ngắn 256, center crop 224, normalization ImageNet. Đây là exploratory transfer trên ảnh Tiny được phóng lớn, không tái tạo baseline đã train trên Tiny. Kết quả không được ghi thành Stage B ImageNet-C, không gộp với Stage A hoặc ImageNet-C, và không dùng để tuyên bố phương pháp tốt hơn ở quần thể.

Tham khảo [benchmark gốc](https://github.com/hendrycks/robustness#imagenet-c), [Tiny ImageNet-C chính thức](https://zenodo.org/records/2536630), [ResNet50 V1 của torchvision](https://docs.pytorch.org/vision/stable/models/generated/torchvision.models.resnet50.html).

## Quy mô bản Tiny

| Thành phần | Giá trị |
|---|---|
| Panel / seed | 1 / 101 |
| Corruptions / severity | gaussian_noise, brightness, defocus_blur / 5 |
| Prefix / maximum washout / Q | 512 / 512 / 512 ID |
| Batch size / W | 32 / 0, 4, 16 |
| Methods / interventions | source, norm, tent, sar_complete / none, all |
| Cặp / lượt Q | 72 / 144 |
| Lượt ảnh Q | 73728, chưa gồm H/W/controls/backward |
| Tổng ID được chọn / file ảnh qua 3 corruption | 1536 / 4608 |
| Q được audit | 512 ID |

Giảm prefix và Q từ 1024 xuống 512 để phù hợp dataset Tiny, giữ washout 512 cho W16. Sampling vẫn chỉ dùng basename và hash `sha256('20260908/' + base_id)`, 20% pilot / 80% reserve. Không dùng nhãn để cân bằng lớp hoặc chọn ID, không mượn ảnh reserve khi thiếu 1536 pilot ID. Ba kịch bản dùng cùng panel; H/W/Q không trùng ID. W4 là 128 ảnh cuối của đoạn W16, không phải một đoạn khác.

Mirror phải có đúng 200 synset được nhận diện trong mapping ImageNet, cùng tên file và lớp cho mỗi ID qua ba corruption. Tên ảnh nhận `test_<số>.JPEG` (cũng chấp nhận `.jpg`/`.jpeg`). Ảnh được chọn phải decode được và đúng 64×64. Không resize/recompress ảnh Input trong bước tạo manifest. Mapping synset này được kiểm là tập con của ImageNet; nguồn mirror chưa được đối chiếu byte-for-byte với archive Tiny chính thức.

Metadata nguồn ghi `claimed_dataset: Tiny ImageNet-C` và `selected_image_hashes_only_not_official_archive_verified`. Các bytes ảnh được chọn, nhãn theo thư mục, thứ tự stream và hashes manifest vẫn được kiểm; đây là provenance do người dùng khai báo, không phải xác minh archive gốc. Không đánh giá hoặc đọc pixels reserve để chọn cấu hình.

## Kết quả

Tải ZIP và checksum từ:

```text
/kaggle/working/kaggle_tiny_exports/
  tiny_imagenetc_kaggle_preliminary_v1_artifacts.zip
  tiny_imagenetc_kaggle_preliminary_v1_artifacts.zip.sha256
```

ZIP chứa source anchor với phép chiếu, JSON mapping, NPZ predictions, manifests, config, môi trường/logs, CSV, bảng/hình và tài liệu. Không chứa JPEG Input hoặc file xác thực Kaggle. Để chạy lại mô hình, cần Dataset ảnh; audit NPZ/CSV không cần GPU hay ảnh Input.

Kết quả hoàn chỉnh cần `run_status.json` có `status: complete`, `stage: TINY`; `evaluation_audit.json` có `passed: true`; mọi entry trong `controls.json` đạt. Audit dự kiến: 144 directional rows, 72 paired rows, 1368 scalar comparisons, 144 manifest checks, 512 unique original Q IDs, 3 panel-scenario groups. Ba groups vẫn chỉ là một panel độc lập.

Xem `preliminary_history.csv` ở W16 và `preliminary_performance.csv` ở cùng phương pháp/kịch bản/W. Disagreement được lưu cả tỷ lệ và điểm phần trăm; một quyết định khác trong Q512 là 0.1953125 pp. Không đồng nhất disagreement với lợi/hại hoặc loss. Reset all xóa trạng thái lịch sử, nhưng mô hình thích nghi vẫn cập nhật trong Q.

Allowance 0–10 giờ và disk 5 GB trong plan chưa được đo trên GPU Kaggle, không phải runtime/footprint đảm bảo. Wrapper kill riêng subprocess chạy model ở cap 10 giờ; thời gian chuẩn bị/tests/render nằm ngoài cap này. Kaggle có thể kết thúc toàn bộ phiên trước khi `finally` xuất ZIP. Artifacts partial/failed vẫn hữu ích để chẩn đoán, không được đánh dấu complete.

Để chạy lại, đổi **cả experiment_id và output** trong config, ví dụ `_attempt2`. Manifest giữ nguyên nếu dữ liệu/đường dẫn/counts không đổi; nếu đổi những phần đó, đổi `manifest_index` sang thư mục mới rồi prepare lại. Nếu muốn export lại, chọn `EXPORT_DIR` mới vì exporter không ghi đè ZIP.

## Kiểm tra local

```powershell
python scripts/kaggle_preliminary.py plan --config configs/kaggle_tiny_preliminary.yaml
python -m pytest tests/test_tiny_imagenetc.py tests/test_kaggle_preliminary.py tests/test_prepare_data.py tests/test_cloud_plan.py -q
```

Tests Tiny dùng JPEG giả lập, mapping ImageNet giả lập riêng có hash pinned theo fixture, model nhỏ CPU với head 1000/chiếu 200. Không dùng weights hoặc pixels benchmark thật. Kiểm tra model projection, nhãn, hash/tamper, cross-corruption identities, runtime shared runner, audit, controls, bảng/hình và notebook. Cần chạy notebook Kaggle để có kết quả thực nghiệm thật.
