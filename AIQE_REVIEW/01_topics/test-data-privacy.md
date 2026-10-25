# Dữ liệu kiểm thử, giá trị biên và quyền riêng tư

## Mục tiêu, tiên quyết và phạm vi

Bạn cần tự thiết kế dữ liệu đúng mục đích kiểm thử, phát hiện dữ liệu AI trông hợp lý nhưng sai ràng buộc, và giữ an toàn trước khi dùng AI. Học [yêu cầu và thiết kế kiểm thử](requirement-test-design.md) trước để xác định scenario/oracle. **Bắt buộc:** data dictionary, boundary, expected validity, liên kết bảng, dữ liệu synthetic, kiểm tra deterministic, reproducibility và cleanup. **Nên biết:** phân loại nhạy cảm, lựa chọn masking/tokenization và rủi ro linkage. **Mở rộng trong khóa:** pairwise, kiểm tra phân phối, volume và các ranh giới thời gian phức tạp khi sản phẩm cần. Không mặc định áp daylight-saving vào mọi sản phẩm.

Nội dung diễn giải từ ARTD Unit 6 và nguyên tắc an toàn DALA; ví dụ tự biên, không có bổ sung web hay kết quả chạy môi trường thật.

## Từ khóa

| Từ khóa | Định nghĩa đầy đủ |
|---|---|
| Synthetic data | Dữ liệu tổng hợp là dữ liệu được tạo cho mục đích kiểm thử thay vì sao chép bản ghi khách hàng thật; vẫn phải kiểm tra bí mật, liên hệ hoạt động và ràng buộc. |
| Data dictionary | Từ điển dữ liệu mô tả ý nghĩa trường, kiểu, format, nullability, range, uniqueness, reference, quy tắc liên trường và mức nhạy cảm. |
| Expected-valid/invalid | Nhãn expected-valid/invalid nêu dữ liệu được thiết kế để thỏa hoặc vi phạm ràng buộc nào; dữ liệu invalid có chủ đích là tài sản kiểm thử, không tự động là lỗi generator. |
| Referential integrity | Toàn vẹn tham chiếu đảm bảo khóa ngoại trỏ tới bản ghi cha hợp lệ, chẳng hạn payment thuộc một order tồn tại. |
| Business invariant | Bất biến nghiệp vụ là quan hệ luôn phải đúng trong phạm vi trạng thái đã định nghĩa, chẳng hạn total sau discount khớp quy tắc tính tiền. |
| Direct identifier | Định danh trực tiếp là trường có thể nhận diện hoặc liên hệ một cá nhân, như tên, email hoặc số điện thoại. |
| Quasi-identifier | Gần định danh là trường có thể góp phần nhận diện cá nhân khi kết hợp với dữ liệu khác, như postal code và tháng sinh. |
| Masking | Che dữ liệu là biến đổi hoặc loại bỏ giá trị để giảm phơi lộ; che một phần không tự bảo đảm người đó không thể bị nhận diện lại. |
| Pseudonymization | Giả danh hóa thay định danh bằng giá trị đại diện nhưng còn khả năng liên kết với chủ thể qua thông tin bổ sung; không đồng nghĩa dữ liệu đã vô danh. |
| Tokenization | Tokenization thay giá trị bằng token và quản lý liên hệ theo cơ chế riêng; token cần vẫn được bảo vệ nếu có thể dùng để liên kết hoặc truy xuất giá trị. |
| Deterministic validation | Kiểm tra xác định dùng quy tắc/script/query cho kết quả có thể tái lập thay vì hỏi mô hình đánh giá bằng cảm tính. |
| Reproducibility | Khả năng tái tạo là việc tạo lại được dataset và kết quả kiểm tra khi có đủ seed, generator/version, nguồn, đồng hồ tham chiếu và môi trường liên quan. |

## 1. Bắt đầu từ scenario, không bắt đầu bằng “sinh 1.000 dòng”

**Input:** scenario IDs, rule/contract đã phê duyệt, schema, môi trường và chính sách dữ liệu. **Xử lý:** xác định mục đích từng hàng, lớp/biên, trạng thái, expected validity, liên hệ và mức nhạy cảm; chỉ nhờ AI gợi ý trong phạm vi đó. **Output:** scenario-to-data map, data dictionary, dataset version, validation report và hướng dẫn vận hành.

Ví dụ `SC-QTY-LOW` cần quantity `0` với customer UUID hợp lệ, SKU còn hàng, paymentMethod `CARD` và các trường khác đúng để riêng quantity gây lỗi. Nếu cùng lúc customer không tồn tại, JSON malformed và quantity 0, hệ thống có thể dừng ở lỗi khác; ca không còn chẩn đoán đúng mục tiêu. Test nhiều lỗi cùng lúc vẫn có thể có mục tiêu riêng nhưng phải ghi rõ, không trộn vào bộ cô lập vi phạm.

Schema tối thiểu ARTD có `customers → orders → order_items/payments/refunds`. Giữ cùng customer synthetic qua các bảng. Đừng sinh lại ID độc lập ở từng bảng vì cùng hình dạng UUID không tạo quan hệ đúng. Schema chưa định nghĩa hết vocabulary trạng thái và partial-refund structure; ghi câu hỏi, không tự hoàn thiện rồi gọi đó là approved.

## 2. Bộ biên phải có ý nghĩa và expected outcome

| Ràng buộc ARTD | Giá trị gợi ý tự biên | Điều cần giữ cố định |
|---|---|---|
| `quantity` nguyên 1–10 | 0, 1, 2, 9, 10, 11; thêm null/thiếu/chuỗi/số lẻ theo lớp | Mỗi giá trị được đặt vào một item hợp lệ về SKU và cấu trúc. |
| `items` 1–20 SKU phân biệt | Số phần tử 0, 1, 2, 19, 20, 21; thêm hai SKU trùng | Quantity và từng SKU khác vẫn hợp lệ. |
| `orderTotal` VND 1.000–50.000.000 sau giảm | 999, 1.000, 1.001; 49.999.999, 50.000.000, 50.000.001 | Total phải hình thành từ item/discount hợp lệ; không ghi total độc lập sai phép tính rồi tưởng chỉ thử biên. |
| `email` tối đa 254 ký tự | 253, 254, 255; thiếu/null/format sai riêng | Domain reserved và phần cấu trúc khác hợp lệ theo contract; độ dài không chứng minh format hợp lệ. |
| `refundReason` 10–500 Unicode characters | 9, 10, 11; 499, 500, 501 | Cần làm rõ cách đếm Unicode nếu code point, grapheme và byte cho kết quả khác. |

Giữ nhãn mỗi hàng: `dataset_id`, `scenario_id`, `purpose`, `expected_valid`, `target_rule`, `required_state`, `expected_result`. Một key trùng với cùng payload là tình huống replay có quy tắc idempotency, không phải lúc nào cũng là dữ liệu sai uniqueness. Cùng key/payload khác chưa có expected behavior được duyệt thì ghi clarification, không mặc định status `409`.

Temporal data cần đồng hồ tham chiếu cố định: tuổi order 30 ngày không kiểm tra bằng “hôm nay” thay đổi mỗi lần chạy. Nguồn nói 30 calendar days nhưng chưa xác định đầy đủ timezone/cutoff ở mọi trường hợp; hỏi owner trước khi assertion ở đúng mốc. Stateful data cần chuỗi trạng thái có ý nghĩa; một refund thành công cho order chưa từng paid có thể là intentional invalid case, không được trộn vào baseline hợp lệ.

## 3. Chọn cách bảo vệ theo mục đích và rủi ro

| Loại trường | Cách xử lý học trong khóa | Điều chưa được bảo đảm |
|---|---|---|
| Tên/email/phone | Tạo synthetic; dùng contact reserved/non-routable và kênh gửi được kiểm soát. | Tên “giả” không đủ nếu email/phone vẫn thuộc người thật. |
| Customer/order/payment IDs | Dùng ID synthetic, giữ ánh xạ nhất quán qua bảng. | Đổi ID không loại bỏ dữ liệu nhạy cảm còn trong transaction hoặc free text. |
| Postal code/birth month | Loại nếu không cần; nếu giữ phải đánh giá tổ hợp hiếm và khả năng linkage. | Không có tên không đồng nghĩa không nhận diện lại được. |
| PAN/CVV/access token/credential | Loại bỏ; dùng stub hoặc provider test token đúng môi trường. | Đổi nhãn hoặc hash không cho phép gửi bí mật gốc tới AI. |
| Amount/status/time | Tạo giá trị tổng hợp, giữ phép tính và state ordering cần kiểm tra. | Sao chép giao dịch hiếm có thể giữ dấu vết liên kết. |

Redaction xóa giá trị; substitution thay giá trị; shuffling hoán đổi có thể phá quan hệ; perturbation thay đổi số có thể phá biên/nghiệp vụ. Hash có thể giữ khả năng liên kết và bị đoán ở miền nhỏ. Encryption có thể đảo ngược với key, không tự tạo anonymization. Tokenization có thể hữu ích cho liên kết có kiểm soát; phải hiểu mapping, quyền truy cập và retention. Chọn fully synthetic khi không chấp nhận nguy cơ đảo ngược/linkage từ bản sao. Đây là hướng dẫn an toàn của khóa, không phải chứng nhận tuân thủ pháp lý.

Không tải raw production records lên AI để nhờ “làm sạch”. Việc phơi lộ xảy ra ngay tại input. Giảm dữ liệu và làm sạch trước trong quy trình được phê duyệt. Email `customer-01@example.com` chỉ là ví dụ reserved; vẫn cần kiểm soát outbound để không phát tán thông báo hoặc gây hoạt động ngoài ý muốn.

## 4. Xác minh dữ liệu và vận hành

Chạy kiểm tra theo tầng: parse/schema → type/format/range → uniqueness/references → cross-field/business/state → privacy/contact → mục đích coverage. Lưu rule, expected, actual và evidence cho cả pass lẫn expected failures. AI sinh bảng JSON đẹp chưa chứng minh JSON parse được, càng chưa chứng minh tổng tiền và foreign keys đúng.

Ví dụ self-check minh họa tự biên, chưa thay cho toàn bộ validator dự án:

```python
samples = [(0, False), (1, True), (10, True), (11, False)]
for quantity, expected_valid in samples:
    actual_valid = type(quantity) is int and 1 <= quantity <= 10
    assert actual_valid == expected_valid
```

Điểm cần hiểu: expected-invalid quantity 0 bị validator từ chối là **đạt mục đích kiểm tra dataset**. Kết quả này chưa nói API đã trả response đúng; API execution cần evidence riêng. Một kiểm tra quantity cũng không thay được schema, references hay privacy scan.

Lưu dataset version, source version, seed, generator version, fixed clock/timezone và prompt/reviewer. Seed không đảm bảo AI tạo lại chính xác cùng output; vì thế giữ artifact dataset đã phê duyệt hoặc hash/reference và generator xác định khi cần tái tạo. Setup gán namespace/run ID, isolate tài khoản/stock, reset phù hợp, giữ bằng chứng rồi teardown. Quy định expiry/retention và ai có quyền đọc; cleanup không được xóa dữ liệu ngoài scope hoặc xóa evidence trước khi điều tra.

## Ví dụ fresher nối đầu-cuối

Bạn kiểm tra không tạo payment khi quantity 0. Dựng một customer UUID synthetic active, SKU thực trong catalog staging, request `CARD`, quantity 0, key/correlation hợp lệ theo baseline. Gắn `DS-QTY-0` với scenario validation và nhãn invalid chỉ vì quantity. Validator chứng minh schema còn lại đúng và quantity bị từ chối theo rule. Chạy API chỉ khi được cấp môi trường: kiểm tra response theo contract và provider stub không nhận lệnh thu tiền. Lưu correlation ID, safe request/response, query stub và cleanup. Nếu mới thiết kế, ghi “chưa chạy”, không viết pass.

## Bẫy và điểm phỏng vấn

- “Đã mask tên” bỏ qua quasi-identifiers, free text và active contacts.
- “Có seed” bỏ qua version, đồng hồ và tính không xác định của AI.
- “24 dòng” không đủ nếu tất cả cùng lớp; mỗi dòng phải có test purpose.
- “Dữ liệu giống production” không tự đồng nghĩa đại diện đúng rủi ro; biên hiếm vẫn cần chủ động đưa vào.
- Ràng buộc Unicode, rounding và temporal cutoff chưa rõ phải thành câu hỏi; không chọn tùy ý cách thư viện đếm rồi coi đó là yêu cầu.

## Tự kiểm tra và nguồn

- [ ] Tôi ánh xạ scenario tới dataset và giải thích mục đích từng hàng.
- [ ] Tôi có expected-valid/invalid và rule vi phạm cụ thể.
- [ ] Tôi kiểm tra biên, keys/references, phép tính và thứ tự trạng thái.
- [ ] Không có production records, secrets, PAN/CVV hoặc contact có thể gây tác động thật.
- [ ] Tôi đánh giá linkage, không coi masking hay hash là bảo đảm vô danh.
- [ ] Tôi lưu version/seed/clock, validation evidence, setup/cleanup/expiry.

Nguồn: [ARTD course](../../document/AIQE%20AI-Assisted%20Requirement%20%26%20Test%20Design/L3_AIQE_ARTD_course_content.md), `Minimum exercise source pack` → Interface/data constraints, Minimal relational schema, Data inventory; Unit 6 Sessions 6.1–6.4, `EX-U6-DATA`, `5. Responsible AI working agreement`. [ARTD DOCX](../../document/AIQE%20AI-Assisted%20Requirement%20%26%20Test%20Design/L3_AIQE_ARTD_exercises.docx), heading `Unit 6 assessed exercise — Reproducible privacy-safe dataset` và schema/data inventory. [Deck EN](../../document/AIQE%20AI-Assisted%20Requirement%20%26%20Test%20Design/L3_AIQE_ARTD_training_deck_ready_v2.pptx), [deck VI](../../document/AIQE%20AI-Assisted%20Requirement%20%26%20Test%20Design/L3_AIQE_ARTD_training_deck_vi_final.pptx), slide 22–23 và speaker notes cùng số. [DALA EN](../../document/AIQE%20AI-Assisted%20Defect,%20API%20%26%20Log%20Analysis/L3_AIQE_DALA_course_content.md), mục `7. Responsible AI working agreement`, Sessions 3.1/3.4 và capstone execution rules. Slide text/notes được đọc từ XML; bố cục/charts native chưa render kiểm chứng.

Luyện [phỏng vấn](../03_interview/test-data-privacy.md), [trắc nghiệm](../04_quiz/test-data-privacy.md), [đáp án giải thích](../04_quiz/test-data-privacy-answers.md).
