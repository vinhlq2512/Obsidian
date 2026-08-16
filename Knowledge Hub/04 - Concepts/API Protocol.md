---
type: concept
status: developing
sources:
  - "[[2025-03-13_api-protocols-101-a-guide-to-choose-the-right-one]]"
  - "[[2025-05-24_ep164-jwt-simply-explained]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - api
  - system-design
---

# API Protocol

## Định nghĩa

API protocol là tập quy tắc định nghĩa cách các hệ thống gửi request, format response, xử lý lỗi, bảo mật và trao đổi dữ liệu qua mạng.

## Cách hiểu bằng lời của tôi

Chọn protocol là chọn trade-off vận hành: REST dễ dùng và cache tốt, GraphQL linh hoạt cho frontend, gRPC hiệu quả cho service nội bộ, WebSocket/SSE xử lý realtime, Webhook phù hợp event server-to-server.

## Câu hỏi chọn protocol

- Dữ liệu là CRUD resource hay workflow/event stream?
- Client là browser/public developer hay service nội bộ?
- Có cần realtime một chiều hay hai chiều?
- Cần strict schema/codegen hay human-readable JSON?
- Caching HTTP có quan trọng không?
- Security model và tooling team đã quen tới đâu?

## Liên kết

- [[REST API]]
- [[GraphQL]]
- [[gRPC]]
- [[SOAP]]
- [[WebSocket]]
- [[Server-Sent Events]]
- [[Webhook]]
