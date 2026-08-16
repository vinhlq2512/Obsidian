---
type: concept
status: understood
sources:
  - "[[2024-11-30_when-elasticsearch-reached-its-limits-doordash-built-their-o]]"
  - "[[2025-12-04_how-discord-indexes-trillions-of-messages-without-falling-ap]]"
  - "[[2023-04-03_twitter-made-searching-scalable-before-elon-musk]]"
source_sections:
  - "[[2024-11-30_when-elasticsearch-reached-its-limits-doordash-built-their-o]]"
  - "[[2025-12-04_how-discord-indexes-trillions-of-messages-without-falling-ap]]"
  - "[[2023-04-03_twitter-made-searching-scalable-before-elon-musk]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - search
  - indexing
---

# Search Indexer

## Định nghĩa

Search Indexer là service xử lý document/message update, tokenize/transform dữ liệu và ghi vào search index hoặc index segment.

## Cách hiểu bằng lời của tôi

Indexer là write path của search. Nếu indexer dùng chung tài nguyên với query serving, bulk update hoặc backfill có thể làm query latency tăng. Vì vậy các hệ lớn thường tách indexing khỏi querying và dùng queue để absorb spike.

## Pattern từ source

- DoorDash tách high-priority update khỏi bulk update theo batch.
- Twitter tách backfill service và ingestion service khỏi Elasticsearch để giảm tải trực tiếp.
- Discord group message theo destination trước khi bulk index để một node lỗi không làm hỏng cả batch.

## Liên kết

- [[Index Segment]]
- [[Destination-Aware Batching]]
- [[Search Broker]]
- [[Message Queue]]
- [[Backpressure]]
