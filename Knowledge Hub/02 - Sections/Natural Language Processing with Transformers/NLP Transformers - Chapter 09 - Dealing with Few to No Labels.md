---
type: reading-section
book: "[[Natural Language Processing with Transformers]]"
status: planned
chapter: 9
start_page: 286
end_page: 325
reading_date: 2026-08-05
planned_sessions:
  - "2026-08-05 | 286-305 | Baseline, ít nhãn và embedding lookup | 55 phút"
  - "2026-08-06 | 306-325 | Prompting, augmentation, unlabeled data và viết lại chiến lược | 55 phút"
estimated_minutes: 90
actual_minutes:
need_review: false
tags:
  - nlp
  - few-shot
  - weak-supervision
---

# NLP Transformers - Chapter 09 - Dealing with Few to No Labels

## Mục tiêu đọc

- Hiểu các chiến lược khi thiếu nhãn dữ liệu.
- Biết dùng baseline đơn giản trước khi fine-tune Transformer.
- Nắm data augmentation, embeddings lookup, prompts và tận dụng unlabeled data.

## Ý chính

- Khi ít nhãn, baseline đơn giản giúp biết Transformer có thật sự cần thiết không.
- Embeddings có thể dùng như lookup table để tìm ví dụ gần nhau.
- Unlabeled data vẫn có giá trị thông qua language model fine-tuning hoặc semi-supervised methods.

## Demo thực hành

Zero-shot classification khi chưa có dữ liệu gán nhãn.

```python
from transformers import pipeline

classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

texts = [
    "The app crashes whenever I try to upload a file.",
    "Please add dark mode to the dashboard.",
]

labels = ["bug", "feature request", "question", "documentation"]

for text in texts:
    result = classifier(text, candidate_labels=labels)
    print(text)
    print(list(zip(result["labels"], result["scores"])))
```

## Khái niệm quan trọng

- [[Few-shot Learning]]
- [[Zero-shot Classification]]
- [[Data Augmentation]]
- [[Embeddings]]
- [[Semi-supervised Learning]]

## Active Recall

1. Khi ít nhãn, vì sao nên làm baseline trước?
2. Zero-shot classification dựa trên giả định gì?
3. Data augmentation có thể làm hỏng dữ liệu ra sao?
4. Unlabeled data giúp được gì cho classifier?

## Checklist

- [ ] Đọc xong chapter
- [ ] Chạy demo zero-shot classification
- [ ] Nghĩ một use case cá nhân có ít nhãn
- [ ] Tách concept cần dùng lại
- [ ] Cập nhật tiến độ sách
