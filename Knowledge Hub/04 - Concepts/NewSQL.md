---
type: concept
status: seed
sources:
  - "[[2025-06-05_sql-vs-nosql-choosing-the-right-database-for-an-application]]"
  - "[[2024-02-17_truetime-chronicles-how-a-clock-powers-google-spanners-scala]]"
source_sections:
  - "[[2025-06-05_sql-vs-nosql-choosing-the-right-database-for-an-application]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - database
  - distributed-systems
---

# NewSQL

## Định nghĩa

[[NewSQL]] là nhóm distributed database cố giữ SQL/relational model và ACID semantics trong khi hỗ trợ horizontal scaling, replication và fault tolerance kiểu hệ phân tán.

## Cách hiểu bằng lời của tôi

NewSQL cố ghép hai thế giới: developer vẫn dùng SQL/transaction, nhưng storage/consensus bên dưới chạy qua nhiều node/region. Nó hợp với workload cần correctness mạnh ở scale lớn, nhưng không miễn phí: write path phải trả latency cho coordination.

## Khi phù hợp

- Global transactional workload.
- Cần SQL và ACID nhưng một node không đủ.
- Cần high availability với consistency mạnh.
- Muốn giảm manual sharding trong RDBMS truyền thống.

## Trade-off

- Cross-region write latency cao hơn local database.
- Debug distributed query/transaction phức tạp.
- Cost và operational model thường khác RDBMS quen thuộc.

## Liên kết

- [[SQL Database]]
- [[Strong Consistency]]
- [[Consensus]]
- [[Strict Serializability]]
- [[CAP and PACELC]]
