# Thuật ngữ Anh–Việt

Bảng tra nhanh, không thay phần giải thích trong bài. Thuật ngữ khóa học giữ nguyên tiếng Anh để luyện phỏng vấn. Nguồn chi tiết và vị trí nội bộ nằm ở bài được liên kết.

| English | Tiếng Việt và nghĩa trong ngữ cảnh AI QE | Bài chính |
|---|---|---|
| Acceptance criteria (AC) | Tiêu chí chấp nhận xác định điều kiện chức năng cần thỏa theo nguồn đã được xác nhận. | [Design](../01_topics/requirement-test-design.md) |
| Ambiguity | Sự mơ hồ cho phép nhiều cách hiểu có hậu quả khác nhau khi thiết kế expected result. | [Design](../01_topics/requirement-test-design.md) |
| Testability | Khả năng kiểm thử thể hiện ở việc có thể kiểm soát điều kiện và quan sát, xác nhận kết quả. | [Design](../01_topics/requirement-test-design.md) |
| Test basis | Cơ sở kiểm thử cung cấp căn cứ để suy ra điều cần kiểm tra. | [QA](../01_topics/qa-foundations.md) |
| Test oracle | Tiêu chí xác nhận giúp đánh giá kết quả quan sát có đúng hay không. | [QA](../01_topics/qa-foundations.md) |
| Test condition | Điều kiện kiểm thử là khía cạnh cần xác minh trước khi cụ thể hóa thành test case. | [QA](../01_topics/qa-foundations.md) |
| Scenario | Kịch bản mô tả một tình huống hành vi hoặc rủi ro cần kiểm tra. | [Design](../01_topics/requirement-test-design.md) |
| Test case | Ca kiểm thử kết hợp tiền điều kiện, dữ liệu, hành động và expected result cụ thể. | [Design](../01_topics/requirement-test-design.md) |
| Traceability | Truy vết duy trì liên hệ giữa nguồn, rủi ro, test, dữ liệu và bằng chứng. | [Design](../01_topics/requirement-test-design.md) |
| Coverage gap | Khoảng trống bao phủ là phần yêu cầu/rủi ro/chiều hành vi chưa được xác minh phù hợp. | [Design](../01_topics/requirement-test-design.md) |
| Equivalence partitioning (EP) | Phân vùng tương đương chia input thành các nhóm dự kiến có xử lý tương tự. | [QA](../01_topics/qa-foundations.md) |
| Boundary value analysis (BVA) | Phân tích giá trị biên tập trung kiểm tra tại và sát ranh giới giữa các miền. | [QA](../01_topics/qa-foundations.md) |
| Decision table | Bảng quyết định ánh xạ tổ hợp điều kiện sang kết quả hoặc hành động. | [QA](../01_topics/qa-foundations.md) |
| State transition | Chuyển trạng thái mô tả thay đổi trạng thái được phép do sự kiện gây ra. | [QA](../01_topics/qa-foundations.md) |
| Pairwise testing | Kiểm thử từng cặp chọn tổ hợp để bao phủ các cặp giá trị, không bảo đảm bao phủ mọi tương tác bậc cao. | [Design](../01_topics/requirement-test-design.md) |
| Risk-based testing | Kiểm thử dựa trên rủi ro phân bổ độ sâu và ưu tiên theo hậu quả và bằng chứng liên quan. | [QA](../01_topics/qa-foundations.md) |
| Residual risk | Rủi ro còn lại là mức phơi nhiễm chưa được loại bỏ sau hoạt động đã chọn. | [QA](../01_topics/qa-foundations.md) |
| Exploratory charter | Định hướng khám phá xác định mục tiêu, phạm vi và thời lượng trong khi cho phép điều chỉnh cách tìm hiểu. | [Design](../01_topics/requirement-test-design.md) |
| Regression testing | Kiểm thử hồi quy tìm hậu quả ngoài ý muốn của thay đổi. | [QA](../01_topics/qa-foundations.md) |
| Confirmation testing | Kiểm thử xác nhận kiểm tra lại vấn đề cụ thể sau khi được sửa. | [QA](../01_topics/qa-foundations.md) |
| Synthetic data | Dữ liệu tổng hợp được tạo cho mục đích kiểm thử và vẫn phải được xác minh an toàn, nhất quán. | [Data](../01_topics/test-data-privacy.md) |
| Masking | Che dữ liệu biến đổi trường nhạy cảm theo mục tiêu bảo vệ nhưng chưa tự chứng minh không thể nhận diện lại. | [Data](../01_topics/test-data-privacy.md) |
| Quasi-identifier | Thuộc tính gần định danh có thể nhận diện cá nhân khi kết hợp với dữ liệu khác. | [Data](../01_topics/test-data-privacy.md) |
| Referential integrity | Toàn vẹn tham chiếu bảo đảm các liên hệ giữa bản ghi tuân thủ ràng buộc định danh. | [Data](../01_topics/test-data-privacy.md) |
| Seed | Giá trị khởi tạo hỗ trợ tái tạo bộ dữ liệu trong cùng thuật toán và phiên bản. | [Data](../01_topics/test-data-privacy.md) |
| Data minimization | Tối thiểu hóa dữ liệu giới hạn dữ liệu thu thập, dùng và lưu ở mức cần cho tác vụ. | [Data](../01_topics/test-data-privacy.md) |
| Severity | Mức nghiêm trọng mô tả tác động của lỗi theo tiêu chí sản phẩm. | [Analysis](../01_topics/defect-api-log-analysis.md) |
| Priority | Độ ưu tiên mô tả thứ tự cần xử lý theo bối cảnh và quyết định nhóm. | [Analysis](../01_topics/defect-api-log-analysis.md) |
| Root-cause hypothesis | Giả thuyết nguyên nhân gốc là lời giải thích cần kiểm chứng, chưa phải nguyên nhân đã xác nhận. | [Analysis](../01_topics/defect-api-log-analysis.md) |
| Correlation ID | Mã tương quan giúp nối sự kiện giữa các thành phần trong cùng hành trình xử lý. | [Analysis](../01_topics/defect-api-log-analysis.md) |
| Idempotency key | Khóa idempotency hỗ trợ nhận diện request lặp theo contract để tránh side effect trùng. | [Analysis](../01_topics/defect-api-log-analysis.md) |
| API contract | Hợp đồng API quy định input, output và hành vi được chấp thuận của giao diện. | [Analysis](../01_topics/defect-api-log-analysis.md) |
| Schema | Lược đồ quy định cấu trúc, kiểu và một số ràng buộc dữ liệu; không tự chứa toàn bộ nghiệp vụ. | [Analysis](../01_topics/defect-api-log-analysis.md) |
| Negative testing | Kiểm thử âm xác minh cách hệ thống xử lý dữ liệu hoặc thao tác không hợp lệ theo contract. | [Analysis](../01_topics/defect-api-log-analysis.md) |
| Authentication | Xác thực kiểm tra danh tính của chủ thể. | [Analysis](../01_topics/defect-api-log-analysis.md) |
| Authorization | Phân quyền xác định chủ thể có được thực hiện hành động lên đối tượng hay không. | [Analysis](../01_topics/defect-api-log-analysis.md) |
| DOM | Mô hình tài liệu của trang không đồng nhất với những gì người dùng nhìn thấy hoặc accessibility tree. | [Locator](../01_topics/playwright-locators.md) |
| Accessible role/name | Vai trò và tên truy cập thể hiện ngữ nghĩa phần tử cho công nghệ hỗ trợ và locator. | [Locator](../01_topics/playwright-locators.md) |
| Locator | Bộ định vị mô tả cách tìm phần tử và có thể được đánh giá lại khi thao tác. | [Locator](../01_topics/playwright-locators.md) |
| Strictness | Tính nghiêm ngặt yêu cầu thao tác đơn phần tử xác định đúng một mục tiêu phù hợp. | [Locator](../01_topics/playwright-locators.md) |
| Test ID | Định danh kiểm thử là hook có chủ sở hữu để định vị ổn định khi phù hợp. | [Locator](../01_topics/playwright-locators.md) |
| Actionability | Điều kiện có thể thao tác là tập kiểm tra readiness tương ứng với action, không phải business oracle. | [Execution](../01_topics/playwright-execution-debugging.md) |
| Auto-wait | Chờ tự động đợi các điều kiện cần cho action theo cơ chế runner. | [Execution](../01_topics/playwright-execution-debugging.md) |
| Web-first assertion | Assertion hỗ trợ retry theo trạng thái trang trong thời hạn cho phép. | [Execution](../01_topics/playwright-execution-debugging.md) |
| Browser context | Ngữ cảnh trình duyệt cung cấp phạm vi session và trạng thái riêng cho kiểm thử. | [Execution](../01_topics/playwright-execution-debugging.md) |
| Fixture | Fixture cung cấp và thu hồi tài nguyên theo lifecycle được runner quản lý. | [Execution](../01_topics/playwright-execution-debugging.md) |
| Trace | Dấu vết thực thi ghi thông tin theo timeline để điều tra đúng run/attempt. | [Execution](../01_topics/playwright-execution-debugging.md) |
| Flaky test | Test không ổn định có kết quả thay đổi giữa các lần chạy trong điều kiện cần được phân tích. | [CI](../01_topics/ci-recovery.md) |
| Prompt | Lời nhắc kết hợp chỉ dẫn và context cho một tác vụ model xác định. | [Prompt](../01_topics/prompt-engineering.md) |
| Grounding | Neo nguồn ràng buộc claim với bằng chứng có thể đối chiếu. | [Prompt](../01_topics/prompt-engineering.md) |
| Hallucination | Đầu ra bịa hoặc thiếu căn cứ có thể được trình bày rất tự tin. | [Prompt](../01_topics/prompt-engineering.md) |
| Few-shot | Vài ví dụ trong context minh họa mẫu output chứ không thực hiện cập nhật trọng số. | [Prompt](../01_topics/prompt-engineering.md) |
| Structured output | Đầu ra có cấu trúc thuận tiện cho validation nhưng chưa chứng minh semantic đúng. | [Prompt](../01_topics/prompt-engineering.md) |
| Human-in-the-loop | Con người tham gia những điểm review và quyết định đã xác định của workflow. | [Prompt](../01_topics/prompt-engineering.md) |
| Planner | Bộ lập kế hoạch đề xuất các bước để đạt goal trong phạm vi context. | [Agent](../01_topics/agent-architecture.md) |
| Controller | Bộ điều khiển cưỡng chế state, policy, quyền và budget trước khi thực hiện bước. | [Agent](../01_topics/agent-architecture.md) |
| Tool adapter | Thành phần chuyển contract đã được kiểm tra sang lời gọi runtime cụ thể. | [Agent](../01_topics/agent-architecture.md) |
| MCP | Model Context Protocol chuẩn hóa cách kết nối công cụ/tài nguyên; không tự cấp quyền nghiệp vụ. | [Agent](../01_topics/agent-architecture.md) |
| Guardrail | Rào chắn giới hạn hành động hoặc dữ liệu và cần cơ chế enforce phù hợp rủi ro. | [Agent](../01_topics/agent-architecture.md) |
| Prompt injection | Chỉ dẫn không đáng tin trong dữ liệu cố làm thay đổi hành vi vượt task hoặc policy. | [Agent](../01_topics/agent-architecture.md) |
| Least privilege | Quyền tối thiểu giới hạn quyền ở mức cần cho task đã cho phép. | [Agent](../01_topics/agent-architecture.md) |
| Checkpoint | Điểm lưu trạng thái hỗ trợ phục hồi với thông tin run/attempt và quyền còn hiệu lực. | [Agent](../01_topics/agent-architecture.md) |
| Reconciliation | Đối soát đọc lại trạng thái có thẩm quyền để làm rõ outcome chưa biết trước khi lặp thao tác ghi. | [CI](../01_topics/ci-recovery.md) |
| Token | Đơn vị xử lý văn bản của model dùng cho giới hạn context và tính usage theo hệ thống. | [Metrics](../01_topics/optimization-metrics.md) |
| Context window | Cửa sổ context giới hạn thông tin có thể tham gia xử lý; không đồng nghĩa trí nhớ đúng và đầy đủ. | [Metrics](../01_topics/optimization-metrics.md) |
| Benchmark | Bộ so sánh có điều kiện, input và tiêu chí cố định để đánh giá thay đổi. | [Metrics](../01_topics/optimization-metrics.md) |
| Cost per accepted run | Chi phí trên run được chấp nhận cần tử số và mẫu số nhất quán với cohort đã công bố. | [Metrics](../01_topics/optimization-metrics.md) |
| Prompt drift | Trôi prompt là thay đổi dẫn đến lệch nguồn, phạm vi hoặc hành vi cần được kiểm soát bằng regression. | [Metrics](../01_topics/optimization-metrics.md) |
| CI | Tích hợp liên tục thực thi kiểm tra theo workflow có version, điều kiện và artifact rõ. | [CI](../01_topics/ci-recovery.md) |
| Quality gate | Cổng chất lượng xác định điều kiện đạt, điều kiện chặn và người quyết định trước khi chuyển giai đoạn. | [Project](../01_topics/project-quality-gates.md) |
| Evidence manifest | Danh mục bằng chứng nối artifact với run, attempt, revision và môi trường. | [Project](../01_topics/project-quality-gates.md) |
| Provenance | Nguồn gốc cho phép truy lại source, công cụ/model, phiên bản và quyết định tạo artifact. | [Project](../01_topics/project-quality-gates.md) |
| ADR | Bản ghi quyết định kiến trúc lưu bối cảnh, lựa chọn và hệ quả để review và bảo trì. | [Project](../01_topics/project-quality-gates.md) |
| Handoff | Bàn giao cung cấp phạm vi, cách vận hành, bằng chứng, hạn chế và owner cho người tiếp nhận. | [Project](../01_topics/project-quality-gates.md) |
