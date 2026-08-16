---
type: concept
status: developing
sources:
  - "[[2026-02-09_how-yelp-built-yelp-assistant]]"
  - "[[2026-01-20_this-isnt-an-ai-summarizer-and-that-matters-byte-sized-design]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - retrieval
  - evaluation
  - llm
---

# Retrieval Evaluation

## Định nghĩa

Retrieval evaluation là đánh giá liệu retrieval layer có đưa đúng evidence/source/candidate vào context cho task downstream hay không.

## Cách hiểu bằng lời của tôi

Nhiều lỗi RAG là retrieval failure ngụy trang thành hallucination. Nếu source đúng không vào context, model tốt mấy cũng phải đoán. Nếu source nhiễu vào quá nhiều, model bị kéo lệch.

## Tín hiệu cần đo

- Relevant source được retrieve không?
- Source không liên quan có bị đưa vào không?
- Query/source selector chọn đúng store không?
- Keyword, vector, hybrid retrieval fail ở loại câu hỏi nào?
- Latency budget của retrieval có phá UX không?

## Bài học từ Yelp

Yelp tách structured facts, reviews, photos và website/menu text thành store khác nhau. Content Source Selector quyết định store nào cần query để tránh lấy review noisy cho câu hỏi cần fact chính xác như giờ mở cửa.

## Liên kết

- [[Retrieval-Augmented Generation]]
- [[AI Search]]
- [[Hybrid Retrieval]]
- [[Evidence-Grounded Generation]]
- [[LLM Evaluation]]
