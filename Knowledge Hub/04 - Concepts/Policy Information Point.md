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

# Policy Information Point

## Định nghĩa

[[Policy Information Point]] là nguồn cung cấp attributes cho authorization engine khi evaluate policy condition trong mô hình ABAC.

## Cách hiểu bằng lời của tôi

Policy nói "cho phép nếu actor.location == resource.location", nhưng engine cần biết hai giá trị đó lấy ở đâu. PIP là cầu nối tới employee directory, ownership service, resource metadata, environment context hoặc hệ thống domain khác.

## Cần thiết kế

- Attribute nào store này hỗ trợ.
- Latency và availability của attribute lookup.
- Caching/freshness của attribute.
- Failure mode: thiếu attribute thì deny, fallback hay error.
- Audit: decision dùng attribute nào, từ nguồn nào.

## Liên kết

- [[Attribute-Based Access Control]]
- [[Fine-Grained Authorization]]
- [[Authorization]]
- [[Latency]]
- [[High Availability]]
