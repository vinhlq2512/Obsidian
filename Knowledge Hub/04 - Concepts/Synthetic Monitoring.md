---
type: concept
status: seed
sources:
  - "[[2026-05-28_must-know-failure-modes-in-distributed-systems]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - observability
  - reliability
---

# Synthetic Monitoring

## Định nghĩa

Synthetic monitoring là cách chủ động chạy các giao dịch mô phỏng user hoặc workload thật để kiểm tra hệ thống, thay vì chỉ chờ traffic thật phát hiện lỗi.

## Cách hiểu bằng lời của tôi

Health check kiểu ping chỉ trả lời câu hỏi "process còn sống không". Synthetic monitoring hỏi câu khó hơn: "đường user quan trọng có thật sự chạy được không?". Vì vậy nó đặc biệt hữu ích với [[Gray Failure]].

## Khi dùng

- Kiểm tra login, checkout, search, payment hoặc các critical path khác.
- Đo end-to-end latency từ góc nhìn gần user.
- Phát hiện service vẫn alive nhưng không làm đúng việc.

## Liên kết

- [[Observability]]
- [[Distributed Tracing]]
- [[Service Level Indicator]]
- [[Alerting]]
- [[Gray Failure]]
