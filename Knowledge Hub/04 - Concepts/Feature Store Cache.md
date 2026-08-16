---
type: concept
status: understood
sources:
  - "[[2024-03-25_doordash-s-game-changing-strategy-70-hit-ratio-in-cache-opti]]"
  - "[[2026-01-12_processing-trillions-how-lyft-s-feature-store-grew-by-12-33]]"
  - "[[2026-05-19_how-snapchat-serves-a-billion-predictions-per-second]]"
source_sections:
  - "[[2024-03-25_doordash-s-game-changing-strategy-70-hit-ratio-in-cache-opti]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - machine-learning
  - caching
  - system-design
---

# Feature Store Cache

## Định nghĩa

Feature Store Cache là cache layer dùng để phục vụ feature lookup latency thấp cho online prediction hoặc model serving.

## Cách hiểu bằng lời của tôi

Feature store thường nằm trên hot path của inference. Nếu mỗi prediction phải đọc nhiều feature từ Redis hoặc store trung tâm, cost và latency tăng nhanh. Local/in-process cache có thể giảm request tới feature store, nhưng phải quan sát hit rate, memory, freshness và thread safety.

Lyft dùng DynamoDB làm source of truth cho online feature, ValKey làm write-through cache, rồi tối ưu payload, pod sizing, retry/timeout và TTL để giảm P95 latency. Snap đi xa hơn với một số ranking workload: document features được colocate trong memory của inference instance để tránh network fanout.

## Cơ chế từ DoorDash

- Thêm in-memory pod-local cache trước Redis feature store.
- Dùng LRU để giới hạn memory.
- Đo latency, hit rate, cache size và memory usage.
- Cân nhắc [[Cache Warmup]] để tránh slow start khi service restart.
- Dùng event/Kafka để giữ feature mới hơn trong cache.

## Trade-off

- Giảm latency và chi phí Redis.
- Tăng nguy cơ stale feature nếu invalidation/update không tốt.
- Local cache phân tán làm observability và consistency khó hơn.

## Liên kết

- [[Feature Store]]
- [[Online Feature Store]]
- [[Feature Collocation]]
- [[AI Model Serving]]
- [[Cache Eviction Policy]]
- [[Cache Invalidation]]
- [[Observability]]
