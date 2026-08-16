---
type: concept
status: understood
sources:
  - "[[2024-11-30_when-elasticsearch-reached-its-limits-doordash-built-their-o]]"
  - "[[2025-12-04_how-discord-indexes-trillions-of-messages-without-falling-ap]]"
source_sections:
  - "[[2024-11-30_when-elasticsearch-reached-its-limits-doordash-built-their-o]]"
  - "[[2025-12-04_how-discord-indexes-trillions-of-messages-without-falling-ap]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - search
  - system-design
---

# Search Broker

## Định nghĩa

Search Broker là service nhận query, chọn shard/stack liên quan, fan-out request, áp timeout/ranking/merge logic và trả kết quả cuối.

## Cách hiểu bằng lời của tôi

Broker là nơi query trở thành distributed operation. Nó không chỉ forward request; nó quyết định query đi đâu, kết quả nào được merge, xử lý shard chậm ra sao và rank cuối thế nào.

## Liên kết

- [[Scatter-Gather Pattern]]
- [[Search Engine Architecture]]
- [[Partial Failure]]
- [[Search Ranking]]
- [[Query Understanding]]
