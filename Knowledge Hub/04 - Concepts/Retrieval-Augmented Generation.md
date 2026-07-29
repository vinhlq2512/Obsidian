---
type: concept
status: seed
source:
  - "[[Hands-On LLM - Chapter 08 - Semantic Search and Retrieval-Augmented Generation]]"
tags:
  - concept
  - rag
  - llm
---

# Retrieval-Augmented Generation

## Định nghĩa

Retrieval-Augmented Generation là pipeline truy xuất tài liệu liên quan rồi đưa chúng vào prompt để LLM sinh câu trả lời dựa trên context đó.

## Cách hiểu bằng lời của tôi

RAG cho LLM đọc tài liệu trước khi trả lời. Retriever tìm context, generator viết câu trả lời, evaluator kiểm tra độ đúng và grounding.

## Cần biết

- Chất lượng retrieval quyết định phần lớn chất lượng câu trả lời.
- Chunking, embedding model, top-k, reranking và prompt đều ảnh hưởng kết quả.
- RAG phù hợp khi kiến thức private, mới, dài hoặc cần citation.
- RAG vẫn có hallucination nếu context sai, thiếu hoặc model không bám context.

## Liên kết

- [[Semantic Search]]
- [[Embedding]]
- [[Vector Database]]
- [[Prompt Engineering]]

