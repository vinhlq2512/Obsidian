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

# Compaction

## Định nghĩa

Compaction là quá trình nền trong LSM-based storage đọc nhiều SSTable, merge chúng, giữ phiên bản mới nhất của key và ghi ra SSTable mới gọn hơn.

## Cách hiểu bằng lời của tôi

LSM Tree viết nhanh bằng cách để dữ liệu hơi lộn xộn trong nhiều file immutable. Compaction là người dọn nhà: gom file, bỏ bản cũ, giảm số nơi cần đọc. Nhưng dọn nhà cũng tốn CPU và I/O.

## Trade-off

- Compaction ít/aggressive thấp: write rẻ hơn nhưng read amplification tăng.
- Compaction nhiều/aggressive cao: read nhanh hơn nhưng write amplification và I/O nền tăng.
- Nếu write đến nhanh hơn compaction xử lý, SSTable phình ra và latency xấu dần.

## Liên kết

- [[LSM Tree]]
- [[Write Amplification]]
- [[Read Amplification]]
- [[Space Amplification]]
