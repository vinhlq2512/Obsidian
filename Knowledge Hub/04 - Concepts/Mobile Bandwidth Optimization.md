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
  - mobile
  - performance
---

# Mobile Bandwidth Optimization

## Định nghĩa

[[Mobile Bandwidth Optimization]] là tập kỹ thuật giảm dữ liệu truyền giữa server và mobile client mà vẫn giữ được responsiveness và freshness cần thiết.

## Cách hiểu bằng lời của tôi

Ở mobile, bandwidth không chỉ là tiền server. Nó ảnh hưởng pin, radio wakeup, latency và cảm giác app mượt. Discord cho thấy giảm data thừa bằng delta update có thể quan trọng hơn đổi thuật toán nén.

## Liên kết

- [[Delta Update]]
- [[Streaming Compression]]
- [[Passive Session]]
- [[Latency]]
- [[Cost Optimization]]
