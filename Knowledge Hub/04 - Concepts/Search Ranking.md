---
type: concept
status: understood
sources:
  - "[[2024-11-30_when-elasticsearch-reached-its-limits-doordash-built-their-o]]"
  - "[[2025-06-18_how-dropbox-optimizes-search]]"
  - "[[2023-11-30_unlock-highly-relevant-search-with-ai]]"
source_sections:
  - "[[2024-11-30_when-elasticsearch-reached-its-limits-doordash-built-their-o]]"
  - "[[2025-06-18_how-dropbox-optimizes-search]]"
  - "[[2023-11-30_unlock-highly-relevant-search-with-ai]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - search
  - ranking
---

# Search Ranking

## Định nghĩa

Search Ranking là lớp quyết định thứ tự kết quả sau khi retrieval tạo candidate set, dựa trên lexical score, ML score, context, business rule và tín hiệu thời gian thực.

## Cách hiểu bằng lời của tôi

Search tốt không chỉ tìm đúng document có chứa token. Ranking quyết định kết quả nào đáng lên trước. DoorDash kết hợp BM25, user behavior, real-time availability/demand và business boosting; Dropbox nhắc tới trade-off giữa user-visible gain và CPU cost khi thêm semantic embedding hoặc preview/OCR.

## Liên kết

- [[Ranking]]
- [[Query Understanding]]
- [[Hybrid Retrieval]]
- [[Retrieval Evaluation]]
- [[Precision-Recall Tradeoff]]
