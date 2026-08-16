---
type: concept
status: understood
sources:
  - "[[2026-04-28_how-stripe-detects-fraudulent-transactions-within-100-ms]]"
source_sections:
  - "[[2026-04-28_how-stripe-detects-fraudulent-transactions-within-100-ms]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - machine-learning
  - evaluation
---

# Precision-Recall Tradeoff

## Định nghĩa

Precision-Recall Tradeoff là đánh đổi giữa việc các case bị chặn có đúng là fraud hay không và việc hệ thống bắt được bao nhiêu fraud thật.

## Cách hiểu bằng lời của tôi

Trong fraud detection, tăng threshold thường làm precision cao hơn vì hệ thống chỉ chặn case chắc hơn, nhưng recall giảm vì nhiều fraud nhẹ lọt qua. Giảm threshold thì bắt được nhiều fraud hơn, nhưng dễ làm khách hàng thật bị chặn nhầm.

## Ý nghĩa hệ thống

- Đây không chỉ là bài toán data science mà còn là bài toán kinh doanh.
- Merchant margin thấp có thể chọn threshold aggressive vì một fraud có thể xóa sạch lợi nhuận của nhiều order tốt.
- Merchant LTV cao có thể chấp nhận bỏ sót một ít fraud để tránh false decline gây mất khách hàng thật.

## Liên kết

- [[Fraud Detection System]]
- [[LLM Evaluation]]
- [[Risk Matrix]]
