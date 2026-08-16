---
type: concept
status: understood
sources:
  - "[[2026-04-20_the-security-architecture-of-github-agentic-workflow]]"
  - "[[2025-09-16_how-anthropic-built-a-multi-agent-research-system]]"
source_sections:
  - "[[2026-04-20_the-security-architecture-of-github-agentic-workflow]]"
  - "[[2025-09-16_how-anthropic-built-a-multi-agent-research-system]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - ai-agent
  - observability
---

# Agent Trust Boundary Logging

## Định nghĩa

Agent Trust Boundary Logging là practice ghi log tại mọi ranh giới agent đi qua: network proxy, model API proxy, MCP gateway, tool invocation, filesystem access và safe output stage.

## Cách hiểu bằng lời của tôi

Agent khó debug vì đường đi không deterministic. Muốn forensic sau incident hoặc policy violation, phải log tại trust boundary chứ không chỉ log transcript cuối. GitHub coi mỗi điểm quan sát là điểm có thể kiểm soát trong tương lai.

## Liên kết

- [[Agent Tracing]]
- [[LLM Observability]]
- [[Distributed Tracing]]
- [[Zero-Secret Agent Architecture]]
- [[Safe Outputs Pipeline]]
