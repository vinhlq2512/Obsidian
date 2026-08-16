---
type: concept
status: understood
sources:
  - "[[2025-07-17_a-guide-to-database-sharding-key-strategies-newsletter]]"
  - "[[2024-06-27_a-crash-course-in-database-sharding-newsletter]]"
  - "[[2025-03-18_how-netflix-stores-140-million-hours-of-viewing-data-per-day]]"
  - "[[2026-01-21_how-netflix-built-a-real-time-distributed-graph-for-internet]]"
source_sections:
  - "[[2025-07-17_a-guide-to-database-sharding-key-strategies-newsletter]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - database
  - system-design
---

# Database Sharding

## Cách hiểu bằng lời của tôi

[[Database Sharding]] là chia dữ liệu thành nhiều phần độc lập để không một node/database phải giữ toàn bộ dữ liệu hoặc chịu toàn bộ tải. Sharding giải quyết giới hạn scale của một database đơn, nhưng đổi lại query, transaction, rebalancing và operational complexity đều khó hơn.

## Chiến lược shard phổ biến

- Range-based sharding: chia theo khoảng key. Tốt cho range query nhưng dễ tạo hot shard nếu dữ liệu hoặc access skew.
- Hash/key-based sharding: hash key để phân tán đều hơn. Tốt cho point lookup nhưng range query kém hiệu quả.
- Directory-based sharding: dùng lookup table để map key sang shard. Linh hoạt khi cần điều khiển placement, nhưng lookup table trở thành dependency quan trọng.

## Chọn shard key

Shard key tốt cần:

- Cardinality đủ cao để chia nhỏ dữ liệu.
- Frequency không quá lệch, tránh một nhóm key chiếm đa số traffic.
- Không monotonic quá mạnh nếu workload write-heavy, vì timestamp/auto-increment dễ dồn write vào shard mới nhất.

## Trade-off cần nhớ

- Sharding làm tăng khả năng scale nhưng phá tính đơn giản của transaction cục bộ.
- Rebalancing phải hạn chế disruption khi thêm node hoặc dữ liệu lệch.
- Hot key vẫn có thể làm nghẽn shard dù hash function phân phối key đều.

## Sharding theo workload và lifecycle

Nguồn Netflix cho thấy shard không chỉ theo customer/key. Viewing history được tách theo loại dữ liệu và tuổi dữ liệu: full title plays, previews, language preferences; recent, past, historical. Real-time graph lại tách theo namespace cho từng node/edge type để mỗi nhóm có thể scale, cache và expire độc lập.

## Liên kết

- [[Data Replication]]
- [[Consistent Hashing]]
- [[High Availability]]
- [[Scalable Distributed Systems Patterns]]
- [[Time-Series Data Storage]]
- [[Key-Value Graph Storage]]
