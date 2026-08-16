---
type: concept
status: seed
sources:
  - "[[2025-11-12_how-tinder-decomposed-its-ios-monolith-app-handling-70m-user]]"
source_sections:
  - "[[2025-11-12_how-tinder-decomposed-its-ios-monolith-app-handling-70m-user]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - build-system
  - migration
---

# Compiler-Driven Modularization

## Định nghĩa

[[Compiler-Driven Modularization]] dùng thông tin declaration/reference từ compiler để dựng dependency graph và lập kế hoạch tách module.

## Cách hiểu bằng lời của tôi

Compiler đã biết file nào định nghĩa symbol nào và file nào dùng symbol đó. Thay vì đoán bằng grep thủ công, dùng dữ liệu compiler làm bản đồ dependency đáng tin hơn cho migration/modularization.

## Liên kết

- [[Mobile App Modularization]]
- [[Critical Path Build Graph]]
- [[Dependency Graph]]
- [[Leaf-to-Root Migration]]
- [[Codemod Migration]]
