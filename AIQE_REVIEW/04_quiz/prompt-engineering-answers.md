# Đáp án — Prompt engineering

[Câu hỏi](prompt-engineering.md) · [Ôn lại](../01_topics/prompt-engineering.md). Câu hỏi tự biên soạn.

1. **A.** Grounding gắn claim với bằng chứng. B nhầm chất lượng với độ dài; C chưa kiểm tra source thực sự hỗ trợ claim; D tên model không tạo bằng chứng.
2. **B.** Parse chỉ xác nhận cú pháp. A cần semantic validation; C vẫn cần review; D cần runtime evidence độc lập.
3. **C.** Nguồn thiếu thì theo dõi clarification. A tự bịa oracle; B che thiếu sót; D biểu quyết không tạo thẩm quyền nghiệp vụ.
4. **D.** Ví dụ nằm trong input. A là quá trình cập nhật model khác; B là quyền quyết định; C không cung cấp ví dụ.
5. **A.** Giữ điều kiện so sánh và đo cả chất lượng. B thay task làm nhiễu; C cherry-pick; D đếm dung lượng không đo source correctness.
6. **B.** Có decision owner và disposition. A bỏ accountability; C bỏ nội dung; D tìm sự đồng thuận chứ không kiểm tra nguồn.
7. **C.** Bảo vệ dữ liệu trước khi gửi và kiểm tra đầu ra. A đã làm lộ dữ liệu trước khi masking; B vẫn lộ secret; D bỏ rò rỉ ở log/output.
8. **D.** Nhãn và scope giúp người nghe hiểu giới hạn. A và B vượt bằng chứng; C dùng chất lượng trình diễn để che loại bằng chứng.
