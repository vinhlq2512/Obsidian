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
  - embeddings
---

# Dense Passage Retrieval

## Định nghĩa

Dense Passage Retrieval là phương pháp retrieval biểu diễn question và passage bằng dense embeddings, rồi tìm passage gần nhất với question trong vector space.

## Cách hiểu bằng lời của tôi

Dense passage retrieval không chỉ hỏi "có trùng từ không?". Nó encode question và passage thành vector ngữ nghĩa, rồi hỏi: passage nào gần câu hỏi nhất về mặt ý nghĩa?

```text
question -> question encoder -> query vector
passage  -> passage encoder  -> passage vector
similarity(query, passage)
-> top-k passages
```

## Cơ chế chính

- Thường dùng bi-encoder: một encoder cho question, một encoder cho passage.
- Mỗi passage được encode thành embedding và lưu/index trước.
- Khi có query, hệ thống encode query rồi tìm passage vector gần nhất.
- Similarity có thể là dot product hoặc cosine similarity tùy setup.
- Passage top-k được đưa sang [[Reader]] trong QA pipeline.
- Trong Chapter 07, DPR được so sánh với [[BM25]] bằng [[Recall@k]] để xem dense retrieval có đưa passage đúng vào top-k tốt hơn không.

## Khác sparse retrieval

- [[Sparse Retriever]] dựa vào overlap từ khóa.
- Dense passage retrieval dựa vào embedding similarity.
- Dense retrieval có thể bắt được paraphrase hoặc cách diễn đạt khác từ khóa.
- Dense retrieval cần model embedding tốt, index vector và thường tốn compute hơn sparse retrieval.

## Ví dụ trực quan

```text
Query: "Can I use it at night?"
Passage: "The camera works well in low-light conditions."
```

Sparse retriever có thể bỏ lỡ vì ít overlap từ khóa. Dense retriever có cơ hội tìm đúng vì "night" gần nghĩa với "low-light conditions".

## Khi áp dụng

- Dùng khi query và document có thể diễn đạt cùng ý bằng từ khác nhau.
- Dùng cho [[Semantic Search]] và retrieval trong QA/RAG.
- Hữu ích khi muốn giảm số passage đưa vào reader mà vẫn giữ recall tốt.
- Có thể cần [[Domain Adaptation]] hoặc fine-tuning nếu domain khác dữ liệu train ban đầu.
- Nếu dense retriever được train trên domain khác, nó không nhất thiết vượt [[BM25]] trên dataset review như [[SubjQA]].

## Câu hỏi review

1. Dense passage retrieval biểu diễn query và passage như thế nào?
2. Vì sao dense retrieval có thể tốt hơn BM25 với paraphrase?
3. Dense retrieval đánh đổi gì so với sparse retrieval?

## Gợi ý trả lời câu hỏi review

1. Bằng dense embeddings được tạo bởi encoder cho question và passage.
2. Vì nó so sánh similarity ngữ nghĩa thay vì chỉ overlap từ khóa.
3. Nó cần embedding model, vector index và compute nhiều hơn; nếu model không hợp domain thì có thể không hơn sparse retrieval.

## Liên kết

- [[NLP Transformers - Chapter 07 - Question Answering]]
- [[Question Answering]]
- [[Retriever]]
- [[Sparse Retriever]]
- [[BM25]]
- [[Recall@k]]
- [[Semantic Search]]
- [[Embedding]]
- [[Vector Database]]
- [[Reader]]
