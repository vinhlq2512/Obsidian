---
type: concept
status: understood
sources:
  - "[[2024-11-21_distributed-caching-the-secret-to-high-performance-applicati]]"
source_sections:
  - "[[2024-11-21_distributed-caching-the-secret-to-high-performance-applicati]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - caching
  - system-design
---

# Write-Through Cache

## Định nghĩa

Write-Through Cache là chiến lược ghi đồng thời vào cache và database để cached value luôn phản ánh update mới nhất.

## Cách hiểu bằng lời của tôi

Write-through đổi latency write lấy consistency đọc sau ghi. Nó hợp khi hệ thống thường đọc ngay sau write và không muốn cache stale, nhưng write path sẽ nặng hơn vì phải cập nhật hai nơi.

## Trade-off

- Ưu: cache và database ít lệch nhau.
- Nhược: write chậm hơn và phức tạp hơn khi volume write lớn.
- Cần xử lý lỗi khi một bên ghi thành công còn bên kia thất bại.

## Liên kết

- [[Caching Strategy]]
- [[Write-Behind Cache]]
- [[Cache Invalidation]]
- [[Read-Your-Writes Consistency]]
