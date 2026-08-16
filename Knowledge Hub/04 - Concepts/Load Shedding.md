---
type: concept
status: seed
sources:
  - "[[2026-05-28_must-know-failure-modes-in-distributed-systems]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - reliability
  - overload-control
---

# Load Shedding

## Định nghĩa

Load shedding là pattern chủ động bỏ hoặc reject một phần request khi hệ thống quá tải để bảo vệ capacity cho phần workload quan trọng hơn.

## Cách hiểu bằng lời của tôi

Khi hệ thống không thể phục vụ tất cả, cố phục vụ tất cả thường làm sập tất cả. Load shedding chọn thất bại có kiểm soát: reject sớm, degrade nhẹ hoặc bỏ request ưu tiên thấp để giữ core path còn hoạt động.

## Khi áp dụng

- Queue depth, CPU, connection pool hoặc tail latency vượt ngưỡng.
- Traffic spike làm retry/failover có nguy cơ tạo [[Cascading Failure]].
- Có thể phân loại request theo priority, tenant, endpoint hoặc freshness.

## Liên kết

- [[Backpressure]]
- [[Rate Limiting]]
- [[Circuit Breaker]]
- [[Service Level Objective]]
- [[Graceful Degradation]]
