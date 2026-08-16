---
type: concept
status: understood
sources:
  - "[[2023-09-07_how-to-choose-a-replication-strategy]]"
  - "[[2025-07-03_a-guide-to-database-replication-key-concepts-and-strategies-newsletter]]"
source_sections:
  - "[[2023-09-07_how-to-choose-a-replication-strategy]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - database
  - distributed-systems
---

# Data Replication

## Cách hiểu bằng lời của tôi

[[Data Replication]] là việc giữ nhiều bản sao dữ liệu trên nhiều node/region để tăng availability, durability, read scalability hoặc latency. Nó không miễn phí: bản sao càng nhiều thì hệ thống càng phải trả giá bằng lag, conflict, coordination hoặc chi phí vận hành.

## Các chiến lược chính

- Leader-follower: một leader nhận write, follower nhận bản sao và có thể phục vụ read. Dễ hiểu, phù hợp read-heavy, nhưng leader là điểm trọng yếu.
- Multi-leader: nhiều leader có thể nhận write. Tăng write availability và giảm latency địa lý, nhưng cần xử lý conflict.
- Leaderless: không có leader cố định, read/write dùng quorum. Tăng availability, nhưng consistency phụ thuộc quorum và conflict resolution.

## Công thức quorum

Với replication factor `n`, write quorum `w`, read quorum `r`:

```text
w + r > n
```

Điều kiện này tạo overlap giữa read và write quorum, giúp read có cơ hội thấy write mới nhất. Đây là trực giác, không phải cam kết tuyệt đối nếu hệ thống còn clock skew, conflict hoặc implementation detail khác.

## Trade-off cần nhớ

- Strong consistency thường làm tăng latency hoặc giảm availability.
- Async replication tăng performance nhưng có replication lag.
- Multi-leader cần chiến lược conflict resolution rõ ràng.
- Replication factor cao tăng resilience nhưng tốn storage và network.

## Liên kết

- [[High Availability]]
- [[Eventual Consistency]]
- [[Database Sharding]]
- [[Read Replica]]
- [[Strong Consistency]]
- [[Consensus]]
- [[Quorum]]
- [[Scalable Distributed Systems Patterns]]
