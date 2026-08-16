---
type: concept
status: seed
sources:
  - "[[2024-12-05_mastering-modern-authentication-cookies-sessions-jwt-and-pas]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - security
  - web
---

# Cross-Site Request Forgery

## Định nghĩa

Cross-Site Request Forgery (CSRF) là attack trong đó browser của user đã đăng nhập bị lợi dụng để gửi request không mong muốn tới site tin cậy.

## Cách hiểu bằng lời của tôi

CSRF nguy hiểm với cookie-based auth vì browser tự động gửi cookie theo request. Nếu server chỉ nhìn cookie và không kiểm ý định của user, attacker có thể dụ browser gửi thao tác thay user.

## Cách giảm rủi ro

- Dùng SameSite cookie.
- Dùng CSRF token cho state-changing request.
- Kiểm Origin/Referer khi phù hợp.
- Không dùng GET cho thao tác có side effect.

## Liên kết

- [[Session-Based Authentication]]
- [[API Security]]
- [[Input Validation]]
