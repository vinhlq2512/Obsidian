---
type: concept
status: developing
sources:
  - "[[2026-03-26_how-to-implement-api-security]]"
  - "[[2024-05-23_api-security-best-practices]]"
  - "[[2025-04-03_the-art-of-rest-api-design-idempotency-pagination-and-securi]]"
  - "[[2026-04-09_must-know-cross-cutting-concerns-in-api-development]]"
  - "[[2024-12-05_mastering-modern-authentication-cookies-sessions-jwt-and-pas]]"
  - "[[2025-10-23_api-gateways-101-the-core-of-modern-api-management-security]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - api
  - security
  - system-design
---

# API Security

## Định nghĩa

API security là tập hợp kiểm soát bảo vệ API khỏi truy cập trái phép, input độc hại, abuse/overload và rò rỉ thông tin.

## Cách hiểu bằng lời của tôi

API có HTTPS và API key chưa chắc đã an toàn. HTTPS bảo vệ đường truyền, authentication xác minh danh tính, còn authorization mới quyết định caller được phép thao tác resource nào.

## Threat categories

- Unauthorized access: sai người hoặc sai quyền truy cập dữ liệu/chức năng.
- Malicious or malformed input: input làm hệ thống crash, corrupt hoặc bị injection.
- Abuse and overload: brute-force, scraping, client lỗi hoặc traffic bất thường.
- Information leakage: lỗi quá chi tiết, trả thừa field, log lộ secret, access control không nhất quán.

## Kiểm soát chính

- HTTPS/TLS để bảo vệ in-transit data.
- [[Authentication]] để xác minh caller.
- [[Authorization]] và least privilege để kiểm tra quyền theo resource/action.
- [[Input Validation]] server-side với allowlist/schema.
- [[Rate Limiting]] và throttling để chống volume.
- [[TLS Termination]] và certificate management ở edge/gateway để bảo vệ traffic vào hệ thống.
- [[Structured Logging]] và monitoring để phát hiện/analyze incident.
- Cross-cutting concerns phải được áp dụng đồng nhất; auth/validation/logging phủ 95% endpoint đôi khi nguy hiểm hơn 0% vì tạo false confidence.

## Liên kết

- [[REST API]]
- [[API Gateway]]
- [[Rate Limiting]]
- [[Throttling]]
- [[TLS Termination]]
- [[Structured Logging]]
- [[JSON Web Token]]
- [[OAuth 2.0]]
- [[SQL Injection]]
- [[Cross-Site Scripting]]
- [[LLM Security]]
