# Nền tảng QA và thiết kế kiểm thử

## Mục tiêu và phạm vi

Đọc xong, bạn có thể biến một quy tắc thành tập kiểm thử có lý do, chọn tầng kiểm thử và báo cáo điều chưa được kiểm tra. **Bắt buộc nắm:** test basis, oracle, EP/BVA, decision table, state transition và risk. **Nên hiểu:** phân bổ kiểm thử theo tầng, estimation và monitoring. **Mở rộng:** tự động tính coverage từ mô hình.

TrainingCalendar có FPR và MTPTD nhưng workspace không có giáo trình riêng cho hai module này. Đây là bài cầu nối do người biên soạn xây dựng từ mục tiêu lịch học, phần kỹ thuật của ARTD và bổ sung được ghi nhãn; không phải bản khôi phục giáo trình hay dự báo đề thi.

## Tiên quyết

Không cần kiến thức AI. Cần đọc được một yêu cầu và phân biệt điều được cung cấp với điều mình tự giả định.

## Keyword cần nắm

| Thuật ngữ | Giải thích |
|---|---|
| Test basis — cơ sở kiểm thử | Đây là nguồn dùng để phân tích điều cần kiểm tra, chẳng hạn yêu cầu, business rule hoặc API contract đã được chấp thuận. |
| Test oracle — tiêu chí xác nhận | Đây là căn cứ quyết định kết quả quan sát có đúng hay không; câu trả lời của AI không tự trở thành oracle. |
| Test condition — điều kiện kiểm thử | Đây là một khía cạnh cần xác minh, ví dụ tính đúng của ngưỡng phê duyệt hoàn tiền. |
| Scenario — kịch bản | Đây là tình huống hành vi ở mức khái quát, chưa nhất thiết đủ dữ liệu và bước để thực thi. |
| Test case — ca kiểm thử | Đây là trường hợp cụ thể có tiền điều kiện, dữ liệu, hành động và kết quả có thể xác nhận. |
| Equivalence partitioning (EP) | Đây là cách chia miền dữ liệu thành các nhóm dự kiến có cùng cách xử lý rồi chọn đại diện có lý do. |
| Boundary value analysis (BVA) | Đây là cách tập trung vào ranh giới giữa các miền, nơi sai lệch so sánh thường bộc lộ. |
| Decision table | Đây là bảng ánh xạ các tổ hợp điều kiện sang hành động/kết quả để tránh bỏ sót tổ hợp luật. |
| State transition | Đây là mô hình mô tả sự kiện nào được phép đưa đối tượng từ trạng thái này sang trạng thái khác. |
| Residual risk | Đây là rủi ro còn lại sau các biện pháp kiểm soát và kiểm thử đã chọn, gồm cả phần chủ động hoãn. |

## Bản chất của kiểm thử

**Bổ sung từ nguồn web:** Kiểm thử cung cấp thông tin về chất lượng và rủi ro; không chứng minh phần mềm tuyệt đối không có lỗi. QA chú trọng cách làm việc để phòng ngừa vấn đề, còn testing đánh giá sản phẩm. Static testing xem xét sản phẩm công việc mà không chạy chương trình; dynamic testing quan sát khi chạy. Confirmation testing kiểm tra lỗi đã sửa; regression testing tìm ảnh hưởng ngoài ý muốn của thay đổi. Test level mô tả phạm vi tích hợp của đối tượng; test type mô tả thuộc tính cần đánh giá. Nguồn: [ISTQB CTFL v4.0.1, §§1.1–1.3, 2.2, 3.1](https://istqb.org/?download_id=3345&sdm_process_download=1).

**Ví dụ tự biên soạn:** khi review câu “hoàn tiền nhanh”, bạn tìm ra thiếu tiêu chí trước khi có phần mềm. Khi gọi Refund API và so với rule đã duyệt, bạn đánh giá hành vi đang chạy. Hai việc bổ sung cho nhau: tìm sớm yêu cầu mơ hồ giúp tránh viết hàng loạt test có oracle sai.

## Từ quy tắc đến tập test

Input là rule có phiên bản, miền dữ liệu và rủi ro. Phân tích điều kiện → chọn kỹ thuật → tạo trường hợp → kiểm tra oracle và tính khả thi → output là bộ test truy vết được. Chỉ chạy sau khi môi trường, quyền và dữ liệu sẵn sàng; trường hợp bị chặn phải được báo riêng.

**Ví dụ từ ARTD, Confirmed business rules:** VIP được giảm 10%; campaign hợp lệ được giảm 15%; không cộng dồn mà chọn mức hợp lệ cao nhất.

| VIP | Campaign hợp lệ | Giảm giá theo rule |
|---|---|---|
| Không | Không | 0% |
| Có | Không | 10% |
| Không | Có | 15% |
| Có | Có | 15% |

Dòng cuối quan trọng vì AI có thể đề xuất sai thành 25%. Một test “VIP nhận giảm giá” không đủ kiểm tra quy tắc ưu tiên. Khi giá trị tiền có làm tròn, kiểm tra thêm đúng rule half-up của ARTD; đừng lấy số thực tùy ý làm oracle tài chính.

**Ví dụ BVA từ ARTD Unit 6:** quantity hợp lệ từ 1 đến 10. Chọn 0, 1, 10, 11 để kiểm tra hai phía biên; thêm đại diện trong miền như 5 nếu cần kiểm tra xử lý điển hình. EP cho bạn nhóm hợp lệ/không hợp lệ; BVA giúp chọn điểm sát ranh giới trong các nhóm. Null, missing và sai kiểu có thể là lớp khác, không được coi đã bao phủ chỉ vì có số 0.

**Ví dụ state:** đơn đang chờ thanh toán khác đơn đã thanh toán. Cùng một thao tác refund có thể hợp lệ ở trạng thái này và không hợp lệ ở trạng thái kia. Nếu nguồn chưa định nghĩa timeout chuyển trạng thái ra sao, ghi câu hỏi thay vì tự thêm transition.

## Chọn độ sâu và tầng kiểm thử

ARTD Unit 3 phân biệt product risk với project risk. Mất tiền do thu trùng là rủi ro sản phẩm; không có tài khoản test đúng hạn là rủi ro dự án. Điểm likelihood × impact × exposure chỉ hỗ trợ xếp hạng khi có bằng chứng và thang điểm thống nhất; điểm số không làm biến mất rủi ro bảo mật nghiêm trọng.

**Ví dụ thiết kế bổ sung:** tính giảm giá thuần có thể kiểm tra ở unit; tương tác Order–Payment kiểm tra ở integration; luồng người dùng đi qua UI/API là E2E; acceptance đối chiếu nhu cầu đã thỏa thuận. Không cần đẩy mọi biến thể dữ liệu lên UI. Cần giữ một số luồng xuyên tầng để phát hiện lỗi nối ghép mà unit test không thấy.

Ước lượng bằng cách tách thời gian chuẩn bị dữ liệu, thực thi, phân tích thất bại và cleanup. Dùng quan sát từ một ca đại diện để điều chỉnh ước lượng; ghi rõ giả định về môi trường. Theo dõi số planned/executed/blocked, lỗi quan trọng và coverage theo rủi ro. Nếu có 8 pass, 1 fail và 3 blocked trên 12 ca, không báo “11/12 thành công” vì blocked chưa được xác minh.

## So sánh, bẫy và phỏng vấn

| Dễ nhầm | Cách phân biệt trong ví dụ |
|---|---|
| Số lượng test / coverage | 100 test cùng happy path vẫn bỏ sót quyền refund. |
| Traceability / oracle đúng | Một test có link REQ vẫn có thể mong đợi giảm 25% sai rule. |
| Smoke / regression | Smoke ưu tiên tín hiệu nhanh về khả năng hoạt động; regression theo ảnh hưởng thay đổi. Hai tập có thể giao nhau. |
| Severity / priority | Tác động của lỗi và thứ tự xử lý là hai quyết định khác nhau; tình huống và lịch phát hành ảnh hưởng thứ tự. |
| Exploratory / làm tùy ý | Charter có mục tiêu, thời lượng và bằng chứng; người kiểm thử điều chỉnh bước theo điều học được. Xem ARTD. |

Khi phỏng vấn, giải thích một lựa chọn: “Em sẽ lấy rule giảm giá làm oracle, dùng decision table vì có tổ hợp điều kiện; bổ sung BVA cho quantity và trạng thái cho refund.” Không cần tuyên bố đã làm dự án thật.

## Tự đánh giá

- [ ] Tôi chỉ ra nguồn cho từng expected result và tách assumption khỏi fact.
- [ ] Tôi giải thích vì sao cần dòng VIP + campaign.
- [ ] Tôi tạo được dữ liệu sát hai phía biên và nhận ra missing không phải zero.
- [ ] Tôi phân biệt rủi ro sản phẩm/dự án và nêu phần hoãn kiểm tra.
- [ ] Tôi báo được blocked mà không biến thành pass/fail giả.

## Nguồn và ôn tiếp

- [TrainingCalendar](../../document/QN26_FR_AUT_01_TrainingCalendar_final_version_1.1.xlsx), sheet `Training Calendar`, hàng 6–46: mục tiêu FPR/MTPTD, không có bài giảng chi tiết.
- [ARTD course](<../../document/AIQE AI-Assisted Requirement & Test Design/L3_AIQE_ARTD_course_content.md>), `Confirmed business rules`, Unit 3 Sessions 3.1–3.4, Unit 6 exercise: căn cứ ví dụ và kỹ thuật.
- [Phỏng vấn](../03_interview/qa-foundations.md) · [Tự làm quiz](../04_quiz/qa-foundations.md).
