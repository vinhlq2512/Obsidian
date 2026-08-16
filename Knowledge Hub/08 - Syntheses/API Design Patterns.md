---
type: synthesis
status: seed
concepts:
  - "[[API Composition]]"
  - "[[Async API Pattern]]"
  - "[[API Protocol]]"
  - "[[API Contract]]"
  - "[[API Security]]"
  - "[[API Lifecycle Management]]"
  - "[[API Documentation]]"
  - "[[Throttling]]"
sources:
  - "[[2026-08-13_a-detailed-guide-to-api-composition-techniques]]"
  - "[[2026-05-21_a-guide-to-async-patterns-in-api-design]]"
  - "[[2025-03-13_api-protocols-101-a-guide-to-choose-the-right-one]]"
  - "[[2026-04-09_must-know-cross-cutting-concerns-in-api-development]]"
  - "[[2025-10-23_api-gateways-101-the-core-of-modern-api-management-security]]"
  - "[[2026-01-29_how-to-scale-an-api]]"
created_at: 2026-08-16
updated_at: 2026-08-16
tags:
  - synthesis
  - api
  - system-design
---

# API Design Patterns

## Ý chính

Thiết kế API tốt không chỉ là đặt endpoint đẹp. Nó là tổ hợp của contract ổn định, protocol phù hợp, composition đúng chỗ, async pattern đúng use case và cross-cutting concerns được áp dụng đồng nhất.

## Map quyết định

| Câu hỏi | Pattern liên quan | Ghi nhớ |
|---|---|---|
| Client cần gom dữ liệu từ nhiều service? | [[API Composition]] | Chọn client, gateway, BFF, GraphQL hoặc edge theo round trip, cache và ownership |
| Các call độc lập hay phụ thuộc nhau? | [[API Aggregation]], [[API Orchestration]] | Parallel giảm latency; chain làm latency cộng dồn |
| Work/event không fit request-response? | [[Async API Pattern]] | Chọn polling, SSE, WebSocket, webhook hoặc queue theo direction/durability |
| Public/simple CRUD hay internal high-performance? | [[API Protocol]] | REST dễ dùng; gRPC nhanh; GraphQL linh hoạt; SSE/WebSocket cho realtime |
| Concern nào phải chạy trên mọi route? | [[API Security]], [[Input Validation]], [[Rate Limiting]] | Partial coverage tạo false confidence |
| API sẽ thay đổi theo thời gian? | [[API Lifecycle Management]], [[API Versioning]], [[API Documentation]] | Version, deprecation và docs là một phần của contract |

## Mental model

```text
API product surface
-> contract và versioning
-> protocol/transport
-> composition hoặc async flow
-> auth/rate limit/validation/logging
-> observability và failure handling
```

## Liên kết

- [[System Design]]
- [[REST API]]
- [[GraphQL]]
- [[API Gateway]]
- [[Backend for Frontend]]
- [[Modern Web Request Architecture]]
