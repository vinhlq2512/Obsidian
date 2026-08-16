---
type: concept
status: developing
sources:
  - "[[2026-08-04_why-an-llms-memory-gets-expensive-and-how-to-fix-it]]"
  - "[[2026-06-15_a-guide-to-ai-inference-engineering]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - llm
  - inference
  - memory
---

# KV Cache

## Định nghĩa

KV cache là bộ nhớ lưu key/value vectors từ attention của các token đã xử lý, để LLM không phải tính lại toàn bộ lịch sử khi sinh token tiếp theo.

## Cách hiểu bằng lời của tôi

Khi model đang trả lời, nó cần nhìn lại những token trước đó. KV cache giống bảng ghi nhớ trung gian cho attention: đã tính phần quá khứ rồi thì giữ lại để bước decode sau đọc nhanh hơn.

## Cần biết

- Prefill tạo KV cache cho prompt ban đầu.
- Decode dùng KV cache để sinh từng token tiếp theo.
- Context càng dài và số user đồng thời càng cao thì KV cache càng tốn GPU memory.
- Prefix caching tận dụng phần prefix giống nhau giữa nhiều request để giảm prefill.
- KV cache là memory runtime, không phải memory tri thức lâu dài của agent.

## Liên kết

- [[Transformer Inference Optimization]]
- [[LLM Inference Engineering]]
- [[LLM Memory]]
- [[Self-Attention]]
