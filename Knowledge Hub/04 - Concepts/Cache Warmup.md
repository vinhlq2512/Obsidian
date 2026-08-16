---
type: concept
status: understood
sources:
  - "[[2024-03-25_doordash-s-game-changing-strategy-70-hit-ratio-in-cache-opti]]"
  - "[[2024-11-21_distributed-caching-the-secret-to-high-performance-applicati]]"
source_sections:
  - "[[2024-03-25_doordash-s-game-changing-strategy-70-hit-ratio-in-cache-opti]]"
  - "[[2024-11-21_distributed-caching-the-secret-to-high-performance-applicati]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - caching
  - reliability
---

# Cache Warmup

## Định nghĩa

Cache Warmup là kỹ thuật nạp trước dữ liệu hot vào cache trước hoặc ngay khi instance mới nhận traffic thật.

## Cách hiểu bằng lời của tôi

Cache miss không chỉ làm một request chậm; khi nhiều instance restart hoặc scale out cùng lúc, cold cache có thể đẩy tải dồn về Redis/database. Warmup dùng traffic mô phỏng, prefetch hoặc preload để instance bước vào production với cache đã có phần dữ liệu quan trọng.

## Khi áp dụng

- Service mới deploy/restart có local cache.
- Hệ thống có hot key hoặc feature lookup lặp lại.
- Cache miss có cost cao hoặc gây latency spike.

## Liên kết

- [[Cache-Aside]]
- [[Cache Stampede]]
- [[Feature Store Cache]]
- [[Phased Rollout]]
