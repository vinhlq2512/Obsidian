---
type: concept
status: understood
sources:
  - "[[2025-12-04_how-discord-indexes-trillions-of-messages-without-falling-ap]]"
  - "[[2024-11-30_when-elasticsearch-reached-its-limits-doordash-built-their-o]]"
source_sections:
  - "[[2025-12-04_how-discord-indexes-trillions-of-messages-without-falling-ap]]"
  - "[[2024-11-30_when-elasticsearch-reached-its-limits-doordash-built-their-o]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - search
  - migration
---

# Zero-Downtime Reindexing

## Định nghĩa

Zero-Downtime Reindexing là migration flow xây index mới, dual-write hoặc backfill dữ liệu, rồi chuyển query traffic sang index mới mà không dừng search.

## Cách hiểu bằng lời của tôi

Search index có thể chạm hard limit hoặc cần schema mới. Nếu chỉ rebuild trực tiếp, search phải dừng hoặc mất dữ liệu mới. Reindex an toàn cần index mới chạy song song, ingest mới được ghi vào cả hai bên, dữ liệu cũ được backfill, sau đó query switch khi đủ parity.

## Flow từ Discord

```text
create new index
-> dual-index new messages
-> historical reindex/backfill
-> serve query from old index while backfill runs
-> switch query traffic to new index
-> stop indexing old index
```

## Liên kết

- [[Expand-Contract Migration]]
- [[Search Indexer]]
- [[Shadow Traffic]]
- [[Rollback Strategy]]
- [[Index Segment]]
