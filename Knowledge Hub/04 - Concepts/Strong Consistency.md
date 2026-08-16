---
type: concept
status: developing
sources:
  - "[[2026-02-26_strong-consistency-in-databases-promises-and-costs]]"
  - "[[2025-02-27_mastering-data-consistency-across-microservices]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - consistency
  - distributed-systems
---

# Strong Consistency

## Định nghĩa

Strong consistency là guarantee rằng sau khi một write hoàn tất, mọi read sau đó đều thấy write đó hoặc giá trị mới hơn.

## Cách hiểu bằng lời của tôi

Từ góc nhìn client, hệ thống giống như chỉ có một bản dữ liệu luôn mới nhất, dù bên dưới có nhiều replica. Guarantee này thường cần [[Consensus]] và quorum, nên chi phí chính là latency và availability khi partition.

## Khi đáng trả giá

- Ledger, balance, payment.
- Inventory, booking, seat reservation.
- Distributed coordination, leader election, service discovery.
- Dữ liệu mà contradiction ngắn cũng gây thiệt hại thật.

## Trade-off

Không thể đồng thời có low-latency writes, regional survivability và strong consistency. Nếu muốn consistency toàn vùng, write phải chờ coordination qua khoảng cách vật lý.

## Liên kết

- [[Linearizability]]
- [[Strict Serializability]]
- [[Consensus]]
- [[Quorum]]
- [[CAP and PACELC]]
- [[Eventual Consistency]]
