---
type: concept
status: developing
sources:
  - "[[2011 - Natural Language Processing Almost from Scratch - JMLR]]"
  - "[[CS224N 2026 - Lecture 03 - Neural Network Foundations]]"
source_sections:
  - "[[2011 - Natural Language Processing Almost from Scratch - JMLR]]"
first_seen: 2026-08-03
last_updated: 2026-08-03
tags:
  - concept
  - nlp
  - cs224n
---

# Neural NLP

## Định nghĩa

Neural NLP là hướng xây hệ thống NLP bằng neural networks học representation từ dữ liệu, thay vì dựa chủ yếu vào feature engineering thủ công cho từng task.

## Cách hiểu bằng lời của tôi

Thay vì con người phải viết feature như "token này viết hoa", "từ này có suffix X", "dependency path là Y", neural NLP để model học các biểu diễn trung gian hữu ích qua training objective.

## Cần biết

- Bước đầu của neural NLP dùng embeddings và task-specific architectures.
- Pretrained [[Transformer]] sau này mở rộng cùng ý tưởng: học representation chung ở scale lớn.
- Neural NLP không xoá nhu cầu thiết kế hệ thống; nó chuyển phần lớn thiết kế sang architecture, objective, data và evaluation.

## Liên kết

- [[Embedding]]
- [[Transformer]]
- [[Representation Model]]
- [[CS224N]]
