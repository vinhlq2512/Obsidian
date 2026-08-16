---
type: concept
status: understood
sources:
  - "[[2023-09-21_a-crash-course-in-redis]]"
source_sections:
  - "[[2023-09-21_a-crash-course-in-redis]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - system-design
  - caching
---

# Redis Event Loop

## Định nghĩa

Redis Event Loop là mô hình xử lý event dùng I/O multiplexing để một thread theo dõi nhiều socket, nhận event và dispatch tới handler tương ứng.

## Cách hiểu bằng lời của tôi

Redis tránh nhiều chi phí context switch bằng cách giữ thao tác đọc/ghi dữ liệu trên một execution path tuần tự. Vì workload thường memory/network-bound hơn CPU-bound, mô hình này đủ nhanh cho nhiều lệnh O(1), O(log N) và giảm race condition trên data structure.

## Cơ chế

- Kernel theo dõi nhiều connection bằng cơ chế kiểu `epoll`.
- Event vào queue, Redis dispatch accept/read/write event tới handler.
- Các tác vụ như persistence và replication có thể dùng thread/process khác; critical path data mutation vẫn được tuần tự hóa.

## Liên kết

- [[Redis]]
- [[Latency]]
- [[Backpressure]]
- event loop
