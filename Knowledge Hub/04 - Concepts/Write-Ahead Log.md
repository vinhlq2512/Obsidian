---
type: concept
status: developing
sources:
  - "[[2025-06-19_a-guide-to-database-transactions-from-acid-to-concurrency-co]]"
  - "[[2026-04-23_b-trees-vs-lsm-trees-comparison-and-trade-offs]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - database
  - storage
---

# Write-Ahead Log

## Định nghĩa

Write-ahead log là log bền vững ghi ý định thay đổi trước khi thay đổi được áp vào storage chính, giúp database recover sau crash và giữ atomicity/durability.

## Cách hiểu bằng lời của tôi

Trước khi sửa dữ liệu thật, database ghi "tôi định sửa gì" vào log. Nếu crash giữa chừng, nó đọc log để biết cần undo hoặc redo gì, thay vì đoán trạng thái nửa vời.

## Cần biết

- WAL thường được fsync/persist trước khi database acknowledge commit.
- B-Tree và LSM đều có thể dùng WAL, nhưng phần storage structure phía sau khác nhau.
- WAL thêm write amplification nhưng đổi lại crash recovery đáng tin cậy.

## Liên kết

- [[ACID]]
- [[Database Transaction]]
- [[B-Tree]]
- [[LSM Tree]]
