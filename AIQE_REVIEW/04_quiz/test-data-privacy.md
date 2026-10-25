# Trắc nghiệm tự luyện: dữ liệu và quyền riêng tư

Tự biên, không phải đề chính thức; chọn **một đáp án tốt nhất**. [Bài học](../01_topics/test-data-privacy.md) · [Giải thích sau khi làm](test-data-privacy-answers.md).

## T1. Hàng quantity 0 được ghi expected-invalid và validator từ chối đúng rule quantity. Kết luận phù hợp?

A. Generator luôn lỗi vì có hàng invalid.
B. Kiểm tra dataset đạt mục đích hàng âm tính; API response cần bằng chứng execution riêng.
C. API đã pass vì validator bắt được quantity.
D. Xóa hàng đó để dataset toàn màu xanh.

## T2. Cách nào cô lập kiểm thử quantity trên 10 tốt nhất?

A. Quantity 11, customer UUID hợp lệ/active, SKU hợp lệ và các trường khác đúng.
B. Quantity 11, customer thiếu, body JSON malformed.
C. Quantity 10 và sai Content-Type.
D. Quantity bất kỳ, expected “request không tốt”.

## T3. orders có customer_id đúng format UUID nhưng ID đó không có trong customers. Điều gì bị vi phạm?

A. Chỉ style naming.
B. Referential integrity, dù hình dạng trường có thể đúng schema.
C. Không có lỗi vì UUID duy nhất.
D. Chỉ performance.

## T4. Nhóm mask tên nhưng giữ email thật, postal code và birth month. Nhận định đúng nhất?

A. Đã anonymize hoàn toàn vì không còn tên.
B. Hash thêm customer ID là chắc chắn đủ.
C. Vẫn có direct contact và linkage risk; cần giảm/thay dữ liệu và đánh giá phần còn lại.
D. Có thể tải lên AI bất kỳ vì đây là staging.

## T5. Cách xử lý PAN/CVV/credential trong dataset đào tạo phù hợp nhất?

A. Giữ raw để giống production.
B. Gửi AI raw rồi yêu cầu che đầu ra.
C. Đổi tên field để người khác khó nhận ra.
D. Loại bỏ, dùng stub hoặc provider test token đúng môi trường và policy.

## T6. Team lưu seed nhưng không lưu dataset, model/prompt version, generator version hay reference clock. Kết luận?

A. Seed đảm bảo mọi mô hình sinh cùng dữ liệu.
B. Chưa đủ tái tạo; cần artifact/version/clock và quy trình kiểm tra xác định phù hợp.
C. Chỉ cần ảnh chụp 5 dòng đầu.
D. Không cần tái tạo vì AI có thể tạo lại dữ liệu tương tự.

## T7. orderTotal tối thiểu 1.000 sau discount. Chọn test data nào đúng thiết kế biên nhất?

A. Ghi total 999 độc lập dù tổng item tính ra 50.000, không gắn expected violation khác.
B. Dùng duy nhất total 10.000 vì nó hợp lệ.
C. Dựng totals 999/1.000/1.001 từ item/discount nhất quán, ghi expected validity theo rule và kiểm tra riêng phép tính.
D. Sinh số ngẫu nhiên và gọi toàn bộ là boundary.

## T8. Dataset có email example.com, cần thêm kiểm soát gì?

A. Không cần gì vì reserved domain tự chứng minh cả pipeline an toàn.
B. Đổi sang email thật để chắc gửi thành công.
C. Bỏ mọi notification test.
D. Kiểm tra outbound/contact safety, dùng stub khi cần, dữ liệu synthetic và cleanup/expiry theo scope.
