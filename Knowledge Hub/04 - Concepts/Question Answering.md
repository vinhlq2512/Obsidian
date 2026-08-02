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

# Question Answering

## Định nghĩa

Question answering là bài toán nhận một câu hỏi và tìm hoặc sinh câu trả lời dựa trên context, tài liệu, hoặc một collection văn bản.

## Cách hiểu bằng lời của tôi

QA không chỉ là "model biết trả lời". Trong workflow thực tế, hệ thống phải tìm đúng context, hiểu câu hỏi, trích hoặc sinh câu trả lời, rồi đánh giá xem câu trả lời có đúng và grounded không.

## Hai hướng chính

- **Extractive QA**: trích span trả lời trực tiếp từ context.
- **Retrieval-based QA**: tìm tài liệu liên quan trước, sau đó dùng reader/model để lấy câu trả lời.

## Cần biết

- [[Extractive QA]] bị giới hạn bởi context được đưa vào model.
- [[Retriever]] quyết định tài liệu nào được đưa tới bước đọc.
- [[Reader]] chỉ có thể trả lời tốt nếu context chứa câu trả lời.
- [[Building a Review-Based QA System]] là một ứng dụng thực tế của QA trên nhiều review/tài liệu.

## Liên kết

- [[NLP Transformers - Chapter 07 - Question Answering]]
- [[Extractive QA]]
- [[Retriever]]
- [[Reader]]
- [[Building a Review-Based QA System]]
