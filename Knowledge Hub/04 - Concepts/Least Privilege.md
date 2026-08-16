---
type: concept
status: seed
sources:
  - "[[2026-03-26_how-to-implement-api-security]]"
  - "[[2025-09-08_how-grab-built-an-authentication-system-for-180-million-user]]"
  - "[[2026-02-24_how-uber-reinvented-access-control-for-microservices]]"
source_sections:
  - "[[2026-03-26_how-to-implement-api-security]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - security
  - authorization
---

# Least Privilege

## Định nghĩa

[[Least Privilege]] là nguyên tắc chỉ cấp cho user, service, token hoặc workload đúng quyền tối thiểu cần để hoàn thành nhiệm vụ.

## Cách hiểu bằng lời của tôi

Least privilege giảm blast radius khi credential, token hoặc service bị compromise. Thay vì service account có quyền rộng, hệ thống nên dùng scope/audience hẹp, policy theo resource/action cụ thể, và context như attribute hoặc relationship khi cần.

## Khi áp dụng

- Token access nên có expiry, scope và audience cụ thể.
- Service-to-service call nên tránh credential dùng chung quá mạnh.
- Policy nên kiểm resource/action, không chỉ kiểm login.
- Admin/break-glass quyền cao cần audit và quy trình rõ.

## Liên kết

- [[Authorization]]
- [[Token Exchange]]
- [[Fine-Grained Authorization]]
- [[Attribute-Based Access Control]]
- [[Blast Radius]]
