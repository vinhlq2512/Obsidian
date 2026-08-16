---
type: synthesis
status: seed
concepts:
  - "[[Multi-Tenancy]]"
  - "[[Tenancy Isolation Spectrum]]"
  - "[[Tenant Storage Model]]"
  - "[[Tenant Context]]"
  - "[[Noisy Neighbor Problem]]"
  - "[[Cross-Tenant Data Leak]]"
  - "[[Resource Quota]]"
sources:
  - "[[2026-07-16_a-guide-to-multi-tenancy-benefits-and-challenges]]"
  - "[[2026-05-26_how-vercel-cut-build-wait-times-from-90-seconds-to-5]]"
questions: []
created_at: 2026-08-16
updated_at: 2026-08-16
tags:
  - synthesis
  - tenancy
  - system-design
---

# Multi-Tenant Architecture Patterns

## Luận điểm chính

Multi-tenancy là bài toán chia sẻ có kiểm soát. Mỗi layer phải trả lời riêng: tenant nào đang dùng chung storage, compute, cache, queue, search, identity và network; failure ở layer đó có thể lan tới ai; tenant context có được giữ đủ xa không.

## Pattern chính

- [[Tenancy Isolation Spectrum]] giúp nhìn pool, silo và bridge như một dải trade-off giữa cost và containment.
- [[Tenant Storage Model]] là quyết định data-layer: shared table, schema per tenant hoặc database per tenant.
- [[Tenant Context]] là invariant xuyên suốt request/job/message để tránh [[Cross-Tenant Data Leak]].
- [[Noisy Neighbor Problem]] là chi phí vận hành của pooling; [[Resource Quota]], rate limit và bulkhead giúp khôi phục fairness.
- [[Hostile Multi-Tenancy]] là biến thể khó hơn khi tenant code/input phải được xem là độc hại, như build platform chạy code khách hàng.

## Mental model

```text
tenant request
-> auth và tenant context
-> compute pool hoặc silo
-> cache/search/queue/database scoped theo tenant
-> quota và isolation giới hạn noisy neighbor
-> blast radius được đo theo từng shared resource
```

## Liên kết

- [[Blast Radius]]
- [[Fine-Grained Authorization]]
- [[Search Tenant Isolation]]
- [[Rate Limiting]]
- [[Sandboxed Build Execution]]
