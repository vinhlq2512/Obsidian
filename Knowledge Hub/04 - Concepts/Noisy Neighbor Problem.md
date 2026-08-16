---
type: concept
status: seed
sources:
  - "[[2026-07-16_a-guide-to-multi-tenancy-benefits-and-challenges]]"
source_sections:
  - "[[2026-07-16_a-guide-to-multi-tenancy-benefits-and-challenges]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - tenancy
  - reliability
---

# Noisy Neighbor Problem

## Định nghĩa

[[Noisy Neighbor Problem]] xảy ra khi một tenant tiêu thụ quá nhiều tài nguyên chung, làm tenant khác trên cùng pool bị chậm, timeout hoặc mất ổn định.

## Cách hiểu bằng lời của tôi

Pooling tiết kiệm vì mọi người dùng chung tài nguyên. Nhưng một report nặng, bulk import hoặc query runaway của một tenant có thể ăn CPU, connection, I/O hoặc queue capacity của người khác. Fairness không tự xuất hiện trong pooled system; nó phải được thiết kế bằng quota, limit và isolation.

## Liên kết

- [[Multi-Tenancy]]
- [[Resource Quota]]
- [[Blast Radius]]
- [[Rate Limiting]]
- [[Bulkhead Pattern]]
- [[Load Shedding]]
