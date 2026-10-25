# Thực hành readiness, giao tiếp và kế hoạch sửa lỗ hổng

Đây là bài tự biên soạn phục vụ mục tiêu FPR/MTPTD/FPE/PSFR trong TrainingCalendar, sheet `Training Calendar`, hàng 6–62 và 195–213. Chưa có giáo trình riêng cho bốn module này; không coi bài là đề thi chính thức.

## Bài 1 — Diagnostic trong 45 phút

Đọc rule discount tại [nền tảng QA](../01_topics/qa-foundations.md). Không mở đáp án quiz. Trong 15 phút viết decision table, ba câu hỏi làm rõ dữ liệu và hai rủi ro; trong 15 phút dùng prompt có nguồn để xin phản biện; trong 15 phút review từng đề xuất và ghi quyết định. Đầu ra gồm bản trước/sau, source IDs và một đề xuất rejected/edited hoặc lý do chưa có đề xuất cần loại.

Tiêu chí: đủ bốn tổ hợp, không cộng dồn 25%, không tạo rule chưa duyệt, không dùng dữ liệu thật. Đây là review thiết kế, chưa có runtime verdict.

## Bài 2 — Kế hoạch kiểm thử tối thiểu trong 30 phút

Chọn một luồng login hoặc refund trong tài liệu đúng module. Ghi scope, source version, môi trường/quyền cần có, test ưu tiên, oracle, dataset, cleanup, estimation và exit criteria. Phân biệt thời gian chuẩn bị/chạy/triage. Nếu môi trường thiếu, đánh dấu blocked và đề nghị owner xử lý thay vì tạo ảnh/log giả.

Peer review: người khác phải theo được từ source → scenario → dữ liệu → expected result. Đề xuất đổi rule phải được ghi riêng với người quyết định. Bài nộp là kế hoạch đã review, không phải chứng minh feature pass.

## Bài 3 — Báo trạng thái 60 giây

Tình huống giả lập: 12 ca được lên kế hoạch; đã chạy 9, trong đó 8 pass/1 fail; 3 blocked vì thiếu account đúng role. Viết status theo bốn ý: kết quả/phạm vi, tác động, điều chưa biết, việc tiếp theo có owner. Không gọi đây là số liệu project thật.

Ví dụ: “Theo dataset và build đã ghi trong run record, 9/12 ca đã chạy, 8 pass và 1 fail; 3 ca authorization đang blocked do account. Lỗi refund cần triage vì có thể ảnh hưởng thao tác quản lý. Chưa đủ dữ liệu để đề nghị release. Em sẽ nhờ người quản lý môi trường cấp account rồi chạy phần còn thiếu.”

## Bài 4 — Demo và cải thiện cá nhân

Chọn một artifact đã review và chỉ rõ nó chứng minh được gì. Demo 5 phút: vấn đề → quyết định thiết kế → bằng chứng → hạn chế → bước tiếp theo. Có thể demo mô phỏng nhưng phải ghi nhãn ngay đầu. Chuẩn bị câu trả lời “điều gì khiến em đổi quyết định?” và “em chưa kiểm tra gì?”.

Tự chấm 0/1/2 cho năm năng lực: source fidelity, test design, runtime evidence, AI review và communication. 0 là chưa giải thích được; 1 là giải thích nhưng chưa tự làm; 2 là có artifact tự làm và bảo vệ được. Đây là thang luyện tập tự chọn. Chọn hai điểm yếu nhất, tạo việc sửa có đầu ra quan sát được và ngày tự kiểm tra lại. Không tự nâng điểm chỉ vì đọc xong.

## Checklist nộp bài

- [ ] Có version/scope và nhãn simulated/design-only/live đúng thực tế.
- [ ] Không có secret hoặc dữ liệu người thật.
- [ ] Có residual risk và câu hỏi chưa có đáp án.
- [ ] Người nghe biết việc tiếp theo và người phụ trách.
- [ ] Giải thích được đóng góp của bản thân mà không bịa trải nghiệm.
