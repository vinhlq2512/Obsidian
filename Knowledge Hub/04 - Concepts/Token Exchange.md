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

# Token Exchange

## Định nghĩa

[[Token Exchange]] là cơ chế đổi hoặc mint token mới với audience/scope phù hợp khi một service cần gọi service khác thay mặt user hoặc workload.

## Cách hiểu bằng lời của tôi

Service account rộng quyền rất nguy hiểm: lộ một credential là mở quá nhiều cửa. Token exchange tạo token hẹp hơn cho đúng service đích và đúng caller context. Service B có thể biết request đến từ Service A nhưng vẫn giữ dấu vết identity của user ban đầu.

## Pattern từ Grab Dex

- User đăng nhập và nhận token cho Service A.
- Service A là trusted peer, được mint token có audience gồm Service A và Service B.
- Service B trust issuer và kiểm audience/scope trước khi xử lý.
- Audit log ghi service nào mint token nào.

## Liên kết

- [[OpenID Connect]]
- [[OAuth 2.0]]
- [[JSON Web Token]]
- [[Authentication]]
- [[Authorization]]
- [[Least Privilege]]
