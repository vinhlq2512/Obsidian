---
type: concept
status: understood
sources:
  - "[[2025-05-30_from-flat-to-flexible-rewriting-github-issue-search-with-nes]]"
source_sections:
  - "[[2025-05-30_from-flat-to-flexible-rewriting-github-issue-search-with-nes]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - search
  - parsing
---

# Search Query AST

## Định nghĩa

Search Query AST là cây cú pháp trừu tượng biểu diễn query người dùng nhập, đặc biệt khi query có AND/OR, grouping, precedence và nested filters.

## Cách hiểu bằng lời của tôi

Flat parser đủ cho query kiểu danh sách filter, nhưng không đủ cho nested search. Khi search language có ngoặc và toán tử logic, query phải được parse thành tree để backend hiểu cấu trúc và generate query chính xác.

## Cơ chế từ GitHub

- Query string được parse bằng grammar thành AST.
- AST node như AND/OR được traverse đệ quy.
- Elasticsearch bool query được sinh từ tree: AND thành `must`, OR thành `should`.
- Rollout phải backward-compatible với query cũ.

## Liên kết

- [[Query Understanding]]
- [[Backward Compatibility]]
- [[Shadow Testing]]
- [[Search Engine Architecture]]
