---
type: concept
status: developing
sources:
  - "[[2025-06-19_a-guide-to-database-transactions-from-acid-to-concurrency-co]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - database
  - concurrency
---

# Concurrency Control

## Định nghĩa

Concurrency control là nhóm cơ chế giúp database xử lý nhiều transaction đồng thời mà vẫn giữ kết quả logic nhất quán.

## Cách hiểu bằng lời của tôi

Nếu hai user cùng cập nhật một record, database phải quyết định ai chờ, ai thắng, ai retry, và kết quả cuối có hợp lệ không. Concurrency control là luật giao thông cho những update chồng nhau.

## Hai hướng chính

- [[Pessimistic Locking]]: giả định conflict dễ xảy ra, khóa trước để ngăn transaction khác can thiệp.
- [[Optimistic Locking]]: giả định conflict hiếm, cho chạy trước rồi validate version lúc commit.

## Trade-off

- Pessimistic locking giảm bất ngờ nhưng tăng blocking/deadlock.
- Optimistic locking tăng throughput cho read-heavy/low-contention nhưng có thể tạo retry herd khi contention cao.
- Isolation level càng mạnh thường càng tốn contention.
- Transaction dài, access order không nhất quán và retry thiếu backoff dễ làm contention biến thành [[Deadlock]] hoặc retry storm.

## Liên kết

- [[Database Transaction]]
- [[Transaction Isolation]]
- [[Pessimistic Locking]]
- [[Optimistic Locking]]
- [[MVCC]]
- [[Deadlock]]
- [[Retry Storm]]
