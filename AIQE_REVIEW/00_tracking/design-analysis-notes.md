# Nhật ký đọc và phủ nội dung: ARTD và DALA

## Sửa lỗi ledger và phương pháp

Bản này thay ledger lỗi. Ledger trước ghép sai path/hash vì dùng vị trí mảng sau khi corpus tái trích xuất thêm file; PowerShell stdin cũng làm mất dấu ở văn bản mới. Bản hiện tại viết bằng apply_patch và tra nguồn theo **đường dẫn**, không theo index.

Output các lần đọc trong hội thoại xác nhận đúng nội dung đã đọc: DALA EN có mục Unit 1–6 và seed duplicate charge, DALA VI mở bằng “Phân tích lỗi, API và log”, ARTD MD/DOCX có source pack/CR-01 và EX-U1-RQA tới EX-U6-DATA, hai deck có đủ slide1–24 và notes1–24. Các lần đọc này diễn ra khi chúng còn ở index 58–64; output có đúng tên hoặc nội dung mục tương ứng. Chỉ bước tạo ledger cuối bị index drift. Không dùng bản ledger cũ hay lời kiểm tra hash theo index cũ làm bằng chứng.

Đọc MD toàn văn, DOCX paragraph/table text trích xuất và PPTX slide/notes XML. Extraction không đồng nghĩa đã xem render. Không sửa file gốc. Không dùng web; nội dung sản phẩm từ khóa học, ví dụ và câu hỏi là tự biên.

## Bảy nguồn đúng, hash và đơn vị đã đọc

Các khoảng ký tự theo Python: đầu bao gồm, cuối không bao gồm. Đây là độ dài text, không phải byte của file.

| Đường dẫn | SHA-256 | Đơn vị đã đọc |
|---|---|---|
| `document/AIQE AI-Assisted Defect, API & Log Analysis/L3_AIQE_DALA_course_content.md` | `3904a4fe1fd6601881878614d12247f49d459e23373e7e750d80b6aa435b4dd1` | 1 unit, 66923 ký tự; [0:18000), [18000:42000), [42000:66923); mục1–13, Unit1–6, bài tập/rubric/templates. |
| `document/AIQE AI-Assisted Defect, API & Log Analysis/L3_AIQE_DALA_course_content_vi.md` | `193c4bae46e17eac24543ce6966234f1166f875f2161a1a020b528dc85da9c96` | 1 unit, 67125 ký tự; [0:23000), [23000:45000), [45000:67125); mục1–13, Học phần1–6. |
| `document/AIQE AI-Assisted Defect, API & Log Analysis/L3_AIQE_DALA_exercises.md` | `270c6e2d28e2d53c4e278af9fda51be47156d81a71d0ffe0ebc2a7c26a87e3a9` | 1 unit, 11534 ký tự; toàn văn EX-U1-DEFECT tới EX-U6-INTEGRATED, instructions/minimum/rubric/critical caps. |
| `document/AIQE AI-Assisted Requirement & Test Design/L3_AIQE_ARTD_course_content.md` | `782bceb9e6a000979c6a2212302542abdb9897b3231cf49d9992f5a1af75acee` | 1 unit, 81298 ký tự; [0:28000), [28000:56000), [56000:81298); source pack, Unit1–6, assessment/capstone/workflow/tooling. |
| `document/AIQE AI-Assisted Requirement & Test Design/L3_AIQE_ARTD_exercises.docx` | `72a7da469852fb6213b5ff3fd91b25cf09a595e89fa3fc1e21703a861b5fab02` | 1 unit, 49453 ký tự; [0:25000), [25000:49453); source pack, sáu bài tập, assessment/capstone/workflow. |
| `document/AIQE AI-Assisted Requirement & Test Design/L3_AIQE_ARTD_training_deck_ready_v2.pptx` | `4fd328cf350f27e4e5cf2cd1f8d31e1cfd0371b8af9d2eabf2d03483f647d1a8` | Đủ 48 units, 11302 ký tự: ppt/slides/slide1.xml–slide24.xml và ppt/notesSlides/notesSlide1.xml–notesSlide24.xml. |
| `document/AIQE AI-Assisted Requirement & Test Design/L3_AIQE_ARTD_training_deck_vi_final.pptx` | `4e040b04aa818b66057e0270cbcf36b2eb249bb20370d41c3bb4ae0002fb4740` | Đủ 48 units, 12468 ký tự: ppt/slides/slide1.xml–slide24.xml và ppt/notesSlides/notesSlide1.xml–notesSlide24.xml. |

DALA EN lần đầu bị wrapper cắt phần giữa; đã đọc lại [18000:42000) và [42000:end) qua output plain để bù. Lần đầu chuyển sang VI lỗi console encoding; đã đặt PYTHONIOENCODING=utf-8 và đọc VI đủ ba khối. ARTD MD/DOCX chia khối liên tục. Speaker notes hai deck đã đọc đủ.

## Hình ảnh và render

Root đã xem 7 PNG unique trong 11 media của mỗi deck; hai deck có media giống byte, quan hệ nằm trong media-map.json. Theo root, phần lớn là nền/decorative grids; artwork slide17 inputs→scenario cards, slide18 settings/data/steps/result, slide23 privacy transform valid/invalid/warnings, không có normative labels đọc được. Tôi không tự xem PNG, nhận kết quả quan sát từ root; contact sheet không chạy do thiếu Pillow. PowerPoint COM render lỗi 80070520 theo root; native shape layout/chart, overlap, màu và accessibility chưa kiểm chứng. Không khẳng định đã xem slides render.

## Conflict và gap

| Vấn đề/nguồn | Cách xử lý |
|---|---|
| ARTD MD/DOCX Interface and data constraints: 201/PENDING_PAYMENT đối lập process note chỉ có order sau paid | Giữ conflict, hỏi owner, không lấy DALA sửa. |
| DALA EN/VI 5.3: 201/PAID và 202/PAYMENT_PENDING | Ghi baseline DALA riêng. |
| DALA 5.3 UUID headers đối lập seed5.4 corr-7a01/idem-b91f | Giữ ID gốc trong evidence; request mới dùng UUID hợp lệ, ghi fixture mismatch. |
| DALA VI5.3 dịch 400 thành “Xác thực request thất bại”; EN là “Request validation failed” | Diễn giải validation input, phân biệt authentication401. |
| ARTD slide16 L×I; EX-U3-SCENARIO instruction5 L×I×E | Phân biệt minh họa và rubric, không trộn thang. |
| ARTD slide13 chỉ nêu bốn coverage states, Session2.1 có Blocked/Not testable | Dạy đủ năm theo course. |
| DALA5.3 same-key/different-payload và GET cross-customer403/404 chưa quy định | Ghi Not specified; không tự chọn409/403/404. |
| ARTD CR-01 thiếu cumulative approval/allocation/rounding/state/concurrency | Questions và impact; không biến simulation outcome thành approved rule. |
| ARTD BR-REF-01 và refundReason thiếu cutoff/timezone/định nghĩa cách đếm Unicode chi tiết | Nêu câu hỏi boundary, không tự chọn. |
| DALA EX-U3-LOGS/control batch và runtime không có gói đầy đủ để chạy | Không bịa parser counts/anomaly counts/execution. |

## Mapping nguồn tới topic

| Nguồn | Đích trong 01_topics | Nội dung |
|---|---|---|
| ARTD Unit1, EX-U1-RQA, slides11–12/notes | requirement-test-design mục1 | Testability, decomposition, ambiguity/conflict, clarification, proposed rewrite. |
| ARTD Unit2, EX-U2-TRACE, slides13–14/notes | requirement-test-design mục2 | Coverage states, false links, obsolete COD, CR-01 direct/indirect impact. |
| ARTD Unit3, EX-U3-SCENARIO, slides15–17/notes | requirement-test-design mục3 | EP/BVA, decision/state, pairwise limit, risk score, budget/residual risk. |
| ARTD Unit4, EX-U4-CASES, slides18–19/notes | requirement-test-design mục4 | Executable cases, oracle, observation layer, cleanup, automation readiness. |
| ARTD Unit5, EX-U5-EXPLORE, slides20–21/notes | requirement-test-design mục5 | Charter/checklist/script, timebox/pivot/evidence/debrief, simulation. |
| ARTD Unit6, EX-U6-DATA, slides22–23/notes | test-data-privacy toàn bài | Dictionary, boundaries, FK/invariants, masking/synthetic/linkage, validation/reproducibility/operations. |
| ARTD metadata, responsible AI, assessment/capstone/workflow, slides1–10/24 và notes | Mở đầu/nguồn/checklist của topics | Scope fresher so Advanced, human accountability, evidence chain; course weights do root tích hợp. |
| DALA Unit1, EX-U1-DEFECT | defect-api-log-analysis mục1 | Report, reproducibility, severity/priority/lifecycle. |
| DALA Unit2, EX-U2-RCA | defect-api-log-analysis mục2 | Evidence classes/confidence/falsification/confirmation. |
| DALA Unit3, EX-U3-LOGS | defect-api-log-analysis mục3 | UTC/reliability/multi-ID/timeline/anomaly/absence caveat. |
| DALA Unit4, EX-U4-API-FOUNDATION | defect-api-log-analysis mục4 | HTTP/auth/schema/semantics/side effects/contracts/setup/cleanup. |
| DALA Unit5, EX-U5-API-SCENARIOS | defect-api-log-analysis mục5 | Negative non-effects, retry/idempotency/unknown outcome/resilience/concurrency. |
| DALA Unit6, EX-U6-INTEGRATED, capstone/templates | defect-api-log-analysis mục5/checklist | Cross-layer package, regression/observability, preservation, stakeholder confidence. |

Cuối mỗi topic có relative links và exact heading/slide/notes. Không gọi trainer outcome là kết quả thực thi của người học.

## Từ khóa để hợp nhất glossary

Định nghĩa đầy đủ nằm trong bảng Từ khóa của ba topics.

- requirement-test-design: requirement, acceptance criterion, business rule, testability, oracle, ambiguity, traceability, condition/scenario/case, equivalence partitioning, boundary value analysis, decision table, state transition, residual risk, charter.
- test-data-privacy: synthetic data, data dictionary, expected-valid/invalid, referential integrity, business invariant, direct/quasi-identifier, masking, pseudonymization, tokenization, deterministic validation, reproducibility.
- defect-api-log-analysis: defect report, severity, priority, authentication/authorization, API contract, schema validation, semantic assertion, side effect, idempotency, reconciliation, correlation/request/entity ID, clock skew, hypothesis, root cause.

## Bộ tự luyện và giới hạn

Mỗi topic có 5 interview questions (intent, khung30–60 giây, follow-up, common mistake) trong 03_interview; 8 MCQs/4 options/1 best trong 04_quiz, answers file riêng giải thích đủ A/B/C/D. Tổng15 interview,24 MCQs,96 option explanations, đều tự biên. Ví dụ thực hành/self-check có trong topics, 05_practice do root tích hợp.

Không chạy API/parser trên môi trường thật. Ví dụ tiền/timing có kiểm tra riêng. 12 docs có kiểm tra relative links và counts. Kiểm tra hash theo index trước đó sai scope, được thay bằng lần kiểm tra mới resolve đúng bảy đường dẫn trên. Không thêm dependency.
