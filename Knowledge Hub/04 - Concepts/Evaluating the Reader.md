---
type: concept
status: seed
sources:
  - "[[NLP Transformers - Chapter 07 - Question Answering]]"
source_sections:
  - "[[NLP Transformers - Chapter 07 - Question Answering]]"
first_seen: 2026-08-02
last_updated: 2026-08-02
created_at: 2026-08-02
updated_at: 2026-08-02
tags:
  - concept
  - evaluation
  - question-answering
---

# Evaluating the Reader

## Định nghĩa

Evaluating the reader là bước đo xem [[Reader]] có trích đúng answer span từ passage đã cho hay không.

## Cách hiểu bằng lời của tôi

Sau khi retriever đưa passage đến, reader phải chọn đoạn trả lời. Evaluation reader hỏi: "Nếu có context, model có gạch chân đúng answer không?"

```text
question + passage
-> reader predicts answer span
-> compare with labels
-> EM / F1
```

## Metric chính

- [[Exact Match]]: prediction khớp chính xác với label.
- [[F1 Score]]: prediction overlap token với label đến mức nào.

## Khi áp dụng

- Dùng để đánh giá [[Extractive QA]] reader khi context đã được cung cấp.
- Dùng để tách lỗi reader khỏi lỗi [[Retriever]].
- Dùng để kiểm tra model fine-tuned trên [[SQuAD]] có generalize sang [[SubjQA]] không.

## Điểm cần cẩn thận

- EM strict nên có thể đánh giá thấp prediction gần đúng.
- F1 mềm hơn nhưng có thể đánh giá cao câu trả lời overlap token mà sai nghĩa.
- Nếu reader train trên domain khác, kết quả có thể kém và cần [[Domain Adaptation]].

## Câu hỏi review

1. Evaluating reader khác evaluating retriever ở điểm nào?
2. EM và F1 bổ sung nhau ra sao?
3. Vì sao reader fine-tuned trên SQuAD có thể kém trên SubjQA?

## Gợi ý trả lời câu hỏi review

1. Retriever evaluation đo khả năng lấy passage đúng; reader evaluation đo khả năng trích answer đúng từ passage.
2. EM strict, F1 mềm theo overlap token; dùng cả hai giúp nhìn cân bằng hơn.
3. Vì SubjQA có review informal và subjective, khác domain Wikipedia/factual của SQuAD.

## Liên kết

- [[NLP Transformers - Chapter 07 - Question Answering]]
- [[Reader]]
- [[Exact Match]]
- [[F1 Score]]
- [[SQuAD]]
- [[SubjQA]]
- [[Domain Adaptation]]
- [[Evaluating the Retriever]]
