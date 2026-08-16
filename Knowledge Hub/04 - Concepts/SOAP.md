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
  - protocol
---

# SOAP

## Định nghĩa

SOAP là messaging protocol dựa trên XML với cấu trúc message chặt chẽ, schema validation và cơ chế lỗi chuẩn.

## Cách hiểu bằng lời của tôi

SOAP nặng và verbose hơn REST/gRPC, nhưng phù hợp môi trường cần contract cứng, validation mạnh và security chuẩn hóa như một số hệ enterprise hoặc banking legacy.

## Thành phần message

- Envelope: gói toàn bộ message.
- Header: metadata như auth/security.
- Body: payload request/response.
- Fault: lỗi theo format chuẩn.

## Liên kết

- [[API Protocol]]
- [[API Contract]]
- [[API Security]]
