---
type: synthesis
status: developing
concepts:
  - "[[Database Transaction]]"
  - "[[ACID]]"
  - "[[Transaction Isolation]]"
  - "[[Read Path]]"
  - "[[Write Path]]"
  - "[[Staleness]]"
  - "[[Read Replica]]"
  - "[[Materialized View]]"
  - "[[Change Data Capture]]"
  - "[[Transactional Outbox]]"
  - "[[CQRS]]"
  - "[[Strong Consistency]]"
  - "[[Consensus]]"
  - "[[Concurrency Control]]"
  - "[[MVCC]]"
  - "[[Snapshot Isolation]]"
  - "[[Deadlock]]"
  - "[[Query Execution Plan]]"
  - "[[Query Planner]]"
  - "[[Storage Engine]]"
  - "[[B-Tree]]"
  - "[[LSM Tree]]"
sources:
  - "[[2025-06-19_a-guide-to-database-transactions-from-acid-to-concurrency-co]]"
  - "[[2026-04-23_b-trees-vs-lsm-trees-comparison-and-trade-offs]]"
  - "[[2026-08-06_the-read-path-versus-the-write-path-strategies-and-technique]]"
  - "[[2026-02-26_strong-consistency-in-databases-promises-and-costs]]"
  - "[[2025-02-27_mastering-data-consistency-across-microservices]]"
  - "[[2025-07-31_top-leader-election-algorithms-in-distributed-databases]]"
  - "[[2024-12-12_database-performance-demystified-essential-tips-and-strategi]]"
  - "[[2026-04-02_database-performance-strategies-and-their-hidden-costs]]"
created_at: 2026-08-16
updated_at: 2026-08-16
tags:
  - synthesis
  - database
  - system-design
---

# Database Internals Tradeoffs

## Hai tầng trade-off

Database correctness và performance cùng nằm trong hai tầng quyết định:

- transaction/concurrency: đổi isolation và locking để lấy correctness hoặc throughput;
- storage engine: đổi read/write/space amplification để phù hợp access pattern.

## Transaction layer

[[Database Transaction]] gom nhiều operation thành một đơn vị all-or-nothing. [[ACID]] mô tả guarantee mong muốn, nhưng [[Transaction Isolation]] luôn là trade-off: càng gần serializable càng an toàn, càng dễ contention. [[Concurrency Control]] chọn giữa blocking sớm bằng [[Pessimistic Locking]] hoặc validate muộn bằng [[Optimistic Locking]].

[[MVCC]] và [[Snapshot Isolation]] là cách nhiều database giảm blocking giữa reader và writer, nhưng chúng không xóa trade-off correctness/performance. Transaction dài, lock order không nhất quán hoặc retry thiếu kiểm soát vẫn có thể tạo [[Deadlock]] và retry herd.

## Query layer

[[Query Execution Plan]] cho biết bottleneck thật nằm ở [[Full Table Scan]], index không được dùng, join order xấu, sort/aggregate nặng hay statistics sai. [[Query Planner]] chỉ chọn tốt khi schema, index và statistics phản ánh workload thật.

## Storage layer

[[B-Tree]] tổ chức dữ liệu sorted trên disk, trả chi phí write để read/range query nhanh. [[LSM Tree]] defer organization: write vào memtable/SSTable nhanh, rồi trả chi phí qua [[Compaction]], [[Read Amplification]], [[Write Amplification]] và [[Space Amplification]].

## Read/write path

[[Read Path]] muốn câu trả lời đã precompute, nhiều copy, ít coordination. [[Write Path]] muốn một source of truth, invariant rõ và ordering an toàn. Vì vậy read optimization như [[Read Replica]], [[Materialized View]], cache, specialized read store hoặc fan-out đều phải trả bằng [[Staleness]], sync pipeline hoặc write amplification.

## Distributed consistency

[[Strong Consistency]] thường cần [[Consensus]] và [[Quorum]], đổi lại read sau write không thấy state cũ. [[Eventual Consistency]] giảm coordination nhưng đẩy trách nhiệm sang conflict resolution, [[Read-Your-Writes Consistency]], [[Saga Pattern]], [[Change Data Capture]] hoặc [[Transactional Outbox]].

## Ghi nhớ

Không có storage engine hay isolation level "tốt nhất". Câu hỏi đúng là workload đang muốn trả chi phí ở đâu: write latency, read latency, disk space, contention, retry hay operational complexity.

## Liên kết

- [[Database Indexing]]
- [[Database Performance Tradeoffs]]
- [[Database Schema Design]]
- [[CAP and PACELC]]
- [[Scalable Distributed Systems Patterns]]
- [[Resilience Failure Control Patterns]]
