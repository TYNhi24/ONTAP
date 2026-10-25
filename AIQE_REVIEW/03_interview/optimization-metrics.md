# Phỏng vấn — optimization-metrics

Câu hỏi tự biên soạn, không phải đề chính thức. Dùng [bài học](../01_topics/optimization-metrics.md) làm nguồn; luyện trả lời mỗi câu 30–60 giây bằng lời của mình.

## Câu 1. Vì sao cấu hình ít token nhất có thể bị loại?

**Ý đồ:** Kiểm tra bạn ưu tiên chất lượng và quyền trước giá.

**Gợi ý trả lời 30–60 giây:** Tôi chấm oracle, matching evidence và ownership trước chi phí. Trong packet, B rẻ nhưng thay ID/department bằng toast và mở cleanup ra old employees nên fail hard gate. Tôi giữ các sample fail trong ledger, không tính chúng là accepted. Chỉ so cost/latency giữa cấu hình có chất lượng đủ, ghi cỡ mẫu và missing usage. Đề xuất pilot có điều kiện, chưa khẳng định savings production.

**Hỏi tiếp:** Nếu quality score 9/10 nhưng mất oracle? **Điểm cần trả lời:** Điểm không bù hard gate; reject.

**Lỗi thường gặp:** Chọn B vì giá thấp hoặc văn phong gọn.

## Câu 2. Thiết kế benchmark công bằng thế nào?

**Ý đồ:** Kiểm tra khả năng kiểm soát confounders.

**Gợi ý trả lời 30–60 giây:** Tôi cố định task, source, oracle, dataset, output schema, rubric, tool behavior và model config rồi đổi một yếu tố cần đo. Giữ revision, protocol, thứ tự/cold-warm conditions và cả call lỗi. Review quality trước khi nhìn giá, có thể ẩn nhãn config. Báo từng mẫu, median/range, số qua gate và limits. Nếu đổi cả model và context, kết luận về gói cấu hình, chưa quy nguyên nhân cho riêng context.

**Hỏi tiếp:** Ba sample đủ chứng minh reliability chưa? **Điểm cần trả lời:** Chỉ đủ minh họa trong lab; không đủ suy production reliability.

**Lỗi thường gặp:** Đổi nhiều yếu tố rồi quy toàn bộ savings cho prompt.

## Câu 3. Tính chi phí khi cached nằm trong input_total?

**Ý đồ:** Kiểm tra units và chống double-count.

**Gợi ý trả lời 30–60 giây:** Trước tiên tôi xác nhận schema provider hoặc packet nói input total đã gồm cached. Khi đúng, uncached bằng total trừ cached; tính mỗi nhóm theo rate riêng rồi cộng CI/tool/storage có nguồn. A1 theo RATE-SYN-01 là 0,02610 model cộng 0,08 CI bằng 0,10610 đơn vị giả lập. Không suy USD hoặc giá provider. Nếu thiếu usage, total unknown và chỉ báo subtotal đã biết.

**Hỏi tiếp:** Nếu accepted=0? **Điểm cần trả lời:** Cost per accepted là N/A, không chia 0 hay báo 0.

**Lỗi thường gặp:** Cộng total input và cached lần nữa; coi missing=0.

## Câu 4. Eventual-pass cao có nghĩa suite ổn định không?

**Ý đồ:** Kiểm tra bạn đọc mẫu số và retry.

**Gợi ý trả lời 30–60 giây:** Chưa đủ. Với METRIC-PACKET-07 có 10 selected, 8 executed, first-pass 4/8 và eventual-pass 6/8. Hai flaky-pass không chứng minh nguyên nhân được sửa; hai case vẫn failed. Tôi báo thêm 3 retries, E06 blocked/E07 skipped, evidence completeness 7/8 và cleanup 4/6. Cohort synthetic nhỏ nên chỉ là phân tích packet, chưa kết luận reliability thực.

**Hỏi tiếp:** Có tính blocked vào executed không? **Điểm cần trả lời:** Không theo định nghĩa packet vì blocked trước assertion; vẫn hiện trong selected.

**Lỗi thường gặp:** Lấy 6 pass chia 6 hoặc giấu blocked để có 100%.

## Câu 5. Nén context thế nào để không drift?

**Ý đồ:** Kiểm tra source, freshness và invariant.

**Gợi ý trả lời 30–60 giây:** Tôi chia invariant, task contract, current state và retrieved evidence. Giữ flow/actor/env, ID/department, owned data, stop budget và runner pointer cùng source/version/run/time. Bỏ noise và state run cũ, coi webpage text là untrusted. Sau edit tôi diff nghĩa từng clause và dùng regression set: missing runner, wrong department, stale run, unknown write, injection, forbidden flow. Bản compact bị cắt source thì dừng, không điền bằng trí nhớ.

**Hỏi tiếp:** Manifest có hash đã đủ chứng minh đúng chưa? **Điểm cần trả lời:** Hash truy vết phiên bản; vẫn cần authority/freshness và review nội dung.

**Lỗi thường gặp:** Đổi verify ID + department thành verify success.

## Câu 6. Cost per evidence-complete pass dùng tử số nào?

**Ý đồ:** Kiểm tra selection bias trong cost.

**Gợi ý trả lời 30–60 giây:** Theo dictionary AOCE, tử số là tổng measured cost cả cohort, gồm failed, blocked và partial-evidence samples. Mẫu số là số pass có full evidence: E01/E02/E03/E08/E10 bằng 5. Subtotal .89 chia 5 ra .178 lower bound vì E08 thiếu model usage. .47/5 chỉ là cost trên riêng các pass và không phải metric được yêu cầu. Budget remaining tối đa .31, chưa xác nhận dưới budget.

**Hỏi tiếp:** Tại sao E04 failed vẫn tính cost? **Điểm cần trả lời:** Vì tài nguyên đã tiêu hao để tạo ra các output được chấp nhận.

**Lỗi thường gặp:** Chỉ cộng successful runs làm savings đẹp hơn.

Tự chấm: nêu đúng nguồn/mode, dùng một ví dụ, giữ unknown, chỉ rõ bằng chứng và next action. Không học thuộc câu trả lời thành lời xác nhận mình đã thực hiện.
