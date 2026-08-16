---
type: concept
status: seed
sources:
  - "[[2025-01-07_how-airbnb-built-a-key-value-store-for-petabytes-of-data]]"
  - "[[2025-06-29_when-kv-falls-cloudflares-two-hour-outage-byte-sized-design]]"
  - "[[2026-01-21_how-netflix-built-a-real-time-distributed-graph-for-internet]]"
source_sections:
  - "[[2025-01-07_how-airbnb-built-a-key-value-store-for-petabytes-of-data]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - database
  - distributed-systems
---

# Distributed Key-Value Store

## Định nghĩa

[[Distributed Key-Value Store]] là database phân tán lưu dữ liệu theo cặp key-value, scale bằng partition/sharding và replication để phục vụ lookup theo key với latency thấp.

## Cách hiểu bằng lời của tôi

Key-value store mạnh khi query chính là "biết key, lấy value". Để chạy ở quy mô lớn, hệ thống phải quyết định key được map vào shard nào, shard replicate ra sao, ai xử lý read/write, và update/rebuild dữ liệu kiểu batch hay realtime.

## Pattern từ Airbnb Mussel

- Shard theo hash của primary key.
- Dùng control plane như Helix để quản lý partition assignment.
- Dùng Kafka như write-ahead log để đồng bộ update.
- Cho replica đọc theo leaderless style để ưu tiên availability/read latency.
- Dùng LSM/HRegion, MemStore, BlockCache và compaction cho storage engine.

## Pitfall từ Cloudflare KV

Một key-value store có thể "distributed at edge" nhưng vẫn phụ thuộc source-of-truth tập trung. Nếu cold read/write cần backend đó và không có fallback, outage của storage phụ thuộc có thể kéo theo identity, config, asset delivery và nhiều sản phẩm khác.

## Liên kết

- [[Database Sharding]]
- [[Data Replication]]
- [[Event Log]]
- [[Apache Kafka]]
- [[LSM Tree]]
- [[Compaction]]
- [[Blast Radius]]
- [[Graceful Degradation]]
