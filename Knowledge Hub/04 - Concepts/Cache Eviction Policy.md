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

# Cache Eviction Policy

## Định nghĩa

Cache Eviction Policy là quy tắc chọn entry nào bị đẩy khỏi cache khi cache hết memory hoặc cần giới hạn kích thước.

## Cách hiểu bằng lời của tôi

Cache memory luôn hữu hạn, nên eviction policy là cách hệ thống đặt cược dữ liệu nào có giá trị giữ lại nhất. LRU giữ dữ liệu vừa dùng gần đây, LFU giữ dữ liệu dùng thường xuyên, TTL loại bỏ dữ liệu theo tuổi.

## Khi chọn policy

- LRU hợp với locality theo thời gian.
- LFU hợp khi có nhóm key hot ổn định.
- TTL hợp khi freshness quan trọng hoặc dữ liệu tự nhiên hết giá trị sau một khoảng thời gian.

## Liên kết

- [[Caching Strategy]]
- [[Redis]]
- [[Cache Invalidation]]
- [[Cost Optimization]]
