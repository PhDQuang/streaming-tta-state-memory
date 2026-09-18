# ĐỀ CƯƠNG PHÁT TRIỂN NGHIÊN CỨU THÀNH BÀI BÁO KHOA HỌC

## What Does Adaptation Remember? Controlled History and State Interventions in Streaming Vision

**Tên tiếng Việt:** Mô hình thích nghi ghi nhớ điều gì? Nghiên cứu có kiểm soát về lịch sử và trạng thái trong thị giác máy tính theo luồng.

| Thông tin | Nội dung |
|---|---|
| Ngày soạn | 10/09/2026 |
| Phiên bản | 1.0 — kế hoạch triển khai từ trạng thái hiện tại của repo |
| Repo được kiểm tra | `C:\Study\Project\streaming-tta-state-memory` |
| Căn cứ | Proposal, trạng thái nghiên cứu, mã chạy thí nghiệm, kết quả Stage A, hai vòng phản biện và bản thảo hiện có |
| Mục tiêu cuối | Bài báo thực nghiệm có đóng góp rõ, bằng chứng kiểm chứng được và bộ mã tái lập đầy đủ |
| Trạng thái | Đã có nền tảng nghiên cứu và kiểm chứng cục bộ; chưa có kết quả benchmark để xác nhận giả thuyết chính |
| Phạm vi tài liệu | Hướng dẫn công việc tiếp theo; không phải báo cáo về các thí nghiệm mới đã chạy |

> **Điểm cần hiểu trước khi triển khai:** Công việc tiếp theo không chỉ là thuê GPU và điền thêm số liệu vào bản thảo. Cần xác định liệu hiện tượng quan sát được có đủ mới, đủ lớn hoặc được giới hạn đủ chặt để trở thành một kết luận khoa học. Không bắt buộc tạo ra một phương pháp tăng accuracy; một kết quả âm có phạm vi rõ và độ chính xác phù hợp cũng có thể là đóng góp. Không có kế hoạch nào bảo đảm bài được nhận.

---

## 1. Đích đến và tiêu chuẩn hoàn thành

Một bài báo hoàn chỉnh từ repo này cần trả lời được ba câu hỏi:

1. **Lịch sử có còn ảnh hưởng không?** Hai thứ tự của cùng các batch quá khứ có tạo ra dự đoán khác nhau trên cùng tương lai, sau khi đã quan sát cùng dữ liệu gần nhất?
2. **Trạng thái nào làm thay đổi ảnh hưởng đó?** Can thiệp vào tham số, optimizer và trạng thái phụ trợ làm thay đổi kết quả như thế nào, trong điều kiện so sánh công bằng?
3. **Ảnh hưởng đó có ý nghĩa gì?** Khác biệt có đi kèm lỗi phân loại, độ tin cậy hoặc khả năng phục hồi đáng quan tâm, hay chỉ là vài quyết định gần ranh giới?

### 1.1. Bộ sản phẩm phải có ở cuối dự án

| Sản phẩm | Tiêu chí hoàn thành |
|---|---|
| Định vị đóng góp | Nêu được khoảng trống cụ thể so với các công trình gần nhất; không gọi hiện tượng đã biết là phát hiện mới |
| Giao thức thực nghiệm | Khóa dữ liệu, model, điều kiện chính, thứ tự cập nhật/dự đoán, can thiệp, thước đo và cách suy luận thống kê trước xác nhận |
| Baseline | Có baseline cơ bản, SAR nguyên bản so với bản sửa, phương pháp gần đây và phương pháp có bộ nhớ/trạng thái bền vững; kiểm tra tính trung thành triển khai |
| Kết quả chính | Có dữ liệu benchmark thực, đủ đơn vị đánh giá để diễn giải khoảng bất định; báo cáo mọi điều kiện đã định trước |
| Phân tích cơ chế | Có đối chứng cần thiết để loại trừ lỗi reset, khác biệt RNG, batch, EMA hoặc việc cập nhật trong Q |
| Khả năng khái quát | Với kết luận rộng như đề xuất hiện tại: ít nhất một kiến trúc thứ hai và một dataset thứ hai, kèm giới hạn phạm vi |
| Tái lập | Có manifest, hash, cấu hình, checkpoint cần thiết, logits, trace, mã phân tích và hướng dẫn chạy lại |
| Bài viết | Bản thảo hoàn chỉnh; số liệu truy được về kết quả gốc; PDF được biên dịch và kiểm tra bố cục |
| Phản biện cuối | Mọi phản biện trọng yếu được giải quyết bằng bằng chứng hoặc được xử lý bằng việc thu hẹp kết luận |

**Không coi dự án hoàn thành chỉ vì:** test pass, pilot chạy hết, một seed có kết quả đẹp, một reset làm giảm disagreement, hoặc đã có file `paper.tex`.

## 2. Hiện trạng thực tế: đang có gì và thiếu gì?

Các số dưới đây là **kết quả đã lưu từ giai đoạn trước**, không phải kết quả chạy mới trong ngày soạn đề cương.

| Hạng mục | Đã có | Giới hạn cần nhớ |
|---|---|---|
| Tổng quan tài liệu | 66 mục tài liệu; 9 đề tài ứng viên; kiểm tra sâu 3 hướng | Danh mục cần cập nhật trước khi chốt đóng góp và trước khi nộp |
| Nền tảng phương pháp | Matched histories, common tail, shared suffix, can thiệp trạng thái | Đây là giao thức nghiên cứu; chưa phải thuật toán mới tăng hiệu năng |
| Baseline ban đầu | Source, normalization-only, Tent, `sar_complete` | Chưa đủ hệ baseline cho kết luận cuối cùng |
| Stage A v2 | 528 lượt chạy theo hướng, 264 so sánh cặp, 408 đối chứng đạt | Dữ liệu UCI nhỏ, chỉ phục vụ kiểm chứng cục bộ |
| Kiểm thử | 126 test đạt, 1 test bỏ qua do quyền symlink Windows | Đây là trạng thái lần kiểm tra đã lưu; cần kiểm tra lại sau sửa mã/môi trường |
| Tái tính số liệu | 5.016 so sánh scalar; tất cả dự đoán v1/v2 trùng khớp | Kiểm chứng tính nhất quán, không chứng minh giá trị khoa học trên benchmark |
| Tín hiệu lịch sử | Hai điều kiện không reset khác nhau ở 1/512 quyết định; các điều kiện còn lại bằng 0 | Chưa hỗ trợ H1; cũng chưa chứng minh tác động không đáng kể ở quy mô lớn |
| So sánh SAR | 6 trajectory thực; một quyết định khác biệt có lợi cho SAR nguyên bản | Không được viết rằng bản sửa luôn tốt hơn |
| Bài viết và hình | Có Markdown, LaTeX, bảng và 6 bộ hình cục bộ | PDF bài báo chưa được biên dịch/kiểm tra; kết quả benchmark còn thiếu |
| Cloud pilot | Có config, runner, chuẩn bị dữ liệu và dự toán | Chưa chạy GPU trả phí; ngân sách đang chờ phê duyệt |
| Phản biện | Hai vòng review | Nếu nộp như bài hoàn chỉnh, đánh giá hiện tại vẫn là Strong Reject |

**Lưu ý về đơn vị thống kê:** Ba seed nguồn ở Stage A dùng chung một tập ảnh. Vì vậy, không được gọi chúng là ba mẫu dữ liệu độc lập; không cộng v1 và v2 thành hai lần lặp khoa học mới; không dùng 528 trajectory làm kích thước mẫu độc lập.

## 3. Cách diễn đạt đóng góp của bài báo

### 3.1. Đóng góp đang theo đuổi

- Giao thức đo ảnh hưởng lịch sử trên **cùng tương lai**, trong khi batch, dữ liệu gần nhất và yếu tố ngẫu nhiên được kiểm soát.
- Hợp đồng lưu/khôi phục toàn bộ trạng thái, giúp phân biệt ảnh hưởng thực của lịch sử với lỗi triển khai.
- Bằng chứng thực nghiệm về độ bền, hệ quả và độ nhạy với can thiệp trạng thái; hoặc một kết quả âm được giới hạn đủ chính xác.

### 3.2. Các tuyên bố cần tránh

Không coi những điều sau là mới nếu chưa có bằng chứng phân biệt với tài liệu trước: cập nhật gradient phụ thuộc thứ tự; optimizer có bộ nhớ; reset có thể giảm collapse; dữ liệu có tương quan thời gian; lựa chọn thành phần reset ảnh hưởng thích nghi.

Không suy ra “optimizer gây ra toàn bộ hiệu ứng” từ một can thiệp lai giữa tham số nguồn và momentum lịch sử. Không đồng nhất giảm disagreement với tăng robustness.

### 3.3. Tài liệu cần tạo tiếp

Tạo `research/contribution_positioning.md` **trước xác nhận**, gồm một bảng so sánh giao thức với các công trình gần nhất được liệt kê trong repo: SAR, RDumb, ASR, OATTA, TTABC, AttenDence/phiên bản liên quan và ít nhất một baseline có bộ nhớ. Với từng bài, ghi phiên bản đã đọc, nguồn gốc, vấn đề đã giải quyết và phần còn khác với nghiên cứu này.

**Nghiệm thu:** Có thể viết một đoạn đóng góp 150–200 từ mà không dựa vào “chúng tôi là người đầu tiên” hoặc “cải thiện đáng kể” khi chưa có bằng chứng. Nếu khác biệt chỉ còn là thêm một script đánh giá, phải thiết kế lại câu hỏi hoặc thu hẹp loại đóng góp.

## 4. Quy ước và thiết kế cần giữ nhất quán

| Ký hiệu | Ý nghĩa |
|---|---|
| H | Lịch sử gồm hai khối domain; hai hướng AB và BA dùng đúng cùng các batch được tạo sẵn |
| W | Đoạn quan sát gần nhất chung; lấy k batch cuối của một tail tối đa cố định |
| Q | Đoạn tương lai chung, chưa xuất hiện trong H/W |
| P | Tham số mô hình |
| B | Buffer và chế độ forward, ví dụ trạng thái chuẩn hóa |
| O | Trạng thái optimizer, bao gồm optimizer lồng bên trong SAM |
| A | Trạng thái phụ trợ, ví dụ entropy EMA và bookkeeping của SAR |
| R | Trạng thái/yếu tố ngẫu nhiên |
| Panel | Một bộ ảnh gốc cho H/W/Q; đơn vị tổng hợp suy luận chính trong thiết kế này |
| pp | Điểm phần trăm: 1 pp tương ứng 0,01 khi disagreement được lưu trong khoảng [0,1] |

Các quy tắc bắt buộc:

1. Không đổi thành viên batch khi đảo thứ tự AB/BA. Cùng multiset ảnh nhưng khác batch chưa đủ để xem là đối chứng phù hợp.
2. ID ảnh gốc giữa H, W và Q không trùng. Nhiều corruption của một ảnh gốc không tạo ra nhiều mẫu độc lập.
3. Can thiệp thực hiện sau H+W, ngay trước Q.
4. Ghi dự đoán Q ở forward đầu tiên, trước cập nhật bằng batch đó. Dùng thống kê batch hiện tại là một phần giao thức được khai báo.
5. Adapter nhận ảnh, không nhận nhãn đích. Nhãn phục vụ evaluator; không dùng nhãn pilot/confirmation để chọn hyperparameter thuận lợi.
6. All-state reset phải khớp adapter mới cùng thuật toán chạy trên Q, không nhất thiết khớp source đóng băng.
7. Ghi riêng các sự kiện update, skip, recovery và mọi lỗi.
8. Cùng panel dùng cho nhiều scenario vẫn là một panel. Khi suy luận, gộp scenario trong panel trước.

## 5. Giả thuyết và kết quả cần đạt

### 5.1. H1 — ảnh hưởng lịch sử tồn tại sau đoạn gần nhất chung

Điều kiện chính đã xác định: **SAR complete / ResNet-50 / không reset bên ngoài / W = 16 batch**, trung bình trọng số bằng nhau trên ba scenario được khóa trước.

Với panel j:

`D_j = số ảnh Q có dự đoán argmax khác nhau giữa AB và BA / số ảnh Q`.

| Kết quả xác nhận | Cách diễn giải cho phép |
|---|---|
| Cận dưới CI 95% của trung bình D lớn hơn 1 pp | Hỗ trợ tồn tại ảnh hưởng có quy mô vượt ngưỡng định trước trong điều kiện đã đánh giá |
| Cận trên CI 95% nhỏ hơn 1 pp | Hỗ trợ giới hạn thực dụng dưới ngưỡng trong điều kiện đã đánh giá; không chứng minh bằng 0 tuyệt đối |
| Khoảng bất định còn cắt qua 1 pp | Chưa đủ kết luận; không gọi là thành công hoặc bằng chứng không có hiệu ứng |

Muốn đưa ra kết luận rộng theo proposal hiện tại, cần lặp lại trên kiến trúc thứ hai và dataset thứ hai. Nếu chỉ có bằng chứng trên một cấu hình, tiêu đề, abstract và conclusion phải giới hạn tương ứng.

### 5.2. H2 — độ nhạy với can thiệp trạng thái

Hai contrast định trước:

- **Optimizer:** `D(P+A reset) − D(P+O+A reset)`.
- **Auxiliary:** `D(no reset) − D(A reset)`.

Giá trị dương biểu thị việc bổ sung reset thành phần đang xét làm giảm disagreement. Lấy trung bình scenario bên trong mỗi panel, rồi tính contrast và bất định ở mức panel.

Theo proposal hiện tại, dùng CI Student-t hai phía 97,5% cho mỗi contrast; Bonferroni cho mức bao phủ đồng thời danh nghĩa 95% của hai contrast, với giá trị tới hạn `t[0.9875, n−1]`. Đây là mức danh nghĩa dưới các giả định đã nêu, không phải bảo đảm chính xác với mọi phân phối hoặc cỡ mẫu nhỏ.

**Điều kiện hỗ trợ tác động thực dụng:** Cận dưới của CI đồng thời phải vượt **0,5 pp**, không chỉ ước lượng điểm. Báo cáo cả hai contrast dù thuận lợi hay bất lợi. H2 được xác nhận theo kế hoạch có điều kiện trên H1; nếu H1 không được hỗ trợ, vẫn trình bày contrast như phân tích phụ, không đổi câu chuyện chính sau khi xem số liệu.

### 5.3. Hệ quả dự đoán cần đánh giá riêng

Luôn đi kèm accuracy/error, signed error gap AB−BA, độ lớn error gap, NLL và Brier. ECE, phân lớp và trace theo batch là phân tích phụ. Các ngưỡng tham chiếu 1 accuracy point và 0,02 NLL nats/example trong proposal là lựa chọn thiết kế, không phải hiệu quả đã đạt.

**Không đặt mục tiêu:** “Phải tăng accuracy X%”. **Đặt mục tiêu:** “Phải định lượng được hiệu ứng, bất định, điều kiện xuất hiện và hệ quả một cách kiểm chứng được”.

## 6. Lộ trình tổng thể và điều kiện chuyển giai đoạn

| Giai đoạn | Công việc chính | Sản phẩm | Điều kiện chuyển tiếp |
|---|---|---|---|
| G0 — Tiếp quản repo | Kiểm tra môi trường, đường dẫn, dữ liệu và mốc nguồn | Biên bản tiếp quản | Không còn lỗi đường dẫn/nguồn dữ liệu ảnh hưởng tái lập |
| G1 — Khóa pilot | Rà contribution, config, kiểm tra host, ngân sách | Kế hoạch chạy được chốt | Có phê duyệt chi phí và host phù hợp trước dùng dịch vụ trả phí |
| G2 — Pilot | Chạy ma trận Stage B, audit và lưu chi phí | Báo cáo pilot | Đối chứng hợp lệ; quyết định tiếp tục/sửa/dừng bằng văn bản |
| G3 — Hoàn thiện phương pháp đánh giá | Baseline mạnh, state contract, ablation, dữ liệu xác nhận | Mã/config và kế hoạch xác nhận | Mọi thiết kế mới được khóa trước khi xem kết quả reserve |
| G4 — Xác nhận | Chạy đủ panel và phân tích H1/H2 | Bảng kết quả chính, CI, audit | Kết luận phù hợp độ chính xác thực tế |
| G5 — Cơ chế và khái quát | Ablation bắt buộc, backbone/dataset thứ hai | Phân tích cơ chế và replication | Giới hạn/khẳng định được dữ liệu hỗ trợ |
| G6 — Hoàn thiện bài | Viết lại theo kết quả, tái lập, phản biện, PDF | Gói bài báo và supplementary | Vượt checklist nghiệm thu cuối |

Có thể chuẩn bị mã baseline và bài viết song song với phân tích pilot, nhưng không mở dữ liệu xác nhận để “tìm cấu hình tốt”.

## 7. G0 — Công việc cần làm đầu tiên trên máy hiện tại

### 7.1. Tiếp quản đúng repo và mốc bằng chứng

Đường dẫn cũ `C:\Study\Project\New folder` không còn tồn tại tại thời điểm soạn tài liệu. Repo hiện ở `C:\Study\Project\streaming-tta-state-memory`. Mọi lệnh bên dưới mặc định chạy từ thư mục gốc repo này, trừ khi có ghi khác.

Đọc theo thứ tự: [README](README.md), [status](research/status.md), [proposal](research/proposal.md), [phân tích Stage A](research/stage_a_analysis.md), [reviewer audit](research/reviewer_audit.md), [source freeze](research/source_freeze.json).

Việc cần làm:

- Kiểm tra Git và môi trường hiện tại; giữ nguyên dữ liệu gốc đã lưu.
- Xác minh checkpoint và file dữ liệu cần thiết còn trên máy. Chúng có thể bị loại khỏi Git theo thiết kế.
- Phân biệt đường dẫn tương đối còn dùng được với đường dẫn tuyệt đối trong metadata, manifest hoặc provenance cần kiểm tra sau di chuyển. Không giả định mọi record đã hỏng: `checkpoints.json` của Stage A v2 hiện dùng đường dẫn tương đối.
- Nếu phải di chuyển dữ liệu/khôi phục thí nghiệm, tạo bản ghi relocation hoặc manifest/run mới có hash và liên hệ với run gốc; không sửa âm thầm metadata của run đã đóng băng.
- `batch_crn_v1` dùng đường dẫn tuyệt đối trong khóa RNG cho ảnh cloud. Thay vị trí dữ liệu có thể đổi chuỗi ngẫu nhiên; muốn khóa độc lập đường dẫn phải tăng phiên bản giao thức và kiểm chứng lại.

Các lệnh kiểm tra gợi ý, chưa được chạy mới bởi tài liệu này:

```powershell
Set-Location 'C:\Study\Project\streaming-tta-state-memory'
git status --short
python -m pytest -q
python scripts/evaluate.py --results results/stage_a_uci_v2 --output results/verification/stage_a_reaudit_20260910.json
python scripts/run_cloud_pilot.py --config configs/cloud_pilot.yaml
```

Lệnh cuối chỉ in kế hoạch, không thuê GPU. Dùng tên file audit khác cho mỗi lần để giữ lịch sử. Chỉ chạy lại huấn luyện Stage A nếu có lý do kỹ thuật; khi chạy lại phải dùng experiment ID/output mới, không ghi đè v2.

**Đầu ra:** `research/resumption_audit.md` ghi môi trường, commit, đường dẫn, hash cần thiết, test/audit và việc sửa đã làm.

**Nghiệm thu:** Có thể kiểm tra lại số liệu cũ; biết chính xác checkpoint/dataset nào còn thiếu; không còn giả định sai về repo hoặc cấu hình đang sử dụng.

## 8. G1–G2 — Chuẩn bị và chạy pilot ImageNet-C

### 8.1. Mục đích pilot

Pilot trả lời bốn vấn đề: pipeline có đúng trên mô hình pretrained thực không; chi phí và bộ nhớ thực tế là bao nhiêu; tác động có biểu hiện gì; việc xác nhận tiếp theo có đáng làm không. **Ba panel pilot không đủ để mặc nhiên xác nhận H1/H2 hoặc practical equivalence.**

### 8.2. Cấu hình đã chuẩn bị

| Thành phần | Cấu hình |
|---|---|
| Config | `configs/cloud_pilot.yaml` |
| Model | ResNet-50, torchvision IMAGENET1K_V1 |
| Dữ liệu | JPEG ImageNet-C phát hành sẵn; severity 5 |
| Corruption | gaussian_noise, brightness, defocus_blur |
| Panel | 3 panel không trùng ID ảnh gốc; 3 scenario dùng lại mỗi panel |
| Mỗi panel | H=1.024, W tối đa=512, Q=1.024 ảnh; tổng 2.560 |
| Tổng ID | 7.680 ảnh gốc |
| Batch/tail | Batch 32; W=0/4/16 batch |
| Baseline | Source, norm, Tent, SAR complete |
| Can thiệp | 8 tổ hợp P/O/A và all-state cho phương pháp thích nghi; source/norm có 2 đối chứng |
| Quy mô | 594 so sánh cặp; 1.188 lượt Q theo hướng |
| Tối ưu | SGD lr 0,00025, momentum 0,9; SAR rho 0,05, margin 0,4 log(1000), threshold 0,2 |

Không tự ý thêm một cấu hình “có vẻ tốt” vào nhóm primary sau khi xem kết quả.

### 8.3. Tài nguyên và trách nhiệm vận hành

Dự toán **đã lập ngày 08/09/2026** trong repo: một GPU 24 GB loại RTX 4090, 8–16 giờ thí nghiệm, 120 GB đĩa, đề nghị trần tổng 20 USD. Đây là dự toán lịch sử chưa được profile, không phải báo giá hiện tại hoặc ngân sách đã được duyệt. Kiểm tra lại giá, khả dụng, thuế/phí và thời gian chuẩn bị trước khi thuê; xem [yêu cầu GPU](research/cloud_gpu_request.md).

Người triển khai phải có phê duyệt chi phí rõ ràng, host có quyền truy cập, khả năng xuất dữ liệu và cách chấm dứt tài nguyên tính phí. Lệnh `timeout` hoặc dừng Python **không tự dừng hóa đơn của nhà cung cấp**. Ngân sách pilot không bao gồm toàn bộ nghiên cứu xác nhận.

### 8.4. Thứ tự thực hiện

1. Kiểm tra driver/CUDA, phiên bản thư viện, RAM, đĩa trống và commit trên host.
2. Chuẩn bị dữ liệu bằng script có sẵn; kiểm tra checksum, class mapping, severity, panel và pool pilot/reserve.
3. Kiểm tra pretrained weights/transform bằng nguồn cấu hình chuẩn, không chọn transform theo accuracy target.
4. Chạy một preflight kỹ thuật có ID riêng trên dữ liệu pilot: forward, một bước thích nghi, lưu/khôi phục junction, thời gian và bộ nhớ. Đây là việc cần thiết kế bổ sung; không coi số đo preflight là kết quả xác nhận.
5. Nếu có lỗi OOM hoặc quá chậm, điều chỉnh kỹ thuật và ghi phiên bản. Đổi batch size, số bước thích nghi hoặc lượng dữ liệu là thay đổi giao thức, cần cập nhật kế hoạch trước chạy chính thức.
6. Chạy ma trận pilot đã khóa bằng [cloud workflow](scripts/cloud_pilot.sh). Không khởi chạy lặp đồng thời vào cùng output.
7. Audit kết quả, tạo bảng/hình, xuất raw/checkpoint/manifests và ghi chi phí trước khi kết thúc tài nguyên trả phí.
8. Nếu timeout/lỗi, giữ trạng thái partial/failed. Không ghép các mảnh không đồng nhất thành một run “complete”.

Sau khi run thực sự hoàn tất, các lệnh phân tích hiện có là:

```text
python scripts/evaluate.py --results results/stage_b_imagenetc_pilot_v1
python scripts/generate_tables.py --results results/stage_b_imagenetc_pilot_v1 --stage B
python scripts/generate_figures.py --results results/stage_b_imagenetc_pilot_v1 --stage B
```

### 8.5. Nội dung bắt buộc của báo cáo pilot

Tạo `research/pilot_report.md` và giữ toàn bộ dữ liệu trong `results/<experiment_id>/`:

- Cấu hình/commit/manifest/model-weight hash, môi trường, thời gian, bộ nhớ và chi phí thực.
- Số điều kiện dự kiến so với số điều kiện hoàn thành; đối chứng và lỗi.
- D của từng panel, scenario, W và phương pháp; không chỉ mean tổng.
- Accuracy/error/NLL/Brier so với source và norm, số update/skip/recovery.
- Tác động của reset; chênh lệch logits ngay đầu Q và diễn biến các batch tiếp theo.
- Hạn chế: ba panel, dữ liệu corruption tổng hợp, mức độ recovery, biến thiên giữa panel.
- Quyết định tiếp tục, chỉnh thiết kế hay dừng, kèm lập luận và ngân sách bước tiếp theo.

**Nghiệm thu kỹ thuật:** Đủ ma trận khi báo complete; hash/ID/mapping hợp lệ; các đối chứng bắt buộc đạt theo đặc tả. Nếu GPU không cho replay bitwise, phải điều tra và định nghĩa tolerance trước diễn giải, không nới tolerance để che một hiệu ứng nhỏ.

### 8.6. Quy tắc quyết định sau pilot

| Quan sát | Quyết định hợp lý |
|---|---|
| Đối chứng lỗi, full reset không khớp hoặc data integrity lỗi | Dừng diễn giải; sửa nguyên nhân, tạo run mới |
| Có tín hiệu và hậu quả đáng khảo sát, chi phí xác nhận khả thi | Tiếp tục G3, khóa thiết kế xác nhận |
| D gần 0 nhưng khoảng bất định rộng | Ghi “chưa kết luận”; xem khả năng đo đủ chính xác, không tuyên bố không có bộ nhớ |
| Recovery gần như liên tục, momentum không có cơ hội tồn tại | Thu hẹp diễn giải và thiết kế đối chứng recovery trên tập phát triển; không tắt recovery âm thầm để tạo tín hiệu |
| Tín hiệu biến mất khi sửa trạng thái/RNG/batch | Ưu tiên kết luận về độ nhạy triển khai nếu đủ bằng chứng; không giữ câu chuyện “bộ nhớ bền vững” |
| Chi phí hoặc dữ liệu không thể đáp ứng độ chính xác cần thiết | Thu hẹp phạm vi hoặc dừng hướng này bằng báo cáo có căn cứ |

## 9. G3 — Những phần mã thực sự cần phát triển thêm

**Quan trọng:** Runner hiện tại phục vụ pilot với tập phương pháp và ma trận được ràng buộc. Đổi tên YAML thành “confirmation” chưa tạo ra một pipeline xác nhận hoàn chỉnh.

| Hạng mục cần làm | Điểm mở rộng | Kết quả cần đạt và test nghiệm thu |
|---|---|---|
| Adapter cho baseline mới | `src/historytta/adapters.py` hoặc module tách riêng | Update/predict timing đúng; state inventory đầy đủ; parity với nguồn chính thức |
| Faithful SAR trong benchmark chung | Đưa so sánh độc lập hiện tại vào runner/analysis phù hợp | Phân biệt tên nguyên bản/bản sửa; chạy cùng dữ liệu và timing; giữ mọi sai khác |
| Q chỉ đọc | `src/historytta/runner.py` và config | Chạy Q không cập nhật P/O/A; khai báo riêng việc dùng BN batch statistics; kiểm tra state không đổi |
| Momentum ablation | Cấu hình/adapter/runner | 0 và 0,9 cùng điều kiện; xác minh momentum thật sự bằng 0 khi yêu cầu |
| Swaps và sham | Snapshot/intervention | Hoán đổi thành phần theo cặp đúng; sham không thay đổi; all-state và first-batch control vẫn đạt |
| Tách EMA với bookkeeping | Adapter SAR và trace | Chứng minh can thiệp chỉ đổi thành phần đã định nghĩa |
| Baseline có teacher/cache/memory | Snapshot, source anchor và serialization | Lưu/khôi phục cả teacher, cache, lịch sử, scheduler hoặc RNG riêng nếu có |
| Dữ liệu confirmation | Mở rộng `scripts/prepare_data.py` | Chọn đúng reserve, không fallback sang pilot, đủ panel disjoint; manifest bất biến |
| Runner confirmation | Runner/config/validation | Kiểm tra đúng số panel, scenario, methods, mode và intervention của thiết kế mới |
| Dataset thứ hai | Loader, mapping, split, source checkpoint | Không leak target labels; transform/checkpoint đúng dataset; giữ H/W/Q disjoint |
| Phân tích xác nhận | `scripts/evaluate.py`, bảng và thống kê | CI ở mức panel; H1/H2, multiplicity, quyết định ngưỡng và inventory cho thiết kế mới |
| Bài viết dựa benchmark | `scripts/build_paper.py` và template | Đọc schema nhiều stage/benchmark; tách số liệu toy; mọi bảng truy được về raw |

**Hai bẫy cụ thể trong repo:**

1. `prepare_data.py extract` có lựa chọn reserve, nhưng chức năng tạo manifest hiện xây **pilot panels**. Chỉ đổi `--output` hoặc `--prefix-size` không chuyển nó thành bộ lấy mẫu confirmation.
2. `scripts/build_paper.py` hiện chỉ nhận **Stage A**, có giả định về ba source seed và đoạn văn toy cố định. Không dùng lệnh đó với Stage B rồi xem là đã cập nhật bài; phải phát triển generator/template hoặc viết lại bản benchmark có kiểm tra claim provenance.

Tên file/module mới do người triển khai quyết định; bảng này là yêu cầu cần xây, không phải danh sách tính năng đã tồn tại.

## 10. Hệ baseline cho bài báo cuối

| Nhóm | Cần trả lời điều gì? | Yêu cầu |
|---|---|---|
| Source | Không thích nghi có hành vi và lỗi gì? | Baseline bắt buộc trên cùng Q |
| Normalization-only | Hiệu quả đến từ batch statistics hay cập nhật? | Bắt buộc khi phù hợp kiến trúc; trên LN phải mô tả đúng tác dụng/giới hạn |
| Tent | Baseline entropy cơ bản có phụ thuộc lịch sử không? | Giữ parity và cấu hình được công bố/giải thích |
| SAR faithful và complete | Reset/serialization có làm thay đổi kết luận? | So sánh benchmark thực, không chỉ bài toán quadratic/UCI |
| Baseline reset gần đây | Giao thức có cho thông tin vượt nghiên cứu reset trước? | ASR là ứng viên trong proposal; đọc/pin phiên bản chính thức trước triển khai |
| Baseline có trạng thái bền vững | Kết luận có chỉ là đặc tính của Tent/SAR? | Chọn ít nhất một trong nhóm RoTTA/PeTTA/ROID theo state contract và dữ liệu hợp lệ |
| EATA, nếu đáp ứng điều kiện | Có ổn định hơn khi có regularization/Fisher hợp lệ? | Chỉ thêm nếu có dữ liệu nguồn phù hợp; không tạo Fisher từ target labels |

Không đánh giá chất lượng bài bằng số baseline đơn thuần. Mỗi baseline phải loại trừ một lời giải thích cạnh tranh. Chốt danh sách sau kiểm tra prior work và trước xác nhận; nếu thiếu một baseline quyết định, phải thu hẹp claim thay vì che bằng nhiều baseline ít liên quan.

Với từng baseline, lập một “implementation card”: paper/version/commit, weights, transforms, hyperparameters, dữ liệu phụ, tham số được update, trạng thái động, reset semantics, predict timing, parity test, chi phí và khác biệt với bản gốc.

## 11. G4 — Thiết kế nghiên cứu xác nhận và phân tích thống kê

### 11.1. Dữ liệu và số panel

Phác thảo hiện tại: **24 panel**, mỗi panel **512 H + 512 W + 512 Q = 1.536 ảnh**, tổng **36.864 ID**, lấy từ pool reserve theo quy tắc hash đã lưu. Kiểm tra số ID thực đủ điều kiện trước freeze; không giả định pool luôn đúng 40.000 ảnh.

Đây là thiết kế theo giới hạn dữ liệu/nguồn lực, **chưa phải chứng minh có đủ power**. Pilot dùng H/Q=1.024/1.024, còn confirmation dùng 512/512; cả tác động và phương sai có thể khác. Không lấy phương sai pilot thay trực tiếp vào công thức cỡ mẫu confirmation.

Hai cách ra quyết định hợp lệ theo kế hoạch:

- Chấp nhận N=24 như thiết kế giới hạn, khóa trước, chạy đủ và kết luận theo CI thực tế; nếu CI chưa đủ hẹp thì ghi inconclusive.
- Nếu cần thiết kế theo độ chính xác, lập một đợt calibration với kích thước H/W/Q tương ứng trên dữ liệu phát triển hợp lệ, dự toán riêng, rồi khóa N trước khi xem kết quả reserve. Không “calibration” bằng chính kết quả xác nhận đã mở.

### 11.2. Tệp cần đóng băng trước chạy

Tạo `research/confirmation_plan.md` và cấu hình tương ứng, ghi tối thiểu:

| Nội dung | Yêu cầu |
|---|---|
| Primary | Model/method/W/H/Q/scenario, trọng số và cách dự đoán |
| Secondary | Các contrast, ablation và hệ quả dự đoán được định trước |
| Dữ liệu | Pool, ID, label map, image hash, manifest, overlap audit |
| Mẫu | N panel, cách tạo panel, các lần lặp và đơn vị suy luận |
| Thống kê | Công thức estimator/CI, mức alpha, xử lý multiplicity, giả định và sensitivity |
| Thiếu/lỗi | Thế nào là failed run; khi nào được chạy lại; cách giữ trace và báo cáo |
| Tài nguyên | Thời gian/đĩa/budget dựa số đo pilot; giới hạn dừng vận hành |
| Version | Commit, config hash, ngày khóa; mọi sửa đổi và lý do |

Không thực hiện optional stopping theo p-value hoặc dừng ngay khi hiệu ứng vừa vượt ngưỡng.

### 11.3. Phân tích bắt buộc

1. Kiểm tra toàn bộ inventory trước tính bảng chính. Không thay ô thiếu bằng 0 hoặc bỏ panel bất lợi.
2. Tính thước đo từ logits/labels/IDs gốc; kiểm tra AB/BA cùng Q.
3. Gộp scenario trong panel theo trọng số đã khóa. Hiển thị cả giá trị từng panel.
4. Tính trung bình và CI của H1; báo CI dưới dạng fraction và/hoặc pp nhất quán.
5. Tính hai H2 contrast và CI đồng thời; báo cả contrast thuận lợi và bất lợi.
6. Kiểm tra phân phối panel, outlier, mức độ giới hạn ở 0; nêu khi xấp xỉ t không đáng tin. Bootstrap toàn panel là sensitivity khi đủ mẫu, không thay ảnh Q thành mẫu IID.
7. Báo accuracy/error/NLL/Brier tương ứng; reset giảm D nhưng làm xấu loss phải được trình bày.
8. Các phân tích chọn sau khi xem dữ liệu phải đánh dấu exploratory; không đổi nhãn thành primary.

**Nghiệm thu:** Người khác có thể tính lại bảng kết luận từ raw bằng lệnh xác định, và nhìn được lý do kết luận positive, practical null hay inconclusive.

## 12. G5 — Ablation và đối chứng để bảo vệ kết luận cơ chế

| Thí nghiệm | Câu hỏi | Điều kiện đạt |
|---|---|---|
| P/O/A factorial và all-state | Thành phần reset nào thay đổi hiệu ứng? | Đủ ô cần thiết, contrast ghép cặp; không trộn all-state vào factorial 8 ô |
| Frozen Q so với adapting Q | Hiệu ứng có ngay ở junction hay được tạo/khuếch đại trong Q? | Chế độ không update được xác minh; BN forward được định nghĩa rõ |
| Momentum 0 so với 0,9 | Động lực optimizer có liên quan không? | Chỉ thay yếu tố đã khóa; so cả D, logits và loss |
| Sham/roundtrip | Can thiệp có tự gây sai khác kỹ thuật không? | Sham không đổi dự đoán/trạng thái theo hợp đồng |
| Swap O hoặc A giữa AB/BA | Hiệu ứng có đổi theo thành phần chuyển sang không? | Source anchor, tensor mapping và pairing hợp lệ |
| EMA-only/bookkeeping-only | Reset auxiliary đang thay cái gì? | Log xác minh chỉ thành phần mục tiêu thay đổi |
| Recovery trace | Auto-reset có xóa/lấn át lịch sử không? | Phân tích thời điểm, số lần và tác động; không suy cơ chế chỉ từ tổng số lần |
| W và H khác nhau | Ảnh hưởng thay đổi theo mức tiếp xúc thế nào? | Chốt độ dài trước; giữ quy tắc tail cuối; báo số ảnh và batch |

Ưu tiên frozen Q, momentum và phân biệt faithful/corrected trước khi viết kết luận về optimizer. State swap/EMA isolation cần làm khi chúng quyết định diễn giải cơ chế. Nếu không hoàn thành được, giữ kết luận ở mức **độ nhạy can thiệp**, không tuyên bố trung gian nhân quả duy nhất.

## 13. G5 — Robustness và kiểm chứng khả năng khái quát

### 13.1. Kiến trúc thứ hai

Theo proposal: ResNet-50 BN và ViT-B/16 LN. Dùng checkpoint/transform hợp lệ cho từng model; phân biệt Tent trên LN là phần mở rộng. Smoke test trên model chưa pretrained trong repo chưa đáp ứng yêu cầu replication.

Không yêu cầu hai model có cùng accuracy tuyệt đối. Cần hỏi liệu kết luận về persistence/reset còn đúng, thay đổi quy mô hay biến mất, và giải thích giới hạn theo kiến trúc.

### 13.2. Dataset thứ hai

Các ứng viên đã nêu trong proposal gồm CIFAR-100-C và một benchmark domain tự nhiên như DomainNet-126 khi split/quyền truy cập/source training đã được kiểm tra. Trước triển khai phải chọn cụ thể, xác minh protocol và nguồn checkpoint; không dùng ImageNet head 1.000 lớp như classifier hợp lệ cho CIFAR-100 hoặc DomainNet.

Tối thiểu cần một dataset độc lập để bảo vệ kết luận rộng. Nếu bài nói về thay đổi tự nhiên trong triển khai, chỉ hai bộ corruption tổng hợp vẫn chưa đủ cho câu chữ đó; cần benchmark tự nhiên phù hợp hoặc thu hẹp claim.

### 13.3. Các chiều kiểm tra bổ sung

Chọn có mục đích, khóa trước: corruption family/severity khác, return-to-clean, thứ tự batch khác ngoài AB/BA, độ dài H/W, mức auto-recovery. Batch reshuffling phải thành thí nghiệm riêng vì nó thay đổi đơn vị batch mà giao thức chính giữ cố định.

**Nghiệm thu:** Có bảng replication riêng với raw và provenance; giữ cả trường hợp không lặp lại hiện tượng. Không đổi tên thành “universal memory effect” nếu bằng chứng chỉ nằm ở một cấu hình.

## 14. Phân tích lỗi và hệ quả thực tế

Không dừng ở biểu đồ disagreement. Với mỗi điều kiện quan trọng, cần xem:

- AB đúng/BA sai, AB sai/BA đúng, cả hai đúng, cả hai sai.
- Source đúng nhưng thích nghi sai; source sai nhưng thích nghi đúng.
- Logit margin/probability/NLL ở các điểm khác quyết định, để nhận diện near-tie.
- Diễn biến theo batch quanh reset/recovery, không chỉ điểm cuối Q.
- Phân bố theo lớp/scenario/severity, khi đủ số lượng và có nhãn evaluator hợp lệ.
- Độ nhạy với source model/seed; tách nguồn biến thiên này khỏi số panel dữ liệu.

Khóa quy tắc chọn ví dụ trước khi xuất hình hoặc dùng lựa chọn xác định. Không chỉ chọn những hình chứng minh reset tốt; hiển thị cả thất bại và nhóm rỗng. Một vài hình minh họa không thay thế bảng thống kê toàn bộ mẫu.

**Đầu ra:** `research/error_analysis.md`, bảng nhóm lỗi, trace và hình ví dụ với ID/hash quay lại raw.

## 15. Bộ bảng và hình của bài báo hoàn chỉnh

Đây là danh sách sản phẩm cần xây từ kết quả thật, không phải yêu cầu điền số ngay bây giờ.

| Sản phẩm | Nội dung | Nguồn dữ liệu |
|---|---|---|
| Bảng 1 | Giao thức, dataset, model, baseline, tài nguyên | Config + implementation cards |
| Bảng 2 | Kết quả H1: từng model/method, W chính, D và CI | Paired rows gộp theo panel |
| Bảng 3 | Accuracy/error/NLL/Brier so với source và norm | Runs ghép đúng điều kiện |
| Bảng 4 | H2 và các can thiệp trạng thái | Factorial/contrast có multiplicity |
| Bảng 5 | Faithful/corrected, frozen Q, momentum, recovery | Thí nghiệm cơ chế |
| Bảng 6 | Kiến trúc/dataset thứ hai và giới hạn replication | Run kiểm chứng độc lập |
| Bảng phụ | Mọi panel/scenario/seed, lỗi, runtime, memory, chi phí | Raw inventory đầy đủ |
| Hình 1 | Sơ đồ H_AB/H_BA → W → can thiệp → Q | Sơ đồ giao thức, ghi rõ không phải số đo |
| Hình 2 | D theo W, có điểm từng panel và bất định phù hợp | Kết quả chính |
| Hình 3 | Reset contrast kèm hệ quả accuracy/loss | Kết quả can thiệp |
| Hình 4 | Trace theo batch quanh recovery | Log sự kiện + logits |
| Hình 5 | Phân tích lỗi minh họa | Quy tắc chọn ví dụ và ID có thể tra lại |

Quy tắc trình bày: ghi rõ pp và %, đơn vị NLL, số panel thật, CI hay SD; dùng trục nhất quán khi so sánh; không phóng đại chênh lệch nhỏ bằng trục cắt khó nhận ra. Đặt bảng đầy đủ vào supplementary nếu main paper thiếu chỗ.

## 16. G6 — Viết lại bản thảo thành bài báo cuối

### 16.1. Cấu trúc đề xuất

| Phần | Nội dung cần viết | Bằng chứng phải có trước khi khẳng định |
|---|---|---|
| Abstract | Vấn đề, đóng góp, thiết kế, phát hiện chính, phạm vi | Số liệu benchmark thật và CI đã kiểm tra |
| Introduction | Vì sao câu hỏi đáng quan tâm và prior work chưa trả lời đủ | Bảng định vị đóng góp cập nhật |
| Related Work | Temporal TTA, reset/memory, evaluation/fidelity | Nguồn và phiên bản đã đọc, không chỉ tên bài |
| Method/Protocol | State, batch, H/W/Q, timing, estimand và controls | Mã/manifest/state inventory tương ứng |
| Experimental Setup | Dataset, model, baseline, split, hyperparameter, compute | Config freeze và provenance |
| Main Results | H1, H2 và hệ quả dự đoán | Bảng chính đầy đủ, không chọn seed |
| Ablation/Mechanism | Điều gì đổi khi thay state/Q mode/momentum | Đối chứng bắt buộc và giới hạn diễn giải |
| Robustness | Điều kiện lặp lại hoặc thất bại | Backbone/dataset/scenario replication |
| Error Analysis | Loại lỗi và ví dụ có quy tắc | Phân nhóm toàn mẫu + ID ví dụ |
| Discussion/Limitations | Phạm vi, nguồn sai lệch, giả định thống kê, chi phí | Hạn chế phù hợp kết quả thực |
| Conclusion | Điều đã biết thêm sau nghiên cứu | Không mạnh hơn các bảng kết quả |
| Supplementary | Chi tiết triển khai, mọi run, công thức, tái lập | Raw và mã xuất bảng/hình |

### 16.2. Việc cần sửa ở bản thảo hiện tại

Giữ bản Stage A như một mốc lịch sử trước khi tạo bản benchmark. Đưa phần UCI và optimizer quadratic về phần verification hoặc supplementary; chúng không nên chiếm vai trò kết quả khoa học chính. Viết lại abstract/contribution theo phát hiện cuối, kể cả khi H1 không được hỗ trợ.

Mỗi số liệu trong bài phải có liên kết từ claim → bảng phân tích → run/manifest/hash. Mở rộng `paper/claims.json` hoặc tạo claim ledger mới cho benchmark; cập nhật hash sau chỉnh nội dung. Không chỉ thay tên dataset trong template cũ.

Sau khi generator/template hỗ trợ đầy đủ nội dung mới, kiểm tra lại exporter LaTeX. Khi có môi trường TeX, biên dịch `paper.tex` và kiểm tra trực quan mọi trang, bảng, caption, font, citation và liên kết. File LaTeX hiện có chưa đồng nghĩa có PDF sẵn sàng nộp.

### 16.3. Chọn nơi nộp

Chọn venue sau khi phạm vi và chất lượng bằng chứng đủ rõ. Nếu đóng góp là đánh giá/giao thức có kết quả mạnh, cân nhắc nơi phù hợp với empirical evaluation; nếu chủ yếu là audit triển khai nhỏ, điều chỉnh phạm vi bài tương ứng. Kiểm tra call for papers, deadline, template, anonymity, giới hạn trang và yêu cầu artifact từ nguồn chính thức tại thời điểm chọn. Không suy ra khả năng được nhận từ số lượng baseline hoặc số trang.

## 17. Quản lý kết quả, phiên bản và chi phí

### 17.1. Hồ sơ bắt buộc cho mỗi experiment ID

`config + commit/source hash + manifest/image/weight hash + seeds + environment + status + logits/labels/IDs + metrics + traces + controls + timing/memory + cost + analysis provenance`.

Một cấu hình đổi về mặt khoa học phải có ID mới. Thí nghiệm thất bại giữ traceback và dữ liệu đã ghi. Audit lại dùng file/mốc riêng khi cần lưu lịch sử. Checkpoint/ảnh lớn không nhất thiết commit vào Git, nhưng phải có nơi lưu được kiểm soát, checksum và hướng dẫn khôi phục phù hợp điều kiện dữ liệu.

### 17.2. Dự toán giai đoạn tiếp theo

Sau pilot, dự toán confirmation bằng số đo runtime cho từng method/mode, số panel, số lần replay, checkpoint, transfer và bộ nhớ. Cộng cả nguồn lực huấn luyện nguồn cho dataset mới nếu cần. Không nhân đơn giản một lần forward với tổng số ảnh vì SAR/backward/replay có overhead đáng kể.

Tạo `research/confirmation_gpu_request.md` trước chi phí mới: mục tiêu, ma trận, runtime đo được, GPU/VRAM, storage, chi phí, contingency, thời điểm dừng và kết quả quyết định tiếp tục. Mức 20 USD của pilot không được trình bày như chi phí đủ để hoàn thành bài báo.

## 18. Kế hoạch thời gian và phân công công việc

Ước lượng dưới đây là **kế hoạch nhân lực tham khảo**, không phải cam kết deadline hay thời gian GPU đã đo. Phụ thuộc nhiều vào việc chạy pilot, baseline chính thức, source checkpoint, ngân sách và kết quả âm.

| Chặng | Thời gian làm việc dự kiến | Việc người phụ trách cần thực hiện |
|---|---|---|
| Tiếp quản và khóa pilot | 1–3 ngày | Kiểm tra repo, thống nhất protocol và ngân sách |
| Pilot và phân tích | 2–4 ngày sau khi có host | Preflight, chạy, audit, xuất dữ liệu, viết quyết định |
| Baseline và đối chứng bổ sung | 1–2 tuần | Đọc implementation chính thức, coding, parity, state tests |
| Khóa và chạy confirmation | 1–2 tuần hoặc hơn | Hoàn thiện sampler/runner/CI; phê duyệt ngân sách; chạy đủ |
| Replication và phân tích lỗi | 1–2 tuần hoặc hơn | Dataset/backbone thứ hai, source model, robustness |
| Viết, phản biện và đóng gói | 1–2 tuần | Kiểm tra claims, supplementary, tái lập, PDF |

Có thể chồng lấp các phần độc lập; không rút ngắn bằng cách bỏ đối chứng thiết yếu. Với một người thực hiện, nên đặt mốc theo **sản phẩm nghiệm thu**, thay vì chỉ ghi “tuần này chạy xong”.

Người phụ trách khoa học chốt giả thuyết và phạm vi; người triển khai chịu trách nhiệm mã/dữ liệu/provenance; người phân tích chịu trách nhiệm thống kê và kiểm tra raw; người phản biện kiểm tra novelty và claims. Một người có thể đảm nhiệm nhiều vai, nhưng nên có một lượt kiểm tra độc lập bởi cộng tác viên/người hướng dẫn trước nộp.

## 19. Checklist nghiệm thu trước khi gọi là “bài báo hoàn chỉnh”

### 19.1. Khoa học

- [ ] Khoảng trống được đối chiếu với prior work gần nhất và đúng phiên bản.
- [ ] H1/H2, primary/secondary và ngưỡng thực dụng được khóa trước confirmation.
- [ ] Có benchmark thực; kết luận không dựa chủ yếu vào UCI hoặc quadratic audit.
- [ ] Hệ baseline đủ sức loại trừ các lời giải thích cạnh tranh quan trọng.
- [ ] Kết quả dương, âm và inconclusive được phân biệt đúng.
- [ ] Claim về optimizer/EMA không vượt mức đối chứng đã làm.
- [ ] Claim về khái quát phù hợp backbone/dataset đã kiểm chứng.

### 19.2. Thực nghiệm và thống kê

- [ ] H/W/Q disjoint theo ảnh gốc; AB/BA đúng cùng batch multiset.
- [ ] Không có target-label tuning hoặc rò rỉ reserve vào phát triển.
- [ ] Full-state replay, cold-reset, sham và timing control đạt.
- [ ] Đủ inventory đã đăng ký hoặc công khai trạng thái thiếu/failed.
- [ ] CI dùng đơn vị panel và giả định hợp lệ; scenario/seed không bị nhân thành n giả.
- [ ] Multiplicity H2 và các phân tích exploratory được xử lý rõ.
- [ ] Báo cả accuracy/loss và chi phí; không chỉ disagreement.
- [ ] Raw audit và replay độc lập của một tập điều kiện đại diện đạt.

### 19.3. Bài viết và artifact

- [ ] Mỗi con số truy được về file kết quả và mã phân tích.
- [ ] Bảng/hình thể hiện đúng đơn vị, n, CI/SD, selection rule và giới hạn.
- [ ] README hướng dẫn được một người mới chạy lại trên môi trường sạch.
- [ ] Checkpoint/dataset lớn có checksum và hướng dẫn lấy lại hợp lệ.
- [ ] LaTeX/PDF hoàn chỉnh đã được biên dịch và kiểm tra trực quan.
- [ ] Không còn câu dự kiến được viết như kết quả đã đạt.
- [ ] Một vòng hostile review cuối đã được giải quyết hoặc dẫn đến thu hẹp claim.
- [ ] Quy định venue, citation, anonymity và artifact được kiểm tra trước nộp.

Nếu một ô chưa đạt, ghi cụ thể nó chặn claim nào, cần thí nghiệm nào và ngân sách nào. Không đánh dấu hoàn thành chỉ để đóng dự án.

## 20. Danh sách hành động theo thứ tự ưu tiên

| Ưu tiên | Hành động của bạn | Sản phẩm cần bàn giao |
|---|---|---|
| 1 | Tiếp quản repo đúng đường dẫn; kiểm tra lại test/audit và tài nguyên đã lưu | `resumption_audit.md` |
| 2 | Đọc proposal/review, xác nhận phạm vi contribution và điều kiện chính | `contribution_positioning.md` và protocol không mâu thuẫn |
| 3 | Phê duyệt hoặc điều chỉnh pilot budget; chuẩn bị host và cơ chế kết thúc tính phí | Quyết định ngân sách + thông tin môi trường chạy |
| 4 | Chạy pilot, audit, phân tích và quyết định tiếp tục/sửa/dừng | `pilot_report.md` và raw đầy đủ |
| 5 | Tích hợp baseline gần đây/persistent và các đối chứng cơ chế cần thiết | Mã, implementation cards, parity/state tests |
| 6 | Hoàn thiện sampler reserve, runner, CI và freeze confirmation | `confirmation_plan.md`, config/manifests, dự toán |
| 7 | Chạy xác nhận và replication đã được duyệt | Bảng H1/H2, consequences, ablation, robustness |
| 8 | Viết lại bài theo phát hiện thật, tái lập và phản biện cuối | Paper, supplementary, artifact và PDF đã kiểm tra |

**Mốc gần nhất cần đạt:** Một pilot ImageNet-C hợp lệ cùng báo cáo quyết định có căn cứ. **Mốc cuối cần đạt:** Một phát biểu khoa học có phạm vi rõ, được hỗ trợ bởi dữ liệu, thống kê, đối chứng và khả năng tái lập — dù kết quả cuối là persistence, practical washout hay một giới hạn của cách triển khai/đánh giá.

---

## Tài liệu nền trong repo

- [README và lệnh chạy hiện có](README.md)
- [Trạng thái nghiên cứu](research/status.md)
- [Proposal và giả thuyết](research/proposal.md)
- [Tổng quan tài liệu](research/literature_review.md)
- [Phân tích novelty](research/novelty_analysis.md)
- [Thiết kế và phản biện thống kê](research/design_audit.md)
- [Kết quả cục bộ và phân tích tác hại](research/stage_a_analysis.md)
- [Mô tả baseline](research/baseline_implementation.md)
- [So sánh SAR nguyên bản và bản sửa](research/sar_recovery_comparison.md)
- [Chuẩn bị dữ liệu cloud](research/data_preparation.md)
- [Dự toán pilot đã lập](research/cloud_gpu_request.md)
- [Phản biện và các điểm chưa đạt](research/reviewer_audit.md)
- [Phản hồi và phần còn thiếu](research/reviewer_response.md)
- [Bản thảo hiện tại](paper/paper.md)
- [Nhật ký nghiên cứu](research/research_log.md)

Các tệp kế hoạch mới được đề xuất trong tài liệu này chưa được coi là đã tạo hoặc hoàn thành. Tài liệu không cập nhật khảo sát công trình mới sau các nguồn đã có trong repo, không xác nhận giá GPU hiện tại và không khởi chạy bất kỳ thí nghiệm hay dịch vụ trả phí nào.
