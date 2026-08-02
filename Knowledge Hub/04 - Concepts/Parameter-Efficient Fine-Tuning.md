---
type: concept
status: seed
sources:
  - "[[Hands-On LLM - Chapter 12 - Fine-Tuning Generation Models]]"
tags:
  - concept
  - fine-tuning
  - llm
---

# Parameter-Efficient Fine-Tuning

## Định nghĩa

Parameter-Efficient Fine-Tuning là nhóm kỹ thuật fine-tune chỉ một phần nhỏ tham số hoặc adapter, thay vì cập nhật toàn bộ model.

## Cách hiểu bằng lời của tôi

Ta giữ model gốc gần như cố định và học một "miếng điều chỉnh" nhỏ. Điều này giảm memory, compute và chi phí lưu trữ.

## Cần biết

- LoRA là kỹ thuật PEFT phổ biến.
- QLoRA kết hợp quantization với LoRA để fine-tune model lớn trên GPU hạn chế.
- PEFT phù hợp khi cần customize model nhưng không đủ tài nguyên full fine-tuning.

## Liên kết

- [[Fine-tuning]]
- [[Generative Model]]
- [[DPO]]

