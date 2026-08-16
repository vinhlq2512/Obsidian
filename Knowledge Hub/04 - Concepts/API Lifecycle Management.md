---
type: concept
status: seed
sources:
  - "[[2025-10-23_api-gateways-101-the-core-of-modern-api-management-security]]"
  - "[[2026-01-29_how-to-scale-an-api]]"
source_sections:
  - "[[2025-10-23_api-gateways-101-the-core-of-modern-api-management-security]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - api
  - system-design
---

# API Lifecycle Management

## Định nghĩa

[[API Lifecycle Management]] là quá trình quản lý API từ thiết kế, phát hành, versioning, documentation, monitoring, deprecation tới sunset.

## Cách hiểu bằng lời của tôi

API là contract sống lâu hơn code bên trong service. Lifecycle management giúp thay đổi API mà không đẩy rủi ro sang client: version cũ vẫn chạy, version mới có migration path, deprecated endpoint có ngày sunset, và usage/latency/error được quan sát.

## Cần có

- [[API Contract]] rõ.
- [[API Versioning]] cho breaking changes.
- [[API Documentation]] và migration guide.
- Deprecation/sunset policy.
- Observability theo endpoint/version/client.
- Gateway routing để nhiều version cùng tồn tại.

## Liên kết

- [[API Gateway]]
- [[API Versioning]]
- [[Backward Compatibility]]
- [[API Documentation]]
- [[API Design Patterns]]
