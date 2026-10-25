# Quiz tự luyện: playwright-execution-debugging

Tự biên soạn, không phải đề thi chính thức. Mỗi câu có bốn lựa chọn và đúng một đáp án tốt nhất. [Ôn kiến thức](../01_topics/playwright-execution-debugging.md).

## Câu 1

Mở tab mới trong context cũ cho isolation nào?

A. Mọi backend data độc lập
B. Có thể vẫn dùng chung auth/storage context
C. Tự có account mới
D. Không còn race

## Câu 2

Click Save thành công chứng minh gì?

A. AC-EMP-02 đã pass
B. Index backend xong
C. Department luôn đúng
D. Action click hoàn tất theo checks áp dụng

## Câu 3

Wait response đăng ký lúc nào?

A. Trước action trigger
B. Sau khi đọc toast
C. Sau action kết thúc
D. Sau test teardown

## Câu 4

Typecheck và discovery pass cho kết luận nào?

A. UI test pass
B. Production đúng
C. Chưa đủ evidence live test
D. MCP server đúng

## Câu 5

Snapshot rerun thể hiện gì?

A. DOM original failure chắc chắn
B. Root cause đã chứng minh
C. Tất cả attempts pass
D. Observation mới có provenance riêng

## Câu 6

First fail rồi retry pass: classification runner phù hợp?

A. Luôn passed sạch
B. Flaky
C. Skipped
D. Không có kết quả

## Câu 7

on-first-retry thu trace nào?

A. Retry đầu tiên
B. Chắc chắn original attempt
C. Mọi attempt
D. Không bao giờ thu

## Câu 8

Browser launch bị sandbox chặn nên báo gì?

A. Product assertion fail
B. Login defect
C. ENV-BLOCKED với sanitized error/context
D. Test pass vì chưa click

## Câu 9

Toast Success sau create là oracle đủ cho search department?

A. Luôn đủ
B. Không, assert đúng ID/department trong search
C. Chỉ cần screenshot
D. Chỉ tăng timeout toast

## Câu 10

Hai workers có context riêng nhưng dùng employee fixed mutable sẽ ra sao?

A. Không thể race
B. Playwright tự khóa DB
C. Teardown không cần
D. Vẫn có thể data collision

[Đáp án tách riêng](playwright-execution-debugging-answers.md).

