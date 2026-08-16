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

# Watermark

## Định nghĩa

[[Watermark]] là ước lượng của streaming system rằng nó có lẽ đã thấy toàn bộ event đến một mốc event time nhất định.

## Cách hiểu bằng lời của tôi

Watermark không phải sự thật tuyệt đối; nó là một lời cá cược có kiểm soát. Nếu chờ lâu, kết quả đúng hơn nhưng chậm hơn. Nếu đóng window sớm, latency tốt hơn nhưng phải chấp nhận late data hoặc correction.

## Vai trò

- Báo cho window khi nào có thể emit kết quả.
- Biến stream vô hạn thành các aggregate hữu hạn có deadline.
- Là điểm điều chỉnh trade-off giữa completeness và latency.

## Liên kết

- [[Stream Processing]]
- [[Data Processing Window]]
- [[Late Data]]
- [[Event Time and Processing Time]]
- [[Data Freshness]]
