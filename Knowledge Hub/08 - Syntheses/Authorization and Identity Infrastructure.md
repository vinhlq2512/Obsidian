---
type: synthesis
status: seed
concepts:
  - "[[Authentication]]"
  - "[[Authorization]]"
  - "[[OpenID Connect]]"
  - "[[Fine-Grained Authorization]]"
  - "[[Attribute-Based Access Control]]"
  - "[[Relationship-Based Access Control]]"
  - "[[Google Zanzibar]]"
  - "[[Permission Tuple]]"
  - "[[Authorization Consistency Token]]"
  - "[[Policy Information Point]]"
  - "[[Token Exchange]]"
  - "[[Federated Identity Provider]]"
sources:
  - "[[2026-01-27_how-google-manages-trillions-of-authorizations-with-zanzibar]]"
  - "[[2026-02-24_how-uber-reinvented-access-control-for-microservices]]"
  - "[[2025-09-08_how-grab-built-an-authentication-system-for-180-million-user]]"
questions: []
created_at: 2026-08-16
updated_at: 2026-08-16
tags:
  - synthesis
  - security
  - system-design
  - bytebytego
---

# Authorization and Identity Infrastructure

## Ý chính

Identity infrastructure tách thành hai lớp: [[Authentication]] xác minh caller là ai, còn [[Authorization]] quyết định caller được làm gì trên resource nào. Ở quy mô lớn, hai lớp này cần chuẩn hóa token, tách policy khỏi code, cache có kiểm soát, và consistency guarantee cho quyền vừa thay đổi.

## Ba case chính

- Grab/Dex: chuẩn hóa login bằng [[OpenID Connect]], federation qua nhiều IdP và [[Token Exchange]] để tránh service account rộng quyền.
- Uber/Charter: dùng [[Attribute-Based Access Control]] để policy dựa trên actor/resource/action/environment attributes.
- Google Zanzibar: dùng [[Relationship-Based Access Control]], [[Permission Tuple]] và [[Authorization Consistency Token]] để phục vụ permission checks global mà vẫn giữ correctness.

## Câu hỏi thiết kế

- Authentication token có audience/scope đủ hẹp không?
- Authorization model nên là RBAC, ABAC, ReBAC hay kết hợp?
- Policy nằm trong code, config hay service trung tâm?
- Attribute/relationship data có stale được không?
- Revoke quyền cần freshness mạnh tới đâu?
- Client nóng có bị quota để không ảnh hưởng tenant khác không?

## Liên kết

- [[API Security]]
- [[Service Mesh]]
- [[Blast Radius]]
- [[Data Replication]]
- [[Caching Strategy]]
