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

# Temporal Information Extraction

## Định nghĩa

Temporal information extraction là task trích các biểu thức thời gian trong text và chuẩn hóa chúng về một dạng thời gian có cấu trúc.

## Cách hiểu bằng lời của tôi

Nếu text nói `today`, `Friday`, `3 p.m.`, hệ thống không chỉ cần nhận ra đó là thời gian mà còn phải đổi chúng về giá trị chuẩn theo ngữ cảnh. Nói cách khác, IE temporal vừa phải “nhìn thấy” thời gian, vừa phải “dịch” nó sang dạng máy dùng được.

## Trong IE

```text
text có time expression
-> extract date/time mention
-> normalize to standard date-time
```

- Practical NLP xem temporal IE và normalization là hai việc đi cùng nhau.
- Extracting date/time có thể làm bằng regex hoặc supervised sequence labeling như NER.
- Normalization khó hơn vì cần map biểu thức tương đối như `today` hoặc `on Friday` sang thời điểm cụ thể dựa trên ngữ cảnh.

## Công cụ

- Duckling là một package được sách nêu ra để parse text và trích temporal events.
- Sách cũng nhắc SUTime, Natty, Parsedatetime và Chronic như các công cụ khác cho human-readable dates and times.
- Duckling hỗ trợ nhiều ngôn ngữ và là điểm khởi đầu thực dụng cho temporal IE.

## Hạn chế

- Biểu thức thời gian phụ thuộc ngữ cảnh, nên normalization không đơn giản như matching string.
- Rule-based và semantic analysis vẫn là hướng chủ đạo trong phần mô tả của sách.
- Nếu text bị nhiễu hoặc thiếu ngữ cảnh, normalization có thể sai ngay cả khi extraction đúng.

## Liên kết

- [[Information Extraction]]
- [[Event Extraction]]
- [[Template Filling]]
