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
  - client
  - realtime
---

# Client State Synchronization

## Định nghĩa

[[Client State Synchronization]] là cơ chế giữ state trên client đủ nhất quán với server qua snapshot, delta, event stream, polling hoặc realtime connection.

## Cách hiểu bằng lời của tôi

Client sync là trade-off giữa freshness, bandwidth, CPU, battery và UX. Active view có thể cần update ngay; passive view có thể nhận delta ít hơn; offline hoặc background state có thể chấp nhận lag.

## Pattern

- Full snapshot: đơn giản nhưng tốn bandwidth.
- [[Delta Update]]: ít dữ liệu hơn nhưng cần state versioning và merge logic.
- Event stream: linh hoạt nhưng phải xử lý reorder, retry và dedup.
- Passive mode: giảm fidelity khi user không actively viewing.

## Liên kết

- [[WebSocket]]
- [[Event Stream]]
- [[Data Freshness]]
- [[Passive Session]]
- [[Mobile Bandwidth Optimization]]
