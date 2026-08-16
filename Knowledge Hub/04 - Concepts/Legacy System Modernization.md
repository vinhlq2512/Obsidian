---
type: concept
status: seed
sources:
  - "[[2025-01-05_modernizing-legacy-systems-without-breaking-production]]"
  - "[[2025-12-18_how-salesforce-migrated-7-years-of-legacy-in-4-months-instea]]"
source_sections:
  - "[[2025-01-05_modernizing-legacy-systems-without-breaking-production]]"
  - "[[2025-12-18_how-salesforce-migrated-7-years-of-legacy-in-4-months-instea]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - migration
  - software-architecture
---

# Legacy System Modernization

## Định nghĩa

[[Legacy System Modernization]] là quá trình thay đổi kiến trúc, runtime, ngôn ngữ, dữ liệu hoặc deployment model của hệ thống cũ mà vẫn giữ production ổn định.

## Cách hiểu bằng lời của tôi

Modernization không phải "viết lại cho sạch". Nó là lấy giá trị nghiệp vụ đã chứng minh của hệ cũ và đưa nó vào ràng buộc mới: scale, compliance, multi-tenancy, cost, developer velocity hoặc platform chuẩn.

## Nguyên tắc

- Đo behavior hiện tại trước khi thay đổi.
- Dùng [[Dependency-Driven Migration]] để biết thứ tự an toàn.
- Kiểm tra [[Behavioral Compatibility]] thay vì chỉ kiểm tra compile.
- Dùng [[Shadow Testing]], [[Traffic Replay]] và [[State Reconciliation Pipeline]] để bắt drift trước user.
- Có control plane bằng [[Feature Flag]] hoặc kill switch.

## Liên kết

- [[Technical Debt]]
- [[Runtime Platform Migration]]
- [[Zero-Downtime Infrastructure Migration]]
- [[Rollback Strategy]]
- [[Data Pipeline Validation]]
