---
type: concept
status: seed
sources:
  - "[[2025-05-08_messaging-patterns-explained-pub-sub-queues-and-event-stream]]"
  - "[[2026-02-21_ep203-rabbitmq-vs-kafka-vs-pulsar]]"
source_sections:
  - "[[2025-05-08_messaging-patterns-explained-pub-sub-queues-and-event-stream]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - messaging
  - streaming
---

# Apache Pulsar

## Định nghĩa

[[Apache Pulsar]] là messaging/streaming platform hỗ trợ cả queue và event stream style, nổi bật ở tiered storage, geo-replication và multi-tenancy.

## Cách hiểu bằng lời của tôi

Pulsar nằm giữa hai thế giới: có thể phục vụ pub-sub/queue nhưng cũng giữ stream history. Điểm khác biệt thường được nhắc tới là tách serving broker khỏi storage layer, giúp lưu trữ dài hạn và multi-tenant cloud-native linh hoạt hơn.

## Khi đáng cân nhắc

- Cần replay và retention dài nhưng cũng muốn queue semantics.
- Nhiều tenant/team dùng chung platform.
- Cần geo-replication built-in.
- Muốn tiered storage để giảm chi phí giữ lịch sử dài.

## Liên kết

- [[Event Stream]]
- [[Message Queue]]
- [[Publish-Subscribe]]
- [[Apache Kafka]]
- [[Data Replication]]
