---
type: concept
status: developing
sources:
  - "[[2023 - Self-Consistency Improves Chain of Thought Reasoning in Language Models - ICLR 2023]]"
source_sections:
  - "[[2023 - Self-Consistency Improves Chain of Thought Reasoning in Language Models - ICLR 2023]]"
first_seen: 2026-08-03
last_updated: 2026-08-03
tags:
  - concept
  - text-generation
  - cs224n
---

# Self-Consistency Decoding

## Định nghĩa

Self-consistency decoding là chiến lược lấy mẫu nhiều reasoning paths, rồi chọn đáp án cuối nhất quán nhất giữa các paths.

## Cách hiểu bằng lời của tôi

Thay vì tin lần suy luận đầu tiên, ta cho model giải nhiều lần. Nếu nhiều đường suy luận khác nhau hội tụ về cùng một đáp án, đáp án đó đáng tin hơn một sample đơn lẻ.

## Cơ chế

```text
prompt chain-of-thought
-> sample nhiều lời giải
-> lấy final answer từng lời giải
-> vote / marginalize
-> chọn answer nhất quán
```

## Liên kết

- [[Chain-of-Thought Prompting]]
- [[Nucleus Sampling]]
- [[Top-k Sampling]]
- [[Test-Time Compute]]
- [[CS224N]]
