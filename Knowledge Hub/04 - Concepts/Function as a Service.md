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
  - cloud
---

# Function as a Service

## Định nghĩa

[[Function as a Service]] (FaaS) là mô hình deploy function stateless được kích hoạt bởi event, trong đó cloud provider quản lý runtime, placement, scaling và lifecycle thực thi.

## Cách hiểu bằng lời của tôi

FaaS là "đưa code handler cho platform". Developer không giữ process chạy lâu; mỗi invocation đi qua platform, được đặt vào execution environment phù hợp, chạy logic rồi trả kết quả. State lâu dài phải nằm ở service khác.

## Cơ chế

```text
event trigger
-> platform chọn/khởi tạo execution environment
-> gọi handler
-> ghi side effect vào BaaS/database/queue
-> scale down hoặc giữ warm tùy traffic
```

## Liên kết

- [[Serverless Architecture]]
- [[Backend as a Service]]
- [[Serverless Cold Start]]
- [[Lambda Execution Environment]]
- [[Event Stream]]
