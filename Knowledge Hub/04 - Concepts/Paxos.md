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

# Paxos

## Định nghĩa

Paxos là consensus algorithm dùng proposal number, prepare/promise và propose/accept để các node đồng ý một value an toàn.

## Cách hiểu bằng lời của tôi

Paxos không bắt đầu bằng "node này là boss". Bất kỳ proposer nào cũng có thể đưa value, nhưng value chỉ thắng khi được quorum accept. Safety đến từ việc proposal mới phải tôn trọng value đã được accept trước đó.

## Vì sao khó

- Proposal number phải unique và ordered.
- Node phải persist promise/accepted value qua restart.
- Multiple proposers có thể làm hệ thống chậm hoặc khó reason.
- Multi-Paxos thêm stable leader để giảm chi phí lặp lại.

## Liên kết

- [[Consensus]]
- [[Quorum]]
- [[Leader Election]]
- [[Raft]]
