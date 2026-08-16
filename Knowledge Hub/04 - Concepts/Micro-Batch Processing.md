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
  - streaming
---

# Micro-Batch Processing

## Định nghĩa

[[Micro-Batch Processing]] chia luồng dữ liệu liên tục thành các khoảng nhỏ rồi xử lý từng khoảng như một batch mini.

## Cách hiểu bằng lời của tôi

Micro-batch là điểm giữa thực dụng: vẫn giữ mental model "chunk hữu hạn chạy xong" của batch, nhưng giảm độ trễ từ ngày/giờ xuống phút/giây. Nó phù hợp khi business nói "real-time" nhưng thực ra chấp nhận một chút lag.

## Trade-off

- Dễ vận hành hơn true streaming vì mỗi chunk có ranh giới.
- Có freshness tốt hơn batch lịch dài.
- Latency tối thiểu bị chặn bởi interval của micro-batch.
- Không phù hợp nếu cần phản ứng sub-second.

## Liên kết

- [[Batch Processing]]
- [[Stream Processing]]
- [[Data Freshness]]
- [[Event Stream]]
