---
type: concept
status: developing
sources:
  - "[[2025-09-16_how-anthropic-built-a-multi-agent-research-system]]"
  - "[[2026-02-09_how-yelp-built-yelp-assistant]]"
  - "[[2026-01-20_this-isnt-an-ai-summarizer-and-that-matters-byte-sized-design]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - llm
  - observability
  - production
---

# LLM Observability

## Định nghĩa

LLM observability là khả năng theo dõi, truy vết và phân tích hành vi của hệ thống LLM/agent trong production: prompt, retrieval, tool calls, guardrails, latency, token cost, citation và outcome quality.

## Cách hiểu bằng lời của tôi

Với app thường, log request/response đã giúp nhiều. Với LLM system, lỗi thường nằm trong đường đi: model chọn source sai, tool call thừa, prompt phình lên, retrieval lấy nhầm evidence, hoặc agent dừng quá sớm. Vì vậy cần nhìn được trajectory, không chỉ output cuối.

## Tín hiệu nên đo

- Latency breakdown: analysis, retrieval, time-to-first-byte, generation.
- Token count và cost theo prompt chunks, retrieved context, tool loop.
- Retrieval quality: source nào được chọn, evidence nào bị bỏ qua.
- Guardrail decisions: blocked, routed, early-stopped.
- Citation quality và grounding.
- Agent path: plan, tool calls, retries, stop reason.

## Liên kết

- [[LLM Evaluation]]
- [[Agent Tracing]]
- [[Retrieval Evaluation]]
- [[Model Benchmarking]]
- [[Observability]]
