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

# RLHF

## Định nghĩa

RLHF là Reinforcement Learning from Human Feedback, phương pháp dùng phản hồi hoặc preference của con người để điều chỉnh model theo hành vi mong muốn.

## Cách hiểu bằng lời của tôi

Sau khi model biết sinh câu trả lời, RLHF giúp model chọn câu trả lời hữu ích, an toàn và hợp ý người dùng hơn. Thường cần preference data và reward model.

## Cần biết

- RLHF thường xuất hiện sau pretraining và supervised fine-tuning.
- Reward model học chấm điểm output.
- Quy trình phức tạp và nhạy với chất lượng preference data.
- Pipeline thường gồm policy model, reward model, frozen reference model và thuật toán RL như PPO.
- KL penalty giữ policy không trôi quá xa khỏi model ban đầu.
- RLHF mạnh khi bài toán là judgment: hữu ích, an toàn, đúng tone, đủ thận trọng.
- Nếu reward proxy bị tối ưu quá mạnh, model có thể học hành vi nghe hay nhưng kém thật.

## Từ ByteByteGo

ByteByteGo nhấn mạnh RLHF học từ comparison: cùng một prompt, nhiều response, con người chọn winner/loser. Reward model biến các phán đoán rời rạc thành hàm điểm, rồi policy được tối ưu để đạt điểm cao hơn. Đây là pipeline mạnh nhưng nhiều thành phần, đắt và dễ nhạy với chất lượng tín hiệu reward.

## Liên kết

- [[DPO]]
- [[Preference Learning]]
- [[Fine-tuning]]
- [[LLM Evaluation]]
- [[Generative Model]]
