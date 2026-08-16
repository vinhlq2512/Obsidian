---
type: concept
status: developing
sources:
  - "[[2026-08-03_llm-security-basics-the-full-threat-model]]"
  - "[[2025-10-20_what-actually-happens-when-you-press-send-to-chatgpt]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - llm
  - security
  - agent
---

# LLM Security

## Định nghĩa

LLM security là việc thiết kế hệ thống quanh LLM để giới hạn rủi ro từ prompt, retrieval, model, tool, output, monitoring và supply chain.

## Cách hiểu bằng lời của tôi

Vấn đề gốc là LLM nhận instruction và data trong cùng một chuỗi token. Một email, web page, ticket hoặc document được retrieve có thể chứa chữ giống instruction và model có thể xử lý nó như lệnh thật. Vì vậy bảo mật LLM không thể chỉ là "lọc prompt"; phải kiểm soát cả context và quyền hành động.

## Threat model theo pipeline

- Input: direct [[Prompt Injection]] và tiêu thụ tài nguyên không kiểm soát.
- Retrieval: [[Indirect Prompt Injection]], poisoned knowledge base, embedding/vector weakness.
- Model: leakage, poisoning, system prompt exposure.
- Tools: [[Excessive Agency]] khi agent có quá nhiều quyền; [[Lethal Trifecta]] là cấu hình rủi ro nhất.
- Output: [[Untrusted Model Output]] chưa sanitize được đưa vào hệ thống downstream.
- Supply chain: [[LLM Supply Chain Security]] cho model, adapter, vector store hoặc tool bị compromise trước khi runtime bắt đầu.

## Defense in depth

- Validate input và giới hạn resource.
- Giữ retrieval source sạch, có provenance.
- Scope tool theo least privilege.
- Treat model output as untrusted trước khi dùng downstream.
- Monitor anomaly và log trajectory.
- Human review cho hành động hậu quả cao.
- Áp dụng [[Agents Rule of Two]] để không gom untrusted input, sensitive access và external action vào cùng agent tự trị.

## Liên kết

- [[Prompt Injection]]
- [[Indirect Prompt Injection]]
- [[Excessive Agency]]
- [[Lethal Trifecta]]
- [[Agents Rule of Two]]
- [[Untrusted Model Output]]
- [[LLM Supply Chain Security]]
- [[Tool Use]]
- [[Model Context Protocol]]
- [[Retrieval-Augmented Generation]]
- [[AI Hallucination]]
- [[LLM Evaluation]]
