---
type: concept
status: understood
sources:
  - "[[2026-02-18_the-first-10-year-evolution-of-stripes-payments-api]]"
  - "[[2026-03-10_how-airbnb-rolled-out-20-local-payment-methods-in-360-days]]"
source_sections:
  - "[[2026-02-18_the-first-10-year-evolution-of-stripes-payments-api]]"
  - "[[2026-03-10_how-airbnb-rolled-out-20-local-payment-methods-in-360-days]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - system-design
  - payments
---

# Payment Method

## Định nghĩa

Payment Method mô tả cách khách hàng muốn trả tiền: thẻ, tài khoản ngân hàng, ví điện tử, chuyển khoản địa phương, QR code hoặc một scheme thanh toán cụ thể.

## Cách hiểu bằng lời của tôi

Trong thiết kế API thanh toán tốt, "cách trả tiền" nên tách khỏi "giao dịch đang cần thu bao nhiêu tiền". [[Payment Method]] chứa thông tin tĩnh hoặc bán tĩnh về instrument, còn [[Payment Intent]] giữ trạng thái của transaction.

## Vì sao cần tách abstraction

- Một người dùng có thể thử nhiều payment method cho cùng một đơn hàng.
- Mỗi payment method có vòng đời khác nhau: thẻ có thể đồng bộ, ví điện tử cần redirect, QR cần webhook, bank debit có thể mất nhiều ngày.
- Nếu nhét tất cả vào một object charge/source, API dễ trở thành state machine khó hiểu.

## Liên kết

- [[Payment Intent]]
- [[Local Payment Method]]
- [[Payment State Machine]]
- [[Payment Service Provider]]
