# Tiến độ và bàn giao

Theo yêu cầu sắp xếp lại của người dùng, 6 thư mục nguồn và TrainingCalendar đã chuyển vào `document/`. Đã cập nhật liên kết, đường dẫn manifest và script; hash của 88 file nguồn giữ nguyên. `.gitignore` bỏ qua `document/`, bản text trích xuất và thư mục ảnh cache nguồn để tránh đưa nội dung tài liệu lên GitHub. Các liên kết nguồn vẫn hoạt động khi có tài liệu local; trên GitHub chúng không mở được vì nguồn được bỏ qua có chủ đích.

Cập nhật **25/10/2026, Asia/Saigon**. Đã biên soạn bộ ôn cho các nguồn hiện có; **chưa hoàn tất toàn bộ mục tiêu khóa học** vì thiếu giáo trình bốn module, chưa render slide và chưa có live evidence.

## Đã thực hiện

- A — Kiểm kê 88 file, 67 hash nội dung khác nhau, 15 nhóm trùng byte. Đã đọc phần text liên quan theo ledger; hai deck đọc slide/notes 1–24, DOCX đọc paragraph/table, Excel đọc sheet Training Calendar hàng 1–215. Đã xem ảnh login đại diện và 7 PNG nhúng unique. Không có PDF trong đầu vào.
- B — Đối chiếu 10 module calendar với 6 module có giáo trình; lập mapping mục tiêu/lab, 36 unit, keyword, prerequisite và những chỗ giao nhau. DALA/ADALA và AAALE/AALE là khác mã giữa folder/calendar, không suy thành module mới.
- C — 11 bài kiến thức; 61 câu phỏng vấn; 100 MCQ với đáp án riêng giải thích mọi lựa chọn; glossary Anh–Việt, bảng dễ nhầm và 4 lab. Các ví dụ tự biên, web additions và simulated/live được phân biệt.
- D — Kiểm tra encoding, đường dẫn local, số câu/lựa chọn, source hashes, review các conflict và số liệu packet. Kết quả máy đọc lưu tại [validation-results.json](validation-results.json). Các giới hạn không được xóa khỏi trạng thái coverage.

Lần kiểm tra cuối: **60 file Markdown, 905 liên kết local hợp lệ, 100 câu quiz/400 lựa chọn, 61 câu phỏng vấn; không phát hiện lỗi bởi checker**. SHA-256 của cả 88 file nguồn không đổi; 7 hash references ARTD/DALA và 76 references AOCE/PBAAD trong ledger khớp snapshot. Đây là kiểm tra cấu trúc và tính nguyên vẹn, không tự chứng minh mọi diễn giải đúng hoặc mọi mục tiêu đã đủ sâu.

Đã mở nguồn chính thức ISTQB, Anthropic prompt docs, Playwright, MCP và GitHub để thêm kiến thức có nhãn. ARTD/DALA vẫn chủ yếu diễn giải course, không thêm luật HTTP/privacy hiện hành từ trí nhớ. [Nguồn web](../06_sources/web_sources.md).

## Kiểm chứng runtime đã làm

Root chạy lại ngày 25/10/2026:

```powershell
node --test 'document/AIQE Project-Based AI Agent Development/finalProject/test/assistant.test.js'
```

Kết quả 8 tests pass, 0 fail, 0 skipped, exit 0. Chỉ là local synthetic unit tests, không cài dependencies, không gọi model/browser/CI. Không sửa source code. Không có dữ liệu PortalLite mới để cleanup.

## Việc còn thiếu và điều kiện để tiếp tục

| Việc | Trạng thái / điều kiện |
|---|---|
| Bổ sung FPR/MTPTD/FPE/PSFR | Chờ giáo trình tương ứng; bài cầu nối đã có nhưng chưa thay thế khóa. |
| Kiểm tra slide native chart/shape/layout | PowerPoint COM lỗi 80070520, không có soffice; cần runtime render hoạt động. |
| DOCX phân trang và workbook bố cục | Chưa kiểm tra bản render; nội dung được dẫn bằng heading/sheet/row thực. |
| Pairwise/metamorphic và widget phức tạp sâu | Đang partial, mở rộng khi cần; không giả nội dung đã dạy đầy đủ. |
| Live Playwright/agent/CI và model eval | Cần approved environment, account/grant, DOM/tool contracts và helper seed/lookup/cleanup. |
| Các thiếu sót code project mẫu | Không nằm trong yêu cầu sửa code. Bộ ôn giải thích gaps local và HOLD, chưa implement thêm verifier/ledger/deadline. |

Chi tiết và độ ưu tiên: [gaps_and_conflicts](gaps_and_conflicts.md). Các phần thiếu không chặn việc sử dụng bộ ôn đã viết; chúng chặn claim “đã bao phủ toàn khóa” hoặc “project đã chạy live”.

## Tiếp tục ở phiên khác

Dùng yêu cầu:

> Tiếp tục AIQE_REVIEW từ 00_tracking/progress.md và source_inventory.md. So hash input hiện tại với extracted-sources.json trước khi tái trích xuất. Chỉ cập nhật những chủ đề chịu ảnh hưởng, giữ ghi chú cá nhân; ưu tiên bốn module thiếu và những hàng partial trong coverage_matrix.md.

Trình tự: đọc progress/inventory/gaps → liệt kê input mới/đổi hash → đọc thêm theo từng module → cập nhật bài và question bank liên quan → cập nhật mapping/ledger → chạy kiểm tra. **Không chạy extractor để ghi đè snapshot trước khi so sánh**, vì sẽ mất baseline phát hiện thay đổi.

Các script chỉ viết đầu ra trong AIQE_REVIEW và không sửa source:

```powershell
python AIQE_REVIEW/00_tracking/check-review.py
```

`extract-sources.py` là công cụ tạo snapshot mới; `build-tracking.py` tái sinh inventory/mapping từ snapshot. Hai script này có thể ghi đè file tracking đã sinh; chỉ dùng sau khi lưu/so thay đổi và kiểm tra không có ghi chú cá nhân. Hiện chưa có ghi chú cá nhân trong output do người biên soạn tạo.
