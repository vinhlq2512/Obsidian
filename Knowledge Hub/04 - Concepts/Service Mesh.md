---
type: concept
status: seed
sources:
  - "[[2025-05-22_api-gateway-vs-service-mesh-which-one-do-you-need]]"
  - "[[2024-08-08_a-crash-course-on-microservices-design-patterns-newsletter]]"
source_sections:
  - "[[2025-05-22_api-gateway-vs-service-mesh-which-one-do-you-need]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - microservices
  - system-design
---

# Service Mesh

## Cách hiểu bằng lời của tôi

[[Service Mesh]] là lớp hạ tầng quản lý service-to-service communication bên trong hệ thống. Nếu [[API Gateway]] kiểm soát traffic đi vào từ bên ngoài, service mesh kiểm soát traffic nội bộ giữa các service.

## Cơ chế

Service mesh thường dùng sidecar proxy cạnh mỗi service instance. Proxy chặn inbound/outbound traffic và áp policy mà application code không cần tự implement.

## Khi hữu ích

- Hệ có nhiều microservices và cần traffic policy nhất quán.
- Muốn mTLS, identity, authorization nội bộ.
- Muốn telemetry/tracing giữa service mà không sửa nhiều code.
- Cần advanced traffic control như canary, retries, timeout, circuit breaking ở hạ tầng.

## Trade-off cần nhớ

Service mesh thêm control plane, sidecar overhead, config complexity và một lớp debug mới. Nếu hệ còn nhỏ, gateway + library pattern có thể đủ.

## Liên kết

- [[API Gateway]]
- [[Microservices Design Patterns]]
- [[Observability]]
- [[Circuit Breaker]]
