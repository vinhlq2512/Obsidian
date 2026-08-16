---
type: concept
status: developing
sources:
  - "[[2026-08-13_a-detailed-guide-to-api-composition-techniques]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - api
  - frontend
  - system-design
---

# Backend for Frontend

## Định nghĩa

Backend for Frontend (BFF) là server-side layer riêng cho một client hoặc một nhóm frontend, dùng để chuyển domain APIs thành response shape phù hợp với UI đó.

## Cách hiểu bằng lời của tôi

BFF tồn tại vì mobile, web và third-party integration không đổi cùng nhịp. Một shared API dễ làm mọi client phải chờ nhau. BFF cho team client sở hữu shape response của mình, đổi lại phải chấp nhận thêm service và một ít duplication.

## Ranh giới nên giữ

- Có thể duplicate formatting, field selection và default phục vụ UI.
- Không nên duplicate pricing, authorization hoặc business rule lõi.
- Nếu BFF chỉ forward request không thêm giá trị, nó chỉ tăng deployment surface.
- Nếu BFF tích tụ business rule, nó trở thành system of record thứ hai.

## Liên kết

- [[API Composition]]
- [[API Contract]]
- [[API Versioning]]
- [[Backward Compatibility]]
- [[API Gateway]]
