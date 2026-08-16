---
type: concept
status: seed
sources:
  - "[[2026-05-21_a-guide-to-async-patterns-in-api-design]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - api
  - async
---

# Short Polling

## Định nghĩa

Short polling là pattern client hỏi server theo lịch cố định để kiểm tra có dữ liệu/event mới không.

## Cách hiểu bằng lời của tôi

Đây là cách đơn giản nhất: cứ vài giây hỏi một lần. Nhiều request sẽ rỗng, nhưng operational model rất dễ hiểu vì mỗi lần hỏi vẫn là HTTP request bình thường.

## Khi dùng

- Event tần suất thấp.
- Scale còn modest.
- Muốn tránh vận hành connection dài hoặc realtime infrastructure.

## Liên kết

- [[Async API Pattern]]
- [[Long Polling]]
- [[Server-Sent Events]]
- [[Latency]]
