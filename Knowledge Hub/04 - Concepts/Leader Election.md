---
type: concept
status: developing
sources:
  - "[[2025-07-31_top-leader-election-algorithms-in-distributed-databases]]"
  - "[[2026-02-26_strong-consistency-in-databases-promises-and-costs]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - distributed-systems
  - database
---

# Leader Election

## Định nghĩa

Leader election là cơ chế để các node trong hệ phân tán đồng ý node nào đang chịu trách nhiệm điều phối write, replication hoặc coordination.

## Cách hiểu bằng lời của tôi

Leader election trả lời câu hỏi "ai đang được quyền quyết định?". Câu trả lời phải sống được qua crash, network delay, partition và restart, vì nhầm leader có thể gây split-brain hoặc conflicting writes.

## Cách tiếp cận

- Bully/Ring đơn giản nhưng giả định mạnh về membership và failure detection.
- [[Paxos]], [[Raft]] và Zab dùng quorum để an toàn hơn dưới partial failure.
- Candidate phải đủ mới; leader cũ/stale phải bị reject theo term/epoch/log freshness.

## Liên kết

- [[Consensus]]
- [[Quorum]]
- [[Failover]]
- [[Strong Consistency]]
- [[Correlated Failure]]
