---
type: dashboard
created: 2026-07-22
tags:
  - dashboard
  - reading
---

# Dashboard đọc hôm nay

## Sách đang đọc

```dataviewjs
const books = dv.pages('"01 - Books"')
  .where(page => page.type === "book" && page.status === "reading")
  .sort(page => page.target_date ?? "9999-12-31");

const dailyReadings = dv.pages('"03 - Daily Reading"')
  .where(page => page.type === "daily-reading" && page.status === "completed" && page.current_page_after);

dv.table(
  ["Sách", "Tác giả", "Trạng thái", "Trang hiện tại", "Tổng trang", "Tiến độ", "Ngày mục tiêu"],
  books.map(book => {
    const readings = dailyReadings.where(reading => String(reading.book) === String(book.file.link));
    const currentPage = readings.length
      ? Math.max(...readings.map(reading => Number(reading.current_page_after)))
      : 0;
    const totalPages = Number(book.total_pages ?? 0);
    const progress = totalPages ? `${Math.round((currentPage / totalPages) * 100)}%` : "";

    return [
      book.file.link,
      book.author ?? "",
      book.status ?? "",
      currentPage,
      totalPages || "",
      progress,
      book.target_date ?? "",
    ];
  })
);
```

## Section cần đọc hôm nay

```dataview
TABLE
  book AS "Sách",
  status AS "Trạng thái",
  reading_date AS "Ngày đọc",
  start_page AS "Trang bắt đầu",
  end_page AS "Trang kết thúc",
  estimated_minutes AS "Phút dự kiến"
FROM "02 - Sections"
WHERE type = "reading-section"
  AND status != "completed"
  AND reading_date = date(today)
SORT reading_date ASC, book ASC, start_page ASC
```

## Lịch đọc sắp tới

```dataview
TABLE
  book AS "Sách",
  reading_date AS "Ngày đọc",
  start_page AS "Từ trang",
  end_page AS "Đến trang",
  estimated_minutes AS "Phút dự kiến"
FROM "02 - Sections"
WHERE type = "reading-section"
  AND status != "completed"
  AND reading_date > date(today)
SORT reading_date ASC, book ASC, start_page ASC
LIMIT 10
```

## Daily reading sắp tới

```dataview
TABLE
  book AS "Sách",
  section AS "Section",
  pages_planned AS "Trang",
  target_minutes AS "Phút",
  status AS "Trạng thái"
FROM "03 - Daily Reading"
WHERE type = "daily-reading"
  AND status != "completed"
  AND date >= date(today)
SORT date ASC
LIMIT 14
```

## Review đến hạn

```dataview
TABLE
  type AS "Loại",
  book AS "Sách",
  section AS "Section",
  review_date AS "Ngày review",
  status AS "Trạng thái"
FROM ""
WHERE need_review = true
  AND review_date
  AND review_date <= date(today)
  AND !contains(file.path, "05 - Templates")
SORT review_date ASC, file.name ASC
```

## Review sắp tới

```dataview
TABLE
  type AS "Loại",
  book AS "Sách",
  section AS "Section",
  review_date AS "Ngày review",
  status AS "Trạng thái"
FROM ""
WHERE need_review = true
  AND review_date
  AND review_date > date(today)
  AND review_date <= date(today) + dur(7 days)
  AND !contains(file.path, "05 - Templates")
SORT review_date ASC, file.name ASC
```

## Section cần review

```dataview
TABLE
  book AS "Sách",
  status AS "Trạng thái",
  reading_date AS "Ngày đọc",
  actual_minutes AS "Phút thực tế"
FROM "02 - Sections"
WHERE type = "reading-section" AND need_review = true
SORT reading_date ASC
```

## Nhật ký đọc gần đây

```dataview
TABLE
  book AS "Sách",
  section AS "Section",
  status AS "Trạng thái",
  target_minutes AS "Dự kiến",
  actual_minutes AS "Thực tế"
FROM "03 - Daily Reading"
WHERE type = "daily-reading"
SORT date DESC
LIMIT 7
```

## Concepts mới

```dataview
TABLE
  sources AS "Nguồn",
  status AS "Trạng thái"
FROM "04 - Concepts"
WHERE type = "concept"
SORT file.mtime DESC
LIMIT 10
```

## Câu hỏi học tập đang mở

```dataview
TABLE
  concepts AS "Concept",
  sources AS "Nguồn",
  updated_at AS "Cập nhật"
FROM "07 - Questions"
WHERE type = "question"
  AND status != "resolved"
SORT file.mtime DESC
LIMIT 10
```

## Synthesis mới

```dataview
TABLE
  concepts AS "Concept",
  sources AS "Nguồn",
  status AS "Trạng thái"
FROM "08 - Syntheses"
WHERE type = "synthesis"
SORT file.mtime DESC
LIMIT 10
```
