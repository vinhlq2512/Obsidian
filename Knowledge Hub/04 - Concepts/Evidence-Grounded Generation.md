---
type: concept
status: developing
sources:
  - "[[2026-02-09_how-yelp-built-yelp-assistant]]"
  - "[[2025-09-16_how-anthropic-built-a-multi-agent-research-system]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - llm
  - rag
  - grounding
---

# Evidence-Grounded Generation

## Định nghĩa

Evidence-grounded generation là pattern buộc model sinh câu trả lời dựa trên evidence đã retrieve hoặc kiểm chứng, thường kèm citation tới nguồn hỗ trợ.

## Cách hiểu bằng lời của tôi

Thay vì nhồi mọi dữ liệu vào prompt và hy vọng model tự tìm đúng, hệ thống tách "tìm bằng chứng" khỏi "viết câu trả lời". Model cuối chỉ nên tổng hợp từ snippet, field hoặc source đã được chọn.

## Cơ chế

```text
user question
-> classify intent/source
-> retrieve evidence liên quan
-> generate answer từ evidence
-> attach citations hoặc provenance
-> evaluate groundedness
```

## Trade-off

- Giảm hallucination và tăng khả năng debug.
- Chất lượng phụ thuộc mạnh vào retrieval/source selection.
- Citation phải map đúng claim, không chỉ gắn nguồn cho đẹp.

## Liên kết

- [[Retrieval-Augmented Generation]]
- [[Retrieval Evaluation]]
- [[AI Hallucination]]
- [[Citation Quality]]
- [[AI Search]]
