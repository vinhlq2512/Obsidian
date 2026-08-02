---
type: concept
status: seed
sources:
  - "[[NLP Transformers - Chapter 06 - Summarization]]"
source_sections:
  - "[[NLP Transformers - Chapter 06 - Summarization]]"
first_seen: 2026-07-30
last_updated: 2026-08-02
created_at: 2026-08-02
updated_at: 2026-08-02
tags:
  - concept
  - nlp
  - evaluation
---

# BLEU

## Định nghĩa

BLEU là metric tự động so sánh text được sinh với reference text, thường dựa trên n-gram precision.

## Cách hiểu bằng lời của tôi

BLEU hỏi: trong các cụm từ model sinh ra, bao nhiêu cụm cũng xuất hiện trong reference? Vì vậy BLEU hợp với translation hơn summarization, nơi có nhiều cách tóm tắt đúng nhưng dùng từ khác reference.

## Cần biết

- BLEU thiên về precision của n-gram.
- BLEU có thể phạt output đúng ý nhưng diễn đạt khác reference.
- Trong summarization, [[ROUGE]] thường phổ biến hơn, nhưng cả hai đều không thay thế human review.

## Khi áp dụng

- Dùng như metric tham khảo khi cần so sánh output sinh với reference.
- Cẩn trọng khi dùng cho [[Summarization]], vì summary tốt có thể không overlap nhiều n-gram.

## Liên kết

- [[ROUGE]]
- [[Summarization]]
- [[Text Summarization Pipelines]]
- [[NLP Transformers - Chapter 06 - Summarization]]

