---
type: concept
status: seed
sources:
  - "[[2023-11-16_serverless-has-servers]]"
  - "[[2025-01-28_aws-lambda-turns-10]]"
  - "[[2026-02-17_how-cloudflare-eliminates-cold-starts-for-serverless-workers]]"
source_sections:
  - "[[2023-11-16_serverless-has-servers]]"
  - "[[2025-01-28_aws-lambda-turns-10]]"
  - "[[2026-02-17_how-cloudflare-eliminates-cold-starts-for-serverless-workers]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - serverless
  - latency
---

# Serverless Cold Start

## Định nghĩa

[[Serverless Cold Start]] là độ trễ phát sinh khi platform phải chuẩn bị execution environment, tải code, compile/initialize runtime rồi mới gọi handler cho request đầu tiên.

## Cách hiểu bằng lời của tôi

Cold start là mặt trái của scale-to-zero. Khi function ít traffic bị eviction để tiết kiệm tài nguyên, request kế tiếp phải trả chi phí khởi động. Với user-facing path, vấn đề không chỉ là trung bình latency mà là tail latency khó đoán.

## Các pha thường gặp

- Provision hoặc chọn môi trường chạy.
- Download code/dependency.
- Khởi tạo runtime và top-level initialization.
- Invoke handler.

## Cách giảm

- Pre-warm trong lúc TLS handshake nếu đủ thời gian.
- Dùng snapshot runtime như [[Lambda SnapStart]].
- Dùng [[Provisioned Concurrency]] cho path cần latency ổn định.
- Giảm số cold start bằng [[Serverless Worker Sharding]].

## Liên kết

- [[Function as a Service]]
- [[Latency]]
- [[Lambda Execution Environment]]
- [[Lambda SnapStart]]
- [[Provisioned Concurrency]]
- [[Serverless Worker Sharding]]
