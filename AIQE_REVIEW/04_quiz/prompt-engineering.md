# Quiz — Prompt engineering

Câu hỏi tự biên soạn, không phải đề thi chính thức. Mỗi câu chọn một đáp án đúng nhất. [Ôn](../01_topics/prompt-engineering.md) · [Đáp án](prompt-engineering-answers.md).

## 1. [Nhận biết] Grounding có ý nghĩa gì trong review test?

A. Ràng buộc claim về sản phẩm với nguồn có thể kiểm tra.
B. Tăng độ dài prompt tối đa.
C. Tin mọi câu trả lời có dẫn một sourceId bất kỳ.
D. Dùng model có tên mới nhất.

## 2. [Hiểu] JSON parse thành công chứng minh điều gì?

A. Mọi business rule đều đúng.
B. Chuỗi thỏa cú pháp JSON, chưa chứng minh đúng nghiệp vụ.
C. Người review không cần kiểm tra nữa.
D. Đã chạy thành công trên hệ thống thật.

## 3. [Vận dụng] Rule không nói rõ cùng idempotency key nhưng payload khác. AI đề nghị luôn trả 409. Nên làm gì?

A. Đưa 409 vào expected vì có vẻ hợp lý.
B. Xóa scenario để không còn gap.
C. Ghi Question/Not specified, chuyển owner xác nhận.
D. Chạy nhiều model rồi lấy đa số làm rule.

## 4. [Hiểu] Few-shot trong bài này là gì?

A. Thay đổi trọng số model bằng training job.
B. Cho AI quyền quyết định release.
C. Chỉ thêm câu ‘hãy chính xác’.
D. Đưa vài ví dụ input–output vào context để minh họa mẫu.

## 5. [Vận dụng] Muốn so prompt trước/sau, cách nào đáng tin nhất?

A. Cùng bộ input có version, tiêu chí cố định, kiểm tra chất lượng và cost.
B. Prompt mới dùng task dễ hơn và so số token.
C. Chọn một câu trả lời đẹp nhất cho mỗi prompt.
D. Chỉ đếm số dòng output.

## 6. [Nhận biết] Bước Decide trong vòng ARTD nhấn mạnh gì?

A. Model tự ký duyệt mọi đề xuất.
B. Con người chấp nhận, sửa, từ chối hoặc chuyển quyết định có trách nhiệm.
C. Chỉ sửa định dạng.
D. Chạy lại đến khi output đồng ý với mình.

## 7. [Vận dụng] Muốn AI tạo dữ liệu an toàn, lựa chọn nào phù hợp nhất?

A. Upload toàn bộ production DB rồi nhờ che tên.
B. Gửi password thật nhưng bỏ tên user.
C. Dùng dữ liệu tổng hợp được phép và review ràng buộc/rò rỉ.
D. Chỉ kiểm tra input, không kiểm tra artifact.

## 8. [Hiểu] Demo mô phỏng thành công nên báo thế nào?

A. Toàn bộ sản phẩm đã pass live.
B. Agent đã được chứng minh production ready.
C. Không cần nói loại bằng chứng nếu UI đẹp.
D. Ghi rõ simulated, phạm vi được chứng minh và phần live chưa kiểm tra.
