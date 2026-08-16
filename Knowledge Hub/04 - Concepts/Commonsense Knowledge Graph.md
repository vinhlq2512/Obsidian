---
type: concept
status: developing
sources:
  - "[[2026-04-27_how-amazon-uses-llms-to-recommend-products]]"
  - "[[2026-07-28_why-doordash-instacart-and-uber-eats-integrated-llms-into-se]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - knowledge-graph
  - recommendation
  - llm
---

# Commonsense Knowledge Graph

## Định nghĩa

Commonsense knowledge graph là knowledge graph lưu các quan hệ ngầm về lý do, mục đích, ngữ cảnh sử dụng hoặc intent của người dùng, không chỉ thuộc tính factual của entity.

## Cách hiểu bằng lời của tôi

Product graph thường biết "đây là áo khoác, màu đen, size M". Commonsense graph cố biết thêm "người tìm winter clothes muốn ấm" hoặc "pregnant women cần giày chống trượt". Nó nối query với nhu cầu ẩn phía sau query.

## Luồng xây dựng kiểu Amazon COSMO

```text
query-purchase / co-purchase behavior
-> LLM generates candidate explanations
-> similarity filtering removes paraphrase/noise
-> human annotation for plausibility and typicality
-> classifier scales judgment to remaining candidates
-> structured triples become knowledge graph
-> smaller instruction-tuned model handles new cases
```

## Cần biết

- LLM sinh hypothesis tốt nhưng nhiễu nhiều, cần filter và human-in-the-loop.
- Typicality khác plausibility: một lý do có thể hợp lý nhưng không đại diện cho hành vi mua thật.
- Graph tĩnh giúp serving nhanh; model nhỏ fine-tuned bổ sung cho query/product mới.
- Daily refresh/caching đổi realtime freshness lấy latency và chi phí.

## Liên kết

- [[AI Search]]
- [[Graph RAG]]
- [[Product Recommendation System]]
- [[Fine-tuning]]
- [[LLM Evaluation]]
