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
---

# Extractive QA

## Định nghĩa

Extractive QA là dạng question answering trong đó model trả lời bằng cách chọn một span nằm sẵn trong context, thường được mô hình hóa như [[Span Classification]].

## Cách hiểu bằng lời của tôi

Model không tự viết câu trả lời mới. Nó đọc `question + context`, rồi dự đoán vị trí token bắt đầu và token kết thúc của answer trong context. Bước biến vị trí token thành câu trả lời cuối cùng nằm ở [[Extracting Answers from Text]].

```text
question + context
-> tokenize pair
-> [[Span Classification|score start/end positions]]
-> choose answer span
```

## Cần biết

- Nếu context không chứa đáp án, extractive QA khó trả lời đúng.
- Context dài cần chia thành nhiều window vì model có giới hạn input length.
- Đánh giá thường dùng exact match và token-level F1.
- Trong hệ thống nhiều tài liệu, extractive QA thường cần [[Retriever]] phía trước.
- [[Reader]] thường dùng span classification để tìm answer span sau khi đã có context phù hợp.
- Tokenizer offset giúp map answer span từ token index về chuỗi text gốc.

## Liên kết

- [[Question Answering]]
- [[Extracting Answers from Text]]
- [[Span Classification]]
- [[Retriever]]
- [[Reader]]
- [[NLP Transformers - Chapter 07 - Question Answering]]
