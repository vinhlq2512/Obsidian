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
  - system-design
---

# Search Engine Architecture

## Định nghĩa

Search Engine Architecture là kiến trúc ingest, index, query, rank và serve kết quả tìm kiếm với latency thấp, freshness đủ tốt và khả năng scale theo dữ liệu lẫn traffic.

## Cách hiểu bằng lời của tôi

Search không chỉ là gọi Elasticsearch. Khi scale lớn, hệ thống phải tách rõ write path tạo index, read path xử lý query, broker fan-out/merge, ranking, tenant isolation và cơ chế reindex/upgrade an toàn.

## Thành phần thường gặp

- [[Inverted Index]] hoặc vector index để lookup nhanh.
- [[Search Indexer]] xử lý update và tạo segment/index.
- [[Search Broker]] fan-out query tới shard và merge results.
- [[Query Understanding]] chuẩn hóa query người dùng.
- [[Search Ranking]] kết hợp lexical score, business rule và ML score.
- [[Search Tenant Isolation]] giảm noisy-neighbor giữa workload.

## Liên kết

- [[AI Search]]
- [[Hybrid Retrieval]]
- [[Vector Search Infrastructure]]
- [[Scatter-Gather Pattern]]
- [[Ranking]]
