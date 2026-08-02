---
type: synthesis
status: evolving
concepts:
  - "[[Large Language Model]]"
  - "[[Representation Model]]"
  - "[[Generative Model]]"
  - "[[Semantic Search]]"
  - "[[Retrieval-Augmented Generation]]"
  - "[[Fine-tuning]]"
sources:
  - "[[Hands-On Large Language Models]]"
  - "[[Hands-On LLM - Chapter 01 - An Introduction to Large Language Models]]"
  - "[[Hands-On LLM - Chapter 08 - Semantic Search and Retrieval-Augmented Generation]]"
questions:
  - "[[When to Use Representation Model Instead of Generative Model]]"
  - "[[When Is RAG Better Than Fine-Tuning]]"
created_at: 2026-08-02
updated_at: 2026-08-02
tags:
  - synthesis
  - llm
---

# Representation Model vs Generative Model vs RAG

## Câu hỏi trung tâm

- Khi xây ứng dụng LLM, lúc nào nên dùng representation model, generative model, hoặc RAG?

## Mental model

```text
Representation model -> biến text thành vector -> search/classification/clustering
Generative model     -> sinh token tiếp theo -> chat/completion/generation
RAG                  -> retrieve context rồi generate -> hỏi đáp trên knowledge private/dài/mới
```

## So sánh nhanh

| Hướng | Output chính | Hợp khi | Rủi ro chính |
| --- | --- | --- | --- |
| [[Representation Model]] | Vector/embedding | classification, retrieval, similarity, clustering | embedding space kém hoặc không đúng domain |
| [[Generative Model]] | Text/token mới | trả lời, viết, biến đổi text, reasoning qua prompt | latency/chi phí/hallucination |
| [[Retrieval-Augmented Generation]] | Câu trả lời grounded bằng context | knowledge private, mới, dài, cần citation | retrieval sai/thiếu, chunking kém, context nhiễu |

## Tổng hợp của tôi

- Không phải bài toán nào cũng cần model sinh.
- Nếu output mong muốn là nhãn, ranking, similarity hoặc cluster, representation model thường là baseline đáng thử trước.
- Nếu cần trả lời bằng ngôn ngữ tự nhiên trên tài liệu dài/private, RAG là cách nối retrieval với generative model.
- Fine-tuning nên được xem như một quyết định riêng: dùng khi cần thay đổi hành vi/model capability, không chỉ để nhồi thêm facts có thể retrieve.

## Nguồn

- [[Hands-On Large Language Models]]
- [[Large Language Model]]
- [[Representation Model]]
- [[Generative Model]]
- [[Retrieval-Augmented Generation]]

## Liên kết

- [[LLM]]
- [[When to Use Representation Model Instead of Generative Model]]
- [[When Is RAG Better Than Fine-Tuning]]

