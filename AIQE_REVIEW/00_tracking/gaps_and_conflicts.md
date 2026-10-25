# Khoảng trống, mâu thuẫn và phần chưa xác minh

Ngày đối chiếu: 25/10/2026. Không sửa nguồn gốc. Đây là sổ vấn đề để người học tránh học thuộc nhầm hoặc kết luận quá bằng chứng.

## Thiếu nguồn và giới hạn công cụ

| Vấn đề | Vị trí nguồn | Cách xử lý trong bộ ôn / việc còn lại |
|---|---|---|
| Thiếu giáo trình FPR, MTPTD, FPE, PSFR | TrainingCalendar, sheet Training Calendar, hàng 6–62 và 195–213 | Đã có cầu nối QA/prompt/readiness; chưa tuyên bố khôi phục toàn bộ module. Cần tài liệu chính thức để bổ sung nguyên tắc/lifecycle/ML/copilot và rubric. |
| Header End Date 27-11-2026 nhưng closing 05-11-2026 | TrainingCalendar C4 và hàng 214–215 | Giữ cả hai, hỏi owner khi cần lịch thực tế; không dùng ngày cuối header để suy còn module. |
| PPTX không render được | Hai deck ARTD: slide 1–24 và notes cùng số | Đọc text/notes, xem 7 PNG unique. PowerPoint COM lỗi 80070520; native chart/shape/layout chưa kiểm tra trực quan. [Chi tiết](visual-inspection.md). |
| DOCX không có số trang render | ARTD exercises, word/document.xml, paragraphs/tables | Đọc text theo heading, không gán số trang; phân trang/bố cục chưa xác minh. |
| Không có live PortalLite/agent provider baseline | PMLM/AAALE/AOCE/PBAAD readiness và exercise packets | Lab/contract có thể phân tích; thiếu runtime/grant/DOM hiện tại để kết luận E2E pass. |
| Nội dung mở rộng mới ở mức giới thiệu | ARTD metamorphic/pairwise; PMLM custom/virtualized/shadow widgets | Ghi bao phủ một phần; chưa có hướng dẫn thuật toán hoặc case runtime sâu. |
| Không có đề thi chính thức | Calendar chỉ liệt kê Quiz/Exam; course có rubric đề xuất | Bộ quiz/phỏng vấn tự biên; không dự báo đáp án hay tỷ lệ câu thi. |

## Mâu thuẫn trong nguồn học và các baseline

| Vấn đề | Vị trí thật | Diễn giải giữ lại và cách xử lý |
|---|---|---|
| Order tạo trước hay sau payment | ARTD course/DOCX, Interface and data constraints + process note | 201 CREATED/PENDING_PAYMENT đối lập note chỉ tạo sau paid là gap có chủ đích. Ghi clarification; không tự chọn expected. |
| 201/202 không đồng nghĩa giữa module | DALA §5.3 so ARTD source pack | DALA 201/PAID và 202/PAYMENT_PENDING thuộc baseline khác. Không dùng DALA sửa ARTD. |
| Constraint UUID nhưng fixture dùng ID rút gọn | DALA §§5.3–5.4 | Giữ ID nguyên bản để correlate log; test request mới theo contract cần UUID đúng. Không coi fixture hoàn toàn schema-valid. |
| Bản dịch 400 dễ nhầm authentication | DALA VI §5.3, đối chiếu EN Request validation failed | 400 trong contract này là request validation. Không học thuộc chữ “xác thực” rồi nhầm 401/403. |
| Công thức risk score khác mức giản lược | ARTD slide16/notes16 so EX-U3-SCENARIO instruction 5 | Slide dùng L×I; exercise dùng L×I×E. Dùng công thức theo bài, không trộn điểm hai thang. |
| Slide không liệt kê hết coverage state | ARTD slide13 so course Session2.1 | Course còn Blocked/Not testable; bộ ôn giữ trạng thái thiếu quyết định/môi trường. |
| Same-key/different-payload hoặc cross-customer GET chưa chốt | ARTD Unit6; DALA §5.3 | Ghi Not specified; không tự ép 409/403/404 khi contract chưa nói. |
| Partial-refund còn quyết định chưa rõ | ARTD CR-01 | Approval cộng dồn, allocation, rounding, concurrency cần clarification, chưa thành approved rule. |
| Cutoff ngày và đơn vị ký tự chưa đủ | ARTD BR-REF-01 và refundReason constraint | Không tự suy timezone, inclusive cutoff hoặc codepoint/grapheme; nêu câu hỏi trước khi chọn oracle sát biên. |
| F02 khác ý nghĩa giữa module | AOCE multi-flow so PBAAD BRIEF/FLOW-PBAAD-v1 | AOCE F02 change-department; PBAAD F02 duplicate-ID. Dẫn cả module và flow ID khi báo cáo. |
| Candidate selector chưa xác nhận | PMLM EX-U7-INCIDENT | Confirm archive là candidate, phải có DOM/snapshot hiện tại trước khi dùng. |
| Layering và approval là convention của lab | PMLM §5.4; AAALE gates | Không suy Playwright/MCP bắt buộc bốn layer hoặc tự enforce gate. Preauthorization hợp lệ có thể bao phủ nhiều bước theo policy. |

## Sai lệch số liệu trong bài nộp mẫu

Các số dưới được đối chiếu bằng packet và phép tính, không phải số đo live. Không sửa original submissions.

| Vấn đề | Nguồn | Cách hiểu đúng trong bài ôn |
|---|---|---|
| 7/9 accepted không khớp bảng | NhiTY14/submissions/U1/U1_benchmark.md, Chấm output cards | A1–A3 và C1–C2 qua gate là 5/9; C3 stale evidence, B bị loại. |
| Cached rate và đơn vị không khớp handout | U1 benchmark/CSV so AOCE RATE-SYN-01 | Handout dùng đơn vị giả lập/triệu tokens, cached=0,25; không coi bảng USD/cached=0 là kết quả cùng rate. |
| Full evidence ghi 6/8 nhưng bảng có 7 | U7_metrics-and-claims.md §1.4; METRIC-PACKET-07 | Evidence completeness là 7/8=87,5%; khác 5 evidence-complete passes. |
| Cost numerator chỉ lấy pass | U7_metrics-and-claims.md Evidence-complete-pass cost; course U7.2 | Theo cohort packet, measured subtotal 0,89/5=0,178 lower bound; không lấy 0,47/5 để đại diện chi phí cả cohort. |
| Budget remaining bị đảo cận | U7_metrics-and-claims.md và sprint review | Khi cost còn thiếu không âm, measured 0,89 và budget 1,20 cho remaining ≤0,31; không phải ≥0,31 hay bảo đảm đủ budget. |

## Runtime và version

Hai `.agents/mcp_config.json` dùng `@playwright/mcp@latest`; đó là cấu hình chưa pin, không xác định version đã cài hay đã dùng. Không chạy npx/cài dependencies trong công việc biên soạn. Package-lock được dùng để phân biệt version của starter và snippet; tài liệu web hiện hành không thay thế lockfile.

finalProject có scripted planner, simulated adapter và artifact gắn nhãn SIMULATED. Unit test local chỉ kiểm chứng logic mô phỏng trong phạm vi test; không chứng minh DOM, LLM planner, live CI hay deployment. Release gate mẫu còn HOLD theo bằng chứng được nộp. Chi tiết: [ledger AOCE/PBAAD](optimization-project-notes.md).

Đã thử một URL Anthropic về long-context nhưng công cụ không mở được; không dùng nội dung URL đó để giảng. Không có thông tin giá model/API hiện hành hoặc hướng dẫn pháp lý được thêm từ trí nhớ. Các nguồn web thực sự dùng nằm tại [web_sources](../06_sources/web_sources.md).

## Thứ tự xử lý tiếp

1. Bổ sung giáo trình FPR/MTPTD/FPE/PSFR và đối chiếu từng mục tiêu đang partial.
2. Render hai deck khi có PowerPoint/LibreOffice chạy được, kiểm tra chart/shape, cập nhật ledger theo slide thật.
3. Có approved lab thì thực hiện một vertical slice với data/cleanup/evidence; không suy pass từ sample.
4. Mở rộng pairwise/metamorphic và UI phức tạp theo nhu cầu thực, giữ nguồn và test oracle rõ.
