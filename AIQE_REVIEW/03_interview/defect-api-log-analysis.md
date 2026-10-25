# Phỏng vấn: defect, API và log

Tự biên, không phải bộ câu hỏi chính thức. Đọc [bài học và nguồn](../01_topics/defect-api-log-analysis.md). Mỗi gợi ý có thể trình bày trong 30–60 giây.

## 1. UI báo payment failed sau timeout; bạn ghi actual thế nào?

**Ý định:** phân biệt UI observation với kết quả thanh toán.

**Gợi ý trả lời:** Em ghi UI hiển thị payment failed và gateway trả 504 theo evidence, không khẳng định payment thực sự thất bại. Theo BR-PAY-01 timeout là outcome chưa xác định cho đến đối soát. Em thu build/environment, request/correlation, recording và provider evidence; nếu provider có capture muộn em cập nhật fact và chỉ rõ mâu thuẫn với thông điệp UI. Report expected/actual tách biệt và root cause để hypothesis. Không có dữ liệu tần suất thì em ghi chưa biết scope, không nói mọi người đều bị.

**Đào sâu:** Bạn đề xuất severity và priority thế nào? **Lỗi thường gặp:** đồng nhất timeout với decline, hoặc khẳng định gateway gây lỗi nghiệp vụ.

## 2. Response 201 và JSON schema pass có đủ kết luận API đúng không?

**Ý định:** kiểm tra oracle nhiều lớp.

**Gợi ý trả lời:** Chưa. Em xác nhận status theo operation, header/media type/correlation, field/type/enum, rồi semantics như customer ownership, amount và status. Em kiểm tra side effects như order/payment/audit và forbidden effects như charge trùng hoặc lộ dữ liệu. Schema hợp lệ không chứng minh tính tiền hay phân quyền đúng. Với response async em theo statusUrl và polling có deadline đã duyệt. Expected chưa quy định thì em mở clarification thay vì sửa test theo behavior hiện tại.

**Đào sâu:** Một negative test validation cần kiểm tra non-effect nào? **Lỗi thường gặp:** assertion duy nhất `status == 201` hoặc snapshot nguyên body bất chấp ID/time biến đổi.

## 3. Làm sao nối hai retry khi correlation ID thay đổi?

**Ý định:** kiểm tra timestamp/ID reasoning.

**Gợi ý trả lời:** Em normalize mọi thời gian về UTC và giữ timestamp gốc, kiểm tra timezone, clock skew, sampling và retention. Em không chỉ tìm một correlation; pivot qua order, payment, provider request/event và action recording để lập map hai attempt. Một order có thể có nhiều request và payment. Em phân biệt event time với ingestion time và không coi thứ tự log hiển thị là nhân quả. Counts, durations và joins AI đề xuất phải xác minh bằng query/script có thể chạy lại.

**Đào sâu:** 14:03:18.420 +07:00 bằng UTC nào, và log không có release chứng minh gì? **Lỗi thường gặp:** trừ sai múi giờ, tìm riêng order ID hoặc coi absence là proof không có sự kiện.

## 4. Hai capture và hai key khác nhau đã chứng minh server idempotency lỗi chưa?

**Ý định:** kiểm tra giới hạn contract và causal claim.

**Gợi ý trả lời:** Chưa chứng minh vi phạm quy tắc same-key/same-payload. Em xác nhận hai capture và key khác nhau từ source, còn lifecycle key và server control theo business intent là câu hỏi hoặc hypothesis. Em thử same-key replay riêng trong stub để kiểm tra contract, rồi kiểm tra khác-key retry theo hành vi được làm rõ. Em xây giả thuyết client key misuse, server guard gap hoặc provider/adapter behavior với bằng chứng hỗ trợ và phản bác. Em không gán ownership từ kết quả AI.

**Đào sâu:** Same-key/different-payload phải trả 409 không? **Lỗi thường gặp:** tự chốt 409, dùng correlation ID thay idempotency key hoặc gọi mọi duplicate là cùng nguyên nhân.

## 5. Bạn dùng AI cho RCA mà tránh kể chuyện nhân quả thế nào?

**Ý định:** kiểm tra hypothesis discipline và human accountability.

**Gợi ý trả lời:** Em dựng timeline và source pack đã làm sạch trước, yêu cầu AI trích evidence IDs và tách fact/inference/hypothesis/unknown. Mỗi hypothesis cần cơ chế, scope, supporting/contradicting evidence và check có kết quả phân biệt dự kiến. Em chủ động tìm phản chứng, hạ confidence khi evidence trái, và xác minh counts/timestamps bằng công cụ xác định. Em chỉ gọi confirmed khi kiểm tra kiểm soát và cơ chế đủ chứng minh; nếu chưa thì viết provisional note, limitation và next action. Con người review mọi quyết định quan trọng.

**Đào sâu:** “Thu thêm log” khác discriminating check ở đâu? **Lỗi thường gặp:** root cause chính là câu AI nói tự tin nhất hoặc lấy tương quan thời gian làm nguyên nhân.
