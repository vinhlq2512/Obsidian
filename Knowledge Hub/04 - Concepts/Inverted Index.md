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

# Inverted Index

## Định nghĩa

Inverted Index là cấu trúc dữ liệu ánh xạ token sang danh sách document chứa token đó, giúp text search lookup nhanh theo từ khóa.

## Cách hiểu bằng lời của tôi

Thay vì duyệt từng document để xem có chứa từ khóa hay không, inverted index bắt đầu từ token và nhảy thẳng tới các document candidate. Đây là lõi của Lucene/Elasticsearch cho search dạng lexical.

## Cơ chế

- Text được tokenize và normalize.
- Mỗi token trỏ tới posting list của document id.
- Query nhiều token sẽ kết hợp posting list bằng AND/OR/filter.
- Ranking như BM25 hoặc ML ranking quyết định thứ tự cuối.

## Liên kết

- [[Search Engine Architecture]]
- [[Database Indexing]]
- [[Search Ranking]]
- [[Query Understanding]]
