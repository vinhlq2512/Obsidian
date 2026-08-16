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

# LSM Tree

## Định nghĩa

LSM Tree là storage/index design ghi dữ liệu vào memtable trong memory, flush thành SSTable immutable trên disk, rồi dùng compaction để merge và dọn phiên bản cũ.

## Cách hiểu bằng lời của tôi

LSM Tree không cố đặt mỗi write vào đúng chỗ trên disk ngay lập tức. Nó gom write lại, ghi tuần tự thành file sorted, rồi dọn dẹp sau. Đổi lại read phải kiểm nhiều nơi hơn.

## Cơ chế

```text
write
-> WAL
-> memtable
-> flush to SSTable
-> compaction merges SSTables
```

## Cần biết

- SSTable immutable nên write path nhanh và tuần tự.
- Compaction là chi phí nền nhưng cạnh tranh CPU/I/O với traffic thật.
- Bloom filter giúp bỏ qua SSTable chắc chắn không chứa key.
- Hợp với write-heavy workload như logging, event ingestion, metrics/time-series.
- Nếu một partition/row tích lũy quá nhiều record theo thời gian, read có thể chậm vì phải kiểm nhiều SSTable và chịu compaction/read-repair overhead.

## Liên kết

- [[Storage Engine]]
- [[B-Tree]]
- [[Write-Ahead Log]]
- [[Compaction]]
- [[Bloom Filter]]
- [[Write Amplification]]
- [[Read Amplification]]
- [[Time-Series Data Storage]]
