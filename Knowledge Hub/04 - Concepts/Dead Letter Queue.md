---
type: concept
status: seed
sources:
  - "[[2025-01-09_understanding-message-queues]]"
  - "[[2025-05-08_messaging-patterns-explained-pub-sub-queues-and-event-stream]]"
source_sections:
  - "[[2025-01-09_understanding-message-queues]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - messaging
  - reliability
---

# Dead Letter Queue

## Định nghĩa

[[Dead Letter Queue]] là queue riêng chứa message không xử lý thành công sau một số lần retry hoặc sau khi bị xác định là không thể xử lý trong luồng chính.

## Cách hiểu bằng lời của tôi

DLQ là van an toàn cho poison message. Thay vì để một message hỏng kẹt mãi ở đầu queue hoặc bị retry vô hạn, hệ thống đưa nó sang nơi khác để điều tra, sửa dữ liệu, replay hoặc bỏ qua có kiểm soát.

## Khi cần

- Message schema không hợp lệ.
- Dependency luôn reject một payload cụ thể.
- Consumer bug gây lỗi lặp lại trên cùng message.
- Dữ liệu thiếu field hoặc vi phạm business invariant.

## Cần vận hành

- Alert khi DLQ tăng.
- Lưu lý do lỗi và metadata để debug.
- Có quy trình replay sau khi fix.
- Không dùng DLQ như thùng rác im lặng; nếu không quan sát, nó chỉ che outage.

## Liên kết

- [[Message Queue]]
- [[Delivery Semantics]]
- [[Retry Pattern]]
- [[Observability]]
- [[Alerting]]
