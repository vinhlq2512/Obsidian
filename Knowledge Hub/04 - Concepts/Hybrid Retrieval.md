---
type: concept
status: developing
sources:
  - "[[2026-02-09_how-yelp-built-yelp-assistant]]"
  - "[[2026-05-20_how-netflix-is-using-multimodal-ai-to-power-video-search]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - retrieval
  - search
  - llm
---

# Hybrid Retrieval

## Định nghĩa

Hybrid retrieval là cách kết hợp nhiều tín hiệu retrieval, thường là keyword/exact match với embedding/vector similarity hoặc structured filters.

## Cách hiểu bằng lời của tôi

Keyword giỏi bắt constraint literal; embedding giỏi bắt nghĩa gần. Hybrid retrieval dùng cả hai để tránh hai lỗi đối xứng: chỉ keyword thì miss cách diễn đạt khác, chỉ vector thì miss điều kiện chính xác.

## Ví dụ từ ByteByteGo

Yelp photo retrieval kết hợp caption text match với image embedding similarity. Câu hỏi về heated patio có thể khớp với caption nhắc "heaters" hoặc ảnh có heat lamp dù caption không đủ rõ.

Netflix video search cần hybrid retrieval vì query có cả constraint literal và semantic. Ví dụ tên nhân vật cần exact/keyword match, còn bối cảnh như "kitchen" có thể cần vector similarity trên scene embedding. Hệ thống còn dùng filter extraction, threshold, phrase slop, fuzzy matching và post-processing để biến nhiều tín hiệu thành một kết quả hữu ích.

## Liên kết

- [[Semantic Search]]
- [[Vector Search Infrastructure]]
- [[Retrieval Evaluation]]
- [[Multimodal Search]]
- [[AI Search]]
- [[Multimodal Annotation Fusion]]
