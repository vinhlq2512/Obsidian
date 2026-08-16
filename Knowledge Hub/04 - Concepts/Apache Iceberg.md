---
type: concept
status: understood
sources:
  - "[[2026-05-12_how-figma-upgraded-data-pipeline-from-multi-day-latency-to-r]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - system-design
  - data-engineering
  - open-table-format
---

# Apache Iceberg

## Định nghĩa

Apache Iceberg là định dạng bảng mở (Open Table Format) hiệu năng cao dành cho các kho dữ liệu Data Lake khổng lồ (Petabyte-scale). Iceberg mang lại tính năng ACID transactions, Schema Evolution, Partition Evolution và Time Travel trực tiếp trên các hệ thống lưu trữ Object Storage như Amazon S3 hay Google Cloud Storage.

## Cơ chế & Điểm sáng

```text
Apache Iceberg Architecture
- Iceberg Catalog (Tracks Current Metadata Pointer)
- Metadata File (Schema, Partition Spec, Snapshot Tree)
- Manifest List (Tracks Manifest Files for a Snapshot)
- Manifest Files (Tracks Data Files + Column-Level Min/Max Stats)
- Data Files (Parquet / ORC)
```

- **Hidden Partitioning**: Người dùng không cần quan tâm đến cách phân vùng vật lý (như `year/month/day`), Iceberg tự động xử lý và tối ưu hóa truy vấn mà không làm sai kết quả.
- **ACID Transactions**: Hỗ trợ nhiều công cụ ghi/đọc song song (Spark, Flink, Trino, Snowflake) mà không gây bẩn dữ liệu (dirty reads).
- **Time Travel**: Cho phép truy vấn lại snapshot dữ liệu chính xác tại bất kỳ mốc thời gian nào trong quá khứ.

## Trade-off

- Đòi hỏi quy trình bảo trì định kỳ (Compaction job và Snapshot expiration) để tránh phồng to dung lượng file metadata trên Object Storage.

## Liên kết

- [[Near-Real-Time Data Pipeline]]
- [[Data Lake]]
- [[Data Warehouse]]
- [[Object Storage]]
