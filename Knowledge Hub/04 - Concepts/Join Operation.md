---
type: concept
status: seed
sources:
  - "[[2024-12-12_database-performance-demystified-essential-tips-and-strategi]]"
  - "[[2025-06-05_sql-vs-nosql-choosing-the-right-database-for-an-application]]"
  - "[[2025-09-17_the-pain-of-joins-in-mongodb-byte-sized-design]]"
source_sections:
  - "[[2024-12-12_database-performance-demystified-essential-tips-and-strategi]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - database
  - query
---

# Join Operation

## Định nghĩa

[[Join Operation]] là operation kết hợp dữ liệu từ nhiều table/collection theo quan hệ hoặc điều kiện chung.

## Cách hiểu bằng lời của tôi

Join là sức mạnh tự nhiên của relational database: normalized data có thể được ghép lại khi đọc. Nhưng join không miễn phí. Join giữa bảng lớn, thiếu index, hoặc filter muộn có thể làm row trung gian phình ra và tạo latency spike. Trong document/microservice world, join read-time thường nên được thay bằng materialized read model.

## Cần tối ưu

- Index trên join keys.
- Filter sớm trước khi join.
- Chọn join order hợp lý qua [[Query Planner]].
- Tránh join xuyên service trong request path.
- Với read-heavy view, cân nhắc [[Materialized View]] hoặc [[CQRS]].

## Liên kết

- [[SQL Database]]
- [[Document Store]]
- [[Query Execution Plan]]
- [[Database Indexing]]
- [[Database Schema Design]]
