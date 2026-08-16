---
type: concept
status: seed
sources:
  - "[[2025-06-03_how-netflix-runs-on-java]]"
source_sections:
  - "[[2025-06-03_how-netflix-runs-on-java]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - api
  - system-design
---

# GraphQL Federation

## Định nghĩa

[[GraphQL Federation]] là cách chia một GraphQL schema lớn thành nhiều phần do các service/domain team sở hữu, rồi compose lại thành một graph chung cho client.

## Cách hiểu bằng lời của tôi

GraphQL federation cố giữ trải nghiệm client như một schema thống nhất, nhưng không ép một team trung tâm sở hữu toàn bộ backend. Mỗi domain service sở hữu phần schema và resolver của mình; gateway/registry biết field nào thuộc service nào.

## Cơ chế từ nguồn Netflix

- Client gọi một GraphQL gateway/schema chung.
- Mỗi team sở hữu một Domain Graph Service cho lát cắt domain của mình.
- Service đăng ký schema fragment vào registry chung.
- Gateway dùng registry để route field resolver tới service đúng.
- Bên trong backend, service có thể dùng gRPC hoặc datastore riêng để resolve field.

## Trade-off

- Tăng độc lập deploy và schema-driven collaboration.
- Dễ sinh fan-out sâu: một query client có thể chạm nhiều service và datastore.
- Cần timeout, fallback, retry và query-cost control để một resolver chậm không kéo cả response.
- Authorization/caching/observability phải đi tới cấp field/resolver, không chỉ endpoint.

## Liên kết

- [[GraphQL]]
- [[API Gateway]]
- [[API Composition]]
- [[Service Mesh]]
- [[Timeout]]
- [[Cascading Failure]]
