# Locator Playwright: tìm đúng phần tử và giữ đúng ý nghĩa

> Bản ôn tập tự biên soạn cho fresher. Nội dung khóa học là nguồn chính; đoạn web được gắn nhãn riêng. Không phải đáp án chính thức.

## Mục tiêu và kiến thức cần có
Đọc được DOM/accessibility, chọn locator có scope và uniqueness, giải thích khi nào sửa test hay báo lỗi accessibility.

[Execution](playwright-execution-debugging.md): biết page/context và async/await. HTML form, label và thuộc tính cần đọc ở mức cơ bản.

## Mức ưu tiên
Bắt buộc: locator contract, semantic inspection, scope, strictness, test ID governance, chống .last()/force chữa cháy. Nên biết: i18n, iframe, virtualized list. Mở rộng: shadow DOM và component policy; chỉ áp dụng khi target thực sự có.

## Từ khóa bằng câu đầy đủ
Locator là truy vấn được đánh giá khi dùng, không phải bản sao element đã khóa. Accessible name là tên control mà tầng accessibility cung cấp, không nhất thiết là class hoặc text nhìn thấy. Scope giới hạn vùng tìm kiếm để cùng tên Save không chọn nhầm. Strictness yêu cầu thao tác một element có đích rõ. Test ID là contract được frontend và QA cùng quản trị.

## Học từ đầu: cái gì, vì sao và khi nào
Một fresher thường copy CSS từ DevTools vì thấy nó chạy lần đầu. Vấn đề là CSS như div:nth-child(3) mô tả vị trí hiện tại, trong khi test cần mô tả ý định “sửa employee E2E-01”. Khi frontend thêm một wrapper hoặc đổi thứ tự hàng, selector vẫn có thể match nhưng thực hiện sai hành động. Locator tốt cần trả lời: intent gì, role/name nào, vùng UI nào, thay đổi nào phải làm test fail.

DOM là cây node, rendered state là điều browser đang hiển thị, accessibility tree diễn tả semantics phục vụ công nghệ hỗ trợ. Một label nhìn giống nhãn chưa chắc liên kết input. Vì vậy hãy inspect role, name, label association và state ở đúng thời điểm. getByRole phù hợp control có semantics tốt; getByLabel phù hợp field có label liên kết; getByText phù hợp nội dung nghiệp vụ; test ID phù hợp hook ổn định được quản trị. Placeholder không thay thế label.

Thứ tự role/name → label → test ID → business text → CSS scoped là mặc định của course, không phải bảng xếp hạng tuyệt đối. Nếu UI thiếu accessible name, thay bằng test ID có thể giúp automation nhưng finding accessibility vẫn cần giữ. Với đa ngôn ngữ, copy text có thể đổi có chủ đích: chọn locale fixture hoặc test hook đã thống nhất.

Hai nút Confirm không phải lý do chọn .first(). Hãy xác định dialog đang mở, rồi tìm nút bên trong. Với bảng, xác định hàng bằng cell ID chính xác, kiểm tra một hàng rồi thao tác trong hàng. Locator resolve lại sau rerender giúp tránh giữ element cũ, nhưng không tự bảo đảm query phản ánh đúng intent.

## Input → xử lý → output
AC-EMP-02 + DOM observation có row/cell và button Edit employee → chọn row theo cell employeeId, kiểm tra count, click Edit trong row → locator inventory và patch có rationale.

## Ví dụ fresher
```ts
const row = page.getByRole('row').filter({
  has: page.getByRole('cell', { name: employeeId, exact: true })
});
await expect(row).toHaveCount(1);
await row.getByRole('button', { name: 'Edit employee', exact: true }).click();
```

Ví dụ chỉ dùng sau khi role/cell/button name được inspect. Khai báo employeeId từ data riêng của run. Không coi code minh họa là evidence đã chạy.

## So sánh dễ nhầm
| Lựa chọn | Dùng khi | Giới hạn |
|---|---|---|
| Role/name | Control có semantics đúng | Name trùng cần scope |
| Label | Input có association | Visual label chưa đủ |
| Test ID | Hook có owner và contract | Không chứng minh accessibility |
| CSS/XPath | Không có contract tốt hơn | Ghi exception, tránh DOM depth |
| frameLocator | Element nằm trong iframe | Xác định frame trước |
| Shadow DOM | Component có shadow root | Kiểm tra hỗ trợ; closed root không suy là truy cập được |

## Bẫy quiz và phỏng vấn
Không suy “thao tác được” thành “đúng nghiệp vụ”; không lấy một output từ tool làm nguồn cho mọi claim. Khi trả lời phỏng vấn, nêu intent, cơ chế, ví dụ cụ thể và giới hạn evidence. Xem [bộ phỏng vấn](../03_interview/playwright-locators.md) và [quiz tự luyện](../04_quiz/playwright-locators-questions.md), làm trước khi mở đáp án.

## Tự kiểm tra
- [ ] Tự giải thích vì sao row theo ID bền hơn row thứ ba
- [ ] Viết inventory sáu element gồm intent, scope, evidence, count và fallback
- [ ] Nêu một trường hợp locator fail là lỗi UI.

## Nguồn và phần bổ sung
Nguồn khóa học: [course](../../document/AIQE%20Playwright%20MCP%20%26%20Locator%20Mastery/L3_AIQE_PMLM_course_content_vi.md), [bài tập](../../document/AIQE%20Playwright%20MCP%20%26%20Locator%20Mastery/L3_AIQE_PMLM_exercises_vi.md). Heading đối chiếu chính xác: PMLM Unit 3 — DOM inspection, accessible roles and locator fundamentals; Unit 4 — Locator strategy: robust selectors and anti-patterns. Exercises: EX-U3-LOCATOR-INVENTORY; EX-U4-HARDEN; EX-U7-INCIDENT.

Bổ sung từ nguồn web: Playwright xác nhận locator được resolve lại khi thực hiện action; ưu tiên user-facing attributes và explicit contracts. [Locators](https://playwright.dev/docs/locators).

