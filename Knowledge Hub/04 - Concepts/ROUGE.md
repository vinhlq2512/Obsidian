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
  - summarization
---

# ROUGE

## Định nghĩa

ROUGE là nhóm metric tự động thường dùng để đánh giá summarization bằng cách đo overlap giữa summary do model sinh và reference summary.

## Cách hiểu bằng lời của tôi

ROUGE hỏi: model có giữ lại những từ/cụm từ/nội dung giống bản tóm tắt chuẩn không? Nó hữu ích để so sánh nhanh nhiều model, nhưng không đảm bảo summary đúng facts hoặc dễ đọc.

## Cần biết

- ROUGE phổ biến trong [[Summarization]] hơn [[BLEU]].
- ROUGE hỗ trợ [[Comparing Different Summaries|so sánh nhanh nhiều summary]], nhiều model hoặc nhiều checkpoint.
- ROUGE thấp chưa chắc summary vô dụng nếu cách diễn đạt khác reference nhưng vẫn đúng.
- ROUGE cao chưa chắc summary tốt nếu summary lặp, thiếu mạch hoặc thêm thông tin sai.

## Khi áp dụng

- Đánh giá baseline summarization.
- So sánh nhiều model summarization bằng cùng một hàm metric.
- Kết hợp với human review để kiểm tra factuality, coverage và coherence.

## Liên kết

- [[Summarization]]
- [[Text Summarization Pipelines]]
- [[Comparing Different Summaries]]
- [[Abstractive Summarization]]
- [[BLEU]]
- [[NLP Transformers - Chapter 06 - Summarization]]
