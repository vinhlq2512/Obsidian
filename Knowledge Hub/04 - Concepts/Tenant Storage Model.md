---
type: concept
status: seed
sources:
  - "[[2026-07-16_a-guide-to-multi-tenancy-benefits-and-challenges]]"
source_sections:
  - "[[2026-07-16_a-guide-to-multi-tenancy-benefits-and-challenges]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - tenancy
  - database
---

# Tenant Storage Model

## Định nghĩa

[[Tenant Storage Model]] là cách đặt dữ liệu của từng tenant trong data layer: shared table, schema per tenant hoặc database per tenant.

## Cách hiểu bằng lời của tôi

Storage model là nơi tenancy hay được nhìn thấy nhất, nhưng nó không giải quyết toàn bộ bài toán. Shared table rẻ nhưng phụ thuộc vào `tenant_id` trong mọi query. Database per tenant cách ly mạnh hơn nhưng làm schema migration, connection management và operations nặng lên.

## Ba mô hình

- Shared table: mọi tenant chung bảng, mỗi row có tenant id.
- Schema per tenant: chung database, mỗi tenant có namespace riêng.
- Database per tenant: mỗi tenant có database riêng.

## Liên kết

- [[Multi-Tenancy]]
- [[Tenant Context]]
- [[Cross-Tenant Data Leak]]
- [[Database Schema Design]]
- [[Data Lifecycle Management]]
