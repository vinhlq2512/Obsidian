---
type: concept
status: developing
sources:
  - "[[2023 - Toolformer - Language Models Can Teach Themselves to Use Tools - arXiv 2302.04761v1]]"
  - "[[CS224N 2026 - Lecture 10 - RAG and Language Agents]]"
  - "[[2026-05-04_connecting-llms-to-the-real-world-tool-use-function-calling]]"
source_sections:
  - "[[CS224N 2026 - Lecture 10 - RAG and Language Agents]]"
first_seen: 2026-08-03
last_updated: 2026-08-16
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
- Model thường chỉ sinh yêu cầu gọi tool theo schema; application layer mới là nơi validate, execute và trả kết quả về model.
- Tool description cũng chiếm context, nên càng nhiều tool càng cần routing, filtering và quyền hạn rõ ràng.
- Tool use trong production cần chống hallucinated tool name, malformed args, side effect nguy hiểm và dữ liệu nhạy cảm.

## Từ ByteByteGo

ByteByteGo tách rõ [[Function Calling]] và [[Model Context Protocol]]: function calling là cách model yêu cầu app gọi một hàm cụ thể, còn MCP là chuẩn kết nối host/client/server để giảm bài toán tích hợp từ N x M xuống N + M. Điểm thực dụng là LLM không "tự hành động"; phần mềm xung quanh nó phải kiểm tra schema, quyền, lỗi và bước cần human approval.

## Liên kết

- [[LLM Agent]]
- [[Retrieval-Augmented Generation]]
- [[Function Calling]]
- [[Model Context Protocol]]
- [[Agentic Loop]]
- [[2023 - Toolformer - Language Models Can Teach Themselves to Use Tools - arXiv 2302.04761v1]]
- [[CS224N]]
