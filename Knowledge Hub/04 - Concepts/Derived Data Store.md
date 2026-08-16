---
type: concept
status: seed
sources:
  - "[[2025-01-07_how-airbnb-built-a-key-value-store-for-petabytes-of-data]]"
  - "[[2025-04-21_how-airbnb-powers-personalization-with-1m-events-per-second]]"
source_sections:
  - "[[2025-01-07_how-airbnb-built-a-key-value-store-for-petabytes-of-data]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - data
  - system-design
---

# Derived Data Store

## Định nghĩa

[[Derived Data Store]] là storage chuyên phục vụ dữ liệu đã được tính toán từ raw data, batch jobs hoặc realtime event streams, thường dùng cho personalization, ranking, feature serving hoặc read-heavy services.

## Cách hiểu bằng lời của tôi

Raw data không phải lúc nào cũng là dạng tốt nhất để phục vụ request online. Derived data store giữ phiên bản đã tính sẵn để service đọc nhanh. Nó giống một read model lớn: được build từ Spark/Kafka/data warehouse, nhưng tối ưu cho lookup latency thấp trong production.

## Cơ chế thường gặp

```text
raw events / warehouse
-> batch hoặc stream processing
-> derived records theo key
-> key-value/read store
-> online service đọc với latency thấp
```

## Trade-off

- Đổi freshness/consistency lấy latency và throughput.
- Cần pipeline publish, bulk load, incremental update và rollback rõ.
- Nếu phải merge online từ nhiều store, read latency có thể tăng mạnh.
- Storage engine phải cân bằng compaction, read availability và update volume.

## Liên kết

- [[Distributed Key-Value Store]]
- [[Materialized View]]
- [[CQRS]]
- [[Event Stream]]
- [[Apache Kafka]]
