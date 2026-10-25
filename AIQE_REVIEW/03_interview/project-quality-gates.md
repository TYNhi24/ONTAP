# Phỏng vấn — project-quality-gates

Câu hỏi tự biên soạn, không phải đề chính thức. Dùng [bài học](../01_topics/project-quality-gates.md) làm nguồn; luyện trả lời mỗi câu 30–60 giây bằng lời của mình.

## Câu 1. Biến “làm agent tự test employee” thành backlog thế nào?

**Ý đồ:** Kiểm tra scope và AC testable.

**Gợi ý trả lời 30–60 giây:** Tôi hỏi quyết định QA lead cần hỗ trợ rồi chốt F01/F02, environment và source baseline. Charter có in/out/unknowns, backlog item có precondition/action/oracle/evidence, dependency, owner và estimate. Ví dụ report phải dẫn assertion ID/department cùng run; thiếu evidence không pass. Dashboard/CI là stretch, production/bulk delete bị reject theo contract. Readiness thiếu có owner; không đánh done khi runtime bắt buộc còn pending.

**Hỏi tiếp:** Task khác AC ra sao? **Điểm cần trả lời:** Implement reporter là task; report thiếu matching evidence không pass là AC.

**Lỗi thường gặp:** Ghi agent thông minh hoặc code done làm tiêu chí nghiệm thu.

## Câu 2. Ai quyết định flow, tool và verdict?

**Ý đồ:** Kiểm tra trust boundaries.

**Gợi ý trả lời 30–60 giây:** Planner chỉ đề xuất. Schema và semantic validation kiểm tra flow/env/source/refs; controller chọn runner đã duyệt trong catalog. Adapter giới hạn quyền độc lập để direct bypass cũng bị chặn. Runner giữ oracle; report verifier đối chiếu provenance; con người chốt sharing/gate theo policy. Model text hoặc planApproved không mở quyền, raw command không phải approved flow. Tradeoff là thêm flow cần catalog/test/review, nhưng dễ kiểm soát và tái hiện.

**Hỏi tiếp:** JSON đúng kiểu nhưng source cũ? **Điểm cần trả lời:** Semantic reject trước execution.

**Lỗi thường gặp:** Cho model tự chấm pass hoặc cho adapter tin planApproved=true.

## Câu 3. F02 của hai module có giống nhau không?

**Ý đồ:** Kiểm tra source/version và không học thuộc flow number.

**Gợi ý trả lời 30–60 giây:** Không. AOCE F02 là đổi department của owned seed rồi search ID/department mới. PBAAD F02 là duplicate-id: seed độc lập, thử tạo trùng, kiểm tra rejection, exact-ID count vẫn một và department không đổi. Tôi luôn ghi module/sourceVersion cùng flowId và oracle refs; không dùng record F01 làm dependency của F02. Helper chưa được cấp thì giữ execution pending, không invent endpoint.

**Hỏi tiếp:** Toast duplicate có đủ không? **Điểm cần trả lời:** Chưa; còn count và original department theo LAB-PBAAD-02.

**Lỗi thường gặp:** Dùng assertion Engineering của AOCE cho PBAAD duplicate flow.

## Câu 4. Bộ test mẫu 8/8 pass cho phép nói gì?

**Ý đồ:** Kiểm tra phạm vi evidence và review test.

**Gợi ý trả lời 30–60 giây:** Nó chứng minh tám local test assertions trong working tree đã pass khi chạy node --test, không chứng minh PortalLite/UI/model thật. Scripted planner và runner in-memory giữ SIMULATED. Test verdict nhận passed:false chưa kiểm tra checker phát hiện record sai department; test prose có runner pass nên chưa kiểm tra prose override assertion fail; chưa có stale-evidence verifier hay call recorder. Tôi giữ manifest HOLD và ưu tiên gaps local trước tích hợp.

**Hỏi tiếp:** Có thể sửa gì khi lab chưa cấp? **Điểm cần trả lời:** Schema/provenance verifier, fake-clock fault tests, negative controls và recorder.

**Lỗi thường gặp:** Đổ toàn bộ missing controls cho thiếu lab hoặc coi 8/8 là project hoàn tất.

## Câu 5. Quality gate cần bằng chứng gì ngoài happy path?

**Ý đồ:** Kiểm tra security/privacy/maintainability.

**Gợi ý trả lời 30–60 giây:** Tôi cần denial tests gồm direct adapter bypass, unknown-write/budget/cancellation evidence, wrong-department và stale-run negative controls, canary/redaction và artifact sharing policy. Peer reproduce frozen revision theo README và lưu actual results. Findings phải có owner, fix và retest revision; missing required evidence giữ HOLD. Business pass, cleanup outcome và release decision là các trường riêng. Conditional demo chỉ trình bày tiến độ đúng mode, chưa release ready.

**Hỏi tiếp:** Cleanup unknown nhưng functional pass? **Điểm cần trả lời:** Giữ test pass đúng scope, cleanup unknown và release HOLD.

**Lỗi thường gặp:** Tích hết checklist hoặc lấy điểm tổng bù blocking finding.

## Câu 6. Demo và retrospective trung thực như thế nào?

**Ý đồ:** Kiểm tra handoff và khả năng bảo vệ claim.

**Gợi ý trả lời 30–60 giây:** Tôi mở đầu mode live/recording/simulator và scripted/model, freeze revision/source/config và dẫn run/attempt evidence. Demo có core và safe-stop case; fallback ghi timestamp chứ không giả current live. Manifest chứa gate/known issues/pending data/recovery owner/reproduction. Mỗi người giải thích một change, review decision, assertion, failure path. Retro lấy ít nhất ba sự kiện có evidence rồi action cụ thể với owner/date/success indicator, không biến kế hoạch thành việc đã làm.

**Hỏi tiếp:** Chưa đo cost thì nói savings sao? **Điểm cần trả lời:** Giữ unknown; không bịa token/productivity savings.

**Lỗi thường gặp:** Giấu manual intervention, kể planned retro như actual events.

Tự chấm: nêu đúng nguồn/mode, dùng một ví dụ, giữ unknown, chỉ rõ bằng chứng và next action. Không học thuộc câu trả lời thành lời xác nhận mình đã thực hiện.
