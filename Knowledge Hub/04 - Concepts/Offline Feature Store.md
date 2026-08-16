---
type: concept
status: seed
sources:
  - "[[2026-01-12_processing-trillions-how-lyft-s-feature-store-grew-by-12-33]]"
  - "[[2026-05-19_how-snapchat-serves-a-billion-predictions-per-second]]"
source_sections:
  - "[[2026-01-12_processing-trillions-how-lyft-s-feature-store-grew-by-12-33]]"
  - "[[2026-05-19_how-snapchat-serves-a-billion-predictions-per-second]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - mlops
  - feature-store
---

# Offline Feature Store

## Định nghĩa

[[Offline Feature Store]] lưu feature lịch sử dung lượng lớn cho training, backfill, evaluation và phân tích.

## Cách hiểu bằng lời của tôi

Offline store tối ưu cho throughput và history, không tối ưu cho millisecond lookup. Lyft ghi batch feature vào Hive cho training; Snap dùng Apache Iceberg cho offline feature. Điều quan trọng là feature offline phải cùng định nghĩa/metadata với online feature.

## Liên kết

- [[Feature Store]]
- [[Online Feature Store]]
- [[Batch Processing]]
- [[Training-Serving Skew]]
- [[Data Warehouse]]
