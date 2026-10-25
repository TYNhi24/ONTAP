# Những khái niệm dễ nhầm

Đây là bảng nhắc nhanh; đọc bài được liên kết để hiểu đầy đủ. Các phân biệt được tổng hợp từ các bài giảng trong bộ ôn, không phải đáp án đề thi.

| Cặp khái niệm | Phân biệt bằng câu hỏi thực tế | Bẫy cần tránh | Ôn lại |
|---|---|---|---|
| QA / testing | Đang cải thiện cách tạo chất lượng hay đánh giá sản phẩm? | QA chỉ là chạy test. | [Nền tảng](../01_topics/qa-foundations.md) |
| Test level / test type | Đang nói phạm vi đối tượng hay thuộc tính cần kiểm tra? | Security luôn là một tầng riêng. | [Nền tảng](../01_topics/qa-foundations.md) |
| EP / BVA | Chia nhóm hành vi hay chọn điểm sát ranh giới? | Một điểm giữa thay thế mọi test biên. | [Nền tảng](../01_topics/qa-foundations.md) |
| Scenario / test case | Có mục tiêu tổng quát hay đã đủ precondition/data/step/oracle? | Scenario dài là case thực thi được. | [Thiết kế](../01_topics/requirement-test-design.md) |
| Traceability / coverage | Có liên kết hay đã kiểm tra đủ chiều rủi ro và có oracle đúng? | Link 100% = chất lượng 100%. | [Thiết kế](../01_topics/requirement-test-design.md) |
| Fact / inference / assumption | Điều gì được nguồn xác nhận, được suy ra, hay tạm giả định? | Giả định hợp lý tự thành rule. | [Thiết kế](../01_topics/requirement-test-design.md) |
| Charter / scripted case | Hướng khám phá có mục tiêu hay chuỗi bước đã xác định? | Exploratory nghĩa là không ghi bằng chứng. | [Thiết kế](../01_topics/requirement-test-design.md) |
| Masking / anonymization | Đã che trường hay đã chứng minh không thể nhận diện lại theo bối cảnh? | Bỏ tên là đủ bảo vệ mọi dữ liệu. | [Dữ liệu](../01_topics/test-data-privacy.md) |
| Synthetic / safe | Dữ liệu được tạo mới hay đã kiểm tra không có secret/contact hoạt động? | AI tạo là mặc nhiên an toàn. | [Dữ liệu](../01_topics/test-data-privacy.md) |
| Severity / priority | Tác động nghiêm trọng tới đâu hay xử lý theo thứ tự nào? | Hai trường luôn phải bằng nhau. | [Defect/API/log](../01_topics/defect-api-log-analysis.md) |
| Symptom / root cause | Quan sát thấy gì hay cơ chế nào đã được kiểm chứng gây ra nó? | Dòng log gần failure nhất chắc chắn là nguyên nhân. | [Defect/API/log](../01_topics/defect-api-log-analysis.md) |
| Authentication / authorization | Là ai hay được phép làm gì? | 400 validation đồng nghĩa lỗi đăng nhập. | [Defect/API/log](../01_topics/defect-api-log-analysis.md) |
| 201 / business completion | Resource được tạo hay nghiệp vụ đã hoàn thành theo contract cụ thể? | 201 luôn có nghĩa đã paid. | [Defect/API/log](../01_topics/defect-api-log-analysis.md) |
| Correlation ID / idempotency key | Nối sự kiện quan sát hay định danh yêu cầu lặp để kiểm soát side effect? | Có correlation ID sẽ ngăn thu tiền trùng. | [Defect/API/log](../01_topics/defect-api-log-analysis.md) |
| DOM / accessibility tree | Cấu trúc tài liệu hay biểu diễn ngữ nghĩa cho công nghệ hỗ trợ? | Thấy chữ bằng mắt là biết accessible name. | [Locator](../01_topics/playwright-locators.md) |
| Locator / snapshot ref | Cách tìm phần tử có thể đánh giá lại hay tham chiếu theo snapshot công cụ? | Dùng mã ref cũ làm selector bền vững. | [Locator](../01_topics/playwright-locators.md) |
| Auto-wait / oracle | Sẵn sàng thực hiện action hay kết quả nghiệp vụ đúng? | Click thành công chứng minh tạo employee thành công. | [Execution](../01_topics/playwright-execution-debugging.md) |
| Test retry / business retry | Chạy lại test hay lặp thao tác gây side effect? | Cứ timeout thì tạo lại bản ghi. | [CI/recovery](../01_topics/ci-recovery.md) |
| LLM / agent / MCP | Model sinh nội dung, hệ điều phối hành động, hay giao thức nối công cụ? | Có MCP là đã có agent an toàn. | [Architecture](../01_topics/agent-architecture.md) |
| Prompt guardrail / enforced policy | Chỉ dặn model hay code thực sự chặn tool không hợp lệ? | Dòng ‘không xóa’ thay thế kiểm tra quyền. | [Architecture](../01_topics/agent-architecture.md) |
| Token reduction / optimization | Giảm đầu vào hay tăng hiệu quả trong khi vẫn giữ quality gate? | Rẻ hơn dù bỏ source vẫn là tốt hơn. | [Metrics](../01_topics/optimization-metrics.md) |
| Pass / accepted / evidence-complete | Oracle đạt, kết quả đủ tiêu chí chấp nhận, hay đủ bộ artifact theo contract? | Dùng lẫn mẫu số tạo báo cáo đẹp. | [Metrics](../01_topics/optimization-metrics.md) |
| Simulated / live | Adapter/dữ liệu mô phỏng hay tương tác hệ thống thực có build/run provenance? | Unit test pass chứng minh live E2E pass. | [Project](../01_topics/project-quality-gates.md) |
| Quality gate / score average | Điều kiện chặn đã thỏa hay chỉ có điểm trung bình cao? | Điểm 90 bù được lộ secret hoặc evidence giả. | [Project](../01_topics/project-quality-gates.md) |
| Few-shot / training | Ví dụ trong context hay quá trình cập nhật model? | Thêm ba ví dụ là fine-tune. | [Prompt](../01_topics/prompt-engineering.md) |
| Structured / correct | Parse/validate cấu trúc được hay đúng semantic/source? | JSON hợp lệ là nguồn sự thật. | [Prompt](../01_topics/prompt-engineering.md) |
