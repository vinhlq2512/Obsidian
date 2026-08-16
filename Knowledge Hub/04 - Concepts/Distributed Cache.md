---
type: concept
status: understood
sources:
  - "[[2024-11-21_distributed-caching-the-secret-to-high-performance-applicati]]"
  - "[[2023-10-12_the-6-most-impactful-ways-redis-is-used-in-production-system]]"
source_sections:
  - "[[2024-11-21_distributed-caching-the-secret-to-high-performance-applicati]]"
  - "[[2023-10-12_the-6-most-impactful-ways-redis-is-used-in-production-system]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - system-design
  - caching
---

# Distributed Cache

## Định nghĩa

Distributed Cache là cache layer được chia qua nhiều node để tăng dung lượng, throughput, fault tolerance và khả năng scale ngang.

## Cách hiểu bằng lời của tôi

Single-node cache là tối ưu latency đơn giản, nhưng dễ thành bottleneck và single point of failure. Distributed cache đưa cache thành một distributed system thật sự: cần sharding, replication, client routing, consistency, invalidation và observability.

## Thành phần chính

- Cache nodes giữ một phần dữ liệu hot.
- Client library định tuyến key tới node đúng, thường bằng [[Consistent Hashing]].
- Replication tăng availability khi một node lỗi.
- Sharding chia tải và memory footprint qua nhiều node.

## Rủi ro

- Cache inconsistency khi dữ liệu thay đổi nhanh.
- Network partition làm node giữ trạng thái lệch nhau.
- TTL sai có thể gây stale data hoặc cache miss quá nhiều.
- Replication và network hop có thể thêm latency.

## Liên kết

- [[Caching Strategy]]
- [[Redis]]
- [[Cache Invalidation]]
- [[Cache Stampede]]
- [[Data Replication]]
