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

# Feature Store

## Định nghĩa

[[Feature Store]] là lớp quản lý, tính toán, lưu trữ, khám phá và phục vụ feature dùng cho model training và online inference.

## Cách hiểu bằng lời của tôi

Feature store tồn tại để model không phải sống trong hai thế giới rời nhau. Offline training cần feature lịch sử lớn; online serving cần lookup nhanh. Nếu metadata, logic hoặc freshness khác nhau, model sẽ train trên một phân phối và serve trên phân phối khác.

## Ba đường ghi phổ biến

- Batch: SQL/Spark job tạo feature theo lịch.
- Streaming: Flink/Kafka/Kinesis cập nhật feature real-time.
- Direct/API: service ghi feature online khi sự kiện xảy ra.

## Liên kết

- [[Offline Feature Store]]
- [[Online Feature Store]]
- [[Training-Serving Skew]]
- [[Feature Discovery]]
- [[Feature Store Cache]]
- [[Data Contract]]
