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

# NoSQL Database

## Định nghĩa

[[NoSQL Database]] là nhóm database không lấy relational table/SQL làm mô hình trung tâm, thường tối ưu cho schema linh hoạt, scale ngang, availability hoặc access pattern chuyên biệt.

## Cách hiểu bằng lời của tôi

NoSQL không phải "không cần model dữ liệu". Ngược lại, vì thường thiếu join/ad-hoc query mạnh như SQL, schema phải được thiết kế quanh access pattern. Đọc nhanh thường đến từ việc denormalize, embed hoặc materialize trước.

## Nhóm phổ biến

- Key-value store: lookup theo key cực nhanh, query linh hoạt hạn chế.
- [[Document Store]]: document JSON/BSON, hợp schema biến đổi và read theo aggregate.
- Column-family store: wide/sparse data, write-heavy, query theo primary key pattern.
- Graph database: tối ưu traversal quan hệ sâu.

## Trade-off

- Scale và availability tốt hơn ở một số workload.
- Consistency, transaction scope và query richness thường cần đánh đổi.
- Application chịu nhiều trách nhiệm hơn về duplication, sync và correctness.

## Liên kết

- [[SQL Database]]
- [[Document Store]]
- [[Distributed Key-Value Store]]
- [[Cassandra]]
- [[Eventual Consistency]]
