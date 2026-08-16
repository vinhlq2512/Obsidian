---
type: concept
status: seed
sources:
  - "[[2025-03-18_how-netflix-stores-140-million-hours-of-viewing-data-per-day]]"
  - "[[2025-02-11_how-netflix-built-a-distributed-counter-for-billions-of-user]]"
  - "[[2026-01-21_how-netflix-built-a-real-time-distributed-graph-for-internet]]"
  - "[[2026-03-24_how-netflix-live-streams-to-100-million-devices-in-60-second]]"
source_sections:
  - "[[2025-03-18_how-netflix-stores-140-million-hours-of-viewing-data-per-day]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - database
  - distributed-systems
---

# Cassandra

## Định nghĩa

[[Cassandra]] là distributed wide-column database thường được dùng cho workload write-heavy, high availability, partitioned data và eventual/tunable consistency.

## Cách hiểu bằng lời của tôi

Cassandra phù hợp khi dữ liệu có thể được model theo key/partition rõ ràng và hệ thống cần ghi rất nhiều với availability cao. Giá phải trả là phải thiết kế query theo access pattern, tránh partition quá rộng, hiểu compaction/SSTable, và chấp nhận consistency trade-off.

## Pattern xuất hiện trong nguồn Netflix

- Viewing history: lưu time-series theo user, sau đó phải tách recent/old/historical vì row rộng và SSTable nhiều làm read chậm.
- Distributed counter: lưu raw event/rollup durable, kết hợp cache để đọc nhanh.
- Live Origin: dùng storage chunked và local quorum để bảo vệ write availability.
- Real-time graph: làm backend cho key-value graph storage qua namespace tách biệt.

## Cần chú ý

- Hợp với write-heavy workload hơn read pattern tùy ý.
- Partition key và time bucket quyết định rất nhiều tới performance.
- Compaction, read repair và wide partition có thể thành bottleneck khi dữ liệu tăng.
- Cache như EVCache thường được đặt phía trước để giảm read load.

## Liên kết

- [[LSM Tree]]
- [[Storage Engine]]
- [[Database Sharding]]
- [[Eventual Consistency]]
- [[Quorum]]
- [[Time-Series Data Storage]]
