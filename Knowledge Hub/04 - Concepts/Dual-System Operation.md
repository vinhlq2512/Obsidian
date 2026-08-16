---
type: concept
status: seed
sources:
  - "[[2025-12-18_how-salesforce-migrated-7-years-of-legacy-in-4-months-instea]]"
  - "[[2025-01-05_modernizing-legacy-systems-without-breaking-production]]"
source_sections:
  - "[[2025-12-18_how-salesforce-migrated-7-years-of-legacy-in-4-months-instea]]"
  - "[[2025-01-05_modernizing-legacy-systems-without-breaking-production]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - migration
  - operations
---

# Dual-System Operation

## Định nghĩa

[[Dual-System Operation]] là giai đoạn vận hành song song hệ cũ và hệ mới trong migration để phục vụ validation, fallback, phased rollout hoặc compliance transition.

## Cách hiểu bằng lời của tôi

Migration hiếm khi là một cú bật công tắc. Team phải có capacity giữ hai thế giới chạy cùng lúc, so behavior/state, xử lý bug từ cả hai phía và biết rõ khi nào có thể tắt hệ cũ.

## Liên kết

- [[Shadow Testing]]
- [[State Reconciliation Pipeline]]
- [[Phased Rollout]]
- [[Rollback Strategy]]
- [[Legacy System Modernization]]
