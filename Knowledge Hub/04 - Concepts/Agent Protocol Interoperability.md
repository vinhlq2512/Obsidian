---
type: concept
status: understood
sources:
  - "[[2026-07-18_mcp-vs-a2a-vs-acp-how-ai-agents-actually-talk-to-each-other]]"
  - "[[2025-09-16_how-anthropic-built-a-multi-agent-research-system]]"
source_sections:
  - "[[2026-07-18_mcp-vs-a2a-vs-acp-how-ai-agents-actually-talk-to-each-other]]"
  - "[[2025-09-16_how-anthropic-built-a-multi-agent-research-system]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - ai-agent
  - protocol
---

# Agent Protocol Interoperability

## Định nghĩa

Agent Protocol Interoperability là khả năng agent, tool, server hoặc agent khác giao tiếp qua protocol/contract đủ rõ để tích hợp mà không cần coupling riêng cho từng vendor.

## Cách hiểu bằng lời của tôi

Khi agent cần tool và agent khác, vấn đề không còn là "LLM gọi API" đơn giản. Cần protocol mô tả capability, schema, auth, state và audit. MCP là một lớp quan trọng cho agent-tool, còn các protocol agent-agent nhắm tới phối hợp giữa agent.

## Liên kết

- [[Model Context Protocol]]
- [[Tool Use]]
- [[API Protocol]]
- [[Multi-Agent System]]
- [[Agent Harness]]
