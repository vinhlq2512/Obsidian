---
type: concept
status: seed
sources:
  - "[[2025-01-28_aws-lambda-turns-10]]"
source_sections:
  - "[[2025-01-28_aws-lambda-turns-10]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - serverless
  - deployment
---

# Lambda Layer

## Định nghĩa

[[Lambda Layer]] là gói dependency hoặc file dùng chung có thể attach vào nhiều Lambda function để không phải đóng gói lặp lại trong từng function artifact.

## Cách hiểu bằng lời của tôi

Layer giúp tách code business khỏi thư viện dùng chung. Nó tiện cho utility, monitoring agent hoặc dependency lớn, nhưng cũng tạo thêm một version boundary cần quản lý trong deployment.

## Liên kết

- [[Lambda Execution Environment]]
- [[Deployment Pipeline]]
- [[Function as a Service]]
- [[Backward Compatibility]]
