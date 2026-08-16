---
type: concept
status: understood
sources:
  - "[[2026-02-18_the-first-10-year-evolution-of-stripes-payments-api]]"
  - "[[2023-05-24_api-redesign-shopping-cart-and-stripe-payment]]"
source_sections:
  - "[[2026-02-18_the-first-10-year-evolution-of-stripes-payments-api]]"
  - "[[2023-05-24_api-redesign-shopping-cart-and-stripe-payment]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - system-design
  - payments
---

# Payment Intent

## Định nghĩa

Payment Intent là object đại diện cho ý định thu tiền của một giao dịch: số tiền, tiền tệ, trạng thái thanh toán và tiến trình xử lý cho tới khi tiền được đảm bảo.

## Cách hiểu bằng lời của tôi

Thay vì xem payment là một request đồng bộ kiểu "charge rồi biết ngay thành công/thất bại", [[Payment Intent]] xem payment là một state machine sống đủ lâu để chịu được redirect, xác thực ngoài app, webhook trễ, client mất kết nối và thử lại bằng phương thức khác.

## Cơ chế

- Server tạo Payment Intent với amount và currency.
- Client nhận `client_secret`, chọn [[Payment Method]] và xác nhận thanh toán.
- Intent có thể đi qua các trạng thái như cần payment method, cần xác nhận, cần user action, đang xử lý, rồi succeeded.
- Merchant fulfillment nên dựa vào trạng thái cuối cùng hoặc webhook, không dựa vào một response HTTP ngắn ngủi.

## Điểm quan trọng

- Payment Intent gom nhiều attempt vào một transaction-level object, nên giảm nguy cơ double charge khi người dùng đổi phương thức thanh toán.
- Đây là ví dụ tốt của [[API Lifecycle Management]]: Stripe giữ compatibility với `Charge` phía sau nhưng đưa developer sang abstraction nhất quán hơn.

## Liên kết

- [[Payment Method]]
- [[Payment State Machine]]
- [[Payment Orchestration]]
- [[Webhook]]
- [[API Lifecycle Management]]
