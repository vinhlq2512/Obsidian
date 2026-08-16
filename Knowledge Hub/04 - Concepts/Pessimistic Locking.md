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

# Pessimistic Locking

## Định nghĩa

Pessimistic locking là concurrency control strategy giả định conflict có khả năng xảy ra, nên khóa dữ liệu trước khi transaction khác đọc/ghi.

## Cách hiểu bằng lời của tôi

Đây là kiểu "giữ chỗ trước rồi làm". Nó an toàn cho dữ liệu nóng nhưng khiến người khác phải chờ, nên dễ làm giảm throughput nếu lock giữ lâu.

## Granularity

- Row-level lock: chính xác nhất, chỉ khóa row liên quan.
- Table-level lock: đơn giản nhưng chặn nhiều operation không cần thiết.
- Page-level lock: khóa một nhóm row cùng page trên disk.

## Khi hợp

- Conflict thường xuyên và rollback đắt.
- Dữ liệu có tính critical như balance, inventory slot, booking.
- Transaction ngắn, access order rõ.

## Liên kết

- [[Concurrency Control]]
- [[Transaction Isolation]]
- [[Database Transaction]]
