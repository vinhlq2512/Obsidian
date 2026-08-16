---
type: concept
status: seed
sources:
  - "[[2023-11-07_shipping-to-production]]"
  - "[[2024-12-23_the-chatgpt-outage-what-openais-post-mortem-revealed]]"
source_sections:
  - "[[2023-11-07_shipping-to-production]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - deployment
  - reliability
---

# Rollback Strategy

## Định nghĩa

[[Rollback Strategy]] là kế hoạch đưa hệ thống về trạng thái an toàn khi một deployment, config change, data migration hoặc experiment gây regression.

## Cách hiểu bằng lời của tôi

Rollback không nên được nghĩ tới sau khi incident xảy ra. Một change rủi ro phải có cách quay lui rõ: lệnh nào chạy, dữ liệu có tương thích ngược không, ai có quyền quyết định, metric nào tự động rollback, và rollback có gây mất dữ liệu hay không.

## Cần có

- Trigger rollback dựa trên health/business metrics.
- Cách revert code/config/schema/data rõ ràng.
- Owner và quyền thao tác khi incident đang diễn ra.
- Kiểm tra rollback trong staging hoặc production-like flow.
- Với data change, cần kế hoạch forward-fix nếu không thể rollback sạch.

## Liên kết

- [[Phased Rollout]]
- [[Incident Response]]
- [[Postmortem]]
- [[Backward Compatibility]]
- [[Disaster Recovery]]
