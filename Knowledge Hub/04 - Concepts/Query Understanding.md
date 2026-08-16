---
type: concept
status: developing
sources:
  - "[[2026-07-28_why-doordash-instacart-and-uber-eats-integrated-llms-into-se]]"
  - "[[2026-05-05_how-instacart-built-a-search-for-billions-of-products]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - search
  - llm
---

# Query Understanding

## Định nghĩa

Query understanding là lớp phân tích query người dùng để nhận ra intent, entity, constraint, synonym, rewrite và tín hiệu ranking trước khi hệ thống retrieve kết quả.

## Cách hiểu bằng lời của tôi

Người dùng không nói chuyện bằng schema của catalog. Họ gõ "small no-milk vanilla ice cream" hoặc "protein" và mong hệ thống hiểu nghĩa thực tế. Query understanding là bước dịch ngôn ngữ người dùng sang ngôn ngữ mà search stack hiểu được.

## Vai trò trong search

- Tách query thành chunks có ý nghĩa.
- Map chunk vào taxonomy hoặc knowledge graph.
- Phân biệt hard filter và soft preference.
- Rewrite query để tăng recall.
- Dùng domain context để tránh general-world answer sai intent sản phẩm.

## Trade-off

- Offline query understanding/cache rẻ và nhanh cho head queries.
- Online LLM/fine-tuned model hữu ích cho tail queries nhưng phải kiểm soát latency.
- LLM output cần bị ràng buộc bởi taxonomy hoặc retrieved candidate set để tránh invent label.

## Liên kết

- [[AI Search]]
- [[Retrieval-Augmented Generation]]
- [[Fine-tuning]]
- [[Context Engineering]]
- [[Entity Linking]]
