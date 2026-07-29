---
type: concept
status: seed
source:
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
- Thường dùng BIO/BILOU tagging scheme.

## Liên kết

- [[Tokenization]]
- [[Representation Model]]
- [[Fine-tuning]]
