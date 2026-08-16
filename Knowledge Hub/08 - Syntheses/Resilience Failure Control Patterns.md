---
type: synthesis
status: developing
concepts:
  - "[[Retry Pattern]]"
  - "[[Retry Storm]]"
  - "[[Circuit Breaker]]"
  - "[[Backpressure]]"
  - "[[Timeout]]"
  - "[[Partial Failure]]"
  - "[[Gray Failure]]"
  - "[[Cascading Failure]]"
  - "[[Load Shedding]]"
  - "[[Bulkhead Pattern]]"
  - "[[Metastable Failure]]"
  - "[[Correlated Failure]]"
  - "[[Failover]]"
  - "[[Rate Limiting]]"
  - "[[Chaos Engineering]]"
  - "[[Observability]]"
sources:
  - "[[2024-11-27_understanding-retry-storms-what-they-are-and-how-to-deal-wit]]"
  - "[[2024-04-11_embracing-chaos-to-improve-system-resilience-chaos-engineeri]]"
  - "[[2025-08-07_top-strategies-to-improve-reliability-in-distributed-systems-part-1]]"
  - "[[2026-05-28_must-know-failure-modes-in-distributed-systems]]"
  - "[[2025-01-23_top-strategies-to-reduce-latency]]"
created_at: 2026-08-16
updated_at: 2026-08-16
tags:
  - synthesis
  - reliability
  - system-design
---

# Resilience Failure Control Patterns

## Mental model

Resilience không phải là luôn thử lại. Resilience là kiểm soát feedback loop khi hệ thống bắt đầu yếu đi: giảm tải, ngăn retry nhân lên, phát hiện sớm, và thử nghiệm có kiểm soát để biết failure path có thật sự hoạt động.

## Pattern map

| Failure pressure | Pattern | Mục tiêu |
|---|---|---|
| Transient error | [[Retry Pattern]] | Tăng khả năng hồi phục |
| Retry nhân tải | [[Retry Storm]] prevention | Tránh biến lỗi nhỏ thành outage |
| Downstream unhealthy | [[Circuit Breaker]] | Cho dependency thời gian hồi phục |
| Producer nhanh hơn consumer | [[Backpressure]] | Làm chậm upstream thay vì queue nổ |
| Traffic vượt ngưỡng | [[Rate Limiting]] | Giữ fairness và bảo vệ capacity |
| Traffic vượt capacity | [[Load Shedding]] | Bỏ bớt request để giữ phần lõi còn sống |
| Resource chung bị flood | [[Bulkhead Pattern]] | Cô lập blast radius |
| Health check xanh nhưng user path lỗi | [[Gray Failure]] | Đo workload thật bằng [[Synthetic Monitoring]] |
| Timeout/retry tự duy trì | [[Metastable Failure]] | Phá feedback loop thay vì chỉ tìm trigger gốc |
| Redundancy không độc lập | [[Correlated Failure]] | Kiểm tra failure domain và dependency chung |
| Unknown weak point | [[Chaos Engineering]] | Tìm điểm yếu trước incident thật |

## Ghi nhớ

Mỗi pattern có mặt trái. Retry làm tăng load, circuit breaker có thể reject request hợp lệ, rate limiting có thể chặn user thật, chaos experiment có thể gây sự cố nếu blast radius quá rộng. Vì vậy resilience pattern phải đi cùng [[Observability]], SLO và post-mortem.

Một điểm mới từ ByteByteGo là nhiều distributed failure không đến từ trigger ban đầu, mà đến từ phản ứng tự động của hệ thống: [[Timeout]] kích hoạt retry, retry tạo [[Retry Storm]], failover dồn tải sang node còn lại, autoscaling hoặc reconnect làm traffic đồng bộ. Vì vậy resilience cần thiết kế feedback loop, không chỉ thêm redundancy.

## Liên kết

- [[Scalable Distributed Systems Patterns]]
- [[High Availability]]
- [[Observability for Distributed Systems]]
- [[Distributed Systems]]
