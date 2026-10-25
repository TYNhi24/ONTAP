# Phỏng vấn — Nền tảng QA

Ôn [bài kiến thức](../01_topics/qa-foundations.md). Câu hỏi tự biên soạn; các câu trả lời là cách tiếp cận, không phải kinh nghiệm cá nhân của bạn.

## 1. Em bắt đầu test một yêu cầu thế nào?

**Kiểm tra:** khả năng tìm test basis và oracle.

**Trả lời 30–60 giây:** “Em sẽ xác định nguồn và phiên bản yêu cầu, các rule liên quan, dữ liệu và kết quả quan sát được. Em tách phần được duyệt khỏi assumption, ghi câu hỏi cho chỗ chưa rõ. Sau đó em chọn kỹ thuật phù hợp, ưu tiên theo rủi ro và review expected result trước khi chạy.”

**Hỏi sâu:** nếu yêu cầu nói “nhanh”, cần làm rõ thao tác, tải, môi trường, phép đo và ngưỡng; chưa tự gán một con số.

**Sai lầm:** mở AI sinh nhiều test trước khi biết thế nào là đúng.

## 2. EP và BVA khác nhau ở đâu?

**Kiểm tra:** hiểu lý do chọn dữ liệu.

**Trả lời 30–60 giây:** “EP chia dữ liệu thành nhóm có cùng cách xử lý dự kiến, giúp giảm số trường hợp có chủ đích. BVA chọn điểm sát ranh giới vì dễ có lỗi so sánh. Với quantity 1–10, em cân nhắc 0, 1, 10, 11 và một điểm giữa. Em vẫn cần test missing, null hoặc sai kiểu nếu contract có các miền đó.”

**Hỏi sâu:** với tiền có độ chính xác tới đơn vị nhỏ nhất, giá trị sát biên phải theo độ chính xác contract chứ không thêm số thập phân tùy ý.

**Sai lầm:** khẳng định một đại diện chứng minh mọi giá trị trong nhóm đều đúng.

## 3. Vì sao có decision table rồi vẫn cần state test?

**Kiểm tra:** chọn mô hình theo loại rủi ro.

**Trả lời 30–60 giây:** “Decision table làm rõ tổ hợp điều kiện và kết quả tại một thời điểm. State test kiểm tra lịch sử và thứ tự sự kiện. Rule discount cần tổ hợp VIP/campaign; refund còn phụ thuộc đơn đã thanh toán hay chưa. Em sẽ dùng cả hai nếu chức năng có hai loại rủi ro.”

**Hỏi sâu:** kiểm tra invalid transition và event lặp, nhưng không tự coi retry luôn hợp lệ.

**Sai lầm:** dùng nhiều tổ hợp input để tuyên bố đã bao phủ mọi thứ tự thao tác.

## 4. Thời gian chỉ đủ chạy 12 scenario thì chọn thế nào?

**Kiểm tra:** risk-based testing và residual risk.

**Trả lời 30–60 giây:** “Em sẽ ưu tiên theo tác động và khả năng xảy ra có bằng chứng, gồm mất tiền, quyền truy cập và hồi phục. Em tính cả chuẩn bị, phụ thuộc dữ liệu và triage, không chỉ số lượng ca. Với phần hoãn, em ghi rủi ro còn lại, người nhận trách nhiệm và điều kiện phải kiểm tra lại.”

**Hỏi sâu:** ARTD Unit 3 có hai ràng buộc đồng thời: không quá 12 scenario và không quá 180 phút; phải thỏa cả hai.

**Sai lầm:** lấy score trung bình che một rủi ro privacy nghiêm trọng.

## 5. Báo cáo 8 pass, 1 fail, 3 blocked như thế nào?

**Kiểm tra:** phân biệt tiến độ, kết quả và đủ điều kiện release.

**Trả lời 30–60 giây:** “Em báo 9/12 ca đã chạy, 8 pass và 1 fail; 3 ca chưa chạy vì blocker được ghi rõ. Em nêu tác động lỗi và rủi ro của phần chưa kiểm tra. Em không gộp blocked vào pass hoặc suy ra release ready chỉ từ tỷ lệ pass.”

**Hỏi sâu:** mỗi tỷ lệ cần mẫu số: pass trên executed là 8/9, còn số ca pass trên planned là 8/12; hai số trả lời hai câu hỏi khác nhau.

**Sai lầm:** báo một phần trăm mà không nói cohort, scope hay mẫu số.
