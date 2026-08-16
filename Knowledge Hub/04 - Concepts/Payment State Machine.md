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

# Payment State Machine

## Định nghĩa

Payment State Machine là mô hình trạng thái dùng để biểu diễn tiến trình thanh toán qua nhiều bước, nhiều hệ thống và nhiều kết quả trung gian.

## Cách hiểu bằng lời của tôi

Payment không luôn là "request vào, response ra". Với global payments, trạng thái mới là phần cốt lõi: user có thể cần xác thực, app có thể redirect, PSP có thể trả webhook sau, và giao dịch có thể đang processing trong một khoảng thời gian.

## Cơ chế

- Trạng thái phải rõ ràng và hữu hạn.
- Mỗi transition nên gắn với event cụ thể: user action, PSP response, webhook, timeout hoặc retry.
- Object transaction như [[Payment Intent]] nên giữ trạng thái bền vững để client disconnect không làm mất giao dịch.

## Trade-off

- State machine làm API ban đầu phức tạp hơn charge đồng bộ.
- Đổi lại, nó giảm logic rẽ nhánh theo từng payment method và giúp integration mở rộng ra nhiều thị trường.

## Liên kết

- [[Payment Intent]]
- [[Payment Method]]
- [[Local Payment Method]]
- [[Workflow Orchestration]]
- [[Webhook]]
