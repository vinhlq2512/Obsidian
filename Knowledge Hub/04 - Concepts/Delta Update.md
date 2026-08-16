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
  - data-sync
---

# Delta Update

## Định nghĩa

[[Delta Update]] là pattern chỉ gửi phần dữ liệu thay đổi thay vì gửi lại toàn bộ snapshot cho client hoặc downstream system.

## Cách hiểu bằng lời của tôi

Trước khi nén mạnh hơn, nên hỏi có đang gửi quá nhiều dữ liệu không. Nếu một server chỉ đổi một phần nhỏ, full snapshot làm tốn bandwidth, CPU encode/decode và pin mobile battery. Delta update tối ưu ngay ở thiết kế dữ liệu.

## Khi hữu ích

- Long-lived connection như [[WebSocket]].
- Client cần giữ state gần đồng bộ nhưng không active toàn thời gian.
- Dataset có thay đổi nhỏ so với snapshot tổng.

## Liên kết

- [[Client State Synchronization]]
- [[Streaming Compression]]
- [[Event Stream]]
- [[Data Freshness]]
- [[Cost Optimization]]
