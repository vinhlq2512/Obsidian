---
type: book
author: Robert C. Martin
status: reading
total_pages: 432
started: 2026-07-21
target_date:
---

# Clean Architecture

## Thông tin

- Tác giả: Robert C. Martin
- Trạng thái: Đang đọc
- Tổng số trang: 432

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

## Mục tiêu

- Đọc 15 trang mỗi ngày
- Hoàn thành 1 section mỗi session
- Viết tóm tắt sau mỗi section

## Sections

- [ ] [[Clean Architecture - Section 01]]
- [ ] [[Clean Architecture - Section 02]]
- [ ] [[Clean Architecture - Section 03]]

## Ý tưởng quan trọng

- 

## Áp dụng thực tế

- 
