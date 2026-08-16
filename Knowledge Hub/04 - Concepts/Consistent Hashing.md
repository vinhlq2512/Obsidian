---
type: concept
status: seed
sources:
  - "[[2025-07-17_a-guide-to-database-sharding-key-strategies-newsletter]]"
  - "[[2024-06-27_a-crash-course-in-database-sharding-newsletter]]"
source_sections:
  - "[[2025-07-17_a-guide-to-database-sharding-key-strategies-newsletter]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - database
  - distributed-systems
---

# Consistent Hashing

## Cách hiểu bằng lời của tôi

[[Consistent Hashing]] là kỹ thuật ánh xạ key vào node sao cho khi thêm/bớt node, chỉ một phần key cần di chuyển. Nó thường xuất hiện trong sharding, cache cluster và hệ phân tán cần rebalancing ít gián đoạn hơn so với modulo hashing đơn giản.

## Vì sao liên quan tới sharding

Trong [[Database Sharding]], hash-based sharding phân phối key đều hơn range-based sharding, nhưng khi số shard/node thay đổi, mapping có thể bị xáo trộn. Consistent hashing giảm lượng dữ liệu cần remap khi topology thay đổi.

## Liên kết

- [[Database Sharding]]
- [[Load Balancer]]
- [[Scalable Distributed Systems Patterns]]
