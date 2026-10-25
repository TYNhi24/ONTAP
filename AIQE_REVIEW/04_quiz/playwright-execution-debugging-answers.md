# Đáp án và giải thích: playwright-execution-debugging

Chỉ đọc sau khi hoàn thành [câu hỏi](playwright-execution-debugging-questions.md). Nguồn và giới hạn API nằm trong [topic](../01_topics/playwright-execution-debugging.md).

## Câu 1: B

- A: Backend ngoài browser context.
- B: Đúng: page không phải context mới.
- C: Không tạo identity mới.
- D: Shared data vẫn race.

## Câu 2: D

- A: Cần assertion business.
- B: Không biết index.
- C: Chưa có oracle.
- D: Đúng: phạm vi action.

## Câu 3: A

- A: Đúng: ngăn race listener.
- B: Có thể lỡ event.
- C: Event nhanh đã xảy ra.
- D: Quá muộn.

## Câu 4: C

- A: Không thực thi UI oracle.
- B: Không kiểm chứng production.
- C: Đúng: chỉ check phạm vi riêng.
- D: Không liên quan.

## Câu 5: D

- A: Không quay lại state cũ.
- B: Cần check phân biệt.
- C: Không có result tương ứng.
- D: Đúng: tách original/rerun.

## Câu 6: B

- A: Xóa failure là sai.
- B: Đúng: giữ hai attempts.
- C: Đã có execution.
- D: Có per-attempt results.

## Câu 7: A

- A: Đúng theo mode.
- B: Original không được thu bởi mode này.
- C: Không phải on.
- D: Có thu retry đầu nếu xảy ra.

## Câu 8: C

- A: Chưa chạy oracle.
- B: Chưa kiểm chứng login.
- C: Đúng: infrastructure blocker.
- D: Không chạy không là pass.

## Câu 9: B

- A: Feedback khác read state.
- B: Đúng: gần AC-EMP-02.
- C: Visual toast không đủ.
- D: Không thêm business evidence.

## Câu 10: D

- A: Context không khóa backend.
- B: Không có bảo đảm này.
- C: Cleanup vẫn cần.
- D: Đúng: unique data vẫn cần.


