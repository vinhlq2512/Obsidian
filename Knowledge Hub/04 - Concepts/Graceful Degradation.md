---
type: concept
status: seed
sources:
  - "[[2026-05-28_must-know-failure-modes-in-distributed-systems]]"
  - "[[2025-08-07_top-strategies-to-improve-reliability-in-distributed-systems-part-1]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - reliability
  - system-design
---

# Graceful Degradation

## Định nghĩa

Graceful degradation là cách hệ thống giảm chất lượng hoặc phạm vi phục vụ có kiểm soát khi một dependency, capacity hoặc feature không còn đủ khỏe.

## Cách hiểu bằng lời của tôi

Thay vì trả lỗi toàn bộ, hệ thống giữ đường quan trọng nhất còn sống: dùng cached response, tắt feature phụ, giảm độ tươi dữ liệu, trả kết quả ít cá nhân hóa hơn, hoặc reject request ưu tiên thấp.

## Khi đi cùng pattern khác

- [[Circuit Breaker]] mở mạch rồi trả fallback.
- [[Load Shedding]] bỏ traffic ít quan trọng.
- [[Backpressure]] yêu cầu upstream giảm tốc.
- [[Service Level Objective]] giúp quyết định phần nào phải giữ, phần nào được giảm.

## Liên kết

- [[High Availability]]
- [[Load Shedding]]
- [[Circuit Breaker]]
- [[Backpressure]]
- [[Observability]]
