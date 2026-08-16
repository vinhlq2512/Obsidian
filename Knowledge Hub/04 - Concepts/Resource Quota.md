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

# Resource Quota

## Định nghĩa

[[Resource Quota]] là giới hạn tài nguyên theo tenant, user, workload hoặc tier để bảo vệ fairness và tránh một actor chiếm hết tài nguyên dùng chung.

## Cách hiểu bằng lời của tôi

Trong pooled multi-tenant system, quota là cách mua lại một phần isolation. Nó làm giảm hiệu suất tối đa của một tenant đơn lẻ nhưng bảo vệ các tenant còn lại khỏi noisy neighbor.

## Ví dụ tài nguyên cần quota

- Database connections.
- CPU hoặc worker slots.
- Queue throughput.
- Search/indexing capacity.
- Export/report concurrency.

## Liên kết

- [[Noisy Neighbor Problem]]
- [[Rate Limiting]]
- [[Load Shedding]]
- [[Bulkhead Pattern]]
- [[Capacity Planning]]
