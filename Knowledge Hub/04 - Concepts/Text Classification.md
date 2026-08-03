---
type: concept
status: seed
sources:
  - "[[Hands-On LLM - Chapter 04 - Text Classification]]"
  - "[[NLP Transformers - Chapter 09 - Dealing with Few to No Labels]]"
last_updated: 2026-08-03
tags:
  - concept
  - classification
  - nlp
---

# Text Classification

## Định nghĩa

Text classification là tác vụ gán một hoặc nhiều nhãn cho văn bản.

## Cách hiểu bằng lời của tôi

Đầu vào là text, đầu ra là label. Có thể làm bằng classic ML, representation model, embedding classifier hoặc generative model.

## Cần biết

- Nếu có dữ liệu nhãn tốt, supervised model thường ổn định.
- Nếu thiếu nhãn, có thể thử zero-shot hoặc few-shot prompting.
- Cần baseline đơn giản để biết LLM có thật sự cần thiết không.
- [[Intent Detection]] là một case study của text classification trong đó nhãn là ý định của người dùng.

## Liên kết

- [[Intent Detection]]
- [[Few-shot Learning]]
- [[Zero-shot Classification]]
- [[Representation Model]]
- [[Generative Model]]
- [[Embedding]]
- [[Fine-tuning]]
