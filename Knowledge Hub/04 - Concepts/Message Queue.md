---
type: concept
status: seed
sources:
  - "[[2023-08-10_why-do-we-need-a-message-queue]]"
  - "[[2023-08-17_how-to-choose-a-message-queue]]"
  - "[[2025-01-09_understanding-message-queues]]"
  - "[[2025-05-08_messaging-patterns-explained-pub-sub-queues-and-event-stream]]"
source_sections:
  - "[[2023-08-10_why-do-we-need-a-message-queue]]"
  - "[[2025-05-08_messaging-patterns-explained-pub-sub-queues-and-event-stream]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - messaging
  - system-design
---

# Message Queue

## Định nghĩa

[[Message Queue]] là messaging pattern point-to-point: producer đưa message vào queue, một consumer/worker lấy message ra xử lý, rồi acknowledge để message được coi là hoàn tất.

## Cách hiểu bằng lời của tôi

Queue là bộ giảm chấn giữa producer nhanh và consumer chậm. Producer không cần chờ downstream xử lý ngay; consumer có thể xử lý theo tốc độ của mình. Đổi lại, hệ thống phải quan sát backlog, retry, ordering và poison message.

## Khi hữu ích

- Background jobs và worker pools.
- Tách request path khỏi xử lý chậm.
- Hấp thụ traffic spike trong flash sale hoặc batch workload.
- Bảo vệ downstream bằng buffering và rate control.

## Pitfall

- Queue depth tăng lâu là dấu hiệu consumer không theo kịp.
- Retry có thể phá FIFO ordering.
- Poison message có thể làm kẹt worker nếu không có [[Dead Letter Queue]].
- Message đã acknowledge thường không replay được nếu không có event log riêng.

## Liên kết

- [[Message Broker]]
- [[Publish-Subscribe]]
- [[Event Stream]]
- [[Delivery Semantics]]
- [[Backpressure]]
- [[Dead Letter Queue]]
