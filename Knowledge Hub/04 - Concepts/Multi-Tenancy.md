---
type: concept
status: seed
sources:
  - "[[2026-07-16_a-guide-to-multi-tenancy-benefits-and-challenges]]"
  - "[[2026-05-26_how-vercel-cut-build-wait-times-from-90-seconds-to-5]]"
source_sections:
  - "[[2026-07-16_a-guide-to-multi-tenancy-benefits-and-challenges]]"
  - "[[2026-05-26_how-vercel-cut-build-wait-times-from-90-seconds-to-5]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - system-design
  - tenancy
---

# Multi-Tenancy

## Định nghĩa

[[Multi-Tenancy]] là kiến trúc trong đó nhiều customer/organization cùng dùng chung một hệ thống, trong khi dữ liệu, request, quyền và tài nguyên của từng tenant vẫn phải được tách logic.

## Cách hiểu bằng lời của tôi

Multi-tenancy là bài toán chọn mức chia sẻ. Chia sẻ nhiều giúp giảm chi phí vận hành, nhưng tăng rủi ro noisy neighbor, blast radius và cross-tenant leak. Vì vậy tenancy không chỉ là database schema; nó phải đi qua compute, cache, queue, search index, identity, network và background jobs.

## Spectrum

- [[Tenancy Isolation Spectrum]]: pool, silo và bridge là các điểm trên cùng một dải chia sẻ/cách ly.
- [[Tenant Storage Model]] quyết định dữ liệu tenant nằm chung bảng, chung database khác schema, hay database riêng.
- Compute, identity, network, cache, queue và search cũng phải có quyết định tenancy riêng.

## Câu hỏi thiết kế

- Tenant context có đi xuyên suốt request path không?
- Resource nào đang pooled và resource nào đang siloed?
- Một tenant noisy có thể ảnh hưởng bao nhiêu tenant khác?
- Compliance hoặc enterprise tier có yêu cầu dedicated storage/compute không?

## Liên kết

- [[Hostile Multi-Tenancy]]
- [[Tenancy Isolation Spectrum]]
- [[Tenant Storage Model]]
- [[Tenant Context]]
- [[Noisy Neighbor Problem]]
- [[Cross-Tenant Data Leak]]
- [[Resource Quota]]
- [[Blast Radius]]
- [[Search Tenant Isolation]]
- [[Fine-Grained Authorization]]
- [[Rate Limiting]]
- [[Least Privilege]]
