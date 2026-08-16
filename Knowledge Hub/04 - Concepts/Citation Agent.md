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
  - evidence
---

# Citation Agent

## Định nghĩa

Citation Agent là agent chuyên kiểm tra claim, ghép citation với source đúng và đảm bảo output cuối có thể truy vết về bằng chứng.

## Cách hiểu bằng lời của tôi

Trong research agent, việc tìm nhiều thông tin chưa đủ. Cần một lớp kiểm chứng riêng để hỏi: claim này đến từ đâu, source có thật sự nói vậy không, và citation có bị gắn nhầm không. [[Citation Agent]] tách nhiệm vụ evidence grounding khỏi nhiệm vụ khám phá.

## Liên kết

- [[Evidence-Grounded Generation]]
- [[Citation Quality]]
- [[LLM-as-Judge]]
- [[Retrieval Evaluation]]
