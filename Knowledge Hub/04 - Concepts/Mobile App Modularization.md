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
  - mobile
  - software-architecture
---

# Mobile App Modularization

## Định nghĩa

[[Mobile App Modularization]] là việc tách codebase mobile monolith thành nhiều module/target có ownership và dependency rõ để giảm build time, tăng parallelism và giảm blast radius thay đổi.

## Cách hiểu bằng lời của tôi

Mobile app cuối cùng vẫn build thành một binary, nhưng codebase không nhất thiết phải là một khối phụ thuộc chằng chịt. Modularization tạo ranh giới để team phát triển nhanh hơn, test hẹp hơn và build graph ngắn hơn.

## Việc phải làm khi tách file/module

- Cập nhật dependency giữa target.
- Sửa import path.
- Điều chỉnh access control.
- Thay shortcut/singleton bằng dependency injection.
- Chặn file mới quay lại monolith cũ.

## Liên kết

- [[Critical Path Build Graph]]
- [[Compiler-Driven Modularization]]
- [[Dependency-Driven Migration]]
- [[Service Layer Refactoring]]
- [[Developer Velocity]]
