---
type: concept
status: developing
sources:
  - "[[2026-05-27_how-airtable-built-the-search-layer-behind-their-ai-features]]"
  - "[[2026-05-05_how-instacart-built-a-search-for-billions-of-products]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - vector-search
  - infrastructure
  - retrieval
---

# Vector Search Infrastructure

## Định nghĩa

Vector search infrastructure là hạ tầng lưu, cập nhật, index và query embeddings ở quy mô production với các ràng buộc về latency, recall, memory, isolation, write throughput và recovery.

## Cách hiểu bằng lời của tôi

Embedding chỉ là đầu vào. Phần khó ở production là giữ hàng triệu/hàng tỷ vector có thể tìm nhanh, cập nhật được, không lẫn tenant, không ăn quá nhiều RAM và phục hồi được khi hỏng.

## Các quyết định thiết kế

- Co-location: đặt vector gần relational/catalog data để filter sớm, hoặc dùng vector DB riêng để scale độc lập.
- Partitioning: shared partition tiết kiệm tài nguyên, one-partition-per-tenant tăng isolation và xóa dữ liệu dễ hơn.
- Index choice: HNSW ưu tiên latency/recall nhưng ăn RAM; IVF-SQ8 tiết kiệm memory hơn; DiskANN đẩy index xuống SSD nhưng tăng latency.
- Hot/cold loading: giữ partition nóng trong memory, offload partition lạnh xuống storage.
- Recovery: restore snapshot hoặc rebuild embeddings từ source-of-truth bằng pipeline async.

## Từ ByteByteGo

Airtable chọn Milvus với one partition per base vì isolation và deletion rõ ràng, rồi dùng hierarchical capping để tránh namespace phình quá mức. Instacart chọn pgvector/Postgres vì cần đưa compute gần catalog/inventory data để filter trước ANN search và giảm application-layer join.

## Liên kết

- [[Semantic Search]]
- [[Vector Database]]
- [[Embedding]]
- [[Database Indexing]]
- [[AI Search]]
- [[Observability]]
