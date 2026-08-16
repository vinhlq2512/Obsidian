---
type: concept
status: seed
sources:
  - "[[2026-05-21_a-guide-to-async-patterns-in-api-design]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - api
  - async
---

# Long Polling

## Định nghĩa

Long polling là pattern client gửi request và server giữ request mở cho đến khi có event hoặc timeout.

## Cách hiểu bằng lời của tôi

Long polling giảm độ trễ so với hỏi theo lịch cố định, nhưng server phải quản lý nhiều connection đang treo. Khi response trả về, client thường gửi request tiếp theo ngay để tiếp tục chờ event.

## Trade-off

- Hữu ích khi WebSocket/SSE khó dùng trong môi trường mạng cụ thể.
- Tốn resource server vì giữ nhiều request mở.
- Timeout trống vẫn tạo overhead.

## Liên kết

- [[Async API Pattern]]
- [[Short Polling]]
- [[Server-Sent Events]]
- [[Timeout]]
