---
type: concept
status: developing
sources:
  - "[[2022 - Chain-of-Thought Prompting Elicits Reasoning in Large Language Models - arXiv 2201.11903v6]]"
  - "[[CS224N 2026 - Lecture 12 - Reasoning Part 1]]"
source_sections:
  - "[[2022 - Chain-of-Thought Prompting Elicits Reasoning in Large Language Models - arXiv 2201.11903v6]]"
first_seen: 2026-08-03
last_updated: 2026-08-03
tags:
  - concept
  - prompting
  - cs224n
---

# Chain-of-Thought Prompting

## Định nghĩa

Chain-of-thought prompting là kỹ thuật prompt yêu cầu hoặc minh hoạ model sinh các bước suy luận trung gian trước khi đưa ra đáp án cuối.

## Cách hiểu bằng lời của tôi

CoT cho model một vùng "nháp bằng chữ". Thay vì nhảy thẳng đến đáp án, model có cơ hội phân rã bài toán thành các bước nhỏ.

## Cần biết

- Hiệu quả rõ hơn ở model đủ lớn.
- CoT có thể cải thiện final answer nhưng reasoning trace vẫn có thể sai.
- Có thể kết hợp với [[Self-Consistency Decoding]] hoặc verifier.

## Liên kết

- [[Prompt Engineering]]
- [[Test-Time Compute]]
- [[Large Language Model]]
- [[CS224N]]
