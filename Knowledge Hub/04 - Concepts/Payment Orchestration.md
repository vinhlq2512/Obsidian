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

# Payment Orchestration

## Định nghĩa

Payment Orchestration là lớp điều phối các bước thanh toán qua nhiều payment method, PSP, redirect, webhook, refund, settlement, eligibility rule và UI requirement.

## Cách hiểu bằng lời của tôi

Payment orchestration là "workflow engine" của checkout. Nó không chỉ gọi API thu tiền, mà còn chuẩn hóa hành vi của nhiều nhà cung cấp để frontend, backend, observability và vận hành nhìn thấy một ngôn ngữ chung.

## Cơ chế từ source

- Airbnb dùng connector/plugin cho từng PSP và framework Multi-Step Transactions để chuẩn hóa các action như redirect, authentication challenge, QR hoặc flow đặc thù.
- Stripe dùng [[Payment Intent]] và [[Payment State Machine]] để gom các payment method khác nhau vào một integration nhất quán.
- Config trung tâm giúp frontend render input field, backend kiểm tra eligibility và hệ thống quan sát phát metric thống nhất.

## Khi áp dụng

- Hệ thống mở rộng nhiều quốc gia hoặc nhiều PSP.
- Payment flow có nhiều bước và kết quả bất đồng bộ.
- Team muốn thêm phương thức thanh toán mới bằng config/plugin thay vì sửa logic rải rác.

## Liên kết

- [[Payment Intent]]
- [[Payment Service Provider]]
- [[Local Payment Method]]
- [[Workflow Orchestration]]
- [[Observability]]
