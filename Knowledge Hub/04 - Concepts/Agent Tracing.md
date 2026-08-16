---
type: concept
status: developing
sources:
  - "[[2025-09-16_how-anthropic-built-a-multi-agent-research-system]]"
  - "[[2026-01-20_this-isnt-an-ai-summarizer-and-that-matters-byte-sized-design]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - agent
  - observability
---

# Agent Tracing

## Định nghĩa

Agent tracing là việc ghi lại đường đi của agent qua plan, tool call, observation, decision, retry, handoff và final answer để debug hoặc đánh giá.

## Cách hiểu bằng lời của tôi

Agent có thể trả lời sai vì rất nhiều bước nhỏ trước đó sai. Nếu chỉ nhìn output cuối, mình không biết lỗi do prompt, retrieval, tool, guardrail, citation hay decision dừng. Trace biến agent từ hộp đen thành chuỗi hành động có thể kiểm tra.

## Cần ghi

- Objective và plan ban đầu.
- Tool được chọn, input/output chính, lỗi và retry.
- Evidence nào được dùng cho claim nào.
- Điểm agent đổi hướng hoặc spawn subagent.
- Stop condition và confidence signal.

## Lưu ý bảo mật

Trace có thể chứa user content hoặc secret. Anthropic case nhấn mạnh production tracing cần tránh lưu sensitive content không cần thiết.

## Liên kết

- [[LLM Agent]]
- [[Multi-Agent System]]
- [[LLM Observability]]
- [[Tool Use]]
- [[LLM Security]]
