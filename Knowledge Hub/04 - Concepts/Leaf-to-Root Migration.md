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
  - migration
---

# Leaf-to-Root Migration

## Định nghĩa

[[Leaf-to-Root Migration]] là cách migrate dependency graph từ các module ít phụ thuộc nhất lên các workflow/module orchestration phụ thuộc vào chúng.

## Cách hiểu bằng lời của tôi

Leaf node như constants, utilities, helpers thường dễ hiểu và dễ verify. Khi chúng ổn định, mid-level business logic và root workflow có nền để gọi, giảm guesswork về signature và behavior.

## Liên kết

- [[Dependency-Driven Migration]]
- [[Dependency Graph]]
- [[Behavioral Compatibility]]
- [[Service Layer Refactoring]]
