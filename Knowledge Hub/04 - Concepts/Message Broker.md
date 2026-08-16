---
type: concept
status: understood
sources:
  - "[[2026-01-08_must-know-message-broker-patterns]]"
  - "[[2023-08-10_why-do-we-need-a-message-queue-newsletter]]"
  - "[[2026-07-30_a-detailed-guide-to-idempotency-delivery-semantics-and-dedup]]"
  - "[[2026-01-21_how-netflix-built-a-real-time-distributed-graph-for-internet]]"
  - "[[2025-02-11_how-netflix-built-a-distributed-counter-for-billions-of-user]]"
  - "[[2023-08-10_why-do-we-need-a-message-queue]]"
  - "[[2023-08-17_how-to-choose-a-message-queue]]"
  - "[[2025-05-08_messaging-patterns-explained-pub-sub-queues-and-event-stream]]"
source_sections:
  - "[[2026-01-08_must-know-message-broker-patterns]]"
  - "[[2023-08-10_why-do-we-need-a-message-queue-newsletter]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - distributed-systems
  - system-design
---

# Message Broker

## Cách hiểu bằng lời của tôi

[[Message Broker]] là lớp trung gian nhận message từ producer, lưu/định tuyến message, rồi giao cho consumer. Nó giúp tách producer và consumer theo thời gian, tốc độ và lỗi: producer không cần biết consumer đang rảnh hay đang down, miễn broker còn nhận được message.

## Vì sao cần

- Decoupling: service gửi và service xử lý không cần gọi nhau trực tiếp.
- Buffering: hấp thụ spike bằng queue thay vì ép downstream xử lý ngay.
- Retry: cho phép xử lý lại khi consumer lỗi.
- Fan-out/pub-sub: một event có thể được nhiều consumer dùng cho mục đích khác nhau.

## Ba pattern cần phân biệt

- [[Message Queue]]: point-to-point, một message cho một worker xử lý.
- [[Publish-Subscribe]]: one-to-many, nhiều subscriber nhận cùng event.
- [[Event Stream]]: append-only log có retention, consumer đọc/replay bằng offset.

## Điều phải thiết kế cẩn thận

- Delivery semantics: at-most-once, at-least-once, effectively-once.
- Ordering: thứ tự thường chỉ được giữ trong một partition/key cụ thể.
- Backpressure: queue depth tăng là tín hiệu downstream không theo kịp.
- Idempotent consumer: retry và duplicate là chuyện bình thường trong hệ phân tán.

## Trade-off cần nhớ

Message broker làm hệ thống bền hơn trước spike và lỗi tạm thời, nhưng thêm độ trễ, operational surface, và debugging khó hơn. Khi side effect quan trọng, consumer phải kết hợp broker với [[Idempotency Key]] hoặc deduplication record.

## Khi làm event backbone

Trong các nguồn Netflix, Kafka xuất hiện như event backbone cho counter/graph: event được partition theo key, consumer xử lý batch hoặc stream, và dữ liệu có thể replay/backfill. Điểm quan trọng là broker không tự tạo read model nhanh; downstream vẫn cần [[Rollup Pipeline]], [[Materialized View]] hoặc graph storage tối ưu cho query.

## Liên kết

- [[Idempotency Key]]
- [[Eventual Consistency]]
- [[Observability]]
- [[Scalable Distributed Systems Patterns]]
- [[Event Log]]
- [[Rollup Pipeline]]
- [[Apache Kafka]]
- [[RabbitMQ]]
- [[Apache Pulsar]]
- [[Delivery Semantics]]
