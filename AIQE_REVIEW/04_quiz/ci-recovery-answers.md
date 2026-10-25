# Giải thích quiz — ci-recovery

Đáp án tự biên soạn theo [bài học và nguồn của bài](../01_topics/ci-recovery.md), không thay rubric hay quyết định trainer.

## Câu 1 — C

- **A:** Không có authorization production.
- **B:** Tìm credentials không thuộc approved workflow.
- **C:** Đúng: PR lane có scope riêng.
- **D:** Skipped không phải assertion pass.

## Câu 2 — D

- **A:** Không có assertion.
- **B:** Empty selection không chứng minh requirement.
- **C:** Chưa có app assertion để kết luận app fail.
- **D:** Đúng: kiểm tra tag/config/command và empty-selection behavior.

## Câu 3 — A

- **A:** Đúng: cộng UTC+7 qua ngày.
- **B:** Không chuyển UTC sang VN.
- **C:** Đảo trường phút/giờ.
- **D:** Phải xét ngày rollover khi đối chiếu slots.

## Câu 4 — B

- **A:** Git không cô lập database.
- **B:** Đúng: lock scope theo tài nguyên; ownership vẫn bắt buộc.
- **C:** Context browser không tách backend data.
- **D:** Timestamp đơn lẻ có thể va chạm, chưa có uniqueness contract.

## Câu 5 — C

- **A:** Runner/process có thể không thực thi teardown.
- **B:** Reporter không bảo đảm lifecycle.
- **C:** Đúng: recovery ngoài job/next preflight theo policy.
- **D:** Prefix rộng không chứng minh ownership.

## Câu 6 — D

- **A:** DOM order không chỉ đúng target.
- **B:** Force không chữa ambiguity/oracle.
- **C:** Sleep không chứng minh readiness hay scope.
- **D:** Đúng: chữa locator layer trước rồi giữ business assertions.

## Câu 7 — A

- **A:** Đúng: write tồn tại không thay UI search assertion.
- **B:** Có nguy cơ duplicate write.
- **C:** Chưa có matching search assertion AC-EMP-02.
- **D:** Ngoài ownership.

## Câu 8 — B

- **A:** Không đáp ứng UI oracle.
- **B:** Đúng: action + assertion theo contract.
- **C:** Virtualization không cho phép bỏ oracle.
- **D:** E2E-1 có thể nhầm E2E-10.

## Câu 9 — C

- **A:** Chưa tương tác app.
- **B:** Flaky runner cần fail/pass attempts; root cause vẫn riêng.
- **C:** Đúng: kiểm tra runner/runtime/permissions.
- **D:** Retry uncontrolled không thay evidence hiện tại.

## Câu 10 — D

- **A:** Chưa có causal/fix evidence.
- **B:** Xóa lịch sử che retry/cost.
- **C:** Một run không đủ reliability.
- **D:** Đúng theo outcome semantics, diagnosis vẫn pending.
