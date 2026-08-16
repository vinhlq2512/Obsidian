---
type: concept
status: seed
sources:
  - "[[2026-08-03_llm-security-basics-the-full-threat-model]]"
source_sections:
  - "[[2026-08-03_llm-security-basics-the-full-threat-model]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - rag
  - security
---

# RAG Knowledge Base Poisoning

## Định nghĩa

[[RAG Knowledge Base Poisoning]] là tấn công đưa tài liệu hoặc passage độc hại vào corpus/vector store để retrieval kéo chúng vào context và làm lệch câu trả lời hoặc hành động của model.

## Cách hiểu bằng lời của tôi

RAG không chỉ phụ thuộc model; nó phụ thuộc chất lượng và provenance của nguồn retrieve. Nếu knowledge base chứa vài đoạn được thiết kế đúng câu hỏi mục tiêu, model có thể bị hướng sang câu trả lời sai hoặc instruction độc hại dù user query hợp lệ.

## Liên kết

- [[Retrieval-Augmented Generation]]
- [[Indirect Prompt Injection]]
- [[LLM Security]]
- [[Citation Quality]]
- [[Retrieval Evaluation]]
