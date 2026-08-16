---
type: concept
status: developing
sources:
  - "[[2026-04-23_b-trees-vs-lsm-trees-comparison-and-trade-offs]]"
  - "[[2025-03-18_how-netflix-stores-140-million-hours-of-viewing-data-per-day]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - database
  - storage
---

# Storage Engine

## Định nghĩa

Storage engine là lớp trong database quyết định dữ liệu được ghi, đọc, index, flush, compact và recover trên storage vật lý như thế nào.

## Cách hiểu bằng lời của tôi

Database query ở tầng SQL/Document nhìn có vẻ giống nhau, nhưng hành vi thật bị quyết định bởi storage engine: nó ưu tiên read hay write, random hay sequential I/O, memory hay disk, compaction hay in-place update.

## Trục trade-off

- [[B-Tree]]: trả chi phí write để read/range query nhanh.
- [[LSM Tree]]: trả chi phí read/compaction để write nhanh.
- SSD làm random write bớt đắt hơn HDD, nên trade-off còn phụ thuộc hardware.
- Chọn database nghĩa là thường đã chọn storage engine mặc định của nó.

## Khi workload time-series tăng

Nguồn Netflix viewing history cho thấy LSM/SSTable không miễn phí ở read path: khi dữ liệu mỗi user lớn dần, read phải chạm nhiều SSTable hơn và compaction/read repair trở thành chi phí nền đáng kể. Vì vậy storage engine phải đi cùng data model, chunking, cache và lifecycle policy.

## Liên kết

- [[Database Indexing]]
- [[B-Tree]]
- [[LSM Tree]]
- [[Write Amplification]]
- [[Read Amplification]]
- [[Space Amplification]]
- [[Time-Series Data Storage]]
