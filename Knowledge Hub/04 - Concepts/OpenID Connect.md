---
type: concept
status: seed
sources:
  - "[[2023-04-12_authentication-methods-passwordless-mfa-sso-oauth-part-2]]"
  - "[[2025-09-08_how-grab-built-an-authentication-system-for-180-million-user]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - security
  - authentication
---

# OpenID Connect

## Định nghĩa

OpenID Connect (OIDC) là authentication layer xây trên OAuth 2.0, dùng ID token để cho client xác minh identity của user.

## Cách hiểu bằng lời của tôi

OAuth trả lời "app này được quyền truy cập gì?". OIDC thêm câu trả lời "user này là ai?". Vì vậy OIDC là mảnh làm cho OAuth flow trở thành login flow chuẩn.

## Khi làm identity layer chung

Nguồn Grab cho thấy OIDC hữu ích khi tổ chức muốn thống nhất login cho nhiều app nội bộ và third-party. Một provider trung gian như Dex có thể phát token chuẩn cho app, đồng thời kết nối tới nhiều IdP phía sau và hỗ trợ failover khi một IdP gặp sự cố.

## Liên kết

- [[OAuth 2.0]]
- [[JSON Web Token]]
- [[Authentication]]
- [[Single Sign-On]]
- [[Federated Identity Provider]]
- [[Token Exchange]]
