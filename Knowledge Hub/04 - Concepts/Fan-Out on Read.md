---
type: concept
status: seed
sources:
  - "[[2026-08-06_the-read-path-versus-the-write-path-strategies-and-technique]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - database
  - scalability
---

# Fan-Out on Read

## Định nghĩa

Fan-out on read là strategy lưu fact một lần và assemble response từ nhiều nguồn tại thời điểm đọc.

## Cách hiểu bằng lời của tôi

Fan-out on read giữ write path nhẹ, nhưng read path phải merge nhiều nguồn lúc user đang chờ. Nó hợp với account cực lớn nơi fan-out on write quá đắt, hoặc dữ liệu thay đổi nhanh mà precompute không đáng.

## Trade-off

- Write rẻ hơn.
- Read latency và query complexity cao hơn.
- Có thể kết hợp hybrid: user thường fan-out on write, celebrity/high-follower fan-out on read.

## Liên kết

- [[Fan-Out on Write]]
- [[Read Path]]
- [[Write Path]]
- [[API Aggregation]]
