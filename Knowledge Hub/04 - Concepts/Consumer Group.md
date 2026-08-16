---
type: concept
status: seed
sources:
  - "[[2023-09-14_why-is-kafka-so-fast-how-does-it-work]]"
  - "[[2025-05-08_messaging-patterns-explained-pub-sub-queues-and-event-stream]]"
source_sections:
  - "[[2023-09-14_why-is-kafka-so-fast-how-does-it-work]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - kafka
  - messaging
---

# Consumer Group

## Định nghĩa

[[Consumer Group]] là nhóm consumer cùng đọc một topic/stream và chia nhau các partition để xử lý song song.

## Cách hiểu bằng lời của tôi

Một consumer group biến event stream thành worker pool: trong cùng group, mỗi event ở một partition được một consumer xử lý; giữa các group khác nhau, cùng event có thể được đọc độc lập cho mục đích khác.

## Cần nhớ

- Unit assignment là partition, không phải từng event.
- Nếu consumer nhiều hơn partition, consumer dư có thể idle.
- Nếu consumer join/leave, broker/coordinator rebalance assignment.
- Offset cho biết group đã đọc tới đâu; commit offset sai có thể mất hoặc xử lý lại event.

## Liên kết

- [[Apache Kafka]]
- [[Kafka Partition]]
- [[Delivery Semantics]]
- [[Backpressure]]
- [[Event Stream]]
