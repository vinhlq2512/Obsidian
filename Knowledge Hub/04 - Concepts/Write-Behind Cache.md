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

# Write-Behind Cache

## Định nghĩa

Write-Behind Cache là chiến lược ghi vào cache trước, rồi đồng bộ xuống database theo batch hoặc background process.

## Cách hiểu bằng lời của tôi

Write-behind tối ưu write latency bằng cách biến database write thành công việc nền. Nó hợp với workload write-heavy chịu được persistence delay, nhưng rủi ro mất dữ liệu tăng nếu cache lỗi trước khi flush.

## Trade-off

- Ưu: giảm số write trực tiếp tới database và cải thiện throughput.
- Nhược: có window mất dữ liệu hoặc inconsistency.
- Cần durable queue, retry và monitoring nếu dữ liệu quan trọng.

## Liên kết

- [[Caching Strategy]]
- [[Write-Through Cache]]
- [[Eventual Consistency]]
- data loss
