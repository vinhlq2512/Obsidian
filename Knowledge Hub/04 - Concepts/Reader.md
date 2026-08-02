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

# Reader

## Định nghĩa

Reader là thành phần đọc context hoặc passage đã được chọn và trích câu trả lời cho câu hỏi.

## Cách hiểu bằng lời của tôi

Trong QA pipeline, retriever tìm nơi có thể có đáp án, còn reader tìm chính xác đoạn trả lời trong nơi đó, thường bằng [[Span Classification]].

```text
question + retrieved passage
-> reader model
-> answer span + score
```

## Cần biết

- Reader thường hoạt động như [[Extractive QA]]: dự đoán start/end span.
- Reader tốt vẫn thất bại nếu [[Retriever]] không đưa passage chứa đáp án vào.
- Cần [[Evaluating the Reader|đánh giá reader]] riêng với context đúng, và đánh giá pipeline tổng thể với retrieval thật.
- Reader thường được đánh giá bằng [[Exact Match]] và [[F1 Score]].
- Khi debug reader, nên xem span được chọn có nằm đúng trong context và có bị lệch biên token không.
- Trong [[Using Haystack to Build a QA Pipeline]], reader nhận các passage do retriever chọn và trả về answer span kèm score.

## Liên kết

- [[Question Answering]]
- [[Extractive QA]]
- [[Evaluating the Reader]]
- [[Exact Match]]
- [[F1 Score]]
- [[Span Classification]]
- [[Retriever]]
- [[Using Haystack to Build a QA Pipeline]]
- [[NLP Transformers - Chapter 07 - Question Answering]]
