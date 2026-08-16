---
type: concept
status: developing
sources:
  - "[[2026-02-26_strong-consistency-in-databases-promises-and-costs]]"
  - "[[2025-07-31_top-leader-election-algorithms-in-distributed-databases]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - distributed-systems
  - consistency
---

# Consensus

## Định nghĩa

Consensus là nhóm protocol giúp nhiều node đồng ý an toàn về một giá trị, log entry hoặc leader dù có crash, delay hoặc message loss.

## Cách hiểu bằng lời của tôi

Consensus là cái giá phải trả để nhiều máy hành xử như một nguồn sự thật. Thay vì một node tự quyết, write phải được propose, replicate và được quorum chấp nhận trước khi client nhận ack.

## Protocol thường gặp

- Paxos: an toàn nhưng khó implement và reason.
- Multi-Paxos: dùng stable proposer/leader để giảm overhead lặp lại.
- Raft: explicit leader, term, RequestVote, AppendEntries; dễ hiểu hơn Paxos.
- Zab/ZooKeeper: dùng cho coordination metadata và leader election.

## Liên kết

- [[Quorum]]
- [[Leader Election]]
- [[Raft]]
- [[Paxos]]
- [[Strong Consistency]]
- [[Distributed Systems]]
