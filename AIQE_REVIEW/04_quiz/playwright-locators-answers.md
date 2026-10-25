# Đáp án và giải thích: playwright-locators

Chỉ đọc sau khi hoàn thành [câu hỏi](playwright-locators-questions.md). Nguồn và giới hạn API nằm trong [topic](../01_topics/playwright-locators.md).

## Câu 1: C

- A: First phụ thuộc thứ tự.
- B: Last che ambiguity.
- C: Scope gắn intent và vùng UI.
- D: Timeout không giảm số match.

## Câu 2: A

- A: Đúng: action tìm element cập nhật.
- B: Locator không khóa node lúc khai báo.
- C: Compile không query DOM.
- D: Browser launch chưa có target DOM.

## Câu 3: D

- A: Visual proximity không đủ.
- B: Placeholder không thay label.
- C: Có thể có role/name hay test hook khác.
- D: Đúng: kiểm chứng semantics.

## Câu 4: B

- A: Vị trí không là identity.
- B: Đúng: identity và scope.
- C: Không có entity scope.
- D: First có thể sai vùng.

## Câu 5: A

- A: Đúng: định danh theo contract.
- B: Không xác nhận semantics.
- C: Không xác nhận persistence.
- D: Chưa có run/assertion.

## Câu 6: C

- A: UI có thể chỉ render viewport.
- B: Node chưa render không tồn tại.
- C: Đúng: theo contract hiện có.
- D: Thiếu backend evidence.

## Câu 7: B

- A: API native select có điều kiện.
- B: Đúng: không giả định control type.
- C: Bypass behavior cần kiểm tra.
- D: Che state/actionability.

## Câu 8: D

- A: Có thể che regression.
- B: Mất coverage.
- C: Phụ thuộc render order.
- D: Đúng: sửa đúng lớp lỗi.

## Câu 9: C

- A: Có thể sai locale.
- B: Bám implementation.
- C: Đúng: copy thay đổi có chủ đích.
- D: Không biểu diễn intent.

## Câu 10: A

- A: Đúng: xử lý frame boundary.
- B: Không liên quan độ dài class.
- C: Không thay uniqueness.
- D: Không cấp permission.


