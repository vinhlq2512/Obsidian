---
type: concept
status: developing
sources:
  - "[[2026-06-18_observability-for-beginners-logs-metrics-traces-and-everythi]]"
  - "[[2025-01-20_the-engineers-guide-to-observability-making-metrics-logs-and]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - observability
  - distributed-systems
---

# Distributed Tracing

## Định nghĩa

Distributed tracing là kỹ thuật theo dõi một request khi nó đi qua nhiều service bằng trace ID chung và các span biểu diễn từng đơn vị công việc.

## Cách hiểu bằng lời của tôi

Metrics nói latency tăng. Logs nói có lỗi ở đâu đó. Trace cho thấy request này đã đi qua service nào, query nào chậm, queue nào nghẽn, và span nào là nút thắt.

## Thành phần

- Trace ID: định danh chung cho toàn bộ request.
- Span: một operation như API call, DB query, queue publish hoặc function call.
- Parent-child relationship: nối span thành cây/timeline.
- Context propagation: truyền trace ID qua header hoặc metadata giữa service.

## Sampling

- Head sampling quyết định ngay từ đầu; rẻ và nhất quán nhưng có thể bỏ mất trace thú vị.
- Tail sampling quyết định sau khi trace hoàn tất; giữ được error/slow trace tốt hơn nhưng cần buffer và vận hành phức tạp hơn.

## Liên kết

- [[Observability]]
- [[Structured Logging]]
- [[Metrics]]
- [[Microservices Design Patterns]]
