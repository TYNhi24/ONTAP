# Phỏng vấn: playwright-execution-debugging

Tự biên soạn, không phải câu hỏi/đáp án chính thức. Mẫu trả lời hướng đến 30–60 giây; hãy diễn đạt lại và thêm ví dụ của mình.

## 1. Context khác page thế nào?

- Ý định: Kiểm tra isolation.
- Trả lời 30–60 giây: Em sẽ giải thích rằng browser chứa context; context giữ session/storage cô lập; page là tab trong context. Hai tab cùng context có thể dùng cùng auth. Test context riêng vẫn dùng chung backend nên em sẽ tạo ID riêng và cleanup owned data. Trong bài lab chạy song song, em sẽ cấp ID theo run hoặc attempt và chỉ cleanup record có ownership rõ. Nếu hai test sửa cùng một employee trên backend, context riêng vẫn không ngăn chúng ghi đè nhau. Em sẽ kiểm tra cả fixture scope và data lifecycle để biết isolation đang nằm ở browser hay ở hệ thống dữ liệu.
- Hỏi sâu: Worker parallel ảnh hưởng fixture dùng chung thế nào?
- Lỗi thường gặp: Nói tab mới cô lập mọi dữ liệu.

## 2. Click pass đã đủ kết luận create pass?

- Ý định: Kiểm tra oracle.
- Trả lời 30–60 giây: Em sẽ giải thích rằng chưa đủ. Click chỉ hoàn tất action; AC yêu cầu employee searchable với department đúng. Em sẽ assert đúng một row theo ID và department. Toast chỉ là feedback, không chứng minh read model đã cập nhật. Em sẽ viết expected state trước rồi mới chọn cách chờ. Nếu search cập nhật chậm, em sẽ dùng web-first assertion hoặc read helper được phép với timeout có căn cứ. Nếu chưa có SLA, em sẽ ghi timeout là chính sách lab, tránh biến một con số tùy chọn thành yêu cầu sản phẩm.
- Hỏi sâu: Chọn signal nào nếu eventual consistency?
- Lỗi thường gặp: Assert Success rồi kết luận toàn flow pass.

## 3. Vì sao waiter đặt trước action?

- Ý định: Kiểm tra race.
- Trả lời 30–60 giây: Em sẽ giải thích rằng response hoặc download có thể xuất hiện ngay khi click. Đăng ký waiter sau action có thể lỡ event. Em sẽ tạo promise chờ signal đúng contract, trigger action rồi await promise và assertion business state. Em sẽ chọn predicate theo request liên quan, chẳng hạn method và endpoint đã được xác nhận, đồng thời tránh bắt nhầm request nền. Response thành công vẫn chỉ chứng minh lớp integration tương ứng. Em sẽ tiếp tục kiểm tra UI state theo acceptance criteria để không bỏ sót trường hợp backend nhận request nhưng màn hình hiển thị sai.
- Hỏi sâu: Predicate response phải chặt đến đâu?
- Lỗi thường gặp: Chờ endpoint bất kỳ có chữ employee.

## 4. MCP snapshot chứng minh gì?

- Ý định: Kiểm tra evidence boundary.
- Trả lời 30–60 giây: Em sẽ giải thích rằng nó chứng minh tool quan sát state tại thời điểm và scope đã ghi. Nó hỗ trợ đề xuất locator, chưa chứng minh source test chạy hoặc pass. Em sẽ cần command, revision, reporter và assertion của đúng attempt. Em sẽ lưu environment, URL hoặc alias, thời điểm quan sát và scope của tool để người khác hiểu giới hạn snapshot. Nếu đang điều tra failure cũ, em sẽ giữ snapshot mới trong investigation run riêng. Em sẽ không dùng nó để khẳng định DOM trong attempt cũ giống hệt hiện tại.
- Hỏi sâu: Snapshot rerun dùng được cho original failure không?
- Lỗi thường gặp: Dùng current DOM thay lịch sử failure.

## 5. Test fail chỉ trên CI làm gì?

- Ý định: Kiểm tra debugging.
- Trả lời 30–60 giây: Em sẽ giữ artifact và so command, revision, project, auth, data và concurrency. Đọc call log/trace rồi chọn kiểm tra phân biệt overlay, data collision hay backend delay. Timeout chỉ đổi khi có căn cứ contract hoặc policy, không sửa mù. Em sẽ nêu một giả thuyết có thể kiểm chứng và bước kiểm tra tiếp theo, ví dụ so trace để biết overlay có chặn click hay không. Nếu browser chưa launch được, em sẽ báo infrastructure blocker thay vì lỗi login. Kết luận cần khớp phạm vi evidence, không chỉ dựa việc local chạy được.
- Hỏi sâu: Browser launch error có là product defect?
- Lỗi thường gặp: Thêm retry ngay.

## 6. Retry pass báo thế nào?

- Ý định: Kiểm tra honesty.
- Trả lời 30–60 giây: Em sẽ giữ first failed attempt và passed retry, báo flaky theo runner. Retry không chứng minh root cause biến mất. Data và cleanup cần độc lập giữa attempt; manifest gắn đúng trace với từng attempt. Em sẽ ghi attempt ID, data ID, command và cleanup outcome cho từng lần chạy để người review tái dựng được timeline. Nếu trace chỉ bật on-first-retry, em sẽ nói rõ có thể thiếu trace của failure đầu. Em sẽ không gọi suite ổn định chỉ vì một lần retry thành công.
- Hỏi sâu: Trace on-first-retry có lưu first failure không?
- Lỗi thường gặp: Xóa failed artifact.

Nguồn đối chiếu và kiến thức nền: [topic](../01_topics/playwright-execution-debugging.md), các heading course/exercise ghi trong topic. Tình huống và lời giải ở đây là tự biên soạn.

