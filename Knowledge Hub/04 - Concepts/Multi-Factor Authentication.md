---
type: concept
status: seed
sources:
  - "[[2023-04-12_authentication-methods-passwordless-mfa-sso-oauth-part-2]]"
  - "[[2024-12-05_mastering-modern-authentication-cookies-sessions-jwt-and-pas]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - security
  - authentication
---

# Multi-Factor Authentication

## Định nghĩa

Multi-Factor Authentication (MFA) yêu cầu nhiều hơn một loại bằng chứng để xác minh identity trước khi cho truy cập.

## Cách hiểu bằng lời của tôi

Password là "thứ bạn biết". MFA thêm "thứ bạn có" như phone/security key hoặc "thứ bạn là" như biometrics. Khi một factor bị lộ, attacker vẫn cần factor khác.

## Factor thường gặp

- Something you know: password, PIN.
- Something you have: phone, hardware key, TOTP app.
- Something you are: fingerprint, face recognition.

## Liên kết

- [[Authentication]]
- [[Single Sign-On]]
- [[API Security]]
