---
type: concept
status: seed
sources:
  - "[[2026-05-19_how-snapchat-serves-a-billion-predictions-per-second]]"
source_sections:
  - "[[2026-05-19_how-snapchat-serves-a-billion-predictions-per-second]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - mlops
  - inference
---

# Inference Compute Graph Split

## Định nghĩa

[[Inference Compute Graph Split]] là kỹ thuật export model thành các phần chạy trên phần cứng khác nhau, ví dụ embedding lookup/feature parsing trên CPU và dense matrix computation trên GPU.

## Cách hiểu bằng lời của tôi

Recommendation model có hai dạng chi phí khác nhau: embedding table ăn memory, dense layer ăn compute. Đặt tất cả lên GPU hoặc CPU đều lãng phí. Snap split graph lúc export để mỗi phần chạy ở nơi hợp lý hơn.

## Liên kết

- [[AI Model Serving]]
- [[LLM Inference Engineering]]
- [[Feature Collocation]]
- [[AI Hardware Accelerator]]
- [[Cost Optimization]]
