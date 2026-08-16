---
type: concept
status: understood
sources:
  - "[[2024-08-29_a-crash-course-on-load-balancers-for-scaling]]"
  - "[[2023-02-15_from-0-to-millions-a-guide-to-scaling-your-app-part-1-newsletter]]"
source_sections:
  - "[[2024-08-29_a-crash-course-on-load-balancers-for-scaling]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - system-design
---

# Load Balancer

## Cách hiểu bằng lời của tôi

[[Load Balancer]] phân phối request qua nhiều instance để đạt hai mục tiêu: chia tải và redundancy. Khi traffic tăng, ta thêm instance; load balancer quyết định instance nào nhận request. Khi một instance unhealthy, traffic được chuyển đi nơi khác để giảm downtime.

## Layer 4 và Layer 7

- Layer 4 nhìn ở tầng transport, dựa vào IP/port. Nó đơn giản, nhanh, ít phải hiểu payload.
- Layer 7 nhìn ở tầng application như HTTP path, header, cookie. Nó route thông minh hơn, có thể cache, terminate TLS, rewrite URL, nhưng chi phí xử lý cao hơn.

## Thuật toán phân phối

- Round robin: đơn giản, chia đều theo lượt.
- Least connections: ưu tiên server đang ít kết nối hơn.
- Weighted routing: server mạnh hơn nhận nhiều traffic hơn.
- Sticky session: giữ cùng user trên cùng instance, nhưng dễ gây lệch tải và làm state khó scale.

## Trade-off cần nhớ

- Load balancer giải quyết bottleneck app server nhưng chính nó cũng cần HA.
- L7 thông minh hơn nhưng tốn CPU/memory hơn L4.
- Sticky session có thể tiện trong ngắn hạn nhưng làm giảm khả năng thay thế instance.

## Liên kết

- [[High Availability]]
- [[API Gateway]]
- [[Horizontal Scaling]]
- [[Scalable Distributed Systems Patterns]]
