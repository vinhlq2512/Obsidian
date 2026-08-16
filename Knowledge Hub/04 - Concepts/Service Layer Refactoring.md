---
type: concept
status: seed
sources:
  - "[[2025-12-18_how-salesforce-migrated-7-years-of-legacy-in-4-months-instea]]"
source_sections:
  - "[[2025-12-18_how-salesforce-migrated-7-years-of-legacy-in-4-months-instea]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - software-architecture
  - migration
---

# Service Layer Refactoring

## Định nghĩa

[[Service Layer Refactoring]] là refactor đưa logic từ static/global/tightly-coupled code sang service boundary có dependency injection, lifecycle và ownership rõ hơn.

## Cách hiểu bằng lời của tôi

Khi hệ cũ được viết cho single-tenant package, static method và global state có thể tiện. Nhưng trong shared multi-tenant core, cùng pattern đó dễ gây leak state, khó test và khó scale. Service layer tạo ranh giới để inject dependency, kiểm soát state và validate behavior theo business capability.

## Liên kết

- [[Microservices Architecture]]
- [[Dependency-Driven Migration]]
- [[Technical Debt]]
- [[Behavioral Compatibility]]
- [[Fine-Grained Authorization]]
