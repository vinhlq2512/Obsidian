---
type: concept
status: seed
sources:
  - "[[2025-01-20_the-engineers-guide-to-observability-making-metrics-logs-and]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - reliability
  - observability
---

# Service Level Indicator

## Định nghĩa

Service Level Indicator là metric đo trực tiếp một thuộc tính user-facing của service, ví dụ availability, latency, error rate hoặc request success ratio.

## Cách hiểu bằng lời của tôi

SLI là thứ ta đo để biết user có đang nhận dịch vụ tốt không. Nó nên gần trải nghiệm user hơn là gần tài nguyên máy.

## Ví dụ

- Tỷ lệ request checkout thành công.
- Latency p95/p99 của API chính.
- Tỷ lệ stream response bị ngắt.
- Availability theo cửa sổ thời gian.

## Liên kết

- [[Service Level Objective]]
- [[Metrics]]
- [[Alerting]]
- [[Observability]]
