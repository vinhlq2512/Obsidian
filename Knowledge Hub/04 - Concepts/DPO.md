---
type: concept
status: seed
source:
  - "[[Hands-On LLM - Chapter 12 - Fine-Tuning Generation Models]]"
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

## Liên kết

- [[RLHF]]
- [[Parameter-Efficient Fine-Tuning]]
- [[Generative Model]]
