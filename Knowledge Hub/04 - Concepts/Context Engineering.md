---
type: concept
status: developing
sources:
  - "[[2026-04-06_a-guide-to-context-engineering-for-llms]]"
  - "[[2026-05-16_ep215-the-anatomy-of-an-ai-agent]]"
  - "[[2026-03-18_how-openai-codex-works]]"
  - "[[2026-07-29_how-chatgpt-optimizes-its-agent-loop-harness-api-and-inferen]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - llm
  - agent
  - production
---

# Context Engineering

## Định nghĩa

Context engineering là việc thiết kế, chọn, nén, sắp xếp và cô lập toàn bộ thông tin đi vào context window trước khi LLM sinh câu trả lời.

## Cách hiểu bằng lời của tôi

Prompt engineering hỏi "nói thế nào cho model hiểu". Context engineering hỏi rộng hơn: "model cần thấy gì ở lượt này, thứ gì nên bỏ ra ngoài, thứ gì cần nén, thứ gì nên giao cho agent khác".

## Vấn đề chính

- Context window hữu hạn và attention không phân bổ đều.
- Thông tin ở giữa prompt dài dễ bị bỏ qua hơn đầu/cuối.
- Thêm context không luôn tốt; thông tin gần đúng nhưng không liên quan có thể thành nhiễu.
- LLM stateless, nên memory thực tế thường là hệ thống bên ngoài được chọn lọc đưa vào prompt.

## Bốn chiến lược

- Write: lưu thông tin ra ngoài context, ví dụ scratchpad hoặc long-term memory.
- Select: chỉ retrieve phần liên quan, ví dụ [[Retrieval-Augmented Generation]].
- Compress: tóm tắt, trim hoặc rút gọn tool output.
- Isolate: chia việc cho nhiều agent có context riêng.

## Trong agent production

- Stable prompt prefix giữ prompt caching hiệu quả; thay đổi thứ tự tool schema cũng có thể phá cache.
- Deferred tool discovery chỉ đưa core tools vào context, còn tool hiếm dùng được tìm bằng tool search khi cần.
- Conversation compaction giảm history dài, nhưng phải giữ quyết định quan trọng.
- Code mode/programmatic tool calls có thể giữ dữ liệu trung gian ngoài prompt và chỉ trả kết quả gọn vào context.

## Liên kết

- [[Prompt Engineering]]
- [[Retrieval-Augmented Generation]]
- [[LLM Memory]]
- [[Multi-Agent System]]
- [[Tool Use]]
- [[Agent Harness]]
