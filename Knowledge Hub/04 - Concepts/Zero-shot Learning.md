---
type: concept
status: seed
source:
  - "[[NLP Transformers - Chapter 04 - Multilingual Named Entity Recognition]]"
  - "[[28-07-2026]]"
tags:
  - concept
  - machine-learning
  - nlp
---

# Zero-shot Learning

## Định nghĩa

Zero-shot learning là khả năng dùng model cho một task, nhãn, domain hoặc ngôn ngữ mới mà không có ví dụ huấn luyện có nhãn trực tiếp cho trường hợp đó.

## Cách hiểu bằng lời của tôi

Model không học từ dữ liệu gán nhãn của tình huống mới, mà dựa vào tri thức hoặc representation đã học trước đó. Trong NLP với Transformer, điều này thường đến từ pretraining lớn, multilingual representation, instruction tuning, hoặc cách diễn đạt task bằng ngôn ngữ tự nhiên.

Trong chapter multilingual NER, zero-shot transfer nghĩa là fine-tune model trên một ngôn ngữ nguồn có nhãn, rồi áp dụng trực tiếp sang ngôn ngữ đích chưa có nhãn NER.

## Công thức trực giác

```text
pretrain đa ngôn ngữ -> fine-tune trên source language -> predict trên target language chưa có nhãn
```

Nếu representation của hai ngôn ngữ đủ gần nhau, model có thể chuyển một phần năng lực nhận diện thực thể từ ngôn ngữ nguồn sang ngôn ngữ đích.

## Ví dụ trực quan

- Fine-tune XLM-R cho NER bằng dữ liệu tiếng Anh.
- Không fine-tune thêm bằng dữ liệu tiếng Việt.
- Đưa câu tiếng Việt vào model và kiểm tra model có nhận ra người, tổ chức, địa điểm hay không.

## Cần biết

- Zero-shot không có nghĩa là không cần dữ liệu nào cả; model thường đã được pretrain trên dữ liệu lớn.
- Hiệu quả phụ thuộc vào độ gần giữa source và target, chất lượng tokenizer, domain, nhãn cần dự đoán và dữ liệu pretraining.
- Trong multilingual NLP, zero-shot transfer là chiến lược mạnh khi target language thiếu dữ liệu gán nhãn.
- Cần đánh giá bằng metric thực tế, vì representation chung không đảm bảo mọi entity type đều transfer tốt.

## Liên kết

- [[Transfer Learning]]
- [[Named Entity Recognition]]
- [[Natural Language Processing with Transformers]]
- [[NLP Transformers - Chapter 04 - Multilingual Named Entity Recognition]]
