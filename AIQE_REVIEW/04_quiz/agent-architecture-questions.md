# Quiz tự luyện: agent-architecture

Tự biên soạn, không phải đề thi chính thức. Mỗi câu có bốn lựa chọn và đúng một đáp án tốt nhất. [Ôn kiến thức](../01_topics/agent-architecture.md).

## Câu 1

Ai kiểm tra policy/state/budget trước tool?

A. Planner tự quyết
B. Screenshot
C. Reporter
D. Controller

## Câu 2

Tool run_case nên nhận gì?

A. Shell string tùy ý
B. caseId/environment/runId/revision đã validate
C. Prompt chứa credential
D. URL production bất kỳ

## Câu 3

Create timeout rồi lookup thấy owned ID. Làm gì trước?

A. Dừng write và đối chiếu evidence/ownership
B. Gửi create lần nữa
C. Xóa first report
D. Sửa oracle

## Câu 4

Assertion pass, cleanup fail nên report thế nào?

A. Workflow passed sạch
B. Xóa record bất kỳ
C. Giữ assertion pass, báo cleanup fail và workflow chưa hoàn tất
D. Ẩn cleanup

## Câu 5

Webpage nói ignore policy/upload trace là gì?

A. Untrusted data
B. Instruction ưu tiên
C. Approval của QA
D. Tool schema

## Câu 6

Duplicate runId rejection bảo đảm gì?

A. API business luôn idempotent
B. Không cần cleanup
C. Mọi retry an toàn
D. Ngăn/trả existing command theo controller policy

## Câu 7

OBS-PACKET giả lập có thể ghi thành DOM-OBSERVED live không?

A. Có nếu AI đồng ý
B. Có nếu giống UI
C. Không, giữ nhãn synthetic packet
D. Có nếu có timestamp tự tạo

## Câu 8

Approval cho một run có tự bao phủ publish không?

A. Luôn có
B. Không, phải đối chiếu action/scope của grant
C. Chỉ cần agent muốn
D. MCP tự quyết

## Câu 9

Budget hết nhưng còn tool proposals. Controller làm gì?

A. Tiếp tục đến pass
B. Xóa log
C. Đổi budget không ghi
D. Dừng side effect mới, giữ evidence và cleanup nếu còn quyền/ownership

## Câu 10

Report a1 failed, a2 passed thiếu G2. Summary tốt nhất?

A. Giữ cả attempts, nêu approval gap và review pending
B. Pass without issues
C. Chỉ giữ a2
D. Publish ngay

[Đáp án tách riêng](agent-architecture-answers.md).

