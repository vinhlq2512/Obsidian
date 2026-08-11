---
type: concept
status: seed
sources:
  - "[[Practical Natural Language Processing]]"
source_sections:
  - "[[Practical NLP - Chapter 05 - Information Extraction]]"
first_seen: 2026-08-11
last_updated: 2026-08-11
tags:
  - concept
  - nlp
  - information-extraction
---

# Entity Linking

## Định nghĩa

Entity linking là task nối một entity mention trong text với thực thể cụ thể tương ứng trong knowledge base hoặc thế giới thực.

## Cách hiểu bằng lời của tôi

NER chỉ nói “Apple” là một organization. Entity linking phải nói rõ đó là Apple Inc., không phải trái táo hay một tổ chức khác có chữ Apple.

## Trong IE

```text
entity mention
-> disambiguation
-> linked entity
```

- Practical NLP gộp named entity disambiguation and linking như một task IE sau NER.
- Task này cần context quanh mention để phân biệt các thực thể có cùng tên hoặc tên gần giống nhau.
- Entity linking làm entity trở thành dữ liệu có thể query và nối vào knowledge base.

## Liên kết

- [[Information Extraction]]
- [[Named Entity Recognition]]
- [[Relation Extraction]]
