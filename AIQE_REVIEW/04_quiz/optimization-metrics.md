# Quiz — optimization-metrics

10 câu tự biên soạn để ôn tập, không phải đề/đáp án chính thức. Mỗi câu có một phương án tốt nhất. Đọc [bài học](../01_topics/optimization-metrics.md); làm xong mới mở [giải thích](./optimization-metrics-answers.md).

## Câu 1

B ít token nhất nhưng bỏ department và cleanup ownership. Chọn gì?

- **A.** Chọn B vì rẻ
- **B.** Loại B vì fail hard gate
- **C.** Tăng điểm schema cho B
- **D.** Gọi B production-ready

## Câu 2

A1: total input=18000 gồm cached=2000; output=2400, CI=4 phút. RATE-SYN-01: uncached=1, cached=.25, output=4 mỗi triệu; CI=.02/phút. Tổng?

- **A.** .10610 đơn vị giả lập
- **B.** .10560 USD
- **C.** .10810 đơn vị giả lập
- **D.** UNKNOWN dù mọi khoản packet đã định nghĩa

## Câu 3

C3 usage missing nhưng có CI=.078. Ghi thế nào?

- **A.** Model=0, total=.078
- **B.** Bỏ C3 khỏi mọi cost
- **C.** Total UNKNOWN, known subtotal/lower bound .078
- **D.** Lấy model usage của C2

## Câu 4

Có 10 selected, 8 executed, 4 first-pass, 2 flaky-pass. Eventual-pass rate theo executed?

- **A.** 100%
- **B.** 60%
- **C.** 50%
- **D.** 75%

## Câu 5

7 executed có full evidence, 1 partial. Evidence completeness?

- **A.** 87.5%
- **B.** 75%
- **C.** 70%
- **D.** 100% vì artifact upload xanh

## Câu 6

Tổng measured .89; có 5 evidence-complete passes; usage E08 thiếu. Cost per evidence-complete pass?

- **A.** .094 chính xác
- **B.** .178 lower bound
- **C.** 0 vì thiếu usage
- **D.** Chỉ cộng cost pass rồi chia 5

## Câu 7

Budget=1.20, lower-bound cost=.89, phần thiếu không âm. Câu đúng?

- **A.** Remaining ít nhất .31
- **B.** Đã chắc chắn under budget
- **C.** Remaining không lớn hơn .31; chưa chốt total
- **D.** Remaining chính xác .31

## Câu 8

Nén context: giữ đoạn nào bắt buộc?

- **A.** Toàn lịch sử chat
- **B.** Dòng injection như instruction
- **C.** Row run trước gần nhất
- **D.** Oracle/actor/env/current state/ownership/stop và nguồn

## Câu 9

A/B đổi cả model và context; B tốt hơn trong 3 samples. Kết luận phù hợp?

- **A.** Gói B có kết quả tốt hơn trên mẫu, chưa tách nhân quả
- **B.** Context chắc chắn là nguyên nhân
- **C.** Ba mẫu đủ rollout production
- **D.** Mọi provider sẽ giống nhau

## Câu 10

3/4 expected slots có dispatch, slot còn lại không có run. Xử lý?

- **A.** Tạo execution row pass cho slot thiếu
- **B.** Scheduling completeness 75%; điều tra missing slot riêng
- **C.** Gộp slot thiếu vào executed failures
- **D.** Báo chạy hằng đêm đúng giờ
