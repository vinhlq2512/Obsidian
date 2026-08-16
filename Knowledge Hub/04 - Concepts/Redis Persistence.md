---
type: concept
status: understood
sources:
  - "[[2023-09-21_a-crash-course-in-redis]]"
  - "[[2024-11-21_distributed-caching-the-secret-to-high-performance-applicati]]"
source_sections:
  - "[[2023-09-21_a-crash-course-in-redis]]"
  - "[[2024-11-21_distributed-caching-the-secret-to-high-performance-applicati]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - caching
  - storage
---

# Redis Persistence

## Định nghĩa

Redis Persistence là cơ chế ghi dữ liệu Redis xuống disk để phục hồi sau restart hoặc failure, thường qua AOF, RDB hoặc kết hợp cả hai.

## Cách hiểu bằng lời của tôi

Redis tối ưu latency bằng cách giữ dữ liệu trong memory, nhưng vẫn cần persistence khi dữ liệu cache có chi phí rebuild cao hoặc Redis được dùng gần như database. Điểm tinh tế là persistence không nên nằm trên critical path đọc/ghi chính.

## Cơ chế

- AOF ghi lại command sau khi command đã chạy trong memory, giống command log để replay khi recover.
- RDB ghi snapshot point-in-time và có thể recover nhanh hơn khi AOF quá dài.
- Background persistence giúp giảm I/O pressure lên main execution path.

## Trade-off

- AOF chi tiết hơn nhưng recovery có thể chậm nếu log lớn.
- RDB recover nhanh hơn nhưng có thể mất update sau snapshot gần nhất.
- Tắt persistence đơn giản hơn khi Redis chỉ là cache có thể rebuild.

## Liên kết

- [[Redis]]
- [[Write-Ahead Log]]
- [[Backup and Restore]]
- recovery point objective
