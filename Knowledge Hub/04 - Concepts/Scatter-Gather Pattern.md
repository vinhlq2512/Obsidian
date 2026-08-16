---
type: concept
status: understood
sources:
  - "[[2026-05-07_container-design-patterns-for-distributed-systems]]"
source_sections:
  - "[[2026-05-07_container-design-patterns-for-distributed-systems]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - distributed-systems
  - search
---

# Scatter-Gather Pattern

## Định nghĩa

Scatter-Gather Pattern là pattern fan-out một request tới nhiều shard/worker song song, rồi merge partial results thành response cuối.

## Cách hiểu bằng lời của tôi

Search engine là ví dụ tự nhiên: query được gửi tới nhiều shard, mỗi shard trả kết quả cục bộ, merge logic gom lại thành ranking cuối. Pattern này giúp dùng parallelism, nhưng timeout, slow shard và partial failure phải được xử lý trong merge policy.

## Liên kết

- [[Database Sharding]]
- search architecture
- [[Fan-Out on Read]]
- [[Partial Failure]]
- [[Ranking]]
