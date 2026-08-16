---
type: concept
status: seed
sources:
  - "[[2025-09-08_how-grab-built-an-authentication-system-for-180-million-user]]"
source_sections:
  - "[[2025-09-08_how-grab-built-an-authentication-system-for-180-million-user]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - security
  - authentication
---

# Federated Identity Provider

## Định nghĩa

[[Federated Identity Provider]] là identity layer trung gian cho phép nhiều application dùng chung chuẩn login/token trong khi vẫn kết nối được với nhiều identity provider phía sau.

## Cách hiểu bằng lời của tôi

Federation giúp app không phải tích hợp riêng từng IdP và từng biến thể OAuth/OIDC. App tin một provider chuẩn hóa token; provider đó nói chuyện với Google, Microsoft hoặc IdP nội bộ. Khi cần failover IdP, layer trung gian có thể đổi backend mà app ít phải thay đổi.

## Pattern từ Grab Dex

- Dex đóng vai trò OIDC provider trung gian.
- Ứng dụng nhận token OIDC chuẩn thay vì custom OAuth flow.
- Có thể thêm IdP mới tập trung.
- Multi-IdP failover giảm downtime khi IdP bên ngoài lỗi.

## Liên kết

- [[OpenID Connect]]
- [[Single Sign-On]]
- [[Authentication]]
- [[Token Exchange]]
- [[High Availability]]
