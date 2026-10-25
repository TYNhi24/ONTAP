# Phân tích yêu cầu và thiết kế kiểm thử có AI hỗ trợ

## Mục tiêu và mức độ cần học

Sau chủ đề này, fresher cần biến một yêu cầu mơ hồ thành câu hỏi làm rõ, dựng chuỗi truy vết tới bài kiểm thử có oracle rõ ràng, và giải thích vì sao chọn kiểm thử một rủi ro trước rủi ro khác. **Bắt buộc:** phân tích yêu cầu, oracle, kỹ thuật thiết kế, truy vết, ca chi tiết và rủi ro còn lại. **Nên biết:** quản lý phiên khám phá và đánh giá khả năng tự động hóa. **Mở rộng trong khóa:** pairwise, metamorphic relation, tích hợp kiểm tra truy vết vào CI; chưa cần tự xây công cụ.

Đây là bản diễn giải phục vụ fresher từ khóa ARTD vốn ghi trình độ Advanced; không phải đề thi chính thức. Nội dung và ví dụ tự biên dựa trên nguồn khóa học; không có kiến thức bổ sung từ web. Tiên quyết: đọc user story, HTTP/JSON và kỹ thuật kiểm thử cơ bản; dữ liệu an toàn được học tiếp ở [chủ đề dữ liệu](test-data-privacy.md), điều tra kết quả ở [defect/API/log](defect-api-log-analysis.md).

## Từ khóa cần hiểu bằng câu hoàn chỉnh

| Từ khóa | Định nghĩa và cách dùng |
|---|---|
| Requirement | Requirement là phát biểu về nhu cầu, hành vi hoặc ràng buộc cần đáp ứng; nó chỉ dùng làm chuẩn kiểm thử khi nguồn và trạng thái phê duyệt rõ ràng. |
| Acceptance criterion | Acceptance criterion là điều kiện quan sát được để đánh giá một hành vi có đáp ứng mong đợi hay không. |
| Business rule | Business rule là quy tắc nghiệp vụ chi phối kết quả, ví dụ chỉ áp dụng một mức giảm giá hợp lệ cao nhất. |
| Testability | Testability là mức có thể kiểm chứng yêu cầu qua điều kiện kiểm soát được và kết quả quan sát, đo lường được. |
| Test oracle | Test oracle là nguồn hoặc quy tắc giúp quyết định kết quả thực tế đúng hay sai; câu trả lời AI chưa được xác minh không phải oracle sản phẩm. |
| Ambiguity | Ambiguity là việc một câu có nhiều cách hiểu hợp lý, chẳng hạn “hoàn thành nhanh” không xác định ngưỡng hay tải. |
| Traceability | Traceability là khả năng lần theo liên hệ giữa yêu cầu, rủi ro, kịch bản, ca hoặc charter, dữ liệu và bằng chứng thực thi. |
| Test condition/scenario/case | Test condition nêu điều cần kiểm tra; scenario diễn tả một tình huống hoặc luồng; case cụ thể hóa tiền điều kiện, dữ liệu, bước, oracle và cleanup để thực thi. |
| Equivalence partitioning | Phân lớp tương đương chia miền input thành các nhóm được kỳ vọng xử lý tương tự, rồi chọn đại diện có chủ đích. |
| Boundary value analysis | Phân tích giá trị biên chọn giá trị ở và sát ranh giới vì lỗi thường xuất hiện khi so sánh hoặc giới hạn bị sai. |
| Decision table | Bảng quyết định ánh xạ tổ hợp điều kiện tới hành động hoặc kết quả, giúp phát hiện tổ hợp bỏ sót và mâu thuẫn. |
| State transition | Kiểm thử chuyển trạng thái đánh giá hành vi theo trạng thái trước đó và sự kiện, gồm chuyển hợp lệ lẫn chuyển bị cấm. |
| Residual risk | Rủi ro còn lại là khả năng và tác động chưa được giải quyết sau phạm vi kiểm thử đã chọn; cần có người chịu trách nhiệm và điều kiện xem lại. |
| Exploratory charter | Charter là nhiệm vụ khám phá có mục tiêu, tài nguyên, rủi ro và timebox; nó cho phép học và điều chỉnh đường đi trong phiên. |

## 1. Từ yêu cầu mơ hồ tới baseline có thể kiểm thử

**Input:** nguồn có ID/phiên bản, glossary, business rule, contract, phạm vi. **Xử lý:** tự phân rã trước thành actor, trigger, precondition, action, rule, data, result, exception và evidence; dùng AI tìm thêm khoảng trống; con người quyết định. **Output:** bảng phân rã, clarification register, đề xuất acceptance criteria, assumption log và quyết định review.

Đọc câu “Checkout phải nhanh” không được sửa ngay thành “dưới 2 giây”. Cần hỏi người sở hữu NFR: đo từ thao tác nào tới sự kiện nào, percentile nào, tải bao nhiêu, môi trường nào, time window nào và chấp nhận sai số ra sao? Dạng đề xuất phù hợp là “Trong [tải cần phê duyệt], [percentile cần phê duyệt] thời gian từ [đầu] đến [cuối] không vượt [ngưỡng cần phê duyệt]”. Các dấu ngoặc là quyết định còn thiếu, chưa phải yêu cầu chính thức.

Kiểm tra bảy tiêu chí: cụ thể, quan sát được, kiểm soát được, đo lường được, nhất quán, khả thi, truy vết được. Given/When/Then giúp cấu trúc câu nhưng không chữa được oracle bị bịa. Ví dụ “Then discount đúng” vẫn không thể đánh giá.

Tách **fact** có nguồn, **inference/risk** suy ra từ nguồn, **assumption** tạm dùng có owner, **question** thiếu quyết định và **suggestion** cải thiện đề xuất. Trong ARTD, API mô tả `201 CREATED/PENDING_PAYMENT`, còn process note nói chỉ tạo order sau thanh toán thành công. Ghi hai nguồn, tác động tới state/setup/oracle, rồi chuyển owner làm rõ. Không tự chọn một nguồn theo thói quen.

## 2. Truy vết thật và phân tích ảnh hưởng thay đổi

Chuỗi tối thiểu là `requirement + risk → scenario → case/charter → dataset → execution evidence → defect`. Một yêu cầu có thể cần nhiều ca; một ca có thể hỗ trợ nhiều yêu cầu nhưng từng liên kết cần lý do riêng. Lưu ID ổn định, phiên bản, reviewer và lý do hạ mức liên kết AI đề xuất.

| Trạng thái coverage trong ARTD | Cách hiểu thực tế |
|---|---|
| Full | Tất cả điều kiện đã phát biểu trong phạm vi liên kết được kiểm tra trực tiếp bằng oracle quan sát được. |
| Partial | Chỉ một phần hành vi hoặc ngưỡng được kiểm tra. |
| Indirect | Chỉ có bằng chứng gián tiếp từ kiểm tra khác hoặc tầng thấp hơn. |
| None | Chưa có liên kết kiểm chứng hợp lệ. |
| Blocked/Not testable | Chưa có quyết định nghiệp vụ hoặc năng lực môi trường cần thiết. |

`TC-LEG-07` “Customer opens order details” không chứng minh khách A không đọc được order B. Nó thiếu actor/object đối nghịch và oracle không lộ dữ liệu. `TC-LEG-08` cash on delivery không thuộc `CARD/WALLET` hiện được phê duyệt; đánh dấu lỗi thời hoặc yêu cầu nguồn mới, không giữ để tăng số lượng ca. Một test chưa chạy có thể đủ thiết kế cho một điều kiện, nhưng không tạo bằng chứng rằng điều kiện đã pass. Luôn tách coverage thiết kế và coverage thực thi.

Với `CR-01` hoàn tiền theo dòng/số lượng, kiểm tra cả UI, API, dữ liệu, authorization, phép tính cộng dồn, phân bổ giảm giá, trạng thái, payment, audit, notification và regression. Câu hỏi còn mở gồm ngưỡng phê duyệt cộng dồn, hoàn lặp, rounding, shipping allocation và concurrency. Mở ticket làm rõ, không dùng AI lấp bằng quy tắc tưởng tượng.

## 3. Sinh kịch bản bằng kỹ thuật và chọn theo rủi ro

**Input:** baseline, rule, contract, lịch sử lỗi, kiến trúc và giới hạn thời gian. **Xử lý:** dựng mô hình thủ công, suy ra kịch bản, nhờ AI phản biện các góc bỏ sót, gộp trùng theo ý nghĩa, xếp hạng có bằng chứng. **Output:** portfolio có nguồn/kỹ thuật/oracle/priority, tập smoke/regression/exploratory và phần hoãn có residual risk.

Ví dụ theo `BR-DIS-01`:

| VIP | Campaign hợp lệ | Mức áp dụng |
|---|---|---|
| Không | Không | Không giảm từ hai quy tắc này. |
| Có | Không | 10%. |
| Không | Có | 15%. |
| Có | Có | 15%, không cộng thành 25%. |

Tổng trước giảm VND 240.000 với VIP và campaign hợp lệ cho giảm VND 36.000, còn VND 204.000; rounding half-up theo đơn vị tiền nhỏ nhất do nguồn quy định. Đây là phép tính ví dụ tự biên, không phải kết quả hệ thống đã thực thi. Quantity `1..10` cần lớp dưới miền, hợp lệ và trên miền; tập sát biên điển hình là `0,1,2,9,10,11`. Decision table phù hợp tổ hợp discount; state transition phù hợp pending/payment/retry; boundary phù hợp số lượng. Pairwise giúp giảm tổ hợp cấu hình nhưng không bảo đảm bắt lỗi cần ba yếu tố hoặc nhiều yếu tố cùng tương tác.

Trong bài `EX-U3-SCENARIO`, chấm L/I/E từ 1–5 có lý do và tính `L × I × E`; số lớn chỉ hỗ trợ xếp hạng, không chứng minh xác suất thống kê. Slide 16 minh họa giản lược `L × I`; khi làm bài tập dùng công thức rubric đã chỉ định, không trộn thang điểm. Bằng chứng `RISK-01` 65% đơn hoàn tất từ mobile và `RISK-02` incident thu trùng thúc đẩy kiểm tra mobile timeout/idempotency sớm. Không bỏ authorization hoặc privacy chỉ vì điểm trung bình thấp.

## 4. Từ scenario tới case thực thi được

Một case cần ID/objective, nguồn, scope, priority, environment, precondition, dataset, action, checkpoint, observation layer, cleanup và khả năng rerun. Sửa một case đầu tiên trước khi nhân thành cả họ. Kiểm tra expected ở UI chưa đủ cho lỗi side effect: cần API, log, audit hoặc provider stub phù hợp.

**Ví dụ fresher tự biên: `TC-DIS-01`, VIP + campaign.** Nguồn `BR-DIS-01`; dùng customer synthetic đang active, SKU in-stock, order subtotal VND 240.000, campaign hợp lệ, payment stub an toàn. Bước 1 mở checkout với dataset riêng và xác nhận subtotal. Bước 2 áp mã và kiểm tra discount VND 36.000, total VND 204.000 tại UI và API theo interface được phê duyệt. Bước 3 nếu scope có đặt đơn, kiểm tra dữ liệu discount/audit tương ứng theo `BR-AUD-01`; chưa giải quyết mâu thuẫn trạng thái order thì không tự đặt expected trạng thái. Cleanup chỉ reset dữ liệu mang nhãn lượt chạy trong staging, không “xóa order” chung chung và mất bằng chứng. Expected đủ cụ thể để người khác quan sát, dữ liệu và cleanup đủ rõ để chạy độc lập.

Automation readiness có ba mức trong bài: `Now`, `Later`, `Not recommended`, xét giá trị, lặp lại, ổn định, oracle, setup và chi phí bảo trì. Việc AI sinh được script không làm oracle trở nên đúng.

## 5. Khám phá có cấu trúc

Scripted case quy định đường đi và checkpoint để lặp lại; charter chỉ định mục tiêu học và rủi ro để tester thích nghi. Checklist nhắc một nhóm quan tâm thường gặp; nó không phải bằng chứng completeness.

Charter ví dụ tự biên: “Trong 45 phút, khám phá mobile checkout khi mất mạng ngay sau submit bằng hai tài khoản synthetic, payment stub và API/log để tìm bất nhất trạng thái và rủi ro thu trùng; không thử production hoặc thanh toán thật.” Ghi timestamp, thao tác, quan sát, câu hỏi, bug, blocker và ý tưởng tiếp. Nếu gặp một trạng thái chưa rõ, lưu bằng chứng, kiểm tra oracle và giải thích quyết định pivot hoặc ở lại nhiệm vụ. Debrief nói đã thử gì, học gì, chưa biết gì và charter tiếp theo; nếu chỉ tabletop phải ghi simulated.

## Bẫy và điểm phỏng vấn

- “100% requirement có link” không chứng minh mọi role, negative flow, state hay NFR đã được kiểm tra.
- “Có 200 ca” không mạnh bằng vài ca có nguồn, oracle và rủi ro rõ; gộp trùng không được làm mất biến thể quan trọng.
- “AI đã xác nhận” không thay cho source và reviewer; ghi accept/edit/reject/escalate có lý do.
- Không dùng snapshot toàn body như oracle mặc định nếu timestamp/ID thay đổi; chọn trường và quan hệ cần kiểm chứng.
- Đề cập công khai phần hoãn, môi trường không hỗ trợ và câu hỏi chưa chốt khi bảo vệ quyết định release.

## Tự kiểm tra

- [ ] Tôi tìm ra actor, trigger, rule, exception và outcome, ghi thiếu thành câu hỏi.
- [ ] Tôi phân biệt fact/assumption/risk/suggestion và không tự đặt ngưỡng.
- [ ] Tôi giải thích từng link Full/Partial bằng hành vi và oracle.
- [ ] Tôi dựng đúng bảng discount, boundary và ít nhất một chuyển trạng thái.
- [ ] Tôi giải thích ưu tiên bằng evidence, budget và residual risk.
- [ ] Case của tôi chạy độc lập, có dữ liệu an toàn, checkpoint và cleanup.
- [ ] Charter cho phép thích nghi; ghi chú giữ nguyên độ bất định.

## Nguồn và luyện tập

Nguồn chính: [ARTD course](../../document/AIQE%20AI-Assisted%20Requirement%20%26%20Test%20Design/L3_AIQE_ARTD_course_content.md), các mục `4. Suggested running case study`, `5. Responsible AI working agreement`, Unit 1–5 (Sessions 1.1–5.4), `6. Assessment strategy`, `7. Recommended reusable AI workflow`. Đối chiếu bài tập [ARTD exercises DOCX](../../document/AIQE%20AI-Assisted%20Requirement%20%26%20Test%20Design/L3_AIQE_ARTD_exercises.docx), các heading `EX-U1-RQA`, `EX-U2-TRACE`, `EX-U3-SCENARIO`, `EX-U4-CASES`, `EX-U5-EXPLORE` và capstone.

Slide và speaker notes đã đọc dạng XML text: [deck EN](../../document/AIQE%20AI-Assisted%20Requirement%20%26%20Test%20Design/L3_AIQE_ARTD_training_deck_ready_v2.pptx), [deck VI](../../document/AIQE%20AI-Assisted%20Requirement%20%26%20Test%20Design/L3_AIQE_ARTD_training_deck_vi_final.pptx), slide 6–21 và notes cùng số. Chưa kiểm chứng bố cục slide/chart bằng bản render PowerPoint; hình ảnh nhúng được người điều phối xem riêng, không làm oracle sản phẩm.

Luyện [phỏng vấn](../03_interview/requirement-test-design.md), [trắc nghiệm](../04_quiz/requirement-test-design.md), rồi xem [giải thích đáp án](../04_quiz/requirement-test-design-answers.md).
