---
type: concept
status: understood
sources:
  - "[[2026-06-30_inside-thinking-machines-interaction-models]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - llm
  - reasoning
  - inference
---

# Reasoning Model

## Định nghĩa

Reasoning Model (Mô hình lập luận) là lớp mô hình AI được tối ưu hóa đặc biệt để dành thêm tài nguyên tính toán ở thời gian suy luận (Test-Time Compute) thông qua các chuỗi suy nghĩ nội tại (internal Chain-of-Thought / reasoning tokens) nhằm giải quyết các bài toán toán học, lập trình và logic phức tạp.

## Cách hiểu bằng lời của tôi

Các LLM truyền thống trả lời ngay lập tức token đầu tiên (Zero-shot instant response). Ngược lại, Reasoning Model (như OpenAI o1/o3 hay DeepSeek R1) tự trò chuyện với chính nó trong một "nhật ký tư duy ẩn" trước khi đưa ra câu trả lời cuối cùng cho người dùng. Càng cho mô hình nhiều thời gian suy nghĩ, chất lượng câu trả lời càng tăng theo quy luật scaling law ở thời gian inference.

## Cơ chế Test-Time Compute

```text
User Question
-> Hidden Reasoning Loop (Thinking Tokens)
   - Self-Correction & Hypothesis Testing
   - Backtracking on Mistakes
   - Verification via Process Reward Model (PRM)
-> Final Answer Output
```

- **Process Reward Models (PRM)**: Đánh giá chính xác từng bước suy luận trung gian (step-by-step) thay vì chỉ đánh giá kết quả cuối cùng (Outcome Reward Model - ORM).
- **Reinforcement Learning on Reasoning**: Sử dụng RL để thưởng cho các chuỗi tư duy tự sửa lỗi (self-correction) hiệu quả.

## Trade-off

- **Latency cao hơn**: Người dùng phải đợi từ 5-30 giây (hoặc lâu hơn) để mô hình "suy nghĩ".
- **Chi phí Token**: Chi phí inference tăng do số lượng token tư duy ngầm sinh ra rất lớn.

## Liên kết

- [[Test-Time Compute]]
- [[Model Context Protocol]]
- [[LLM Inference Engineering]]
- [[Coding Agent]]
