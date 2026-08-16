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
  - testing
  - migration
---

# Intent-Based Test Migration

## Định nghĩa

[[Intent-Based Test Migration]] là cách rewrite test theo mục đích hành vi cần bảo vệ thay vì dịch nguyên xi assertion gắn với implementation cũ.

## Cách hiểu bằng lời của tôi

Nếu test cũ kiểm tra static method hoặc class boundary đã bị loại bỏ, migrate test 1:1 sẽ giữ lại giả định legacy. Test mới nên hỏi: user/business flow nào phải vẫn đúng, contract nào phải không đổi, và side effect nào phải giữ nguyên.

## Liên kết

- [[Behavioral Compatibility]]
- [[Service Layer Refactoring]]
- [[API Contract]]
- [[Data Pipeline Validation]]
- [[Shadow Testing]]
