---
type: question
status: open
concepts:
  - "[[Representation Model]]"
  - "[[Generative Model]]"
  - "[[Large Language Model]]"
sources:
  - "[[Hands-On Large Language Models]]"
  - "[[Representation Model]]"
  - "[[Generative Model]]"
created_at: 2026-08-02
updated_at: 2026-08-02
tags:
  - question
  - llm
---

# When to Use Representation Model Instead of Generative Model

## Tôi đang thắc mắc gì?

- Khi nào nên dùng representation model thay vì generative model?

## Vì sao câu hỏi này quan trọng?

- Không phải workflow LLM nào cũng cần sinh text.
- Chọn sai loại model có thể làm hệ thống tốn chi phí, chậm hơn hoặc khó đánh giá hơn.

## Giải thích hiện tại

- [[Representation Model]] tạo vector cho classification, clustering, retrieval hoặc similarity search.
- [[Generative Model]] sinh token/text mới và phù hợp với chat, completion hoặc generation.
- [[Representation Model vs Generative Model vs RAG]] là synthesis note để gom trade-off này.

## Cần kiểm tra thêm

- Với classification, khi nào embedding baseline đủ tốt?
- Khi nào cần generative model dù output cuối chỉ là nhãn?
- Cách đánh giá hai hướng này nên khác nhau thế nào?

## Source evidence

- [[Hands-On Large Language Models]]
- [[Representation Model]]
- [[Generative Model]]

## Related

- [[LLM]]
- [[Representation Model vs Generative Model vs RAG]]

