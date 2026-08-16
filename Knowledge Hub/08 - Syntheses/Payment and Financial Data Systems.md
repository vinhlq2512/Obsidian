---
type: synthesis
status: seed
concepts:
  - "[[Payment Intent]]"
  - "[[Payment Method]]"
  - "[[Payment State Machine]]"
  - "[[Local Payment Method]]"
  - "[[Payment Orchestration]]"
  - "[[Payment Service Provider]]"
  - "[[Fraud Detection System]]"
  - "[[Precision-Recall Tradeoff]]"
  - "[[Financial Source of Truth]]"
  - "[[Data Contract]]"
  - "[[Shadow Testing]]"
  - "[[Data Freshness]]"
sources:
  - "[[2026-02-18_the-first-10-year-evolution-of-stripes-payments-api]]"
  - "[[2023-05-24_api-redesign-shopping-cart-and-stripe-payment]]"
  - "[[2026-03-10_how-airbnb-rolled-out-20-local-payment-methods-in-360-days]]"
  - "[[2026-04-28_how-stripe-detects-fraudulent-transactions-within-100-ms]]"
  - "[[2026-03-03_how-agoda-built-a-single-source-of-truth-for-financial-data]]"
questions: []
created_at: 2026-08-16
updated_at: 2026-08-16
tags:
  - synthesis
  - system-design
  - payments
  - finance
---

# Payment and Financial Data Systems

## Mental model

Payment systems là nơi API design, workflow orchestration, ML decisioning và data governance gặp nhau. Một checkout thành công không chỉ là "charge tiền", mà là chuỗi trạng thái bền vững qua client, merchant backend, PSP, webhook, fraud model, ledger và downstream reporting.

## Các lớp chính

| Lớp | Concept | Vai trò |
| --- | --- | --- |
| Payment API | [[Payment Intent]], [[Payment Method]], [[Payment State Machine]] | Tách "what" của giao dịch khỏi "how" của phương thức thanh toán |
| Local expansion | [[Local Payment Method]], [[Payment Service Provider]], [[Payment Orchestration]] | Chuẩn hóa redirect, async flow, QR, PSP plugin và config-driven UI |
| Risk decisioning | [[Fraud Detection System]], [[Precision-Recall Tradeoff]] | Chấm điểm giao dịch trong latency thấp nhưng vẫn cho merchant điều chỉnh threshold |
| Financial data | [[Financial Source of Truth]], [[Data Contract]], [[Shadow Testing]], [[Data Freshness]] | Giữ số liệu tài chính nhất quán, đúng hạn và có thể kiểm chứng |

## Bài học thiết kế

- Abstraction đúng quan trọng hơn số lượng endpoint ít. `Charge` đơn giản cho thẻ, nhưng [[Payment Intent]] phù hợp hơn khi payment method có trạng thái bất đồng bộ.
- Payment flow cần resilient với client disconnect; trạng thái bền vững và [[Webhook]] giúp fulfillment không phụ thuộc vào một request.
- Local payment method nên được tích hợp bằng plugin/config, không hardcode mỗi thị trường trong UI và backend.
- Fraud model phải được deploy như một production system: feature latency, model drift, merchant-level impact và explainability đều là phần của kiến trúc.
- Financial data nên có một nguồn tin cậy trung tâm khi sai lệch định nghĩa có thể ảnh hưởng reconciliation hoặc ledger.

## Liên kết

- [[API Design Patterns]]
- [[Modern Web Request Architecture]]
- [[Observability for Distributed Systems]]
- [[Reliability Operations Loop]]
