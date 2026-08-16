---
type: concept
status: seed
sources:
  - "[[2025-02-11_how-netflix-built-a-distributed-counter-for-billions-of-user]]"
source_sections:
  - "[[2025-02-11_how-netflix-built-a-distributed-counter-for-billions-of-user]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - system-design
  - distributed-systems
---

# Distributed Counter

## Định nghĩa

[[Distributed Counter]] là abstraction để tăng, giảm, đọc và reset counter khi update đến từ nhiều node/region với throughput rất cao.

## Cách hiểu bằng lời của tôi

Đếm trong một process thì đơn giản. Đếm trên toàn cầu thì khó vì retry có thể làm đếm đôi, hot counter có thể nghẽn một partition, read cần nhanh nhưng count chính xác lại cần durable event log hoặc aggregation. Vì vậy counter ở scale lớn thường là một tập trade-off giữa tốc độ, độ chính xác, độ bền và chi phí.

## Hai nhóm nhu cầu

- Best-effort counter: ưu tiên latency và throughput, chấp nhận gần đúng, phù hợp A/B test hoặc metric ngắn hạn.
- Eventually consistent counter: ưu tiên độ bền và count cuối cùng đúng, phù hợp billing, báo cáo quan trọng hoặc metric cần audit.

## API tối thiểu

- `add_count`: cộng/trừ một delta vào counter.
- `add_and_get_count`: cộng/trừ rồi trả count mới.
- `get_count`: đọc count hiện tại, có thể hơi stale.
- `clear_count`: reset counter, cần idempotency để retry an toàn.

## Điều phải thiết kế cẩn thận

- [[Idempotency Key]] hoặc event id để tránh double-count khi retry.
- Partitioning theo counter key để tránh hot shard.
- Rollup để không phải scan raw event khi đọc.
- Cache cho counter nóng, chấp nhận freshness policy rõ ràng.
- Retention cho raw events và aggregated rollups.

## Liên kết

- [[Rollup Pipeline]]
- [[Event Log]]
- [[Idempotency Key]]
- [[Eventual Consistency]]
- [[Caching Strategy]]
- [[Database Sharding]]
