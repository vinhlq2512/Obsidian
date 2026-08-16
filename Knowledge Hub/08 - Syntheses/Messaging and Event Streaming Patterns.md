---
type: synthesis
status: seed
concepts:
  - "[[Message Broker]]"
  - "[[Message Queue]]"
  - "[[Publish-Subscribe]]"
  - "[[Event Stream]]"
  - "[[Apache Kafka]]"
  - "[[Kafka Partition]]"
  - "[[Consumer Group]]"
  - "[[Delivery Semantics]]"
  - "[[Dead Letter Queue]]"
  - "[[RabbitMQ]]"
  - "[[Apache Pulsar]]"
sources:
  - "[[2023-08-10_why-do-we-need-a-message-queue]]"
  - "[[2023-08-17_how-to-choose-a-message-queue]]"
  - "[[2025-01-09_understanding-message-queues]]"
  - "[[2025-05-08_messaging-patterns-explained-pub-sub-queues-and-event-stream]]"
  - "[[2023-09-14_why-is-kafka-so-fast-how-does-it-work]]"
  - "[[2026-02-21_ep203-rabbitmq-vs-kafka-vs-pulsar]]"
questions: []
created_at: 2026-08-16
updated_at: 2026-08-16
tags:
  - synthesis
  - messaging
  - system-design
  - bytebytego
---

# Messaging and Event Streaming Patterns

## Ý chính

Messaging không phải một pattern duy nhất. Queue, pub-sub và event stream có mô hình delivery, replay, ordering và scaling khác nhau. Chọn sai pattern dễ dẫn tới backlog, mất message, duplicate side effect hoặc không thể rebuild state.

## So sánh nhanh

| Pattern | Mental model | Điểm mạnh | Cẩn thận |
|---|---|---|---|
| [[Message Queue]] | Một việc cho một worker | Background job, smoothing spike | Poison message, retry, queue depth |
| [[Publish-Subscribe]] | Một event cho nhiều subscriber | Fan-out, notification, realtime update | Subscriber lag, delivery guarantee |
| [[Event Stream]] | Lịch sử event append-only | Replay, CDC, analytics, read model | Partitioning, retention, consumer lag |

## Tool map

- [[RabbitMQ]]: queue-first, routing/ack/delay mạnh, hợp worker queue và transactional tasks.
- [[Apache Kafka]]: log-first, partitioned event stream, hợp high-throughput analytics, telemetry, CDC và replay-heavy systems.
- [[Apache Pulsar]]: hybrid queue/stream, tiered storage, geo-replication, multi-tenancy.

## Câu hỏi chọn hệ

- Message có cần replay/backfill không?
- Ordering cần theo key, theo queue hay toàn cục?
- Consumer lag thì muốn buffer, drop hay backpressure?
- Side effect có idempotent không?
- Retention dài hay chỉ cần deliver xong là xóa?
- Workload là task queue, pub-sub notification hay event-streaming backbone?

## Liên kết

- [[Message Broker]]
- [[Delivery Semantics]]
- [[Backpressure]]
- [[Transactional Outbox]]
- [[Change Data Capture]]
- [[Zero-Downtime Infrastructure Migration]]
