---
type: concept
status: understood
sources:
  - "[[2026-07-30_a-detailed-guide-to-idempotency-delivery-semantics-and-dedup]]"
  - "[[2025-02-06_mastering-idempotency-building-reliable-apis]]"
source_sections:
  - "[[2026-07-30_a-detailed-guide-to-idempotency-delivery-semantics-and-dedup]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - system-design
  - distributed-systems
---

# Idempotency Key

## Cách hiểu bằng lời của tôi

[[Idempotency Key]] là một identity ổn định cho một thao tác logic, giúp server nhận ra nhiều lần retry thật ra đang cố hoàn tất cùng một việc. Nó đặc biệt quan trọng với các operation không tự idempotent, ví dụ charge tiền, tạo order, gửi email, append event.

Một key tự nó không đủ. Nó chỉ có tác dụng khi đi cùng record bền vững về thao tác đã xử lý và một bước claim nguyên tử để tránh hai request đồng thời cùng vượt qua check.

## Cơ chế

```text
Client tạo key cho logical operation
-> gửi request kèm key
-> server atomic claim key trong durable store
-> nếu claim thành công: thực thi operation và lưu kết quả
-> nếu key đã tồn tại: trả lại kết quả cũ hoặc trạng thái đã xử lý
```

Ba thành phần bắt buộc:

- Identity: key phải đại diện cho thao tác logic, không phải từng attempt.
- Durable record: server phải nhớ key đã được xử lý trong một khoảng thời gian phù hợp.
- Atomic claim: check và claim phải là một hành động nguyên tử, nếu không retry đồng thời vẫn có thể tạo duplicate.

## Trade-off cần nhớ

- Deduplication window càng dài thì bảo vệ tốt hơn nhưng tốn storage hơn.
- Key hết hạn nghĩa là cùng key có thể được xem như operation mới.
- "Exactly once" trong thực tế thường là at-least-once delivery cộng deduplication ở receiver.
- HTTP method idempotent chỉ mô tả ý định; handler vẫn phải được viết đúng.

## Khi áp dụng

Dùng cho API payment, order creation, job submission, webhook processing, message consumer, hoặc bất kỳ workflow nào có retry mà side effect không được phép lặp lại.

## Liên kết

- [[Message Broker]]
- [[Eventual Consistency]]
- [[API Gateway]]
- [[Scalable Distributed Systems Patterns]]
