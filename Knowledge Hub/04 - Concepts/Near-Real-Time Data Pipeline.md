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
  - data-pipeline
---

# Near-Real-Time Data Pipeline

## Định nghĩa

Near-Real-Time Data Pipeline (Đường ống dữ liệu cận thời gian thực) là kiến trúc xử lý dữ liệu hiện đại cho phép đồng bộ hóa dữ liệu từ các kho lưu trữ OLTP (Transactional DB) sang Data Lakehouse / Data Warehouse với độ trễ tính bằng phút (sub-5 minute latency) thay vì các batch job theo ngày (multi-day batch latency) truyền thống.

## Kiến trúc nâng cấp (Case Study Figma)

```text
OLTP Databases (PostgreSQL / MySQL)
-> Change Data Capture (Debezium / Kafka Connect)
-> Stream Ingestion Layer (Kafka / Pulsar)
-> Micro-batch Transformation & Open Table Format (Apache Iceberg / Delta Lake)
-> Analytical Data Warehouse (Snowflake / ClickHouse)
```

- **CDC Ingestion**: Đọc trực tiếp WAL/Binlog của database giao dịch mà không làm ảnh hưởng đến hiệu năng truy vấn OLTP.
- **Open Table Formats (Apache Iceberg)**: Cho phép append dữ liệu mới và thực hiện ACID transactions trực tiếp trên Object Storage (S3), hỗ trợ compaction và time travel.
- **Incremental Materialized Views**: Chỉ tính toán lại phần dữ liệu mới thay đổi thay vì tính lại toàn bộ bảng lớn.

## Trade-off

- Chi phí điện toán và lưu trữ cao hơn so với chạy một batch job duy nhất vào ban đêm.
- Phải giải quyết bài toán Small File Problem (quá nhiều file nhỏ được ghi liên tục lên Object Storage, cần cơ chế compaction định kỳ).

## Liên kết

- [[Change Data Capture]]
- [[Data Platform Processing Patterns]]
- [[Apache Iceberg]]
- [[Data Warehouse]]
