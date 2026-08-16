---
type: concept
status: seed
sources:
  - "[[2026-04-25_ep212-data-warehouse-vs-data-lake-vs-data-mesh]]"
  - "[[2025-11-11_how-spotify-built-its-data-platform-to-understand-1-4-trilli]]"
source_sections:
  - "[[2026-04-25_ep212-data-warehouse-vs-data-lake-vs-data-mesh]]"
  - "[[2025-11-11_how-spotify-built-its-data-platform-to-understand-1-4-trilli]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - data-engineering
  - architecture
---

# Data Mesh

## Định nghĩa

[[Data Mesh]] phân quyền sở hữu dữ liệu về các domain/team, trong khi tổ chức vẫn giữ chuẩn chung về schema, quality, documentation, access và interoperability.

## Cách hiểu bằng lời của tôi

Data mesh là phản ứng với bottleneck của một team data trung tâm. Team tạo ra dữ liệu cũng phải coi dataset như sản phẩm: có owner, SLA/freshness, schema, access policy và tài liệu đủ để team khác dùng.

## Điều kiện để không vỡ

- Mỗi domain có người và quy trình chịu trách nhiệm data quality.
- Platform cung cấp self-service tooling thay vì bắt từng team tự dựng hạ tầng.
- Chuẩn chung giúp dữ liệu từ nhiều domain vẫn ghép được với nhau.

## Liên kết

- [[Data Platform as Code]]
- [[Data Contract]]
- [[Data Freshness]]
- [[Data Warehouse]]
- [[Data Lake]]
