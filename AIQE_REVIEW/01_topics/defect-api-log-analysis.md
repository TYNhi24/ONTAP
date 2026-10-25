# Điều tra defect, kiểm thử API và phân tích log

## Mục tiêu, tiên quyết và mức học

Fresher cần báo cáo được khác biệt expected/actual có bằng chứng, kiểm tra API sâu hơn status, ghép timeline đúng múi giờ và đề xuất giả thuyết có phép kiểm chứng. Học [thiết kế kiểm thử](requirement-test-design.md) và [dữ liệu an toàn](test-data-privacy.md) trước. Cần đọc HTTP/JSON, log có timestamp/service và biết thao tác công cụ API cơ bản.

**Bắt buộc:** oracle, defect report, severity/priority, phân loại evidence, request/response/schema/semantics/side effects, UTC/correlation, negative test và giới hạn kết luận. **Nên biết:** hypothesis matrix, discriminating check, idempotency/reconciliation và regression. **Mở rộng trong khóa:** concurrency, fault injection, evidence graph xuyên nhiều dịch vụ và kiểm tra compatibility. Chủ đề tổng hợp toàn bộ sáu unit DALA dành cho người có kinh nghiệm, diễn giải lại cho fresher; không yêu cầu tự chẩn đoán production.

Nội dung và case bắt nguồn khóa học; ví dụ phân tích và câu hỏi tự biên. Không có bổ sung từ web. Những observation trong case là dữ liệu đào tạo do nguồn cung cấp, không phải tác giả đã chạy hệ thống.

## Từ khóa và khác biệt cốt lõi

| Từ khóa | Định nghĩa đầy đủ |
|---|---|
| Defect report | Báo cáo defect là tài liệu mô tả khác biệt giữa hành vi kỳ vọng có nguồn và hành vi quan sát, đủ ngữ cảnh để tái lập hoặc điều tra. |
| Severity | Severity diễn tả mức tác động kỹ thuật/nghiệp vụ của lỗi, gồm tài chính, dữ liệu, bảo mật, khả dụng và khả năng khôi phục. |
| Priority | Priority là thứ tự xử lý do quyết định nghiệp vụ chịu ảnh hưởng bởi severity, tần suất, exposure, workaround và lịch phát hành. |
| Authentication | Authentication kiểm tra danh tính hoặc credential của người gọi có hợp lệ hay không. |
| Authorization | Authorization kiểm tra người gọi đã xác thực có quyền hành động trên tài nguyên cụ thể hay không. |
| API contract | API contract mô tả operation, input, auth, header, schema và response được cam kết; ví dụ payload không thay thế toàn bộ contract. |
| Schema validation | Kiểm tra schema đánh giá cấu trúc, kiểu, required field, enum và các ràng buộc hình thức đã được định nghĩa. |
| Semantic assertion | Assertion ngữ nghĩa kiểm tra ý nghĩa và quan hệ nghiệp vụ, ví dụ order thuộc đúng customer hoặc amount đúng theo rule. |
| Side effect | Side effect là thay đổi bền vững hoặc tác động bên ngoài do request tạo ra, như reservation, capture payment, event hoặc notification. |
| Idempotency | Trong contract của case, cùng key và cùng payload được retry mà không tạo thêm order hoặc charge; không suy ra bảo đảm này cho mọi key khác. |
| Reconciliation | Đối soát là việc xác minh và đồng bộ kết quả khi response tức thì không đủ biết giao dịch bên ngoài thành công hay thất bại. |
| Correlation ID | Correlation ID liên kết các sự kiện thuộc một luồng qua dịch vụ; nó hỗ trợ điều tra, không tự ngăn xử lý trùng. |
| Request/entity ID | Request ID định danh một request tại phạm vi liên quan, còn entity ID định danh đối tượng nghiệp vụ như order; một order có thể có nhiều request và payment attempt. |
| Clock skew | Clock skew là độ lệch giữa đồng hồ các nguồn, khiến sắp xếp timestamp chưa chắc phản ánh thứ tự nhân quả. |
| Hypothesis | Giả thuyết là cơ chế giải thích có thể kiểm thử nhưng chưa được xác nhận; cần evidence hỗ trợ, phản chứng và phép kiểm phân biệt. |
| Root cause | Nguyên nhân gốc là cơ chế đã được xác minh trong phạm vi điều tra, không phải tên component được AI đoán từ nơi xuất hiện error. |

## 1. Quan sát → oracle → báo cáo có thể xử lý

**Input:** observation, environment/build, nguồn expected, safe evidence. **Xử lý:** bảo toàn evidence gốc, ghi điều kiện đã biết/chưa biết, đối chiếu expected với actual, nhờ AI sửa cấu trúc và tìm thiếu sót. **Output:** defect report, reproduction matrix, evidence index, severity rationale, câu hỏi priority và AI review log.

Một report có title nêu symptom/condition, environment/build/role/data, preconditions, numbered steps, expected/actual cùng mức chi tiết, frequency/scope, impact, severity rationale, workaround và evidence refs. Lỗi không tái lập liên tục vẫn báo được nếu nói rõ lần đã thấy và evidence đủ điều tra. Không đổi một lần quan sát thành “100% người dùng bị ảnh hưởng”. Vòng đời được dạy gồm draft, review, triage, assign, resolve, retest, reopen, close; resolve chưa thay cho retest/closure evidence.

Case nguồn: staging, mobile `4.8.2-rc3`, khách synthetic `CUST-SYN-1042`; submit lần đầu nhận `504`, ứng dụng báo payment failed, khách retry một lần; provider stub có hai capture VND 240.000, API có một order paid. Tiêu đề tốt: “Hai capture sau retry khi mobile nhận timeout ở checkout”. Tiêu đề “Mobile bug sinh key gây thu trùng” vượt bằng chứng vì ownership và cơ chế tạo key chưa được chứng minh.

Expected dẫn `BR-PAY-01`: timeout là outcome chưa xác định, không được báo chắc chắn thất bại. `BR-IDEM-01` bảo vệ same-key/same-payload; case này dùng **hai key khác nhau**, do đó không được nói đã chứng minh server vi phạm same-key idempotency. Impact tiền bị thu trùng đủ nghiêm trọng để đề xuất severity có lý do; priority còn cần frequency, exposure, workaround, thời điểm release và owner.

## 2. Nhãn bằng chứng và ma trận giả thuyết

| Nhãn DALA | Cách áp dụng vào case |
|---|---|
| FACT-SOURCE | `BR-PAY-01` quy định timeout chưa phải thất bại chắc chắn. |
| FACT-OBSERVED | Provider evidence ghi `pe-551` và `pe-552` đều CAPTURED. |
| INFERENCE | Luồng retry có thể liên quan tới việc tạo lần thu thứ hai. |
| HYPOTHESIS | Client sinh key theo mỗi tap thay vì theo business intent. |
| CONTRADICTED | “Khoản thu đầu thất bại” mâu thuẫn với capture `pe-551`. |
| UNKNOWN | Chưa biết ownership vòng đời key và kiểm soát server độc lập phải có. |

Confidence là confirmed/strongly supported/possible/weak/ruled out **for this run**, không phải phần trăm tự tin của AI. Giữ đối chiếu này ở cả bản kỹ thuật lẫn bản cho business; đổi audience không làm tăng mức chắc chắn.

| Giả thuyết minh họa tự biên | Hỗ trợ / giới hạn | Kiểm tra phân biệt an toàn |
|---|---|---|
| Client thay key trong retry | Seed có `idem-b91f` rồi `idem-c44a`; chưa thấy code hoặc chính sách lifetime. | Ghi request của một retry có kiểm soát, review quy tắc lifetime/code được cấp quyền. |
| Server không chặn capture lần hai theo cùng business intent | Cùng `ORD-90017` gắn hai payment; chưa có contract cho khác key. | Hỏi control kỳ vọng, xem transition/guard và thử bằng stub trong môi trường cho phép. |
| Provider tự retry một request | Hai capture có provider request khác `pr-881/pr-882`, nên câu chuyện một request retry bị yếu đi. | Đối chiếu provider request/event map và adapter outbound evidence. |

Không chỉ thu “thêm log” vô hướng. Mỗi check cần dự đoán nếu giả thuyết đúng/sai, chi phí, quyền truy cập và cách làm không phá evidence. Theo khóa, xác nhận nguyên nhân cần tái lập kiểm soát, cơ chế thể hiện trong code/config hoặc hành vi xác định, và bản sửa/loại bỏ cơ chế triệt tiêu lỗi mà không có bằng chứng phản bác. Nếu chưa đủ, viết provisional conclusion và next action. Five Whys/fishbone chỉ tổ chức suy nghĩ, không tự tạo proof.

## 3. Log: chuẩn hóa trước, liên kết sau, kết luận cuối

**Input:** nguồn log/API/UI/provider, metadata timezone, clock, sampling và retention. **Xử lý:** parse, giữ rejected lines, giữ timestamp gốc, normalize UTC, nối các ID, so baseline và xác minh count/join bằng query/script. **Output:** timeline, identifier map, anomaly table, reliability note và các query có thể chạy lại.

`14:03:18.420 +07:00` bằng `07:03:18.420Z`, không phải lệch bảy giờ giữa các sự kiện. Case có các mốc sau:

| UTC theo nguồn | Sự kiện và ý nghĩa |
|---|---|
| 07:03:18.501 | Gateway nhận request đầu `corr-7a01`. |
| 07:03:21.612 | Gateway trả 504, duration 3.111 ms. |
| 07:03:22.426 | Provider capture lần đầu `pe-551`; adapter ghi nhận lúc .430. |
| 07:03:22.980 | Người dùng retry theo recording đã chuyển UTC. |
| 07:03:23.020 | Gateway nhận retry `corr-7a02`. |
| 07:03:23.476 | Provider capture lần hai `pe-552`. |
| 07:03:23.550 | Gateway trả 201 cho retry. |

Hai capture cách nhau 1.050 giây theo provider evidence; capture đầu đến sau gateway timeout 0.814 giây theo hai nguồn, nên vẫn phải xét độ chính xác/clock metadata trước khi diễn giải nhân quả chính xác dưới giây. Event time, ingestion time và processing time khác nhau; buffering và queue có thể đổi thứ tự log xuất hiện. Dùng causal link và sequence/state cùng timestamp.

Chỉ tìm `corr-7a02` sẽ bỏ lần đầu. Chỉ tìm order ID có thể bỏ payment timeout không ghi order. Pivot qua correlation → payment/provider request → provider event → order, ghi rõ quan hệ một-nhiều. Idempotency key là control xử lý replay, correlation ID là control quan sát, order ID là entity; không dùng thay thế lẫn nhau.

Anomaly phải lệch baseline/invariant rõ ràng: hai capture cho một luồng đặt hàng, thiếu transition audit, correlation không truyền, retry burst hoặc dữ liệu nhạy cảm. `ERROR` có thể là lỗi input dự kiến; “không thấy release log” chưa chứng minh không release nếu sampling/retention thiếu. Báo riêng vấn đề observability và vấn đề khách hàng. Bài `EX-U3-LOGS` yêu cầu parse ít nhất 95% **valid supplied records**, ghi malformed/rejected riêng, không sửa mẫu số để giấu parser lỗi.

## 4. API: nhiều tầng oracle

Request gồm method/path/query, authentication, header và body; kiểm tra cả thiếu/null/rỗng/sai kiểu/format. Response cần status **theo operation**, media type và correlation header, schema, semantic relationships, expected side effects và forbidden side effects. Ví dụ `201` với amount sai hoặc charge hai lần vẫn không đạt dù JSON đủ field. Schema không tự chứng minh customer sở hữu order hay payment đúng một lần.

Theo **baseline DALA**, `POST /orders` quantity nguyên 1–10, items 1–20 SKU phân biệt, customerId UUID khớp authenticated customer, `CARD/WALLET`, unknown fields bị từ chối. `201` đi với PAID; `202` đi với PAYMENT_PENDING và statusUrl. `400` là request validation; `401` thiếu/invalid authentication; `403` cho POST dùng identity khác; `404` SKU không tồn tại; `500` phải có safe generic message/correlationId, không stack trace. GET cross-customer cố ý chưa chốt `403` hay `404`, nhưng không được lộ đơn người khác theo `BR-AUTH-01`.

**Không trộn baseline:** ARTD có mâu thuẫn `201/PENDING_PAYMENT` riêng; không lấy DALA âm thầm sửa ARTD. DALA contract đòi UUID headers nhưng seed dùng chuỗi rút gọn `corr-7a01/idem-b91f`; giữ chúng đúng khi phân tích bằng chứng, dùng UUID hợp lệ khi dựng request chạy theo contract, ghi rõ khác biệt fixture. Bản VI gọi dòng `400` là “Xác thực request thất bại”, dễ nhầm authentication; EN ghi “Request validation failed”, nên hiểu là validation input.

API test flow dùng Arrange–Act–Assert–Cleanup: setup dữ liệu riêng, thực hiện một hành động, kiểm tra các lớp, giữ safe evidence/correlation rồi reset. Test async dùng polling có deadline theo yêu cầu đã duyệt; một sleep cố định không chứng minh trạng thái cuối hoặc độ trễ hợp lệ. Một response sample từ AI hoặc stub chưa phải kết quả môi trường thật; phải ghi simulated/stubbed đúng bản chất.

## 5. Negative, retry, concurrency và kết thúc điều tra

Xây positive baseline trước, rồi negative cô lập từng vi phạm. Các lớp gồm missing/null/empty/wrong type, boundary, duplicate/unknown fields, malformed JSON, identity mismatch, object ownership, trạng thái cấm, dependency timeout và recovery. Cần **non-effect oracle**: input invalid không làm đổi order, reserve inventory hay tạo charge; error không lộ thông tin. Không mặc định status cho wrong media type hoặc same-key/different-payload khi case chưa quy định.

Same-key/same-payload kiểm tra không thêm order/charge; different-key/same business intent sau unknown outcome cần kiểm tra rủi ro riêng và clarification control. Concurrent submits cần quan sát durable effects, không chỉ hai response. Notification failure không rollback paid order theo `BR-NOT-01`; retry notification phải tránh trùng thông điệp. Inventory release theo `BR-INV-01` cần state/audit evidence, không chỉ UI báo lỗi.

Gói điều tra tích hợp gồm scope/source versions, defect, evidence index, timeline/map, API checks, log findings, hypotheses/confidence, unknowns/residual risk, regression/observability guidance và AI review. Preserve evidence trước mutation/cleanup. Fix verification chạy lại original flow, biến thể retry/timeout/idempotency, side effects và rủi ro liền kề; không đóng ticket chỉ vì developer gửi ảnh “fixed”.

## Ví dụ trả lời ngắn kiểu fresher

“Em xác nhận hai capture dựa vào provider events, và biết retry dùng key khác. Em chưa kết luận component nào là nguyên nhân. Em chuẩn hóa thời gian về UTC, nối hai correlation qua order/payment/provider request, rồi viết expected theo BR-PAY-01. Em đề nghị kiểm tra lifecycle key và server guard bằng stub an toàn. Em sẽ kiểm tra same-key replay riêng để tránh đánh đồng với case hiện tại, đồng thời giữ unknowns và bằng chứng chưa có.”

## Tự kiểm tra và nguồn

- [ ] Tôi viết report có oracle/build/steps/evidence, không bịa frequency/root cause.
- [ ] Tôi phân biệt severity/priority và fact/hypothesis/confidence.
- [ ] Tôi normalize timezone nhưng giữ timestamp gốc, kiểm tra clock/source reliability.
- [ ] Tôi nối được cả hai attempt bằng nhiều ID, không dùng correlation làm idempotency.
- [ ] API assertion có status/header/schema/semantics/side effects/non-effects.
- [ ] Tôi không tự chốt status chưa quy định hoặc coi timeout là payment failed.
- [ ] Tôi giữ dữ liệu an toàn, provenance AI và next check có thể phản chứng giả thuyết.

Nguồn chính: [DALA EN course](../../document/AIQE%20AI-Assisted%20Defect,%20API%20%26%20Log%20Analysis/L3_AIQE_DALA_course_content.md), [DALA VI course](../../document/AIQE%20AI-Assisted%20Defect,%20API%20%26%20Log%20Analysis/L3_AIQE_DALA_course_content_vi.md), mục 5.2–5.5, 6–7, Unit/Học phần 1–6 với Sessions/Phiên 1.1–6.4, mục 8–13; [DALA exercises](../../document/AIQE%20AI-Assisted%20Defect,%20API%20%26%20Log%20Analysis/L3_AIQE_DALA_exercises.md), `EX-U1-DEFECT`, `EX-U2-RCA`, `EX-U3-LOGS`, `EX-U4-API-FOUNDATION`, `EX-U5-API-SCENARIOS`, `EX-U6-INTEGRATED` và rubric/critical caps tương ứng.

Luyện [phỏng vấn](../03_interview/defect-api-log-analysis.md), [trắc nghiệm](../04_quiz/defect-api-log-analysis.md), [giải thích đáp án](../04_quiz/defect-api-log-analysis-answers.md).
