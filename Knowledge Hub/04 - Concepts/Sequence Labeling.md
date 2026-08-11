---
type: concept
status: seed
sources:
  - "[[Practical Natural Language Processing]]"
source_sections:
  - "[[Practical NLP - Chapter 05 - Information Extraction]]"
first_seen: 2026-08-10
last_updated: 2026-08-10
tags:
  - concept
  - nlp
  - ner
---

# Sequence Labeling

## Định nghĩa

Sequence labeling là bài toán gán nhãn cho từng phần tử trong một chuỗi, trong đó nhãn của phần tử hiện tại có thể phụ thuộc vào context xung quanh.

## Cách hiểu bằng lời của tôi

Khác với classification kiểu mỗi sample đứng riêng, sequence labeling đọc cả hàng rồi mới quyết định nhãn cho từng token trong hàng đó.

## Trong NER

- [[Named Entity Recognition]] thường được model như sequence labeling.
- Với mỗi word, model phải quyết định có phải entity không và nếu có thì là loại gì.
- Context của surrounding words rất quan trọng.
- Ví dụ `Washington` chỉ phân biệt rõ là person hay location khi nhìn câu như “Washington is a rainy state”.

## Dữ liệu thường gặp

- Dữ liệu train thường ở mức sentence.
- NER hay dùng BIO notation:
  `B` = beginning
  `I` = inside
  `O` = outside/non-entity

## Hướng triển khai

- Practical NLP nhắc CRF là một sequence classifier phổ biến cho NER.
- Feature có thể dựa trên word và POS tags để đưa thêm contextual information.

## Liên kết

- [[Named Entity Recognition]]
- [[Gazetteer]]
- [[Information Extraction]]
