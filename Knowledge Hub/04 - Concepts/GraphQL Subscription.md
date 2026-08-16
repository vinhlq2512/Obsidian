---
type: concept
status: seed
sources:
  - "[[2026-05-21_a-guide-to-async-patterns-in-api-design]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - graphql
  - api
---

# GraphQL Subscription

## Định nghĩa

GraphQL subscription là GraphQL operation giữ một stream update liên tục cho dữ liệu mà client đăng ký theo schema.

## Cách hiểu bằng lời của tôi

Subscription không phải transport riêng. Nó là contract layer đặt trên WebSocket hoặc SSE: client dùng syntax GraphQL để nói muốn nghe thay đổi nào, server đẩy event phù hợp theo thời gian.

## Khi dùng

- Hệ đã dùng GraphQL cho query/mutation.
- Muốn semantics thống nhất cho live data.
- Không nên adoption GraphQL chỉ vì cần realtime nếu SSE/WebSocket thuần đã đủ.

## Liên kết

- [[GraphQL]]
- [[Async API Pattern]]
- [[WebSocket]]
- [[Server-Sent Events]]
