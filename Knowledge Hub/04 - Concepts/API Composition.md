---
type: concept
status: developing
sources:
  - "[[2026-08-13_a-detailed-guide-to-api-composition-techniques]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - api
  - system-design
---

# API Composition

## Định nghĩa

API composition là việc fan-out tới nhiều service/source rồi merge kết quả thành một response phù hợp với client hoặc use case.

## Cách hiểu bằng lời của tôi

Khi dữ liệu bị chia theo service boundary, không còn một query database duy nhất để join mọi thứ cho màn hình. Composition là nơi ta quyết định join đó chạy ở đâu: client, server, gateway, BFF, GraphQL layer hoặc edge.

## Cơ chế

```text
client cần một view
-> composition point gọi nhiều upstream
-> gom/biến đổi dữ liệu
-> xử lý partial failure
-> trả response theo shape client cần
```

## Trade-off

- Giảm round trip qua mạng chậm, nhất là mobile-to-datacenter.
- Làm availability của response phụ thuộc vào nhiều upstream.
- Response càng personalized càng khó cache.
- Nếu composition chứa product logic trong shared gateway, nó dễ thành bottleneck tổ chức.

## Liên kết

- [[API Aggregation]]
- [[API Orchestration]]
- [[Backend for Frontend]]
- [[API Gateway]]
- [[GraphQL]]
- [[Partial Failure]]
