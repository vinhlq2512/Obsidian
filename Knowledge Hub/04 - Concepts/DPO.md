---
type: concept
status: seed
sources:
  - "[[Hands-On LLM - Chapter 12 - Fine-Tuning Generation Models]]"
  - "[[2026-07-14_how-llms-learn-to-be-helpful-rlhf-vs-dpo]]"
last_updated: 2026-08-16
tags:
  - concept
  - alignment
  - llm
---

# DPO

## Định nghĩa

DPO là Direct Preference Optimization, phương pháp preference tuning dùng các cặp preferred/rejected responses để tối ưu model trực tiếp theo preference.

## Cách hiểu bằng lời của tôi

Thay vì train reward model rồi chạy reinforcement learning phức tạp, DPO học trực tiếp từ ví dụ "câu trả lời A tốt hơn câu trả lời B".

## Cần biết

- DPO cần dữ liệu preference gồm chosen và rejected outputs.
- Thường đơn giản hơn pipeline RLHF truyền thống.
- Hữu ích khi mục tiêu là align style, helpfulness hoặc preference cụ thể.
- DPO tăng xác suất response được chọn và giảm xác suất response bị loại, đo tương đối với frozen reference model.
- DPO không xóa reward signal; nó gộp reward vào chính policy thay vì train reward model riêng.
- DPO vẫn thừa hưởng lỗi của preference data, ví dụ người chấm thích câu trả lời tự tin/dễ nghe hơn câu trả lời đúng.

## Liên kết

- [[RLHF]]
- [[Preference Learning]]
- [[Parameter-Efficient Fine-Tuning]]
- [[LLM Evaluation]]
- [[Generative Model]]
