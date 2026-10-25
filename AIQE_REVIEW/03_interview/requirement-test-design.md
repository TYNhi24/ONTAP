# Phỏng vấn: yêu cầu và thiết kế kiểm thử

Các câu hỏi và gợi ý tự biên để luyện fresher, không phải đề chính thức. Đọc [bài học và nguồn](../01_topics/requirement-test-design.md) trước. Mỗi đáp án là khung nói khoảng 30–60 giây, nên điều chỉnh bằng trải nghiệm thật.

## 1. Bạn xử lý “Checkout phải nhanh và an toàn” thế nào?

**Ý định:** kiểm tra testability và khả năng không tự thêm requirement.

**Gợi ý trả lời:** Em tách performance và security thành hai nhóm quan tâm. Với “nhanh”, em hỏi thời điểm bắt đầu/kết thúc đo, percentile, tải, môi trường và ngưỡng được chấp nhận. Với “an toàn”, em hỏi hành vi/control và oracle cụ thể liên quan sản phẩm. Em lập clarification register có source ID, tác động, owner và ưu tiên. Em có thể nhờ AI tìm câu hỏi còn thiếu nhưng mọi ngưỡng mới đều là đề xuất, chưa phải approved. Nếu chưa có quyết định, em ghi Not specified hoặc blocked thay vì tự đặt expected.

**Đào sâu:** Given/When/Then có khiến yêu cầu tự động testable không? **Lỗi thường gặp:** chọn “2 giây” hoặc một checklist security chung rồi coi là đặc tả.

## 2. Matrix có 100% requirement linked, có đủ coverage chưa?

**Ý định:** phân biệt liên kết hình thức với kiểm chứng hành vi.

**Gợi ý trả lời:** Chưa đủ. Em xem từng link có action, điều kiện và oracle kiểm tra đủ hành vi hay chỉ trùng từ khóa. Em phân loại Full, Partial, Indirect, None hoặc Blocked/Not testable và kiểm tra chiều role, negative, state/recovery, integration, NFR. Ví dụ ca mở order details chưa chứng minh user A không đọc được order B. Em tách coverage thiết kế khỏi kết quả đã chạy và ưu tiên xử lý gap theo rủi ro. Số ca hay tỷ lệ link chỉ là thông tin hỗ trợ.

**Đào sâu:** Một ca ở tầng thấp có thể tạo indirect coverage ra sao? **Lỗi thường gặp:** gọi mọi requirement có một test ID là Full hoặc pass.

## 3. VIP có campaign hợp lệ, bạn thiết kế kiểm thử gì?

**Ý định:** xem có suy ra kỹ thuật và oracle từ business rule hay chỉ kể happy path.

**Gợi ý trả lời:** Theo BR-DIS-01, VIP được 10%, campaign hợp lệ 15%, không cộng, chọn mức hợp lệ cao nhất. Em dựng bảng quyết định hai chiều VIP/campaign với bốn tổ hợp, kiểm tra precedence và ví dụ số tiền cụ thể. Với subtotal 240.000 thì giảm 36.000, còn 204.000; đây là expected tính từ rule, chưa phải kết quả chạy. Em thêm lớp mã hết hạn/không hợp lệ nếu nguồn định nghĩa, boundary về total và rounding theo half-up. Dữ liệu phải synthetic, có stock/setup và cleanup độc lập.

**Đào sâu:** Làm sao phát hiện AI tạo bảng 25% nhưng diễn đạt rất tự tin? **Lỗi thường gặp:** expected “discount đúng”, cộng hai discount hoặc tự sáng tạo eligibility.

## 4. Thay đổi hoàn tiền theo dòng ảnh hưởng những gì?

**Ý định:** kiểm tra change-impact xuyên lớp và quản lý decision gaps.

**Gợi ý trả lời:** Em baseline CR-01 rồi lần từ refund rule sang UI/API, dữ liệu quantity, payment, trạng thái order/refund, authorization, approval, audit, notification và regression. Em hỏi cumulative approval, hoàn lặp, discount/shipping allocation, rounding và concurrency vì nguồn cố ý chưa chốt. Em phân biệt asset cần sửa, cần thêm, cần retest hoặc lỗi thời; ghi owner và confidence. Em không dùng AI tự quyết cách chia tiền rồi sửa expected cho suite pass.

**Đào sâu:** Bạn ưu tiên gap nào trong budget 12 scenario/180 phút? **Lỗi thường gặp:** chỉ cập nhật màn hình refund, bỏ audit, cộng dồn và quyền duyệt độc lập.

## 5. Khi nào dùng case, charter hay checklist?

**Ý định:** đánh giá cách chọn tài sản kiểm thử và mức thực thi.

**Gợi ý trả lời:** Case phù hợp hành vi cần lặp lại với precondition, dữ liệu, bước, expected và cleanup rõ. Charter phù hợp mục tiêu học về rủi ro, có target/resources/timebox nhưng cho phép đổi đường đi khi có evidence mới. Checklist nhắc các điểm review lặp lại và phải có applicability. Em dùng case cho discount rule ổn định, charter cho mobile mất mạng sau submit, checklist để nhắc auth/error/privacy. Sau khám phá em lưu action/observation/question/bug riêng và debrief điều còn chưa biết, không gọi mọi observation là defect.

**Đào sâu:** Bạn làm gì nếu phiên chỉ là tabletop simulation? **Lỗi thường gặp:** biến charter thành script cứng hoặc coi checklist đã tick là đủ completeness.
