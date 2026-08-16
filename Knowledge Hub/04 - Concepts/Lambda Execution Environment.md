---
type: concept
status: seed
sources:
  - "[[2023-11-16_serverless-has-servers]]"
  - "[[2025-01-28_aws-lambda-turns-10]]"
source_sections:
  - "[[2023-11-16_serverless-has-servers]]"
  - "[[2025-01-28_aws-lambda-turns-10]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - serverless
  - aws
---

# Lambda Execution Environment

## Định nghĩa

[[Lambda Execution Environment]] là môi trường cô lập nơi một Lambda function được khởi tạo và invoke, gồm runtime, code package, dependency và tài nguyên CPU/memory tương ứng.

## Cách hiểu bằng lời của tôi

Lambda không chạy function "trên không khí". Frontend/worker manager phải nhận request, placement service chọn worker, rồi môi trường chạy được init hoặc reuse. Nếu không có môi trường warm, request đi qua cold start.

## Luồng đồng bộ

```text
frontend nhận invocation
-> worker manager hỏi placement service
-> worker init code/runtime nếu cần
-> frontend invoke function
-> trả response
```

## Liên kết

- [[Serverless Architecture]]
- [[Function as a Service]]
- [[Firecracker MicroVM]]
- [[Serverless Cold Start]]
- [[Provisioned Concurrency]]
