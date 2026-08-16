---
type: concept
status: seed
sources:
  - "[[2026-04-23_b-trees-vs-lsm-trees-comparison-and-trade-offs]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - database
  - data-structure
---

# Bloom Filter

## Định nghĩa

Bloom filter là cấu trúc dữ liệu xác suất cho biết một key chắc chắn không tồn tại hoặc có thể tồn tại trong một tập.

## Cách hiểu bằng lời của tôi

Bloom filter là bộ lọc rẻ trước khi đọc disk. Nếu nó nói "không có", ta tin chắc và bỏ qua file. Nếu nó nói "có thể có", ta vẫn phải kiểm tra thật vì có false positive.

## Trong LSM Tree

Mỗi SSTable có thể gắn Bloom filter. Khi đọc một key, storage engine dùng Bloom filter để bỏ qua các SSTable chắc chắn không chứa key, giảm read amplification.

## Liên kết

- [[LSM Tree]]
- [[Read Amplification]]
- [[Storage Engine]]
