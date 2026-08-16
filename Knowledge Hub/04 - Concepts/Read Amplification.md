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

# Read Amplification

## Định nghĩa

Read amplification là số lượng read vật lý mà storage engine phải thực hiện để phục vụ một read logic.

## Cách hiểu bằng lời của tôi

User hỏi một key, nhưng database có thể phải đọc nhiều page hoặc nhiều file để chắc chắn tìm thấy hoặc chắc chắn không có key đó.

## Trong storage engine

- B-Tree thường đọc vài page từ root xuống leaf, nhiều page trên cao thường đã cache.
- LSM Tree có thể phải kiểm nhiều SSTable, đặc biệt với key không tồn tại; [[Bloom Filter]] giúp giảm số file cần đọc.

## Liên kết

- [[Storage Engine]]
- [[B-Tree]]
- [[LSM Tree]]
- [[Bloom Filter]]
