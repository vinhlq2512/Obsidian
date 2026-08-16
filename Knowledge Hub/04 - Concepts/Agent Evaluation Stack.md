---
type: concept
status: understood
sources:
  - "[[2026-07-18_mcp-vs-a2a-vs-acp-how-ai-agents-actually-talk-to-each-other]]"
  - "[[2025-09-16_how-anthropic-built-a-multi-agent-research-system]]"
  - "[[2026-01-26_how-cursor-shipped-its-coding-agent-to-production]]"
source_sections:
  - "[[2026-07-18_mcp-vs-a2a-vs-acp-how-ai-agents-actually-talk-to-each-other]]"
  - "[[2025-09-16_how-anthropic-built-a-multi-agent-research-system]]"
  - "[[2026-01-26_how-cursor-shipped-its-coding-agent-to-production]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - ai-agent
  - evaluation
---

# Agent Evaluation Stack

## Định nghĩa

Agent Evaluation Stack là tập eval nhiều lớp cho agent: task set, grader, code/test execution, LLM-as-judge, human review, trace analysis và adoption/usage signal.

## Cách hiểu bằng lời của tôi

Agent có nhiều điểm lỗi hơn LLM/RAG: retrieval sai, tool chọn sai, loop quá dài, patch hỏng, phối hợp subagent kém. Vì vậy eval phải đo outcome end-to-end và từng component quan trọng, không chỉ chấm câu trả lời cuối.

## Các lớp eval

- Coding agent: unit/integration tests trên patch cuối.
- Research agent: factuality, completeness, citation quality và source quality.
- Multi-agent: coordination, role adherence, duplication và tool efficiency.
- Production: user trust, adoption, rollback/incident signal.

## Liên kết

- [[Agent Evaluation]]
- [[LLM-as-Judge]]
- [[Retrieval Evaluation]]
- [[Citation Agent]]
- [[Agent Tracing]]
