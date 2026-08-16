---
type: concept
status: seed
sources:
  - "[[Hands-On LLM - Chapter 08 - Semantic Search and Retrieval-Augmented Generation]]"
  - "[[2026-05-05_how-instacart-built-a-search-for-billions-of-products]]"
  - "[[2026-05-27_how-airtable-built-the-search-layer-behind-their-ai-features]]"
  - "[[2026-07-28_why-doordash-instacart-and-uber-eats-integrated-llms-into-se]]"
  - "[[2026-08-10_how-to-fight-clickbait-meta-linkedin-youtube-case-studies]]"
last_updated: 2026-08-16
tags:
  - concept
  - retrieval
  - embeddings
---

# Semantic Search

## Định nghĩa

Semantic search là tìm kiếm theo ý nghĩa bằng cách so sánh embeddings của query và documents.

## Cách hiểu bằng lời của tôi

Thay vì chỉ khớp từ khóa, semantic search hỏi: query này gần đoạn nào về mặt nghĩa trong vector space?

## Cần biết

- Cần embedding model tốt, chunking hợp lý và vector database.
- Dense retrieval có thể tìm kết quả dùng từ khác nhưng cùng nghĩa.
- Có thể kết hợp keyword search và semantic search để tăng độ phủ.
- Reranking thường cải thiện kết quả top-k.
- ANN index giúp tìm vector gần đúng nhanh hơn so với quét toàn bộ corpus.
- Trong product search, semantic search thường phải kết hợp filter như availability, location, fulfillment type hoặc tenant boundary.
- Vector search không tự giải quyết ranking cuối; nó thường là candidate generation trước khi reranker/business rules xử lý.

## Từ ByteByteGo

Instacart cho thấy semantic search không chỉ là chọn vector database. Khi keyword và semantic retrieval nằm ở hai hệ thống khác nhau, app phải overfetch, filter muộn và merge kết quả ở application layer. Khi đưa vector search về gần dữ liệu catalog/inventory bằng pgvector, hệ thống có thể filter trước ANN search và giảm round trip.

Airtable cho thấy đặc tính workload quyết định kiến trúc vector search: nhiều tenant nhỏ, isolation mạnh, phần lớn base cold, p99 dưới 500ms. Vì vậy partitioning, index type và hot/cold loading quan trọng ngang embedding model.

Feed retrieval case mở rộng semantic search từ query-document sang user-content: user/profile/activity và post/video cùng được đưa vào không gian meaning để lấy candidate trước ranking.

## Liên kết

- [[Embedding]]
- [[Vector Database]]
- [[Retrieval-Augmented Generation]]
- [[AI Search]]
- [[Vector Search Infrastructure]]
- [[Two-Tower Retrieval]]
- [[Semantic Retrieval]]
- [[Feed Retrieval]]
