---
type: synthesis
status: developing
concepts:
  - "[[Observability]]"
  - "[[Structured Logging]]"
  - "[[Metrics]]"
  - "[[Metric Cardinality]]"
  - "[[Distributed Tracing]]"
  - "[[Service Level Indicator]]"
  - "[[Service Level Objective]]"
  - "[[Alerting]]"
sources:
  - "[[2026-06-18_observability-for-beginners-logs-metrics-traces-and-everythi]]"
  - "[[2025-01-20_the-engineers-guide-to-observability-making-metrics-logs-and]]"
created_at: 2026-08-16
updated_at: 2026-08-16
tags:
  - synthesis
  - observability
  - reliability
  - system-design
---

# Observability for Distributed Systems

## Mental model

Một event runtime có thể được nhìn qua ba projection:

- log: một sự kiện cụ thể với context chi tiết;
- metric: tổng hợp nhiều event thành time series;
- trace: nối các span của một request qua nhiều service.

Observability tốt không phải có thật nhiều dữ liệu, mà là có dữ liệu đúng dạng để hỏi câu hỏi mới khi hệ thống có hành vi lạ.

## Thiết kế dữ liệu

| Câu hỏi | Dùng gì trước | Lý do |
|---|---|---|
| Error rate đang tăng không? | [[Metrics]] | Tổng hợp nhanh, alert được |
| Request cụ thể lỗi vì sao? | [[Structured Logging]] | Context chi tiết của event |
| Latency nằm ở service nào? | [[Distributed Tracing]] | Thấy timeline qua service |
| Có nên đánh thức người trực không? | [[Service Level Objective]] + [[Alerting]] | Bám vào user impact |

## Những lỗi hay gặp

- Gắn `user_id` hoặc `request_id` vào metric label làm nổ [[Metric Cardinality]].
- Alert theo CPU/memory thay vì symptom user cảm nhận.
- Dashboard giữ mọi chart từng dùng trong incident cũ.
- Log thiếu correlation ID nên không nối được câu chuyện.
- Trace sampling quá thô làm mất đúng request cần điều tra.

## Liên kết

- [[Scalable Distributed Systems Patterns]]
- [[High Availability]]
- [[Microservices Design Patterns]]
- [[Production LLM System Design]]
