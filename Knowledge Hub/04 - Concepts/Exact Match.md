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

# Exact Match

## Định nghĩa

Exact Match, viết tắt là EM, là metric đánh giá extractive QA bằng cách kiểm tra prediction có khớp chính xác với answer label hay không.

## Cách hiểu bằng lời của tôi

EM rất nghiêm khắc: chỉ cần model thêm hoặc thiếu một token quan trọng thì điểm có thể về 0.

```text
prediction: "about 6000 hours"
label:      "6000 hours"
EM: 0
```

## Phần cần biết

- EM thường được tính sau một số bước normalize như lowercase, bỏ punctuation và chuẩn hóa whitespace.
- Nếu câu hỏi không có answer nhưng model vẫn dự đoán text, EM = 0.
- EM dễ đánh giá thiếu công bằng khi prediction gần đúng nhưng không khớp tuyệt đối.
- Vì EM quá strict, nên thường theo dõi cùng [[F1 Score]].

## Khi áp dụng

- Dùng để đánh giá [[Reader]] trong [[Extractive QA]].
- Hợp khi answer cần đúng chính xác, ví dụ tên, số, ngày tháng.
- Nên dùng cùng F1 để thấy mức overlap token khi prediction gần đúng.

## Câu hỏi review

1. Exact Match đo gì?
2. Vì sao EM nghiêm khắc hơn F1?
3. Khi nào EM hữu ích?

## Gợi ý trả lời câu hỏi review

1. Nó đo prediction có khớp chính xác với ground truth answer hay không.
2. Vì chỉ cần thêm/thiếu token cũng có thể làm điểm về 0, còn F1 đo overlap token.
3. Khi cần câu trả lời chính xác tuyệt đối hoặc muốn metric dễ diễn giải.

## Liên kết

- [[NLP Transformers - Chapter 07 - Question Answering]]
- [[Evaluating the Reader]]
- [[F1 Score]]
- [[Reader]]
- [[Extractive QA]]
