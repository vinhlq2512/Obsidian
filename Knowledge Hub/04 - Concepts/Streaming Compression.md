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
  - performance
---

# Streaming Compression

## Định nghĩa

[[Streaming Compression]] là cách nén chuỗi payload liên tiếp bằng cách giữ context nén qua nhiều message thay vì nén từng payload như một khối độc lập.

## Cách hiểu bằng lời của tôi

Với WebSocket, payload thường nhỏ, dày và có cấu trúc lặp lại. Nếu mỗi message nén từ đầu, algorithm không tận dụng được pattern đã thấy. Streaming compression giữ rolling context để message sau hưởng lợi từ message trước.

## Trade-off

- Tốt cho payload nhỏ, thường xuyên, có pattern lặp.
- Cần cân bằng compression ratio, CPU và memory.
- Dictionary có thể giúp payload nhỏ nhưng tạo overhead đồng bộ dictionary giữa client/server.
- Cần instrumentation để biết setting nào thật sự tốt cho workload.

## Liên kết

- [[WebSocket]]
- [[Delta Update]]
- [[Observability]]
- [[Latency]]
- [[Cost Optimization]]
