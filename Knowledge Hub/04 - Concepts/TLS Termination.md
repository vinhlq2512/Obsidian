---
type: concept
status: seed
sources:
  - "[[2025-10-23_api-gateways-101-the-core-of-modern-api-management-security]]"
  - "[[2026-06-04_the-path-of-a-request-a-tour-of-modern-web-architecture]]"
source_sections:
  - "[[2025-10-23_api-gateways-101-the-core-of-modern-api-management-security]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - security
  - networking
---

# TLS Termination

## Định nghĩa

[[TLS Termination]] là việc kết thúc kết nối HTTPS/TLS tại gateway, load balancer, reverse proxy hoặc CDN để layer đó giải mã request trước khi chuyển tiếp nội bộ.

## Cách hiểu bằng lời của tôi

TLS termination đặt trust boundary ở edge. Nó giúp centralize certificate management, inspect/rate-limit/log request và giảm gánh TLS cho backend. Đổi lại, traffic nội bộ sau termination phải được bảo vệ bằng network policy, mTLS hoặc trusted network tùy threat model.

## Liên kết

- [[API Gateway]]
- [[Reverse Proxy]]
- [[API Security]]
- [[Service Mesh]]
- [[Authentication]]
