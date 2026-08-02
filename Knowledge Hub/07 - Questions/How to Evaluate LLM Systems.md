---
type: question
status: open
concepts:
  - "[[Large Language Model]]"
  - "[[Retrieval-Augmented Generation]]"
  - "[[Performance Measures for NER]]"
sources:
  - "[[Hands-On Large Language Models]]"
created_at: 2026-08-02
updated_at: 2026-08-02
tags:
  - question
  - llm
  - evaluation
---

# How to Evaluate LLM Systems

## Tôi đang thắc mắc gì?

- Làm thế nào để đánh giá hệ thống LLM thay vì chỉ đánh giá một model đơn lẻ?

## Vì sao câu hỏi này quan trọng?

- Một ứng dụng LLM thường gồm nhiều phần: retrieval, prompt, model, post-processing, evaluation và UX.
- Nếu chỉ đo model output chung chung, dễ bỏ sót lỗi retrieval, grounding hoặc latency/cost.

## Giải thích hiện tại

- [[Hands-On Large Language Models]] đặt câu hỏi này như một câu hỏi lớn của sách.
- [[Retrieval-Augmented Generation]] cho thấy chất lượng hệ thống phụ thuộc nhiều vào retrieval/chunking/reranking/prompt, không chỉ generator.
- [[Performance Measures for NER]] là ví dụ tốt về việc metric phải khớp với task, không dùng accuracy đơn giản khi task cần entity-level correctness.

## Cần kiểm tra thêm

- Với RAG, cần đo retrieval, grounding và answer quality riêng như thế nào?
- Với generative tasks, cần kết hợp human eval, automatic eval và regression tests ra sao?
- Khi nào cần đánh giá theo cost/latency/safety thay vì chỉ accuracy?

## Source evidence

- [[Hands-On Large Language Models]]
- [[Retrieval-Augmented Generation]]
- [[Performance Measures for NER]]

## Related

- [[LLM]]
- [[Representation Model vs Generative Model vs RAG]]

