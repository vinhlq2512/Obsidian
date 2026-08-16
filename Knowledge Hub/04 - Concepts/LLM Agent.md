---
type: concept
status: seed
sources:
  - "[[Hands-On LLM - Chapter 07 - Advanced Text Generation Techniques and Tools]]"
  - "[[2026-05-16_ep215-the-anatomy-of-an-ai-agent]]"
  - "[[2026-05-23_ep216-rags-vs-agents]]"
  - "[[2026-03-18_how-openai-codex-works]]"
  - "[[2026-07-29_how-chatgpt-optimizes-its-agent-loop-harness-api-and-inferen]]"
last_updated: 2026-08-16
tags:
  - concept
  - agent
  - llm
---

# LLM Agent

## Định nghĩa

LLM Agent là hệ thống dùng LLM để quyết định bước tiếp theo, gọi tool và lặp lại cho tới khi hoàn thành nhiệm vụ.

## Cách hiểu bằng lời của tôi

Agent không chỉ trả lời một lần. Nó quan sát, suy luận, hành động, nhận kết quả, rồi tiếp tục. Vì vậy nó linh hoạt hơn chain nhưng cũng khó kiểm soát hơn.

## Cần biết

- Agent phù hợp với task nhiều bước và cần tool use.
- ReAct là pattern kết hợp reasoning và acting.
- Production agent cần logging, guardrails, timeout và giới hạn quyền.
- Một agent thực tế thường có brain, perception, tools, memory và loop điều khiển.
- Agent nên dùng khi hệ thống cần hành động, quyết định nhiều bước, hoặc tự sửa hướng đi; nếu chỉ cần trả lời từ tài liệu sạch thì [[Retrieval-Augmented Generation]] thường rẻ và dễ debug hơn.

## Từ ByteByteGo

ByteByteGo mô tả agent gần như một vòng lặp: nhận trạng thái, quyết định bước tiếp theo, gọi tool nếu cần, đọc observation, rồi lặp lại. Vì vậy năng lực của agent không chỉ nằm ở model, mà nằm ở cách thiết kế [[Agentic Loop]], [[Tool Use]], [[LLM Memory]] và [[Context Engineering]].

Với Codex/ChatGPT Work, ByteByteGo tách rõ model và [[Agent Harness]]. Model dự đoán token hoặc tool call; harness mới là lớp chạy command, quản lý sandbox, thu output, áp approval policy và quyết định loop có tiếp tục không. Đây là lý do "agent" nên được hiểu là system, không phải một model đơn lẻ.

## Liên kết

- [[Prompt Engineering]]
- [[Generative Model]]
- [[Retrieval-Augmented Generation]]
- [[Agentic Loop]]
- [[Tool Use]]
- [[LLM Memory]]
- [[Model Context Protocol]]
- [[Agent Harness]]
- [[Coding Agent]]
