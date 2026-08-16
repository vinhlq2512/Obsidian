---
type: concept
status: seed
sources:
  - "[[2026-01-12_processing-trillions-how-lyft-s-feature-store-grew-by-12-33]]"
  - "[[2025-11-11_how-spotify-built-its-data-platform-to-understand-1-4-trilli]]"
source_sections:
  - "[[2026-01-12_processing-trillions-how-lyft-s-feature-store-grew-by-12-33]]"
  - "[[2025-11-11_how-spotify-built-its-data-platform-to-understand-1-4-trilli]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - data-engineering
  - metadata
---

# Data Catalog

## Định nghĩa

[[Data Catalog]] là hệ thống giúp người dùng tìm dataset/feature, xem owner, schema, lineage, quality, freshness, quyền truy cập và tài liệu liên quan.

## Cách hiểu bằng lời của tôi

Catalog là discovery layer của data platform. Nếu không tìm được dữ liệu/feature đã có, team sẽ tạo bản mới, hỏi người khác trong chat, hoặc dùng sai nguồn. Catalog làm metadata thành một phần của workflow, không phải tài liệu phụ.

## Liên kết

- [[Feature Discovery]]
- [[Data Platform as Code]]
- [[Data Contract]]
- [[Data Freshness]]
- [[Data Mesh]]
