---
type: concept
status: understood
sources:
  - "[[2026-07-14_how-llms-learn-to-be-helpful-rlhf-vs-dpo]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - llm
  - alignment
  - rlhf
---

# Reinforcement Learning from Human Feedback

## Định nghĩa

Reinforcement Learning from Human Feedback (RLHF - Học tăng cường từ phản hồi của con người) là quy trình tinh chỉnh mô hình AI bằng cách kết hợp học tăng cường (Reinforcement Learning) với một Reward Model được huấn luyện dựa trên sở thích và đánh giá xếp hạng của con người.

## Luồng huấn luyện 3 bước

```text
Step 1: Supervised Fine-Tuning (SFT)
        Prompt -> High-Quality Human Demonstrations -> Baseline SFT Model

Step 2: Reward Model Training
        Prompt -> Model generates multiple outputs (y1, y2) -> Human ranks y1 > y2
        -> Train Reward Model (RM) to predict human preference scores

Step 3: Reinforcement Learning Fine-Tuning (PPO)
        Prompt -> Policy LLM generates output -> Reward Model scores output
        -> Proximal Policy Optimization (PPO) updates Policy LLM parameters
```

1. **Step 1 - SFT**: Huấn luyện base model trên dữ liệu hội thoại mẫu.
2. **Step 2 - Reward Model**: Thu thập dữ liệu đánh giá xếp hạng giữa các câu trả lời $y_w \succ y_l$ và huấn luyện Reward Model để chấm điểm bất kỳ câu trả lời nào.
3. **Step 3 - PPO Optimization**: Dùng thuật toán PPO để tối ưu hóa Policy LLM sinh câu trả lời có Reward score cao nhất, đồng thời thêm KL-penalty để tránh mô hình lệch quá xa khỏi SFT model gốc.

## So sánh với DPO

- **RLHF (PPO)**: Cần duy trì 4 mô hình đồng thời trong bộ nhớ GPU (Policy, Reference, Value, Reward). Phức tạp và tốn kém nhưng rất mạnh cho các task mở.
- **[[Direct Preference Optimization|DPO]]**: Bỏ qua bước huấn luyện Reward Model và PPO, tối ưu trực tiếp Policy bằng hàm classification loss.

## Liên kết

- [[Direct Preference Optimization]]
- [[Model Alignment]]
- [[Preference Learning]]
- [[Production LLM System Design]]
