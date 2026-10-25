# Quiz — ci-recovery

10 câu tự biên soạn để ôn tập, không phải đề/đáp án chính thức. Mỗi câu có một phương án tốt nhất. Đọc [bài học](../01_topics/ci-recovery.md); làm xong mới mở [giải thích](./ci-recovery-answers.md).

## Câu 1

PR fork không có live secrets. Lane phù hợp?

- **A.** Cho dùng production account
- **B.** Cho model tự tìm credentials
- **C.** Static/fixture/discovery không dùng lab secrets
- **D.** Skip rồi báo live passed

## Câu 2

Wrapper exit0, selected=0, artifact chỉ install log. Kết luận?

- **A.** Live pass
- **B.** 100% pass vì không failure
- **C.** App fail
- **D.** No execution/false green cần sửa selector/wrapper

## Câu 3

Cron UTC 17 18 * * * tương ứng giờ Việt Nam nào?

- **A.** 01:17 ngày kế tiếp
- **B.** 18:17 cùng giờ địa phương
- **C.** 17:18 ngày kế tiếp
- **D.** 01:17 cùng ngày UTC ghi trong log

## Câu 4

Hai branch ghi cùng isolated-lab. Group theo branch có đủ?

- **A.** Đủ vì Git branch cô lập DB
- **B.** Chưa; phối hợp shared environment và unique namespace
- **C.** Đủ nếu browser context riêng
- **D.** Chỉ cần timestamp đến giây

## Câu 5

Job force-cancel sau write. always() đảm bảo cleanup?

- **A.** Có trong mọi trường hợp
- **B.** Có nếu reporter list
- **C.** Không; cần durable ownership evidence và recovery owner
- **D.** Chỉ cần xóa mọi E2E-* lần sau

## Câu 6

INC-61 match hai Save buttons, chưa click. Fix phù hợp nhất?

- **A.** first()
- **B.** force:true
- **C.** Sleep5s rồi chọn đầu
- **D.** Scope dialog từ DOM card, unique target và condition wait

## Câu 7

Save timeout, authorized exact lookup tìm thấy owned record QA; UI assertion chưa có. Làm gì?

- **A.** Không create lại; tiếp tục read-only oracle/cleanup trong policy
- **B.** Create lần nữa để chắc
- **C.** Report F01 passed ngay
- **D.** Xóa mọi record cũ

## Câu 8

Row trong iframe virtualized list, backend có record. Oracle UI cần gì?

- **A.** Chỉ backend count
- **B.** Scope frame/search rồi assert exact ID và department trong UI
- **C.** Bỏ row check vì list virtualized
- **D.** Dùng substring ID gần giống

## Câu 9

Browser startup exception trước body. Phân loại?

- **A.** App regression chắc chắn
- **B.** Flaky app vì có exception
- **C.** Environment/infrastructure blocked, chưa app assertion
- **D.** Pass nếu retry thứ10 chạy được

## Câu 10

Run X fail a1, pass a2. Nói gì chính xác nhất?

- **A.** Root cause resolved
- **B.** Không cần giữ a1
- **C.** Ổn định production
- **D.** Flaky/pass-after-retry observed; cần triage và fix validation
