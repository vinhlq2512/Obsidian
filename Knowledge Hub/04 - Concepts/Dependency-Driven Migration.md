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
  - software-architecture
---

# Dependency-Driven Migration

## Định nghĩa

[[Dependency-Driven Migration]] dùng dependency graph để quyết định thứ tự migration, thường chuyển từ leaf node lên root node để giảm cascading error.

## Cách hiểu bằng lời của tôi

Với codebase nhiều năm, migrate file ngẫu nhiên là tự tạo lỗi compile và lỗi hành vi. Dependency graph cho biết module nào có thể trở thành nền tảng verified trước, rồi các layer phía trên dựa vào nó.

## Cơ chế

```text
scan dependency graph
-> phân lớp leaf, mid-level, root workflow
-> migrate leaf trước
-> validate từng layer
-> dùng layer đã verified làm reference cho layer tiếp theo
```

## Liên kết

- [[Dependency Graph]]
- [[Leaf-to-Root Migration]]
- [[Service Layer Refactoring]]
- [[Behavioral Compatibility]]
- [[Technical Debt]]
