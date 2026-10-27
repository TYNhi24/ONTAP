# 📘 CHỦ ĐỀ 09: BẢNG TRA CỨU THUẬT NGỮ TOÀN DIỆN & BỘ CÂU HỎI SÁT HẠCH FRESHER AIQE

> **Mục tiêu:** Cung cấp từ điển tra cứu nhanh hơn 50+ thuật ngữ kiểm thử & AIQE cốt lõi theo thứ tự A-Z, cùng bộ câu hỏi phỏng vấn / thi sát hạch thực tế kèm câu trả lời mẫu giúp Fresher tự tin vượt qua các kỳ đánh giá năng lực.

---

## 📚 PHẦN 1: TỪ ĐIỂN THUẬT NGỮ KIỂM THỬ & AIQE (A - Z GLOSSARY)

### 🔤 Nhóm 1: Kiểm thử Phần mềm & Nền tảng QA (ISTQB)

1. **Acceptance Criteria (AC):** Tiêu chí chấp nhận - Các điều kiện bắt buộc mà một tính năng phần mềm phải thỏa mãn để được Product Owner hoặc khách hàng nghiệm thu.
2. **Actionability:** Tính khả thi hành động - Trạng thái của phần tử giao diện trong Playwright đảm bảo phần tử đã sẵn sàng để tương tác (visible, enabled, stable, editable, receiving pointer events).
3. **Boundary Value Analysis (BVA):** Phân tích giá trị biên - Kỹ thuật thiết kế kiểm thử hộp đen tập trung vào các ranh giới giữa các phân vùng dữ liệu hợp lệ và không hợp lệ.
4. **Defect Clustering:** Sự tập trung của khiếm khuyết - Nguyên lý cho thấy phần lớn lỗi trong phần mềm thường tập trung tại một số ít module có logic phức tạp nhất.
5. **Defect Life Cycle:** Vòng đời của lỗi - Trình tự các trạng thái mà một lỗi trải qua từ khi được phát hiện (`New`), giao việc (`Assigned`), sửa chữa (`Fixed`), kiểm tra lại (`Retest`), đến khi đóng (`Closed`) hoặc mở lại (`Reopened`).
6. **Defect Triage:** Sàng lọc lỗi - Phiên họp giữa QA, Dev và Product Owner để đánh giá mức độ nghiêm trọng (Severity) và độ khẩn cấp (Priority) của các lỗi mới phát sinh.
7. **Equivalence Partitioning (EP):** Phân vùng tương đương - Kỹ thuật chia tập dữ liệu đầu vào thành các nhóm dữ liệu mà phần mềm xử lý theo cùng một cách thức.
8. **Exploratory Testing:** Kiểm thử khám phá - Phương pháp kiểm thử đồng thời kết hợp giữa việc học hỏi, thiết kế kiểm thử và thực thi bài test mà không cần tài liệu kịch bản cố định.
9. **Heuristic Recovery:** Phục hồi phỏng đoán - Thuật toán xử lý tình huống bất ngờ trên giao diện web (như pop-up quảng cáo, banner che khuất) để đưa test flow trở lại đúng quỹ đạo.
10. **Idempotency:** Tính bất biến / lũy thừa - Tính chất của một hành động hay API mà khi thực hiện một lần hay nhiều lần liên tiếp với cùng tham số thì hệ thống vẫn giữ nguyên một trạng thái duy nhất.
11. **Negative Testing:** Kiểm thử âm tính - Kiểm tra xem phần mềm xử lý các đầu vào sai, không hợp lệ hoặc các tình huống bất thường có chuẩn xác và an toàn hay không.
12. **Positive Testing:** Kiểm thử dương tính - Kiểm tra phần mềm với các dữ liệu hợp lệ trong điều kiện bình thường (Happy Path) để xác nhận tính năng chạy đúng chức năng.
13. **Regression Testing:** Kiểm thử hồi quy - Chạy lại bộ bài test đã có để xác nhận việc sửa code hay cập nhật tính năng mới không làm phát sinh lỗi phụ trên các tính năng cũ.
14. **Requirements Traceability Matrix (RTM):** Ma trận truy xuất nguồn gốc - Bảng đối chiếu hai chiều kết nối từng dòng yêu cầu (Requirement) với các kịch bản kiểm thử (Test Cases) tương ứng.
15. **Root Cause Analysis (RCA):** Phân tích nguyên nhân gốc - Phương pháp điều tra chuyên sâu nhằm xác định nguyên nhân kỹ thuật cốt lõi sinh ra lỗi, phân biệt với triệu chứng bên ngoài.
16. **Sanity Testing:** Kiểm thử hợp lý - Tập hợp bài test hẹp chạy nhanh sau khi nhận bản vá lỗi để xác nhận lỗi cụ thể đó đã được sửa hoàn chỉnh trước khi test sâu hơn.
17. **Smoke Testing:** Kiểm thử khói - Bộ bài test cơ bản nhất chạy ngay khi có build mới nhằm xác nhận các tính năng sống còn của phần mềm hoạt động bình thường.
18. **Test Basis:** Căn cứ kiểm thử - Toàn bộ kho tài liệu, thiết kế, thông số kỹ thuật được dùng làm cơ sở để suy luận và thiết kế bài test.
19. **Test Oracle:** Nguồn chân lý kiểm thử - Tiêu chuẩn khách quan (tài liệu nghiệp vụ, hệ thống cũ, luật pháp) dùng để đối chiếu xem kết quả thực tế (Actual Result) có đúng hay không.
20. **Verification vs Validation:** Thẩm định vs Xác thực - *Verification* kiểm tra phần mềm có được xây dựng đúng theo thiết kế không; *Validation* kiểm tra phần mềm có đáp ứng đúng nhu cầu thực tế của người dùng không.

---

### 🤖 Nhóm 2: AI, LLM & Kỹ thuật Tác tử (AIQE Core)

21. **Agent State Machine:** Máy trạng thái của Agent - Mô hình điều khiển cấu trúc luồng chạy của Agent thành các trạng thái rời rạc và quy định rõ điều kiện chuyển trạng thái.
22. **Chain of Thought (CoT):** Chuỗi suy luận logic - Kỹ thuật thúc đẩy LLM phân tích từng bước logic trước khi đưa ra câu trả lời cuối cùng nhằm tăng độ chính xác trong kiểm thử.
23. **Circuit Breaker:** Cầu dao ngắt tự động - Rào chắn an toàn tự động ngắt hoạt động của Agent khi phát hiện vượt ngưỡng số bước lặp, vượt thời gian timeout hoặc lỗi lặp lại liên tục.
24. **Context Window:** Cửa sổ ngữ cảnh - Dung lượng bộ nhớ tối đa tính theo đơn vị token mà mô hình LLM có thể tiếp nhận và ghi nhớ trong một phiên làm việc.
25. **Correlation ID:** Mã định danh tương quan - Chuỗi mã định danh duy nhất truyền qua tất cả các microservices để xâu chuỗi toàn bộ nhật ký log của một giao dịch người dùng.
26. **Deterministic Controller:** Bộ điều khiển tất định - Đoạn code truyền thống bọc ngoài LLM nhằm đảm bảo các hành động của Agent được điều phối theo quy tắc cố định, không phụ thuộc vào may rủi.
27. **Evidence Boundary:** Ranh giới bằng chứng - Quy tắc bắt buộc không được suy diễn vượt quá những gì được ghi lại cụ thể trong log hoặc mã lỗi của hệ thống.
28. **Fault Injection:** Tiêm lỗi có kiểm soát - Chủ động gây ra các sự cố mạng hoặc dữ liệu để đánh giá khả năng tự phục hồi và độ bền bỉ của kịch bản kiểm thử.
29. **Few-shot Prompting:** Lời nhắc kèm ví dụ mẫu - Cung cấp từ 1 đến vài cặp ví dụ (Input ➔ Output mẫu) trong prompt để định hình câu trả lời mong muốn cho AI.
30. **Flaky Test:** Bài test chập chờn - Bài test tự động có kết quả không ổn định (lúc Pass, lúc Fail) dù mã nguồn không thay đổi.
31. **Grounding:** Neo thông tin - Ràng buộc LLM chỉ được phép trả lời dựa trên các dữ liệu thực tế do người dùng cung cấp, ngăn chặn hiện tượng bịa đặt thông tin.
32. **Hallucination:** Hiện tượng ảo giác - Hiện tượng mô hình ngôn ngữ lớn đưa ra thông tin hoàn toàn sai lệch nhưng được diễn đạt rất tự tin và trôi chảy.
33. **Human Approval Gate:** Cổng phê duyệt của con người - Điểm dừng trong quy trình tự hành mà Agent bắt buộc phải dừng lại chờ xác nhận từ con người trước khi thực hiện hành động rủi ro.
34. **Least Privilege:** Nguyên tắc đặc quyền tối thiểu - Chỉ cấp cho AI Agent những quyền hạn và công cụ tối thiểu vừa đủ để hoàn thành bài test được giao.
35. **Model Context Protocol (MCP):** Giao thức ngữ cảnh mô hình - Chuẩn kết nối mở giúp AI Agent dễ dàng gọi các công cụ kiểm thử bên ngoài (như Playwright Browser).
36. **Page Object Model (POM):** Mô hình đối tượng trang - Mẫu kiến trúc tách biệt giữa cấu trúc các phần tử trang web và kịch bản kiểm thử tự động.
37. **Personally Identifiable Information (PII):** Dữ liệu định danh cá nhân - Dữ liệu nhạy cảm của người dùng (CCCD, SĐT, Số thẻ, Email) bắt buộc phải che chắn (Masking) trước khi gửi cho AI.
38. **Prompt Drift:** Trôi dạt lời nhắc - Sự suy giảm chất lượng hoặc thay đổi hành vi đầu ra của prompt theo thời gian khi nhà cung cấp nâng cấp mô hình AI ngầm định.
39. **ReAct Pattern:** Mẫu hình Suy luận & Hành động - Kiến trúc kết hợp vòng lặp giữa Suy luận (Reasoning) và Thực thi công cụ (Acting) của Agent.
40. **Synthetic Test Data:** Dữ liệu kiểm thử nhân tạo - Dữ liệu được sinh bằng thuật toán/AI có đặc tính tương đương dữ liệu thật nhưng không thuộc về bất kỳ người dùng có thật nào.
41. **Trust Boundary:** Ranh giới tin cậy - Ranh giới bảo mật phân chia giữa vùng dữ liệu không an toàn (đầu vào từ người dùng/AI) và vùng lõi hệ thống thực thi.
42. **Web-First Assertions:** Khẳng định web bất đồng bộ - Lệnh kiểm tra trong Playwright tự động chờ đợi và thử lại cho đến khi điều kiện mong đợi xuất hiện trên trang.

---

## 🎯 PHẦN 2: BỘ CÂU HỎI PHỎNG VẤN & SÁT HẠCH THỰC CHIẾN CHO FRESHER AIQE

### ❓ Câu 1: Sự khác biệt lớn nhất giữa một Manual Tester truyền thống, một Automation QA và một AI Quality Engineer (AIQE) là gì?
> **Trả lời mẫu:**
> * **Manual Tester:** Tập trung đọc tài liệu yêu cầu thủ công, thiết kế test case trên bảng tính và thực hiện thao tác kiểm thử trực tiếp bằng tay trên giao diện.
> * **Automation QA:** Viết mã nguồn (code) kịch bản để máy tính tự động hóa việc lặp lại các bài test theo một kịch bản tất định cố định.
> * **AIQE (AI Quality Engineer):** Nâng cấp lên tầng cao hơn: ứng dụng AI/LLM để phân tích yêu cầu, phát hiện lỗ hổng nghiệp vụ, tự động sinh BDD/Test Case, xây dựng các **AI Testing Agents** có khả năng tự suy luận, tự thích ứng với thay đổi của giao diện và ứng dụng AI để phân tích nguyên nhân gốc (RCA) từ hàng triệu dòng log phân tán.

---

### ❓ Câu 2: Trong Playwright, tại sao locator `page.getByRole('button', { name: 'Submit' })` lại luôn được ưu tiên hơn `page.locator('.btn-submit')` hoặc XPath?
> **Trả lời mẫu:**
> Locator chuẩn Accessibility (`getByRole`) phản ánh trực tiếp cách mà người dùng thật và các công cụ trợ năng tương tác với trang web. Nó mang tính **bền vững cao (resilient)** trước các thay đổi về mặt kỹ thuật code:
> * Khi lập trình viên đổi framework CSS, đổi class từ `.btn-submit` sang class tiện ích của Tailwind như `.bg-blue-500`, hoặc thay đổi cấu trúc thẻ HTML lồng nhau, kịch bản dùng `getByRole` vẫn **hoạt động 100% không bị gãy**.
> * Trái lại, XPath hoặc CSS Class thường gắn chặt vào chi tiết kỹ thuật nội bộ, rất dễ vỡ (brittle) và gây ra chi phí bảo trì kịch bản tự động hóa cực lớn.

---

### ❓ Câu 3: Hiện tượng Hallucination của AI là gì? Bạn làm thế nào để đảm bảo AI không sinh ra các test case "ảo" sai lệch với thực tế dự án?
> **Trả lời mẫu:**
> * **Bản chất:** Hallucination là hiện tượng LLM tự bịa đặt ra các tính năng, tham số API hoặc quy tắc nghiệp vụ không hề tồn tại do cơ chế dự đoán xác suất từ ngữ.
> * **Biện pháp ngăn chặn của AIQE:**
>   1. **Áp dụng Grounding nghiêm ngặt:** Đính kèm trực tiếp tài liệu yêu cầu (PRD/API Contract) vào prompt và chỉ thị rõ ràng: *"Chỉ được sử dụng dữ liệu trong tài liệu đính kèm, tuyệt đối không tự suy diễn"*.
>   2. **Đặt Guardrail cấm đoán:** Ép AI tạo riêng danh sách các *"Câu hỏi làm rõ (Clarification Questions)"* thay vì tự ý giả định câu trả lời khi gặp điểm mơ hồ.
>   3. **Nguyên tắc Human-in-the-Loop (HITL):** Mọi kịch bản do AI sinh ra bắt buộc phải có QA đọc thẩm định và phê duyệt trước khi đưa vào test suite chính thức.

---

### ❓ Câu 4: Hãy giải thích nguyên tắc "Tách pha" (Phasing Separation) khi tích hợp kịch bản kiểm thử vào hệ thống CI/CD?
> **Trả lời mẫu:**
> Quy trình CI/CD đòi hỏi tốc độ nhanh, chi phí thấp và tính ổn định tuyệt đối (Deterministic). Do đó ta tách thành 2 pha rõ rệt:
> * **Pha 1 - Preparation Phase (Pha ngoại tuyến có AI):** Dùng AI Agent hỗ trợ viết code test, tối ưu prompt, phân tích rủi ro. Pha này chạy trên máy local của QA hoặc server phân tích riêng. Khi kịch bản đã chuẩn, code được compile và commit vào Git.
> * **Pha 2 - Execution Phase (Pha thực thi trên CI):** Khi chạy trên GitHub Actions CI, bài test được thực thi 100% bằng Playwright Test Runner ở chế độ Headless cố định, **hoàn toàn không gọi API ra các mô hình LLM bên ngoài**. Điều này loại bỏ rủi ro mạng lag, tiết kiệm chi phí token và đảm bảo thời gian chạy CI ổn định dưới 15 phút.

---

### ❓ Câu 5: Khi phân tích một lỗi người dùng bị trừ tiền hai lần (Duplicate Charge), bạn sẽ điều tra những yếu tố kỹ thuật nào để tìm ra Root Cause thay vì chỉ nhìn vào giao diện UI?
> **Trả lời mẫu:**
> Để tìm nguyên nhân gốc (Root Cause):
> 1. **Dùng Correlation ID:** Lấy mã giao dịch từ request của khách hàng và truy vết ngược trên toàn bộ log của API Gateway, Order Service và Payment Gateway.
> 2. **Kiểm tra Lỗi mạng & Timeout:** Xem xét có sự xuất hiện của `SocketTimeoutException` giữa hệ thống và cổng thanh toán ngân hàng hay không.
> 3. **Kiểm tra tính Idempotency:** Đối chiếu xem backend khi thực hiện cơ chế Retry có truyền kèm `Idempotency-Key` sang ngân hàng hay không. Nếu không có key này, phía ngân hàng sẽ xử lý lần gọi thứ hai như một giao dịch rút tiền mới, dẫn đến lỗi trừ tiền kép.
> 4. **Khẳng định bằng chứng (Evidence Boundary):** Chỉ kết luận lỗi do logic Retry thiếu Idempotency khi trích dẫn được chính xác dòng log ghi nhận 2 giao dịch độc lập được gửi sang cổng thanh toán.

---

### ❓ Câu 6: Trong kiến trúc AI Agent, tại sao phải có "Deterministic Controller" bọc bên ngoài "LLM Core"?
> **Trả lời mẫu:**
> Mô hình LLM bản chất là xử lý ngôn ngữ mang tính xác suất (Probabilistic). Nếu để Agent tự do 100%, Agent có thể:
> * Tự ý nhảy cóc qua bước xác thực hoặc kiểm tra form.
> * Rơi vào vòng lặp vô tận (Infinite loop) khi gặp lỗi giao diện, làm cháy ngân sách token.
> * Tự ý thực hiện các hành động phá hoại dữ liệu (như xóa hàng loạt bản ghi).  
> **Deterministic Controller** đóng vai trò là "chiếc khung sắt" bọc ngoài: nó quản lý Máy trạng thái (State Machine), kiểm soát rào chắn an toàn (Guardrails), giới hạn ngân sách thời gian (Timeout budget) và kích hoạt Cổng phê duyệt của con người (Human Approval Gate) khi gặp các thao tác nguy hiểm.

---

### ❓ Câu 7: Bạn xử lý một bài test bị "Flaky" trên hệ thống CI như thế nào?
> **Trả lời mẫu:**
> Quy trình chuẩn 3 bước:
> 1. **Điều tra nguyên nhân gốc:** Mở file `trace.zip` trong Playwright Trace Viewer để tua lại video, soi DOM Snapshot trước/sau thao tác click và kiểm tra Network Tab xem có API nào bị trễ hay không.
> 2. **Sửa đổi mã nguồn:**
>    * Nếu do phần tử chưa kịp xuất hiện: Thay thế toàn bộ hardcoded sleep bằng Web-First Assertions (`await expect(locator).toBeVisible()`).
>    * Nếu do xung đột dữ liệu: Tạo dữ liệu kiểm thử động kèm UUID/Timestamp ngẫu nhiên để các bài test chạy song song không tranh chấp dữ liệu.
>    * Nếu do phần tử bị che khuất: Dùng locator chuẩn trợ năng `getByRole` để đợi đúng trạng thái Actionability.
> 3. **Kiểm chứng độ ổn định:** Dùng cờ `--repeat-each=20` để chạy liên tiếp 20 lần bài test trên môi trường CI. Nếu đạt 20/20 Pass thì mới gỡ nhãn flaky và merge code.

---

## 💡 PHẦN 3: LỜI KHUYÊN DÀNH CHO FRESHER ĐỂ ĐẠT ĐIỂM XUẤT SẮC

1. **Luôn nói bằng Bằng chứng (Evidence-driven Mindset):** Khi trả lời phỏng vấn hoặc giải trình lỗi với khách hàng, luôn dẫn chứng bằng log file, mã lỗi HTTP, ảnh chụp màn hình hoặc file Trace Viewer.
2. **Không học vẹt câu lệnh:** Hãy nắm chắc chuỗi tư duy **Input ➔ Process ➔ Output**. Khi hiểu rõ dữ liệu đầu vào cần gì và tiêu chí nghiệm thu đầu ra là gì, bạn sẽ tự tin xử lý mọi tình huống thi cử.
3. **Thực hành viết Prompt có cấu trúc:** Luyện tập thói quen viết prompt chuẩn 5 thành phần (Role, Context, Test Basis, Guardrails, Output Format). Đây là kỹ năng phân biệt một kỹ sư AIQE chuyên nghiệp với người dùng AI thông thường.

