---
type: concept
status: understood
sources:
  - "[[2025-09-16_how-anthropic-built-a-multi-agent-research-system]]"
source_sections:
  - "[[2025-09-16_how-anthropic-built-a-multi-agent-research-system]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - ai-agent
  - reliability
---

# Agent State Checkpointing

## Định nghĩa

Agent State Checkpointing là cơ chế lưu trạng thái tiến độ, plan, intermediate results và tool context để agent dài hơi có thể recover hoặc tiếp tục sau lỗi.

## Cách hiểu bằng lời của tôi

Agent production khác chatbot ở chỗ nó có thể chạy lâu qua nhiều tool call. Nếu một tool lỗi hoặc deployment đổi version, bắt đầu lại từ đầu vừa tốn tiền vừa dễ mất work. Checkpoint giúp agent resume gần điểm lỗi.

## Liên kết

- [[Agentic Loop]]
- [[Workflow Orchestration]]
- [[Retry Pattern]]
- [[Agent Tracing]]
- [[Rollback Strategy]]
