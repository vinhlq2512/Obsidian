---
type: concept
status: seed
sources:
  - "[[2026-05-28_must-know-failure-modes-in-distributed-systems]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - distributed-systems
  - reliability
---

# Partial Failure

## Định nghĩa

Partial failure là trạng thái trong đó một phần của hệ phân tán lỗi, chậm hoặc không quan sát được, trong khi các phần khác vẫn tiếp tục chạy.

## Cách hiểu bằng lời của tôi

Trên một máy đơn, lỗi thường khá rõ: process còn sống hoặc đã chết. Trong hệ phân tán, caller chỉ thấy một tín hiệu mơ hồ như timeout, còn trạng thái thật của request có thể khác nhau. Chính sự mơ hồ đó làm retry, idempotency và consistency trở nên quan trọng.

## Ví dụ từ ByteByteGo

Một request timeout có thể nghĩa là:

- request chưa bao giờ tới server;
- server crash trước khi xử lý;
- server xử lý xong nhưng response bị mất;
- server vẫn đang xử lý và sắp trả lời.

## Liên kết

- [[Timeout]]
- [[Idempotency Key]]
- [[Retry Pattern]]
- [[Distributed Systems]]
- [[CAP and PACELC]]
