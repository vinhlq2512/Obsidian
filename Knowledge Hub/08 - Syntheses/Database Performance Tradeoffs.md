---
type: synthesis
status: seed
concepts:
  - "[[Query Execution Plan]]"
  - "[[Query Planner]]"
  - "[[Full Table Scan]]"
  - "[[Database Indexing]]"
  - "[[Database Partitioning]]"
  - "[[Database Schema Design]]"
  - "[[Join Operation]]"
  - "[[SQL Database]]"
  - "[[NoSQL Database]]"
  - "[[NewSQL]]"
  - "[[Document Store]]"
  - "[[MVCC]]"
  - "[[Snapshot Isolation]]"
  - "[[Deadlock]]"
  - "[[Database Workload Isolation]]"
sources:
  - "[[2024-12-12_database-performance-demystified-essential-tips-and-strategi]]"
  - "[[2026-04-02_database-performance-strategies-and-their-hidden-costs]]"
  - "[[2025-06-19_a-guide-to-database-transactions-from-acid-to-concurrency-co]]"
  - "[[2025-06-05_sql-vs-nosql-choosing-the-right-database-for-an-application]]"
  - "[[2025-09-17_the-pain-of-joins-in-mongodb-byte-sized-design]]"
  - "[[2026-04-16_a-guide-to-relational-database-design]]"
questions: []
created_at: 2026-08-16
updated_at: 2026-08-16
tags:
  - synthesis
  - database
  - performance
  - bytebytego
---

# Database Performance Tradeoffs

## Ý chính

Database performance không có một đòn tối ưu duy nhất. Mỗi cải tiến đổi chi phí sang chỗ khác: index tăng read speed nhưng làm write chậm; denormalization giảm join nhưng tăng sync complexity; cache giảm load nhưng tạo stale read; sharding scale write nhưng tăng vận hành.

## Vòng chẩn đoán

```text
slow path
-> đọc [[Query Execution Plan]]
-> xác định scan/index/join/sort/lock bottleneck
-> sửa query hoặc index
-> kiểm tra schema/partition/workload isolation
-> đo lại latency, throughput, CPU, memory, I/O
```

## Bảng trade-off

| Kỹ thuật | Giúp | Giá phải trả |
|---|---|---|
| [[Database Indexing]] | Read/filter/join nhanh | Write chậm, storage, maintenance |
| [[Database Partitioning]] | Scan ít dữ liệu hơn | Key sai làm query xuyên partition chậm |
| Denormalization | Read path nhanh | Duplicate data, stale/inconsistency |
| [[Materialized View]] | Query phức tạp thành lookup | Refresh lag, pipeline vận hành |
| [[Read Replica]] | Scale read | Replication lag |
| [[Database Sharding]] | Scale write/storage ngang | Cross-shard query, rebalancing, ops complexity |
| [[MVCC]] | Reader/writer ít block nhau | Version cleanup, conflict semantics |

## Chọn database

- [[SQL Database]]: ưu tiên schema, constraints, join và transaction correctness.
- [[NoSQL Database]]: ưu tiên scale, schema flexibility hoặc access pattern chuyên biệt.
- [[NewSQL]]: cần SQL/ACID nhưng phải scale phân tán, chấp nhận coordination latency.
- [[Document Store]]: đọc theo aggregate/document, tránh join read-time bằng materialized read model.

## Liên kết

- [[Database Internals Tradeoffs]]
- [[Distributed Data Consistency Patterns]]
- [[Object and Key-Value Storage Patterns]]
- [[Capacity Planning]]
