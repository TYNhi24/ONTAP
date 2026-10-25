# Giải thích: yêu cầu và thiết kế kiểm thử

Đáp án cho [câu hỏi tự biên](requirement-test-design.md). Căn cứ chi tiết trong [bài học và nguồn ARTD](../01_topics/requirement-test-design.md).

| Câu | Đáp án | Giải thích từng lựa chọn |
|---|---|---|
| R1 | B | **A sai:** thêm ngưỡng chưa duyệt. **B đúng:** biến mơ hồ thành câu hỏi đo lường có owner. **C sai:** gap cần quản lý, không tự bỏ scope. **D sai:** benchmark AI không phải approved product rule. Nguồn: Unit 1 Sessions 1.1–1.4, EX-U1-RQA. |
| R2 | C | **A sai:** happy path không chứng minh chống truy cập chéo. **B sai:** confidence mô hình không thay evidence. **C đúng:** kiểm tra role/object và non-disclosure cần có riêng. **D sai:** absence automation không xóa requirement. Nguồn: Unit 2 Session 2.2, EX-U2-TRACE minimum standard. |
| R3 | C | **A sai:** cộng 10+15 vi phạm rule. **B sai:** bỏ campaign cao hơn. **C đúng:** 240.000 × 0,85 = 204.000, chọn mức hợp lệ cao nhất. **D sai:** “đúng” không là oracle đo được. Nguồn: minimum source pack BR-DIS-01, Unit 3 decision table, Unit 4 oracle. |
| R4 | D | **A sai:** nguồn không định nghĩa hierarchy luôn ưu tiên API. **B sai:** tuổi tài liệu không tự quyết tính đúng. **C sai:** che conflict làm mất evidence. **D đúng:** giữ hai nguồn, hỏi quyết định và chặn assertion không có căn cứ. Nguồn: interface/data constraints, EX-U1-RQA. |
| R5 | C | **A sai:** chỉ thay UI bỏ tác động hệ thống. **B sai:** cumulative approval là deliberate gap, không tự chọn per-request. **C đúng:** impact analysis trực tiếp/gián tiếp và clarification đầy đủ. **D sai:** quantity không phải rủi ro duy nhất. Nguồn: CR-01, EX-U2-TRACE. |
| R6 | B | **A sai:** vượt 12 dù dưới 180 phút. **B đúng:** thỏa cả giới hạn và minh bạch phần hoãn. **C sai:** vượt thời gian. **D sai:** AI không quyết định cuối và kế hoạch phải khả thi. Nguồn: EX-U3-SCENARIO Inputs, Instructions 5–7. |
| R7 | A | **A đúng:** có target/resources/risk/timebox, cho phép thích nghi. **B sai:** đây là scripted path. **C sai:** thiếu applicability và mission. **D sai:** quá rộng, không đủ mục tiêu/giới hạn. Nguồn: Unit 5 Sessions 5.1–5.4, EX-U5-EXPLORE. |
| R8 | D | **A sai:** chỉ đổi nhãn, không sửa oracle. **B sai:** selector không chữa business expectation. **C sai:** tạo hidden dependency và order sensitivity. **D đúng:** sửa executability, observability, side effects và operations theo nguồn. Nguồn: Unit 4 Sessions 4.1–4.4, EX-U4-CASES. |
