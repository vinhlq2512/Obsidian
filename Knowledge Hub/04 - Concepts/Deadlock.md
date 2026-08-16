---
type: concept
status: seed
sources:
  - "[[2025-06-19_a-guide-to-database-transactions-from-acid-to-concurrency-co]]"
  - "[[2024-12-12_database-performance-demystified-essential-tips-and-strategi]]"
source_sections:
  - "[[2025-06-19_a-guide-to-database-transactions-from-acid-to-concurrency-co]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - database
  - concurrency
---

# Deadlock

## Định nghĩa

[[Deadlock]] là tình huống hai hoặc nhiều transaction giữ lock mà transaction khác cần, rồi chờ nhau vô hạn nếu database không phát hiện và abort một bên.

## Cách hiểu bằng lời của tôi

Deadlock thường không phải vì một lock, mà vì thứ tự lock khác nhau. Transaction A giữ row 1 rồi chờ row 2; transaction B giữ row 2 rồi chờ row 1. Database thường sẽ detect và rollback một transaction, nên application phải biết retry an toàn.

## Cách giảm

- Giữ transaction ngắn.
- Tránh network call trong transaction.
- Access resource theo thứ tự nhất quán.
- Chọn isolation/locking phù hợp workload.
- Retry có backoff và timeout.

## Liên kết

- [[Pessimistic Locking]]
- [[Concurrency Control]]
- [[Transaction Isolation]]
- [[Retry Pattern]]
- [[Timeout]]
