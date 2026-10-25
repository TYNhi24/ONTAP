# Trắc nghiệm tự luyện: defect, API và log

Tự biên, không phải đề chính thức. Mỗi câu có **một đáp án tốt nhất**. Dùng baseline DALA, trừ khi câu hỏi nói khác. [Bài học](../01_topics/defect-api-log-analysis.md) · [Giải thích](defect-api-log-analysis-answers.md).

## D1. Gateway trả 504 nhưng provider ghi CAPTURED muộn. Kết luận nào đúng?

A. Khoản thu chắc chắn thất bại vì 504.
B. Provider event phải sai vì response đến trước.
C. Timeout không xác nhận payment failed; cần đối soát và giữ cả hai nguồn evidence.
D. Có thể cho retry bất kỳ key nào mà không cần kiểm tra side effect.

## D2. Hai capture, request đầu/retry có hai key khác nhau. Điều gì đã được chứng minh?

A. Hai capture và sự khác nhau của key; chưa tự chứng minh nguyên nhân hay vi phạm same-key contract.
B. Chắc chắn server idempotency hỏng trong same-key replay.
C. Mobile là owner duy nhất của defect.
D. Provider tự retry cùng một request.

## D3. 14:03:18.420 +07:00 tương ứng UTC nào?

A. 21:03:18.420Z.
B. 07:03:18.420Z.
C. 14:03:18.420Z.
D. Không thể đổi vì UTC không có millisecond.

## D4. API trả 201, schema hợp lệ nhưng customer A nhận dữ liệu order B. Kết luận tốt nhất?

A. Pass vì hai check kỹ thuật đã đạt.
B. Chỉ UI mới có trách nhiệm authorization.
C. Không cần bug nếu user không thấy link trên UI.
D. Vẫn có vi phạm ownership/authorization cần evidence; schema/status không đủ kiểm tra semantics.

## D5. Không có release event trong log sample. Phát biểu phù hợp nhất?

A. Chắc chắn inventory chưa release.
B. Không thấy trong tập đã thu; cần xét sampling/retention/coverage và kiểm tra state hoặc nguồn bổ sung.
C. Không thể điều tra gì thêm.
D. Thêm một release event giả để timeline đủ.

## D6. Cùng idempotency key nhưng đổi payload, DALA chưa quy định behavior. Expected nên là gì?

A. 409 vì thường gặp.
B. 200 vì giữ key là đủ.
C. Not specified; mở câu hỏi contract và chưa tự chốt status/business behavior.
D. 500 vì payload đã thay đổi.

## D7. Negative test quantity 0 trả 400 đúng contract. Check bổ sung nào có giá trị nhất?

A. Safe error/correlation và không tạo order/payment/reservation ngoài cam kết.
B. Chỉ đếm số ký tự của message rồi so với AI.
C. Cho phép tạo payment vì request cuối cùng đã bị từ chối.
D. Xóa log ngay để giảm thời gian cleanup.

## D8. Hai hypothesis khác nhau đều giải thích symptom. Cách dùng AI tiếp phù hợp nhất?

A. Chọn cái AI viết dài nhất làm root cause.
B. Hỏi AI lặp lại đến khi cả hai lần đồng ý.
C. Hạ hết unknown thành fact để summary ngắn.
D. Yêu cầu supporting/contradicting evidence và check có outcome phân biệt, rồi xác minh trong điều kiện được phép.
