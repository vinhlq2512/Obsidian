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
  - system-design
---

# Tenancy Isolation Spectrum

## Định nghĩa

[[Tenancy Isolation Spectrum]] là dải lựa chọn giữa pooling nhiều tenant trên tài nguyên chung và siloing tenant vào tài nguyên riêng.

## Cách hiểu bằng lời của tôi

Không có một kiểu multi-tenancy duy nhất. Pool rẻ và dễ vận hành tập trung nhưng blast radius rộng hơn. Silo cách ly tốt nhưng chi phí và số lượng thứ phải vận hành tăng theo tenant. Bridge là kiểu thực tế nhất: phần lớn tenant pooled, tenant lớn hoặc regulated có lớp dedicated.

## Liên kết

- [[Multi-Tenancy]]
- [[Tenant Storage Model]]
- [[Blast Radius]]
- [[Resource Quota]]
- [[Hostile Multi-Tenancy]]
