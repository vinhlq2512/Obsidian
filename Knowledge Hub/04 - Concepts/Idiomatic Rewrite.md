---
type: concept
status: seed
sources:
  - "[[2025-09-29_how-grabs-migration-from-go-to-rust-cut-costs-by-70]]"
source_sections:
  - "[[2025-09-29_how-grabs-migration-from-go-to-rust-cut-costs-by-70]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - migration
  - software-architecture
---

# Idiomatic Rewrite

## Định nghĩa

[[Idiomatic Rewrite]] là rewrite hệ thống sang ngôn ngữ/runtime mới dựa trên contract input-output và idiom của nền tảng đích, thay vì dịch từng dòng từ implementation cũ.

## Cách hiểu bằng lời của tôi

Grab không cố viết Go bằng Rust. Họ coi service cũ như black box qua gRPC contract, rồi chọn thư viện và concurrency model phù hợp Rust. Cách này giảm baggage của code cũ nhưng đòi hỏi validation mạnh để không mất edge case.

## Điều kiện nên cân nhắc

- Service đủ đơn giản về chức năng để rewrite không nổ scope.
- Traffic đủ lớn để efficiency gain đáng tiền.
- Team có khả năng duy trì ngôn ngữ/runtime mới lâu dài.
- Dependency ecosystem của runtime mới đủ trưởng thành.

## Liên kết

- [[Runtime Platform Migration]]
- [[Behavioral Compatibility]]
- [[API Contract]]
- [[Cost Optimization]]
- [[Technical Debt]]
