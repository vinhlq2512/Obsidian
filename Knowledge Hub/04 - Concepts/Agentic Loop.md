---
type: concept
status: developing
sources:
  - "[[2026-05-16_ep215-the-anatomy-of-an-ai-agent]]"
  - "[[2026-03-23_how-agentic-rag-works]]"
  - "[[2026-07-08_the-agent-loop-how-ai-goes-from-answering-questions-to-doing]]"
  - "[[2026-03-18_how-openai-codex-works]]"
  - "[[2026-07-29_how-chatgpt-optimizes-its-agent-loop-harness-api-and-inferen]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - agent
  - llm
---

# Agentic Loop

## Định nghĩa

Agentic loop là vòng lặp observe -> decide -> act -> observe trong đó LLM agent dùng trạng thái hiện tại, chọn bước tiếp theo, gọi tool nếu cần, rồi cập nhật context từ kết quả.

## Cách hiểu bằng lời của tôi

Khác với prompt một lần, agentic loop biến LLM thành bộ điều khiển có feedback. Mỗi tool call là một lần agent kiểm tra thế giới, không phải chỉ tưởng tượng trong đầu.

## Cần biết

- Loop cần điều kiện dừng: task done, quá số bước, timeout, lỗi không phục hồi, hoặc cần user approval.
- Observation phải đủ gọn và đúng cấu trúc để không làm context phình ra.
- Logging trajectory quan trọng hơn log câu trả lời cuối, vì lỗi thường nằm ở bước chọn tool hoặc đọc observation.
- Loop càng dài thì chi phí, latency và nguy cơ drift càng cao.
- Trong coding agent, mỗi vòng thường là search/read/edit/run-test rồi đưa output về context.
- Optimization của loop thường là tránh trả tiền hai lần cho cùng một work: giữ WebSocket, stable prompt prefix, delta tokenization, cache-aware routing.

## Liên kết

- [[LLM Agent]]
- [[Agent Harness]]
- [[Tool Use]]
- [[Function Calling]]
- [[Agentic RAG]]
- [[LLM Evaluation]]
