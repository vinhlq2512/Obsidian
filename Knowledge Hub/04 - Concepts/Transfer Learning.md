---
type: concept
status: seed
sources:
  - "[[NLP Transformers - Chapter 01 - Hello Transformers]]"
tags:
  - concept
  - machine-learning
  - nlp
---

# Transfer Learning

## Định nghĩa

Transfer learning là cách dùng lại tri thức đã học từ một bài toán hoặc tập dữ liệu lớn để cải thiện hiệu quả học trên một bài toán mới.

## Cách hiểu bằng lời của tôi

Trong NLP hiện đại, mình thường không bắt đầu từ model rỗng. Model được pretrain trên lượng văn bản lớn để học biểu diễn ngôn ngữ chung, sau đó được fine-tune trên dataset nhỏ hơn cho task cụ thể như phân loại văn bản, NER, QA hoặc summarization.

## Cần biết

- Pretraining học biểu diễn tổng quát từ dữ liệu lớn.
- Fine-tuning điều chỉnh model cho downstream task.
- Transfer learning đặc biệt hữu ích khi dữ liệu có nhãn ít hoặc chi phí train từ đầu quá cao.
- [[Zero-shot Learning]] là một trường hợp transfer khi model được dùng cho task, nhãn, domain hoặc ngôn ngữ mới mà không có dữ liệu gán nhãn trực tiếp cho trường hợp đó.
- [[Cross-Lingual Transfer]] là transfer learning giữa các ngôn ngữ, ví dụ fine-tune NER trên source language rồi đánh giá trên target language.
- Chất lượng transfer phụ thuộc vào độ phù hợp giữa dữ liệu pretraining, domain mới, task mới và metric đánh giá.

## Liên kết

- [[Transformer]]
- [[Fine-tuning]]
- [[Zero-shot Learning]]
- [[Cross-Lingual Transfer]]
- [[NLP Transformers - Chapter 01 - Hello Transformers]]
