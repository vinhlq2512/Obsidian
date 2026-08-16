---
type: concept
status: seed
sources:
  - "[[2025-07-31_top-leader-election-algorithms-in-distributed-databases]]"
  - "[[2026-02-26_strong-consistency-in-databases-promises-and-costs]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - distributed-systems
  - consensus
---

# Raft

## Định nghĩa

Raft là consensus algorithm dùng leader rõ ràng, term, RequestVote và AppendEntries để replicate log an toàn qua nhiều node.

## Cách hiểu bằng lời của tôi

Raft cố làm consensus dễ hiểu hơn Paxos. Node là follower, candidate hoặc leader. Nếu follower không thấy heartbeat, nó thành candidate, tăng term, xin vote. Nếu được majority, nó thành leader và replicate log.

## Safety idea

- Một leader cần majority vote.
- Node chỉ vote một lần trong một term.
- Candidate log phải ít nhất mới bằng voter.
- Stale leader bị reject nếu follower đã thấy term mới hơn.

## Liên kết

- [[Consensus]]
- [[Quorum]]
- [[Leader Election]]
- [[Strong Consistency]]
