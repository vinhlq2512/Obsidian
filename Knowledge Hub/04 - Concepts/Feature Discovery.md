---
type: concept
status: seed
sources:
  - "[[2026-01-12_processing-trillions-how-lyft-s-feature-store-grew-by-12-33]]"
source_sections:
  - "[[2026-01-12_processing-trillions-how-lyft-s-feature-store-grew-by-12-33]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - mlops
  - metadata
---

# Feature Discovery

## Định nghĩa

[[Feature Discovery]] là khả năng tìm, hiểu owner, metadata, freshness và cách dùng của feature đã tồn tại trước khi tạo feature mới.

## Cách hiểu bằng lời của tôi

Feature trùng là technical debt âm thầm: hai team tính gần cùng một feature bằng tên khác nhau, tốn compute và tạo kết quả lệch. Lyft nối generated DAG metadata vào Amundsen để engineer search feature trước khi viết mới.

## Liên kết

- [[Feature Store]]
- [[Data Catalog]]
- [[Data Contract]]
- [[Technical Debt]]
- [[Internal Platform as Product]]
