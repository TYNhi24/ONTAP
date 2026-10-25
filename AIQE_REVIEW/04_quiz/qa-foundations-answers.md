# Đáp án — Nền tảng QA

[Câu hỏi](qa-foundations.md) · [Ôn lại](../01_topics/qa-foundations.md). Câu hỏi tự biên soạn.

1. **A.** Rule đã duyệt là oracle. B chỉ là tự đánh giá của model; C không xác định sản phẩm đang test; D dùng chính actual làm expected sẽ bỏ sót lỗi.
2. **B.** Có dưới/đúng biên dưới và đúng/trên biên trên. A chỉ trong miền; C lặp một điểm; D bỏ phía ngoài biên. Bộ này chưa có nghĩa bao phủ mọi lớp dữ liệu.
3. **C.** Chọn mức hợp lệ cao nhất là 15%. A bỏ rule campaign; B vi phạm không cộng dồn; D bỏ qua nguồn đã đủ quyết định.
4. **D.** Thứ tự và trạng thái ảnh hưởng tính hợp lệ. A kiểm tra trường dữ liệu, không kiểm tra vòng đời; B chỉ là số lượng; C kiểm tra nền tảng nhưng không xác nhận transition.
5. **A.** Thu trùng tác động chất lượng và người dùng. B là nhân sự, C là readiness, D là lịch trình: đều thuộc rủi ro dự án trong ví dụ.
6. **B.** Executed=8+1=9; blocked phải báo riêng. A đếm sai executed; C đổi mẫu số của pass/executed; D bỏ qua lỗi, blocker và scope.
7. **C.** Link không đảm bảo nội dung test đủ hoặc đúng. A nhầm structural traceability với coverage; B bỏ qua oracle; D nhầm thiết kế với kết quả chạy.
8. **D.** Hai giới hạn phải cùng thỏa. A bỏ giới hạn thời gian; B retry không làm giảm budget; C sửa ước lượng vô căn cứ che rủi ro thay vì giải quyết.
