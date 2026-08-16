---
type: concept
status: seed
sources:
  - "[[2023-11-16_serverless-has-servers]]"
source_sections:
  - "[[2023-11-16_serverless-has-servers]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - serverless
  - cloud
---

# Backend as a Service

## Định nghĩa

[[Backend as a Service]] (BaaS) là nhóm managed service cung cấp backend capability qua API, như auth, database, storage, remote config hoặc analytics.

## Cách hiểu bằng lời của tôi

FaaS xử lý logic stateless, còn BaaS giữ các phần cần trạng thái và vận hành lâu dài. Một app serverless thực tế thường là tổ hợp function nhỏ cộng với database, queue, storage và auth do provider quản lý.

## Trade-off

- Tăng tốc phát triển vì không phải tự vận hành backend phổ biến.
- Giảm khả năng kiểm soát implementation và portability.
- Debug khó hơn vì flow đi qua nhiều managed service.

## Liên kết

- [[Function as a Service]]
- [[Serverless Architecture]]
- [[Backend for Frontend]]
- [[Authentication]]
- [[Object Storage]]
