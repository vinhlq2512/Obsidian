---
type: concept
status: seed
sources:
  - "[[Hands-On LLM - Chapter 11 - Fine-Tuning Representation Models for Classification]]"
  - "[[NLP Transformers - Chapter 04 - Multilingual Named Entity Recognition]]"
tags:
  - concept
  - ner
  - nlp
---

# Named Entity Recognition

## Định nghĩa

Named Entity Recognition là tác vụ nhận diện và gán nhãn các thực thể trong văn bản, ví dụ người, tổ chức, địa điểm, sản phẩm hoặc ngày tháng.

## Cách hiểu bằng lời của tôi

NER không gán nhãn cho cả câu mà gán nhãn cho token/span. Vì tokenizer có thể tách một từ thành nhiều subword, phần align label rất quan trọng.

## Cần biết

- Đây là token-level task.
- Cần xử lý special tokens và subword labels đúng cách.
- [[Tokenizing Texts for NER]] là bước nối word-level labels với token/subword IDs, thường dùng `word_ids()` và label `-100` cho vị trí không tính loss.
- [[Performance Measures for NER]] nên dùng entity-level precision, recall và F1 vì token accuracy dễ bị nhãn `O` làm đẹp giả.
- Thường dùng BIO/BILOU tagging scheme.

## Liên kết

- [[Tokenization]]
- [[Tokenizing Texts for NER]]
- [[Performance Measures for NER]]
- [[Representation Model]]
- [[Fine-tuning]]
