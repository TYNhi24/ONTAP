# Phỏng vấn: playwright-locators

Tự biên soạn, không phải câu hỏi/đáp án chính thức. Mẫu trả lời hướng đến 30–60 giây; hãy diễn đạt lại và thêm ví dụ của mình.

## 1. Vì sao locator là contract?

- Ý định: Kiểm tra tư duy maintenance.
- Trả lời 30–60 giây: Em sẽ mô tả user intent, role/name, scope và uniqueness thay vì vị trí DOM. Ví dụ Edit employee phải nằm trong row có ID chính xác. Như vậy thêm một row không đổi đích click; mất accessible name có thể là regression cần báo UI. Trong bài lab, em sẽ ghi mỗi locator cùng intent, scope và nguồn DOM vào inventory để người review hiểu vì sao nó đúng. Nếu chưa inspect được target, em sẽ đánh dấu candidate là cần evidence thay vì nói selector đã chạy. Cách này giúp phân biệt thay đổi UI có chủ đích với lỗi chọn nhầm element.
- Hỏi sâu: Nếu label đổi do i18n, chọn locale expectation hoặc test ID có owner.
- Lỗi thường gặp: Nói role luôn tốt nhất mà không inspect.

## 2. Có hai nút Save thì xử lý sao?

- Ý định: Kiểm tra strictness.
- Trả lời 30–60 giây: Em sẽ inspect hai vùng, xác định dialog đúng rồi scope Save bên trong. Em sẽ không dùng last vì thứ tự render có thể đổi; nếu scope vẫn match nhiều thì cần thêm contract có nghĩa. Em sẽ kiểm tra dialog có visible và có tên truy cập đúng trước khi thao tác. Sau khi click, em sẽ thêm assertion cho kết quả nghiệp vụ chứ không dừng ở việc hết strictness error. Nếu vẫn có hai nút trong cùng dialog, em sẽ tìm thêm contract có nghĩa hoặc báo thiếu thông tin, không chọn theo vị trí.
- Hỏi sâu: Kiểm tra hidden duplicate và trạng thái dialog ở attempt lỗi.
- Lỗi thường gặp: Dùng first để hết lỗi.

## 3. Test ID có thay accessibility test không?

- Ý định: Kiểm tra trách nhiệm oracle.
- Trả lời 30–60 giây: Em sẽ giải thích rằng test ID định danh được element qua hook riêng nhưng không chứng minh role/name đúng. Em sẽ dùng nó khi contract user-facing không ổn định và vẫn báo finding nếu interactive control thiếu tên truy cập. Trong bài lab, em sẽ ghi rõ ai sở hữu test hook và thay đổi nào cần cập nhật test. Em sẽ không tự thêm hook ẩn vào DOM chỉ để test chạy. Khi cần kiểm tra accessibility, em sẽ dùng assertion hoặc công cụ phù hợp cho semantics thay vì lấy việc tìm thấy test ID làm bằng chứng.
- Hỏi sâu: Ai sở hữu hook và khi nào đổi tên?
- Lỗi thường gặp: Cho rằng data-testid tự làm UI accessible.

## 4. Lọc hàng theo employee ID thế nào?

- Ý định: Kiểm tra scope theo entity.
- Trả lời 30–60 giây: Em sẽ tìm row có cell chứa ID exact, assert count một, rồi thao tác Edit trong row. Pattern chỉ hợp lệ nếu app expose row/cell như observation. Data unique theo run giúp không đụng employee khác. Trước khi dùng pattern này, em sẽ xác nhận UI thực sự expose row và cell, vì custom grid có thể có cấu trúc khác. Với danh sách ảo hóa, em sẽ đi theo search hoặc scroll flow được product hỗ trợ. Em sẽ không kết luận mất dữ liệu chỉ vì DOM chỉ chứa các hàng đang hiển thị.
- Hỏi sâu: Virtualized grid không render toàn bộ dataset xử lý ra sao?
- Lỗi thường gặp: Assert DOM count bằng tổng database.

## 5. getByLabel khác placeholder ra sao?

- Ý định: Kiểm tra semantics form.
- Trả lời 30–60 giây: Em sẽ giải thích rằng getByLabel tìm qua label association; placeholder là gợi ý trong field và có thể biến mất hay đổi copy. Em sẽ inspect association thật, ưu tiên label contract cho form. Visual text gần input chưa đủ chứng minh liên kết. Em sẽ ưu tiên control native có semantics đúng khi thiết kế test, nhưng vẫn dựa trên UI hiện tại. Nếu form dùng custom component, em sẽ inspect role, trạng thái và cách mở/chọn option trước khi chọn API thao tác. Điều quan trọng là test phản ánh cách người dùng thực hiện flow, không chỉ làm giá trị field thay đổi.
- Hỏi sâu: Custom combobox có phải selectOption không?
- Lỗi thường gặp: Coi mọi dropdown là native select.

## 6. Khi locator fail có luôn sửa test?

- Ý định: Kiểm tra diagnosis.
- Trả lời 30–60 giây: Em sẽ xem trace, requirement và DOM của attempt để biết UI thay đổi có chủ đích hay mất semantics. Nếu accessible name bị xóa trái AC accessibility thì mở finding; nếu scope test sai em sẽ sửa locator, review rồi chạy lại. Em sẽ giữ artifact của failure gốc và ghi rõ điều nào là observation, điều nào mới là giả thuyết. Sau đó em sẽ chọn bước kiểm tra giúp phân biệt hai khả năng thay vì đổi selector ngay. Bản sửa cần giữ nguyên test intent, được review và có run evidence riêng nếu môi trường cho phép.
- Hỏi sâu: Evidence nào phân biệt UI regression với test drift?
- Lỗi thường gặp: Sửa selector ngay để suite xanh.

Nguồn đối chiếu và kiến thức nền: [topic](../01_topics/playwright-locators.md), các heading course/exercise ghi trong topic. Tình huống và lời giải ở đây là tự biên soạn.

