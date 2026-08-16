---
type: concept
status: understood
sources:
  - "[[2026-03-10_how-airbnb-rolled-out-20-local-payment-methods-in-360-days]]"
  - "[[2026-02-18_the-first-10-year-evolution-of-stripes-payments-api]]"
source_sections:
  - "[[2026-03-10_how-airbnb-rolled-out-20-local-payment-methods-in-360-days]]"
  - "[[2026-02-18_the-first-10-year-evolution-of-stripes-payments-api]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - system-design
  - payments
---

# Local Payment Method

## Định nghĩa

Local Payment Method là phương thức thanh toán phổ biến ở một thị trường cụ thể, ví dụ ví nội địa, QR payment, bank redirect, cash voucher hoặc phương thức do hệ thống ngân hàng địa phương vận hành.

## Cách hiểu bằng lời của tôi

Nếu chỉ hỗ trợ thẻ, hệ thống payment có thể bỏ lỡ người dùng ở những thị trường mà thẻ không phải hành vi chính. [[Local Payment Method]] biến payment platform từ một card processor thành hạ tầng checkout có thể thích nghi theo quốc gia, tiền tệ, thiết bị và quy định.

## Flow thường gặp

- Direct flow: user nhập credential trong app và nhận kết quả gần thời gian thực.
- Redirect flow: user đi sang app/site của bên thứ ba rồi quay lại với result token.
- Async flow: user quét QR hoặc xác nhận ngoài app, hệ thống nhận kết quả qua [[Webhook]].

## Liên kết

- [[Payment Service Provider]]
- [[Payment Orchestration]]
- [[Payment State Machine]]
- [[Webhook]]
- [[Observability]]
