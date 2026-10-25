# Phỏng vấn — ci-recovery

Câu hỏi tự biên soạn, không phải đề chính thức. Dùng [bài học](../01_topics/ci-recovery.md) làm nguồn; luyện trả lời mỗi câu 30–60 giây bằng lời của mình.

## Câu 1. Tách PR/manual/scheduled lanes để làm gì?

**Ý đồ:** Kiểm tra trigger và quyền execution.

**Gợi ý trả lời 30–60 giây:** PR lane kiểm tra diff/static fixtures/discovery không cần live secrets. Manual lane chạy trusted revision trong lab sau preflight và lưu assertions/cleanup/artifacts. Scheduled lane dùng cùng controls nhưng phải quan sát trigger schedule thật. Starter login test chưa có flow lab hay helper nên draft YAML chưa thể deploy ngay. Tôi không gọi discovery hay manual run là bằng chứng scheduled execution.

**Hỏi tiếp:** Fork PR thiếu secret có phải lỗi app? **Điểm cần trả lời:** Không; PR lane nên không phụ thuộc live secret.

**Lỗi thường gặp:** Bật tất cả live tests trên mọi PR hoặc gọi discovery là live pass.

## Câu 2. CI xanh nhưng selected=0 thì kết luận gì?

**Ý đồ:** Kiểm tra false green và evidence.

**Gợi ý trả lời 30–60 giây:** Tôi ghi no execution và không có assertion evidence. Exit 0 của wrapper không chứng minh test đã chạy. Kiểm tra selector/tag/config/revision, bỏ cơ chế pass-with-no-tests cho required suite, xác nhận selected và executed counts rồi chạy lại đúng revision. Install log không thay reporter. Nếu thiếu credential làm test skip, cũng phải giữ skipped/pending thay vì live pass.

**Hỏi tiếp:** Có thể kết luận nguyên nhân chắc là grep không? **Điểm cần trả lời:** Không; đó là hypothesis cần kiểm tra từ command/config/reporter.

**Lỗi thường gặp:** Tính empty array thành 100% pass.

## Câu 3. Save timeout thì có retry không?

**Ý đồ:** Kiểm tra an toàn write và state.

**Gợi ý trả lời 30–60 giây:** Timeout client không chứng minh write chưa xảy ra. Tôi chặn mutating calls rồi reconcile exact owned ID bằng helper được phép. Nếu found thì không create lại, tiếp tục read-only oracle/cleanup trong policy; nếu inconclusive thì safe stop với pending record, owner và next action. Chỉ cân nhắc retry khi contract chứng minh an toàn. INC-62 lookup found vẫn chưa có search assertion, nên không được report F01 pass.

**Hỏi tiếp:** Search UI chưa thấy row có nghĩa record vắng? **Điểm cần trả lời:** Không nếu consistency/index SLA chưa xác định.

**Lỗi thường gặp:** Click Save lại vì lần trước có exception.

## Câu 4. Hai Save buttons gây strict violation: sửa sao?

**Ý đồ:** Kiểm tra scope locator và oracle.

**Gợi ý trả lời 30–60 giây:** Tôi đọc DOM/timeline xem action đã xảy ra chưa. INC-61 chưa click; dialog Create employee có một Save nên scope dialog rồi button, xác nhận unique target. Nếu overlay chặn, chờ condition đã quan sát trong timeout budget. Không dùng first hoặc force để bỏ ambiguity. Sau action vẫn search exact ID và department; một click thành công chưa đủ business pass. Tôi giữ before/after revisions và negative controls.

**Hỏi tiếp:** Force có bỏ mọi kiểm tra không? **Điểm cần trả lời:** Không; official docs nói bỏ một số non-essential checks như receives-events.

**Lỗi thường gặp:** Thêm first, force và sleep 5s rồi coi đã sửa root cause.

## Câu 5. Fail rồi pass retry có phải flaky đã được sửa?

**Ý đồ:** Kiểm tra runner semantics so với diagnosis.

**Gợi ý trả lời 30–60 giây:** Runner phân loại flaky khi fail lần đầu rồi pass retry; chưa xác nhận nguyên nhân. Tôi giữ attempt history, revision/config/data namespace, trace/network/DOM để tạo hypothesis và kiểm tra phân biệt. Fix cần unchanged oracle, baseline/fixed evidence và negative controls. Browser startup exception trước body là env blocked, không tự gọi app flaky. Retry nhiều lớp còn nhân attempts và cost nên phải có tổng budget.

**Hỏi tiếp:** Quarantine có xóa khỏi report không? **Điểm cần trả lời:** Không; cần owner, expiry, residual risk và coverage thay thế.

**Lỗi thường gặp:** Kết luận resolved từ một lần rerun xanh.

## Câu 6. always() có bảo đảm cleanup sau cancel không?

**Ý đồ:** Kiểm tra lifecycle và recovery ngoài job.

**Gợi ý trả lời 30–60 giây:** Không bảo đảm khi force cancel, runner mất hoặc hard timeout. Tôi dùng capture/upload-on-failure cho lỗi thường, nhưng durable ownership ledger/helper và recovery owner mới giúp xử lý write chưa rõ sau mất process. Preflight run sau phải kiểm tra unresolved state; không tin file local đã biến mất. Cleanup failure giữ outcome riêng và release HOLD, không suppress bằng || true. Concurrency phải theo shared environment, namespace vẫn độc lập.

**Hỏi tiếp:** Rollback code có xóa data đã tạo không? **Điểm cần trả lời:** Không; side effects cần reconcile/cleanup theo ownership.

**Lỗi thường gặp:** Hứa always() chạy xong trong mọi trường hợp.

Tự chấm: nêu đúng nguồn/mode, dùng một ví dụ, giữ unknown, chỉ rõ bằng chứng và next action. Không học thuộc câu trả lời thành lời xác nhận mình đã thực hiện.
