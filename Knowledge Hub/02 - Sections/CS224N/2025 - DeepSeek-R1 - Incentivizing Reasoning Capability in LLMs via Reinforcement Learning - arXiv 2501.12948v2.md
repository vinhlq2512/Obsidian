---
type: course-source
course: "[[CS224N]]"
status: completed
source_type: paper
title: "2025 - DeepSeek-R1 - Incentivizing Reasoning Capability in LLMs via Reinforcement Learning"
year: 2025
venue: "arXiv"
arxiv: "2501.12948v2"
source_file: "[[2025 - DeepSeek-R1 - Incentivizing Reasoning Capability in LLMs via Reinforcement Learning - arXiv 2501.12948v2.pdf]]"
pages: 86
created_at: 2026-08-02
updated_at: 2026-08-03
completed_at: 2026-08-03
related_concepts:
  - "[[Prompt Engineering]]"
  - "[[Large Language Model]]"
  - "[[RLHF]]"
tags:
  - cs224n
  - paper
---
# 2025 - DeepSeek-R1 - Incentivizing Reasoning Capability in LLMs via Reinforcement Learning - arXiv 2501.12948v2

## Nguồn

- PDF gốc: [[2025 - DeepSeek-R1 - Incentivizing Reasoning Capability in LLMs via Reinforcement Learning - arXiv 2501.12948v2.pdf]]
- Đọc cùng: [[CS224N 2026 - Lecture 12 - Reasoning Part 1]], [[CS224N 2026 - Lecture 19 - The Art of Artificial Reasoning for Small Language Models]]
- Concept: [[RLHF]], [[Prompt Engineering]], [[Large Language Model]]

## Vấn đề paper giải quyết

General reasoning vẫn là thách thức lớn. Paper đặt trọng tâm vào việc khuyến khích reasoning capability bằng reinforcement learning, giảm phụ thuộc vào human-labeled reasoning trajectories.

## Đóng góp chính

- Cho thấy RL có thể làm xuất hiện các pattern reasoning như self-reflection, verification và strategy adaptation.
- Nhấn mạnh vai trò của reward/training framework trong việc tạo hành vi reasoning.
- Trở thành case study cho lecture về reasoning, test-time compute và smart scaling.

## Cơ chế trực giác

```text
base model
-> RL objective thưởng lời giải đúng / hành vi reasoning hữu ích
-> model khám phá reasoning traces
-> distill hoặc dùng model reasoning cho inference-time scaling
```

## Vì sao quan trọng với CS224N

Lecture 12 và 19 dùng DeepSeek-R1 như ví dụ rằng reasoning không chỉ đến từ scale pretraining, mà có thể được incentivize bằng training signal và thuật toán phù hợp.

## Hạn chế / câu hỏi

- Reward thiết kế sai có thể tạo shortcut hoặc reasoning trace giả.
- Cần tách năng lực final answer khỏi chất lượng process.
- RL reasoning đòi hỏi evaluation nghiêm túc vì output dài và nhiều bước.

## Câu hỏi review

1. Paper muốn giảm phụ thuộc vào loại data nào?
2. RL có thể khuyến khích các pattern reasoning nào?
3. Vì sao reasoning trace không tự động đáng tin?
