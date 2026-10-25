# Kiểm tra hình ảnh — 25/10/2026

## Phương pháp và giới hạn

Đã trích PNG trực tiếp từ ZIP của hai PPTX, tính SHA-256 và xem cả 7 ảnh có nội dung byte khác nhau bằng công cụ xem ảnh. Mỗi deck chứa 11 media entries; media tương ứng giữa hai deck giống hash. [media-map.json](media-map.json) lưu ánh xạ tới slide khi slide tham chiếu trực tiếp; media không được tham chiếu trực tiếp có thể thuộc layout/master.

Không render được slide đầy đủ: PowerPoint COM trả `80070520` (logon session không tồn tại); không tìm thấy `soffice`. Vì vậy chữ/notes trích được và ảnh nhúng đã xem không chứng minh đã kiểm tra bố cục, hướng mũi tên hoặc chart/shape gốc trên mọi slide. Không suy diễn giá trị chart từ hình trang trí.

## Những ảnh đã xem

| Media trong cả hai deck | Vị trí tham chiếu trực tiếp | Quan sát |
|---|---|---|
| image.png, image2.png | Không có trong slide relationships trực tiếp | Nền lưới/margin màu hồng; không có kiến thức bằng chữ. |
| image3.png và image5–image8.png | slide 1, 3, 5, 6, 24 tùy entry | Cùng một nền gradient, không có chữ quy tắc. |
| image4.png | slide 3, 5, 6, 17, 18 | Nền ô bàn cờ; không có kiến thức bằng chữ. |
| image9.png | slide 17 | Minh họa nhiều nguồn/tín hiệu/kiến trúc đi vào danh mục thẻ scenario; không có số hay nhãn đọc được để làm rule. |
| image10.png | slide 18 | Minh họa cấu hình, dữ liệu, luồng bước và kiểm tra kết quả; phần chữ chuẩn tắc phải lấy từ slide text. |
| image11.png | slide 23 | Minh họa dữ liệu đi qua biến đổi/bảo vệ và phân nhóm đạt, sai, cảnh báo; không chứng minh phương pháp masking cụ thể. |

Nguồn: [ARTD ready v2](<../../document/AIQE AI-Assisted Requirement & Test Design/L3_AIQE_ARTD_training_deck_ready_v2.pptx>) và [ARTD vi final](<../../document/AIQE AI-Assisted Requirement & Test Design/L3_AIQE_ARTD_training_deck_vi_final.pptx>).

Hai PNG trong `.playwright-mcp` của Agent CI và NhiTY14 có cùng SHA-256. Đã xem một bản đại diện: trang Login OrangeHRM với Username, Password, nút Login và chân trang phiên bản OS 5.9. Đây chỉ là ảnh trang login, không có verdict chạy test, không chứng minh login pass hay employee lifecycle. Không chép credential hiển thị trên ảnh vào tài liệu ôn hoặc dùng nó để truy cập hệ thống.

Workbook chỉ có sheet `Training Calendar`; kiểm tra ZIP không có `xl/media/`. Đã đọc dữ liệu ô, không kiểm tra bố cục bằng Excel. DOCX không có media entry trong `word/media`; việc trích paragraph không cung cấp số trang render.
