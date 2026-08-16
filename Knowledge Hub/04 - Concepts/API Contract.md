---
type: concept
status: developing
sources:
  - "[[2025-04-03_the-art-of-rest-api-design-idempotency-pagination-and-securi]]"
  - "[[2024-04-18_a-crash-course-in-api-versioning-strategies]]"
  - "[[2026-08-13_a-detailed-guide-to-api-composition-techniques]]"
  - "[[2026-04-09_must-know-cross-cutting-concerns-in-api-development]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - api
  - system-design
---

# API Contract

## Định nghĩa

API contract là thỏa thuận ổn định giữa provider và consumer về endpoint, method, request/response schema, status code, error shape, version và behavior.

## Cách hiểu bằng lời của tôi

API không chỉ là route chạy được. Nó là lời hứa với client. Nếu response hôm nay là `{data, error}` nhưng ngày mai đổi tùy endpoint, mỗi client sẽ phải viết ngoại lệ và niềm tin vào API giảm.

## Cần biết

- Resource naming nên nhất quán và dùng danh từ.
- HTTP method phải giữ semantic: GET không side effect, PUT/DELETE idempotent, POST cần idempotency key nếu có side effect lớn.
- Response shape ổn định giúp shared parser, logging và error handling dễ hơn.
- Schema-first design dùng OpenAPI/Protobuf làm source of truth và contract validation.
- Contract diff nên phát hiện breaking change trước khi deploy.
- Với mobile và third-party integrations, contract cũ có thể sống rất lâu vì client không update ngay; vì vậy backward compatibility và deprecation window quan trọng hơn cảm giác "dọn sạch API".

## Liên kết

- [[REST API]]
- [[API Versioning]]
- [[API Pagination]]
- [[Idempotency Key]]
- [[GraphQL]]
- [[Backend for Frontend]]
- [[API Composition]]
