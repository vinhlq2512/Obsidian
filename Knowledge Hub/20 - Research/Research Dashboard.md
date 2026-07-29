---
type: dashboard
created: 2026-07-22
tags:
  - dashboard
  - research
---

# Dashboard nghiên cứu

## Paper đang đọc

```dataview
TABLE
  authors AS "Tác giả",
  year AS "Năm",
  venue AS "Venue",
  topic AS "Chủ đề",
  priority AS "Ưu tiên"
FROM "20 - Research/Papers"
WHERE type = "paper"
  AND (reading_status = "reading" OR status = "reading")
SORT priority ASC, year DESC
```

## Paper cần đọc tiếp

```dataview
TABLE
  authors AS "Tác giả",
  year AS "Năm",
  topic AS "Chủ đề",
  reading_status AS "Trạng thái đọc",
  priority AS "Ưu tiên"
FROM "20 - Research/Papers"
WHERE type = "paper"
  AND (reading_status = "not-started" OR status = "unread")
SORT priority ASC, year DESC
LIMIT 20
```

## Paper đã đọc

```dataview
TABLE
  authors AS "Tác giả",
  year AS "Năm",
  venue AS "Venue",
  topic AS "Chủ đề",
  rating AS "Đánh giá"
FROM "20 - Research/Papers"
WHERE type = "paper"
  AND (reading_status = "completed" OR status = "completed")
SORT year DESC, rating DESC
LIMIT 20
```

## Nhật ký đọc paper gần đây

```dataview
TABLE
  paper AS "Paper",
  status AS "Trạng thái",
  target_minutes AS "Dự kiến",
  actual_minutes AS "Thực tế",
  review_date AS "Ngày review"
FROM "20 - Research/Paper Reading"
WHERE type = "paper-reading"
SORT date DESC
LIMIT 14
```

## Câu hỏi nghiên cứu đang mở

```dataview
TABLE
  topic AS "Chủ đề",
  priority AS "Ưu tiên",
  related_papers AS "Paper liên quan"
FROM "20 - Research/Research Questions"
WHERE type = "research-question"
  AND status = "open"
SORT priority ASC, created DESC
```

## Experiment đang chạy

```dataview
TABLE
  project AS "Project",
  research_question AS "Câu hỏi",
  method AS "Method",
  metric AS "Metric",
  result AS "Kết quả"
FROM "20 - Research/Experiments"
WHERE type = "experiment"
  AND status != "completed"
SORT started DESC
```

## Literature notes mới

```dataview
TABLE
  topic AS "Chủ đề",
  scope AS "Phạm vi",
  papers AS "Papers"
FROM "20 - Research/Literature Notes"
WHERE type = "literature-note"
SORT file.mtime DESC
LIMIT 10
```

## Technical notes mới

```dataview
TABLE
  area AS "Mảng",
  language AS "Ngôn ngữ",
  framework AS "Framework",
  difficulty AS "Độ khó"
FROM "10 - Technical"
WHERE type = "technical-note"
SORT file.mtime DESC
LIMIT 10
```
