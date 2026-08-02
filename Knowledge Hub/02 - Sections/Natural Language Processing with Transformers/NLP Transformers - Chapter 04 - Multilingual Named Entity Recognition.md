---
type: reading-section
book: "[[Natural Language Processing with Transformers]]"
status: completed
chapter: 4
start_page: 119
end_page: 149
reading_date: 2026-07-28
planned_sessions:
  - "2026-07-28 | 119-149 | NER, token-level labels và cross-lingual transfer | 60 phút"
estimated_minutes: 75
actual_minutes: 60
need_review: true
review_date: 2026-08-04
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
- [[Tokenizing Texts for NER]] cần giữ mapping từ subword về word gốc bằng `word_ids()` hoặc offsets, rồi dùng `-100` cho special tokens/subword phụ nếu không muốn tính loss.
- [[Transformers Model Class]] trong Hugging Face tách pretrained body khỏi task-specific head; với NER, token classification head dự đoán logits cho từng token/subword.
- [[Custom Model for Token Classification]] giúp hiểu rõ cách ghép pretrained body, dropout, linear classifier, loss và output chuẩn để fine-tune NER.
- [[Loading a Custom Model]] là bước nạp pretrained checkpoint vào custom class bằng `from_pretrained()`, trong đó body nhận pretrained weights còn head mới có thể được khởi tạo lại.
- [[Performance Measures for NER]] nên ưu tiên entity-level precision, recall và F1 thay vì chỉ nhìn token accuracy, nhất là khi nhãn `O` chiếm đa số.
- [[Fine-Tuning XLM-RoBERTa]] kết hợp tokenizer XLM-R, label alignment, token classification head, `Trainer` và `seqeval` để train/evaluate NER đa ngôn ngữ.
- [[Error Analysis for NER]] giúp đọc lỗi sau metric: sai ranh giới, sai entity type, false positive/negative, lỗi BIO, lỗi tokenizer/alignment và lỗi theo từng ngôn ngữ.
- [[Cross-Lingual Transfer]] là mục tiêu chính của multilingual NER: dùng dữ liệu/tri thức từ source language để dự đoán hoặc cải thiện performance trên target language.
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
- [[Tokenizing Texts for NER]]
- [[Transformers Model Class]]
- [[Custom Model for Token Classification]]
- [[Loading a Custom Model]]
- [[Performance Measures for NER]]
- [[Fine-Tuning XLM-RoBERTa]]
- [[Error Analysis for NER]]
- [[Cross-Lingual Transfer]]
- [[Multilingual Transformer]]
- [[Zero-shot Learning]]
- [[XLM-RoBERTa]]

## Active Recall

1. NER khác text classification ở điểm nào?
2. Vì sao token-level labels khó hơn sequence-level labels?
3. Tokenizer pipeline gồm những bước nào và mỗi bước làm gì?
4. SentencePiece tokenizer làm thay đổi cách align nhãn NER như thế nào?
5. Khi tokenizing texts for NER, `word_ids()` giúp align label như thế nào?
6. Transformers model class tách body và head như thế nào?
7. Khi tạo custom model cho token classification, `forward()` cần làm những bước nào?
8. Vì sao loss trong NER cần ignore label `-100`?
9. Khi load custom model, cảnh báo head mới chưa được initialize nên hiểu thế nào?
10. Vì sao NER nên dùng entity-level precision/recall/F1 thay vì chỉ accuracy?
11. Fine-tuning XLM-RoBERTa cho NER gồm những bước chính nào?
12. Error analysis trong NER nên nhìn những lỗi nào?
13. Cross-lingual transfer khác zero-shot transfer ở điểm nào?
14. Zero-shot transfer nên dùng khi nào?

## Checklist

- [x] Đọc xong chapter
- [x] Chạy demo NER
- [x] Ghi lại ví dụ tiếng Việt đúng/sai
- [x] Tách concept cần dùng lại
- [x] Cập nhật tiến độ sách
