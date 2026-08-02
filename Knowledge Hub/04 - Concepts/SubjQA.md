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

# SubjQA

## Định nghĩa

SubjQA là dataset question answering gồm hơn 10,000 customer reviews tiếng Anh trên nhiều domain như TripAdvisor, Restaurants, Movies, Books, Electronics và Grocery.

## Cách hiểu bằng lời của tôi

SubjQA dùng review làm nguồn context. Mỗi ví dụ có câu hỏi và một review, trong đó câu trả lời có thể là một hoặc nhiều span nằm trong review.

```text
product review
+ question
-> answer text + answer_start
```

## Vì sao dataset này khó

- Nhiều câu hỏi và câu trả lời mang tính chủ quan.
- Query có thể dùng cách diễn đạt không xuất hiện nguyên văn trong review.
- Review là user-generated content nên thường nhiễu, ngắn, informal và thiếu cấu trúc.
- Dataset tương đối nhỏ, nên phản ánh tình huống thực tế: label QA chất lượng cao thường đắt và khó tạo.

## Khi áp dụng

- Dùng để benchmark [[Building a Review-Based QA System]].
- Phù hợp để kiểm tra [[Extractive QA]] trên dữ liệu review thực tế hơn Wikipedia.
- Dùng để quan sát vì sao [[Domain Adaptation]] quan trọng với QA.

## Câu hỏi review

1. SubjQA khác SQuAD ở điểm nào?
2. Vì sao subjective answers làm QA khó hơn factual answers?
3. Vì sao keyword search có thể thất bại trên SubjQA?

## Gợi ý trả lời câu hỏi review

1. SubjQA dựa trên customer reviews và nhiều câu trả lời chủ quan; SQuAD dựa nhiều trên Wikipedia và factual reading comprehension.
2. Vì câu trả lời phụ thuộc trải nghiệm/ngữ cảnh của người review, không chỉ là một fact cố định.
3. Vì query và review có thể dùng từ khác nhau; ý trong query như "poor quality" có thể không xuất hiện trực tiếp trong review.

## Liên kết

- [[NLP Transformers - Chapter 07 - Question Answering]]
- [[Question Answering]]
- [[Building a Review-Based QA System]]
- [[Extractive QA]]
- [[Domain Adaptation]]
- [[SQuAD]]
