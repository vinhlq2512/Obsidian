---
type: concept
status: seed
source:
  - "[[Hands-On LLM - Chapter 07 - Advanced Text Generation Techniques and Tools]]"
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

## Liên kết

- [[Prompt Engineering]]
- [[Generative Model]]
- [[Retrieval-Augmented Generation]]

