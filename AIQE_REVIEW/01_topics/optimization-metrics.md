# Tối ưu agent bằng quality gate và metrics có mẫu số

Tài liệu ôn tập tự biên soạn từ AOCE U1–U3/U7; ví dụ đều là **SIMULATED**. Đây không phải đáp án hay thang điểm chính thức.

## Mục tiêu và đầu vào

Sau bài này, bạn tính được chi phí có cached tokens, chọn cấu hình không làm mất oracle, lập context manifest và giải thích một dashboard có blocked/flaky/missing usage. Cần hiểu [oracle và flow execution](ci-recovery.md) và biết đọc một bảng dữ liệu. Học tiếp [quality gate project](project-quality-gates.md) để biến số đo thành quyết định bàn giao.

**Bắt buộc:** quality trước cost; source/version; không điền missing=0; mẫu số và cohort rõ; không bỏ failed samples. **Nên có:** blind review, ledger kiểm tra lại bằng bảng tính, median/range. **Mở rộng:** actual provider benchmark và telemetry dashboard chỉ khi có quyền, rate/version và môi trường phù hợp.

## Từ khóa cần giải thích được

| Từ khóa | Định nghĩa bằng câu đầy đủ |
|---|---|
| Baseline | Baseline là cấu hình và tập đầu vào được cố định để mọi thay đổi có mốc so sánh có thể tái hiện. |
| Quality gate | Quality gate là điều kiện chấp nhận bắt buộc; điểm cao hoặc giá rẻ không bù việc mất oracle hay sai quyền. |
| Token usage | Token usage là số liệu sử dụng do công cụ/provider trả theo schema; độ dài văn bản chỉ có thể là ước lượng riêng. |
| Cached input | Cached input là phần input được provider phân loại theo cơ chế cache và phải tính theo rate tương ứng, tránh cộng hai lần. |
| Measured subtotal | Measured subtotal là tổng các khoản đã đo được trong scope; nó chưa phải total khi còn thành phần thiếu. |
| Cohort | Cohort là tập case/run có window, build và cấu hình xác định dùng chung trong một phép tính. |
| Logical case và attempt | Logical case là một lần thực thi case cùng tham số đã chọn; attempt là mỗi lần thử case đó, kể cả retry. |
| Prompt drift | Prompt drift là sự lệch hành vi khỏi contract sau thay prompt/context, ví dụ đổi exact ID + department thành “verify success”. |
| Context manifest | Context manifest là danh mục nguồn/version/run/time được dùng hoặc loại bỏ, giúp giải thích quyết định nén context. |
| Observability | Observability là khả năng dùng logs, metrics và traces liên kết để biết hệ thống đã làm gì và cần điều tra gì. |
| Risk register | Risk register là sổ nguyên nhân → sự kiện → tác động kèm control, detection, owner và bằng chứng đóng rủi ro. |

## Đo cái gì, vì sao và khi nào?

Tối ưu không phải cắt càng nhiều token càng tốt. QA cần report giữ được source, đúng dữ liệu và quyền thao tác. Trong `OUTPUT-PACKET-01`, B dùng ít token nhưng bỏ department, lấy toast thay runner và đề nghị xóa “old employees”. B bị loại trước khi so giá. A có ba output qua gate; C có hai, vì C3 dẫn evidence run trước. **Accepted=5/9**, không phải 7/9 như một dòng trong bài nộp U1.

Input → process → output: nhận task cố định + source/oracle + usage + rates → chấm quality trước khi nhìn giá, kiểm tra dữ liệu thiếu, tính chi phí cùng units → ledger và recommendation có điều kiện. Ba lớp đo phải tách nhau: model tokens/calls; execution setup/tool/CI/retry/cleanup; QA correctness/review time. Context window là sức chứa, khác billed usage; test duration khác end-to-end; phút reviewer không tự thành tiền nếu chưa có internal rate.

Protocol tối thiểu: đóng băng task/dataset/schema/rubric/model/tool fixtures; đổi một yếu tố nếu muốn kết luận nhân quả; giữ cả output lỗi; lặp và báo cỡ mẫu; so cùng cold/warm conditions. Packet A/B/C thay cả context và prompt nên chỉ so **gói cấu hình**, chưa quy lợi ích riêng cho context. Ba sample/config phục vụ học tập, chưa chứng minh reliability production.

## Chi phí với đơn vị và unknown

Trong handout `RATE-SYN-01`, rate là **đơn vị giả lập/triệu tokens**, không USD: input uncached=1; cached=0,25; output=4; CI=0,02/phút. Packet xác nhận input_total gồm cached:

```text
uncached = input_total - cached
model = (uncached × 1 + cached × 0,25 + output × 4) / 1_000_000
measured = model + CI_minutes × 0,02 + tools + storage
cost / accepted = mọi measured cost trong cohort / số output qua gate
```

Ví dụ A1: total input 18.000, cached 2.000, output 2.400, CI 4 phút → uncached 16.000; model=0,02610; CI=0,08000; tổng=0,10610. Không cộng thêm phí model/tool calls vì packet đã tổng hợp và không định nghĩa charge riêng. Nếu provider khác, phải đọc lại cached accounting; công thức trừ cache này không phải quy tắc cho mọi API.

Tính lại toàn benchmark theo handout: A=0,325175, B=0,237005; C1+C2=0,176075; C3 CI-only=0,078 và model UNKNOWN. A/accepted=0,1083917; B/accepted=N/A vì accepted=0; toàn C có lower bound 0,254075/2=0,1270375 và total chưa biết. So C chỉ trên hai sample đủ usage rồi tuyên bố rẻ nhất sẽ loại mất chi phí C3. Bài nộp U1/CSV dùng cached rate=0 và USD minh họa: không chép con số đó như kết quả của RATE-SYN-01 hiện tại.

## Nén context mà không nén mất ý nghĩa

Input gồm requirement, policy, DOM hiện tại, dòng run trước, debug chatter và webpage injection → phân loại instruction/current observation/stale/noise/untrusted → compact context + source manifest + regression matrix. Giữ goal hẹp, flow/actor/env, exact oracle, owned IDs, current state, stop/budget, matching runner pointer; bỏ DOM không liên quan, không mượn state run cũ. Hash giúp truy nguồn nhưng không chứng minh source đúng hoặc mới.

Ví dụ CTX-08 nói runner chưa có result, nên dù CTX-04 có row đúng ID/QA, trạng thái vẫn pending. Cắt câu “chỉ cleanup owned ID” thành “clean old employees” đã đổi quyền. Nội dung webpage yêu cầu bulk delete là dữ liệu không đáng tin; controller phải chặn call ngoài quyền bằng code. Nén ≤250 từ trong lab là word budget, không phải 250 tokens. Sau edit, chạy/thiết kế RG-01…08, đặc biệt wrong department, stale evidence, unknown write và forbidden flow; lưu rollback/refresh rule khi build/source đổi.

## Đọc dashboard từ METRIC-PACKET-07

| Metric | Phép tính đúng trong packet | Điều quyết định |
|---|---|---|
| Execution completeness | 8/10=80% | E06 blocked, E07 skipped vẫn hiện trong selected. |
| First-pass | 4/8=50% | Không bị eventual-pass che khuất. |
| Eventual-pass | 6/8=75% | Có hai case vẫn failed. |
| Flaky proportion | 2/8=25% | Pass sau retry chưa phải root cause fixed. |
| Retry overhead | 11 attempts−8 cases=3 | Bao gồm retry của E04 failed cuối. |
| Evidence completeness | 7/8=87,5% | E05 partial; E04/E09 fail vẫn có full evidence. |
| Cleanup completion | 4/6≈66,7% | E04 failed, E08 unknown nằm trong mẫu số cần cleanup. |
| Evidence-complete passes | 5 | E01/E02/E03/E08/E10; khác full-evidence count 7. |
| Cost/evidence-complete pass | 0,89/5=0,178 lower bound | Giữ cả chi phí failed, blocked và partial case trong tử số. |
| Scheduling completeness | 3/4=75% | SL-04 chưa dispatch; không tự tạo thêm execution row. |

Measured subtotal 0,89 chưa cho biết total nhỏ hơn budget 1,20. Nếu các khoản chưa biết không âm, remaining budget **không lớn hơn 0,31**, không phải “ít nhất 0,31”. Evidence completeness chỉ đánh giá linkage/existence theo rubric, chưa chứng minh nội dung đúng. Requirement mapping 4/4 là design mapping, khác backend security; thiếu baseline backend thì ghi chưa kiểm chứng, không tự xuất 0% có vẻ chính xác.

Dispatch delays 3/0/2 phút có median 2, range 0–3 (n=3); queue delays 2/8/1 median 2, range 1–8. Test duration n=8 có median 82,5s, range 40–170, không gồm queue/setup/cleanup. Không suy percentile hay SLO khi nguồn chưa quy định.

## Phỏng vấn, bẫy và tự kiểm tra

Khi được hỏi “giảm 60% token có tốt không?”, trả lời theo quality gate → protocol → cost đủ scope → limitations → pilot/next evidence. Đừng chỉ kể công cụ. Risk khác issue: “unknown write có thể gây duplicate” là risk; “E04 cleanup failed trong packet” là issue giả lập. Risk closure cần control retest và owner; việc AI đã viết patch chưa đóng rủi ro.

- [ ] Tôi tính được A1 và giải thích vì sao không double-count cached.
- [ ] Tôi phân biệt 7 full-evidence cases với 5 evidence-complete passes.
- [ ] Tôi không bỏ failed costs hoặc biến missing usage thành 0.
- [ ] Tôi giữ exact ID/department/ownership khi nén context và biết fixture phát hiện drift.
- [ ] Recommendation của tôi nêu mode, cohort, owner và next evidence.

Luyện [phỏng vấn](../03_interview/optimization-metrics.md), [trắc nghiệm](../04_quiz/optimization-metrics.md), [lab](../05_practice/project-evidence-lab.md).

## Nguồn đối chiếu chính xác

Đường dẫn tính từ file này; headings sau link là vị trí đọc. [AOCE content](<../../document/AIQE Agent Optimization & CI Execution/L3_AIQE_AOCE_course_content_vi.md>): “U1.1–U1.3”, “U2.1–U2.3”, “U3.1”, “U7.1–U7.4”. [AOCE handout](<../../document/AIQE Agent Optimization & CI Execution/L3_AIQE_AOCE_exercises_vi.md>): “BENCH-PACKET-01”, “OUTPUT-PACKET-01”, “CONTEXT-PACKET-02”, “REG-PACKET-02”, “METRIC-PACKET-07”. [U1 benchmark](<../../document/AIQE Agent Optimization & CI Execution/NhiTY14/submissions/U1/U1_benchmark.md>): “Chấm output cards”, “Giả định minh họa cho cost”. [U7 metrics](<../../document/AIQE Agent Optimization & CI Execution/NhiTY14/submissions/U7/U7_metrics-and-claims.md>): “1.4 Evidence Completeness”, “Evidence-complete-pass cost”; các chỗ lệch được sửa trong phép tính ôn tập, không sửa nguồn. [U7 sprint memo](<../../document/AIQE Agent Optimization & CI Execution/NhiTY14/submissions/U7/U7_sprint-review.md>): “3.4 Cost”. Danh mục mọi bài nộp và ledger đọc nằm ở [tracking](../00_tracking/optimization-project-notes.md).
