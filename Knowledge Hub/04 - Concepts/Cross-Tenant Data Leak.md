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

# Cross-Tenant Data Leak

## Định nghĩa

[[Cross-Tenant Data Leak]] là sự cố một tenant nhìn thấy, truy vấn được hoặc nhận được dữ liệu thuộc tenant khác.

## Cách hiểu bằng lời của tôi

Đây là failure nghiêm trọng nhất của multi-tenancy. Nó không chỉ xảy ra ở database query thiếu `tenant_id`; nó có thể xảy ra ở cache key thiếu tenant, search index không scope tenant, background job xử lý nhầm tập dữ liệu hoặc queue/log trộn tenant.

## Cách giảm rủi ro

- Tenant context phải đi cùng request/job/message.
- Cache key và index query phải include tenant boundary.
- Test có case cross-tenant negative.
- Audit log đủ để truy vết tenant nào thấy dữ liệu nào.

## Liên kết

- [[Tenant Context]]
- [[Tenant Storage Model]]
- [[Search Tenant Isolation]]
- [[API Security]]
- [[Least Privilege]]
