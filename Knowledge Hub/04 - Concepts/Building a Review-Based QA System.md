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
  - retrieval
---

# Building a Review-Based QA System

## Định nghĩa

Building a review-based QA system là workflow xây hệ thống trả lời câu hỏi dựa trên nhiều review, trong đó hệ thống tìm review liên quan rồi trích câu trả lời từ nội dung review.

## Cách hiểu bằng lời của tôi

Bài toán không phải chỉ đưa một đoạn context ngắn cho model. Review-based QA giống một pipeline:

```text
user question
-> retrieve relevant reviews
-> reader extracts answer span
-> rank answers
-> return answer with supporting review
```

Nếu retriever chọn sai review, reader dù mạnh cũng không có đủ bằng chứng để trả lời đúng.

## Thành phần chính

- **Review corpus**: tập review làm nguồn tri thức.
- **Question**: câu hỏi người dùng muốn trả lời từ review.
- **Retriever**: chọn review/passage liên quan nhất.
- **Reader**: đọc passage và trích answer span.
- **Answer ranking**: chọn câu trả lời tốt nhất khi có nhiều passage ứng viên.
- **Evaluation**: tách lỗi retrieval, lỗi reader và lỗi pipeline tổng thể.

## Cần biết

- Đây là ứng dụng của [[Question Answering]] trên nhiều tài liệu ngắn và nhiễu.
- [[Extractive QA]] phù hợp khi câu trả lời xuất hiện trực tiếp trong review.
- [[Retriever]] quyết định recall: đáp án có nằm trong top-k review được đưa cho reader không?
- [[Reader]] quyết định extraction: từ review đúng, nó có tìm đúng span trả lời không?
- [[Domain Adaptation]] có thể cần thiết vì review có văn phong riêng, nhiều ý kiến chủ quan và thiếu cấu trúc.

## Khi áp dụng

- Hỏi đáp trên product reviews, customer feedback, support tickets hoặc survey comments.
- Cần câu trả lời có grounding vào review cụ thể.
- Muốn phân tích nhiều tài liệu ngắn thay vì một context duy nhất.

## Điểm dễ lỗi

- Retriever bỏ lỡ review chứa đáp án.
- Reader trích span đúng cú pháp nhưng không thật sự trả lời câu hỏi.
- Review chứa nhiều ý chủ quan hoặc mâu thuẫn nhau.
- Câu hỏi cần tổng hợp nhiều review, nhưng extractive reader chỉ trích được một span.

## Câu hỏi review

1. Vì sao review-based QA cần cả retriever và reader?
2. Retriever sai thì reader còn cứu được không?
3. Khi nào extractive QA không đủ cho review-based QA?

## Gợi ý trả lời câu hỏi review

1. Vì có nhiều review; retriever lọc review liên quan, reader trích câu trả lời từ review đã lọc.
2. Thường là không, vì reader chỉ đọc passage được đưa vào. Nếu passage không chứa đáp án, reader sẽ đoán hoặc trả lời sai.
3. Khi câu hỏi cần tổng hợp nhiều review, cần suy luận ngoài một span, hoặc các review mâu thuẫn nhau.

## Liên kết

- [[NLP Transformers - Chapter 07 - Question Answering]]
- [[Question Answering]]
- [[Extractive QA]]
- [[Retriever]]
- [[Reader]]
- [[Domain Adaptation]]
- [[Retrieval-Augmented Generation]]
