---
type: reading-section
book: "[[Natural Language Processing with Transformers]]"
status: planned
chapter: 4
start_page: 119
end_page: 149
reading_date: 2026-07-28
planned_sessions:
  - "2026-07-28 | 119-149 | NER, token-level labels và cross-lingual transfer | 60 phút"
estimated_minutes: 75
actual_minutes:
need_review: false
tags:
  - nlp
  - ner
  - multilingual
---

# NLP Transformers - Chapter 04 - Multilingual Named Entity Recognition

## Mục tiêu đọc

- Hiểu bài toán Named Entity Recognition.
- Biết cách tokenization ảnh hưởng đến nhãn token-level.
- Nắm ý tưởng cross-lingual transfer với multilingual Transformer.

## Ý chính

- NER là bài toán gán nhãn thực thể cho từng token hoặc span.
- Khi tokenizer tách một từ thành nhiều subword, nhãn cần được căn chỉnh lại.
- Multilingual model như XLM-R có thể transfer giữa các ngôn ngữ nếu representation đủ chia sẻ.

## Demo thực hành

Chạy NER đa ngôn ngữ bằng pipeline.

```python
from transformers import pipeline

ner = pipeline(
    "ner",
    model="Davlan/xlm-roberta-base-ner-hrl",
    aggregation_strategy="simple",
)

texts = [
    "Hugging Face is based in New York City.",
    "Nguyễn Nhật Ánh sinh tại Quảng Nam.",
]

for text in texts:
    print(text)
    print(ner(text))
```

## Khái niệm quan trọng

- [[Named Entity Recognition]]
- [[Token Classification]]
- [[SentencePiece]]
- [[Cross-Lingual Transfer]]
- [[XLM-RoBERTa]]

## Active Recall

1. NER khác text classification ở điểm nào?
2. Vì sao token-level labels khó hơn sequence-level labels?
3. Zero-shot transfer nên dùng khi nào?
4. Error analysis trong NER nên nhìn những lỗi nào?

## Checklist

- [ ] Đọc xong chapter
- [ ] Chạy demo NER
- [ ] Ghi lại ví dụ tiếng Việt đúng/sai
- [ ] Tách concept cần dùng lại
- [ ] Cập nhật tiến độ sách
