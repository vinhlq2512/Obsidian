---
type: concept
status: developing
sources:
  - "[[2024-11-27_understanding-retry-storms-what-they-are-and-how-to-deal-wit]]"
  - "[[2025-12-18_a-guide-to-retry-pattern-in-distributed-systems]]"
  - "[[2026-05-28_must-know-failure-modes-in-distributed-systems]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - reliability
  - distributed-systems
---

# Retry Storm

## Định nghĩa

Retry storm là failure mode trong đó nhiều client/service retry cùng lúc, làm tải tăng mạnh và khiến downstream đang lỗi càng khó hồi phục.

## Cách hiểu bằng lời của tôi

Retry là thuốc, nhưng quá liều thành độc. Nếu mọi tầng service đều retry một lỗi tạm thời theo cùng nhịp, traffic không giảm mà nhân lên thành sóng đánh vào service yếu nhất.

## Nguyên nhân

- Fixed interval retry tạo synchronized waves.
- Unlimited retries làm tải tăng không giới hạn.
- Không có exponential backoff hoặc jitter.
- Nested service dependencies khiến retry nhân theo chiều sâu call graph.
- Thiếu backpressure/circuit breaker từ downstream.

## Cách phòng

- Exponential backoff với jitter.
- Retry budget và max attempts.
- [[Circuit Breaker]] để ngừng retry khi downstream unhealthy.
- [[Rate Limiting]] hoặc token bucket cho retry traffic.
- [[Observability]] đo retry rate, amplification factor, queue depth và downstream health.

## Liên kết

- [[Retry Pattern]]
- [[Backpressure]]
- [[Circuit Breaker]]
- [[Metastable Failure]]
- [[Timeout]]
- [[Rate Limiting]]
- [[Alerting]]
