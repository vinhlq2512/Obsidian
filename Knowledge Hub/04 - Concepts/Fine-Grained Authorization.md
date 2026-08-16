---
type: concept
status: seed
sources:
  - "[[2026-01-27_how-google-manages-trillions-of-authorizations-with-zanzibar]]"
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

# Fine-Grained Authorization

## Định nghĩa

[[Fine-Grained Authorization]] là authorization kiểm quyền ở mức actor, action, resource và context cụ thể, thay vì chỉ hỏi user thuộc role chung nào.

## Cách hiểu bằng lời của tôi

Khi hệ thống nhỏ, rule kiểu "admin được đọc mọi thứ" có thể đủ. Khi sản phẩm có nhiều resource, tenant, vùng địa lý, ownership và privacy rule, authorization phải trả lời câu chi tiết hơn: ai, làm gì, trên object nào, trong điều kiện nào, với dữ liệu mới tới mức nào.

## Hai hướng phổ biến

- [[Attribute-Based Access Control]]: quyết định dựa trên thuộc tính của actor/resource/action/environment.
- [[Relationship-Based Access Control]]: quyết định dựa trên quan hệ giữa user, group, folder, document, channel hoặc object.

## Trade-off

- Chính xác hơn RBAC thô, nhưng policy/model phức tạp hơn.
- Cần audit, test và observability cho decision path.
- Caching giúp latency nhưng phải cẩn thận với quyền vừa bị revoke.
- Policy nên tách khỏi application code để dễ thay đổi và review.

## Liên kết

- [[Authorization]]
- [[Attribute-Based Access Control]]
- [[Relationship-Based Access Control]]
- [[Google Zanzibar]]
- [[Policy Information Point]]
