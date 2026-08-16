---
type: synthesis
status: seed
concepts:
  - "[[LLM Security]]"
  - "[[Prompt Injection]]"
  - "[[Indirect Prompt Injection]]"
  - "[[Excessive Agency]]"
  - "[[Lethal Trifecta]]"
  - "[[Agents Rule of Two]]"
  - "[[Untrusted Model Output]]"
  - "[[LLM Supply Chain Security]]"
  - "[[RAG Knowledge Base Poisoning]]"
sources:
  - "[[2026-08-03_llm-security-basics-the-full-threat-model]]"
questions: []
created_at: 2026-08-16
updated_at: 2026-08-16
tags:
  - synthesis
  - llm
  - security
---

# LLM Threat Model and Agent Security

## Luận điểm chính

Threat model của LLM bắt đầu từ việc instruction và data cùng đi vào một chuỗi token. Vì vậy rủi ro không chỉ nằm ở prompt input, mà trải qua retrieval, model, tool, output, monitoring và supply chain.

## Bản đồ rủi ro

- Input: [[Prompt Injection]] trực tiếp và tiêu thụ tài nguyên không kiểm soát.
- Retrieval: [[Indirect Prompt Injection]] và [[RAG Knowledge Base Poisoning]].
- Tool/action: [[Excessive Agency]] và [[Lethal Trifecta]].
- Output: [[Untrusted Model Output]] trước khi render, execute hoặc ghi downstream.
- Supply chain: [[LLM Supply Chain Security]] cho model, adapter, vector store và tool server.

## Defense posture

Không có một filter đủ mạnh để giữ mọi thứ. Cách bền hơn là defense in depth: giảm quyền tool, tách untrusted content khỏi privileged action, giữ provenance, validate/sanitize output, monitor anomaly và dùng human review cho action hậu quả cao. [[Agents Rule of Two]] là checklist nhanh để tránh gom ba capability nguy hiểm vào cùng agent.

## Liên kết

- [[Least Privilege]]
- [[Safe Outputs Pipeline]]
- [[Model Context Protocol]]
- [[Agent Trust Boundary Logging]]
- [[Retrieval-Augmented Generation]]
