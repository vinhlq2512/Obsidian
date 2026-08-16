---
type: concept
status: seed
sources:
  - "[[2025-01-08_how-discord-reduced-websocket-traffic-by-40percent]]"
source_sections:
  - "[[2025-01-08_how-discord-reduced-websocket-traffic-by-40percent]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - realtime
  - client
---

# Passive Session

## Định nghĩa

[[Passive Session]] là trạng thái client vẫn cần được cập nhật ở mức đủ dùng nhưng user không đang chủ động xem phần dữ liệu đó.

## Cách hiểu bằng lời của tôi

Không phải mọi session realtime đều đáng nhận full fidelity. Nếu user không mở server/channel đó, hệ thống chỉ cần giữ client gần đúng để quay lại nhanh, không cần gửi mọi snapshot chi tiết. Discord giảm traffic bằng cách gửi delta cho passive sessions thay vì snapshot đầy đủ.

## Liên kết

- [[WebSocket]]
- [[Delta Update]]
- [[Client State Synchronization]]
- [[Load Shedding]]
- [[Mobile Bandwidth Optimization]]
