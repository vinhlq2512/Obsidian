---
type: concept
status: understood
sources:
  - "[[2023-09-21_a-crash-course-in-redis]]"
  - "[[2023-10-12_the-6-most-impactful-ways-redis-is-used-in-production-system]]"
source_sections:
  - "[[2023-09-21_a-crash-course-in-redis]]"
  - "[[2023-10-12_the-6-most-impactful-ways-redis-is-used-in-production-system]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - data-structures
  - caching
---

# Redis Data Structures

## Định nghĩa

Redis Data Structures là tập kiểu dữ liệu trong Redis như String, List, Hash, Set, Sorted Set, Stream, Bitmap, HyperLogLog và Geospatial index.

## Cách hiểu bằng lời của tôi

Redis hữu ích vì nó không chỉ là key-value string store. Mỗi data structure đóng gói một pattern truy cập phổ biến: list cho queue đơn giản, sorted set cho rank, hash cho object nhỏ, stream cho log, HyperLogLog cho approximate cardinality.

## Điểm cần nhớ

- Redis keyspace dùng hash table để lookup key-value gần O(1).
- Value type có implementation tối ưu riêng, ví dụ SDS cho string và skip list cho sorted set lớn.
- Data structure càng tiện thì càng phải hiểu complexity của command; lệnh O(N) trên hot path có thể phá latency.

## Liên kết

- [[Redis]]
- [[Redis Sorted Set]]
- [[Redis Streams]]
- [[HyperLogLog]]
- data structure
