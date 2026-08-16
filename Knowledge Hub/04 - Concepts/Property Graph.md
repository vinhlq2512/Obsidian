---
type: concept
status: seed
sources:
  - "[[2026-01-21_how-netflix-built-a-real-time-distributed-graph-for-internet]]"
source_sections:
  - "[[2026-01-21_how-netflix-built-a-real-time-distributed-graph-for-internet]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - graph
  - data-modeling
---

# Property Graph

## Định nghĩa

[[Property Graph]] là graph model trong đó node và edge đều có identifier, type/label và tập property metadata.

## Cách hiểu bằng lời của tôi

Property graph không chỉ nói "A nối với B". Nó còn lưu A là loại entity gì, cạnh là quan hệ gì, và metadata của node/cạnh như timestamp, trạng thái hoặc thuộc tính nghiệp vụ. Điều này làm graph phù hợp với interaction data và domain relationship.

## Thành phần

- Node: entity như account, title, device, game.
- Edge: relationship hoặc interaction như watched, logged-in-from, plays.
- Property: metadata gắn với node/edge.
- Identifier: khóa để lookup và update chính xác.

## Liên kết

- [[Real-Time Graph Architecture]]
- [[Unified Domain Model]]
- [[Key-Value Graph Storage]]
- [[Database Schema Design]]
