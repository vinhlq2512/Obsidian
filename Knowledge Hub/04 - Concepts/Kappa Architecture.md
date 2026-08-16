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
  - architecture
---

# Kappa Architecture

## Định nghĩa

[[Kappa Architecture]] dùng một đường streaming duy nhất cho cả xử lý mới và reprocessing, bằng cách replay event log khi cần dựng lại kết quả.

## Cách hiểu bằng lời của tôi

Kappa giảm drift vì chỉ có một code path. Nhưng nó đặt cược rằng event log đủ bền, đủ lâu và replay đủ khả thi. Nếu lịch sử quá lớn hoặc computation không hợp với stream, chi phí replay có thể rất cao.

## Trade-off

- Mạnh: một mental model và một logic xử lý.
- Mạnh: replay dùng lại cùng pipeline production.
- Yếu: reprocess lịch sử dài có thể chậm và đắt.
- Yếu: không phải mọi workload batch lớn đều biểu diễn tự nhiên dưới dạng stream.

## Liên kết

- [[Stream Processing]]
- [[Event Log]]
- [[Lambda Architecture]]
- [[Cost Optimization]]
- [[Data Freshness]]
