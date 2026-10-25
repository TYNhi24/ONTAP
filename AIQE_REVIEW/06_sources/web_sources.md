# Nguồn web đã dùng

Ngày mở đọc: **25/10/2026**, theo Asia/Saigon. Chỉ tra khái niệm chung; không upload tài liệu nội bộ. Bảng ghi nguồn thực sự đã mở; không coi snippet tìm kiếm là bằng chứng. Version “hiện hành” không có nghĩa đã chạy trên project trong workspace.

| Nguồn và URL | Version/phạm vi đã đọc | Nội dung bổ sung và nơi dùng |
|---|---|---|
| [ISTQB CTFL overview](https://istqb.org/certifications/certified-tester-foundation-level-ctfl-v4-0/) | Overview CTFL 4.0; trang dẫn syllabus 4.0.1 | Xác định tài liệu nền chính thức để đọc tiếp; không dùng cấu trúc thi CTFL làm cấu trúc thi AIQE. |
| [ISTQB CTFL Syllabus](https://istqb.org/?download_id=3345&sdm_process_download=1) | PDF v4.0.1, 2024-09-15; §§1–3 được tham chiếu cho phân biệt nền tảng | Đoạn ngắn “Bổ sung từ nguồn web” trong [qa-foundations](../01_topics/qa-foundations.md): QA/testing, static/dynamic, level/type, confirmation/regression. Phần lớn ví dụ kỹ thuật dựa local ARTD và tự biên. |
| [Anthropic Prompt engineering overview](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview) | Trang docs sống, không pin model; Before prompt engineering/When to prompt engineer | [prompt-engineering](../01_topics/prompt-engineering.md): xác lập success criteria và empirical check trước tối ưu. Không suy model cụ thể hoặc API đã được kiểm chứng. |
| [Playwright Locators](https://playwright.dev/docs/locators) | Docs hiện hành, không pin version | [playwright-locators](../01_topics/playwright-locators.md): locator resolve lại và ưu tiên user-facing attributes/explicit contracts. |
| [Playwright Auto-waiting](https://playwright.dev/docs/actionability) | Docs hiện hành, action-specific checks | [execution-debugging](../01_topics/playwright-execution-debugging.md): click checks khác fill; actionability không thay oracle. |
| [Playwright Retries](https://playwright.dev/docs/test-retries) | Docs hiện hành, worker/retry classification | [execution-debugging](../01_topics/playwright-execution-debugging.md): flaky classification và worker replacement, không suy retry đã sửa root cause. |
| [Playwright Trace viewer](https://playwright.dev/docs/trace-viewer-intro) | Docs hiện hành; ví dụ on-first-retry | [execution-debugging](../01_topics/playwright-execution-debugging.md): mode thu trace retry đầu không chứng minh original failure đã có trace. |
| [MCP Tools](https://modelcontextprotocol.io/specification/2025-06-18/server/tools) | Revision 2025-06-18; không khẳng định là revision mới nhất | [agent-architecture](../01_topics/agent-architecture.md): tool schema/discovery/call và giới hạn protocol, không tự cấp business approval. |
| [GitHub Events — schedule](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#schedule) | Docs hiện hành; agent đã mở đọc 2026-10-25, không pin GitHub platform version | [ci-recovery](../01_topics/ci-recovery.md): UTC mặc định, tùy chọn timezone, default branch và khả năng delay/drop; lịch mong đợi khác dispatch thực. |

ARTD/DALA được biên soạn từ nguồn khóa học và ví dụ tự tạo, không thêm chuẩn HTTP/privacy hiện hành chưa được xác minh. Các chi tiết contract 201/202/400 trong những bài đó thuộc source pack cụ thể, không phải luật áp cho mọi API.

## Nguồn đã xem nhưng không dùng để thêm kiến thức

- [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework): đã mở overview; không đưa thêm mục tiêu/rubric AIQE từ framework.
- [Anthropic Building effective agents](https://www.anthropic.com/research/building-effective-agents): đã mở bài, ghi nhận có cảnh báo tooling landscape đã đổi; không dùng danh sách công cụ hoặc model làm khuyến nghị trong bộ ôn.
- URL `https://www.anthropic.com/engineering/prompting-for-long-context`: mở lỗi công cụ; **chưa xác minh**, không sử dụng nội dung.

Ledger truy cập cho phần Playwright/MCP: [browser-agents-notes](../00_tracking/browser-agents-notes.md). Nếu có thêm nguồn cho AOCE/PBAAD, phải đồng bộ bảng này và nhãn tại đoạn bài tương ứng trước khi phát hành cập nhật.
