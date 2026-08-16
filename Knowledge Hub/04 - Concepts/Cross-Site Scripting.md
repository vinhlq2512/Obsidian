---
type: concept
status: seed
sources:
  - "[[2026-04-09_must-know-cross-cutting-concerns-in-api-development]]"
  - "[[2025-10-11_ep184-api-vs-sdk]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - security
  - web
---

# Cross-Site Scripting

## Định nghĩa

Cross-Site Scripting (XSS) là attack trong đó attacker đưa script độc hại vào trang để chạy trong browser của user.

## Cách hiểu bằng lời của tôi

XSS làm browser tin nhầm code của attacker là code của site. Khi chạy được trong context site, script có thể đánh cắp token/cookie không được bảo vệ, thao tác DOM hoặc gửi request thay user.

## Dạng thường gặp

- Stored XSS: payload được lưu trong database rồi chạy cho nhiều user.
- DOM-based XSS: payload thao túng DOM phía browser mà không nhất thiết đi qua server.

## Cách giảm rủi ro

- Escape output theo context.
- Sanitize HTML nếu phải cho phép rich text.
- Dùng Content Security Policy khi phù hợp.
- Dùng HttpOnly cookie để giảm khả năng script đọc token.

## Liên kết

- [[Input Validation]]
- [[API Security]]
- [[Session-Based Authentication]]
