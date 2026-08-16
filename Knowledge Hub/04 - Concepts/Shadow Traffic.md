---
type: concept
status: understood
sources:
  - "[[2026-06-11_must-know-deployment-strategies-from-big-bang-to-progressive]]"
source_sections:
  - "[[2026-06-11_must-know-deployment-strategies-from-big-bang-to-progressive]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - deployment
  - testing
---

# Shadow Traffic

## Định nghĩa

Shadow Traffic là kỹ thuật duplicate request production sang service mới để service mới xử lý dưới tải thật nhưng response bị bỏ đi, không ảnh hưởng user.

## Cách hiểu bằng lời của tôi

Shadow traffic kiểm tra cả service mới dưới traffic thật, khác với [[Dark Launch]] thường chạy code path mới trong cùng service. Đây là cách mạnh để test performance và correctness, nhưng cực kỳ nguy hiểm nếu request có side effect không được cô lập.

## Điều kiện an toàn

- Write phải bị chặn, redirect sang sandbox hoặc đảm bảo idempotent.
- Response mới phải được so sánh/log mà không gửi cho user.
- Traffic duplicate không được làm backend dependency quá tải.

## Liên kết

- [[Dark Launch]]
- [[Idempotency Key]]
- [[Synthetic Monitoring]]
- [[Load Testing]]
