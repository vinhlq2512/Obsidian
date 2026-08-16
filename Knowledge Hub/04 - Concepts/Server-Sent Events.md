---
type: concept
status: developing
sources:
  - "[[2026-05-21_a-guide-to-async-patterns-in-api-design]]"
  - "[[2025-03-13_api-protocols-101-a-guide-to-choose-the-right-one]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - api
  - streaming
---

# Server-Sent Events

## Định nghĩa

Server-Sent Events (SSE) là cơ chế server đẩy stream event một chiều tới client qua một HTTP connection dài.

## Cách hiểu bằng lời của tôi

SSE hợp khi server liên tục có update, còn client chủ yếu chỉ lắng nghe. Token streaming trong LLM UI là ví dụ rất hợp: server gửi token dần về browser, client không cần gửi message ngược trong cùng stream.

## Trade-off

- Dễ debug vì format text và dùng HTTP.
- Browser EventSource tự reconnect khi connection rớt.
- Chỉ một chiều server-to-client, không phù hợp nếu hai bên đều gửi event thường xuyên.
- Mỗi connection vẫn giữ tài nguyên server.

## Liên kết

- [[Async API Pattern]]
- [[WebSocket]]
- [[Long Polling]]
- [[LLM Inference Engineering]]
- [[API Protocol]]
