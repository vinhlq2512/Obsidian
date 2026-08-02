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
  - retrieval
  - question-answering
---

# Retriever

## Định nghĩa

Retriever là thành phần tìm các tài liệu hoặc passage liên quan nhất với câu hỏi trước khi hệ thống đọc và trả lời.

## Cách hiểu bằng lời của tôi

Retriever giống bước "lọc ngữ cảnh". Nếu nó không đưa đúng tài liệu vào top kết quả, [[Reader]] gần như không có cơ hội trích đúng câu trả lời.

## Cần biết

- Retriever thường được đánh giá bằng [[Recall@k]] hoặc các metric ranking như [[Mean Average Precision]].
- [[Sparse Retriever|Sparse retrieval]] dựa nhiều vào overlap từ khóa; [[BM25]] là baseline phổ biến cho hướng này.
- [[Dense Passage Retrieval|Dense retrieval]] biểu diễn query/document bằng vector để tìm gần nhau về ngữ nghĩa.
- Trong [[Building a Review-Based QA System]], retriever chọn những review có khả năng chứa đáp án.
- Trong [[Using Haystack to Build a QA Pipeline]], retriever là component lấy top-k passage từ DocumentStore trước khi đưa sang reader.
- Trong QA pipeline, retriever đặt upper bound: nếu nó không đưa passage chứa đáp án vào top-k, reader không thể trích đúng answer từ bằng chứng bị thiếu.

## Liên kết

- [[Question Answering]]
- [[Evaluating the Retriever]]
- [[Recall@k]]
- [[Mean Average Precision]]
- [[Sparse Retriever]]
- [[Dense Passage Retrieval]]
- [[BM25]]
- [[Reader]]
- [[Using Haystack to Build a QA Pipeline]]
- [[Semantic Search]]
- [[Vector Database]]
- [[Retrieval-Augmented Generation]]
- [[NLP Transformers - Chapter 07 - Question Answering]]
