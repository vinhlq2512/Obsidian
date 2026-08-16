---
type: concept
status: developing
sources:
  - "[[2026-05-21_a-guide-to-async-patterns-in-api-design]]"
  - "[[2025-03-13_api-protocols-101-a-guide-to-choose-the-right-one]]"
  - "[[2025-01-08_how-discord-reduced-websocket-traffic-by-40percent]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - api
  - realtime
---

# WebSocket

## Định nghĩa

WebSocket là protocol giữ một kết nối persistent full-duplex để client và server gửi message cho nhau bất cứ lúc nào.

## Cách hiểu bằng lời của tôi

WebSocket đáng dùng khi cả hai phía đều thật sự nói chuyện liên tục: multiplayer game, collaborative editor, trading interface. Nếu chỉ server đẩy update một chiều, [[Server-Sent Events]] thường đơn giản hơn.

## Trade-off

- Giảm overhead request-response lặp lại.
- Hỗ trợ realtime hai chiều.
- Tốn tài nguyên vì mỗi client giữ connection.
- Cần xử lý reconnect, heartbeat, backpressure, auth và abuse trên connection dài.
- Với payload nhỏ, thường xuyên và lặp lại, [[Streaming Compression]] và [[Delta Update]] có thể giảm bandwidth đáng kể hơn chỉ scale thêm server.

## Liên kết

- [[Async API Pattern]]
- [[Server-Sent Events]]
- [[Backpressure]]
- [[API Protocol]]
- [[Streaming Compression]]
- [[Delta Update]]
