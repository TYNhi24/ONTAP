# Quiz — Nền tảng QA

Câu hỏi tự biên soạn, không phải đề thi chính thức. Mỗi câu chọn một đáp án đúng nhất. [Bài ôn](../01_topics/qa-foundations.md) · [Đáp án](qa-foundations-answers.md).

## 1. [Nhận biết] Căn cứ phù hợp nhất cho expected discount là gì?

A. Rule được duyệt có phiên bản.
B. Câu trả lời AI có confidence cao.
C. Hành vi của sản phẩm khác.
D. Số tiền UI vừa hiển thị, không cần đối chiếu.

## 2. [Hiểu] Quantity cho phép số nguyên 1–10. Bộ nào nhắm vào hai phía biên?

A. 2, 4, 6, 8.
B. 0, 1, 10, 11.
C. 1, 1, 1, 1.
D. 5, 5, 10, 10.

## 3. [Vận dụng] VIP 10%, campaign hợp lệ 15%, không cộng dồn, chọn cao nhất. VIP có campaign hợp lệ nhận bao nhiêu?

A. 10%.
B. 25%.
C. 15%.
D. Chưa xác định dù đã có đủ rule.

## 4. [Hiểu] Muốn kiểm tra refund xảy ra trước và sau khi paid, mô hình phù hợp nhất là gì?

A. Chỉ kiểm tra độ dài chuỗi refundReason.
B. Đếm tổng số test đã tạo.
C. Chỉ so giao diện giữa hai browser.
D. State transition với sự kiện và trạng thái có nguồn.

## 5. [Nhận biết] Trường hợp nào là product risk?

A. Có khả năng thu tiền trùng khi retry.
B. Người kiểm thử nghỉ phép.
C. Account test chưa cấp đúng hạn.
D. Lịch review bị dời.

## 6. [Vận dụng] Có 8 pass, 1 fail và 3 blocked trên 12 ca planned. Kết luận nào đúng?

A. Tất cả 12 ca đã chạy vì blocked cũng là kết quả chạy.
B. 9/12 ca đã chạy; phần blocked còn rủi ro chưa được đánh giá bằng execution.
C. Pass rate trên executed là 8/12.
D. Có thể kết luận release ready chỉ từ 8 pass.

## 7. [Hiểu] Mọi requirement có link ít nhất một test. Điều gì vẫn có thể xảy ra?

A. Chắc chắn không còn coverage gap.
B. Không cần xem quality của expected result.
C. Test có link nhưng oracle sai hoặc chỉ bao phủ happy path.
D. Đã chứng minh mọi hành vi runtime đúng.

## 8. [Vận dụng] Ngân sách ARTD giới hạn 12 scenario hoặc 180 phút, giới hạn nào chạm trước. Chọn 10 scenario tổng 200 phút thì sao?

A. Hợp lệ vì ít hơn 12.
B. Hợp lệ nếu thêm retry.
C. Tự động giảm thời gian dự kiến để vừa budget.
D. Không hợp lệ; cần chọn lại hoặc thống nhất thay đổi budget.
