---
type: concept
status: understood
sources:
  - "[[2026-04-11_ep210-monolithic-vs-microservices-vs-serverless]]"
  - "[[2025-01-28_aws-lambda-turns-10]]"
  - "[[2023-11-16_serverless-has-servers]]"
source_sections:
  - "[[2026-04-11_ep210-monolithic-vs-microservices-vs-serverless]]"
  - "[[2025-01-28_aws-lambda-turns-10]]"
  - "[[2023-11-16_serverless-has-servers]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - cloud
  - system-design
---

# Serverless Architecture

## Định nghĩa

Serverless Architecture là mô hình xây dựng hệ thống quanh function hoặc managed service được kích hoạt bởi event, nơi cloud provider vận hành server, scaling và phần lớn runtime infrastructure.

## Cách hiểu bằng lời của tôi

"Serverless" không có nghĩa là không có server; nó nghĩa là team không quản lý server trực tiếp. Đổi lại, team nhận được scaling tự động và pay-per-use, nhưng phải chấp nhận cold start, khó debug flow stateless rải rác và lock-in vào runtime/cloud provider.

Nhìn từ bài AWS Lambda và Cloudflare Workers, serverless là một lớp platform gồm placement, runtime isolation, event routing, billing, observability và cơ chế giữ latency ổn định. Phần "không phải vận hành server" của developer chỉ tồn tại vì provider đang vận hành một hệ thống phân tán phức tạp phía sau.

## Khi dùng

- Background jobs, notifications, webhook processing.
- Workload event-driven, bursty, không cần process sống lâu.
- Team muốn giảm vận hành server cho phần phụ trợ.

## Liên kết

- [[Function as a Service]]
- [[Backend as a Service]]
- [[Serverless Cold Start]]
- [[Serverless Cost Model]]
- [[Lambda Execution Environment]]
- [[Firecracker MicroVM]]
- [[Event Stream]]
- [[Workflow Orchestration]]
- [[Cost Optimization]]
- cloud lock-in
