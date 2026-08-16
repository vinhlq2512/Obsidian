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
  - build-system
---

# Critical Path Build Graph

## Định nghĩa

[[Critical Path Build Graph]] là dependency chain dài nhất trong build graph, quyết định thời gian build tối thiểu vì các bước trên chuỗi đó không thể chạy song song.

## Cách hiểu bằng lời của tôi

Muốn build nhanh hơn không chỉ là mua máy nhiều core. Nếu module phụ thuộc sâu thành một dây dài, build system vẫn phải chờ từng mắt xích. Tinder giảm build time bằng cách flatten build graph để nhiều target compile độc lập hơn.

## Liên kết

- [[Dependency Graph]]
- [[Mobile App Modularization]]
- [[Leaf-to-Root Migration]]
- [[Technical Debt]]
- [[Developer Velocity]]
