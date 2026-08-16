---
type: concept
status: understood
sources:
  - "[[2026-03-10_how-airbnb-rolled-out-20-local-payment-methods-in-360-days]]"
source_sections:
  - "[[2026-03-10_how-airbnb-rolled-out-20-local-payment-methods-in-360-days]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - system-design
  - payments
---

# Payment Service Provider

## Định nghĩa

Payment Service Provider là nhà cung cấp hoặc cổng thanh toán bên ngoài mà hệ thống tích hợp để xử lý charge, redirect, refund, settlement hoặc thông báo kết quả thanh toán.

## Cách hiểu bằng lời của tôi

PSP là dependency vừa kỹ thuật vừa vận hành. Mỗi PSP có API, timeout, webhook, trạng thái và quy tắc thị trường khác nhau. Vì vậy hệ thống lớn thường cần connector/plugin để giấu sự khác biệt này sau một contract nội bộ.

## Rủi ro thiết kế

- Logic PSP rải trong frontend/backend làm khó thêm phương thức mới.
- Không có emulator thì khó test flow địa phương.
- Không có metric theo PSP thì incident dễ bị phát hiện muộn hoặc đổ lỗi sai tầng.

## Liên kết

- [[Payment Orchestration]]
- [[Local Payment Method]]
- [[Webhook]]
- [[Synthetic Monitoring]]
- [[Incident Response]]
