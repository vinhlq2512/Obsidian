---
type: synthesis
status: seed
concepts:
  - "[[Multimodal Search]]"
  - "[[Multimodal Annotation Fusion]]"
  - "[[Foundation Model for Recommendation]]"
  - "[[Embedding Lifecycle Management]]"
  - "[[Product Recommendation System]]"
  - "[[Multimodal LLM]]"
  - "[[AI Search]]"
sources:
  - "[[2026-05-20_how-netflix-is-using-multimodal-ai-to-power-video-search]]"
  - "[[2025-05-01_inside-netflixs-radical-shift-to-a-single-foundation-model]]"
  - "[[2026-07-07_chatgpt-vs-gemini-vs-claude-how-they-differ]]"
created_at: 2026-08-16
updated_at: 2026-08-16
tags:
  - synthesis
  - ai-search
  - recommendation
  - multimodal
---

# Multimodal and Recommendation AI Systems

## Ý chính

Ba source ByteByteGo này cùng chỉ vào một pattern: hệ AI production không chỉ là model mạnh hơn, mà là cách biến nhiều tín hiệu dị thể thành representation có thể retrieve, rank và phục vụ đúng latency.

## Cầu nối giữa search và recommendation

- [[Multimodal Search]] biến video thành annotation/embedding theo thời gian để search được những đoạn không có text trực tiếp.
- [[Foundation Model for Recommendation]] biến chuỗi hành vi và metadata thành token/embedding để dự đoán preference tiếp theo.
- [[Multimodal Annotation Fusion]] là lớp "plumbing" nối output dị thể của nhiều model vào cùng timeline/index.
- [[Embedding Lifecycle Management]] giữ embedding ổn định khi catalog, model và downstream consumers thay đổi.
- [[LLM Architecture Comparison]] nhắc rằng multimodal và context dài có nhiều chiến lược kiến trúc khác nhau, không thể đánh giá chỉ bằng một nhãn "LLM".

## Mental model

```text
raw multimodal/user events
-> encoders hoặc feature extraction
-> embeddings/annotations/tokens
-> fusion hoặc compression
-> index/model serving
-> retrieve/rank/post-process
```

## Trade-off cần nhớ

- Offline fusion hoặc pre-computation giảm latency runtime nhưng làm freshness khó hơn.
- Model thống nhất giảm fragmentation nhưng tăng rủi ro debug, latency và retraining.
- Hybrid search/recommendation vẫn cần rule, threshold, keyword search, vector search và post-processing; LLM không thay thế toàn bộ hệ thống retrieval/ranking.

## Liên kết

- [[AI Search and Recommendation Systems]]
- [[Production LLM System Design]]
- [[Vector Search Infrastructure]]
- [[KV Cache]]
- [[Multimodal Annotation Fusion]]
- [[Embedding Lifecycle Management]]
