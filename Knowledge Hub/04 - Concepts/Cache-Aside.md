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
  - caching
  - system-design
---

# Cache-Aside

## Định nghĩa

Cache-Aside là chiến lược ứng dụng tự đọc cache trước, nếu miss thì đọc database rồi ghi kết quả vào cache cho lần sau.

## Cách hiểu bằng lời của tôi

Cache-aside để cache là lớp tăng tốc bên cạnh source of truth. App chịu trách nhiệm xử lý cache miss, nên pattern này đơn giản và kiểm soát tốt, nhưng logic cache nằm trong application code.

## Flow

```text
request
-> read cache
-> hit: return cached value
-> miss: read database
-> write cache
-> return value
```

## Trade-off

- Ưu: chỉ cache dữ liệu thật sự được truy cập, tiết kiệm memory.
- Nhược: cache miss có cold-start latency và có nguy cơ [[Cache Stampede]] nếu nhiều request miss cùng lúc.

## Liên kết

- [[Caching Strategy]]
- [[Distributed Cache]]
- [[Read-Through Cache]]
- [[Cache Invalidation]]
