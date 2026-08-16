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
---

# Indirect Prompt Injection

## Định nghĩa

[[Indirect Prompt Injection]] là prompt injection nằm trong nội dung bên ngoài mà hệ thống đọc hoặc retrieve thay cho user, như email, issue, website, ticket hoặc document.

## Cách hiểu bằng lời của tôi

Nguy hiểm của indirect injection là user không nhất thiết nhìn thấy instruction độc hại. Họ chỉ hỏi một việc hợp lệ, còn instruction nằm trong data mà agent được yêu cầu xử lý. Vì LLM không có boundary chắc chắn giữa instruction và data, nội dung đó vẫn có thể điều khiển output hoặc tool use.

## Khi xuất hiện

- RAG đọc tài liệu trong knowledge base bị poison.
- Agent đọc email/ticket/comment từ nguồn không tin cậy.
- Tool output chứa text có dạng instruction.

## Liên kết

- [[Prompt Injection]]
- [[LLM Security]]
- [[Retrieval-Augmented Generation]]
- [[Excessive Agency]]
- [[Untrusted Model Output]]
