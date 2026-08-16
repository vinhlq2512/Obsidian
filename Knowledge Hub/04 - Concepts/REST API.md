---
type: concept
status: understood
sources:
  - "[[2024-05-30_a-crash-course-on-rest-apis-newsletter]]"
  - "[[2024-02-22_how-to-design-a-good-api-newsletter]]"
  - "[[2025-04-03_the-art-of-rest-api-design-idempotency-pagination-and-securi]]"
  - "[[2025-03-13_api-protocols-101-a-guide-to-choose-the-right-one]]"
source_sections:
  - "[[2024-05-30_a-crash-course-on-rest-apis-newsletter]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - api
  - system-design
---

# REST API

## Cách hiểu bằng lời của tôi

[[REST API]] là cách thiết kế API quanh resource, URL và HTTP method. Client thao tác với resource bằng các động từ chuẩn như GET, POST, PUT, PATCH, DELETE. Thiết kế tốt làm API dễ đoán, dễ version, dễ cache và dễ vận hành.

## Thành phần cần nhớ

- Resource: danh từ nghiệp vụ được expose qua endpoint.
- HTTP method: biểu diễn intent của thao tác.
- Status code: phản hồi kết quả theo quy ước HTTP.
- Pagination/filtering/sorting: kiểm soát dữ liệu trả về.
- Versioning: cho phép API tiến hóa mà không phá client cũ.
- Response shape nên nhất quán để client dùng shared parser và xử lý lỗi ổn định.
- Schema-first design với OpenAPI/Protobuf giúp phát hiện contract drift sớm.

## Trade-off cần nhớ

REST đơn giản và phổ biến, nhưng có thể tạo over-fetching/under-fetching khi client cần shape dữ liệu khác nhau. Với view cần gom nhiều resource, có thể cần [[API Gateway]], BFF hoặc cân nhắc [[GraphQL]].

REST cũng hưởng lợi trực tiếp từ HTTP caching, status code và tooling phổ biến. Nếu use case chuyển sang realtime, streaming hoặc service-to-service hiệu năng cao, nên cân nhắc [[Server-Sent Events]], [[WebSocket]] hoặc [[gRPC]] thay vì cố nhồi mọi thứ vào request-response JSON.

## Liên kết

- [[API Gateway]]
- [[Idempotency Key]]
- [[API Versioning]]
- [[API Pagination]]
- [[API Security]]
- [[API Contract]]
- [[Rate Limiting]]
- [[GraphQL]]
- [[API Protocol]]
- [[Async API Pattern]]
