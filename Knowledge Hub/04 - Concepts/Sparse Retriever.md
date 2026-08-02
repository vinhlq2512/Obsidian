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
  - nlp
  - retrieval
  - question-answering
---

# Sparse Retriever

## Định nghĩa

Sparse retriever là retriever biểu diễn query và document bằng vector thưa dựa trên từ khóa/term, rồi xếp hạng document theo mức overlap lexical với query.

## Cách hiểu bằng lời của tôi

Sparse retriever giống tìm kiếm từ khóa có chấm điểm. Nó hỏi: document nào chứa các từ quan trọng trong query, đặc biệt là những từ hiếm và phân biệt tốt?

```text
query text
-> tách thành terms
-> so với term index của documents
-> tính relevance score
-> trả về top-k passages
```

## Phần cần biết

- Vector gọi là "sparse" vì mỗi document chỉ có giá trị ở một số term trong vocabulary rất lớn.
- [[BM25]] là baseline phổ biến cho sparse retrieval.
- Sparse retriever nhanh, dễ debug và hoạt động tốt khi query/document có overlap từ khóa rõ.
- Nó yếu hơn dense retrieval khi query và document dùng từ khác nhau nhưng cùng nghĩa.
- Trong QA pipeline, sparse retriever quyết định passage nào được đưa sang [[Reader]].

## Ví dụ trực quan

```text
Query: "battery life good?"
Review A: "battery lasts two days"        -> match tốt
Review B: "power endurance is excellent" -> cùng nghĩa nhưng ít overlap từ khóa
```

Sparse retriever dễ tìm Review A hơn Review B.

## Khi áp dụng

- Dùng làm baseline đầu tiên cho [[Building a Review-Based QA System]].
- Dùng khi corpus lớn và cần retrieval nhanh.
- Dùng khi muốn debug bằng term match thay vì embedding similarity.
- Có thể kết hợp với [[Dense Passage Retrieval]] hoặc reranking để tăng chất lượng top-k.

## Câu hỏi review

1. Vì sao gọi là sparse retriever?
2. Sparse retriever mạnh khi nào?
3. Sparse retriever dễ thất bại trong tình huống nào?

## Gợi ý trả lời câu hỏi review

1. Vì query/document được biểu diễn bằng vector term rất lớn nhưng chỉ có ít chiều khác 0.
2. Khi query và document có overlap từ khóa rõ, hoặc cần baseline nhanh/dễ debug.
3. Khi cùng ý nghĩa nhưng dùng từ khác nhau, paraphrase nhiều, hoặc cần hiểu ngữ nghĩa sâu.

## Liên kết

- [[NLP Transformers - Chapter 07 - Question Answering]]
- [[Question Answering]]
- [[Retriever]]
- [[BM25]]
- [[Dense Passage Retrieval]]
- [[Reader]]
