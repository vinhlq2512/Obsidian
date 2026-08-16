---
type: concept
status: developing
sources:
  - "[[2025-06-19_a-guide-to-database-transactions-from-acid-to-concurrency-co]]"
  - "[[2025-02-27_mastering-data-consistency-across-microservices]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - database
  - system-design
---

# Database Transaction

## Định nghĩa

Database transaction là nhóm read/write operations được xử lý như một đơn vị all-or-nothing: hoặc commit toàn bộ, hoặc rollback toàn bộ.

## Cách hiểu bằng lời của tôi

Transaction là cách database ngăn hệ thống rơi vào trạng thái nửa chừng. Chuyển tiền, đặt hàng, giữ inventory hay ghi booking thường cần nhiều bước; nếu một bước fail thì toàn bộ operation logic phải được xem như chưa xảy ra.

## Lifecycle

```text
BEGIN
-> READ / WRITE
-> COMMIT nếu hợp lệ
-> ROLLBACK nếu lỗi hoặc abort
```

## Cần biết

- Transaction càng dài càng giữ lock/resource lâu và tăng contention.
- Không nên gọi network hoặc chờ user input trong transaction mở.
- Cần truy cập dữ liệu theo thứ tự nhất quán để giảm deadlock.
- Transaction retry cần backoff, timeout và logging rõ.

## Liên kết

- [[ACID]]
- [[Transaction Isolation]]
- [[Concurrency Control]]
- [[Write-Ahead Log]]
- [[Retry Pattern]]
- [[Serializability]]
- [[Saga Pattern]]
- [[Transactional Outbox]]
