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

# RLHF

## Định nghĩa

RLHF là Reinforcement Learning from Human Feedback, phương pháp dùng phản hồi hoặc preference của con người để điều chỉnh model theo hành vi mong muốn.

## Cách hiểu bằng lời của tôi

Sau khi model biết sinh câu trả lời, RLHF giúp model chọn câu trả lời hữu ích, an toàn và hợp ý người dùng hơn. Thường cần preference data và reward model.

## Cần biết

- RLHF thường xuất hiện sau pretraining và supervised fine-tuning.
- Reward model học chấm điểm output.
- Quy trình phức tạp và nhạy với chất lượng preference data.

## Liên kết

- [[DPO]]
- [[Fine-tuning]]
- [[Generative Model]]

