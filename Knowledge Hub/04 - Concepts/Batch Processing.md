---
type: concept
status: seed
sources:
  - "[[2026-07-09_streaming-vs-batch-two-philosophies-of-data-processing]]"
source_sections:
  - "[[2026-07-09_streaming-vs-batch-two-philosophies-of-data-processing]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - data-engineering
---

# Batch Processing

## Định nghĩa

[[Batch Processing]] xử lý dữ liệu theo một tập hữu hạn có ranh giới rõ, ví dụ file đã đóng, ngày đã kết thúc hoặc partition đã hoàn tất.

## Cách hiểu bằng lời của tôi

Batch đổi latency lấy sự đơn giản. Khi dữ liệu có điểm kết thúc, hệ thống có thể chờ đủ, tính lại toàn bộ hoặc tính incremental, rồi xuất ra kết quả ổn định hơn streaming.

## Biến thể

- Full load: đọc lại toàn bộ dataset; dễ đúng nhưng đắt khi dữ liệu lớn.
- Incremental load: chỉ xử lý phần thay đổi; rẻ hơn nhưng cần xử lý correction.
- Big-window aggregation: tạo rollup theo ngày/tháng; truy vấn nhanh nhưng freshness thấp.

## Liên kết

- [[Micro-Batch Processing]]
- [[Stream Processing]]
- [[Data Freshness]]
- [[Cost Optimization]]
