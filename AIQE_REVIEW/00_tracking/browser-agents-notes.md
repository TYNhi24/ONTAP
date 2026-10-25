# Ghi chú nguồn — browser/agents

## Phạm vi và trạng thái đọc
Ngày truy cập web: 2026-10-25. Bốn file dưới được đọc **toàn văn**, bao gồm preamble, unit/session, exercises, rubric, capstone, trainer notes và provenance; chia chunk hữu hạn để không cắt output. Không thay đổi nguồn gốc.
- document/AIQE Playwright MCP & Locator Mastery/L3_AIQE_PMLM_course_content_vi.md — toàn văn đã đọc (35934 ký tự theo extracted-sources).
- document/AIQE Playwright MCP & Locator Mastery/L3_AIQE_PMLM_exercises_vi.md — toàn văn đã đọc (20583 ký tự).
- document/AIQE AI Agent Architecture & Live Execution/L3_AIQE_AAALE_course_content_vi.md — toàn văn đã đọc (30080 ký tự).
- document/AIQE AI Agent Architecture & Live Execution/L3_AIQE_AAALE_exercises_vi.md — toàn văn đã đọc (14694 ký tự).

## Unit/keyword → output mapping
Mỗi topic có interview riêng (6 câu), quiz riêng (10 câu, answers tách riêng giải thích A–D) và liên kết nguồn. Tất cả câu hỏi/lab tự biên soạn, không phải answer key của course.

| Nguồn/heading | Keywords/ý cần giữ | Output |
|---|---|---|
| PMLM 1–4: audience, prerequisites, outcomes, working principles | async/await; DOM; HTTP; manual first; labels; locator contract | playwright-locators + execution-debugging |
| PMLM 5.1–5.4 PortalLite | AC-AUTH/EMP/RBAC/AUD; NFR-A11Y/ASYNC; synthetic data; cleanup; Elements/Pages/Steps/Specs | cả ba topic; integrated lab |
| PMLM U1 Session 1–4 | runner, worker, context/page, fixtures, retry/shard, actionability, lazy locator, MCP client/server/tools, observation timeline | execution-debugging |
| PMLM U2 Session 1–4 | package/config/env/browser install; interaction; popup/dialog/download waiter; first login; heading/URL; focused run/discovery/cleanup | execution-debugging; lab |
| PMLM U3 Session 1–4 | DOM/render/accessibility; roles/names/labels; role/label/placeholder/text/testId; filter has/hasText; strictness; tables/dialog/composite; iframe/shadow/virtualization; inventory | playwright-locators |
| PMLM U4 Session 1–4 | priority strategy; i18n; stable identity; testID ownership/naming; CSS/XPath/nth/last/force anti-pattern; refactor naming/count guard | playwright-locators; quiz/interview |
| PMLM U5 Session 1–4 | oracle, web-first assertions, exact/partial/negative, event waiter-before-trigger, response contract, polling/eventual consistency, retry budgets, timeline | execution-debugging |
| PMLM U6 Session 1–4 | bounded prompt, redact, human review checklist, draft errors, provenance/reviewer/validation, no auto-merge | execution-debugging; agent-architecture; lab |
| PMLM U7 Session 1–4 | zero/many/wrong-frame/hidden/detached, overlay, auth expiry, infra blocker, trace/screenshot/video/console/network, manifest, original vs investigation, bug report | execution-debugging; lab |
| PMLM exercises 1.1–1.3; EX-U1-EXEC-MCP; EX-U2-FIRST-LIVE | safety, layer mapping, run record, lifecycle, first-run evidence | execution-debugging; lab |
| PMLM EX-U3-LOCATOR-INVENTORY; EX-U4-HARDEN | six elements, uniqueness guard, risk P0-P3, eight selector refactor, ownership policy | playwright-locators; lab |
| PMLM EX-U5-SYNC; EX-U6-AI-REVIEW | state model, no fixed wait, run matrix, ACCEPT/CHANGE/REJECT/NEEDS-EVIDENCE | execution-debugging; lab |
| PMLM EX-U7-INCIDENT | Confirm duplicate; rerun snapshot; unverified Confirm archive candidate; artifact boundaries | locator + execution quiz; lab |
| PMLM Capstone/trainer setup/pacing | employee lifecycle, optional audit, cleanup, three business test.step, stable target, retained artifacts, critical fail | integrated lab; scope limitations |
| AAALE 1–2 + claim table | one-case scope, no live app/runtime supplied, requirements vs observation/proposal/result/hypothesis/unknown | agent-architecture |
| AAALE U1 1.1–1.4 | goal/planner/controller/runner/adapters/state; tool contracts; allowlist/least privilege; injection; append-only log/checkpoint; duplicate runId; terminal state | agent-architecture |
| AAALE U2 2.1–2.4 | intake/preflight/setup/action/oracle/teardown/review; source IDs; state transitions; grant scope; runner inputs/outputs; bounded review | agent-architecture; lab |
| AAALE U3 3.1–3.4 | error taxonomy, signal wait, read/poll/whole-test retry, ambiguous create, budget/termination, ownership cleanup | agent-architecture; execution-debugging; quiz |
| AAALE U4 4.1–4.4 | manifest/run-attempt correlation, trace modes, report, testInfo.attach referenced source, G1-G4, redaction/review/handoff | agent-architecture; lab |
| AAALE trainer/provenance | simulator vs live; version check; approved runtime; evidence-first reasoning | all topic boundaries; lab |
| AAALE exercises 1.1–1.5 | OBS-PACKET vs live; tool cards six capabilities; no arbitrary shell; manual before AI | agent-architecture; lab |
| AAALE EX-U1-ARCH; EX-U2-WORKFLOW | invariants, injection proposal rejection, source-linked oracle, duplicate protection | agent interview/quiz; lab |
| AAALE EX-U3-RESILIENCE INC-A/B/C/D | read transport, ambiguous write/lookup, assertion timeout, pass+cleanup fail | agent quiz/interview; lab |
| AAALE EX-U4-EVIDENCE RUN-PACKET-04; mẫu nộp | a1 fail/a2 pass; missing G2/G4; placeholder traces; no fabricated command; claim review | agent quiz/interview; lab |

## Nguồn web đã mở đọc, không dựa search snippet
| URL | Title | Ngày truy cập | Version/phạm vi |
|---|---|---|---|
| https://playwright.dev/docs/locators | Locators | 2026-10-25 | Docs hiện hành không pin version; đối chiếu package lock lab |
| https://playwright.dev/docs/actionability | Auto-waiting | 2026-10-25 | Docs hiện hành; bảng checks theo action |
| https://playwright.dev/docs/test-retries | Retries | 2026-10-25 | Docs hiện hành; worker restart, flaky classification |
| https://playwright.dev/docs/trace-viewer-intro | Trace viewer | 2026-10-25 | Docs hiện hành; on-first-retry là mode minh họa template |
| https://modelcontextprotocol.io/specification/2025-06-18/server/tools | Tools | 2026-10-25 | Specification revision 2025-06-18, không khẳng định latest |

Các bổ sung web được gắn nhãn inline “Bổ sung từ nguồn web” và link primary source trong topic. Không chọn agent SDK hoặc suy capability runtime khi chưa có environment. Giữ phần derived web tóm tắt ngắn, phần giảng giải chủ yếu dựa course.

## Xung đột, khoảng trống và quyết định biên tập
- Course mô tả framework layers là convention dạy học; không tuyên bố mọi Playwright project buộc có cả bốn layers. Lab dùng mapping tương đương nếu repo có cấu trúc sẵn.
- Candidate Confirm archive ở EX-U7-INCIDENT chưa được snapshot xác nhận; giữ NEEDS-EVIDENCE thay vì học thuộc selector.
- AAALE dùng approval gate từng run như mẫu shared-lab; environment cô lập có thể được preauthorize. Không biến instruction mô phỏng thành yêu cầu xin phép cho việc viết tài liệu hiện tại.
- Playwright trace intro minh họa config CI retries=2 và on-first-retry; đây không phải đảm bảo config mọi repo. Topic yêu cầu đọc config thực, không suy mặc định runtime.
- PMLM first-login sample dùng env non-null assertion; topic vẫn yêu cầu validate env sớm, không coi dấu ! là runtime validation.
- PortalLite/packets/trace refs là synthetic; không có live app, SDK hoặc run artifacts trong phạm vi bốn nguồn. Chưa chạy E2E; không gán RUN-PASSED cho tài liệu.
- Không mở rộng thành project agent hay framework mới. Optional audit chỉ khi contract/environment expose; SLA search/endpoint không được bịa.
- Coverage là sắp xếp lại kiến thức và giải thích cho fresher; không chép lại rubric từng dòng, không phát hành answer key chính thức.

