---
type: concept
status: seed
sources:
  - "[[2026-03-26_how-to-implement-api-security]]"
  - "[[2024-12-05_mastering-modern-authentication-cookies-sessions-jwt-and-pas]]"
  - "[[2023-04-12_authentication-methods-passwordless-mfa-sso-oauth-part-2]]"
  - "[[2025-09-08_how-grab-built-an-authentication-system-for-180-million-user]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - security
  - api
---

# Authentication

## Định nghĩa

Authentication là quá trình xác minh caller là ai, thường bằng session, API key, OAuth token, JWT hoặc credential khác.

## Cách hiểu bằng lời của tôi

Authentication trả lời câu hỏi "bạn là ai?". Nó không trả lời "bạn có được phép làm việc này không"; câu hỏi đó thuộc [[Authorization]].

## Cần biết

- API key đơn giản nhưng giống password dài, cần giữ kín và rotate.
- Token nên có expiry và scope phù hợp.
- Log không nên ghi credential hoặc secret.
- HTTPS bảo vệ token trên đường truyền nhưng không cứu được token bị leak.
- Session-based auth dễ revoke hơn nhưng cần server-side session store khi scale.
- JWT stateless hơn nhưng khó revoke ngay sau khi đã phát hành.
- SSO/OIDC giúp nhiều app dùng chung identity provider thay vì mỗi app tự quản credential.
- Federated identity layer như Dex có thể chuẩn hóa OIDC token cho nhiều app và nhiều IdP.
- Token exchange giúp service-to-service call giữ scope/audience hẹp hơn service account rộng quyền.

## Liên kết

- [[API Security]]
- [[Authorization]]
- [[Session-Based Authentication]]
- [[JSON Web Token]]
- [[OAuth 2.0]]
- [[OpenID Connect]]
- [[Single Sign-On]]
- [[Multi-Factor Authentication]]
- [[Federated Identity Provider]]
- [[Token Exchange]]
- [[Structured Logging]]
