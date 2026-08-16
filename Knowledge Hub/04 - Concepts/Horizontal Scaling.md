---
type: concept
status: seed
sources:
  - "[[2024-08-29_a-crash-course-on-load-balancers-for-scaling]]"
  - "[[2025-08-07_top-scalability-strategies-for-real-world-load-part-1]]"
source_sections:
  - "[[2024-08-29_a-crash-course-on-load-balancers-for-scaling]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - system-design
---

# Horizontal Scaling

## Cách hiểu bằng lời của tôi

[[Horizontal Scaling]] là tăng capacity bằng cách thêm nhiều instance/node thay vì làm một máy mạnh hơn. Nó là nền của app tier sau [[Load Balancer]], nhưng chỉ hiệu quả khi state được externalize hoặc phân phối đúng cách.

## Trade-off cần nhớ

- Tăng fault tolerance vì mất một node không làm mất toàn bộ service.
- Cần load balancing, health check, deployment coordination.
- Stateful component khó scale ngang hơn stateless component.
- Khi chuyển bottleneck khỏi app tier, database hoặc downstream service có thể trở thành điểm nghẽn mới.

## Liên kết

- [[Load Balancer]]
- [[Database Sharding]]
- [[High Availability]]
