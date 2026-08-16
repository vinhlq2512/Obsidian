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
  - virtualization
---

# Firecracker MicroVM

## Định nghĩa

[[Firecracker MicroVM]] là lightweight virtual machine dùng để chạy serverless/container workload với isolation mạnh hơn process/container thuần nhưng khởi động nhanh hơn VM truyền thống.

## Cách hiểu bằng lời của tôi

Firecracker là câu trả lời cho bài toán multi-tenant serverless: provider muốn chạy nhiều tenant trên cùng hạ tầng, nhưng không muốn đánh đổi quá nhiều giữa security isolation và startup latency.

## Vai trò trong Lambda

- Tạo môi trường cô lập cho function.
- Giảm overhead so với cấp cả EC2 instance cho từng tenant/function.
- Hỗ trợ cold start nhanh hơn nhờ microVM nhẹ.

## Liên kết

- [[Lambda Execution Environment]]
- [[Virtualization]]
- [[Containerization]]
- [[Serverless Cold Start]]
- [[Least Privilege]]
