---
type: concept
status: developing
sources:
  - "[[2026-05-21_a-guide-to-async-patterns-in-api-design]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - api
  - async
---

# Async API Pattern

## Định nghĩa

Async API pattern là nhóm thiết kế API dùng khi request-response ngắn không đủ: công việc lâu, event xảy ra theo lịch server, giao tiếp liên tục, hoặc producer/consumer không online cùng lúc.

## Bốn đòn bẩy thiết kế

- Ai khởi tạo kết nối?
- Kết nối giữ mở bao lâu?
- Có broker trung gian không?
- Delivery guarantee là gì?

## Pattern map

- [[Short Polling]] cho event tần suất thấp và muốn đơn giản.
- [[Long Polling]] cho server-held request nhưng chưa dùng stream thật.
- [[Server-Sent Events]] cho server-to-client stream một chiều.
- [[WebSocket]] cho giao tiếp hai chiều liên tục.
- [[Webhook]] cho server-to-server event delivery.
- [[Message Broker]] cho producer/consumer lệch thời gian và cần durability.

## Liên kết

- [[REST API]]
- [[Timeout]]
- [[Backpressure]]
- [[Idempotency Key]]
- [[GraphQL Subscription]]
