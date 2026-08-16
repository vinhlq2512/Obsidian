---
type: concept
status: developing
sources:
  - "[[2025-06-19_a-guide-to-database-transactions-from-acid-to-concurrency-co]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - database
  - concurrency
---

# Optimistic Locking

## Định nghĩa

Optimistic locking là concurrency control strategy cho transaction chạy mà không khóa trước, rồi kiểm tra version hoặc điều kiện lúc commit để phát hiện conflict.

## Cách hiểu bằng lời của tôi

Đây là kiểu "cứ làm đi, cuối cùng xem dữ liệu có bị ai đổi chưa". Nếu version đã đổi, update thất bại và caller phải retry trên dữ liệu mới.

## Pattern phổ biến

```sql
UPDATE products
SET stock = 150, version = version + 1
WHERE id = 42 AND version = 3;
```

Nếu không có row nào được update, nghĩa là version đã thay đổi và transaction bị conflict.

## Trade-off

- Giảm blocking và phù hợp workload read-heavy/low-contention.
- Có thể tạo nhiều retry khi nhiều transaction cùng cập nhật một record nóng.
- Retry phải có backoff và timeout, nếu không có thể góp phần tạo [[Retry Storm]].

## Liên kết

- [[Concurrency Control]]
- [[Transaction Isolation]]
- [[Database Transaction]]
- [[Retry Pattern]]
