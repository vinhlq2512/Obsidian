---
type: concept
status: seed
source:
  - "[[NLP Transformers - Chapter 04 - Multilingual Named Entity Recognition]]"
  - "[[28-07-2026]]"
tags:
  - concept
  - transformer
  - nlp
  - multilingual
---

# Multilingual Transformer

## Định nghĩa

Multilingual Transformer là Transformer được pretrain trên dữ liệu của nhiều ngôn ngữ để học representation có thể dùng lại cho các task đa ngôn ngữ, ví dụ classification, NER, retrieval hoặc translation-related tasks.

## Cách hiểu bằng lời của tôi

Thay vì train một model riêng cho từng ngôn ngữ, ta dùng một model chung học từ nhiều ngôn ngữ. Model cố gắng đặt token, cụm từ và ngữ cảnh có chức năng tương tự vào một không gian biểu diễn gần nhau hơn, nhờ đó kiến thức học từ ngôn ngữ có nhiều dữ liệu có thể hỗ trợ ngôn ngữ ít dữ liệu.

Trong chapter NER đa ngôn ngữ, ý chính là multilingual Transformer như XLM-R có thể làm nền cho [[Cross-Lingual Transfer]]: fine-tune trên source language có nhãn, rồi đánh giá hoặc áp dụng trên target language.

## Mental model

```text
nhiều ngôn ngữ -> shared tokenizer + shared Transformer -> shared representation space
```

Nếu representation đủ chia sẻ, model có thể nhận ra một số pattern như tên người, tổ chức, địa điểm qua nhiều ngôn ngữ mà không cần train riêng cho từng ngôn ngữ.

## Khi áp dụng

- Dùng khi cần hỗ trợ nhiều ngôn ngữ nhưng không có đủ dữ liệu gán nhãn cho từng ngôn ngữ.
- Hữu ích cho [[Zero-shot Learning|zero-shot transfer]] và few-shot transfer trong các ngôn ngữ ít tài nguyên.
- Phù hợp với task understanding như [[Named Entity Recognition]], token classification, text classification và semantic retrieval.

## Cần biết

- Tokenizer rất quan trọng: nếu một ngôn ngữ bị tách thành quá nhiều subword, input dài hơn và nhãn token-level khó align hơn.
- Không phải ngôn ngữ nào cũng được hưởng lợi như nhau; ngôn ngữ ít xuất hiện trong pretraining hoặc khác domain có thể yếu hơn.
- Cần đánh giá theo từng ngôn ngữ và từng entity type, thay vì chỉ nhìn một điểm trung bình.
- Multilingual model thường đánh đổi giữa độ phủ nhiều ngôn ngữ và capacity dành riêng cho một ngôn ngữ.

## Liên kết

- [[Transformer]]
- [[Transfer Learning]]
- [[Zero-shot Learning]]
- [[Named Entity Recognition]]
- [[NLP Transformers - Chapter 04 - Multilingual Named Entity Recognition]]
