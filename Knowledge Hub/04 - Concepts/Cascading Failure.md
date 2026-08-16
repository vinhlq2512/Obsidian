---
type: concept
status: developing
sources:
  - "[[2026-05-28_must-know-failure-modes-in-distributed-systems]]"
  - "[[2025-08-07_top-strategies-to-improve-reliability-in-distributed-systems-part-1]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - reliability
  - distributed-systems
---

# Cascading Failure

## Định nghĩa

Cascading failure là failure mode trong đó lỗi ban đầu ở một component lan sang các component khác và biến thành outage lớn hơn.

## Cách hiểu bằng lời của tôi

Vấn đề không chỉ là một node chết. Vấn đề là phần traffic/work của node đó bị đẩy sang node khác, node khác quá tải, latency tăng, timeout xuất hiện, retry/failover tiếp tục đẩy tải đi nơi khác. Hệ thống tự khuếch đại lỗi ban đầu.

## Cách cắt lan truyền

- [[Circuit Breaker]] để fail fast thay vì tiếp tục gọi dependency đang yếu.
- [[Backpressure]] để upstream giảm tốc.
- [[Load Shedding]] để bỏ một phần request và giữ phần còn lại sống.
- [[Bulkhead Pattern]] để cô lập resource theo tenant, region hoặc workload.

## Liên kết

- [[Retry Storm]]
- [[Metastable Failure]]
- [[High Availability]]
- [[Observability]]
