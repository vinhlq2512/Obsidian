---
type: question
status: open
concepts:
  - "[[Retrieval-Augmented Generation]]"
  - "[[Fine-tuning]]"
  - "[[Semantic Search]]"
sources:
  - "[[Hands-On Large Language Models]]"
  - "[[Retrieval-Augmented Generation]]"
created_at: 2026-08-02
updated_at: 2026-08-02
tags:
  - question
  - llm
  - rag
---

# When Is RAG Better Than Fine-Tuning

## Tôi đang thắc mắc gì?

- Khi nào embedding/search/RAG tốt hơn fine-tuning?

## Vì sao câu hỏi này quan trọng?

- RAG và fine-tuning giải quyết hai loại vấn đề khác nhau.
- Nếu chỉ cần đưa facts private/mới/dài vào hệ thống, retrieval có thể hợp hơn fine-tuning.

## Giải thích hiện tại

- [[Retrieval-Augmented Generation]] cho LLM đọc tài liệu trước khi trả lời.
- Note hiện tại nhấn mạnh retrieval quality, chunking, embedding model, top-k, reranking và prompt đều ảnh hưởng chất lượng.
- Fine-tuning nên được xem như cách thay đổi hành vi/capability của model, không phải nơi lưu mọi knowledge.

## Cần kiểm tra thêm

- Dấu hiệu nào cho thấy vấn đề là retrieval, không phải model capability?
- Khi nào RAG cần thêm reranker?
- Khi nào fine-tuning vẫn cần thiết sau khi đã có RAG?

## Source evidence

- [[Hands-On Large Language Models]]
- [[Retrieval-Augmented Generation]]
- [[Representation Model vs Generative Model vs RAG]]

## Related

- [[LLM]]
- [[Semantic Search]]

