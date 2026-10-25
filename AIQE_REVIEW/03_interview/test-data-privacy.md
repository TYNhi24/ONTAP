# Phỏng vấn: dữ liệu kiểm thử và quyền riêng tư

Tự biên, không phải đề chính thức. Nền tảng và nguồn ở [bài học](../01_topics/test-data-privacy.md). Khung trả lời hướng đến 30–60 giây.

## 1. AI sinh 1.000 customer JSON đẹp, bạn kiểm tra gì?

**Ý định:** kiểm tra validation và purpose, không đánh đồng hình thức với chất lượng.

**Gợi ý trả lời:** Em bắt đầu từ scenario-to-data map để biết mỗi lớp dữ liệu dùng kiểm tra gì, rồi parse/schema, type/format/range, uniqueness và liên kết customer/order/payment. Tiếp theo em kiểm tra cross-field, phép tính, trạng thái, privacy và contact safety bằng script/query. Em giữ nhãn expected-valid/invalid và expected failure cho hàng âm tính. Em lưu version, seed, đồng hồ và report actual so với expected. Một ngàn dòng trùng mục đích không thay được biên hoặc quyền truy cập còn thiếu.

**Đào sâu:** Từ chối một hàng intentionally invalid có khiến generator fail không? **Lỗi thường gặp:** hỏi chính AI “dữ liệu này đúng chưa” rồi coi đó là proof.

## 2. Bạn chọn dữ liệu cho quantity 1–10 như thế nào?

**Ý định:** kiểm tra equivalence/boundary và cô lập vi phạm.

**Gợi ý trả lời:** Em chia lớp dưới miền, hợp lệ và trên miền; chọn 0,1,2,9,10,11 để chạm cả hai phía biên. Em thêm missing/null/wrong type/số lẻ thành lớp riêng theo contract. Với mỗi hàng em giữ customer, SKU và các trường khác hợp lệ, gắn scenario ID và expected validity. Quantity 0 bị validator bắt là expected failure của dữ liệu; API response và non-effect như không charge phải có kiểm thử execution riêng. Nếu một hàng có nhiều vi phạm thì ghi rõ mục tiêu thay vì vô tình tạo nhiễu.

**Đào sâu:** Nếu total có discount, bạn dựng dữ liệu sát biên thế nào? **Lỗi thường gặp:** chỉ thử 1 và 10, hoặc làm sai nhiều trường cùng lúc.

## 3. Mask tên và hash customer ID đã đủ an toàn chưa?

**Ý định:** phát hiện hiểu sai masking/anonymity.

**Gợi ý trả lời:** Chưa đủ để kết luận. Email, phone, free text, amount/timestamp hiếm và quasi-identifiers vẫn có thể nhận diện hoặc liên kết. Hash có thể giữ linkage và bị đoán ở miền nhỏ. Em giảm dữ liệu không cần, dùng synthetic cho direct identifiers, loại PAN/CVV/secrets và dùng test token/stub. Nếu cần liên kết bảng em dùng ánh xạ nhất quán được kiểm soát. Em kiểm tra residual risk, quyền truy cập và retention; không gửi raw production vào AI để nhờ che vì dữ liệu đã bị phơi lộ tại input.

**Đào sâu:** Khi nào tokenization tốt hơn shuffling? **Lỗi thường gặp:** cho rằng không có tên thì đã vô danh.

## 4. Dữ liệu đúng schema nhưng payment trỏ order không tồn tại thì sao?

**Ý định:** kiểm tra referential/business integrity.

**Gợi ý trả lời:** Hình dạng schema chưa đủ. Em kiểm tra payment.order_id thuộc tập order tồn tại, order.customer_id tham chiếu đúng customer và quantity/amount/state thỏa rule. Với invalid-reference scenario em giữ hàng đó, gắn expected-invalid và xác nhận nó fail đúng check. Với baseline em sửa generator/map dùng cùng ID xuyên bảng, không patch ngẫu nhiên từng bản ghi. Em kiểm tra lại các dòng bị ảnh hưởng và giữ provenance/version để người khác tái tạo được.

**Đào sâu:** Mã hóa nhất quán ở từng bảng có tự bảo đảm đúng quan hệ không? **Lỗi thường gặp:** chỉ dùng UUID regex hoặc đếm row.

## 5. Có seed là tái tạo được dataset AI chưa?

**Ý định:** kiểm tra giới hạn reproducibility và vận hành.

**Gợi ý trả lời:** Seed chỉ là một phần. Em lưu generator version, nguồn/rule version, prompt/model nếu được phép, fixed reference clock/timezone và artifact dataset đã phê duyệt. Mô hình có thể không tạo lại cùng giá trị, nên khi cần chính xác em giữ dataset hoặc dùng generator xác định và hash/reference. Setup gắn run namespace và dữ liệu riêng; reset/teardown có scope, giữ evidence trước cleanup, đặt expiry và quyền truy cập. Kết quả validation phải chạy lại được trên cùng artifact.

**Đào sâu:** Vì sao refund 30 ngày không nên dùng ngày hệ thống tự đổi? **Lỗi thường gặp:** chỉ lưu prompt, không lưu dataset/clock/version.
