---
type: concept
status: developing
sources:
  - "[[2026-08-04_why-an-llms-memory-gets-expensive-and-how-to-fix-it]]"
  - "[[2026-04-06_a-guide-to-context-engineering-for-llms]]"
  - "[[2026-06-29_how-ai-agents-manage-memory-and-avoid-forgetfulness]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - llm
  - memory
  - agent
---

# LLM Memory

## Định nghĩa

LLM memory là các cơ chế giúp hệ thống giữ hoặc khôi phục thông tin qua nhiều lượt gọi model, từ context ngắn hạn trong prompt tới bộ nhớ dài hạn nằm ngoài model.

## Cách hiểu bằng lời của tôi

Model gốc không nhớ giữa các API call. Thứ ta gọi là memory thường là hệ thống bao quanh model: conversation history, summary, file, vector store, database, cache hoặc rule được chèn lại vào context đúng lúc.

## Các lớp memory

- Short-term memory: context window hiện tại và lịch sử hội thoại được giữ lại.
- Working memory: scratchpad, plan, state hoặc tool result đang dùng cho task.
- Long-term memory: preference, project facts, profile, documents hoặc vector store.
- Hardware/runtime memory: [[KV Cache]] phục vụ inference, không giống memory tri thức.

## Trade-off

- Giữ nhiều memory làm context đắt và dễ nhiễu.
- Nén memory tiết kiệm token nhưng có thể làm mất chi tiết quan trọng.
- Retrieval memory cần tiêu chí relevance tốt, nếu không sẽ đưa ký ức sai vào prompt.
- Memory liên quan đến quyền riêng tư, retention và khả năng người dùng sửa/xóa.

## Liên kết

- [[Context Engineering]]
- [[LLM Agent]]
- [[KV Cache]]
- [[Retrieval-Augmented Generation]]
