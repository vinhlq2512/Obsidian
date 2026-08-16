---
type: concept
status: seed
sources:
  - "[[2026-04-16_a-guide-to-relational-database-design]]"
  - "[[2025-06-05_sql-vs-nosql-choosing-the-right-database-for-an-application]]"
source_sections:
  - "[[2026-04-16_a-guide-to-relational-database-design]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - database
  - sql
---

# Relational Database Design

## Định nghĩa

[[Relational Database Design]] là cách mô hình hóa dữ liệu thành tables, rows, columns, keys, constraints và relationships để giữ integrity và hỗ trợ query bằng SQL.

## Cách hiểu bằng lời của tôi

Thiết kế relational database không bắt đầu từ câu lệnh SQL, mà từ việc nhận diện entity nào xứng đáng thành table, relationship nào cần foreign key, dữ liệu nào nên normalize, và query nào cần join/index. Schema đúng làm invariant rõ; schema sai khiến application phải vá lỗi dữ liệu mãi về sau.

## Building blocks

- Primary key định danh duy nhất một row.
- Foreign key nối table và giữ referential integrity.
- One-to-one, one-to-many, many-to-many mô tả quan hệ entity.
- Junction table biểu diễn many-to-many.
- Normalization giảm redundancy và anomaly.
- [[Join Operation]] ghép dữ liệu đã normalize khi đọc.

## Liên kết

- [[SQL Database]]
- [[Database Schema Design]]
- [[Database Indexing]]
- [[Join Operation]]
- [[ACID]]
