---
type: synthesis
status: evolving
concepts:
  - "[[Tokenization]]"
  - "[[Tokenizer Pipeline]]"
  - "[[SentencePiece]]"
  - "[[Named Entity Recognition]]"
  - "[[Tokenizing Texts for NER]]"
sources:
  - "[[NLP Transformers - Chapter 04 - Multilingual Named Entity Recognition]]"
  - "[[28-07-2026]]"
questions: []
created_at: 2026-08-02
updated_at: 2026-08-02
tags:
  - synthesis
  - nlp
  - ner
  - tokenization
---

# Tokenization to NER Label Alignment

## Câu hỏi trung tâm

- Vì sao NER khó hơn text classification ở bước tokenization?

## Mental model

```text
words + word-level labels
-> tokenizer(is_split_into_words=True)
-> input_ids + attention_mask + word_ids
-> align labels sang subword tokens
-> ignore special tokens/subword phụ bằng -100
-> train token classification model
```

## Luồng hoặc cơ chế

- [[Tokenization]] biến text thành token IDs, nhưng NER cần giữ nhãn theo token/span.
- [[Tokenizer Pipeline]] có nhiều bước: normalization, pretokenization, tokenizer model, postprocessing.
- Khi tokenizer tách một word thành nhiều subword, nhãn word-level phải được map sang subword-level.
- `word_ids()` giúp biết token/subword nào thuộc word gốc nào.
- `-100` thường dùng để bỏ qua special tokens hoặc subword phụ trong loss.

## Tổng hợp của tôi

- Với classification, tokenize xong chỉ cần một nhãn cho cả câu.
- Với [[Named Entity Recognition]], tokenize xong phải giữ ranh giới nhãn. Nếu alignment sai, model có thể học sai entity boundary dù code vẫn chạy.
- [[SentencePiece]] hữu ích cho multilingual NLP, nhưng vì có thể tách từ/tên riêng thành nhiều subword, bước alignment càng phải được kiểm tra thủ công.

## Nguồn

- [[NLP Transformers - Chapter 04 - Multilingual Named Entity Recognition]]
- [[Tokenizer Pipeline]]
- [[Tokenizing Texts for NER]]
- [[SentencePiece]]

## Liên kết

- [[NLP]]
- [[Multilingual NER Workflow]]

