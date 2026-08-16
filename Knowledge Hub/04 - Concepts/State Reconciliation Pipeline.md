---
type: concept
status: seed
sources:
  - "[[2025-01-05_modernizing-legacy-systems-without-breaking-production]]"
source_sections:
  - "[[2025-01-05_modernizing-legacy-systems-without-breaking-production]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - migration
  - data-consistency
---

# State Reconciliation Pipeline

## Định nghĩa

[[State Reconciliation Pipeline]] so sánh và điều hòa state giữa hệ cũ và hệ mới trong giai đoạn migration để phát hiện drift trước khi ảnh hưởng user.

## Cách hiểu bằng lời của tôi

Khi hai hệ chạy song song, "không crash" chưa đủ. Cần biết state có đang lệch không, lệch ở field nào, lệch do timing hay bug logic, và có thể tự heal hoặc rollback không.

## Cơ chế

```text
old system state + new system state
-> real-time comparison
-> drift detection
-> conflict rule hoặc manual review
-> audit log + alert + optional healing
```

## Liên kết

- [[Eventual Consistency]]
- [[Data Pipeline Validation]]
- [[Shadow Testing]]
- [[Rollback Strategy]]
- [[Observability]]
