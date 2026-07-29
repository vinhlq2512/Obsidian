---
type: reading-section
book: "[[Natural Language Processing with Transformers]]"
status: planned
chapter: 7
start_page: 195
end_page: 233
reading_date: 2026-08-01
planned_sessions:
  - "2026-08-01 | 195-214 | Extractive QA và cách model tìm span trả lời | 55 phút"
  - "2026-08-02 | 215-233 | Retriever-reader pipeline, evaluation và tóm tắt | 55 phút"
estimated_minutes: 80
actual_minutes:
need_review: false
tags:
  - nlp
  - question-answering
  - retrieval
---

# NLP Transformers - Chapter 07 - Question Answering

## Mục tiêu đọc

- Hiểu extractive QA và review-based QA system.
- Nắm vai trò của retriever và reader.
- Biết cách đánh giá từng phần trong QA pipeline.

## Ý chính

- Extractive QA tìm span trả lời trong context có sẵn.
- Retriever chọn tài liệu liên quan, reader trích câu trả lời từ tài liệu đó.
- Đánh giá QA nên tách retriever, reader và pipeline tổng thể.

## Demo thực hành

Chạy extractive QA trên context tự viết.

```python
from transformers import pipeline

qa = pipeline("question-answering")

context = """
Hugging Face provides the Transformers library for working with pretrained models.
It also provides Datasets for loading and processing datasets, and the Hub for
sharing models, datasets, and demos with the community.
"""

questions = [
    "What library is used for pretrained models?",
    "What is the Hub used for?",
]

for question in questions:
    print(qa(question=question, context=context))
```

## Khái niệm quan trọng

- [[Question Answering]]
- [[Extractive QA]]
- [[Retriever]]
- [[Reader]]
- [[Domain Adaptation]]

## Active Recall

1. Extractive QA bị giới hạn bởi điều gì?
2. Retriever sai thì reader còn cứu được không?
3. Exact match và F1 trong QA đo gì?
4. Domain adaptation giúp QA pipeline như thế nào?

## Checklist

- [ ] Đọc xong chapter
- [ ] Chạy demo QA
- [ ] Ghi lại câu hỏi model trả lời sai
- [ ] Tách concept cần dùng lại
- [ ] Cập nhật tiến độ sách
