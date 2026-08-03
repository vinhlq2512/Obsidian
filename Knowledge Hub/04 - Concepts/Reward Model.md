---
type: concept
status: developing
sources:
  - "[[CS224N 2026 - Lecture 08 - Post-training]]"
  - "[[2025 - Multimodal RewardBench - Holistic Evaluation of Reward Models for Vision Language Models - arXiv 2502.14191v1]]"
source_sections:
  - "[[CS224N 2026 - Lecture 08 - Post-training]]"
first_seen: 2026-08-03
last_updated: 2026-08-03
tags:
  - concept
  - llm
  - alignment
  - cs224n
---

# Reward Model

## Định nghĩa

Reward model là model học chấm điểm response theo mức phù hợp với preference/rubric, thường dùng trong [[RLHF]] hoặc đánh giá alignment.

## Cách hiểu bằng lời của tôi

Reward model là giám khảo học từ dữ liệu preference. Nếu giám khảo lệch, policy được train theo nó cũng có thể lệch.

## Cần biết

- Reward model thường học từ cặp response thắng/thua.
- Trong multimodal setting, reward model phải hiểu cả image/video và text response.
- Reward hacking xảy ra khi policy tìm cách tối đa reward nhưng không thật sự tốt cho người dùng.

## Liên kết

- [[RLHF]]
- [[DPO]]
- [[Multimodal LLM]]
- [[Measuring the Quality of Generated Text]]
- [[CS224N]]
