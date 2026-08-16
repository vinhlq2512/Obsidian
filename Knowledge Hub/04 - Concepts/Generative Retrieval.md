---
type: concept
status: seed
sources:
  - "[[2026-08-10_how-to-fight-clickbait-meta-linkedin-youtube-case-studies]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - retrieval
  - recommendation
  - llm
---

# Generative Retrieval

## Định nghĩa

Generative retrieval là hướng retrieval trong đó model sinh identifier hoặc code của item cần retrieve, thay vì tìm nearest neighbors trong một index truyền thống.

## Cách hiểu bằng lời của tôi

Index-based retrieval hỏi "vector nào gần user nhất trong index?". Generative retrieval hỏi model "hãy sinh ID của item phù hợp tiếp theo". Với YouTube PLUM, video được gán Semantic ID, rồi model sinh các Semantic ID candidate bằng decoding.

## Trade-off

- Có thể giảm phụ thuộc vào embedding table/index lớn.
- Có thể tăng coverage cho long-tail item.
- Có failure mode riêng: model có thể sinh identifier không tồn tại hoặc khó map về item thật.
- Vẫn cần hệ thống kiểm tra, decode và map ID an toàn.

## Liên kết

- [[Semantic Retrieval]]
- [[Product Recommendation System]]
- [[LLM Architecture Comparison]]
- [[Vector Search Infrastructure]]
- [[Cold Start Problem]]
