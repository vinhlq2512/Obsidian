---
type: concept
status: seed
sources:
  - "[[2025-09-25_graphql-101-api-approach-beyond-rest-newsletter]]"
  - "[[2024-05-16_a-crash-course-in-graphql-newsletter]]"
  - "[[2026-08-13_a-detailed-guide-to-api-composition-techniques]]"
  - "[[2025-03-13_api-protocols-101-a-guide-to-choose-the-right-one]]"
  - "[[2025-06-03_how-netflix-runs-on-java]]"
source_sections:
  - "[[2025-09-25_graphql-101-api-approach-beyond-rest-newsletter]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - api
  - system-design
---

# GraphQL

## Cách hiểu bằng lời của tôi

[[GraphQL]] là cách xây API nơi client mô tả chính xác shape dữ liệu cần lấy. Thay vì nhiều endpoint REST cố định, GraphQL thường expose một schema typed và resolver để lấy dữ liệu từ nhiều nguồn.

## Khi hữu ích

- Client đa dạng cần shape dữ liệu khác nhau.
- Muốn giảm over-fetching/under-fetching.
- Frontend cần compose nhiều resource trong một round trip.
- API cần schema discoverable và tooling tốt.

## Trade-off cần nhớ

GraphQL chuyển một phần complexity sang query planning, resolver performance, authorization theo field, caching, rate limiting theo query cost và chống N+1 query. Nó không tự động làm backend đơn giản hơn.

Khi GraphQL làm composition layer, resolver có thể tạo N+1 upstream calls nếu không batching. Vì response phụ thuộc query document, caching thường chuyển từ HTTP URL cache sang entity/field-level caching trong application.

## Federation ở backend lớn

Nguồn Netflix mô tả cách tách schema thành nhiều Domain Graph Service. Mỗi team sở hữu schema fragment và resolver của domain mình, còn gateway compose thành graph chung. Pattern này tăng độc lập deploy nhưng làm query fan-out chạm nhiều service, nên timeout, fallback và observability ở resolver là bắt buộc.

## Liên kết

- [[REST API]]
- [[API Gateway]]
- [[Rate Limiting]]
- [[API Composition]]
- [[GraphQL Subscription]]
- [[API Protocol]]
- [[GraphQL Federation]]
