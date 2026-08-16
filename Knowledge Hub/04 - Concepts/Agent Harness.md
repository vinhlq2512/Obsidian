---
type: concept
status: developing
sources:
  - "[[2026-03-18_how-openai-codex-works]]"
  - "[[2026-07-29_how-chatgpt-optimizes-its-agent-loop-harness-api-and-inferen]]"
  - "[[2026-01-26_how-cursor-shipped-its-coding-agent-to-production]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - agent
  - llm
  - production
---

# Agent Harness

## Định nghĩa

Agent harness là lớp orchestration bao quanh LLM, chịu trách nhiệm lắp context, gọi model, parse tool call, thực thi tool trong môi trường kiểm soát, đưa observation trở lại và điều khiển vòng lặp agent.

## Cách hiểu bằng lời của tôi

Model chỉ dự đoán token. Harness biến token đó thành hành động có kiểm soát. Nếu model nói "hãy chạy test", harness mới quyết định có được chạy không, chạy ở đâu, lấy output thế nào, và đưa phần nào quay lại context.

## Trách nhiệm chính

- Quản lý conversation history và context gửi cho model.
- Expose tool schema và áp policy/approval khi tool được gọi.
- Chạy command hoặc thao tác file trong sandbox.
- Stream progress, diff hoặc event về client.
- Compact history khi context quá dài.
- Ghi log trajectory để debug và eval.

## Optimization

- Persistent WebSocket giảm chi phí mở kết nối trong loop dài.
- Stable prompt prefix giữ prompt cache hit.
- Deferred tool discovery tránh đưa mọi tool schema vào prompt.
- Delta tokenization chỉ xử lý phần mới thay vì retokenize toàn bộ history.

## Liên kết

- [[LLM Agent]]
- [[Agentic Loop]]
- [[Tool Use]]
- [[Context Engineering]]
- [[LLM Security]]
- [[AI Model Serving]]
