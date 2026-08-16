---
type: concept
status: seed
sources:
  - "[[2026-05-28_must-know-failure-modes-in-distributed-systems]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - reliability
  - isolation
---

# Bulkhead Pattern

## Định nghĩa

Bulkhead pattern là pattern chia resource thành các ngăn độc lập để lỗi hoặc quá tải ở một phần không tiêu thụ hết capacity của phần khác.

## Cách hiểu bằng lời của tôi

Bulkhead giống việc không để mọi tenant, region, queue hoặc dependency dùng chung một bể connection/thread duy nhất. Khi một phần bị flood, phần còn lại vẫn còn quota riêng để sống.

## Ví dụ resource cần cô lập

- Thread pool hoặc connection pool theo dependency.
- Queue theo tenant hoặc priority.
- Capacity theo region/zone.
- Budget cho retry traffic tách khỏi user traffic chính.

## Liên kết

- [[Cascading Failure]]
- [[Load Shedding]]
- [[Backpressure]]
- [[High Availability]]
- [[Service Level Objective]]
