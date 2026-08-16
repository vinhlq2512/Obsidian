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
  - distributed-systems
---

# Metastable Failure

## Định nghĩa

Metastable failure là trạng thái hệ thống tiếp tục hỏng hoặc degraded sau khi trigger ban đầu đã biến mất, vì behavior nội tại của hệ thống tự giữ nó trong trạng thái xấu.

## Cách hiểu bằng lời của tôi

Một traffic spike hoặc database chậm có thể chỉ là mồi lửa. Khi request timeout, client retry, retry làm tải tăng, tải tăng làm timeout tiếp tục. Ngay cả khi mồi lửa đã tắt, feedback loop vẫn giữ hệ thống mắc kẹt.

## Dấu hiệu

- Không tìm thấy "root cause" hiện tại rõ ràng vì trigger gốc đã qua.
- Tải do retry/queue/reconnect/autoscale reaction cao hơn tải thật.
- Hệ thống chỉ hồi phục khi cắt tải, reset queue hoặc phá feedback loop.

## Liên kết

- [[Retry Storm]]
- [[Cascading Failure]]
- [[Backpressure]]
- [[Load Shedding]]
- [[Circuit Breaker]]
