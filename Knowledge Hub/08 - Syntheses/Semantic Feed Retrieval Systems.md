---
type: synthesis
status: seed
concepts:
  - "[[Feed Retrieval]]"
  - "[[Semantic Retrieval]]"
  - "[[Generative Retrieval]]"
  - "[[Recommendation Funnel]]"
  - "[[Cold Start Problem]]"
  - "[[Two-Tower Retrieval]]"
sources:
  - "[[2026-08-10_how-to-fight-clickbait-meta-linkedin-youtube-case-studies]]"
created_at: 2026-08-16
updated_at: 2026-08-16
tags:
  - synthesis
  - retrieval
  - recommendation
  - ai-engineering
---

# Semantic Feed Retrieval Systems

## Ý chính

Clickbait không chỉ là moderation problem. Nó là dấu hiệu retrieval đang tối ưu một proxy dễ bị thao túng như engagement thô. LinkedIn, Meta và YouTube cùng chuyển retrieval sang meaning, nhưng chọn ba kiến trúc khác nhau.

## Ba hướng thiết kế

| Hệ | Hướng | Trade-off |
|---|---|---|
| LinkedIn | Một language-model dual encoder chung cho member/post | Dễ align objective và giảm hệ thống song song, nhưng rollback khó hơn nếu model chung regress |
| Meta/Instagram | Staged [[Recommendation Funnel]] với nhiều model chuyên biệt | Kiểm soát từng objective tốt hơn, nhưng vận hành phức tạp |
| YouTube | [[Generative Retrieval]] bằng Semantic IDs | Giảm index/embedding table lớn, nhưng có rủi ro sinh ID không tồn tại |

## Mental model

```text
hundreds of millions of candidates
-> cheap retrieval by meaning
-> smaller candidate set
-> heavier ranking/value model
-> diversity/integrity pass
-> feed
```

## Ghi nhớ

Model không phải lúc nào cũng là phần khó nhất. LinkedIn case cho thấy representation của structured features trong prompt/input format có thể quyết định chất lượng retrieval nhiều hơn bản thân model.

## Liên kết

- [[AI Search and Recommendation Systems]]
- [[Production LLM System Design]]
- [[Vector Search Infrastructure]]
- [[Product Recommendation System]]
