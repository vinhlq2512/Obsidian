---
type: concept
status: seed
sources:
  - "[[2025-10-23_api-gateways-101-the-core-of-modern-api-management-security]]"
  - "[[2026-01-29_how-to-scale-an-api]]"
source_sections:
  - "[[2026-01-29_how-to-scale-an-api]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - reliability
  - api
---

# Throttling

## Định nghĩa

[[Throttling]] là cơ chế làm chậm, trì hoãn hoặc giới hạn tốc độ xử lý request để bảo vệ hệ thống khi load vượt ngưỡng mong muốn.

## Cách hiểu bằng lời của tôi

Rate limiting thường trả lời "client này có vượt ngân sách không?". Throttling rộng hơn: hệ thống có thể delay, queue, giảm tốc hoặc reject một phần traffic để backend không sập. Nó là van điều áp nằm ở gateway, queue, worker pool hoặc client SDK.

## Khi dùng

- Client gửi request quá nhanh.
- Downstream đang yếu và cần giảm pressure.
- Muốn bảo vệ database/message queue khỏi spike.
- Muốn giữ fairness giữa tenant hoặc API key.

## Liên kết

- [[Rate Limiting]]
- [[Backpressure]]
- [[Load Shedding]]
- [[API Gateway]]
- [[Retry Storm]]
