---
type: concept
status: seed
sources:
  - "[[2024-08-08_a-crash-course-on-microservices-design-patterns-newsletter]]"
  - "[[2024-10-03_api-gateway-newsletter]]"
  - "[[2025-08-07_top-strategies-to-improve-reliability-in-distributed-systems-part-1]]"
  - "[[2026-05-28_must-know-failure-modes-in-distributed-systems]]"
source_sections:
  - "[[2024-08-08_a-crash-course-on-microservices-design-patterns-newsletter]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - reliability
  - microservices
---

# Circuit Breaker

## Cách hiểu bằng lời của tôi

[[Circuit Breaker]] là pattern chặn tạm thời request tới một dependency đang lỗi để tránh cascading failure. Thay vì để mọi call tiếp tục timeout và làm cạn thread/connection, circuit breaker mở mạch, fail fast, rồi thử lại có kiểm soát.

## Trạng thái

- Closed: request đi qua bình thường, lỗi được đếm.
- Open: dependency bị xem là không khỏe, request bị chặn hoặc fallback.
- Half-open: cho một lượng nhỏ request thử lại để xem dependency đã phục hồi chưa.

## Trade-off cần nhớ

Circuit breaker bảo vệ hệ thống khỏi lỗi dây chuyền, nhưng threshold sai có thể làm chặn dependency vẫn còn dùng được hoặc mở lại quá sớm.

## Liên kết

- [[Microservices Design Patterns]]
- [[API Gateway]]
- [[Cascading Failure]]
- [[Graceful Degradation]]
- [[Retry Storm]]
- [[Observability]]
