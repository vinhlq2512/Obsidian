---
type: concept
status: developing
sources:
  - "[[2024-12-05_mastering-modern-authentication-cookies-sessions-jwt-and-pas]]"
  - "[[2025-05-24_ep164-jwt-simply-explained]]"
  - "[[2026-04-09_must-know-cross-cutting-concerns-in-api-development]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - security
  - authentication
  - api
---

# JSON Web Token

## Định nghĩa

JSON Web Token (JWT) là token compact, URL-safe, self-contained dùng để truyền claims giữa các bên và thường dùng cho authentication/authorization.

## Cấu trúc

- Header: type và signing algorithm.
- Payload: claims như subject, issuer, expiration, role hoặc custom data.
- Signature: chữ ký để kiểm tính toàn vẹn và nguồn phát hành.

## Cách hiểu bằng lời của tôi

JWT giúp service validate identity mà không cần lookup session server-side cho mỗi request. Điều này scale tốt trong hệ phân tán, nhưng token đã phát hành khó revoke ngay nếu không thêm blacklist, short expiry hoặc refresh-token flow.

## Trade-off bảo mật

- Payload signed không đồng nghĩa encrypted; không nhét secret vào JWT.
- Token bị steal có thể dùng tới khi hết hạn.
- Token quá lớn làm tăng overhead request.
- Cần quản lý key, expiry, audience, issuer và rotation cẩn thận.

## Liên kết

- [[Authentication]]
- [[Authorization]]
- [[Session-Based Authentication]]
- [[PASETO]]
- [[OAuth 2.0]]
- [[API Security]]
