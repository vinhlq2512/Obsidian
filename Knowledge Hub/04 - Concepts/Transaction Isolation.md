---
type: concept
status: developing
sources:
  - "[[2025-06-19_a-guide-to-database-transactions-from-acid-to-concurrency-co]]"
  - "[[2026-02-26_strong-consistency-in-databases-promises-and-costs]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - database
  - transaction
---

# Transaction Isolation

## Định nghĩa

Transaction isolation là guarantee giới hạn cách các transaction đồng thời nhìn thấy thay đổi của nhau.

## Cách hiểu bằng lời của tôi

Database muốn chạy song song để có throughput, nhưng application lại muốn cảm giác như từng transaction chạy một mình. Isolation là núm chỉnh giữa correctness và performance.

## Isolation levels

- Read Uncommitted: có thể dirty read.
- Read Committed: chỉ đọc dữ liệu đã commit, nhưng có thể non-repeatable read.
- Repeatable Read: đọc lại cùng row thấy cùng giá trị, nhưng vẫn có thể phantom read tùy database.
- Serializable: hành vi như transaction chạy tuần tự, an toàn nhất nhưng dễ contention nhất.

## Anomalies

- Dirty read: đọc dữ liệu chưa commit rồi transaction kia rollback.
- Non-repeatable read: đọc cùng row hai lần ra hai kết quả.
- Phantom read: query điều kiện giống nhau nhưng lần sau có thêm row mới.

## Snapshot và MVCC

Nhiều database dùng [[MVCC]] để giảm blocking giữa reader và writer. Với [[Snapshot Isolation]], transaction đọc một snapshot nhất quán, nhưng không nên mặc định coi nó tương đương [[Serializability]] trong mọi engine.

## Liên kết

- [[Database Transaction]]
- [[ACID]]
- [[Concurrency Control]]
- [[MVCC]]
- [[Snapshot Isolation]]
- [[Deadlock]]
- [[Optimistic Locking]]
- [[Pessimistic Locking]]
- [[Serializability]]
- [[Strict Serializability]]
