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

# Fan-Out on Write

## Định nghĩa

Fan-out on write là strategy sao chép hoặc precompute dữ liệu tới nhiều read targets ngay khi write xảy ra.

## Cách hiểu bằng lời của tôi

Timeline là ví dụ rõ: khi account thường đăng bài, hệ thống copy post vào timeline của từng follower để sau này đọc cực rẻ. Nhưng với account có hàng triệu follower, write path có thể nổ vì một write biến thành hàng triệu write.

## Khi hợp

- Nhiều read trên mỗi write.
- Số target cho mỗi write nhỏ hoặc có giới hạn.
- Fresh read latency quan trọng hơn write cost.

## Liên kết

- [[Fan-Out on Read]]
- [[Write Path]]
- [[Read Path]]
- [[CQRS]]
