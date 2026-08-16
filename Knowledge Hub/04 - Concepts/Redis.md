---
type: concept
status: understood
sources:
  - "[[2023-09-21_a-crash-course-in-redis]]"
  - "[[2023-10-12_the-6-most-impactful-ways-redis-is-used-in-production-system]]"
  - "[[2024-11-21_distributed-caching-the-secret-to-high-performance-applicati]]"
source_sections:
  - "[[2023-09-21_a-crash-course-in-redis]]"
  - "[[2023-10-12_the-6-most-impactful-ways-redis-is-used-in-production-system]]"
  - "[[2024-11-21_distributed-caching-the-secret-to-high-performance-applicati]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - system-design
  - caching
---

# Redis

## Định nghĩa

Redis là in-memory data store thường dùng làm cache, session store, lightweight message broker, leaderboard, counter và một số workload real-time cần latency thấp.

## Cách hiểu bằng lời của tôi

Redis nhanh không chỉ vì "nằm trong RAM". Nó kết hợp [[Redis Data Structures]], hash table keyspace, [[Redis Event Loop]], persistence nền, replication và các primitive như Sorted Set, Stream, HyperLogLog để xử lý nhiều bài toán hot-path mà database chính không nên gánh.

## Khi dùng

- Cache dữ liệu hot để giảm latency và tải cho database.
- Lưu session chung để app server không cần sticky session.
- Làm leaderboard bằng [[Redis Sorted Set]].
- Làm queue/event log nhẹ bằng [[Redis Streams]] hoặc Pub/Sub khi yêu cầu reliability không quá nặng.
- Làm approximate analytics bằng [[HyperLogLog]].
- Làm [[Distributed Lock]] cho một số case cần mutual exclusion đơn giản.

## Giới hạn

- Memory đắt hơn disk; dữ liệu phải được chọn lọc bằng [[Cache Eviction Policy]] hoặc sharding.
- Nếu dùng Redis như message system, cần hiểu rõ khác biệt giữa List, Stream và Pub/Sub.
- Nếu Redis thành dependency duy nhất cho hot path, cần thiết kế failover, replication và degradation.

## Liên kết

- [[Caching Strategy]]
- [[Distributed Cache]]
- [[Redis Persistence]]
- [[Redis Event Loop]]
- [[Cache Invalidation]]
