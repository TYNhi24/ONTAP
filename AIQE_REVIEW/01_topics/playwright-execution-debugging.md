# Playwright execution, waits, MCP và điều tra failure

> Bản ôn tập tự biên soạn cho fresher. Nội dung khóa học là nguồn chính; đoạn web được gắn nhãn riêng. Không phải đáp án chính thức.

## Mục tiêu và kiến thức cần có
Vẽ lifecycle runner, chọn signal chờ đúng oracle, phân loại failure và lập evidence package tái lập được.

Biết TypeScript async/await, HTTP, terminal và Git. Đọc [Locator](playwright-locators.md) trước phần synchronization; đọc [Agent](agent-architecture.md) sau khi hiểu evidence.

## Mức ưu tiên
Bắt buộc: lifecycle, isolation, config inventory, state assertion, waiter-before-action, artifact-first triage, AI review và secret handling. Nên biết: popup/download/dialog, timeout riêng, expect.poll/toPass có side effect review. Mở rộng: shard, worker tuning và run distribution để nghiên cứu flake.

## Từ khóa bằng câu đầy đủ
Browser context cô lập cookie/storage giữa test. Fixture quản lý setup và teardown theo lifecycle. Actionability kiểm tra điều kiện thao tác của element. Oracle là căn cứ xác định expected behavior. Web-first assertion retry việc kiểm tra UI state trong timeout. MCP là cầu nối tool, không phải chứng nhận test pass. Trace ghi diễn biến của attempt đã được thu thập.

## Học từ đầu: cái gì, vì sao và khi nào
Một command chạy test đi qua discovery, worker, fixture, browser/context/page, actions, assertions, teardown và reporter. Discovery thấy test không có nghĩa test đã chạy. Worker có thể chạy song song; context riêng không cô lập employee trong backend. Mỗi run vẫn cần data unique và cleanup cả khi assertion fail. Browser process chứa context; page là tab trong context. Mở tab mới trong cùng context không tạo isolation auth tương đương context riêng.

Trước khi viết test, đọc package.json, config, lockfile, script, environment mechanism và CI convention. Node package và browser runtime là dependency khác nhau. Validate tên biến bắt buộc nhưng không in giá trị secret. Dùng script của repo; command minh họa trên mạng không chứng minh command dự án tồn tại.

Click hoàn thành chưa chứng minh employee được index vào search. Auto-wait đợi điều kiện element đủ để action, còn assertion phải kiểm tra state gắn AC: đúng ID, đúng department, đúng một row. Chọn signal gần oracle: UI assertion, response/event đã có contract hoặc read helper được duyệt. Waiter phải được tạo trước action để tránh lỡ event nhanh. Không dùng sleep cố định để đoán backend đã xong.

MCP giúp inspect, snapshot, điều hướng và exploratory interaction tùy server/runtime. Snapshot là state thời điểm gọi tool. Test result cần source-controlled test và reporter của attempt phù hợp. AI draft cần bounded facts, source IDs, convention, forbidden data và human review; kiểm tra locator, oracle, synchronization, isolation, cleanup, security và provenance.

Khi fail, giữ original artifacts trước rerun. Đọc call log: zero match, many match, hidden/detached, sai frame hay overlay? Đọc trace timeline với console/network đã redact để chọn kiểm tra phân biệt. Phân loại sơ bộ product, locator, synchronization, data/environment hay implementation; root cause chỉ được kết luận sau evidence. Snapshot rerun không thay DOM trong original trace. Browser launch bị chặn là infrastructure blocker, chưa có product assertion failure.

## Input → xử lý → output
AC + config + synthetic credentials + observed DOM → setup, action, assertion, cleanup, reporter rồi triage → run record chứa command/revision/project/attempt/data/artifact/unknowns.

## Ví dụ fresher
```ts
const responsePromise = page.waitForResponse(r =>
  r.url().includes('/api/employees') && r.request().method() === 'POST');
await page.getByRole('button', { name: 'Save employee', exact: true }).click();
await expect((await responsePromise).status()).toBe(201);
// Tiếp tục assert row ID và department theo AC-EMP-02.
```

Đây là ví dụ integration chỉ hợp lệ nếu endpoint/status đã được duyệt; 201 chưa tự chứng minh search state. Không tự tạo endpoint cho app thật.

## So sánh dễ nhầm
| Khái niệm | Trả lời câu hỏi | Không bảo đảm |
|---|---|---|
| Auto-wait | Element đã thao tác được? | Business hoàn thành |
| Web-first assertion | UI đạt expected state trong hạn? | Backend khác UI |
| Polling read-only | Read model đã đổi? | Create được phép retry |
| Test retry | Attempt mới có pass? | First failure biến mất |
| Screenshot | Visual state ra sao? | DOM/backend commit |
| Trace | Recorded attempt diễn ra thế nào? | Attempt không được thu |
| MCP snapshot | Tool thấy gì lúc inspect? | Suite pass |

## Bẫy quiz và phỏng vấn
Không suy “thao tác được” thành “đúng nghiệp vụ”; không lấy một output từ tool làm nguồn cho mọi claim. Khi trả lời phỏng vấn, nêu intent, cơ chế, ví dụ cụ thể và giới hạn evidence. Xem [bộ phỏng vấn](../03_interview/playwright-execution-debugging.md) và [quiz tự luyện](../04_quiz/playwright-execution-debugging-questions.md), làm trước khi mở đáp án.

## Tự kiểm tra
- [ ] Vẽ command → reporter
- [ ] Giải thích toast false positive
- [ ] Phân loại duplicate Confirm và expired auth
- [ ] Tạo manifest giữ hai attempt
- [ ] Chứng minh cleanup failure được báo riêng.

## Nguồn và phần bổ sung
Nguồn khóa học: [course](../../document/AIQE%20Playwright%20MCP%20%26%20Locator%20Mastery/L3_AIQE_PMLM_course_content_vi.md), [bài tập](../../document/AIQE%20Playwright%20MCP%20%26%20Locator%20Mastery/L3_AIQE_PMLM_exercises_vi.md). Heading đối chiếu chính xác: PMLM Unit 1 — Playwright concepts, execution model and MCP overview; Unit 2 — Environment setup, browser interaction and first live test; Unit 5 — Assertions, waits and synchronization for stable execution; Unit 6 — AI-assisted script generation and mandatory code review; Unit 7 — Debugging locator failures and collecting evidence. Exercises EX-U1-EXEC-MCP, EX-U2-FIRST-LIVE, EX-U5-SYNC, EX-U6-AI-REVIEW, EX-U7-INCIDENT và Capstone.

Bổ sung từ nguồn web: click kiểm tra unique, visible, stable, receives events và enabled; fill có tập checks khác. [Auto-waiting](https://playwright.dev/docs/actionability). Retry pass sau fail được phân loại flaky; worker lỗi được thay. [Retries](https://playwright.dev/docs/test-retries). Trace on-first-retry thu retry đầu, không thu original failure; phải đọc config thật. [Trace viewer](https://playwright.dev/docs/trace-viewer-intro).

