---
type: book
author:
status: not-started
total_pages:
started:
target_date:
priority: medium
source_file:
created_at: {{date}}
updated_at: {{date}}
tags:
  - book
---

# {{title}}

## Thông tin

- Tác giả:
- Trạng thái:
- Tổng số trang:
- Ngày bắt đầu:
- Ngày mục tiêu:

## Nguồn

- PDF gốc:
- Vị trí: `00 - Sources/PDFs/Books`

## Tiến độ tự động

```dataview
TABLE WITHOUT ID
  max(rows.current_page_after) AS "Trang hiện tại",
  this.total_pages AS "Tổng trang",
  round((max(rows.current_page_after) / this.total_pages) * 100) + "%" AS "Tiến độ"
FROM "03 - Daily Reading"
WHERE type = "daily-reading"
  AND status = "completed"
  AND book = this.file.link
  AND current_page_after
GROUP BY book
```

## Lý do đọc

- 

## Mục tiêu đọc

- Số trang mỗi ngày:
- Số section mỗi session:
- Kết quả mong muốn sau khi đọc:

## Sections

- [ ] [[Tên sách - Section 01]]
- [ ] [[Tên sách - Section 02]]
- [ ] [[Tên sách - Section 03]]

## Ý tưởng quan trọng

- 

## Khái niệm liên quan

- [[Khái niệm 1]]
- [[Khái niệm 2]]

## Áp dụng thực tế

- 

## Ghi chú sau khi hoàn thành

- 
