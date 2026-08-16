---
type: concept
status: seed
sources:
  - "[[2026-02-24_how-uber-reinvented-access-control-for-microservices]]"
source_sections:
  - "[[2026-02-24_how-uber-reinvented-access-control-for-microservices]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - security
  - authorization
---

# Attribute-Based Access Control

## Định nghĩa

[[Attribute-Based Access Control]] là access control model dùng policy condition dựa trên attributes của actor, resource, action và environment để quyết định allow/deny.

## Cách hiểu bằng lời của tôi

ABAC hữu ích khi role không đủ diễn đạt business rule. Ví dụ support chỉ được xem payment của khách ở vùng mình phụ trách, hoặc employee chỉ được xem hồ sơ của chính mình hay người mình quản lý. Quyền không còn là danh sách tĩnh; nó là biểu thức được evaluate với context runtime.

## Cơ chế từ Uber Charter

```text
request(actor, action, resource)
-> match policy cơ bản
-> nếu policy có condition, expression engine tìm attributes cần dùng
-> lấy attributes từ [[Policy Information Point]]
-> evaluate boolean expression
-> allow/deny
```

## Lợi ích

- Một policy tổng quát có thể áp cho nhiều resource.
- Attribute thay đổi thì decision thay đổi mà không cần deploy code.
- Tách policy khỏi business logic giúp audit và governance dễ hơn.
- Có thể bảo vệ microservice endpoint, database query, Kafka topic và internal tools.

## Liên kết

- [[Fine-Grained Authorization]]
- [[Authorization]]
- [[Policy Information Point]]
- [[Apache Kafka]]
- [[Microservices Design Patterns]]
