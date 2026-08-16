---
type: concept
status: seed
sources:
  - "[[2023-11-16_serverless-has-servers]]"
  - "[[2025-01-28_aws-lambda-turns-10]]"
  - "[[2024-11-01_baselime-s-big-move-from-aws-to-cloudflare-faster-simpler-ch]]"
source_sections:
  - "[[2023-11-16_serverless-has-servers]]"
  - "[[2025-01-28_aws-lambda-turns-10]]"
  - "[[2024-11-01_baselime-s-big-move-from-aws-to-cloudflare-faster-simpler-ch]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - serverless
  - cost
---

# Serverless Cost Model

## Định nghĩa

[[Serverless Cost Model]] tính chi phí theo invocation, duration, memory/CPU allocation và các dịch vụ managed đi kèm thay vì trả trước cho server chạy liên tục.

## Cách hiểu bằng lời của tôi

Serverless rẻ khi workload bursty hoặc idle nhiều, vì không phải trả cho capacity nằm im. Nhưng nếu function chạy liên tục, gọi quá nhiều service phụ, hoặc cần provisioned concurrency lớn, hóa đơn có thể chuyển từ compute sang request, network, analytics, storage và observability.

## Cost driver

- Số lần invocation.
- Thời lượng mỗi invocation.
- Memory allocation kéo theo CPU.
- Network, queue, storage, analytics engine và log volume.
- Capacity warm như provisioned concurrency.

## Liên kết

- [[Cost Optimization]]
- [[Function as a Service]]
- [[Provisioned Concurrency]]
- [[Capacity Planning]]
- [[Observability]]
