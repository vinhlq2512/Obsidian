---
type: concept
status: seed
sources:
  - "[[2025-06-19_a-guide-to-database-transactions-from-acid-to-concurrency-co]]"
source_sections:
  - "[[2025-06-19_a-guide-to-database-transactions-from-acid-to-concurrency-co]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - database
  - concurrency
---

# MVCC

## Định nghĩa

[[MVCC]] là concurrency control approach trong đó database giữ nhiều version của row để transaction đọc một snapshot nhất quán mà không phải chặn mọi writer.

## Cách hiểu bằng lời của tôi

MVCC giảm va chạm giữa read và write: reader có thể đọc version phù hợp với snapshot của mình, còn writer tạo version mới. Đổi lại database phải dọn version cũ và hiểu rõ transaction nào còn cần snapshot nào.

## Khi hữu ích

- OLTP có nhiều read đồng thời.
- Cần tránh reader block writer và writer block reader.
- Cần isolation như read committed, repeatable read hoặc snapshot isolation tùy database.

## Trade-off

- Version cũ tạo storage overhead.
- Cleanup/vacuum/compaction trở thành phần vận hành quan trọng.
- Write conflict vẫn phải xử lý bằng lock, validation hoặc retry.
- Semantics khác nhau giữa PostgreSQL, MySQL InnoDB và các engine khác.

## Liên kết

- [[Snapshot Isolation]]
- [[Concurrency Control]]
- [[Transaction Isolation]]
- [[Optimistic Locking]]
- [[Storage Engine]]
