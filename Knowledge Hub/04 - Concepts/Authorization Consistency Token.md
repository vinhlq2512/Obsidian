---
type: concept
status: seed
sources:
  - "[[2026-01-27_how-google-manages-trillions-of-authorizations-with-zanzibar]]"
source_sections:
  - "[[2026-01-27_how-google-manages-trillions-of-authorizations-with-zanzibar]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - security
  - distributed-systems
---

# Authorization Consistency Token

## Định nghĩa

[[Authorization Consistency Token]] là token freshness được application truyền vào authorization check để yêu cầu hệ thống kiểm quyền trên dữ liệu ít nhất mới bằng một mốc thời gian đã biết.

## Cách hiểu bằng lời của tôi

Trong Zanzibar, token này được gọi là zookie. Nó giải quyết vấn đề revoke quyền rồi sửa nội dung: nếu app dùng permission cache quá cũ, người vừa bị thu hồi quyền vẫn có thể đọc nội dung mới. Token freshness buộc authorization check nhìn thấy các thay đổi quyền trước mốc đã lưu.

## Cơ chế rút gọn

```text
permission/content change
-> auth service trả freshness token
-> application lưu token cùng content/version
-> lần đọc sau gửi token vào permission check
-> auth service không được trả lời bằng snapshot cũ hơn token
```

## Trade-off

- Freshness cao hơn làm tăng latency vì cần dữ liệu mới hơn/coordination nhiều hơn.
- Stale read có thể nhanh và cache tốt nếu workload chấp nhận.
- Token giúp app chọn correctness boundary thay vì luôn ép global fresh read.

## Liên kết

- [[Google Zanzibar]]
- [[Relationship-Based Access Control]]
- [[Read-Your-Writes Consistency]]
- [[Strict Serializability]]
- [[Caching Strategy]]
