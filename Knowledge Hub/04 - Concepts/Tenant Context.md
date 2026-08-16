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
  - security
---

# Tenant Context

## Định nghĩa

[[Tenant Context]] là thông tin xác định request, dữ liệu, job hoặc operation đang thuộc tenant nào và phải được truyền/enforce xuyên suốt hệ thống.

## Cách hiểu bằng lời của tôi

Tenant context là "nhãn an toàn" của multi-tenant system. Nếu nhãn này rơi mất ở cache key, search query, background job hoặc queue consumer, hệ thống có thể trả dữ liệu tenant khác dù database layer có vẻ đã tách đúng.

## Điểm cần enforce

- API request và auth/session.
- Database query và row filter.
- Cache key.
- Search index query.
- Queue message, background job và log.

## Liên kết

- [[Multi-Tenancy]]
- [[Cross-Tenant Data Leak]]
- [[Fine-Grained Authorization]]
- [[Search Tenant Isolation]]
- [[Least Privilege]]
