---
type: course-source
course: "[[CS224N]]"
status: completed
source_type: paper
title: "2025 - DAPO - An Open-Source LLM Reinforcement Learning System at Scale"
year: 2025
venue: "arXiv"
arxiv: "2503.14476v2"
source_file: "[[2025 - DAPO - An Open-Source LLM Reinforcement Learning System at Scale - arXiv 2503.14476v2.pdf]]"
pages: 16
created_at: 2026-08-02
updated_at: 2026-08-03
completed_at: 2026-08-03
related_concepts:
  - "[[NLP]]"
tags:
  - cs224n
  - paper
---

# 2025 - DAPO - An Open-Source LLM Reinforcement Learning System at Scale - arXiv 2503.14476v2

## Nguồn

- PDF gốc: [[2025 - DAPO - An Open-Source LLM Reinforcement Learning System at Scale - arXiv 2503.14476v2.pdf]]
- Vai trò trong CS224N: paper/system về RL cho LLM ở scale, liên quan tới reasoning/post-training.

## Câu hỏi trung tâm

Một hệ thống open-source để chạy reinforcement learning cho LLM ở scale cần giải quyết những gì?

## Kiến thức cốt lõi

- DAPO thuộc cụm cải tiến RL reasoning sau PPO/GRPO.
- Open-source RL system cần recipe, infrastructure, data, reward và evaluation rõ ràng.
- RL ở scale nhạy với stability, sampling, reward design và distributed training.
- Paper liên hệ với DeepSeek-R1 và Lecture 12 về reasoning RL.
- Giá trị chính là làm quy trình RL reasoning tái lập hơn.

## Cơ chế / công thức / kiến trúc

```text
base/instruction model
-> rollout generation
-> reward / advantage estimation
-> policy optimization
-> evaluation trên reasoning benchmarks
-> iterate system-level recipe
```

## Khi áp dụng

- Dùng khi muốn hiểu RL post-training như hệ thống, không chỉ objective toán.
- Cần log và kiểm soát data/reward để tránh reward hacking.
- Open-source recipe hữu ích nhưng vẫn cần reproduce trên hardware/data cụ thể.

## Kết quả / bằng chứng đáng giữ

- Title nêu open-source LLM reinforcement learning system at scale.
- Lecture 12 đặt DAPO cạnh PPO/GRPO/DeepSeek-R1.
- Source thuộc nhóm reasoning RL trong CS224N.

## Cách hiểu bằng lời của tôi

DAPO nhắc rằng reasoning RL là bài toán pipeline. Loss function chỉ là một mảnh; rollout, reward, distributed infra và eval mới quyết định hệ thống chạy được không.

## Câu hỏi review

1. RL for LLM khác SFT ở bước dữ liệu nào?
2. Reward hacking có thể xuất hiện thế nào?
3. Vì sao open-source RL system quan trọng?

## Liên kết

- [[RLHF]]
- [[DPO]]
- [[Test-Time Compute]]
- [[Large Language Model]]
- [[CS224N]]
