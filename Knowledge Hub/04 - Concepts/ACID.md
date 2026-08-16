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
  - transaction
---

# ACID

## Định nghĩa

ACID là bốn guarantee của transaction đáng tin cậy: Atomicity, Consistency, Isolation và Durability.

## Cách hiểu bằng lời của tôi

ACID là hợp đồng giữa application và database. Nó nói rằng operation nhiều bước không bị nửa vời, không phá constraint, không nhìn thấy trạng thái giữa chừng của transaction khác, và nếu đã commit thì không mất sau crash.

## Bốn thuộc tính

- Atomicity: mọi bước cùng thành công hoặc cùng rollback.
- Consistency: transaction đưa database từ một valid state sang valid state khác.
- Isolation: transaction chạy đồng thời nhưng không thấy intermediate state của nhau.
- Durability: commit xong thì thay đổi được lưu bền vững.

## Cơ chế thường gặp

- Atomicity/durability thường dựa vào [[Write-Ahead Log]] hoặc undo/redo log.
- Isolation dựa vào lock, MVCC hoặc validation lúc commit.
- Consistency phụ thuộc cả constraint database và rule application.

## Liên kết

- [[Database Transaction]]
- [[Transaction Isolation]]
- [[Concurrency Control]]
- [[Write-Ahead Log]]
