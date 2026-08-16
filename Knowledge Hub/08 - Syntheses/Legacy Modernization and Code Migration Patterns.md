---
type: synthesis
status: seed
concepts:
  - "[[Legacy System Modernization]]"
  - "[[Traffic Replay]]"
  - "[[State Reconciliation Pipeline]]"
  - "[[Behavioral Compatibility]]"
  - "[[Codemod Migration]]"
  - "[[Dependency-Driven Migration]]"
  - "[[Leaf-to-Root Migration]]"
  - "[[Service Layer Refactoring]]"
  - "[[Intent-Based Test Migration]]"
  - "[[Idiomatic Rewrite]]"
  - "[[Dual-System Operation]]"
sources:
  - "[[2025-01-05_modernizing-legacy-systems-without-breaking-production]]"
  - "[[2025-05-04_pinterest-migrated-3-7m-lines-to-typescript-heres-how-they-p]]"
  - "[[2025-09-29_how-grabs-migration-from-go-to-rust-cut-costs-by-70]]"
  - "[[2025-12-18_how-salesforce-migrated-7-years-of-legacy-in-4-months-instea]]"
questions: []
created_at: 2026-08-16
updated_at: 2026-08-16
tags:
  - synthesis
  - migration
  - software-architecture
---

# Legacy Modernization and Code Migration Patterns

## Luận điểm chính

Migration an toàn không bắt đầu bằng rewrite. Nó bắt đầu bằng việc hiểu behavior hiện tại, dependency order, validation strategy và rollback/control plane. Code mới chỉ là một phần; bằng chứng rằng nó hành xử đúng mới là phần quyết định.

## Pattern chính

- [[Traffic Replay]] và [[Shadow Testing]] dùng production-like input để bắt edge case thật.
- [[State Reconciliation Pipeline]] phát hiện drift khi old/new system cùng chạy.
- [[Behavioral Compatibility]] giữ observable contract thay vì bám implementation cũ.
- [[Codemod Migration]] phù hợp khi migration có phần syntax/tooling cơ học lớn.
- [[Dependency-Driven Migration]] và [[Leaf-to-Root Migration]] giảm cascade error trong codebase nhiều phụ thuộc.
- [[Service Layer Refactoring]] xử lý static/global-state legacy khi chuyển sang kiến trúc multi-tenant.
- [[Intent-Based Test Migration]] bảo vệ mục đích business thay vì đóng băng test legacy.
- [[Idiomatic Rewrite]] hợp lý khi service đơn giản, traffic lớn và runtime mới có lợi ích efficiency rõ.
- [[Dual-System Operation]] là chi phí vận hành phải dự trù trong giai đoạn chuyển tiếp.

## Mental model

```text
capture behavior
-> map dependency graph
-> automate transformation hoặc rewrite theo contract
-> validate layer by layer
-> shadow/replay/canary
-> operate dual systems
-> cutover và cleanup debt
```

## Câu hỏi thiết kế

- Ta đang bảo vệ contract nào: API, data, log, route, UI hay business flow?
- Có dependency graph đủ tốt để chọn migration order chưa?
- Test hiện tại kiểm behavior hay chỉ kiểm implementation cũ?
- Có đường rollback và cleanup phase không?

## Liên kết

- [[Runtime Platform Migration]]
- [[Technical Debt]]
- [[Zero-Downtime Infrastructure Migration]]
- [[Deployment and CI-CD Release Strategies]]
