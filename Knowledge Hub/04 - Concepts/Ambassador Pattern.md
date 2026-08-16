---
type: concept
status: understood
sources:
  - "[[2026-05-07_container-design-patterns-for-distributed-systems]]"
source_sections:
  - "[[2026-05-07_container-design-patterns-for-distributed-systems]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - containers
  - design-pattern
---

# Ambassador Pattern

## Định nghĩa

Ambassador Pattern là pattern dùng helper container làm proxy cho main container khi giao tiếp với thế giới bên ngoài.

## Cách hiểu bằng lời của tôi

Main app nói chuyện với localhost như thể dependency rất đơn giản. Ambassador đứng cạnh đó và xử lý service discovery, routing, retry, TLS hoặc topology phức tạp. Lợi ích là app bớt biết về network; chi phí là thêm hop và thêm contract vận hành.

## Liên kết

- [[Sidecar Pattern]]
- [[Service Discovery]]
- [[Reverse Proxy]]
- [[Retry Pattern]]
