---
type: reading-section
book: "[[Practical Natural Language Processing]]"
status: planned
chapter: 5
start_page: 293
end_page: 351
reading_date: 2026-08-07
planned_sessions:
  - "2026-08-07 | 293-310 | IE applications, tasks, pipeline, keyphrase, NER mở đầu | 55 phút"
  - "2026-08-08 | 311-330 | NER system, active learning, entity linking, RE mở đầu | 55 phút"
  - "2026-08-09 | 331-351 | Relationship extraction, event extraction, template filling | 55 phút"
tags:
  - nlp
  - practical-nlp
  - information-extraction
---

# Practical NLP - Chapter 05 - Information Extraction

## Mục tiêu cần hiểu

- Information extraction biến text tự do thành thực thể, quan hệ, sự kiện hoặc schema có cấu trúc.
- [[Named Entity Recognition]] chỉ là một phần của IE pipeline.
- Entity linking, relationship extraction và template filling mở rộng NER thành dữ liệu dùng được.

## Định nghĩa quan trọng

- Information extraction
- Keyphrase extraction
- [[Named Entity Recognition]]
- Named entity disambiguation
- Entity linking
- Relationship extraction
- Event extraction
- Template filling

## Mental model

```text
Text thô
-> mention / keyphrase
-> entity
-> entity linking
-> relation / event
-> structured record
```

## Phần cần biết

- Giá trị thực tế của IE nằm ở việc biến văn bản thành dữ liệu có thể query, đo lường, hoặc đưa vào workflow.
- Khi đọc, chú ý ranh giới giữa extraction, disambiguation và linking.

## Câu hỏi review

1. NER khác entity linking ở đâu?
2. Relationship extraction cần thêm thông tin gì so với nhận diện entity?
3. Template filling phù hợp với loại bài toán nào?

## Gợi ý trả lời câu hỏi review

- Dùng ví dụ một hóa đơn, một tin tức hoặc một hồ sơ y tế để chỉ ra entity, relation và event.

## Liên kết

- [[Practical Natural Language Processing]]
- [[Named Entity Recognition]]
