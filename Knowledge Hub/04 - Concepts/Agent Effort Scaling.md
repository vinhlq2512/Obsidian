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
  - evaluation
---

# Agent Effort Scaling

## Định nghĩa

Agent Effort Scaling là kỹ thuật gắn mức effort của agent với độ phức tạp nhiệm vụ, ví dụ số subagent, số tool call, độ sâu tìm kiếm và thời gian chạy.

## Cách hiểu bằng lời của tôi

Agent thường không tự biết nên đầu tư bao nhiêu. Nếu không có guideline, bài đơn giản có thể bị over-search, còn bài khó lại thiếu coverage. Anthropic viết quy tắc effort vào prompt để lead agent chọn số subagent/tool call phù hợp.

## Ví dụ guideline

- Fact check đơn giản: một agent, ít tool call.
- So sánh trực tiếp: vài subagent, mỗi subagent có scope riêng.
- Research phức tạp: nhiều subagent chạy song song, có phân công rõ để tránh trùng lặp.

## Liên kết

- [[Agent Orchestrator-Worker Pattern]]
- [[Cost Optimization]]
- [[Agent Evaluation]]
- [[Context Engineering]]
