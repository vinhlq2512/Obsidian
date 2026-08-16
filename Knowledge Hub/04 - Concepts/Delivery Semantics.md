---
type: concept
status: seed
sources:
  - "[[2026-07-30_a-detailed-guide-to-idempotency-delivery-semantics-and-dedup]]"
  - "[[2025-05-08_messaging-patterns-explained-pub-sub-queues-and-event-stream]]"
  - "[[2023-09-14_why-is-kafka-so-fast-how-does-it-work]]"
source_sections:
  - "[[2026-07-30_a-detailed-guide-to-idempotency-delivery-semantics-and-dedup]]"
  - "[[2025-05-08_messaging-patterns-explained-pub-sub-queues-and-event-stream]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - messaging
  - distributed-systems
---

# Delivery Semantics

## Định nghĩa

[[Delivery Semantics]] là cam kết của messaging system về việc message/event có thể được giao bao nhiêu lần và trong điều kiện lỗi sẽ xử lý ra sao.

## Ba mức thường gặp

- At-most-once: message được giao tối đa một lần; có thể mất nhưng không lặp.
- At-least-once: message không mất nếu hệ hoạt động đúng, nhưng có thể bị giao lặp.
- Exactly-once/effectively-once: side effect cuối cùng giống như xử lý đúng một lần, thường cần transaction, idempotency hoặc dedup.

## Cách hiểu bằng lời của tôi

Delivery semantics không chỉ là tính năng broker. Nó là hợp đồng giữa producer, broker, consumer, offset/ack, datastore và side effect. Nếu consumer gửi email rồi crash trước khi commit offset, retry có thể gửi email lần nữa dù broker không "sai".

## Thiết kế an toàn

- Dùng [[Idempotency Key]] hoặc dedup table cho side effect.
- Commit offset sau khi side effect đã bền vững.
- Có [[Dead Letter Queue]] cho message lỗi lặp lại.
- Ghi rõ operation nào chịu được duplicate, operation nào cần transaction.

## Liên kết

- [[Message Queue]]
- [[Apache Kafka]]
- [[Consumer Group]]
- [[Transactional Outbox]]
- [[Retry Pattern]]
