---
type: concept
status: understood
sources:
  - "[[2024-10-03_api-gateway-newsletter]]"
  - "[[2024-08-08_a-crash-course-on-microservices-design-patterns-newsletter]]"
  - "[[2025-10-23_api-gateways-101-the-core-of-modern-api-management-security]]"
  - "[[2026-08-13_a-detailed-guide-to-api-composition-techniques]]"
  - "[[2026-04-09_must-know-cross-cutting-concerns-in-api-development]]"
source_sections:
  - "[[2024-10-03_api-gateway-newsletter]]"
  - "[[2024-08-08_a-crash-course-on-microservices-design-patterns-newsletter]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - system-design
  - api
---

# API Gateway

## Cách hiểu bằng lời của tôi

[[API Gateway]] là cửa vào thống nhất cho client khi backend đã có nhiều service. Nó che bớt topology nội bộ, gom các cross-cutting concerns ở edge, và giúp client không phải tự biết gọi service nào, version nào, protocol nào.

Gateway không chỉ là reverse proxy. Trong hệ microservices, nó thường kiêm routing, authentication, authorization, rate limiting, caching, request aggregation, protocol translation, logging, monitoring và đôi khi circuit breaker.

## Cơ chế

```text
Client request
-> API Gateway
-> xác thực / phân quyền / rate limit / logging
-> route hoặc compose request tới service phù hợp
-> transform response nếu cần
-> trả response thống nhất về client
```

## Policy và lifecycle ở gateway

Gateway thường là nơi thực thi [[TLS Termination]], request routing, [[API Lifecycle Management]], version routing, [[Throttling]], caching, logging, schema validation và security policy. Nguồn API Gateway 101 nhấn mạnh gateway hữu ích nhất khi nó giữ cross-cutting concerns nhất quán, nhưng không nhồi business logic riêng của từng domain vào đây.

## Khi nào hữu ích

- Client cần một endpoint ổn định dù backend có nhiều service.
- Nhiều service dùng protocol khác nhau nhưng client cần interface đơn giản.
- Muốn centralize auth, quota, logging, monitoring.
- Muốn aggregate nhiều call backend thành một response để giảm round trip.

## Trade-off cần nhớ

- Gateway có thể thành bottleneck hoặc single point of failure nếu không scale/HA tốt.
- Quá nhiều logic nghiệp vụ trong gateway làm nó biến thành monolith mới.
- Centralization giúp quản trị dễ hơn nhưng cũng tăng blast radius khi config sai.
- Gateway phù hợp với cross-cutting concerns chung như auth, rate limit, TLS termination, routing, logging và metrics. Nếu response logic chỉ phục vụ một screen/client, [[Backend for Frontend]] thường giữ ownership tốt hơn.

## Liên kết

- [[Rate Limiting]]
- [[Throttling]]
- [[Load Balancer]]
- [[Reverse Proxy]]
- [[TLS Termination]]
- [[Service Discovery]]
- [[Circuit Breaker]]
- [[Microservices Design Patterns]]
- [[API Composition]]
- [[Backend for Frontend]]
- [[API Security]]
- [[API Lifecycle Management]]
