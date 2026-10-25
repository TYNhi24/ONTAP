# CI execution, điều tra flaky và recovery an toàn

Bài ôn tự biên soạn, không phải đáp án chính thức. Các CI/incident packets AOCE là **SIMULATED**; workflow trong submissions là draft, chưa deploy.

## Mục tiêu và kiến thức trước

Bạn cần biết test assertion và async/await; đọc [metrics](optimization-metrics.md) để hiểu selected/executed/attempt. Sau bài này, bạn thiết kế được PR/manual/scheduled lanes, phân tích bốn incidents và biết khi nào được đọc lại, khi nào phải dừng ghi. [Quality gate project](project-quality-gates.md) giải thích cách đưa kết quả này vào bàn giao.

**Bắt buộc:** preflight, allowlist, nonzero execution, evidence matching, exit code thật, owned cleanup và bounded recovery. **Nên có:** manifest máy đọc được, trace policy, durable ownership ledger và missing-slot monitoring khi chạy write jobs. **Mở rộng:** schedule/live CI chỉ sau quyền lab và manual validation; chạy model trong CI cần policy/budget riêng.

## Từ khóa

| Từ | Định nghĩa |
|---|---|
| CI lane | CI lane là luồng kiểm tra có trigger, mục tiêu và quyền riêng, ví dụ PR static hoặc manual live smoke. |
| Preflight | Preflight là bước xác minh environment/account/role/readiness/data/budget trước execution, trả lỗi rõ khi thiếu điều kiện. |
| Test discovery | Test discovery là tìm các test khớp selector; có tên test chưa chứng minh assertion đã chạy. |
| Deterministic runner | Deterministic runner chạy test đã version/review và tính outcomes từ assertions thay vì lời model. |
| Artifact | Artifact là file/report/trace được giữ để review; upload tồn tại chưa đảm bảo nội dung đầy đủ hoặc đúng run. |
| Concurrency group | Concurrency group là phạm vi phối hợp các job tranh chấp cùng tài nguyên; branch khác nhau vẫn có thể tranh cùng lab. |
| Flaky | Flaky theo runner là test fail lần đầu rồi pass khi retry; nhãn này không xác nhận nguyên nhân. |
| Reconcile | Reconcile là đối chiếu trạng thái thực bằng helper được phép với exact owned ID trước quyết định xử lý write chưa rõ. |
| Unknown write | Unknown write là trạng thái client chưa biết thao tác ghi đã xảy ra hay chưa, ví dụ timeout sau Save. |
| Idempotency | Idempotency là tính chất thao tác lặp lại không tạo thêm hiệu ứng ngoài kết quả đã định nghĩa; phải có contract, không suy từ tên API. |
| Actionability | Actionability là điều kiện phần tử đủ sẵn sàng cho action; nó khác việc transaction nghiệp vụ đã hoàn tất. |
| Quarantine | Quarantine là tạm tách test có vấn đề với owner/expiry/coverage thay thế, vẫn báo debt thay vì xóa lịch sử flaky. |

## CI chạy gì và vì sao phải tách lanes?

Input → process → output: trusted revision + approved selector + lab policy → install locked deps, preflight, discover, execute, reconcile, capture/upload và verify evidence → report per-case, attempts, cleanup và gaps. Agent có thể chuẩn bị test/triage; CI không cần mỗi đêm tự sinh assertion mới rồi tự công bố pass.

| Lane | Input/quyền | Output được phép kết luận |
|---|---|---|
| PR | Diff, static fixtures; không cần live secrets | Typecheck/regression/discovery đúng scope; chưa phải live pass. |
| Manual live smoke | Trusted revision, lab role, ownership và helper được cấp | Matching runtime assertions + cleanup + artifact review. |
| Scheduled live smoke | Cùng prerequisites; trigger schedule được quan sát | Runtime của scheduled run cụ thể; manual run không chứng minh schedule. |

Starter OrangeHRM hiện chỉ có login/dashboard test. Thiếu credentials thì `test.skip` chứ không assert app; không được lấy job xanh/skipped làm live acceptance. `.env.example` trỏ public demo làm mặc định; write flows phải dùng isolated instance. `package.json` chưa có preflight/reconcile, F01–F03/tag @smoke chưa được implement; copy draft U5 vào CI sẽ không tự tạo những thứ đó.

Cron UTC `17 18 * * *` tương ứng 01:17 Việt Nam ngày kế tiếp. **Bổ sung web đã mở 2026-10-25:** GitHub mặc định schedule theo UTC, hiện có tùy chọn IANA timezone; schedule dùng default branch, có thể trễ hoặc bị bỏ lúc tải cao. Do đó ghi expected slot, dispatch và start riêng, đừng hứa đúng từng phút. [GitHub Events: schedule](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#schedule).

## Tám lỗi vận hành cần nhận ra

| Card | Điều cần làm | Vì sao |
|---|---|---|
| CI-51 fork PR không có live secrets | Giữ PR lane không dùng live account. | Thiếu secret không thành quyền dùng account khác. |
| CI-52 thiếu password nhưng wrapper “passed” | Preflight fail, executed=0. | Không assertion thì chưa có live result. |
| CI-53 0 test với pass-with-no-tests | Chặn empty selection cho required suite. | Exit 0 không chứng minh requirement. |
| CI-54 failure không có artifact | Cả capture policy và upload-on-failure. | Upload không tạo trace chưa capture. |
| CI-55 force cancel sau write | Pending ledger + owner/outside-job reconcile. | always() không đảm bảo chạy khi process/runner mất. |
| CI-56 hai branch cùng lab | Phối hợp theo environment dùng chung và namespace độc lập. | Lock theo branch không khóa chung tài nguyên. |
| CI-57 workflow chỉ trên feature branch | Xác minh default branch và trigger metadata. | Config tồn tại chưa chứng minh schedule active. |
| CI-58 cleanup lỗi bị || true | Giữ test outcome, cleanup failure và release HOLD riêng. | Làm xanh job sẽ che pending data. |

Không dùng file local làm nguồn ownership bền vững duy nhất sau runner mất. Ledger/helper phải được cấp và có semantics/authorization; không invent endpoint hoặc đọc DB quyền rộng. Preflight check-then-create cũng có race; lookup trống không thay thế unique run identity hoặc lock/lease thích hợp. Namespace phải đủ run/attempt/flow/worker trong scope thực tế. Browser context mới không cô lập database.

## Triage theo timeline trước khi sửa

Input incident gồm revision, attempt, actions, network/DOM/helper/reporter và cleanup → tách fact/hypothesis/gap → chọn phép kiểm tra phân biệt giả thuyết → fix ở lớp gây lỗi → negative controls + retest unchanged oracle. Một log lỗi đơn lẻ chưa phân biệt app defect, locator bug, data collision và environment.

**INC-61:** page có hai Save buttons, strict-mode violation trước click. DOM card cho dialog Create employee có một Save. Scope dialog rồi button; nếu overlay che thì đợi condition từ observation. `.first()` chỉ chọn theo thứ tự, không giải nghĩa target. `force:true` không chữa ambiguous locator; sleep 5s không chứng minh readiness.

**Bổ sung web:** click bình thường kiểm tra unique element, visibility, stability, receives-events và enabled; force bỏ một số kiểm tra không thiết yếu, ví dụ receives-events. Không nói force luôn bỏ mọi visibility/enabled check như vài đoạn bài nộp. Actionability pass vẫn chưa chứng minh ID/department. [Playwright Auto-waiting](https://playwright.dev/docs/actionability), mở 2026-10-25.

**INC-63:** main page không thấy row; target nằm trong iframe và virtualized list chỉ render 20 rows. Scope frame từ observation, search exact owned ID theo UI contract rồi assert một row có exact cell ID và department Engineering. `filter({hasText: id})` trong pseudocode bài nộp có thể khớp substring; ID E2E-1 không được chấp nhận từ E2E-10. Không đoán accessible name `/search/i` là đã verify DOM. API tồn tại không thay UI oracle.

**INC-64:** browser permission exception trước test body là infrastructure/environment blocked; không có assertion để kết luận app flaky. Kiểm tra install/runtime/permissions theo policy runner, giữ exception evidence; không mặc định bỏ sandbox để né lỗi. Sau environment fix, chạy lại approved preflight/test và giữ revision/config rõ.

## Unknown write: đọc lại khác ghi lại

INC-62: Save được gửi lúc t+0; client timeout t+1500; server fixture ghi created t+1800; UI search chưa thấy row t+2100; lookup t+2600 trả owned record department QA. Sự tồn tại đã được fixture xác nhận, nhưng search assertion vẫn pending. Không click Save lại và không kết luận AC-EMP-02 pass từ lookup alone.

```text
write timeout → đóng mutating path → exact owned lookup
  found + ownership confirmed → tiếp tục oracle read-only trong budget / cleanup theo policy
  confirmed absent + replay contract đủ → chỉ cân nhắc retry đã được review
  inconclusive → safe stop, pending record, recovery owner và next evidence
```

Reconcile thành công không sửa test failure cũ. Cleanup chỉ exact owned record có bằng chứng; “xóa mọi E2E-*” không đủ ownership. Nếu deadline hết khi operation còn in-flight, dừng nhận action mới, truyền cancellation nếu adapter hỗ trợ, giữ outcome unknown và recovery owner. Không hứa cleanup hoàn tất sau hard kill.

Retry từng lớp có thể nhân chi phí: 3 agent attempts × 2 tool × 2 runner=12 executions. Dùng tổng budget controller và attempt ledger. AOCE packet có tối đa một runner retry khi safe, một tool-read recovery, 20 phút wall-time; đây là policy lab, không phải mặc định Playwright. PBAAD có budget khác: 300s operations +90s reserve +30s finalize; watchdog đề xuất 480s, CI stretch tổng 900s. Không kế thừa 20 phút AOCE vào project PBAAD.

**Bổ sung web:** Playwright giữ nhãn passed/flaky/failed theo attempts và có thể tạo worker/browser mới sau failure; setup vì vậy phải an toàn khi chạy lại. [Playwright Retries](https://playwright.dev/docs/test-retries), mở 2026-10-25. Rerun pass một lần chỉ là observed outcome. Fix cần reason, before/after evidence và negative control; bản code sửa có revision mới, nên ghi baseline revision và fixed revision riêng với cùng dataset/build/config liên quan.

## Version control và kiểm chứng fix

Version code cùng prompt/context selector/tool schema/catalog/fixtures/model config nếu ảnh hưởng behavior. Staging có chọn lọc; `.gitignore` không xóa secret đã track/history. Auth state/trace có thể chứa thông tin nhạy cảm; không đưa vào prompt/source để tiện review. Nếu có secret lộ, xử lý revoke/rotate theo owner trước; untrack file không thu hồi secret.

Khi merge prompt conflict, giữ exact ID+department, matching runner evidence, UNKNOWN fields và word budget đã review; đừng lấy nhánh “mới nhất” theo thói quen. Sau resolve cần checks trên revision mới. Revert code/prompt không đảo write side effects; cần reconcile dữ liệu và xử lý active schedules/runs riêng. Lệnh revert merge commit trong bài nộp là minh họa, chưa đủ tham số/chọn mainline cho mọi lịch sử Git; không copy mù.

## Tự kiểm tra và phỏng vấn

- [ ] Tôi phân biệt discovery/static checks với actual execution và scheduled trigger.
- [ ] Tôi giải thích được vì sao scope dialog chữa ambiguity, force không chữa business oracle.
- [ ] Tôi giữ fact/hypothesis/next discriminating check riêng.
- [ ] Tôi dừng ghi khi unknown write và có exact ownership + recovery owner.
- [ ] Tôi không xóa flaky history, suppressed failure hoặc pending cleanup khỏi report.

Trả lời phỏng vấn theo evidence → layer → safe action → validation. Luyện [6 câu hỏi](../03_interview/ci-recovery.md), [quiz](../04_quiz/ci-recovery.md) và [lab](../05_practice/project-evidence-lab.md).

## Nguồn local chính xác

[AOCE content](<../../document/AIQE Agent Optimization & CI Execution/L3_AIQE_AOCE_course_content_vi.md>): “U3.2–U3.3”, “U4.1–U4.3”, “U5.1–U5.4”, “U6.1–U6.3”. [AOCE handout](<../../document/AIQE Agent Optimization & CI Execution/L3_AIQE_AOCE_exercises_vi.md>): “CI-PACKET-05”, “INCIDENT-PACKET-06”, “RET-PACKET-06”, “GIT-PACKET-04”. [U5 design](<../../document/AIQE Agent Optimization & CI Execution/NhiTY14/submissions/U5/U5_ci-design.md>): “Script Contracts”; [workflow draft](<../../document/AIQE Agent Optimization & CI Execution/NhiTY14/submissions/U5/U5_workflow.yml>): preflight/reconcile/upload steps; [config draft](<../../document/AIQE Agent Optimization & CI Execution/NhiTY14/submissions/U5/U5_playwright-config.ts>): trace/reporters/outputDir; [U6 recovery](<../../document/AIQE Agent Optimization & CI Execution/NhiTY14/submissions/U6/U6_recovery-and-validation.md>): “INC-61”, “INC-63”, “Validation Plan Before/After Fix”. [Starter README](<../../document/AIQE Agent Optimization & CI Execution/Agent CI/README.md>): “Setup”; [login spec](<../../document/AIQE Agent Optimization & CI Execution/Agent CI/tests/specs/login.spec.ts>): test.skip. [PBAAD content](<../../document/AIQE Project-Based AI Agent Development/L4_AIQE_PBAAD_course_content_vi.md>): “U4.2 Retry, reconcile và safe termination”. Ledger đầy đủ: [tracking](../00_tracking/optimization-project-notes.md).
