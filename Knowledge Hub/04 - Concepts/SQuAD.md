---
type: concept
status: seed
sources:
  - "[[NLP Transformers - Chapter 07 - Question Answering]]"
source_sections:
  - "[[NLP Transformers - Chapter 07 - Question Answering]]"
first_seen: 2026-08-01
last_updated: 2026-08-02
created_at: 2026-08-02
updated_at: 2026-08-02
tags:
  - concept
  - nlp
  - question-answering
  - dataset
---

# SQuAD

## Định nghĩa

SQuAD là benchmark extractive question answering dùng các đoạn văn Wikipedia, trong đó model phải đọc passage và trả lời câu hỏi bằng một span trong passage.

## Cách hiểu bằng lời của tôi

SQuAD là "bài kiểm tra đọc hiểu" cho model QA: đưa một đoạn Wikipedia và một câu hỏi, model phải tìm đoạn chữ đúng để trả lời.

```text
Wikipedia paragraph
+ question
-> answer span
```

## Phần cần biết

- SQuAD 1.1 đảm bảo câu trả lời tồn tại trong passage.
- SQuAD 2.0 thêm các câu hỏi không thể trả lời từ passage để làm bài toán khó hơn.
- Model có thể đạt điểm rất cao trên SQuAD nhưng chưa chắc hiểu đọc theo nghĩa rộng.
- Hiệu năng tốt trên SQuAD có thể không chuyển tốt sang domain khác như [[SubjQA]].

## Khi áp dụng

- Dùng làm benchmark và pretrained/fine-tuned checkpoint cho [[Extractive QA]].
- Dùng để hiểu các metric reader như exact match và token-level F1.
- Dùng làm điểm khởi đầu trước khi làm [[Domain Adaptation]] sang dữ liệu chuyên biệt.

## Câu hỏi review

1. SQuAD 2.0 khác SQuAD 1.1 ở điểm nào?
2. Vì sao model giỏi SQuAD có thể yếu trên SubjQA?
3. SQuAD đo năng lực nào của model QA?

## Gợi ý trả lời câu hỏi review

1. SQuAD 2.0 có thêm câu hỏi không thể trả lời từ passage.
2. Vì SubjQA là review chủ quan, informal và khác Wikipedia; model có thể overfit vào pattern của SQuAD.
3. Nó đo khả năng đọc passage và trích answer span cho câu hỏi.

## Liên kết

- [[NLP Transformers - Chapter 07 - Question Answering]]
- [[Question Answering]]
- [[Extractive QA]]
- [[SubjQA]]
- [[Domain Adaptation]]
