---
type: concept
status: developing
sources:
  - "[[2024-12-05_mastering-modern-authentication-cookies-sessions-jwt-and-pas]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - security
  - authentication
---

# Session-Based Authentication

## Định nghĩa

Session-based authentication là cơ chế server lưu session state, còn client giữ session ID thường qua cookie.

## Cách hiểu bằng lời của tôi

Client không giữ toàn bộ identity data. Nó chỉ giữ một khóa tham chiếu; server dùng khóa đó để đọc session thật. Cách này revoke dễ và kiểm soát server-side tốt, nhưng cần session store khi scale nhiều server.

## Trade-off

- Dễ invalidate khi logout hoặc phát hiện rủi ro.
- Session data không phơi ra client.
- Cần centralized session store hoặc sticky session trong distributed systems.
- Cookie cần HttpOnly, Secure, SameSite và TTL hợp lý.

## Liên kết

- [[Authentication]]
- [[JSON Web Token]]
- [[API Security]]
- [[Cross-Site Request Forgery]]
