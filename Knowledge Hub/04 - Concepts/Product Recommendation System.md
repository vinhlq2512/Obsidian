---
type: concept
status: developing
sources:
  - "[[2026-04-27_how-amazon-uses-llms-to-recommend-products]]"
  - "[[2026-07-28_why-doordash-instacart-and-uber-eats-integrated-llms-into-se]]"
  - "[[2024-02-29_how-video-recommendations-work-part-1]]"
  - "[[2025-05-01_inside-netflixs-radical-shift-to-a-single-foundation-model]]"
  - "[[2026-08-10_how-to-fight-clickbait-meta-linkedin-youtube-case-studies]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - recommendation
  - search
  - llm
---

# Product Recommendation System

## Định nghĩa

Product recommendation system là hệ thống chọn, xếp hạng hoặc gợi ý item cho user dựa trên intent, hành vi, thuộc tính sản phẩm, context phiên và tín hiệu business.

## Cách hiểu bằng lời của tôi

Recommendation không chỉ là "người giống bạn mua gì". Trong e-commerce/search, nó còn phải hiểu nhu cầu ẩn sau query, constraint đang có, item nào còn bán được và lý do nào làm item phù hợp với phiên hiện tại.

## Lớp dữ liệu quan trọng

- Query-purchase pairs: user hỏi gì rồi mua gì.
- Co-purchase pairs: item nào thường đi cùng nhau trong session.
- Product attributes: category, brand, material, size, dietary preference.
- Intent/commonsense triples: dùng để giải khoảng cách giữa câu chữ và nhu cầu.
- Real-time state: inventory, price, location, fulfillment.

## Từ ByteByteGo

Amazon COSMO dùng LLM để tạo commonsense triples rồi phục vụ search relevance, recommendation và navigation. DoorDash/Instacart/Uber Eats cho thấy recommendation/search production thường là hybrid: LLM giúp hiểu intent hoặc tạo embedding, còn retrieval, ranking, guardrail và cache vẫn là hệ thống cổ điển được tối ưu mạnh.

Netflix đưa recommendation về hướng foundation model: token không phải chỉ là word token mà là chuỗi event/user-item/context dị thể. Để phục vụ trong vài chục mili-giây, hệ thống phải dùng compression phân cấp, sparse attention, KV cache, batch pre-computation, vector store và quản lý vòng đời embedding để tránh drift sau retrain.

LinkedIn, Meta và YouTube cho thấy recommendation retrieval có ba hướng: hợp nhất nhiều retrieval system thành một semantic dual encoder, giữ nhiều model chuyên biệt trong staged funnel, hoặc để model sinh Semantic IDs của item tiếp theo. Khác biệt nằm ở data shape, latency budget, rollback strategy và long-tail coverage.

## Liên kết

- [[AI Search]]
- [[Commonsense Knowledge Graph]]
- [[Semantic Search]]
- [[Two-Tower Retrieval]]
- [[LLM Evaluation]]
- [[Foundation Model for Recommendation]]
- [[Feed Retrieval]]
- [[Recommendation Funnel]]
- [[Generative Retrieval]]
- [[Cold Start Problem]]
