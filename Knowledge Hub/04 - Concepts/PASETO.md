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
  - authentication
---

# PASETO

## Định nghĩa

PASETO là token format thay thế JWT, thiết kế theo hướng opinionated để giảm lỗi cấu hình cryptography.

## Cách hiểu bằng lời của tôi

JWT linh hoạt nhưng dễ dùng sai, nhất là phần algorithm negotiation và payload signed nhưng đọc được. PASETO cố giảm không gian sai bằng version/purpose rõ ràng và thuật toán mạnh theo mặc định.

## Hai purpose

- Local token: payload được mã hóa, có confidentiality.
- Public token: payload được ký, có integrity/authenticity nhưng không giấu nội dung.

## Trade-off

- An toàn theo mặc định hơn JWT ở một số điểm.
- Ecosystem, middleware và adoption nhỏ hơn JWT.
- Team quen JWT cần học lại model và tooling.

## Liên kết

- [[JSON Web Token]]
- [[Authentication]]
- [[API Security]]
