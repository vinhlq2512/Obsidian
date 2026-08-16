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
  - latency
---

# Lambda SnapStart

## Định nghĩa

[[Lambda SnapStart]] là kỹ thuật pre-initialize runtime rồi lưu snapshot của execution environment để invocation sau có thể restore nhanh hơn thay vì init từ đầu.

## Cách hiểu bằng lời của tôi

SnapStart giống như chụp lại function sau đoạn khởi động nặng. Khi request đến, platform restore trạng thái đã sẵn sàng thay vì tải code và chạy init lại từ zero.

## Khi hữu ích

- Runtime có startup nặng.
- Function user-facing nhạy với latency.
- Init code ổn định và an toàn khi được snapshot/restore.

## Liên kết

- [[Serverless Cold Start]]
- [[Lambda Execution Environment]]
- [[Latency]]
- [[Cost Optimization]]
