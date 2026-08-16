---
type: concept
status: seed
sources:
  - "[[2026-05-28_must-know-failure-modes-in-distributed-systems]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - reliability
  - observability
---

# Gray Failure

## Định nghĩa

Gray failure là lỗi mà component vẫn có vẻ khỏe theo health check bề mặt nhưng không thực hiện đúng workload thật.

## Cách hiểu bằng lời của tôi

Gray failure nguy hiểm vì hệ thống tự tin sai. Ping còn trả lời, process còn chạy, dashboard có thể vẫn xanh, nhưng user path thật đang chậm, sai hoặc mất dữ liệu. Vì vậy health check chỉ kiểm tra "còn sống không" là chưa đủ.

## Cách phát hiện

- Synthetic transaction chạy qua đường xử lý thật.
- Peer-based detection để node xung quanh quan sát hành vi thực tế.
- End-to-end latency đo từ góc nhìn user thay vì chỉ đo bên trong service.

## Liên kết

- [[Observability]]
- [[Distributed Tracing]]
- [[Service Level Indicator]]
- [[Alerting]]
- [[Synthetic Monitoring]]
