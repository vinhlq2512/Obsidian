---
type: concept
status: seed
sources:
  - "[[2025-06-05_sql-vs-nosql-choosing-the-right-database-for-an-application]]"
  - "[[2025-09-17_the-pain-of-joins-in-mongodb-byte-sized-design]]"
source_sections:
  - "[[2025-06-05_sql-vs-nosql-choosing-the-right-database-for-an-application]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - database
  - nosql
---

# Document Store

## Định nghĩa

[[Document Store]] là NoSQL database lưu dữ liệu thành document tự chứa, thường ở dạng JSON/BSON, với schema linh hoạt và query theo field trong document.

## Cách hiểu bằng lời của tôi

Document store mạnh khi một aggregate được đọc cùng nhau: order kèm shipping/payment snapshot, product catalog, profile, content document. Triết lý là "store together what you read together". Nếu dùng nó như relational database và join nhiều collection ở read time, latency và complexity sẽ tăng nhanh.

## Pattern MongoDB

- Embed hoặc denormalize dữ liệu thường đọc cùng nhau.
- Shape document theo access pattern.
- Với read view phức tạp, dùng [[CQRS]] và event processing để materialize collection tối ưu cho query.
- Tránh biến mỗi request thành mini-ETL nhiều `$lookup`.

## Trade-off

- Read nhanh và predictable hơn khi document đúng shape.
- Write/update phức tạp hơn vì duplication cần đồng bộ.
- Multi-document transaction có thể có overhead hoặc caveat.
- Schema linh hoạt không thay thế data modeling.

## Liên kết

- [[NoSQL Database]]
- [[Join Operation]]
- [[Materialized View]]
- [[CQRS]]
- [[Event Stream]]
