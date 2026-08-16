---
type: synthesis
status: developing
concepts:
  - "[[AI Search]]"
  - "[[Query Understanding]]"
  - "[[Semantic Search]]"
  - "[[Two-Tower Retrieval]]"
  - "[[Vector Search Infrastructure]]"
  - "[[Commonsense Knowledge Graph]]"
  - "[[Product Recommendation System]]"
  - "[[Feed Retrieval]]"
  - "[[Semantic Retrieval]]"
  - "[[Generative Retrieval]]"
sources:
  - "[[2026-04-27_how-amazon-uses-llms-to-recommend-products]]"
  - "[[2026-05-05_how-instacart-built-a-search-for-billions-of-products]]"
  - "[[2026-05-27_how-airtable-built-the-search-layer-behind-their-ai-features]]"
  - "[[2026-07-28_why-doordash-instacart-and-uber-eats-integrated-llms-into-se]]"
  - "[[2026-08-10_how-to-fight-clickbait-meta-linkedin-youtube-case-studies]]"
created_at: 2026-08-16
updated_at: 2026-08-16
tags:
  - synthesis
  - search
  - recommendation
  - ai-engineering
---

# AI Search and Recommendation Systems

## Mental model

AI search là chuỗi quyết định về vị trí đặt intelligence:

- trước retrieval: [[Query Understanding]], rewrite, taxonomy mapping;
- trong retrieval: [[Semantic Search]], [[Two-Tower Retrieval]], ANN;
- quanh retrieval: guardrail, hard filter, domain context;
- sau retrieval: ranking, reranking, business logic;
- ngoài hot path: graph enrichment, cache, offline feature generation.

## Ba độ sâu tích hợp LLM

| Độ sâu | Ví dụ | Khi hợp |
|---|---|---|
| LLM ở offline/periphery | DoorDash enrich graph, parse query có output ràng buộc | Đã có taxonomy/knowledge graph mạnh |
| LLM ở query understanding | Instacart dùng RAG/cache cho head query và fine-tuned model cho tail query | Muốn hợp nhất nhiều model query cũ |
| LLM là embedding backbone | Uber Eats dùng fine-tuned Qwen trong two-tower retrieval | Cần shared semantic space đa domain/ngôn ngữ |

## Bài học từ case study

- Amazon COSMO: LLM tốt để sinh hypothesis commonsense, nhưng production cần filter, annotation, classifier và graph serving.
- Instacart Postgres/pgvector: đưa compute gần data có thể giảm latency hơn việc thêm một service chuyên dụng.
- Airtable Milvus: data shape quyết định kiến trúc, nhất là tenant isolation và hot/cold pattern.
- DoorDash/Instacart/Uber Eats: model choice ít quan trọng hơn câu hỏi LLM nên nằm ở đâu trong stack.
- LinkedIn/Meta/YouTube: cùng chuyển retrieval từ engagement proxy sang meaning, nhưng chọn consolidation, specialization funnel hoặc generative retrieval tùy data shape và rollback/cost trade-off.

## Ghi nhớ

Hybrid là mặc định. Keyword search, vector search, knowledge graph, cache, filter và reranker vẫn cùng tồn tại. LLM hữu ích nhất khi nó được đặt đúng vị trí: hiểu intent, tạo representation, sinh tri thức có kiểm chứng, hoặc thu hẹp output vào taxonomy an toàn.

## Liên kết

- [[Production LLM System Design]]
- [[AI Engineering Systems from RAG to Agents]]
- [[Graph RAG]]
- [[Vector Database]]
- [[Semantic Feed Retrieval Systems]]
