---
type: concept
status: seed
sources:
  - "[[2025-05-08_messaging-patterns-explained-pub-sub-queues-and-event-stream]]"
  - "[[2023-08-17_how-to-choose-a-message-queue]]"
source_sections:
  - "[[2025-05-08_messaging-patterns-explained-pub-sub-queues-and-event-stream]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - messaging
  - system-design
---

# Publish-Subscribe

## Định nghĩa

[[Publish-Subscribe]] là messaging pattern one-to-many: producer publish event vào topic/channel, nhiều subscriber độc lập nhận bản sao và xử lý theo nhu cầu riêng.

## Cách hiểu bằng lời của tôi

Queue giao một việc cho một worker. Pub-sub phát một sự kiện cho nhiều hệ cùng quan tâm. Producer không cần biết có bao nhiêu subscriber; subscriber mới có thể xuất hiện mà không sửa producer.

## Khi hữu ích

- Event broadcasting: user upload ảnh, nhiều hệ thống cùng cập nhật.
- Notification: email, push, in-app notification là các subscriber riêng.
- Realtime updates: ticker, collaboration, sports score.
- Distributed state change: cache invalidation, search indexing, analytics.

## Trade-off

- Slow subscriber có thể tạo backlog/backpressure tùy broker.
- Không phải pub-sub nào cũng replay được; Redis Pub/Sub mất message nếu subscriber offline.
- Delivery guarantee phụ thuộc broker và config.
- Ordering thường chỉ có trong một key/subscription/partition, không phải toàn cục.

## Liên kết

- [[Message Broker]]
- [[Message Queue]]
- [[Event Stream]]
- [[Fan-Out on Write]]
- [[Backpressure]]
