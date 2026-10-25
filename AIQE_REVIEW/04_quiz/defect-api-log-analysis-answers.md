# Giải thích: defect, API và log

Đáp án cho [câu hỏi tự biên](defect-api-log-analysis.md). Căn cứ [bài học và nguồn DALA EN/VI/exercises](../01_topics/defect-api-log-analysis.md).

| Câu | Đáp án | Giải thích từng lựa chọn |
|---|---|---|
| D1 | C | **A sai:** timeout là unknown outcome, không phải decline. **B sai:** callback muộn có thể hợp lệ; không tự loại evidence. **C đúng:** giữ cả HTTP và provider, đối soát theo BR-PAY-01. **D sai:** retry có thể tạo side effect trùng và cần contract/control. Nguồn: 5.2 BR-PAY-01, 5.4 seed, Session 5.3. |
| D2 | A | **A đúng:** đó là mức source xác nhận; ownership/cause còn cần điều tra. **B sai:** hai key khác không phải same-key test. **C sai:** không có proof độc quyền về owner. **D sai:** provider request IDs khác, chưa chứng minh provider tự retry. Nguồn: 5.4 đoạn giới hạn evidence, Unit 2. |
| D3 | B | **A sai:** cộng offset thay vì trừ. **B đúng:** giờ local bằng UTC+7 nên UTC bằng local−7. **C sai:** đổi ký hiệu mà không đổi giờ. **D sai:** timestamp UTC vẫn có phần millisecond. Nguồn: NFR-OBS-01, Session 3.2, EX-U3-LOGS. |
| D4 | D | **A sai:** status/schema chỉ là một phần oracle. **B sai:** API phải thực thi authorization theo BR-AUTH-01. **C sai:** hidden UI link không ngăn gọi API trực tiếp. **D đúng:** ownership là semantic/security assertion độc lập. Nguồn: 5.2 BR-AUTH-01, Sessions 4.2/5.2. |
| D5 | B | **A sai:** absence trong sample không chứng minh absence thực tế. **B đúng:** kiểm tra source reliability và bổ sung state evidence. **C sai:** vẫn có next queries và observability checks. **D sai:** bịa evidence là critical failure. Nguồn: Sessions 3.1/3.4, log quality criteria. |
| D6 | C | **A sai:** thông lệ không phải contract. **B sai:** key giống không định nghĩa kết quả changed payload. **C đúng:** ghi gap và owner question. **D sai:** tự phát minh behavior. Nguồn: 5.3 contract, Session 4.3, EX-U5-API-SCENARIOS. |
| D7 | A | **A đúng:** strong negative oracle gồm error an toàn và forbidden effects. **B sai:** AI/message length không là oracle nghiệp vụ được duyệt. **C sai:** phản hồi lỗi không cho phép tạo payment ngoài cam kết. **D sai:** cleanup trước lưu evidence gây mất khả năng điều tra. Nguồn: Sessions 5.2/6.1, EX-U4-API-FOUNDATION. |
| D8 | D | **A sai:** độ dài không là evidence. **B sai:** đồng thuận mô hình không xác nhận cơ chế. **C sai:** che uncertainty thành fabricated certainty. **D đúng:** check phân biệt tăng thông tin, có phản chứng và xác minh con người. Nguồn: Sessions 2.2–2.4, hypothesis matrix và generic prompt frame. |
