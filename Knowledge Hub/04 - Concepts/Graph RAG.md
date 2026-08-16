---
type: concept
status: developing
sources:
  - "[[2026-06-27_ep220-rag-vs-graph-rag-vs-agentic-rag]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - rag
  - knowledge-graph
  - llm
---

# Graph RAG

## Định nghĩa

Graph RAG là pattern retrieval cho LLM dùng knowledge graph để tìm và tổng hợp context theo entity, quan hệ và community, thay vì chỉ lấy top-k chunks bằng vector similarity.

## Cách hiểu bằng lời của tôi

RAG chuẩn tìm đoạn gần query. Graph RAG tìm node/entity liên quan rồi đi theo quan hệ trong graph để gom bối cảnh có cấu trúc. Nó hữu ích khi câu hỏi không chỉ cần một đoạn văn, mà cần hiểu quan hệ giữa người, tổ chức, quy định, thuốc, sự kiện hoặc khái niệm.

## Hai kiểu search

- Local search: embed query, tìm entity liên quan trong vector DB, traverse graph để lấy linked context, rồi LLM synthesize.
- Global search: dùng community report hoặc summary cấp cao, chấm relevance, chọn context tốt nhất, rồi synthesize.

## Trade-off

- Mạnh với domain có tri thức quan hệ như legal, compliance, biomedical.
- Đắt để build vì cần extraction, entity resolution, graph maintenance.
- Chậm update hơn RAG chuẩn nếu source thay đổi liên tục.
- Có thể kết hợp với [[Agentic RAG]] khi query cần cả graph traversal lẫn loop tự kiểm tra.

## Liên kết

- [[Retrieval-Augmented Generation]]
- [[Agentic RAG]]
- [[Vector Database]]
- [[Entity Linking]]
