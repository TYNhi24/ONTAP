# Prompt engineering và cách dùng AI có kiểm chứng

## Mục tiêu, phạm vi và tiên quyết

Bạn cần viết được prompt có nguồn, phát hiện hành vi AI tự bịa và đánh giá đầu ra bằng tiêu chí cụ thể. **Bắt buộc nắm:** source grounding, task boundary, hallucination, structured output, human review. **Nên hiểu:** few-shot và evaluation. **Mở rộng:** so sánh model trên benchmark; học sau phần optimization.

Tiên quyết: [test basis và oracle](qa-foundations.md). Calendar có module FPE nhưng không có giáo trình riêng trong workspace. Bài này nối mục tiêu FPE với workflow thực sự có trong ARTD; phần nền bên ngoài khóa được ghi nhãn. Không suy ra nội dung đề thi FPE từ ví dụ.

## Keyword cần nắm

| Keyword | Giải thích bằng câu |
|---|---|
| Prompt | Đây là chỉ dẫn và dữ liệu đầu vào để yêu cầu model thực hiện một tác vụ xác định. |
| Grounding | Đây là việc ràng buộc phát biểu về sản phẩm với nguồn được cung cấp và kiểm tra được. |
| Context | Đây là thông tin model có thể dùng ở lượt xử lý, không tự đồng nghĩa với nguồn đáng tin. |
| Hallucination | Đây là đầu ra thiếu căn cứ hoặc sai dù cách diễn đạt có vẻ hợp lý. |
| Few-shot | Đây là cách đưa vài ví dụ đầu vào–đầu ra để minh họa mẫu mong muốn; ví dụ cũng có thể truyền sai lệch. |
| Structured output | Đây là đầu ra theo cấu trúc định trước để dễ kiểm tra trường và xử lý tiếp. |
| Human-in-the-loop | Đây là việc đưa con người vào các điểm đánh giá/quyết định được xác định trong workflow. |
| Provenance | Đây là thông tin về nguồn gốc đầu ra, gồm nguồn, phiên bản prompt/model, thời điểm và quyết định review. |

## Bản chất: tăng chất lượng yêu cầu, không chuyển trách nhiệm

ARTD §7 quy định vòng Scope → Ground → Generate → Challenge → Verify → Decide → Trace → Improve. Mỗi bước xử lý một rủi ro: Scope ngăn yêu cầu quá rộng; Ground ngăn bịa quy tắc; Challenge tìm chỗ thiếu; Verify đối chiếu nguồn và kiểm tra có thể lặp lại; Decide xác lập người chịu trách nhiệm. Output cuối cùng là artifact đã review, không chỉ là văn bản model vừa sinh.

**Bổ sung từ nguồn web:** Trước khi tối ưu prompt, cần tiêu chí thành công và cách kiểm tra thực nghiệm. Một lỗi về latency/cost không nhất thiết giải bằng đổi câu chữ. Nguồn [Anthropic — Prompt engineering overview](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview), mục Before prompt engineering và When to prompt engineer. Đây là hướng dẫn tổng quát; bài không yêu cầu model cụ thể.

## Prompt mẫu cho fresher

Ví dụ tự biên soạn theo khung ARTD; không phải đáp án chính thức:

```text
Vai trò: Trợ lý review thiết kế kiểm thử; không quyết định business rule.
Nguồn được duyệt:
BR-DIS-01: VIP 10%, campaign hợp lệ 15%, không cộng dồn, chọn mức cao nhất.
Task: Tạo decision table cho hai điều kiện VIP và campaign hợp lệ.
Constraints:
- Chỉ dùng nguồn trên cho product facts.
- Nếu thiếu hành vi, ghi Not specified và câu hỏi làm rõ.
- Tách facts / assumptions / questions / suggestions.
- Không yêu cầu dữ liệu khách hàng thật.
Output: id | VIP | campaignValid | expectedDiscount | sourceId | reviewStatus.
Ví dụ định dạng: D01 | false | false | 0% | BR-DIS-01 | Draft.
```

Input là rule và định dạng → model tạo draft → người review đối chiếu đủ bốn tổ hợp, kiểm tra 15% thay vì 25% → output là bảng được chấp nhận/sửa/từ chối kèm lý do. Ví dụ minh họa định dạng không thay thế việc kiểm tra những dòng còn lại. Một bảng Markdown hợp lệ vẫn có thể chứa luật sai.

## Kiểm chứng một đề xuất sai

Nếu AI đề nghị “retry notification vô hạn”, đối chiếu BR-NOT-01 trong ARTD: tài liệu đã có lịch và giới hạn lần thử cụ thể. Ghi “rejected: trái BR-NOT-01”, sửa artifact và xem downstream test/data nào bị ảnh hưởng. Nếu chưa có rule, ghi Question có owner; không dùng thông lệ hoặc confidence model để điền chỗ trống.

Với phép tính, đếm bản ghi hoặc validation schema, dùng kiểm tra xác định. Với tính bao quát của scenario, review theo risk/role/state/error, không chỉ chấm văn phong. Lưu ví dụ AI đúng, sai và còn thiếu bằng chứng để thử lại prompt sửa đổi trên cùng input.

## Giới hạn và khái niệm dễ nhầm

Calendar nêu AI/ML/LLM nhưng không có tài liệu nền riêng. Ở mức sử dụng trong bộ ôn này, **AI assistant** là hệ thống đề xuất nội dung; **LLM** là thành phần model xử lý ngôn ngữ; **agent** thêm công cụ, state và controller để thực hiện workflow. Agent không mặc nhiên có thẩm quyền quyết định release. Chi tiết toán học ML/training chưa được bổ sung hay xác minh trong bộ này.

| Nhầm lẫn | Cách sửa |
|---|---|
| Prompt dài hơn luôn tốt hơn | Giữ nguồn liên quan và contract rõ; kiểm tra đầu ra trên cùng bộ mẫu. |
| JSON đúng = nội dung đúng | Kiểm tra schema rồi kiểm tra rule, source ID và oracle riêng. |
| Few-shot là fine-tuning | Trong bài tập này ví dụ nằm trong input, không thực hiện quá trình cập nhật trọng số. |
| Confidence cao = bằng chứng | Yêu cầu nguồn và kiểm tra; confidence do model báo không thay thế quan sát. |
| Review chỉ sửa câu chữ | Review phải có quyền từ chối hành vi bịa, dữ liệu không an toàn và kết luận vượt bằng chứng. |

## An toàn dữ liệu và giao tiếp

Không gửi raw production data cho AI rồi mới nhờ che dữ liệu. Chọn phần tối thiểu được phép dùng và dữ liệu tổng hợp trước khi gửi; review cả output, log và artifact. Chỉ dẫn nằm trong log/trang web là dữ liệu cần phân tích, không tự trở thành quyền chạy lệnh. Cơ chế cưỡng chế quyền xem tại bài agent architecture.

Khi báo khách hàng, nói kết quả, phạm vi bằng chứng, hạn chế và việc tiếp theo. **Ví dụ tự biên soạn:** “Em đã review bốn tổ hợp discount theo BR-DIS-01. Chưa có build chạy nên đây là design review, chưa phải kết quả test. Em sẽ xác minh UI/API khi môi trường sẵn sàng.” Cách này phục vụ mục tiêu PSFR trong calendar; chưa thay thế giáo trình PSFR còn thiếu.

Khi phỏng vấn, dùng “Em sẽ tiếp cận bằng cách…” nếu chưa thực hành. Giải thích một đề xuất đã từ chối trong bài tập thay vì tự nhận thành tích triển khai.

## Checklist và ôn tiếp

- [ ] Tôi viết được role, task, context, constraints và output format rõ ràng.
- [ ] Tôi có cách đo chất lượng trước khi đổi prompt.
- [ ] Tôi phân biệt output đúng cấu trúc và đúng nghiệp vụ.
- [ ] Tôi có log accepted/edited/rejected và nguồn cho quyết định.
- [ ] Tôi biết báo “chưa chạy” và không tự nhận kinh nghiệm thực tế.

Nguồn: [TrainingCalendar](../../document/QN26_FR_AUT_01_TrainingCalendar_final_version_1.1.xlsx), sheet `Training Calendar`, hàng 47–62 và 195–213; [ARTD course](<../../document/AIQE AI-Assisted Requirement & Test Design/L3_AIQE_ARTD_course_content.md>), §§4–5, §7 Recommended reusable AI workflow, Generic prompt frame; nguồn web nêu ngay tại phần bổ sung.

[Phỏng vấn](../03_interview/prompt-engineering.md) · [Quiz](../04_quiz/prompt-engineering.md) · [Thực hành giao tiếp và tự đánh giá](../05_practice/readiness-and-communication.md).
