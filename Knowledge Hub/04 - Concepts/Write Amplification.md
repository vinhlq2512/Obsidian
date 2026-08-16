---
type: concept
status: developing
sources:
  - "[[2026-04-23_b-trees-vs-lsm-trees-comparison-and-trade-offs]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - database
  - storage
---

# Write Amplification

## Định nghĩa

Write amplification là tỷ lệ giữa lượng ghi vật lý xuống storage và lượng ghi logic mà application yêu cầu.

## Cách hiểu bằng lời của tôi

Một write ở application không nhất thiết là một write ở disk. WAL, page split, flush, compaction hoặc replication có thể khiến cùng một dữ liệu bị ghi nhiều lần.

## Trong storage engine

- B-Tree có WAL và page split nhưng write amplification thường dự đoán được.
- LSM Tree ghi WAL, flush SSTable rồi rewrite trong compaction, nên tổng physical writes có thể lớn dù write ban đầu nhanh.

## Liên kết

- [[Storage Engine]]
- [[B-Tree]]
- [[LSM Tree]]
- [[Compaction]]
