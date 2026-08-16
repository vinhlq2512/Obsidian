---
type: concept
status: understood
sources:
  - "[[2025-12-04_how-discord-indexes-trillions-of-messages-without-falling-ap]]"
source_sections:
  - "[[2025-12-04_how-discord-indexes-trillions-of-messages-without-falling-ap]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - reliability
  - indexing
---

# Destination-Aware Batching

## Định nghĩa

Destination-Aware Batching là kỹ thuật gom message/update theo đích đến trước khi batch, để một lỗi ở một destination không làm hỏng batch của nhiều destination khác.

## Cách hiểu bằng lời của tôi

Batch lớn không tự động tốt. Nếu một batch chứa message rải qua nhiều node, một node lỗi có thể làm retry cả batch và khuếch đại failure. Gom theo cluster/index/shard trước giúp lỗi bị localize.

## Liên kết

- [[Search Indexer]]
- [[Bulkhead Pattern]]
- [[Backpressure]]
- [[Message Queue]]
- [[Partial Failure]]
