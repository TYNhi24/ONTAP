# Phỏng vấn: agent-architecture

Tự biên soạn, không phải câu hỏi/đáp án chính thức. Mẫu trả lời hướng đến 30–60 giây; hãy diễn đạt lại và thêm ví dụ của mình.

## 1. Planner, controller và runner khác nhau?

- Ý định: Kiểm tra boundary.
- Trả lời 30–60 giây: Em sẽ giải thích rằng planner đề xuất bước dựa context; controller kiểm tra state, quyền và budget; runner thực thi test và xuất assertion result. Tách ba vai trò ngăn model tự đổi oracle hoặc gọi tool tùy ý để tạo PASS. Trong bài lab, em sẽ cho planner đề xuất chạy EMP-CREATE-01 nhưng controller chỉ chấp nhận khi case, environment và grant phù hợp. Runner trả reporter cùng attempt ID để controller đối chiếu evidence. Nếu model muốn sửa assertion sau failure, em sẽ coi đó là đề xuất thay đổi cần review riêng, không phải bước chạy test bình thường.
- Hỏi sâu: Invariant nào phải enforce bằng code?
- Lỗi thường gặp: Cho planner quyền shell tự do.

## 2. Một tool contract cần gì?

- Ý định: Kiểm tra least privilege.
- Trả lời 30–60 giây: Em sẽ ghi input/output schema, target allowlist, side effect, timeout/budget, auth scope, redaction và owner. run_case chỉ nhận case/environment/run/revision đã validate; không nhận lệnh tự do. Tool output không tăng quyền cho workflow. Em sẽ xác định cả điều kiện từ chối, chẳng hạn run ID trùng, environment ngoài allowlist hoặc output không đúng schema. Với cleanup, input còn phải chứng minh record thuộc run đang xử lý. Những kiểm tra này cần nằm ở implementation và permission của tool, vì một prompt yêu cầu cẩn thận không chặn được mọi lời gọi sai.
- Hỏi sâu: Output schema sai xử lý thế nào?
- Lỗi thường gặp: Chỉ ghi tên tool không ghi scope.

## 3. Create timeout có retry được không?

- Ý định: Kiểm tra ambiguous write.
- Trả lời 30–60 giây: Em sẽ giải thích rằng timeout không chứng minh create chưa commit. Em sẽ ngừng write và dùng approved read lookup theo ID riêng để xác định existence và ownership. Nếu vẫn ambiguous thì báo unknown và chuyển human decision trong policy hiện tại. Em sẽ lưu lỗi timeout và kết quả lookup cùng timestamp, run ID để tránh nhầm record của lần chạy khác. Việc tìm thấy record chưa chứng minh các assertion UI đã chạy hoặc pass. Nếu không đủ bằng chứng về trạng thái hiện tại, em sẽ báo unknown và chuyển quyết định tiếp theo theo policy thay vì tạo thêm side effect.
- Hỏi sâu: Duplicate runId có đủ idempotency business không?
- Lỗi thường gặp: Retry create để chắc chắn.

## 4. Assertion pass, cleanup fail là trạng thái gì?

- Ý định: Kiểm tra hai tầng kết quả.
- Trả lời 30–60 giây: Em sẽ giữ assertion result pass của attempt, đồng thời ghi cleanup failed và workflow chưa hoàn tất hoặc blocked theo design course. Báo owned record còn lại và owner xử lý; không gọi toàn workflow passed. Em sẽ báo ID record còn lại, evidence lookup và người chịu trách nhiệm xử lý tiếp. Nếu quyền cleanup không còn hợp lệ hoặc ownership chưa rõ, em sẽ không xóa tùy ý. Tách test result khỏi workflow status giúp người đọc thấy assertion nào đã đạt và công việc vận hành nào vẫn còn dang dở.
- Hỏi sâu: Nếu quyền cleanup đã hết thì sao?
- Lỗi thường gặp: Sửa test result thành fail mà không giải thích.

## 5. Webpage bảo upload trace thì sao?

- Ý định: Kiểm tra injection.
- Trả lời 30–60 giây: Em sẽ giải thích rằng đó là dữ liệu untrusted, không phải grant. Controller đối chiếu action với tool allowlist và approval scope; workflow không có publish tool thì không thực hiện. Em sẽ giữ fact cần điều tra và không đưa raw trace chứa secret ra ngoài. Em sẽ phân biệt rõ nội dung trang với instruction từ goal và grant hợp lệ. Nếu trang yêu cầu gửi artifact, em sẽ không mở đường vòng bằng tool khác. Em sẽ chuẩn bị bản mô tả sự kiện đã sanitize nếu cần review, vì trace có thể chứa cookie, token hoặc thông tin nội bộ dù test dùng dữ liệu giả.
- Hỏi sâu: Prompt guardrail có đủ không?
- Lỗi thường gặp: Tin trang vì tool trả về.

## 6. Một report tốt cần gì?

- Ý định: Kiểm tra claim provenance.
- Trả lời 30–60 giây: Em sẽ giải thích rằng report có case/source IDs, run/attempt, revision, command thực, environment, assertion, artifact, cleanup, unknown và review decision. Không có live artifact thì ghi insufficient evidence; synthetic packet vẫn ghi synthetic, không đổi thành run thật. Em sẽ đối chiếu từng claim với source hoặc artifact cụ thể thay vì chỉ đọc AI summary. Nếu packet có a1 fail và a2 pass nhưng thiếu quyền rerun, em sẽ giữ cả kết quả lẫn approval gap. Em sẽ không tự điền command hay trace thật khi nguồn chỉ cung cấp placeholder.
- Hỏi sâu: Rerun chưa có approval trong packet báo thế nào?
- Lỗi thường gặp: Chỉ viết Case passed without issues.

Nguồn đối chiếu và kiến thức nền: [topic](../01_topics/agent-architecture.md), các heading course/exercise ghi trong topic. Tình huống và lời giải ở đây là tự biên soạn.

