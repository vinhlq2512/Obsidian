---
type: concept
status: developing
sources:
  - "[[2024 - Scaling LLM Test-Time Compute Optimally Can Be More Effective Than Scaling Model Parameters - arXiv 2408.03314v1]]"
  - "[[CS224N 2026 - Lecture 12 - Reasoning Part 1]]"
  - "[[CS224N 2026 - Lecture 13 - Reasoning Part 2]]"
source_sections:
  - "[[CS224N 2026 - Lecture 12 - Reasoning Part 1]]"
first_seen: 2026-08-03
last_updated: 2026-08-03
tags:
  - concept
  - llm
  - cs224n
---

# Test-Time Compute

## Định nghĩa

Test-time compute là lượng compute dùng trong lúc inference để cải thiện output mà không cập nhật trọng số model.

## Cách hiểu bằng lời của tôi

Thay vì làm model lớn hơn, ta cho model thêm thời gian và quy trình suy nghĩ: lấy nhiều mẫu, kiểm chứng, tìm kiếm, dùng verifier hoặc gọi tool.

## Ví dụ

- [[Self-Consistency Decoding]].
- Sinh nhiều candidates rồi rerank.
- Verifier chấm từng bước.
- Search/planning trong agent.

## Trade-off

- Tăng chất lượng trên bài khó.
- Tăng latency và cost.
- Cần chính sách phân bổ compute theo độ khó, nếu không sẽ lãng phí.

## Liên kết

- [[Speculative Decoding]]
- [[Chain-of-Thought Prompting]]
- [[Prompt Engineering]]
- [[LLM Agent]]
- [[CS224N]]
