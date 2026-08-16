---
type: concept
status: understood
sources:
  - "[[2026-05-07_container-design-patterns-for-distributed-systems]]"
source_sections:
  - "[[2026-05-07_container-design-patterns-for-distributed-systems]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - containers
  - design-pattern
---

# Container Adapter Pattern

## Định nghĩa

Container Adapter Pattern là pattern dùng helper container để chuyển output/interface của app thành format chuẩn mà hệ thống bên ngoài kỳ vọng.

## Cách hiểu bằng lời của tôi

Nếu mỗi app export metric/log khác nhau, monitoring platform sẽ rối. Adapter đứng cạnh app, đọc format riêng và biến nó thành format chung, đặc biệt hữu ích với legacy hoặc third-party app không sửa được.

## Liên kết

- [[Adapter]]
- [[Sidecar Pattern]]
- [[Observability]]
- [[Metrics]]
