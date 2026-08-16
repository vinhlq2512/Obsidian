---
type: concept
status: seed
sources:
  - "[[2026-08-03_llm-security-basics-the-full-threat-model]]"
source_sections:
  - "[[2026-08-03_llm-security-basics-the-full-threat-model]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - llm
  - security
  - supply-chain
---

# LLM Supply Chain Security

## Định nghĩa

[[LLM Supply Chain Security]] là việc kiểm soát provenance và integrity của model, adapter, vector store, dataset, tool server và dependency trong LLM application.

## Cách hiểu bằng lời của tôi

Runtime filter không giúp nhiều nếu model/tool/dataset đã bị compromise trước khi app chạy. Với LLM stack, supply chain trải dưới toàn bộ pipeline: model file có thể chứa code khi load, vector store có thể bị poison, tool server có thể ship cấu hình injectable.

## Cách giảm rủi ro

- Ưu tiên nguồn model/tool/dataset có provenance rõ.
- Dùng serialization format an toàn khi có thể.
- Kiểm tra chữ ký/model signing hoặc release integrity.
- Tách quyền runtime của component được tải từ bên ngoài.

## Liên kết

- [[LLM Security]]
- [[Retrieval-Augmented Generation]]
- [[Model Context Protocol]]
- [[Least Privilege]]
- [[Prompt Injection]]
