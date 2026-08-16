---
type: concept
status: seed
sources:
  - "[[2025-01-28_aws-lambda-turns-10]]"
  - "[[2023-11-16_serverless-has-servers]]"
source_sections:
  - "[[2025-01-28_aws-lambda-turns-10]]"
  - "[[2023-11-16_serverless-has-servers]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - serverless
  - scaling
---

# Provisioned Concurrency

## Định nghĩa

[[Provisioned Concurrency]] giữ sẵn một số execution environment đã khởi tạo để serverless function có thể xử lý request với latency ổn định hơn.

## Cách hiểu bằng lời của tôi

Đây là cách mua lại một phần predictability mà scale-to-zero đánh đổi. Thay vì để mọi thứ ngủ rồi chịu cold start, ta trả tiền cho một lượng capacity warm cố định.

## Trade-off

- Giảm tail latency cho path quan trọng.
- Tăng chi phí vì vẫn trả cho capacity sẵn sàng.
- Cần capacity planning tối thiểu, dù vẫn đơn giản hơn tự vận hành server.

## Liên kết

- [[Serverless Cold Start]]
- [[Serverless Cost Model]]
- [[Capacity Planning]]
- [[Latency]]
