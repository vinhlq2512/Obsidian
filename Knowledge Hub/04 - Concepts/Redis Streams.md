---
type: concept
status: understood
sources:
  - "[[2023-10-12_the-6-most-impactful-ways-redis-is-used-in-production-system]]"
  - "[[2023-09-21_a-crash-course-in-redis]]"
source_sections:
  - "[[2023-10-12_the-6-most-impactful-ways-redis-is-used-in-production-system]]"
  - "[[2023-09-21_a-crash-course-in-redis]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - messaging
  - redis
---

# Redis Streams

## Định nghĩa

Redis Streams là append-only log trong Redis dùng cho event stream hoặc message queue có ID, ordering và consumer group.

## Cách hiểu bằng lời của tôi

Redis List phù hợp queue đơn giản; Pub/Sub phù hợp fire-and-forget; Redis Streams nằm giữa: vẫn nhẹ hơn Kafka nhưng có persistence, acknowledgement và consumer group tốt hơn cho queue cần xử lý song song.

## Cơ chế

- Producer dùng `XADD` để append message vào stream.
- Consumer group chia tải qua nhiều consumer bằng `XREADGROUP`.
- Message đã đọc nằm trong pending entries list cho tới khi consumer `XACK`.

## Giới hạn

- Không thay thế hoàn toàn Kafka/Pulsar cho event streaming quy mô lớn, retention dài hoặc ecosystem stream processing sâu.
- Vẫn bị ràng buộc bởi memory, replication và vận hành Redis.

## Liên kết

- [[Redis]]
- [[Event Stream]]
- [[Message Queue]]
- [[Consumer Group]]
- [[Delivery Semantics]]
