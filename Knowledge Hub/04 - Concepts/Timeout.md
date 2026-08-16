---
type: concept
status: developing
sources:
  - "[[2026-05-28_must-know-failure-modes-in-distributed-systems]]"
  - "[[2025-01-23_top-strategies-to-reduce-latency]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - reliability
  - latency
---

# Timeout

## Định nghĩa

Timeout là giới hạn thời gian chờ một operation trước khi caller coi operation đó là không còn đáng chờ nữa.

## Cách hiểu bằng lời của tôi

Timeout không chứng minh request đã thất bại. Nó chỉ nói caller không nhận được kết quả trong ngân sách thời gian. Trong hệ phân tán, request có thể chưa tới server, server có thể crash, response có thể bị mất, hoặc server vẫn đang xử lý và sắp trả lời.

## Vì sao quan trọng

- Timeout quá dài giữ connection/thread lâu và làm queue phình ra.
- Timeout quá ngắn tạo false failure, kích hoạt retry/failover không cần thiết.
- Timeout ở nhiều tầng phải được thiết kế theo budget chung; nếu tầng ngoài hết thời gian trước tầng trong, hệ thống dễ sinh work vô ích.

## Liên kết

- [[Partial Failure]]
- [[Retry Pattern]]
- [[Retry Storm]]
- [[Circuit Breaker]]
- [[Latency]]
