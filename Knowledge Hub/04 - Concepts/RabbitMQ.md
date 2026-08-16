---
type: concept
status: seed
sources:
  - "[[2023-08-17_how-to-choose-a-message-queue]]"
  - "[[2025-05-08_messaging-patterns-explained-pub-sub-queues-and-event-stream]]"
  - "[[2026-02-21_ep203-rabbitmq-vs-kafka-vs-pulsar]]"
source_sections:
  - "[[2025-05-08_messaging-patterns-explained-pub-sub-queues-and-event-stream]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - messaging
  - queue
---

# RabbitMQ

## Định nghĩa

[[RabbitMQ]] là general-purpose message broker theo queue-first semantics, mạnh ở routing, acknowledgement, task queues và delayed/durable delivery.

## Cách hiểu bằng lời của tôi

RabbitMQ hợp khi bài toán là giao việc cho worker và cần routing linh hoạt hơn là giữ event history dài. Broker đẩy message tới consumer, message thường được xóa sau khi acknowledge.

## Khi phù hợp

- Worker queue/task orchestration.
- Transactional systems cần routing rõ.
- Delayed messages hoặc retry scheduling.
- Hệ cần AMQP/routing exchange như direct, fanout, topic, headers.

## Khác Kafka

- RabbitMQ queue-first, message consumed xong thường biến mất.
- Kafka log-first, event được giữ theo retention và consumer tự quản lý offset.
- RabbitMQ thường đơn giản hơn cho job queue; Kafka tốt hơn cho event streaming, replay và throughput rất cao.

## Liên kết

- [[Message Queue]]
- [[Publish-Subscribe]]
- [[Delivery Semantics]]
- [[Apache Kafka]]
