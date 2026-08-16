---
type: concept
status: seed
sources:
  - "[[2025-03-13_api-protocols-101-a-guide-to-choose-the-right-one]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - api
  - microservices
---

# gRPC

## Định nghĩa

gRPC là API protocol hiệu năng cao dùng Protocol Buffers làm schema/binary serialization và chạy trên HTTP/2.

## Cách hiểu bằng lời của tôi

gRPC hợp với service-to-service hơn public web API: payload nhỏ, parse nhanh, codegen rõ contract, HTTP/2 multiplexing và streaming tốt. Đổi lại browser support và debug thủ công kém hơn REST JSON.

## Khi dùng

- Microservices nội bộ cần latency thấp.
- Cần strict typing và generated client/server stubs.
- Cần unary, server streaming, client streaming hoặc bidirectional streaming.

## Liên kết

- [[API Protocol]]
- [[API Contract]]
- [[Microservices Design Patterns]]
- [[WebSocket]]
