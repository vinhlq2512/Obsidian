---
type: concept
status: understood
sources:
  - "[[2024-08-08_a-crash-course-on-microservices-design-patterns-newsletter]]"
  - "[[2025-01-16_from-monolith-to-microservices-key-transition-patterns]]"
  - "[[2025-05-22_api-gateway-vs-service-mesh-which-one-do-you-need]]"
source_sections:
  - "[[2024-08-08_a-crash-course-on-microservices-design-patterns-newsletter]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - microservices
  - system-design
---

# Microservices Design Patterns

## Cách hiểu bằng lời của tôi

[[Microservices Design Patterns]] là các lời giải lặp lại cho vấn đề xuất hiện khi hệ thống bị chia thành nhiều service độc lập. Microservices cho phép scale, deploy và ownership theo service, nhưng đổi lại là consistency, network failure, observability, security và data ownership phức tạp hơn.

## Pattern chính

- Database per service: mỗi service sở hữu data của mình, giảm coupling nhưng làm cross-service transaction khó hơn.
- API Gateway: một cửa vào cho client, xử lý routing và cross-cutting concerns.
- Backends for Frontends: backend riêng cho từng loại client để tránh một API chung quá méo mó.
- CQRS: tách read path và write path khi hai nhu cầu khác nhau rõ rệt.
- Event Sourcing: lưu chuỗi event thay vì chỉ lưu state hiện tại.
- Saga: điều phối transaction dài qua nhiều service bằng local transaction và compensation.
- Sidecar: tách chức năng operational như logging, proxy, config ra container/process bên cạnh service.
- Circuit Breaker: chặn gọi service đang lỗi để tránh cascading failure.

## Trade-off cần nhớ

Pattern không phải checklist để áp dụng hết. Mỗi pattern giải quyết một loại pain nhưng thêm một loại complexity. Nếu team chưa có observability, automation và ownership rõ, microservices dễ biến lỗi local thành lỗi hệ thống khó debug.

## Liên kết

- [[API Gateway]]
- [[Message Broker]]
- [[Observability]]
- [[Eventual Consistency]]
- [[Circuit Breaker]]
