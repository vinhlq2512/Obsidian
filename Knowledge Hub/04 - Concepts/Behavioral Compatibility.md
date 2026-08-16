---
type: concept
status: seed
sources:
  - "[[2025-05-04_pinterest-migrated-3-7m-lines-to-typescript-heres-how-they-p]]"
  - "[[2025-09-29_how-grabs-migration-from-go-to-rust-cut-costs-by-70]]"
  - "[[2025-12-18_how-salesforce-migrated-7-years-of-legacy-in-4-months-instea]]"
source_sections:
  - "[[2025-05-04_pinterest-migrated-3-7m-lines-to-typescript-heres-how-they-p]]"
  - "[[2025-09-29_how-grabs-migration-from-go-to-rust-cut-costs-by-70]]"
  - "[[2025-12-18_how-salesforce-migrated-7-years-of-legacy-in-4-months-instea]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - migration
  - testing
---

# Behavioral Compatibility

## Định nghĩa

[[Behavioral Compatibility]] là mức độ hệ mới giữ cùng observable behavior, contract và output quan trọng như hệ cũ dù implementation bên trong thay đổi.

## Cách hiểu bằng lời của tôi

Migration thành công không phải vì code mới giống code cũ từng dòng. Nó thành công khi caller, dashboard, route, log, test, API và business flow vẫn nhìn thấy hành vi đúng. Vì vậy cần so behavior, không chỉ so syntax.

## Cách kiểm tra

- Byte-for-byte diff cho transpilation/output artifact khi phù hợp.
- Contract test trên API/gRPC/schema.
- Shadow traffic và response comparison.
- Test intent thay vì test implementation detail.

## Liên kết

- [[API Contract]]
- [[Shadow Testing]]
- [[Traffic Replay]]
- [[Data Contract]]
- [[Backward Compatibility]]
