---
type: concept
status: developing
sources:
  - "[[2026-06-18_observability-for-beginners-logs-metrics-traces-and-everythi]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - observability
  - metrics
---

# Metric Cardinality

## Định nghĩa

Metric cardinality là số lượng time series riêng biệt được tạo ra bởi mọi tổ hợp label/tag của một metric.

## Cách hiểu bằng lời của tôi

Metric không chỉ tốn theo số điểm dữ liệu, mà tốn theo số chuỗi cần lưu. Một label như `region` có vài giá trị thường ổn; một label như `user_id` có thể tạo hàng triệu series và làm hệ thống metrics nổ tung.

## Ví dụ

```text
request_count{endpoint=6 giá trị}
-> 6 time series

request_count{endpoint=6, status=50, region=10}
-> 6 * 50 * 10 = 3000 time series
```

## Quy tắc thực dụng

- Dùng label bounded: status code, region, environment, service.
- Tránh label unbounded: user ID, session ID, request ID, raw URL, email.
- High-cardinality context nên đặt trong [[Structured Logging]] hoặc [[Distributed Tracing]].

## Liên kết

- [[Metrics]]
- [[Observability]]
- [[Distributed Tracing]]
