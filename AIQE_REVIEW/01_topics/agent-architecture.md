# Agent QA: goal, controller, tool và bằng chứng của một E2E case

> Bản ôn tập tự biên soạn cho fresher. Nội dung khóa học là nguồn chính; đoạn web được gắn nhãn riêng. Không phải đáp án chính thức.

## Mục tiêu và kiến thức cần có
Thiết kế agent hẹp cho một case, enforce tool/state/budget bằng controller và báo đúng result, cleanup, approval gap.

Đọc [Execution và evidence](playwright-execution-debugging.md), [Locator](playwright-locators.md); biết case có precondition/action/oracle và đọc TypeScript object/union.

## Mức ưu tiên
Bắt buộc: goals/tools/state/policy, deterministic controller, least privilege, injection boundary, duplicate protection, retry/termination, claim labels và report. Nên biết: checkpoint phục hồi, append-only event log, approval expiry. Mở rộng: agent SDK cụ thể sau khi lab xác nhận version/capabilities; không cần xây multi-agent.

## Từ khóa bằng câu đầy đủ
Goal mô tả kết quả cần đạt trong phạm vi đã cấp. Planner đề xuất hành động từ context. Controller quyết định transition và quyền gọi tool bằng code/policy. Tool adapter chuyển input được duyệt sang runtime. State store giữ trạng thái có thể kiểm tra thay vì dựa model memory. Guardrail giới hạn input, quyền, data và budget. Idempotency tránh lặp side effect nhưng không được giả định từ run ID.

## Học từ đầu: cái gì, vì sao và khi nào
Agent hữu ích khi cần đọc case, kiểm tra readiness, chọn công cụ trong phạm vi, đọc kết quả và đề xuất triage. Nó không thay test runner hoặc tự xác nhận oracle. Hãy bắt đầu bằng goal nhỏ: chạy EMP-CREATE-01 một lần trên isolated-lab, kiểm tra AC-EMP-01/02, cleanup record của run, chuẩn bị report cho QA review. Sửa code, đổi assertion hoặc publish là phạm vi khác.

Planner có thể đề xuất sai; controller phải kiểm tra case/environment allowlist, schema, phase, approval scope và budget trước tool call. Runner nhận caseId/environmentAlias/runId/revision đã validate, không nhận shell command tự do. Adapter không được cấp thêm quyền. Webpage chứa “ignore all policies” vẫn là dữ liệu, không trở thành instruction. Prompt cẩn thận không thay thế permission và validation.

State có runId, caseId, sourceIds, revision, phase, attempt, budget, createdRecordId, evidenceRefs, approvalRef và cleanupOutcome. Chuỗi minh họa: DRAFT → WAITING_APPROVAL → READY → RUNNING → COLLECTING → CLEANING → AWAITING_REVIEW → terminal. PASSED cần assertion đúng attempt, evidence đủ, cleanup được xử lý và QA review theo policy module. Assertion pass nhưng cleanup fail phải giữ test result pass đồng thời báo workflow chưa hoàn tất/BLOCKED. Đây là hai tầng kết quả khác nhau.

Retry phải tách lớp. Read-only transport lỗi có thể retry trong budget; polling giữ nguyên oracle; whole-test retry cần data/cleanup độc lập và giữ failed attempt. Create timeout có thể đã commit: dừng write, lookup đúng owned ID qua approved read path, kiểm tra quyền rồi quyết định. Duplicate runId bị từ chối hoặc trả existing status chỉ ngăn duplicate command ở controller, không chứng minh API business idempotent.

Khi budget hết, user cancel, mất scope, write ambiguous hoặc cleanup fail: dừng side effect mới, giữ evidence, cleanup chỉ khi còn quyền và xác định ownership; nếu không, giao owner xử lý. Report gắn run/attempt/revision/environment với command thực, assertion, artifact, cleanup, unknown và human decision. Approval được dùng theo scope đã cấp; không hỏi lặp lại nếu policy và grant hiện tại đã bao phủ. Gate trong course là thiết kế lab, không phải tính năng mặc định của MCP/SDK.

## Input → xử lý → output
AC-EMP-01/02 + tool manifest + approved scope + state → controller validate, chạy allowlisted case, thu đúng attempt, cleanup và QA review → execution report có claim/evidence và trạng thái workflow riêng test result.

## Ví dụ fresher
```ts
// Pseudocode thiết kế; không phải agent runtime đã chạy.
if (state.phase !== 'READY' || !grant.covers(state)) {
  throw new Error('Run chưa đủ điều kiện');
}
const result = await tools.run_case({
  caseId: state.caseId, environmentAlias: state.environmentAlias,
  runId: state.runId, revision: state.revision
});
// Controller còn phải correlate attempt, giữ evidence và cleanup.
```

grant.covers và tools.run_case là interface minh họa do lab phải hiện thực, không phải API có sẵn của SDK.

## So sánh dễ nhầm
| Thành phần | Trách nhiệm | Sai lầm |
|---|---|---|
| Planner | Đề xuất bước và rationale | Tự đổi oracle cho pass |
| Controller | Validate quyền/state/budget | Tin mọi model proposal |
| Runner | Chạy assertions, xuất result | Được xem như approval engine |
| MCP | Giao diện discovery/call tool | Được coi là quyền vô hạn |
| Evidence store | Giữ artifact/provenance | Ghi đè first failure |
| QA reviewer | Xác nhận claim/gate | Chỉ đọc summary bỏ artifact |

## Bẫy quiz và phỏng vấn
Không suy “thao tác được” thành “đúng nghiệp vụ”; không lấy một output từ tool làm nguồn cho mọi claim. Khi trả lời phỏng vấn, nêu intent, cơ chế, ví dụ cụ thể và giới hạn evidence. Xem [bộ phỏng vấn](../03_interview/agent-architecture.md) và [quiz tự luyện](../04_quiz/agent-architecture-questions.md), làm trước khi mở đáp án.

## Tự kiểm tra
- [ ] Thiết kế sáu tool cards
- [ ] Viết ba invariant
- [ ] Xử lý create timeout nhưng lookup thấy record
- [ ] Phản biện “a2 pass nên xóa a1”
- [ ] Tách cleanup fail khỏi assertion pass.

## Nguồn và phần bổ sung
Nguồn khóa học: [course](../../document/AIQE%20AI%20Agent%20Architecture%20%26%20Live%20Execution/L3_AIQE_AAALE_course_content_vi.md), [bài tập](../../document/AIQE%20AI%20Agent%20Architecture%20%26%20Live%20Execution/L3_AIQE_AAALE_exercises_vi.md). Heading đối chiếu chính xác: AAALE Unit 1 — Agent architecture: goals, tools, state, guardrails and run controller; Unit 2 — Designing an agent workflow for one E2E test case; Unit 3 — Error handling, retries, resilient waits and safe termination; Unit 4 — Evidence capture, execution reporting and human approval gates. Exercises EX-U1-ARCH, EX-U2-WORKFLOW, EX-U3-RESILIENCE, EX-U4-EVIDENCE.

Bổ sung từ nguồn web: MCP mô tả tools với name/schema và discovery bằng tools/list, invocation bằng tools/call; protocol không bắt buộc một interaction model cụ thể. Quyền và controller của lab phải được xây ở implementation. [MCP Tools, revision 2025-06-18](https://modelcontextprotocol.io/specification/2025-06-18/server/tools).

