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

# Lambda Architecture

## Định nghĩa

[[Lambda Architecture]] chạy song song một batch layer chính xác chậm và một speed layer nhanh cho dữ liệu mới, rồi hợp nhất kết quả ở read path.

## Cách hiểu bằng lời của tôi

Lambda dùng batch làm nguồn sửa sai dài hạn cho streaming. Nó hợp lý khi cần cả dữ liệu gần real-time và khả năng reprocess lịch sử chắc chắn, nhưng đổi lại phải duy trì logic ở hai đường khác nhau.

## Trade-off

- Mạnh: batch layer có thể recompute toàn bộ lịch sử để sửa sai.
- Mạnh: speed layer phục vụ latency thấp.
- Yếu: business logic bị nhân đôi và có thể drift.
- Yếu: vận hành phức tạp vì hai stack xử lý phải được quan sát và debug cùng lúc.

## Liên kết

- [[Batch Processing]]
- [[Stream Processing]]
- [[Kappa Architecture]]
- [[Data Pipeline Validation]]
