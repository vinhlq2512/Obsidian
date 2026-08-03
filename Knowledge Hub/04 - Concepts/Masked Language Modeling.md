---
type: concept
status: developing
sources:
  - "[[SLP 2026 - Chapter 10 - Masked Language Models]]"
  - "[[2018 - BERT - Pre-training of Deep Bidirectional Transformers for Language Understanding - arXiv 1810.04805v2]]"
source_sections:
  - "[[SLP 2026 - Chapter 10 - Masked Language Models]]"
first_seen: 2026-08-03
last_updated: 2026-08-03
tags:
  - concept
  - nlp
  - cs224n
---

# Masked Language Modeling

## Định nghĩa

Masked language modeling là pretraining objective che một số token trong input và yêu cầu model dự đoán token bị che bằng cả ngữ cảnh trái và phải.

## Cách hiểu bằng lời của tôi

MLM giống bài điền vào chỗ trống. Vì chỗ trống nằm giữa câu, model được học representation hai chiều thay vì chỉ nhìn prefix như causal LM.

## Cơ chế

```text
input sentence
-> mask một số token
-> bidirectional Transformer encoder
-> dự đoán token bị mask
-> dùng hidden states cho downstream tasks
```

## Liên kết

- [[Bidirectional Attention]]
- [[Transformer]]
- [[Named Entity Recognition]]
- [[Causal Language Model]]
- [[CS224N]]
