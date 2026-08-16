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

# Quorum

## Định nghĩa

Quorum là số lượng node tối thiểu cần đồng ý để hệ phân tán coi một decision hoặc write là committed.

## Cách hiểu bằng lời của tôi

Trong cụm 3 node, quorum thường là 2; trong cụm 5 node, quorum thường là 3. Quorum giúp chịu lỗi vì một node chết vẫn còn đa số, nhưng write phải chờ đủ phản hồi nên latency tăng theo khoảng cách giữa replica.

## Vai trò

- Commit write trong consensus.
- Tránh hai leader cùng hợp lệ trong cùng term/epoch.
- Đổi availability lấy safety khi partition làm mất majority.

## Liên kết

- [[Consensus]]
- [[Strong Consistency]]
- [[Raft]]
- [[Paxos]]
- [[CAP and PACELC]]
