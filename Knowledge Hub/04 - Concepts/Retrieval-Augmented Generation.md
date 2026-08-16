---
type: concept
status: seed
sources:
  - "[[Hands-On LLM - Chapter 08 - Semantic Search and Retrieval-Augmented Generation]]"
  - "[[2026-05-23_ep216-rags-vs-agents]]"
  - "[[2026-03-23_how-agentic-rag-works]]"
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
- RAG chuẩn thường là pipeline một chiều: query -> retrieve -> đưa context vào prompt -> generate.
- Khi câu hỏi mơ hồ hoặc cần nhiều nguồn, cần cân nhắc [[Agentic RAG]] thay vì chỉ tăng top-k.

## Từ ByteByteGo

ByteByteGo nhấn mạnh RAG là lựa chọn tốt khi câu trả lời nằm trong tài liệu và hệ thống cần grounded answer có chi phí/độ trễ dự đoán được. Điểm yếu của RAG chuẩn là nó thường không tự hỏi "kết quả retrieve đã đủ tốt chưa"; nếu retrieval sai, generator vẫn có thể trả lời rất tự tin trên context yếu.

## Liên kết

- [[Semantic Search]]
- [[Embedding]]
- [[Vector Database]]
- [[Prompt Engineering]]
- [[Agentic RAG]]
- [[Context Engineering]]
