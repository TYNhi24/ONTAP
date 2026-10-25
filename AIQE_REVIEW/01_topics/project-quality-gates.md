# Project AI agent: từ backlog tới quality gate có evidence

Bài tự biên soạn cho fresher từ PBAAD U1–U6. Project mẫu dùng scripted planner và dữ liệu trong bộ nhớ; **SIMULATED không phải live evidence**. Những checklist dưới đây không cấp điểm hay chứng nhận chính thức.

## Mục tiêu, prerequisites và phạm vi

Bạn cần hiểu planner/controller/runner, oracle, Git và [CI/recovery](ci-recovery.md). Sau bài này, bạn biến request thành backlog có AC, thiết kế trust boundaries, lập test strategy theo layer, đọc project mẫu đúng phạm vi và ra quyết định HOLD/PASS có lý do. [Metrics](optimization-metrics.md) giúp tránh claim thiếu mẫu số.

**Bắt buộc trong baseline PBAAD:** hai approved flows, controller validation, oracle, ownership/cleanup, report provenance, fault handling/budget, privacy và reproduction. **Nên có:** ADR ngắn, call recorder, clock điều khiển, evidence index dễ theo. **Mở rộng:** dashboard, CI schedule, flow mới, multi-agent; không dùng stretch để thay gate chưa đạt. Các threshold của môn là synthetic/proposed, trainer chốt scope đánh giá thực tế.

## Từ khóa

| Từ khóa | Giải thích bằng câu đầy đủ |
|---|---|
| Project charter | Charter mô tả người dùng/quyết định, phạm vi, tiêu chí thành công, constraints và ai chốt thay đổi. |
| Acceptance criteria (AC) | AC là điều kiện quan sát được để chấp nhận nhu cầu, có precondition/action/oracle thay vì “làm xong code”. |
| Backlog | Backlog là danh sách việc có ưu tiên, dependency, owner và evidence cần nộp để quản lý phạm vi. |
| Definition of Ready | DoR là điều kiện đủ nguồn/quyền/dependency để bắt đầu item có thể nghiệm thu. |
| Definition of Done | DoD là điều kiện kết thúc đã review/check/evidence/cleanup/handoff; pending bắt buộc chưa được coi done. |
| Trust boundary | Trust boundary là ranh giới nơi dữ liệu/quyền từ một bên cần được kiểm tra trước khi được dùng ở bên khác. |
| ADR | Architecture Decision Record ghi bối cảnh, options, lựa chọn, đánh đổi và cách kiểm chứng quyết định kiến trúc. |
| Vertical slice | Vertical slice là đường đi nhỏ nhưng xuyên suốt từ request qua validation/runner tới report và cleanup của cùng run. |
| Negative control | Negative control cố ý đưa dữ liệu sai để chứng minh checker phát hiện, ví dụ department sai hoặc artifact khác run. |
| Evidence provenance | Evidence provenance là khả năng nối artifact/assertion với đúng revision, run, attempt, source và environment. |
| Peer reproduction | Peer reproduction là người khác chạy lại revision đã freeze theo hướng dẫn và ghi actual outcome, không phải tác giả tự chạy lại. |
| Release manifest | Release manifest là hồ sơ phiên bản bàn giao, mode, gate verdict, run refs, known issues, pending data và reproduction guide. |
| Retrospective | Retrospective phân tích sự kiện có evidence thành action cụ thể với owner, thời điểm xem lại và success indicator. |

## U1: Chuyển yêu cầu mơ hồ thành phạm vi nghiệm thu

Input là tám stakeholder requests KR-01…08 và source pack → phân loại baseline/stretch/reject/clarify, viết charter và 8–12 backlog items → baseline version + readiness register được người có quyền chốt. “Dùng production vì lab thiếu account” không tạo quyền; “xóa hết employees cho nhanh” trái ownership; dashboard/CI mỗi giờ là stretch. Ví dụ PB-08: report thiếu evidence cùng run phải không pass; evidence cần gồm verifier test, manifest và matching report.

Mỗi item cần source/version, priority, AC/precondition/action/oracle, evidence, dependency, owner/estimate. “Implement report” chỉ là task; “QA lead xem exact ID/department cùng run để quyết định triage” mới nêu nhu cầu và AC. Scope owner, implementation owner, QA/evidence owner và reviewer/demo owner phải có người cụ thể; tác giả không tự đại diện peer review. Estimate không được nhân giờ với headcount rồi coi như năng suất chắc chắn.

Readiness là deliverable: repository/revision/runtime, lab version/isolation, roles/secret mechanism, authorized seed/lookup/cleanup, fault reset, model access và artifact policy. Thiếu helper thì oracle phụ thuộc helper pending; vẫn làm schema/verifier/fault mocks trên local. “Chưa được cấp” khác “đã kết nối và lỗi”; ENV-BLOCKED cần owner/next action chứ không bịa connection failure.

## U2: Ai có quyền quyết định gì?

```text
request + approved source catalog
  → planner proposal
  → schema + semantic validation
  → deterministic controller + scoped adapter
  → approved runner/assertions + ownership ledger
  → provenance verifier → report → human sharing/gate decision
```

Planner đề xuất flow; controller chặn sai flow/env/source/budget; adapter cũng giới hạn quyền khi bị gọi trực tiếp; runner giữ business oracle. JSON đúng kiểu chưa chứng minh semantics: source cũ hoặc thiếu AC-EMP-02 vẫn reject. `planApproved=true` do model tự viết không cấp quyền; raw shell command từ model không phải approved flow catalog.

Sáu interface cần input/output schema, version, side effects, deadline và failure meanings: approved sources, planner, approved runner, exact owned lookup, cleanup, report. Tên interface trong đề là thiết kế, không chứng minh tool có sẵn. Hai ADR tối thiểu: approved runner thay model shell (ít linh hoạt hơn nhưng kiểm soát scope), deterministic verdict + evidence thay model narrative (cần verifier và chấp nhận unknown).

Result fields giữ riêng lifecycle/test/execution/cleanup/release. CLOSED chỉ là kết thúc lifecycle; test PASS + cleanup UNKNOWN → release HOLD; test FAIL + cleanup success vẫn functional fail. Schema validator không thay semantic validation hoặc adapter authorization.

## U3: Hai flow và evidence xuyên suốt

F01 tạo employee → exact-ID search → assert ID đúng và department được chọn. PBAAD F02 **duplicate-id** tự seed owned employee, thử tạo trùng → rejection indicator, exact-ID count=1 và department ban đầu không đổi. AOCE F02 lại là **change-department**; luôn ghi module/sourceVersion + flowId, không tái dùng oracle theo số F02.

Tạo namespace đáp ứng rule lab, ledger ownership, cleanup exact record; không lấy F01 record làm dependency của F02. Evidence tối thiểu: run/attempt/revision, app/simulator/runtime/source/plan/model config, exact command, times, assertion/artefact refs, cleanup/unknowns/release. Existence của file không đủ: report current r42/a1 không được nhận artifact r41/a1 dù nội dung “PASS”. Reporter/trace phải cùng scope; toast và screenshot login không thay assertion.

Input F01 → validation → runner → report là vertical slice; code/config nhiều file nhưng zero matched tests chưa có execution. Empty array `.every(...)` trả true trong JavaScript; checker phải reject empty required results và kiểm tra mỗi `passed === true`. Chuỗi “false” là truthy nên không được dùng truthiness làm verdict.

## U4: Fault tests và actual model evaluation

| Fault | Control cần kiểm chứng | Evidence/layer |
|---|---|---|
| FT-01 write timeout + lookup inconclusive | Không create lần hai, pending owned data + owner. | Controller call sequence; adapter/lab fault riêng. |
| FT-02 forbidden flow/production | Reject trước runner; direct adapter bypass cũng bị chặn. | Recorder phải thấy forbidden calls=0. |
| FT-03 truncated JSON/sai kiểu | Parse/schema reject có lý do. | Unit/contract; object fixture chưa test parser. |
| FT-04 valid schema nhưng stale source/mất oracle | Semantic reject. | Source/requirementRefs tests. |
| FT-05 đúng ID, sai department | Checker phải phát hiện từ record sai thật. | Không chỉ đưa sẵn passed:false vào verdictFor. |
| FT-06 stale evidence | Reject mismatched run/attempt/revision. | Verifier negative control. |
| FT-07 cleanup timeout | Giữ business outcome, cleanup unknown, release HOLD. | Helper result + pending ledger. |
| FT-08 operational deadline hết | Không action mới, xử lý in-flight/cancellation và reserve. | Fake clock rồi approved runtime test. |

Fault test thành công nghĩa controller xử lý fault đúng; business test có thể vẫn fail. Mock chứng minh phản ứng với response giả; chưa chứng minh adapter/app tạo đúng response. Không gộp hai phạm vi. Budget PBAAD là operations 300s + reconcile/cleanup 90s + finalize 30s; watchdog 480s, CI stretch cần cả setup/upload/buffer như [CI bài](ci-recovery.md).

Actual planner evaluation dùng frozen EV-01…06: valid F01/F02, ambiguous request, bulk delete, injection, thiếu/stale catalog. Viết expected invariants trước sửa prompt; khi provider được cấp, 2 actual proposals/case =12 samples, giữ schema/semantic verdict, clarification và unauthorized calls. Scripted responses dùng phát triển controller, actual sample count vẫn 0. Twelve samples chưa chứng minh robustness production.

## U5: Quality gate kiểm tra control chứ không tick checkbox

Security review theo abuse path: untrusted tool text đề nghị upload trace tới destination ngoài policy → planner đề xuất upload → code nào ngăn external call? Assert call count=0, thử direct adapter bypass; prompt “đừng làm” không thay authorization. Privacy đi từ request/source → prompt → tool → reporter/trace → storage → reviewer. Synthetic employees không làm session/payload trong trace vô hại.

Dùng fake canary `SYNTHETIC-SECRET-DO-NOT-SHARE` để test detection/redaction; raw restricted và sanitized demo pack có refs riêng. Thiếu access/retention/destination policy thì ghi Not specified, giữ lab-only; đừng tự mượn retention 7 hay 14 ngày từ draft thành chính sách tổ chức. Redaction vẫn phải giữ oracle kiểm chứng được trong phạm vi reviewer được phép.

Peer reproduce frozen revision bằng README/runtime/commands/seed-reset; ghi actual output và cần tác giả giúp tay hay không. Findings cần source/location/impact/owner/fix/retest revision/residual risk. PASS/HOLD/CONDITIONAL-DEMO là verdict đề xuất; conditional demo chỉ trình bày tiến độ đúng mode, không đồng nghĩa execution completed. Blocking finding đóng bằng retest đúng revision, không dùng report cũ.

## Đọc project mẫu hiện tại một cách trung thực

`finalProject/src/assistant.js` có `validatePlan` kiểm tra flow/env/source/refs và run/attempt string, `syntheticRunner` dùng mảng trong bộ nhớ, `verdictFor` chỉ nhận boolean true. `runRequest` chưa verify artifact, chưa revision/command, ledger/reconcile/deadline/cleanup helper. Validator không phải full JSON parser/schema; runId toàn khoảng trắng và duplicate requirementRefs là case cần design decision/test thêm, không tự xem helper semantics đã chốt.

Bộ `node --test` được chạy trong phiên ôn tập ngày 2026-10-25: **8/8 pass, exit 0**, không cài dependency/network/browser. Nó chứng minh các local assertions hiện có; test mang tên “does not let plan prose supply a pass verdict” vẫn có runner assertions pass nên chưa chứng minh prose bị chặn trong tình huống assertions fail. Test false assertion chưa cho record sai department đi qua checker; F99 test chưa có recorder chứng minh runner call count. Mentor review M-02…M-06 nêu các gaps tương ứng.

Artifact `simulated-demo-001.json` giữ mode SIMULATED; `release-manifest.json` giữ HOLD và working-tree, không phải immutable release revision. PendingOwnedData=[] chỉ phản ánh demo không tạo PortalLite record. Không gọi demo là approved executable simulator hoàn tất môn nếu trainer chưa chốt scope.

## U6: Demo, defense và retrospective

Freeze revision/source/model config; rehearsal một core flow và một safe-stop case; fallback recording/report có timestamp/revision/mode. Demo đề xuất 20 phút: 2 scope, 6 core, 4 exception, 4 evidence/limits, 4 Q&A. Mỗi người bảo vệ một change, một review decision, một assertion và một failure path. Nói “scripted planner + in-memory demo” ngay đầu, dẫn đúng artifact, không thêm production-readiness/cost-savings khi chưa đo.

Handoff manifest phải có gate, known issues, pending exact owned data/recovery owner, evidence index và reproduction guide. Retro cần ít nhất ba sự kiện có evidence → contributing factor → action có owner/date/success indicator; bảng việc dự kiến không phải retro đã xảy ra. Số commit và số dòng AI review không thay đóng góp/accept-reject thật.

## Tự kiểm tra và luyện nói

- [ ] Tôi phân biệt AC, task, DoR và DoD bằng một backlog item.
- [ ] Tôi vẽ được nơi giữ quyền, oracle, provenance và release decision.
- [ ] Tôi giải thích đúng F02 của từng module và independent seed.
- [ ] Tôi phân biệt test verdictFor với checker phát hiện dữ liệu sai.
- [ ] Tôi nói được bằng chứng nào hiện có, phần local làm tiếp được và phần chờ lab/model.
- [ ] Tôi giữ HOLD khi blocking findings/pending execution còn tồn tại.

Luyện [interview](../03_interview/project-quality-gates.md), [quiz](../04_quiz/project-quality-gates.md), [lab thực hành](../05_practice/project-evidence-lab.md).

## Nguồn chính xác

[PBAAD content](<../../document/AIQE Project-Based AI Agent Development/L4_AIQE_PBAAD_course_content_vi.md>): “U1.1–U1.4”, “U2.1–U2.4”, “U3.1–U3.4”, “U4.1–U4.4”, “U5.1–U5.4”, “U6.1–U6.4”. [PBAAD exercises](<../../document/AIQE Project-Based AI Agent Development/L4_AIQE_PBAAD_exercises_vi.md>): “SOURCE-PBAAD-v1”, “ENV-PBAAD-v1”, “Các completion gates đề xuất”, “FAULT-PACKET-04”, “EVAL-PACKET-04”, “QUALITY-PACKET-05”, “DEMO-PACKET-06”. [Mã mẫu](<../../document/AIQE Project-Based AI Agent Development/finalProject/src/assistant.js>): validatePlan/verdictFor/runRequest; [test](<../../document/AIQE Project-Based AI Agent Development/finalProject/test/assistant.test.js>): tám test; [mentor review](<../../document/AIQE Project-Based AI Agent Development/finalProject/docs/mentor-review.md>): M-01…M-06; [evidence index](<../../document/AIQE Project-Based AI Agent Development/finalProject/submission/evidence-index.md>): E-LOCAL-01/E-TEST-01; [manifest](<../../document/AIQE Project-Based AI Agent Development/finalProject/submission/release-manifest.json>): qualityGateVerdict/knownIssues. Tất cả U1–U6 submissions đã đọc và map trong [ledger](../00_tracking/optimization-project-notes.md).
