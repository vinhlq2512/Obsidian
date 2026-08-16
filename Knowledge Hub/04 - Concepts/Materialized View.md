---
type: concept
status: developing
sources:
  - "[[2026-08-06_the-read-path-versus-the-write-path-strategies-and-technique]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - database
  - read-model
---

# Materialized View

## Định nghĩa

Materialized view là kết quả query được lưu lại thành bảng/read model và refresh theo cơ chế hoặc lịch định trước.

## Cách hiểu bằng lời của tôi

Materialized view trả trước chi phí query để read rẻ hơn. Khác cache ở chỗ staleness window thường được quyết định bởi refresh strategy, không chỉ tình cờ theo TTL hoặc traffic.

## Refresh strategy

- Full refresh: đơn giản nhưng tốn, làm refresh interval dài.
- Incremental refresh: rẻ hơn nhưng khó đúng vì phải xử lý delete, out-of-order update và partial failure.

## Khi không hợp

- Refresh cost gần bằng query gốc.
- Freshness yêu cầu ngắn hơn thời gian refresh.
- Logic thay đổi quá nhanh khiến read model khó giữ đúng.

## Liên kết

- [[Read Path]]
- [[Staleness]]
- [[CQRS]]
- [[Change Data Capture]]
