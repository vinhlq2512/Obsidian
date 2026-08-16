---
type: concept
status: developing
sources:
  - "[[2026-03-23_how-agentic-rag-works]]"
  - "[[2026-05-23_ep216-rags-vs-agents]]"
  - "[[2026-06-27_ep220-rag-vs-graph-rag-vs-agentic-rag]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - rag
  - agent
  - llm
---

# Agentic RAG

## Định nghĩa

Agentic RAG là biến thể RAG dùng agent hoặc control loop để chọn nguồn, viết lại truy vấn, đánh giá kết quả retrieve và thử lại trước khi sinh câu trả lời.

## Cách hiểu bằng lời của tôi

RAG chuẩn hỏi một lần rồi trả lời. Agentic RAG đặt một người gác giữa retrieval và generation: kết quả này có đủ không, cần tìm nguồn khác không, câu hỏi có cần tách nhỏ không?

## Khi hữu ích

- Câu hỏi mơ hồ hoặc cần phân rã thành nhiều sub-question.
- Câu trả lời nằm rải rác ở nhiều hệ thống: docs, SQL, ticket, policy.
- Retrieval đầu tiên hay trả về tài liệu cũ, thiếu hoặc gần đúng nhưng sai ngữ cảnh.

## Trade-off

- Tăng latency vì có nhiều vòng LLM call và retrieval.
- Tăng cost, thường cao hơn RAG chuẩn nhiều lần nếu loop dài.
- Khó debug hơn vì trajectory có thể khác nhau giữa các lượt.
- Self-evaluation vẫn phụ thuộc năng lực judge của LLM.

## So sánh với Graph RAG

[[Graph RAG]] thêm knowledge graph để đi theo quan hệ giữa entity và community/context; Agentic RAG thêm decision loop để chọn nguồn, chia câu hỏi và retry. Hai hướng có thể kết hợp, nhưng giải quyết vấn đề khác nhau: Graph RAG mạnh khi tri thức có quan hệ cấu trúc, Agentic RAG mạnh khi truy vấn cần nhiều bước quyết định.

## Liên kết

- [[Retrieval-Augmented Generation]]
- [[Graph RAG]]
- [[LLM Agent]]
- [[Agentic Loop]]
- [[Tool Use]]
- [[LLM Evaluation]]
