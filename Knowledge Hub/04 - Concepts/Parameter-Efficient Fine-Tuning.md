---
type: concept
status: developing
sources:
  - "[[Hands-On LLM - Chapter 12 - Fine-Tuning Generation Models]]"
  - "[[CS224N 2026 - Lecture 09 - Efficient Adaptation]]"
  - "[[2021 - LoRA - Low-Rank Adaptation of Large Language Models - arXiv 2106.09685v2]]"
last_updated: 2026-08-03
tags:
  - concept
  - fine-tuning
  - llm
  - peft
---

# Parameter-Efficient Fine-Tuning

## Định nghĩa

Parameter-Efficient Fine-Tuning là nhóm kỹ thuật fine-tune chỉ một phần nhỏ tham số hoặc adapter, thay vì cập nhật toàn bộ model.

## Vấn đề cần giải quyết

Full fine-tuning cập nhật toàn bộ model nên tốn VRAM, optimizer state, thời gian train và chi phí lưu checkpoint cho từng task. Với LLM lớn, chi phí này nhanh chóng trở thành điểm nghẽn khi cần nhiều domain hoặc nhiều khách hàng khác nhau.

## Cách hiểu bằng lời của tôi

Ta giữ model gốc gần như cố định và học một "miếng điều chỉnh" nhỏ. Điều này giảm memory, compute và chi phí lưu trữ.

## Các nhóm phương pháp

- [[Adapter]] chèn module bottleneck nhỏ vào giữa các layer.
- [[LoRA]] freeze weight gốc và học update hạng thấp $\Delta W = BA$ cho một số ma trận như $W_q$ và $W_v$.
- [[QLoRA]] kết hợp quantization 4-bit của base model với LoRA để giảm thêm memory.
- Prompt tuning học embedding prompt liên tục thay vì sửa toàn bộ model.

## Cần biết

- PEFT không chỉ giảm số tham số trainable mà còn giúp lưu nhiều task-specific variants gọn hơn.
- LoRA mạnh ở điểm có thể merge update vào weight gốc, nên không tăng inference latency.
- Adapter dễ hiểu như module phụ, nhưng có thể thêm độ trễ nếu giữ module trong đường forward.
- PEFT phù hợp khi cần customize model nhưng không đủ tài nguyên full fine-tuning.

## Liên kết

- [[Fine-tuning]]
- [[Generative Model]]
- [[LoRA]]
- [[QLoRA]]
- [[Adapter]]
- [[DPO]]
