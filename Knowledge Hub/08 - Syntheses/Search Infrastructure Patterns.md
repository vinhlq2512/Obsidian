---
type: synthesis
status: seed
concepts:
  - "[[Search Engine Architecture]]"
  - "[[Inverted Index]]"
  - "[[Index Segment]]"
  - "[[Search Indexer]]"
  - "[[Search Broker]]"
  - "[[Search Tenant Isolation]]"
  - "[[Cell-Based Architecture]]"
  - "[[Destination-Aware Batching]]"
  - "[[Search Query AST]]"
  - "[[Search Ranking]]"
  - "[[Zero-Downtime Reindexing]]"
sources:
  - "[[2024-11-30_when-elasticsearch-reached-its-limits-doordash-built-their-o]]"
  - "[[2025-05-30_from-flat-to-flexible-rewriting-github-issue-search-with-nes]]"
  - "[[2025-12-04_how-discord-indexes-trillions-of-messages-without-falling-ap]]"
  - "[[2023-04-03_twitter-made-searching-scalable-before-elon-musk]]"
  - "[[2025-06-18_how-dropbox-optimizes-search]]"
questions: []
created_at: 2026-08-16
updated_at: 2026-08-16
tags:
  - synthesis
  - search
  - system-design
---

# Search Infrastructure Patterns

## Mental model

Search infrastructure có hai vòng lặp chính: ingest/indexing để dữ liệu trở thành searchable, và query/ranking để user nhận kết quả đúng trong latency thấp. Khi scale lớn, bottleneck thường không nằm ở thuật toán search đơn lẻ, mà ở isolation, batching, shard fan-out, migration, backfill và cách đo relevance.

## Các lớp thiết kế

| Lớp | Concept | Câu hỏi cần trả lời |
| --- | --- | --- |
| Index core | [[Inverted Index]], [[Index Segment]] | Dữ liệu được token hóa, segment hóa và replicate thế nào? |
| Write path | [[Search Indexer]], [[Destination-Aware Batching]] | Update/backfill có làm query latency xấu đi không? Batch có localize failure không? |
| Read path | [[Search Broker]], [[Scatter-Gather Pattern]] | Query fan-out tới shard nào, timeout ra sao, merge kết quả thế nào? |
| Multi-tenancy | [[Search Tenant Isolation]], [[Cell-Based Architecture]] | Một tenant hoặc guild cực lớn có làm ảnh hưởng phần còn lại không? |
| Query language | [[Search Query AST]], [[Query Understanding]] | User query có được parse thành cấu trúc backend hiểu được không? |
| Relevance | [[Search Ranking]], [[Hybrid Retrieval]] | Kết quả được rank bằng lexical, semantic, ML và business signal thế nào? |
| Migration | [[Zero-Downtime Reindexing]] | Schema/index mới được rollout mà không dừng search bằng cách nào? |

## Bài học

- Tách indexing khỏi querying để bulk update không phá query latency.
- Batch theo destination tốt hơn batch ngẫu nhiên khi downstream có nhiều shard/node.
- Search cluster khổng lồ có coordination tax; nhiều cell nhỏ có thể giảm blast radius.
- Query language càng mạnh càng cần parser/AST và rollout backward-compatible.
- Ranking là một lớp riêng, không nên bị trộn lẫn hoàn toàn với retrieval.
- Hard limit của engine như Lucene MAX_DOC cần escape hatch trước khi chạm trần.

## Liên kết

- [[AI Search and Recommendation Systems]]
- [[Vector Search Infrastructure]]
- [[Database Performance Tradeoffs]]
- [[Reliability Operations Loop]]
