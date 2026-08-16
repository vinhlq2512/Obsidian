---
type: synthesis
status: seed
concepts:
  - "[[Redis]]"
  - "[[Distributed Cache]]"
  - "[[Redis Data Structures]]"
  - "[[Redis Event Loop]]"
  - "[[Redis Persistence]]"
  - "[[Cache-Aside]]"
  - "[[Read-Through Cache]]"
  - "[[Write-Through Cache]]"
  - "[[Write-Behind Cache]]"
  - "[[Cache Invalidation]]"
  - "[[Cache Eviction Policy]]"
  - "[[Redis Streams]]"
  - "[[Redis Sorted Set]]"
  - "[[HyperLogLog]]"
  - "[[Distributed Lock]]"
  - "[[Cache Warmup]]"
  - "[[Feature Store Cache]]"
sources:
  - "[[2023-09-21_a-crash-course-in-redis]]"
  - "[[2023-10-12_the-6-most-impactful-ways-redis-is-used-in-production-system]]"
  - "[[2024-11-21_distributed-caching-the-secret-to-high-performance-applicati]]"
  - "[[2024-03-25_doordash-s-game-changing-strategy-70-hit-ratio-in-cache-opti]]"
questions: []
created_at: 2026-08-16
updated_at: 2026-08-16
tags:
  - synthesis
  - system-design
  - caching
---

# Redis and Distributed Caching Patterns

## Mental model

Caching là time-space trade-off: hệ thống trả thêm memory, invalidation và vận hành để mua latency thấp hơn. Redis là cache phổ biến vì nó còn cung cấp data structures và primitive real-time, nhưng khi cache scale ra nhiều node, vấn đề trở thành distributed systems: sharding, replication, consistency, failure và observability.

## Các lớp thiết kế

| Lớp | Concept | Câu hỏi thiết kế |
| --- | --- | --- |
| Engine | [[Redis]], [[Redis Event Loop]], [[Redis Persistence]], [[Redis Data Structures]] | Vì sao Redis nhanh, bền tới mức nào, lệnh nào an toàn trên hot path? |
| Cache topology | [[Distributed Cache]], [[Consistent Hashing]], [[Data Replication]] | Cache nằm local, dedicated node, hay managed service? Key được chia và replicate thế nào? |
| Read/write policy | [[Cache-Aside]], [[Read-Through Cache]], [[Write-Through Cache]], [[Write-Behind Cache]] | App hay cache layer chịu trách nhiệm miss/write? Đổi latency lấy consistency ra sao? |
| Freshness | [[Cache Invalidation]], [[Cache Eviction Policy]], [[Cache Warmup]], [[Cache Stampede]] | Khi nào cache entry hết tin cậy, bị loại, hoặc cần preload? |
| Redis primitives | [[Redis Streams]], [[Redis Sorted Set]], [[HyperLogLog]], [[Distributed Lock]] | Có nên dùng Redis cho queue, leaderboard, approximate analytics hoặc lock không? |
| ML hot path | [[Feature Store Cache]], [[AI Model Serving]] | Feature lookup có đang làm inference chậm hoặc tốn Redis quá mức không? |

## Bài học

- Redis không thay database chính; trong cache pattern thông thường, database vẫn là source of truth.
- Cache hit rate cao chỉ có ý nghĩa khi freshness, memory cost và failure mode được kiểm soát.
- Local cache giảm network hop nhưng làm consistency và rollout khó hơn.
- Distributed cache cần observability riêng: hit rate, miss rate, latency, memory, eviction, stale read và backend fallback.
- Redis Streams, Sorted Set, HyperLogLog và lock rất tiện, nhưng mỗi primitive có giới hạn về reliability, scale hoặc correctness.

## Liên kết

- [[Caching Strategy]]
- [[Object and Key-Value Storage Patterns]]
- [[Messaging and Event Streaming Patterns]]
- [[Reliability Operations Loop]]
