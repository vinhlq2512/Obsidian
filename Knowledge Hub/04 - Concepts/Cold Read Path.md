---
type: concept
status: understood
sources:
  - "[[2025-06-29_when-kv-falls-cloudflares-two-hour-outage]]"
source_sections:
  - "[[2025-06-29_when-kv-falls-cloudflares-two-hour-outage]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - reliability
  - caching
---

# Cold Read Path

## Định nghĩa

Cold Read Path là đường đọc khi cache không có dữ liệu và request phải chạm source of truth hoặc backend dependency.

## Cách hiểu bằng lời của tôi

Cache hit làm hệ thống trông resilient hơn thực tế. Khi dependency source-of-truth lỗi, hot cache có thể giữ một phần traffic sống, nhưng cold read sẽ fail. Vì vậy cache không phải backup nếu hệ thống vẫn cần đọc dữ liệu mới hoặc dữ liệu chưa warm.

## Liên kết

- [[Caching Strategy]]
- [[Cache Stampede]]
- [[Cache Warmup]]
- [[Hidden Dependency]]
- [[Distributed Cache]]
