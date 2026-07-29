---
type: reading-section
book: "[[Natural Language Processing with Transformers]]"
status: planned
chapter: 6
start_page: 164
end_page: 194
reading_date: 2026-07-30
planned_sessions:
  - "2026-07-30 | 164-179 | Abstractive summarization, baseline và metric | 50 phút"
  - "2026-07-31 | 180-194 | Fine-tuning summarization và viết lại quy trình | 50 phút"
estimated_minutes: 75
actual_minutes:
need_review: false
tags:
  - nlp
  - summarization
  - evaluation
---

# NLP Transformers - Chapter 06 - Summarization

## Mục tiêu đọc

- Hiểu abstractive summarization và các baseline.
- Biết so sánh summary bằng BLEU và ROUGE.
- Nắm workflow fine-tune model summarization như PEGASUS.

## Ý chính

- Summary tốt không chỉ ngắn mà còn phải giữ thông tin cốt lõi.
- BLEU thường dùng cho translation, ROUGE phổ biến hơn cho summarization.
- Fine-tuning trên domain cụ thể giúp summary sát ngữ cảnh hơn.

## Demo thực hành

Tóm tắt một đoạn dài và đánh giá nhanh bằng ROUGE.

```python
from transformers import pipeline

summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

article = """
Transformers have become a standard architecture for natural language processing.
They are used for classification, question answering, summarization, translation,
and text generation. The Hugging Face ecosystem provides tools that make it easier
to load datasets, tokenize text, fine-tune models, and share trained models.
"""

summary = summarizer(article, max_length=45, min_length=15, do_sample=False)
print(summary[0]["summary_text"])
```

## Khái niệm quan trọng

- [[Summarization]]
- [[Abstractive Summarization]]
- [[BLEU]]
- [[ROUGE]]
- [[PEGASUS]]

## Active Recall

1. Extractive và abstractive summarization khác nhau thế nào?
2. ROUGE đo điều gì?
3. Vì sao metric tự động không đủ để đánh giá summary?
4. Khi fine-tune summarizer cần chú ý gì về input length?

## Checklist

- [ ] Đọc xong chapter
- [ ] Chạy demo summarization
- [ ] So sánh summary với bản tự viết
- [ ] Tách concept cần dùng lại
- [ ] Cập nhật tiến độ sách
