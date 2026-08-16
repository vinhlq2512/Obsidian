---
type: concept
status: seed
sources:
  - "[[2025-05-04_pinterest-migrated-3-7m-lines-to-typescript-heres-how-they-p]]"
  - "[[2025-12-18_how-salesforce-migrated-7-years-of-legacy-in-4-months-instea]]"
source_sections:
  - "[[2025-05-04_pinterest-migrated-3-7m-lines-to-typescript-heres-how-they-p]]"
  - "[[2025-12-18_how-salesforce-migrated-7-years-of-legacy-in-4-months-instea]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - migration
  - tooling
---

# Codemod Migration

## Định nghĩa

[[Codemod Migration]] dùng chương trình chuyển đổi mã nguồn để tự động thay đổi syntax, API usage, file extension hoặc architectural pattern trên quy mô lớn.

## Cách hiểu bằng lời của tôi

Codemod chỉ mạnh khi nó là pipeline lặp lại được. Mỗi edge case bị miss phải được ghi lại, sửa rule, chạy lại và commit như một patch reproducible. Nếu phải sửa tay rải rác, migration sẽ mất kiểm soát.

## Pattern từ Pinterest

- Chuẩn bị compiler/linter/build tooling trước.
- Dùng codemod cho phần syntax cơ học.
- Thêm lint/autofix rule cho type yếu hoặc import thừa.
- Chạy daily rebase/dry-run để bắt drift từ main.
- Validate build/test/transpilation trước cutover.

## Liên kết

- [[Runtime Platform Migration]]
- [[Behavioral Compatibility]]
- [[Deployment Pipeline]]
- [[Technical Debt]]
