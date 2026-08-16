---
type: synthesis
status: seed
concepts:
  - "[[Strong Consistency]]"
  - "[[Eventual Consistency]]"
  - "[[Saga Pattern]]"
  - "[[Change Data Capture]]"
  - "[[Transactional Outbox]]"
  - "[[Consensus]]"
  - "[[Leader Election]]"
sources:
  - "[[2025-02-27_mastering-data-consistency-across-microservices]]"
  - "[[2026-02-26_strong-consistency-in-databases-promises-and-costs]]"
  - "[[2025-07-31_top-leader-election-algorithms-in-distributed-databases]]"
  - "[[2026-08-06_the-read-path-versus-the-write-path-strategies-and-technique]]"
created_at: 2026-08-16
updated_at: 2026-08-16
tags:
  - synthesis
  - database
  - distributed-systems
---

# Distributed Data Consistency Patterns

## Ý chính

Khi dữ liệu nằm trên nhiều service, database hoặc region, consistency không còn là một tính chất mặc định. Nó là một lựa chọn theo từng invariant: dữ liệu nào cần đúng ngay, dữ liệu nào được stale, workflow nào cần compensation, và coordination nào đáng trả latency.

## Map quyết định

| Nhu cầu | Pattern | Giá phải trả |
|---|---|---|
| Mọi read sau write phải thấy giá trị mới | [[Strong Consistency]] | [[Consensus]], quorum latency, giảm availability khi mất majority |
| Dữ liệu được phép stale trong một cửa sổ | [[Eventual Consistency]] | Conflict resolution, observability cho lag và hội tụ |
| Workflow nhiều service không dùng transaction toàn cục | [[Saga Pattern]] | Compensating action và debugging event flow |
| Đồng bộ read store/index/warehouse | [[Change Data Capture]] | Coupling với log, consumer lag, replay |
| Publish event cùng transaction với state change | [[Transactional Outbox]] | Thêm outbox table và publisher lifecycle |
| Cần một node điều phối write/log | [[Leader Election]] | Election timeout, quorum, split-brain safety |

## Mental model

```text
business invariant
-> chọn consistency guarantee
-> chọn coordination hoặc async sync
-> thiết kế failure/compensation
-> đo lag, conflict, retry và user-visible stale read
```

## Ghi nhớ

Strong consistency không miễn phí, nhưng eventual consistency cũng không miễn phí. Một bên trả bằng coordination/latency; bên kia trả bằng application logic, compensation, read-your-writes handling và observability.

## Liên kết

- [[Database Internals Tradeoffs]]
- [[Resilience Failure Control Patterns]]
- [[Message Broker]]
- [[Data Replication]]
