---
type: concept
status: seed
sources:
  - "[[2025-02-11_how-netflix-built-a-distributed-counter-for-billions-of-user]]"
  - "[[2026-01-21_how-netflix-built-a-real-time-distributed-graph-for-internet]]"
  - "[[2025-05-08_messaging-patterns-explained-pub-sub-queues-and-event-stream]]"
source_sections:
  - "[[2025-02-11_how-netflix-built-a-distributed-counter-for-billions-of-user]]"
  - "[[2026-01-21_how-netflix-built-a-real-time-distributed-graph-for-internet]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - system-design
  - data
---

# Event Log

## Định nghĩa

[[Event Log]] là chuỗi event durable, có thể replay, ghi lại thay đổi hoặc hành vi theo thời gian để downstream system xử lý, aggregate hoặc dựng lại state.

## Cách hiểu bằng lời của tôi

Thay vì chỉ lưu trạng thái cuối cùng, event log lưu từng sự kiện đã xảy ra. Điều này hữu ích khi cần idempotency, audit, replay, backfill hoặc nhiều consumer cùng tạo các read model khác nhau.

## Khi hữu ích

- Counter cần tránh double-count và có thể tính lại count.
- Graph realtime cần nhận stream interaction rồi biến thành node/edge.
- Pipeline analytics cần backfill khi logic xử lý thay đổi.
- Hệ thống cần fan-out event tới nhiều consumer độc lập.

## Trade-off

- Read trực tiếp từ event log thường chậm; cần [[Rollup Pipeline]] hoặc [[Materialized View]].
- Retention phải được thiết kế, vì giữ raw event mãi có thể quá đắt.
- Ordering thường chỉ chắc trong một partition/key.
- Consumer phải idempotent vì replay và duplicate là chuyện bình thường.

## Liên kết

- [[Message Broker]]
- [[Event Stream]]
- [[Idempotency Key]]
- [[Rollup Pipeline]]
- [[Materialized View]]
- [[Change Data Capture]]
