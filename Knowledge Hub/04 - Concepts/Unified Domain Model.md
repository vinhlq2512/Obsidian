---
type: concept
status: seed
sources:
  - "[[2025-07-02_netflix-ended-data-chaos-with-unified-domain-models]]"
source_sections:
  - "[[2025-07-02_netflix-ended-data-chaos-with-unified-domain-models]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - architecture
  - data
---

# Unified Domain Model

## Định nghĩa

[[Unified Domain Model]] là cách định nghĩa entity nghiệp vụ một lần ở tầng khái niệm, rồi project định nghĩa đó ra nhiều schema/API/pipeline mà vẫn giữ cùng semantics.

## Cách hiểu bằng lời của tôi

Khi mỗi service tự định nghĩa "movie", "actor" hay "account" theo cách riêng, hệ thống bắt đầu lệch nghĩa dù vẫn chạy. Unified domain model cố đưa nghĩa nghiệp vụ về một nguồn chung, để GraphQL schema, Avro event, SQL table hay Java API không trôi xa nhau.

## Cơ chế từ nguồn Netflix UDA

- Domain model được định nghĩa một lần cho business entity.
- Hệ thống tự generate schema cụ thể như GraphQL, Avro, SQL hoặc Java API.
- Mapping nối domain model tới data container thật như resolver, table hoặc data product.
- Knowledge graph cho phép search, introspection và traversal quan hệ giữa model, schema, data source.

## Lợi ích

- Giảm schema drift và terminology drift.
- Giảm integration debt khi nhiều team cùng dùng một khái niệm.
- Tách business semantics khỏi implementation detail.
- Tăng tốc thay đổi vì model/schema/pipeline được sinh nhất quán.

## Liên kết

- [[Database Schema Design]]
- [[GraphQL]]
- [[API Contract]]
- [[Commonsense Knowledge Graph]]
- [[Real-Time Graph Architecture]]
