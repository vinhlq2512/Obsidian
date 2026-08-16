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

# Data Processing Window

## Định nghĩa

[[Data Processing Window]] là cách cắt một stream vô hạn thành các lát hữu hạn để aggregate như count, sum, average hoặc session metrics.

## Cách hiểu bằng lời của tôi

Window là quyết định "mình đang hỏi câu hỏi theo lát thời gian nào". Cùng một event stream, tumbling, sliding và session window có thể tạo ra ba sự thật khác nhau vì chúng gom event theo ranh giới khác nhau.

## Các kiểu chính

- Tumbling window: fixed size, không overlap; đơn giản và rẻ nhưng nhạy với ranh giới.
- Sliding window: fixed size, có overlap; mượt cho trend nhưng tăng compute/state.
- Session window: đóng theo khoảng im lặng; hợp với hành vi user nhưng khó vận hành hơn.

## Liên kết

- [[Stream Processing]]
- [[Event Time and Processing Time]]
- [[Watermark]]
- [[Late Data]]
- [[Data Freshness]]
