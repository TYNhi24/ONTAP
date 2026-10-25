# Giải thích: dữ liệu và quyền riêng tư

Cho [bộ câu hỏi tự biên](test-data-privacy.md). Căn cứ: [bài học/nguồn ARTD Unit 6](../01_topics/test-data-privacy.md).

| Câu | Đáp án | Giải thích từng lựa chọn |
|---|---|---|
| T1 | B | **A sai:** intentional invalid là tài sản negative testing. **B đúng:** validator khớp expected, nhưng chưa có API execution. **C sai:** trộn kiểm tra dữ liệu với behavior hệ thống. **D sai:** làm mất lớp âm tính có chủ đích. Nguồn: Unit 6 Session 6.4, EX-U6-DATA validation report. |
| T2 | A | **A đúng:** chỉ target quantity sai, chẩn đoán rõ. **B sai:** nhiều lỗi có thể khiến request dừng trước quantity. **C sai:** quantity 10 hợp lệ, lại thử media type. **D sai:** input và oracle không cụ thể. Nguồn: Session 6.2, expected-invalid quality criteria. |
| T3 | B | **A sai:** không chỉ hình thức. **B đúng:** FK phải trỏ bản ghi cha hợp lệ. **C sai:** uniqueness không tạo parent tồn tại. **D sai:** lỗi quan hệ dữ liệu không chỉ là tốc độ. Nguồn: Minimal relational schema; Sessions 6.1/6.4. |
| T4 | C | **A sai:** email vẫn trực tiếp liên hệ cá nhân, quasi-identifiers vẫn có nguy cơ. **B sai:** hash không bảo đảm vô danh và không bỏ email thật. **C đúng:** cần minimization/synthetic/linkage review. **D sai:** staging không cấp phép gửi dữ liệu tới dịch vụ AI chưa duyệt. Nguồn: Data inventory; Session 6.3; responsible AI agreement. |
| T5 | D | **A sai:** vi phạm dữ liệu an toàn. **B sai:** phơi lộ ngay ở input. **C sai:** rename không bảo vệ giá trị. **D đúng:** loại bí mật, dùng cơ chế kiểm thử được phê duyệt. Nguồn: EX-U6-DATA minimum standard và critical cap. |
| T6 | B | **A sai:** seed không bảo đảm mô hình/dịch vụ lặp đúng output. **B đúng:** giữ artifact/provenance, clock và validation để tái lập. **C sai:** ảnh vài dòng thiếu dữ liệu và môi trường. **D sai:** tương tự không đồng nghĩa tái tạo case lỗi. Nguồn: Session 6.4, EX-U6-DATA Instructions 7–8; lưu artifact là cách triển khai tự biên phù hợp yêu cầu provenance. |
| T7 | C | **A sai:** tạo thêm lỗi cross-field, không cô lập biên total. **B sai:** bỏ ranh giới. **C đúng:** sát biên, quan hệ số tiền nhất quán, expected rõ. **D sai:** random không chứng minh boundary coverage. Nguồn: interface orderTotal constraint; Sessions 6.1/6.2/6.4. |
| T8 | D | **A sai:** domain không tự kiểm soát outbound pipeline hoặc các contact khác. **B sai:** tạo tác động tới người thật. **C sai:** vẫn test an toàn bằng stub. **D đúng:** bảo vệ dữ liệu lẫn vận hành. Nguồn: EX-U6-DATA contact-safety/setup/cleanup; responsible AI agreement. |
