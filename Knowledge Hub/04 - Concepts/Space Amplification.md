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
  - storage
---

# Space Amplification

## Định nghĩa

Space amplification là lượng storage thực tế database dùng vượt quá kích thước dữ liệu logic.

## Cách hiểu bằng lời của tôi

Database cần metadata, index, log và đôi khi giữ nhiều phiên bản dữ liệu tạm thời. Vì vậy 100GB data logic có thể tiêu tốn nhiều hơn 100GB disk.

## Trong storage engine

- LSM Tree có thể giữ nhiều phiên bản của cùng key cho tới khi compaction dọn.
- B-Tree có page trống sau split hoặc fragmentation, nhưng thường ít space amplification hơn LSM.

## Liên kết

- [[Storage Engine]]
- [[LSM Tree]]
- [[B-Tree]]
- [[Compaction]]
