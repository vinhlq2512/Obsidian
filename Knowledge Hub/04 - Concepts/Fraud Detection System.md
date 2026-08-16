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
  - system-design
  - machine-learning
  - payments
---

# Fraud Detection System

## Định nghĩa

Fraud Detection System là hệ thống đánh giá giao dịch để quyết định cho qua, chặn hoặc đưa vào manual review dựa trên tín hiệu rủi ro, mô hình ML và chính sách kinh doanh.

## Cách hiểu bằng lời của tôi

Fraud detection trong payment là bài toán thời gian thực có base rate rất thấp: gian lận hiếm nhưng cost cao. Hệ thống tốt không chỉ cần model chính xác, mà còn cần feature production latency thấp, label feedback loop, explainability và kiểm soát tác động theo từng merchant.

## Cơ chế từ Stripe Radar

- Thu thập nhiều tín hiệu từ transaction, device, card, merchant, network và dispute label.
- Dùng feature aggregate trên toàn mạng lưới để phát hiện pattern mà merchant đơn lẻ không thấy.
- Chọn threshold theo [[Precision-Recall Tradeoff]] và economics của từng merchant.
- Đưa borderline case vào manual review để thay đổi trade-off giữa block nhầm và bỏ sót fraud.
- Kiểm tra model mới trên aggregate metrics lẫn per-merchant impact trước khi release.

## Liên kết

- [[Precision-Recall Tradeoff]]
- [[LLM Evaluation]]
- model drift
- [[Observability]]
- [[Risk Matrix]]
