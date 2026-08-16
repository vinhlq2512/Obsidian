---
type: concept
status: seed
sources:
  - "[[2025-11-11_how-spotify-built-its-data-platform-to-understand-1-4-trilli]]"
source_sections:
  - "[[2025-11-11_how-spotify-built-its-data-platform-to-understand-1-4-trilli]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - data-engineering
  - platform
---

# Data Platform as Code

## Định nghĩa

[[Data Platform as Code]] là pattern để team định nghĩa schema, pipeline, endpoint, retention, access control và deployment của tài nguyên dữ liệu bằng code/config có version.

## Cách hiểu bằng lời của tôi

Khi số pipeline tăng lên hàng chục nghìn, thao tác thủ công không scale. Platform cần biến dữ liệu thành "sản phẩm có owner": có schema, lineage, health, policy và deploy tự động khi repo thay đổi.

## Thành phần

- Schema và event definition do team sở hữu.
- Operator/controller tự deploy infrastructure từ định nghĩa.
- Endpoint có partitioning, retention, ACL, lineage và quality check.
- Portal/observability cho freshness, cost, failure và documentation.

## Liên kết

- [[Data Contract]]
- [[Workflow Orchestration]]
- [[Kubernetes Operator Pattern]]
- [[Observability]]
- [[Data Freshness]]
- [[Least Privilege]]
