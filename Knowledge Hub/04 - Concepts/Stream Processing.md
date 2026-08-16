---
type: concept
status: seed
sources:
  - "[[2026-07-09_streaming-vs-batch-two-philosophies-of-data-processing]]"
  - "[[2025-11-11_how-spotify-built-its-data-platform-to-understand-1-4-trilli]]"
source_sections:
  - "[[2026-07-09_streaming-vs-batch-two-philosophies-of-data-processing]]"
  - "[[2025-11-11_how-spotify-built-its-data-platform-to-understand-1-4-trilli]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - data-engineering
  - streaming
---

# Stream Processing

## Định nghĩa

[[Stream Processing]] xử lý event khi chúng đến trên một luồng dữ liệu không có điểm kết thúc tự nhiên.

## Cách hiểu bằng lời của tôi

Streaming không có "đợi đủ rồi tính". Nó phải trả lời bằng dữ liệu chưa chắc đã hoàn chỉnh, vì event có thể đến trễ hoặc sai thứ tự. Đổi lại, hệ thống có thể tạo dashboard, fraud decision, personalization hoặc alert gần real-time.

## Cơ chế cần đi kèm

- Phân biệt [[Event Time and Processing Time]].
- Cắt stream bằng [[Data Processing Window]].
- Đóng window bằng [[Watermark]].
- Quyết định xử lý [[Late Data]].
- Làm side effect idempotent nếu muốn hiệu ứng exactly-once.

## Liên kết

- [[Event Stream]]
- [[Apache Kafka]]
- [[Delivery Semantics]]
- [[Batch Processing]]
- [[Micro-Batch Processing]]
- [[Data Freshness]]
