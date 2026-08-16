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
  - reliability
---

# Metrics

## Định nghĩa

Metrics là dữ liệu time-series tổng hợp hành vi hệ thống theo thời gian, thường ở dạng counter, gauge hoặc histogram.

## Cách hiểu bằng lời của tôi

Metrics trả lời câu hỏi "đang xảy ra bao nhiêu, nhanh thế nào, tỷ lệ lỗi là gì" mà không cần đọc từng event. Nó nhẹ và phù hợp để alert, nhưng thường không đủ context để giải thích vì sao lỗi xảy ra.

## Loại metric thường gặp

- Counter: số request, số error, số retry.
- Gauge: queue depth, active connections, memory usage.
- Histogram/distribution: latency p50/p90/p99, payload size, query duration.
- Derived metric: error rate = errors / total requests.

## Cần biết

- Percentile latency hữu ích hơn average khi điều tra tail latency.
- Metric label phải bounded; high-cardinality field nên nằm trong logs/traces.
- Metric nên nối với SLI/SLO nếu dùng cho alert user-facing.

## Liên kết

- [[Observability]]
- [[Metric Cardinality]]
- [[Service Level Indicator]]
- [[Service Level Objective]]
- [[Alerting]]
