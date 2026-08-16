---
type: concept
status: developing
sources:
  - "[[2026-07-14_how-llms-learn-to-be-helpful-rlhf-vs-dpo]]"
  - "[[2025-09-24_how-fine-tuning-transforms-generic-ai-models-into-specialist]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - llm
  - alignment
  - fine-tuning
---

# Preference Learning

## Định nghĩa

Preference learning là nhóm phương pháp dạy model chọn response tốt hơn dựa trên so sánh winner/loser, thay vì chỉ học một đáp án cố định.

## Cách hiểu bằng lời của tôi

Nhiều câu trả lời đều đúng nhưng khác nhau về độ hữu ích, độ dài, giọng điệu, độ thận trọng hoặc mức bám sát yêu cầu. Preference learning biến judgment kiểu "A tốt hơn B" thành tín hiệu train được.

## Hai hướng chính

- [[RLHF]]: train reward model từ preference data, rồi dùng reinforcement learning để tối ưu policy.
- [[DPO]]: dùng cùng loại dữ liệu chosen/rejected nhưng tối ưu policy trực tiếp, đơn giản hơn pipeline RLHF.

## Rủi ro

- Reward hoặc preference là proxy, không phải chân lý.
- Nếu tối ưu proxy quá mạnh, model có thể học cách làm hài lòng evaluator thay vì đúng.
- Với task có đáp án kiểm chứng được, verifiable reward bằng chương trình/test có thể tốt hơn human preference.

## Liên kết

- [[Fine-tuning]]
- [[Instruction Fine-Tuning]]
- [[RLHF]]
- [[DPO]]
- [[LLM Evaluation]]
