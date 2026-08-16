---
type: concept
status: seed
sources:
  - "[[2023-04-12_authentication-methods-passwordless-mfa-sso-oauth-part-2]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - security
  - authentication
---

# Single Sign-On

## Định nghĩa

Single Sign-On (SSO) là cơ chế cho phép user đăng nhập một lần rồi truy cập nhiều ứng dụng bằng cùng một phiên xác thực.

## Cách hiểu bằng lời của tôi

SSO gom login về một identity provider hoặc central authentication service. App con không tự hỏi password nữa; nó redirect user qua nơi xác thực chung rồi nhận ticket/token để biết user đã login.

## Protocol thường gặp

- SAML phổ biến trong enterprise, dùng XML assertion.
- [[OpenID Connect]] phổ biến trong consumer/web/mobile app hiện đại.

## Liên kết

- [[Authentication]]
- [[OAuth 2.0]]
- [[OpenID Connect]]
- [[JSON Web Token]]
