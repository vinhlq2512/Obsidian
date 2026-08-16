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

# Late Data

## Định nghĩa

[[Late Data]] là event đến sau khi window của nó đã được hệ thống xem là đủ dữ liệu và đã emit kết quả.

## Cách hiểu bằng lời của tôi

Late data là chi phí tự nhiên của việc không thể chờ mãi. Nó không nhất thiết là bug; nó là hậu quả của network delay, retry, thiết bị offline hoặc producer bị nghẽn.

## Cách xử lý

- Drop: nhanh và đơn giản, chấp nhận sai số nhỏ.
- Allowed lateness: giữ window mở thêm một khoảng để update kết quả.
- Correction path: gửi late event sang luồng sửa sau, phù hợp khi correctness quan trọng.

## Liên kết

- [[Stream Processing]]
- [[Watermark]]
- [[Data Processing Window]]
- [[Event Time and Processing Time]]
- [[Data Pipeline Validation]]
