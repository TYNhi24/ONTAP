# Lab: bảo vệ claim bằng evidence project

Bài tập tự biên soạn, không phải handout/đáp án chính thức. Mục tiêu là đọc, kiểm tra và viết quyết định có thể bảo vệ; không yêu cầu cài dependencies, gọi model, mở browser, truy cập public demo hay deploy CI. Giữ nguyên mọi source gốc. Làm vào thư mục mới `AIQE_REVIEW/05_practice/my-project-evidence/` do bạn tạo; không điền kết quả thay cho việc chưa làm.

## Chuẩn bị và đầu vào

Đọc [metrics](../01_topics/optimization-metrics.md), [CI/recovery](../01_topics/ci-recovery.md), [project gates](../01_topics/project-quality-gates.md). Cần Node.js có sẵn để chạy bộ test local; thiếu Node thì làm phần đọc và ghi execution pending. Không cài runtime/dependency chỉ để hoàn thành lab này.

Nguồn có thật:

- [Project README](<../../document/AIQE Project-Based AI Agent Development/finalProject/README.md>), headings “Bài hiện làm được gì?”, “Cách chạy”, “Kết quả và giới hạn”.
- [Code](<../../document/AIQE Project-Based AI Agent Development/finalProject/src/assistant.js>), các hàm validatePlan, verdictFor, syntheticRunner, runRequest; [tests](<../../document/AIQE Project-Based AI Agent Development/finalProject/test/assistant.test.js>).
- [Evidence index](<../../document/AIQE Project-Based AI Agent Development/finalProject/submission/evidence-index.md>), [release manifest](<../../document/AIQE Project-Based AI Agent Development/finalProject/submission/release-manifest.json>), [demo artifact](<../../document/AIQE Project-Based AI Agent Development/finalProject/submission/runtime-artifacts/simulated-demo-001.json>).
- [AOCE exercises](<../../document/AIQE Agent Optimization & CI Execution/L3_AIQE_AOCE_exercises_vi.md>), BENCH-PACKET-01, OUTPUT-PACKET-01, CI-PACKET-05, INCIDENT-PACKET-06, METRIC-PACKET-07.
- [PBAAD exercises](<../../document/AIQE Project-Based AI Agent Development/L4_AIQE_PBAAD_exercises_vi.md>), SOURCE-PBAAD-v1, FAULT-PACKET-04, EVAL-PACKET-04, QUALITY-PACKET-05, DEMO-PACKET-06.

**Bắt buộc:** tasks 1–7 và report scope trung thực. **Nên có:** bạn khác kiểm tra arithmetic và chạy lại local với cùng revision. **Mở rộng:** task8 chỉ là backlog thiết kế; actual app/model/CI execution cần readiness được cấp riêng, không phải điều kiện để thực hiện bản lab offline này.

## 1. Tạo claim inventory trước khi nhìn mentor review — 20 phút

Viết ít nhất sáu claim có thể kiểm tra từ source: F01/F02 làm gì; flow/env bị giới hạn ở đâu; verdict tính từ đâu; artifact giữ mode nào; cleanup có thật chưa; model có thật chưa. Với mỗi claim điền:

| Claim | Source path + hàm/heading | Loại: contract/code/static/runtime | Điều chứng minh được | Gap | Next action/owner đề xuất |
|---|---|---|---|---|---|
| Tự điền | Tự điền | Tự điền | Tự điền | Tự điền | Tự điền |

Không gọi code path là runtime evidence khi chưa chạy; không gọi fake planner là actual-model eval. So sánh F02 của AOCE và PBAAD, nêu vì sao phải ghi sourceVersion + flowId thay vì chỉ “F02”.

## 2. Chạy bộ test local hiện có — 15 phút

Từ root workspace trên PowerShell:

```powershell
Push-Location -LiteralPath 'document/AIQE Project-Based AI Agent Development/finalProject'
try {
    node --version
    node --test
} finally {
    Pop-Location
}
```

Các lệnh này không cài dependency hay gọi browser/app/model. Ghi ngày giờ, working directory, Node version, exact command, exit code và test summary thực thấy. Không tự sửa source để ép pass. Khi kiểm tra trong phiên biên soạn 2026-10-25, command `node --test` đạt 8/8, exit0; đây là mốc tham khảo **không thay kết quả bạn chạy**. Source content hash được giữ trong extraction ledger; working-tree không phải immutable release SHA.

Kết luận tối đa: các local test assertions hiện có đạt tại tree đã đọc/chạy. Không kết luận HR Admin quyền đúng, UI locators ổn, ownership cleanup thành công, model robust hay quality gate hoàn tất. Không gọi `npm test` của starter Playwright vì đó là browser/live test ngoài scope lab offline.

## 3. Kiểm tra test đang chứng minh đúng điều gì — 25 phút

Mở test “returns FAIL when an assertion already reports failure” và lần theo verdictFor. Input đã chứa `passed:false`, chưa có record department sai đi qua checker. Viết negative-control design có expected QA nhưng observed Sales và chỉ ra checker cần tính assertion nào. Đây là design-only nếu bạn chưa implement ở bản sao riêng.

Mở test “does not let plan prose supply a pass verdict”: runner result của trường hợp đó vẫn PASS. Thiết kế counterexample runner assertion FAIL trong khi prose yêu cầu PASS; cần injection boundary cho fake runner hoặc checker/report verifier để test được. Không mô tả test hiện tại như đã chứng minh scenario mới.

Mở F99 rejection test: có assert throws, chưa call recorder. Ghi kiểm tra mạnh hơn cần runner call count=0. Test source cũ/thiếu AC-EMP-02 có thật; truncated JSON parser, production riêng, deadline và stale-evidence tests chưa có trong bộ tám. Dùng bảng coverage theo layer, không chỉ đếm tên tests.

## 4. Thiết kế verifier evidence và tám fault outcomes — 30 phút

Trên giấy hoặc file Markdown, đề xuất input/output cho verifier: current revision/run/attempt/source/flow + required assertion IDs + artifacts có metadata → accept/reject + reasons; không để narrative thay verdict. Ít nhất thử các fixtures tự biên soạn sau và ghi **expected**, không ghi actual khi chưa chạy:

| Fixture | Dữ liệu | Expected invariant |
|---|---|---|
| NC-01 | ID đúng, expected QA, observed Sales | Business assertion FAIL. |
| NC-02 | Current r42/a1, artifact r41/a1 | Evidence mismatch, không claim current pass. |
| NC-03 | Current run đúng nhưng revision/source cũ | Reject provenance/contract mismatch. |
| NC-04 | Required results rỗng | Không pass bằng every trên empty array. |
| NC-05 | passed là chuỗi “false” | Không chấp nhận truthy thay boolean true. |
| NC-06 | Business PASS, cleanup timeout | Giữ business PASS, cleanup UNKNOWN, release HOLD. |

Đối chiếu FT-01…08 trong handout: với mỗi case ghi state, allowed/blocked calls, test outcome, execution outcome, cleanup outcome, release decision, required evidence và layer. Với unknown write/lookup inconclusive, expected create calls không tăng trước reconcile; deadline hết thì không operation mới, giữ in-flight/pending owner. Không thử fault bằng mutating action trên public/production.

## 5. Sửa metrics trong bản review riêng — 25 phút

Dùng E01…E10 và SL-01…04 của METRIC-PACKET-07. Tính selected/executed/first-pass/eventual/flaky, retry overhead, full-evidence count, evidence-complete-pass count, cleanup completion, measured subtotal, cost/evidence-complete pass, schedule completeness, dispatch/queue median và duration median/range. Mỗi dòng nêu numerator/denominator/EIDs/units/unknowns.

Mốc tự kiểm tra sau khi làm: executed8/10; first4/8; eventual6/8; flaky2/8; attempts11; retry overhead3; full evidence7/8; evidence-complete passes5; cleanup4/6; measured .89; cost/evidence-complete pass .178 lower bound; schedule3/4; dispatch median2 phút; queue median2 phút; test duration median82.5s, range40–170. E08 missing usage không thành0; remaining budget<=.31 nếu phần thiếu không âm. Dữ liệu synthetic không chứng minh actual billing.

Đọc bài nộp U7 rồi ghi ít nhất ba discrepancies có source/heading và correction. Không sửa packet/submissions gốc. Phân biệt lỗi arithmetic, định nghĩa metric và claim vượt scope.

## 6. Review CI draft mà không deploy — 25 phút

Mở [U5_workflow.yml](<../../document/AIQE Agent Optimization & CI Execution/NhiTY14/submissions/U5/U5_workflow.yml>) và [U5_playwright-config.ts](<../../document/AIQE Agent Optimization & CI Execution/NhiTY14/submissions/U5/U5_playwright-config.ts>). Đối chiếu starter package.json để tìm prerequisites còn thiếu: flows/tags/scripts/helpers/secrets/ledger. Viết tám outcomes CI-51…58 bằng từ của bạn.

Nêu ba câu hỏi review sâu: ledger local trong test-results có bị runner reset hay mất khi force cancel? Config CI không có HTML reporter nhưng workflow upload playwright-report thì evidence contract trông đợi gì? Reconcile step cần credential/authorization nào để đọc durable source, trong khi step env hiện chỉ có runId/path? Chưa có helper implementation thì đây là design gaps cần chốt, không khẳng định runtime failure đã quan sát.

Chuyển cron UTC 18:17 sang VN01:17 ngày sau; ghi default branch phải xác minh tên thật. Chọn lock scope theo shared environment, không branch. Retention14 ngày trong draft và7 ngày trong course là ví dụ khác nhau, không tự thành policy được duyệt.

## 7. Nộp quality-gate memo và demo ngắn — 25 phút

Đầu ra trong thư mục bài làm riêng:

```text
claim-inventory.md
local-run-evidence.md
fault-and-negative-controls.md
metrics-recalculated.md
ci-design-review.md
quality-gate-memo.md
review-decisions.md
```

Memo tối đa khoảng một trang: scope/version/mode, checks actual, checks design-only, pending local/lab/model/peer riêng, gate verdict và lý do, findings/owner/next evidence. Dùng **HOLD** nếu blocking controls chưa verified; có thể demo tiến độ có disclose, không đổi thành release-ready.

Tập nói 3 phút:30s scope/mode,60s một assertion và actual local test,45s unknown-write safe stop chỉ ở design,45s evidence/gaps/HOLD. Người nghe hỏi: “8/8 có chứng minh model đúng không?”, “vì sao không retry Save?”, “record nào thuộc run?”, “stale artifact bị chặn ở đâu?”. Nếu chưa có verifier, trả lời đúng “chưa implement”, dẫn next test.

Review log cần ít nhất hai quyết định accept/reject **thực tế của bạn**, source, lý do, change và check. Không để AI điền bạn đã đồng ý. Retro chỉ dùng sự kiện thật trong lab đọc/chạy của bạn; proposed work chưa thực hiện giữ kế hoạch.

## 8. Backlog extension sau offline lab

Chỉ sau readiness/authorization phù hợp: làm trong bản sao project, thêm full schema/verifier, injectable runner/clock và eight fault tests trước lab adapter; peer reproduce frozen revision; actual model6cases×2proposals với provider/config cố định; approved lab F01/F02 và cleanup; CI nếu chọn cần actual manual rồi scheduled evidence. Không deploy workflow draft hoặc gửi artifact ra ngoài chỉ để có evidence.

## Tự đánh giá

Đạt bài ôn offline khi mọi actual claim có source/lệnh/kết quả, mọi design-only được gắn nhãn, các phép tính đúng và known gaps có next action. Không cộng điểm để bù false pass, unauthorized call, secret exposure hay xóa sai ownership. Hoàn thành bài ôn offline không đồng nghĩa hoàn thành G1–G6 của học phần.
