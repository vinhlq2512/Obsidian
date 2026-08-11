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

# Relation Extraction

## Định nghĩa

Relation extraction là task trích quan hệ giữa các entities được nhắc trong text.

## Cách hiểu bằng lời của tôi

NER tìm các “điểm”; relation extraction nối các điểm đó bằng một cạnh có nghĩa. Ví dụ không chỉ biết `Luca Maestri` và `Apple`, mà biết quan hệ `finance chief of`.

## Trong IE

```text
entity A
entity B
context
-> relation label / relation record
```

- Practical NLP dùng ví dụ: `Luca Maestri` là finance chief của `Apple`.
- Relation extraction cần nhiều thông tin hơn NER vì phải hiểu mối liên hệ giữa nhiều entity trong cùng context.
- Đây là bước quan trọng để biến text thành structured records hoặc knowledge graph.

## Liên kết

- [[Information Extraction]]
- [[Named Entity Recognition]]
- [[Entity Linking]]
