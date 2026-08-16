---
type: concept
status: seed
sources:
  - "[[2025-06-05_sql-vs-nosql-choosing-the-right-database-for-an-application]]"
  - "[[2026-04-16_a-guide-to-relational-database-design]]"
source_sections:
  - "[[2025-06-05_sql-vs-nosql-choosing-the-right-database-for-an-application]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - database
  - sql
---

# SQL Database

## Định nghĩa

[[SQL Database]] là database quan hệ dùng bảng, schema rõ, keys, constraints và SQL để truy vấn dữ liệu có cấu trúc.

## Cách hiểu bằng lời của tôi

SQL database mạnh khi dữ liệu có quan hệ rõ và correctness quan trọng. Schema, foreign key, transaction và join giúp database giữ invariant thay cho application code. Đổi lại, scale ngang và migration schema ở quy mô lớn cần thiết kế cẩn thận.

## Khi phù hợp

- Transactional workloads như payment, booking, inventory.
- Dữ liệu có quan hệ nhiều bảng và cần query linh hoạt.
- Cần [[ACID]], constraints và [[Transaction Isolation]].
- Team muốn tận dụng tooling trưởng thành: SQL, EXPLAIN, migration, backup.

## Trade-off

- JOIN lớn có thể thành bottleneck nếu index/schema không tốt.
- Vertical scaling có giới hạn.
- Distributed SQL/strong consistency trả thêm latency coordination.

## Liên kết

- [[Relational Database Design]]
- [[Database Schema Design]]
- [[Join Operation]]
- [[NewSQL]]
- [[NoSQL Database]]
