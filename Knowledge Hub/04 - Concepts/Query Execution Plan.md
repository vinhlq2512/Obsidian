---
type: concept
status: seed
sources:
  - "[[2024-12-12_database-performance-demystified-essential-tips-and-strategi]]"
  - "[[2026-04-02_database-performance-strategies-and-their-hidden-costs]]"
source_sections:
  - "[[2024-12-12_database-performance-demystified-essential-tips-and-strategi]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - database
  - performance
---

# Query Execution Plan

## Định nghĩa

[[Query Execution Plan]] là mô tả cách database sẽ thực thi một query: scan bảng hay dùng index, join theo thứ tự nào, sort ở đâu, và operation nào tốn tài nguyên nhất.

## Cách hiểu bằng lời của tôi

Execution plan là bản đồ "database thật sự làm gì", không phải "mình nghĩ query này làm gì". Khi query chậm, đọc plan thường cho thấy nguyên nhân: [[Full Table Scan]], index không được dùng, join quá lớn, sort/hash tốn memory, hoặc statistics đã lỗi thời.

## Cần quan sát

- Table scan hay index scan.
- Join order và join algorithm.
- Số row ước lượng so với row thực tế.
- Sort, aggregate, temporary table hoặc spill to disk.
- Cost/time ở từng bước với `EXPLAIN` hoặc `EXPLAIN ANALYZE`.

## Liên kết

- [[Query Planner]]
- [[Full Table Scan]]
- [[Database Indexing]]
- [[Join Operation]]
- [[Database Performance Tradeoffs]]
