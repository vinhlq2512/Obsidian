---
type: dashboard
created: 2026-07-22
tags:
  - dashboard
  - technical
---

# Dashboard kỹ thuật

## Ghi chú kỹ thuật mới

```dataview
TABLE
  area AS "Mảng",
  language AS "Ngôn ngữ",
  framework AS "Framework",
  status AS "Trạng thái",
  difficulty AS "Độ khó"
FROM "10 - Technical"
WHERE type = "technical-note"
SORT file.mtime DESC
LIMIT 20
```

## Project đang làm

```dataview
TABLE
  area AS "Mảng",
  target_date AS "Ngày mục tiêu",
  related_papers AS "Paper liên quan",
  related_concepts AS "Concept liên quan"
FROM "30 - Projects"
WHERE type = "project"
  AND status = "active"
SORT target_date ASC
```

## Concept kỹ thuật gần đây

```dataview
TABLE
  sources AS "Nguồn",
  status AS "Trạng thái"
FROM "04 - Concepts"
WHERE type = "concept"
SORT file.mtime DESC
LIMIT 15
```

## Synthesis kỹ thuật gần đây

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
