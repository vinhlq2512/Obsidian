---
type: concept
status: seed
sources:
  - "[[2024-12-12_database-performance-demystified-essential-tips-and-strategi]]"
  - "[[2026-04-02_database-performance-strategies-and-their-hidden-costs]]"
  - "[[2025-06-05_sql-vs-nosql-choosing-the-right-database-for-an-application]]"
source_sections:
  - "[[2026-04-02_database-performance-strategies-and-their-hidden-costs]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - database
  - performance
---

# Query Planner

## Định nghĩa

[[Query Planner]] là thành phần của database chọn cách thực thi SQL query dựa trên schema, index, statistics, estimated cardinality và cost model.

## Cách hiểu bằng lời của tôi

SQL nói "muốn dữ liệu gì"; planner quyết định "lấy bằng cách nào". Planner có thể chọn index scan, sequential scan, nested loop, hash join, merge join hoặc một thứ tự join khác. Nếu statistics sai hoặc index không khớp access pattern, planner có thể chọn plan tệ dù query nhìn có vẻ đúng.

## Điều ảnh hưởng tới planner

- Statistics về data distribution và cardinality.
- Index có sẵn và thứ tự column trong composite index.
- Predicate selectivity.
- Join condition và filter có được đẩy sớm không.
- Kích thước bảng/partition và cost I/O.

## Liên kết

- [[Query Execution Plan]]
- [[Database Indexing]]
- [[Join Operation]]
- [[Database Schema Design]]
- [[Database Partitioning]]
