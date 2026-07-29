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
- [[Tokenizer Pipeline]] gồm normalization, pretokenization, tokenizer model và postprocessing; mỗi bước đều có thể ảnh hưởng đến token IDs, offsets và alignment nhãn.
- Khi tokenizer tách một từ thành nhiều subword, nhãn cần được căn chỉnh lại.
- [[SentencePiece]] hữu ích cho multilingual Transformer vì nó học subword từ raw text và ít phụ thuộc vào quy ước tách từ bằng khoảng trắng.
- [[Multilingual Transformer]] như XLM-R có thể transfer giữa các ngôn ngữ nếu representation đủ chia sẻ.
- Multilingual Transformer học từ nhiều ngôn ngữ bằng shared tokenizer và shared model parameters, nên có thể tạo một representation space chung cho các pattern ngôn ngữ tương tự.
- [[Zero-shot Learning]] trong chapter này nên hiểu như zero-shot cross-lingual transfer: model được fine-tune trên ngôn ngữ nguồn có nhãn NER, rồi áp dụng trực tiếp sang ngôn ngữ đích không có nhãn.
- Zero-shot transfer hữu ích khi target language ít dữ liệu, nhưng cần kiểm tra lỗi theo entity type, tokenizer và domain vì representation chung không đảm bảo transfer đều cho mọi ngôn ngữ.

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
- [[Tokenizer Pipeline]]
- [[SentencePiece]]
- [[Cross-Lingual Transfer]]
- [[Multilingual Transformer]]
- [[Zero-shot Learning]]
- [[XLM-RoBERTa]]

## Active Recall

1. NER khác text classification ở điểm nào?
2. Vì sao token-level labels khó hơn sequence-level labels?
3. Tokenizer pipeline gồm những bước nào và mỗi bước làm gì?
4. SentencePiece tokenizer làm thay đổi cách align nhãn NER như thế nào?
5. Zero-shot transfer nên dùng khi nào?
6. Error analysis trong NER nên nhìn những lỗi nào?

## Checklist

- [ ] Đọc xong chapter
- [ ] Chạy demo NER
- [ ] Ghi lại ví dụ tiếng Việt đúng/sai
- [ ] Tách concept cần dùng lại
- [ ] Cập nhật tiến độ sách
