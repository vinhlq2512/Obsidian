---
type: concept
status: developing
sources:
  - "[[2026-08-10_how-to-fight-clickbait-meta-linkedin-youtube-case-studies]]"
  - "[[2025-05-01_inside-netflixs-radical-shift-to-a-single-foundation-model]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - recommendation
  - retrieval
---

# Cold Start Problem

## Định nghĩa

Cold start problem là vấn đề recommendation/search gặp phải khi user, item hoặc context mới có quá ít behavioral history để model cá nhân hóa tốt.

## Cách hiểu bằng lời của tôi

Behavioral retrieval cần quá khứ. User mới chưa click gì thì hệ thống chỉ biết rất ít. Semantic retrieval và pretrained language models giúp bằng cách dùng ý nghĩa từ profile/content/metadata để suy luận trước khi có đủ hành vi.

## Trade-off

- Pretraining giúp infer từ profile mỏng, hữu ích cho user mới.
- Inference từ profile sparse có thể sai hoặc biến user thành stereotype.
- Metadata-based initialization giúp item mới có embedding ban đầu, nhưng vẫn cần feedback thật để ổn định.

## Liên kết

- [[Semantic Retrieval]]
- [[Product Recommendation System]]
- [[Foundation Model for Recommendation]]
- [[Two-Tower Retrieval]]
