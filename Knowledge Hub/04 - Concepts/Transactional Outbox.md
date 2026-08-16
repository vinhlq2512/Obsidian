---
type: concept
status: developing
sources:
  - "[[2026-08-06_the-read-path-versus-the-write-path-strategies-and-technique]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - database
  - event-driven
---

# Transactional Outbox

## Định nghĩa

Transactional outbox là pattern ghi business change và event record vào cùng database transaction, sau đó một publisher riêng đọc outbox để phát event.

## Cách hiểu bằng lời của tôi

Pattern này tránh lỗi dual-write: database update thành công nhưng publish event fail, hoặc ngược lại. Event chưa cần rời database ngay, nhưng phải được ghi cùng transaction với state change để không mất sự thật đã commit.

## Cơ chế

```text
BEGIN
-> update business table
-> insert outbox event
-> COMMIT
-> publisher đọc outbox
-> publish tới broker/downstream
```

## Liên kết

- [[Database Transaction]]
- [[Change Data Capture]]
- [[Message Broker]]
- [[Idempotency Key]]
- [[Eventual Consistency]]
