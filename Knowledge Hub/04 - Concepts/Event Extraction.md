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

# Event Extraction

## Định nghĩa

Event extraction là task nhận diện event được nói tới trong text và các thông tin liên quan đến event đó.

## Cách hiểu bằng lời của tôi

Event extraction không chỉ lấy entity riêng lẻ; nó cố gắng hiểu “chuyện gì đã xảy ra” và có thể nối nhiều bài viết nói về cùng một chuyện.

## Trong IE

```text
text
-> event mention / event type
-> related arguments / time
-> temporally ordered event graph
```

- Practical NLP dùng ví dụ event “Apple buys back stocks”.
- Event extraction có thể giúp liên kết nhiều articles nói về cùng một event theo thời gian.
- Sách mô tả mục tiêu cuối là nối các event theo thời gian để tạo temporally ordered event graph.
- Temporal information extraction là task liên quan, tập trung vào times và dates, hữu ích cho calendar apps và personal assistants.

## Cách làm

- Sách xem event extraction là supervised learning problem.
- Contemporary approaches dùng sequence tagging và multilevel classifiers.
- Với task khó, sách khuyên bắt đầu bằng rule-based approach dựa trên domain knowledge, rồi follow up bằng weak supervision.
- Khi có đủ data hơn, có thể tiến dần sang ML approaches.

## Giới hạn

- Đây vẫn là active area of research.
- Theo sách, chưa có off-the-shelf service hoặc package thật sự generic cho task này.

## Liên kết

- [[Information Extraction]]
- [[Temporal Information Extraction]]
- [[Relation Extraction]]
- [[Template Filling]]
