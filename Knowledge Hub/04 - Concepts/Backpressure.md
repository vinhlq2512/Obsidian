---
type: concept
status: seed
sources:
  - "[[2025-09-04_a-guide-to-rate-limiting-strategies-bytebytego-newsletter]]"
  - "[[2026-01-08_must-know-message-broker-patterns]]"
  - "[[2026-05-28_must-know-failure-modes-in-distributed-systems]]"
source_sections:
  - "[[2025-09-04_a-guide-to-rate-limiting-strategies-bytebytego-newsletter]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - system-design
---

# Backpressure

## Cách hiểu bằng lời của tôi

[[Backpressure]] là tín hiệu để upstream chậm lại khi downstream không theo kịp. Khác với [[Rate Limiting]] là một "cổng" chủ động chặn request theo policy, backpressure thường phản ánh trạng thái runtime như queue depth, consumer lag, saturation hoặc latency tăng.

## Cơ chế

```text
Downstream chậm / queue đầy
-> metric hoặc protocol báo quá tải
-> upstream giảm tốc, retry chậm hơn, shed load hoặc degrade
-> hệ thống tránh tự khuếch đại lỗi
```

## Khi áp dụng

Dùng khi hệ thống có pipeline, queue, stream processing, service chain hoặc bất kỳ điểm nào producer có thể tạo tải nhanh hơn consumer xử lý.

## Liên kết

- [[Message Broker]]
- [[Rate Limiting]]
- [[Load Shedding]]
- [[Cascading Failure]]
- [[Observability]]
