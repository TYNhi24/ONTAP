# Quiz tự luyện: playwright-locators

Tự biên soạn, không phải đề thi chính thức. Mỗi câu có bốn lựa chọn và đúng một đáp án tốt nhất. [Ôn kiến thức](../01_topics/playwright-locators.md).

## Câu 1

Hai nút Confirm trùng tên ở toolbar và dialog. Cách sửa tốt nhất?

A. Dùng first()
B. Dùng last()
C. Scope vào dialog có tên đã inspect
D. Tăng timeout

## Câu 2

Locator được resolve khi nào trong action thông thường?

A. Khi dùng action trên locator
B. Chỉ lúc khai báo
C. Chỉ khi compile TypeScript
D. Chỉ lúc browser launch

## Câu 3

Field có visual text Username nhưng không có association. Kết luận nào đúng?

A. getByLabel chắc chắn chạy
B. Placeholder sửa được accessibility
C. CSS là phương án bắt buộc
D. Cần inspect association và ghi finding nếu thiếu

## Câu 4

Employee ID unique cần Edit trong bảng. Chọn gì?

A. Nút Edit thứ ba
B. Row có cell ID exact rồi Edit trong row
C. Mọi button có text Edit
D. Text employee đầu tiên

## Câu 5

Test ID chứng minh điều gì tốt nhất?

A. Hook định danh nếu contract được quản trị
B. Control accessible
C. Backend đã lưu
D. Test đã pass

## Câu 6

Virtualized list có 20 node trên tổng 1000 records. Assertion nào hợp lý?

A. Luôn count 1000 node
B. Dùng nth(999)
C. Kiểm tra flow tìm record theo UI contract
D. Kết luận mất dữ liệu

## Câu 7

Dropdown custom không phải select. Bước đầu là gì?

A. Luôn selectOption
B. Inspect role/state và interaction thật
C. Set value bằng evaluate
D. Force click mọi option

## Câu 8

Tên nút mất sau refactor trái NFR-A11Y. Làm gì?

A. Chỉ thay bằng class
B. Bỏ test
C. Chọn nút cuối
D. Ghi finding accessibility và đánh giá locator theo contract

## Câu 9

Test đa locale cần strategy nào?

A. Hardcode tiếng Anh mọi nơi
B. Dùng SVG path
C. Dùng translated expectation theo locale hoặc hook đã quản trị
D. Dùng index DOM

## Câu 10

frameLocator hữu ích khi nào?

A. Element nằm trong iframe đã xác định
B. Element có class dài
C. Muốn bỏ strictness
D. Muốn tăng quyền browser

[Đáp án tách riêng](playwright-locators-answers.md).

