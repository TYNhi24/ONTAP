# Quiz — project-quality-gates

10 câu tự biên soạn để ôn tập, không phải đề/đáp án chính thức. Mỗi câu có một phương án tốt nhất. Đọc [bài học](../01_topics/project-quality-gates.md); làm xong mới mở [giải thích](./project-quality-gates-answers.md).

## Câu 1

AC tốt cho report là gì?

- **A.** Thiếu matching evidence thì không report pass, có run/revision refs
- **B.** Implement reporter.js
- **C.** Code xong 90%
- **D.** Agent thông minh

## Câu 2

Plan JSON valid nhưng source cũ, ai xử lý?

- **A.** Model tự duyệt
- **B.** Semantic validator/controller reject trước execution
- **C.** Reporter sửa sourceVersion sau
- **D.** Chạy rồi xem có lỗi không

## Câu 3

PBAAD F02 cần oracle nào?

- **A.** Department Engineering sau edit
- **B.** Toast success chung
- **C.** Duplicate rejection + exact-ID count1 + original department unchanged
- **D.** Chỉ có file test

## Câu 4

8/8 node --test local mẫu pass chứng minh gì?

- **A.** PortalLite UI đúng
- **B.** Model planner robust
- **C.** G5 hoàn tất
- **D.** Tám local test assertions pass trong scope synthetic

## Câu 5

Test verdictFor([{passed:false}]) cho biết gì?

- **A.** Aggregator trả FAIL cho assertion false, chưa chứng minh phát hiện department sai
- **B.** Checker phát hiện mọi record sai
- **C.** Exact-ID lookup đã chạy
- **D.** Stale evidence bị reject

## Câu 6

Test nghiệp vụ PASS, cleanup UNKNOWN. Report?

- **A.** Gộp tất cả PASS
- **B.** Giữ test PASS, cleanup UNKNOWN, release HOLD
- **C.** Đổi business assertion thành FAIL để dễ báo
- **D.** Xóa cleanup khỏi manifest

## Câu 7

Scripted proposals12/12 hợp lệ. Actual model sample count?

- **A.** 12
- **B.** 24 vì có hai flows
- **C.** 0; model evaluation pending
- **D.** 100% production robust

## Câu 8

QF-03 canary lộ trong public draft. Việc phù hợp?

- **A.** Dùng secret thật để thử lại
- **B.** Chỉ đổi tên file
- **C.** Public luôn vì employee synthetic
- **D.** Restrict raw, sanitize/demo review và canary retest

## Câu 9

Peer reproduction đúng nghĩa là gì?

- **A.** Người khác chạy frozen revision theo README và ghi actual results
- **B.** Tác giả chạy lại lần2
- **C.** AI viết “looks reproducible”
- **D.** Copy report lần trước

## Câu 10

Demo hiện scripted/in-memory, chưa có rehearsal events. Chọn cách nói?

- **A.** Live AI đã production-ready
- **B.** Disclose SIMULATED và HOLD; retro events chưa có thì pending
- **C.** Ghi planned events như đã xảy ra
- **D.** Đổi mode thành live để khách dễ hiểu
