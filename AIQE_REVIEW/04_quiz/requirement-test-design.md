# Trắc nghiệm tự luyện: yêu cầu và thiết kế kiểm thử

Tự biên, không phải đề chính thức. Mỗi câu chỉ có **một đáp án tốt nhất** trong bối cảnh đã nêu. Đọc [bài học](../01_topics/requirement-test-design.md); làm xong mới xem [đáp án](requirement-test-design-answers.md).

## R1. NFR chỉ ghi “Checkout nhanh trong giờ cao điểm”. Bước phù hợp nhất?

A. Đặt expected dưới 2 giây theo kinh nghiệm.
B. Hỏi owner về phép đo, percentile, tải, môi trường và ngưỡng; ghi decision gap.
C. Đánh dấu không cần test vì chưa đo được.
D. Nhờ AI chọn benchmark rồi đưa thẳng vào baseline.

## R2. TC-LEG-07 chỉ mở trang order của chính customer. Link tới BR-AUTH-01 “chỉ xem order của mình” nên xử lý ra sao?

A. Full vì đã mở được trang order.
B. Full nếu AI confidence trên 90%.
C. Không chấp nhận nó như bằng chứng đầy đủ về authorization; bổ sung actor/object đối nghịch và oracle chống lộ dữ liệu.
D. Xóa BR-AUTH-01 vì không có automated test.

## R3. VIP 10%, campaign hợp lệ 15%, không cộng dồn. Với subtotal 240.000 VND, expected phù hợp là gì?

A. Giảm 25%, còn 180.000.
B. Giảm 10%, còn 216.000 vì VIP có sẵn.
C. Giảm 15%, còn 204.000.
D. “Discount đúng” để không phụ thuộc con số.

## R4. ARTD API nói 201/PENDING_PAYMENT, process note nói chỉ có order sau paid. Cách xử lý tốt nhất?

A. Chọn API vì API luôn ưu tiên.
B. Chọn note cũ vì đã tồn tại lâu hơn.
C. Nhờ AI bỏ một nguồn khỏi prompt để nhất quán.
D. Ghi conflict, ảnh hưởng và câu hỏi owner; chưa tự phê duyệt expected trạng thái.

## R5. CR-01 thêm partial refund nhưng bỏ ngỏ cumulative approval. Việc nào hợp lý nhất?

A. Giữ test cũ và đổi nút refund thành partial refund.
B. Dùng ngưỡng 2 triệu cho mỗi request và mặc định không cần cộng dồn.
C. Phân tích UI/API/data/payment/auth/audit/notification và mở câu hỏi cumulative approval, allocation, trạng thái, concurrency.
D. Chỉ thêm case quantity 1 vì đó là phần mới duy nhất.

## R6. Bạn có budget tối đa 12 scenarios và 180 phút. Kế hoạch nào đáp ứng đúng cả hai?

A. 13 scenarios tổng 150 phút vì đủ thời gian.
B. 10 scenarios tổng 175 phút, có rationale ưu tiên và residual risk cho ca hoãn.
C. 12 scenarios tổng 190 phút vì đúng số lượng.
D. Chỉ xếp theo điểm AI, không cần tính phút.

## R7. Tài sản nào đúng bản chất exploratory charter nhất?

A. 45 phút khám phá mobile sau mất mạng, dùng stub/API/log để tìm bất nhất trạng thái, có scope và điều kiện dừng.
B. 60 bước click bắt buộc theo thứ tự, không đổi dù có evidence mới.
C. Checklist mọi chủ đề QA, không có product context.
D. Mục tiêu “test tất cả checkout” không timebox hay rủi ro.

## R8. Case thanh toán bị decline có expected “hiện đúng lỗi”, cleanup “none”. Cải thiện tốt nhất?

A. Chỉ sửa câu expected thành “pass”.
B. Thêm selector CSS cụ thể nhưng giữ oracle cũ.
C. Chạy nó sau case tạo order để tận dụng state ngầm.
D. Chỉ rõ setup/stub, response/observable checkpoint theo nguồn, inventory/audit cần kiểm tra và cleanup/rerun an toàn.
