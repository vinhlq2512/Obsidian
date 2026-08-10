---
type: reading-section
book: "[[Practical Natural Language Processing]]"
status: planned
chapter: 8
start_page: 488
end_page: 540
reading_date: 2026-08-16
planned_sessions:
  - "2026-08-16 | 488-514 | Social media challenges, tokenizer, trends, sentiment | 55 phút"
  - "2026-08-17 | 515-540 | Social preprocessing, support, memes, fake news | 55 phút"
tags:
  - nlp
  - practical-nlp
  - social-media
---

# Practical NLP - Chapter 08 - Social Media

## Mục tiêu cần hiểu

- Social media text khác văn bản chuẩn ở nhiễu, slang, hashtag, emoji, URL, mention và tốc độ drift.
- Pipeline NLP cần điều chỉnh tokenizer, preprocessing và monitoring cho social data.
- Sentiment, trend detection, support và fake news có failure modes riêng.

## Định nghĩa quan trọng

- Social media text data
- Trending topics
- Twitter sentiment
- Fake news detection
- Meme identification

## Mental model

```text
Noisy social text
-> normalization / tokenizer
-> task-specific representation
-> model
-> drift-aware monitoring
```

## Phần cần biết

- Đừng xử lý social data như văn bản sạch.
- Khi đọc, chú ý những quyết định preprocessing nào có thể xóa mất tín hiệu quan trọng.

## Câu hỏi review

1. Hashtag, mention và URL nên được giữ hay xóa trong từng task?
2. Sentiment trên social media sai vì những loại ambiguity nào?
3. Fake news detection cần dữ liệu ngoài text không?

## Gợi ý trả lời câu hỏi review

- Trả lời theo từng task: trend, support, sentiment, fake news.

## Liên kết

- [[Practical Natural Language Processing]]
- [[Sentiment Analysis]]
