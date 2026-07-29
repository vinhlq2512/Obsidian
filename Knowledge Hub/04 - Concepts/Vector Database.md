---
type: concept
status: seed
source:
  - "[[Hands-On LLM - Chapter 08 - Semantic Search and Retrieval-Augmented Generation]]"
tags:
  - concept
  - retrieval
  - database
---

# Vector Database

## Định nghĩa

Vector database là hệ thống lưu trữ embeddings và hỗ trợ tìm kiếm nearest neighbors theo similarity.

## Cách hiểu bằng lời của tôi

Đây là index cho meaning. Ta lưu vector của từng chunk/tài liệu, rồi khi có query thì embed query và tìm các vector gần nhất.

## Cần biết

- Thường lưu cả vector và metadata như source, page, title, chunk id.
- Similarity metric thường là cosine similarity, dot product hoặc Euclidean distance.
- Indexing giúp tìm nhanh trong corpus lớn.
- Metadata filtering giúp giới hạn search theo nguồn, thời gian, permission hoặc loại tài liệu.

## Liên kết

- [[Embedding]]
- [[Semantic Search]]
- [[Retrieval-Augmented Generation]]

