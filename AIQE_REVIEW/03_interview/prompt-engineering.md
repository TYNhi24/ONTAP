# Phỏng vấn — Prompt và AI review

[Bài ôn](../01_topics/prompt-engineering.md). Câu hỏi tự biên soạn; dùng “Em sẽ…” khi chưa có trải nghiệm.

## 1. Prompt tốt cho review yêu cầu có gì?

**Kiểm tra:** task boundary và nguồn.

**Trả lời 30–60 giây:** “Em sẽ nêu task nhỏ, nguồn đã duyệt có ID, tiêu chí review, điều không được tự suy diễn và định dạng output. Em yêu cầu phân biệt fact, assumption, question và suggestion. Prompt phải dẫn tới artifact có thể kiểm tra, không chỉ câu trả lời nghe hay.”

**Hỏi sâu:** yêu cầu sourceId cho từng expected result và ghi Not specified nếu thiếu; role prompt không tự tạo kiến thức sản phẩm.

**Sai lầm:** chỉ viết ‘hãy đóng vai chuyên gia’ rồi coi kết quả là chính xác.

## 2. Structured output có loại bỏ hallucination không?

**Kiểm tra:** phân biệt validation cấu trúc và ngữ nghĩa.

**Trả lời 30–60 giây:** “Không. Bảng hoặc JSON dễ parse có thể chứa rule sai. Em sẽ kiểm tra cấu trúc, đối chiếu sourceId và expected result với nguồn, rồi kiểm tra phép tính và ràng buộc bằng cách xác định. Dòng giảm giá 25% vẫn sai dù đủ mọi trường.”

**Hỏi sâu:** sourceId tồn tại cũng chưa đủ; cần xem source đó thực sự hỗ trợ claim hay không.

**Sai lầm:** đánh đồng parse thành công với nghiệp vụ đúng.

## 3. Làm sao biết prompt mới tốt hơn?

**Kiểm tra:** đánh giá thực nghiệm.

**Trả lời 30–60 giây:** “Em sẽ xác định tiêu chí như source correctness, gap detection và mức review cần thiết. Em so trước/sau trên cùng input có version, giữ cả trường hợp khó và negative. Em đo chất lượng trước rồi mới xem token hoặc tốc độ, để tránh tối ưu prompt bằng cách bỏ mất dữ liệu quan trọng.”

**Hỏi sâu:** tách bộ dùng điều chỉnh khỏi bộ dùng đánh giá cuối nếu đủ dữ liệu; ghi model/settings và không kết luận từ một lần sinh.

**Sai lầm:** đổi prompt và dataset cùng lúc rồi gán mọi cải thiện cho prompt.

## 4. AI đề nghị một rule hợp lý nhưng nguồn không nói thì làm gì?

**Kiểm tra:** giới hạn thẩm quyền.

**Trả lời 30–60 giây:** “Em sẽ ghi là suggestion hoặc question, giải thích rủi ro và nhờ đúng owner xác nhận. Em chưa dùng nó làm oracle hay đưa vào AC được duyệt. Em lưu quyết định để downstream test không vô tình coi bản draft là rule thật.”

**Hỏi sâu:** khi cần tiếp tục công việc, assumption phải có owner và trạng thái, không âm thầm trở thành fact.

**Sai lầm:** viện dẫn ‘thông lệ ngành’ làm bằng chứng cho hành vi sản phẩm cụ thể.

## 5. Dùng AI và báo khách hàng thế nào cho an toàn?

**Kiểm tra:** privacy và giao tiếp bằng chứng.

**Trả lời 30–60 giây:** “Em sẽ dùng nguồn tối thiểu đã được phép và dữ liệu tổng hợp, không gửi raw production data để nhờ AI che sau. Em review cả output và artifact. Khi báo kết quả, em nói rõ thiết kế đã review, mô phỏng hay đã chạy thật, nêu giới hạn và bước tiếp theo để khách hàng hiểu mức tin cậy.”

**Hỏi sâu:** log/trace cũng có thể chứa dữ liệu nhạy cảm; nơi lưu và cách chia sẻ cần nằm trong phạm vi review.

**Sai lầm:** nghĩ rằng input an toàn thì mọi artifact sinh ra đều an toàn, hoặc demo đẹp có nghĩa release ready.
