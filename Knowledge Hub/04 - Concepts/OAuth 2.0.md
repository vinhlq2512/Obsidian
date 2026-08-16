---
type: concept
status: developing
sources:
  - "[[2023-04-12_authentication-methods-passwordless-mfa-sso-oauth-part-2]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - security
  - authorization
---

# OAuth 2.0

## Định nghĩa

OAuth 2.0 là authorization framework cho phép delegated access bằng token ngắn hạn thay vì chia sẻ password cho third-party application.

## Cách hiểu bằng lời của tôi

OAuth không phải chủ yếu để "đăng nhập"; nó là cách user cho app A quyền truy cập một phần resource ở service B. Khi kết hợp với [[OpenID Connect]], nó mới trở thành flow đăng nhập kiểu "Sign in with Google".

## Vai trò chính

- Resource owner: user sở hữu dữ liệu.
- Resource server: server giữ protected resource.
- Client: app muốn truy cập resource.
- Authorization server: nơi cấp token.

## Grant cần nhớ

- Authorization code grant là mode đầy đủ và phổ biến.
- Implicit grant không còn được khuyến nghị cho frontend hiện đại.
- Client credentials grant dùng cho server-to-server.
- Authorization Code + PKCE là hướng an toàn hơn cho public clients.

## Liên kết

- [[OpenID Connect]]
- [[Authentication]]
- [[Authorization]]
- [[JSON Web Token]]
- [[Single Sign-On]]
