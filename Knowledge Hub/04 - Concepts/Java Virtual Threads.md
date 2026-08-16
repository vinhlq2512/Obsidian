---
type: concept
status: seed
sources:
  - "[[2025-06-03_how-netflix-runs-on-java]]"
source_sections:
  - "[[2025-06-03_how-netflix-runs-on-java]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - java
  - concurrency
---

# Java Virtual Threads

## Định nghĩa

[[Java Virtual Threads]] là lightweight thread do JVM schedule, cho phép viết blocking code theo phong cách quen thuộc nhưng scale tốt hơn mô hình OS thread-per-request.

## Cách hiểu bằng lời của tôi

Virtual thread làm cho nhiều tác vụ I/O blocking không còn cần một platform thread riêng trong suốt thời gian chờ. Với backend fan-out nhiều RPC, developer có thể giữ code tuần tự/dễ đọc hơn thay vì chuyển hết sang callback/reactive chain.

## Khi hữu ích

- Resolver hoặc handler phải gọi nhiều service/datastore blocking.
- Muốn parallelize I/O mà không tự quản lý nhiều thread pool.
- Muốn giảm complexity so với reactive programming cho request/response backend thông thường.
- Framework có thể bật support ở tầng platform để team app không phải tự viết concurrency plumbing.

## Failure mode cần nhớ

Virtual threads không tự loại bỏ mọi lỗi concurrency. Nguồn Netflix nhấn mạnh vấn đề thread pinning: khi virtual thread bị pin vào platform thread trong synchronized block hoặc đoạn blocking đặc biệt, nhiều virtual thread bị pin có thể làm cạn platform thread và gây deadlock/latency.

## Liên kết

- [[Runtime Platform Migration]]
- [[Latency]]
- [[Timeout]]
- [[Backpressure]]
- [[GraphQL Federation]]
