# Chạy Stage B sơ bộ trên Kaggle

Nếu Dataset của bạn có **200 lớp, ảnh 64×64 và tên `test_*.JPEG`**, dùng [bản Tiny riêng](kaggle_tiny_preliminary.md) và notebook `kaggle_tiny_imagenetc_preliminary.ipynb`. Notebook trong hướng dẫn này dành cho ImageNet-C 1000 lớp.

Đây là bản thăm dò riêng `stage_b_imagenetc_kaggle_preliminary_v1`, không thay thế hay ghi đè `configs/cloud_pilot.yaml`. Bộ file chưa được chạy trên GPU Kaggle; kiểm tra local dùng fixtures CPU, không tạo kết quả ImageNet-C thật.

## Quy mô

| Thành phần | Giá trị |
|---|---|
| Backbone / weights | ResNet50 / IMAGENET1K_V1 |
| Panel / seed | 1 / 101 |
| Kịch bản | gaussian_noise + brightness → defocus_blur; defocus_blur + gaussian_noise → brightness; brightness + defocus_blur → gaussian_noise |
| Severity | 5 |
| Prefix / washout tối đa / Q | 1024 / 512 / 1024 ảnh gốc |
| Batch size / W | 32 / 0, 4, 16 batch |
| Phương pháp | source, norm, tent, sar_complete |
| Reset | none, all |
| Số cặp / lượt Q | 72 / 144 |
| Số lượt ảnh trên Q | 147456, chưa tính H/W/controls/backward |
| Junction checkpoint lưu đĩa | Không; snapshots cần thiết vẫn tồn tại trong RAM/VRAM |

Ba kịch bản dùng chung 2560 ID ảnh gốc, tương ứng 7680 file JPEG qua ba corruption. Không tính ba kịch bản thành ba panel độc lập. Không có ablation factorial đầy đủ, p-value hay kết luận quần thể. Khoảng 0–10 giờ trong plan là allowance, chưa đo thời gian thực tế. `disk_gb: 10` là dự trù cho dữ liệu đã chọn và artifacts, không phải giới hạn cưỡng chế hoặc footprint của các archive chính thức.

## 1. Đưa mã nguồn lên Kaggle

ZIP nguồn đã tạo nằm tại `artifacts/kaggle/streaming-tta-kaggle-source.zip`. ZIP chỉ chứa mã nguồn, config, tests, notebook và tài liệu cần thiết; không chứa `.git`, kết quả Stage A, dữ liệu ảnh hay secrets.

Nếu sửa mã nguồn và muốn tạo bundle mới:

```powershell
python scripts/create_kaggle_bundle.py --output artifacts/kaggle/streaming-tta-kaggle-source-v2.zip
```

Builder không ghi đè ZIP cũ. Notebook tự nhận thư mục nguồn đã giải nén trong Kaggle Input. Nếu Input giữ nguyên ZIP, nó tìm tên mặc định `streaming-tta-kaggle-source.zip`; đổi tên file mới về tên đó khi upload ZIP nguyên dạng hoặc sửa tên tìm trong cell đầu.

Trên Kaggle, tạo **private Dataset** từ ZIP nguồn rồi import `notebooks/kaggle_stage_b_preliminary.ipynb` qua chức năng import/upload notebook. Add Input cả Dataset nguồn và Dataset ảnh. Notebook hỗ trợ Kaggle tự giải nén ZIP thành thư mục, hoặc giữ nguyên ZIP nguồn.

## 2. Chuẩn bị dữ liệu ảnh

Notebook mặc định dùng **ImageNet-C đã giải nén**, không tự tải các archive hàng chục GB. Dữ liệu phải có cấu trúc:

```text
/kaggle/input/<dataset>/imagenet-c/
  gaussian_noise/5/n01440764/ILSVRC2012_val_00000001.JPEG
  brightness/5/n01440764/ILSVRC2012_val_00000001.JPEG
  defocus_blur/5/n01440764/ILSVRC2012_val_00000001.JPEG
  ... 1000 thư mục synset cho mỗi variant ...
```

ID trong ví dụ chỉ minh họa đường dẫn; synset phải đúng lớp thực của ảnh. Không nhận layout toàn bộ JPEG nằm chung một thư mục, labels CSV riêng, CIFAR-C, ImageNet-A, hoặc ảnh corruption tự tạo rồi gọi là ImageNet-C. Mọi variant phải có đúng cùng tập basename và synset assignment. Sampler cần tối thiểu **2560 ID thuộc pilot** theo hash split cố định, không chỉ 2560 ảnh bất kỳ. Không giảm batch size hoặc đổi W để chữa lỗi OOM rồi xem kết quả là cùng thiết kế.

Nguồn chính thức: [ImageNet-C, Zenodo 2235448](https://zenodo.org/records/2235448). Mapping số lớp: [imagenet_class_index.json](https://storage.googleapis.com/download.tensorflow.org/data/imagenet_class_index.json), SHA256 pinned `a1e7a966a1f601d39e4b43e119b3e7dd4a2ad3ea08cf69847cbaf021013767bc`.

Nếu đã có các archive chính thức trên máy chuẩn bị dữ liệu, có thể dùng flow hiện có rồi đính kèm phần đã giải nén cùng `_provenance` lên Kaggle, theo quyền sử dụng dữ liệu của bạn:

```bash
python scripts/prepare_data.py extract --archives /path/noise.tar /path/blur.tar /path/weather.tar --destination /path/imagenet-c --corruptions gaussian_noise brightness defocus_blur --severities 5 --partition pilot --execute
```

Flow này kiểm MD5/size archive và ghi extraction provenance. Giữ `_provenance` khi chuyển dữ liệu. Extraction script vẫn cần archive đầy đủ; `--partition pilot` chỉ giảm phần JPEG được giải nén. Đừng tải ba archive vào working của phiên GPU chỉ để bắt đầu bản sơ bộ. Xem [quy trình dữ liệu](data_preparation.md) nếu muốn dùng flow archive.

Đối với Dataset giải nén đính kèm **không có provenance extraction**: nhập URL thật của Dataset trong `DATA_SOURCE_URL`. Wrapper opt-in nguồn khai báo cho bản exploratory, lưu `selected_image_hashes_only_not_official_archive_verified`. Hash của các file ảnh được chọn vẫn được kiểm, thứ tự/nhãn và mapping vẫn được kiểm; không khẳng định Dataset mirror giống byte-for-byte phân phối chính thức. Luồng cloud/manifest chuẩn vẫn yêu cầu archive provenance nếu không có opt-in này. Không đổi/mạo nhận provenance archive để vượt kiểm tra.

## 3. Chạy notebook

1. Bật GPU và Internet. Xem quota còn lại trong Settings. Kaggle công bố tối đa 12 giờ một phiên CPU/GPU; wrapper giới hạn riêng subprocess chạy thí nghiệm ở 10 giờ, để chừa thời gian xuất kết quả. Quota thực tế phụ thuộc tài khoản và được hiển thị trong giao diện.
2. Sửa `DATA_ROOT` đến thư mục chứa trực tiếp ba corruption; sửa `DATA_SOURCE_URL` đến trang Dataset bạn đính kèm.
3. Chạy tuần tự các cell hoặc Save Version → Run All. Cell đầu copy nguồn vào `/kaggle/working/streaming-tta-state-memory`.
4. Môi trường giữ Torch/torchvision của Kaggle và lưu phiên bản thực tế. Các tests nhỏ phải đạt trước khi chạy. Không `pip install -r requirements.txt` mặc định vì đó là pins local Stage A; thay CUDA wheels có thể gây xung đột driver/runtime.
5. Tạo manifest mới trên Kaggle (absolute paths Input). Chuẩn bị có đọc bytes ảnh được chọn nhưng không chạy mô hình. GPU quota vẫn có thể tiêu hao nếu session đã bật GPU; nên đính kèm dữ liệu sẵn trước khi mở phiên.
6. Chạy thật, audit, kiểm deterministic controls, xuất bảng/hình và ZIP. Internet được dùng để tải trọng số ResNet50 V1 khi chưa cache; runner chỉ dùng GPU đầu tiên.

Notebook có thể dùng mapping được đính kèm nếu đặt `DOWNLOAD_CLASS_INDEX=False` và sửa `CLASS_INDEX`. Chạy offline còn cần checkpoint ResNet50 V1 trong cache Torch đúng tên/đường dẫn; mặc định hướng dẫn này chạy có Internet.

Tài liệu nền tảng: [Kaggle Notebooks](https://www.kaggle.com/docs/notebooks), [GPU usage](https://www.kaggle.com/docs/efficient-gpu-usage).

## 4. Kết quả tải về

Tải `/kaggle/working/kaggle_exports/stage_b_imagenetc_kaggle_preliminary_v1_artifacts.zip` và `.zip.sha256` từ Output của phiên đã lưu. ZIP gồm results/NPZ, source anchor, manifests/index, environment/logs, config, source snapshot, tables/figures và diễn giải exploratory; không chứa JPEG ImageNet-C. Giữ ZIP và checksum cùng nhau.

Chỉ đọc kết quả như một lần chạy hoàn chỉnh khi:

- `run_status.json`: `complete`.
- `evaluation_audit.json`: `passed: true`, 144 directional rows, 72 paired rows, 1368 scalar comparisons. `unique_original_ids` ở audit là **1024** vì audit chỉ đếm Q; toàn bộ H/W/Q dùng 2560 ID.
- `controls.json`: toàn bộ controls `passed: true`.
- Không có lỗi mới trong logs của lần chạy đó.

Hai CSV dễ đọc nhất nằm trong results:

- `preliminary_history.csv`: disagreement_pp, error gap, NLL gap và chênh lệch logits theo từng kịch bản/W/reset. Xem W16 trước.
- `preliminary_performance.csv`: accuracy_percent và loss, trung bình AB/BA nhưng giữ kịch bản riêng. So source/norm với Tent/SAR ở cùng kịch bản/W.

`disagreement_pp` là điểm phần trăm: ví dụ 0.09765625 pp tương ứng một quyết định khác trong Q có 1024 mẫu. Disagreement không tự cho biết phương pháp gây hại hay có lợi. Zero disagreement không đảm bảo logits hoặc loss bằng nhau. `all` xóa lịch sử nhưng Q vẫn được thích nghi theo batch, không phải mô hình source đông cứng.

## 5. Nếu lỗi hoặc muốn chạy lại

`finally` xuất cả artifacts thiếu/failed để chẩn đoán. Nếu wrapper kill runner ở cap, logs có `wrapper_failure.json`; `run_status.json` có thể vẫn `running` vì bị dừng đột ngột. Không tự đánh dấu complete. Nếu Kaggle kill cả session, `finally` cũng không được bảo đảm chạy; giữ những output thực sự đã lưu, không suy luận từ ma trận thiếu.

Để chạy lại sau lỗi, sửa **cả `experiment_id` và `output`** trong YAML, ví dụ `_attempt2`, rồi chạy lại. Manifest có thể giữ nguyên khi đường dẫn/ảnh/cấu hình panel không đổi. Nếu thay dữ liệu hoặc đường dẫn, đổi cả `manifest_index` sang thư mục mới và tạo lại manifest. Runner không hỗ trợ resume giữa chừng và không ghi đè thí nghiệm cũ. Nếu cần export lại ZIP, chọn `EXPORT_DIR` mới; exporter không ghi đè archive.

Để audit local sau khi giải nén ZIP, chạy từ thư mục nguồn đi kèm:

```powershell
python scripts/evaluate.py --results results/stage_b_imagenetc_kaggle_preliminary_v1
```

Audit NPZ/CSV local không cần GPU hay JPEG Input. Chạy lại mô hình cần Input ảnh và tạo manifest mới theo đường dẫn runtime. Có thể mở rộng nhiều panel và đủ reset sau khi đo thời gian thực tế/tín hiệu, với ID/config mới.
