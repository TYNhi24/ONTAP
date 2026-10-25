# Đáp án và giải thích: agent-architecture

Chỉ đọc sau khi hoàn thành [câu hỏi](agent-architecture-questions.md). Nguồn và giới hạn API nằm trong [topic](../01_topics/agent-architecture.md).

## Câu 1: D

- A: Proposal có thể sai.
- B: Không thi hành quyền.
- C: Xuất test result.
- D: Đúng: enforce code/policy.

## Câu 2: B

- A: Quá rộng.
- B: Đúng: bounded contract.
- C: Secret không cần đưa prompt.
- D: Sai allowlist/scope.

## Câu 3: A

- A: Đúng: outcome có thể commit.
- B: Có thể double create.
- C: Làm mất provenance.
- D: Không được đổi expected để pass.

## Câu 4: C

- A: Sai trạng thái lifecycle.
- B: Vượt ownership.
- C: Đúng: tách hai tầng.
- D: Mất thông tin rủi ro.

## Câu 5: A

- A: Đúng: injection boundary.
- B: Trang không cấp quyền.
- C: Không có human grant.
- D: Không phải định nghĩa tool.

## Câu 6: D

- A: Không suy ra business API.
- B: Side effect cũ vẫn tồn tại.
- C: Write còn ambiguous.
- D: Đúng: phạm vi controller.

## Câu 7: C

- A: AI không tạo live evidence.
- B: Giống không là quan sát.
- C: Đúng: provenance không đổi.
- D: Timestamp bịa không hợp lệ.

## Câu 8: B

- A: Run và publish khác scope.
- B: Đúng: dùng grant thực tế.
- C: Model không cấp quyền.
- D: Protocol không cấp business approval.

## Câu 9: D

- A: Vượt stop condition.
- B: Mất evidence.
- C: Né policy.
- D: Đúng: termination có kiểm soát.

## Câu 10: A

- A: Đúng: claim theo packet.
- B: Giấu first failure và gap.
- C: Xóa evidence.
- D: Chưa có publish scope.


