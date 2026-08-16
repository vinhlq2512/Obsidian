---
type: concept
status: seed
sources:
  - "[[2025-02-25_how-amazon-s3-stores-350-trillion-objects-with-11-nines-of-d]]"
source_sections:
  - "[[2025-02-25_how-amazon-s3-stores-350-trillion-objects-with-11-nines-of-d]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - storage
  - indexing
---

# Object Metadata Index

## Định nghĩa

[[Object Metadata Index]] là lớp index phân tán map object key và metadata sang vị trí lưu trữ vật lý, giúp object storage tìm object bằng lookup thay vì scan toàn bộ dữ liệu.

## Cách hiểu bằng lời của tôi

Trong object storage, bytes của object và "bản đồ tìm object" là hai chuyện khác nhau. Nếu metadata index nghẽn, object vẫn còn đó nhưng hệ thống không tìm/ghi nhanh được. Vì vậy index phải shard, replicate, rebalance và sửa lỗi như một distributed database riêng.

## Cơ chế từ S3

- Global metadata store theo dõi bucket, key, permission và vị trí.
- Partitioning engine chia metadata theo key/prefix.
- Lexicographic key distribution giúp phân tán workload.
- Background indexing/auditing giữ index nhất quán và sửa entry lỗi.

## Pitfall

- Prefix quá đồng nhất có thể gom request vào một partition nóng.
- Metadata consistency ảnh hưởng trực tiếp tới read/write path.
- Index scale không tốt thì storage node còn rảnh cũng không cứu được latency.

## Liên kết

- [[Object Storage]]
- [[Amazon S3]]
- [[Database Sharding]]
- [[Database Indexing]]
- [[Consistent Hashing]]
- [[Data Replication]]
