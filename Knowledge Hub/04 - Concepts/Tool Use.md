---
type: concept
status: developing
sources:
  - "[[2023 - Toolformer - Language Models Can Teach Themselves to Use Tools - arXiv 2302.04761v1]]"
  - "[[CS224N 2026 - Lecture 10 - RAG and Language Agents]]"
source_sections:
  - "[[CS224N 2026 - Lecture 10 - RAG and Language Agents]]"
first_seen: 2026-08-03
last_updated: 2026-08-03
tags:
  - concept
  - agent
  - cs224n
---

# Tool Use

## Định nghĩa

Tool use là khả năng model hoặc agent gọi công cụ bên ngoài, như search, calculator, database, retriever hoặc API, để hoàn thành task.

## Cách hiểu bằng lời của tôi

Tool use biến LLM từ người chỉ nói thành người có thể thao tác. Model không cần tự nhớ hoặc tự tính mọi thứ nếu biết khi nào nên gọi công cụ đúng.

## Cần biết

- Model phải học khi nào gọi tool, gọi với tham số gì và dùng observation ra sao.
- Tool result là dữ liệu đầu vào mới, không phải sự thật tuyệt đối.
- Agent evaluation cần chấm cả trajectory tool calls.

## Liên kết

- [[LLM Agent]]
- [[Retrieval-Augmented Generation]]
- [[2023 - Toolformer - Language Models Can Teach Themselves to Use Tools - arXiv 2302.04761v1]]
- [[CS224N]]
