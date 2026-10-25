# Lab — Từ requirement tới dữ liệu và điều tra API

Bài tự biên soạn, không phải đề thi. Dùng tài liệu local như input; không tạo thêm kết quả chạy. Mục tiêu là nối ARTD với DALA bằng cách tư duy, **không trộn hai baseline API**.

Tiên quyết: [thiết kế test](../01_topics/requirement-test-design.md), [dữ liệu](../01_topics/test-data-privacy.md), [API/log](../01_topics/defect-api-log-analysis.md).

## Phần A — Thiết kế theo ARTD, 60 phút

Nguồn: [ARTD course](<../../document/AIQE AI-Assisted Requirement & Test Design/L3_AIQE_ARTD_course_content.md>), Confirmed business rules, Interface and data constraints, CR-01, Unit 3 và Unit 6.

1. Baseline rule discount và quantity, ghi source IDs/version. Tạo decision table bốn tổ hợp VIP/campaign. Với subtotal 240.000 và cả hai điều kiện đúng, tự tính discount và total bằng phép tính có thể kiểm tra; chưa gọi API.
2. Tạo tám dòng dữ liệu có mục đích gồm valid, quantity dưới/đúng/trên biên, missing và invalid type. Mỗi dòng ghi rule, expected-valid/invalid, lý do và trạng thái order cần có. Tách test sai kiểu khỏi test sai giá trị để failure có tính chẩn đoán.
3. Với refund, chọn một threshold trong nguồn, ghi đơn vị tiền và giả định đồng hồ. Ghi câu hỏi cutoff thay vì tự chọn timezone. Với partial refund CR-01, liệt kê những quyết định còn thiếu trước khi viết expected result.
4. Chọn ba scenario ưu tiên, mỗi scenario có risk/source/oracle/data/cleanup. Viết một case hoàn chỉnh và một charter có timebox. Yêu cầu AI tìm gap rồi giữ log accepted/edited/rejected; không cho đề xuất tự thay baseline.

Đầu ra: source-baseline, clarification-log, decision-table, dataset, cases và charter. Kiểm tra: không có 25% do cộng discount; không có dữ liệu thật; mọi dòng có mục đích; unresolved state conflict chưa bị đánh dấu Full.

## Phần B — Điều tra theo DALA, 60 phút

Nguồn: [DALA course EN](<../../document/AIQE AI-Assisted Defect, API & Log Analysis/L3_AIQE_DALA_course_content.md>), §5.3 contract, §5.4 seed và Units 1–6; [bài tập](<../../document/AIQE AI-Assisted Defect, API & Log Analysis/L3_AIQE_DALA_exercises.md>), EX-U1-DEFECT, EX-U2-RCA, EX-U3-LOGS, EX-U6-INTEGRATED.

1. Lấy nguyên seed evidence trong nguồn, ghi file/heading/line nếu xác định được. Tạo timeline: timestamp, service, correlation/request/entity/idempotency IDs, event, điều chứng minh và điều chưa biết. Không tự sinh thêm log cho lỗ hổng.
2. Viết ba giả thuyết cho duplicate charge. Mỗi giả thuyết có supporting/contradicting evidence, phép kiểm tra để phân biệt và kết quả nào làm bạn từ bỏ giả thuyết. Không coi gần nhau về thời gian là chứng minh nguyên nhân.
3. Viết bug report đủ build/environment/precondition/steps/expected/actual/evidence/impact. Mức severity/priority phải có lý do; nếu source không có build thì ghi unknown.
4. Thiết kế positive và negative API tests theo **contract DALA**. Chọn một test authorization, một same-key/same-payload và một unknown-write case. Với same-key/different-payload chưa chốt, output là clarification chứ không tự chọn 409.
5. Báo stakeholder trong một phút: fact, giả thuyết mạnh nhất, điều chưa biết, hành động tiếp và owner. Nói rõ đây là packet analysis, chưa phải tái hiện trên live API.

## Tự kiểm tra và tiêu chí hoàn thành

- [ ] Tất cả expected result đều có nguồn đúng baseline hoặc trạng thái chưa xác định.
- [ ] Bảng dữ liệu không có secret/contact người thật và giữ referential integrity khi có bảng liên quan.
- [ ] Timeline giữ nguyên ID nguồn dù fixture ID chưa đúng UUID constraint; có note về mâu thuẫn.
- [ ] Bug report không chuyển giả thuyết thành root cause đã xác nhận.
- [ ] Case negative kiểm tra cả việc side effect không xảy ra khi contract yêu cầu.
- [ ] Có danh sách thiếu evidence, không dùng placeholder để giả log hoặc report runtime.

Khi có môi trường được cấp, thực hiện từng case có dữ liệu riêng, thu actual artifacts rồi so expected. Bài tabletop hoàn tất ở thiết kế và phân tích bằng chứng đã có; trạng thái live vẫn chưa thực hiện.
