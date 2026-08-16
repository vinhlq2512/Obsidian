---
type: synthesis
status: seed
concepts:
  - "[[Agent Orchestrator-Worker Pattern]]"
  - "[[Citation Agent]]"
  - "[[Agent Effort Scaling]]"
  - "[[Agent State Checkpointing]]"
  - "[[Diff Problem]]"
  - "[[Sandboxed Agent Execution]]"
  - "[[Zero-Secret Agent Architecture]]"
  - "[[Safe Outputs Pipeline]]"
  - "[[Agent Trust Boundary Logging]]"
  - "[[Agent Protocol Interoperability]]"
  - "[[Agent Evaluation Stack]]"
sources:
  - "[[2025-09-16_how-anthropic-built-a-multi-agent-research-system]]"
  - "[[2026-01-26_how-cursor-shipped-its-coding-agent-to-production]]"
  - "[[2026-04-20_the-security-architecture-of-github-agentic-workflow]]"
  - "[[2026-07-18_mcp-vs-a2a-vs-acp-how-ai-agents-actually-talk-to-each-other]]"
questions: []
created_at: 2026-08-16
updated_at: 2026-08-16
tags:
  - synthesis
  - ai-agent
  - system-design
---

# Production Agent Platform Patterns

## Mental model

Production agent không phải một prompt hay một model. Nó là platform gồm model, orchestrator, tool harness, context retrieval, sandbox, security boundary, eval stack, tracing và rollout strategy. Càng agentic, hệ thống càng phải coi model như thành phần không deterministic cần containment.

## Các lớp thiết kế

| Lớp | Concept | Câu hỏi cần trả lời |
| --- | --- | --- |
| Orchestration | [[Agent Orchestrator-Worker Pattern]], [[Agent Effort Scaling]] | Task có đáng parallelize không, và effort có khớp độ khó không? |
| Evidence | [[Citation Agent]], [[Evidence-Grounded Generation]] | Claim cuối có truy vết được về source không? |
| Reliability | [[Agent State Checkpointing]], [[Agent Tracing]] | Agent dài hơi recover và debug thế nào? |
| Coding workflow | [[Diff Problem]], [[Sandboxed Agent Execution]] | Patch có apply đúng và được verify an toàn không? |
| Security | [[Zero-Secret Agent Architecture]], [[Safe Outputs Pipeline]], [[Agent Trust Boundary Logging]] | Agent bị prompt-injected thì blast radius dừng ở đâu? |
| Protocol | [[Agent Protocol Interoperability]], [[Model Context Protocol]] | Tool/agent/server giao tiếp bằng contract nào? |
| Evaluation | [[Agent Evaluation Stack]], [[LLM-as-Judge]] | Evals bắt lỗi end-to-end và lỗi từng layer chưa? |

## Bài học

- Multi-agent phù hợp bài toán cần breadth; coding thường cần coordination chặt hơn nên không tự động hưởng lợi.
- Tool description là API design cho model; mô tả kém làm agent chọn sai tool.
- Coding agent production cần giải diff problem, latency compound và sandbox startup.
- Agent security nên dựa vào architecture: agent không thấy secret, output bị vet, trust boundary được log.
- Eval agent phải đo task outcome, tool efficiency, evidence quality và user trust.

## Liên kết

- [[Coding Agent System Design]]
- [[AI Engineering Systems from RAG to Agents]]
- [[Production AI Evaluation and Observability]]
- [[LLM Security]]
