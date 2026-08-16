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

# Event Time and Processing Time

## Định nghĩa

[[Event Time and Processing Time]] phân biệt thời điểm sự kiện thật sự xảy ra với thời điểm hệ thống xử lý nhận được event đó.

## Cách hiểu bằng lời của tôi

Trong streaming, dữ liệu không luôn đến đúng thứ tự. Một payment có thể xảy ra lúc 10:01 nhưng đến pipeline lúc 10:05. Nếu aggregate theo processing time, kết quả nhanh hơn nhưng có thể sai theo thế giới thật; nếu aggregate theo event time, cần cơ chế chờ và sửa late data.

## Hệ quả thiết kế

- Window theo event time phản ánh business timeline tốt hơn.
- Watermark là tín hiệu để hệ thống đoán đã thấy đủ event cho một mốc thời gian.
- Chênh lệch giữa hai loại thời gian càng lớn thì trade-off freshness/correctness càng khó.

## Liên kết

- [[Stream Processing]]
- [[Data Processing Window]]
- [[Watermark]]
- [[Late Data]]
- [[Data Freshness]]
