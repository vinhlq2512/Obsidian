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
  - indexing
---

# Index Segment

## Định nghĩa

Index Segment là phần immutable nhỏ của search index, thường được thêm mới hoặc replicate thay vì ghi đè toàn bộ index.

## Cách hiểu bằng lời của tôi

Segment giúp search index xử lý update hiệu quả hơn: thay vì rebuild mọi thứ, indexer tạo segment mới. DoorDash tận dụng segment-based replication để giảm chi phí và tránh query workload bị indexing workload kéo chậm.

## Liên kết

- [[Search Indexer]]
- [[Inverted Index]]
- [[Data Replication]]
- [[Object Storage]]
