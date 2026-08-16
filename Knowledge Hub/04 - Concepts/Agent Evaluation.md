---
type: concept
status: developing
sources:
  - "[[2025-09-16_how-anthropic-built-a-multi-agent-research-system]]"
  - "[[2026-01-20_this-isnt-an-ai-summarizer-and-that-matters-byte-sized-design]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - agent
  - evaluation
---

# Agent Evaluation

## Định nghĩa

Agent evaluation là đánh giá hệ agent theo outcome và trajectory, gồm chất lượng kết quả, tool efficiency, evidence use, citation, stop behavior và khả năng phục hồi lỗi.

## Cách hiểu bằng lời của tôi

Agent không chạy cùng một path mỗi lần, nên test kiểu so chuỗi output rất yếu. Cần chấm liệu agent có tìm đúng bằng chứng, tránh nguồn kém, dùng tool hợp lý, không hallucinate confidence và dừng khi đủ thông tin chưa.

## Rubric từ ByteByteGo

- Factual accuracy.
- Citation quality.
- Completeness.
- Source quality.
- Tool efficiency.
- Pass/fail grade theo ngưỡng sản phẩm.

## Ghi nhớ

LLM-as-judge hữu ích để scale eval, nhưng cần calibrate với human reviewers, nhất là edge case, hallucination và bias về nguồn SEO-heavy.

## Liên kết

- [[LLM Evaluation]]
- [[LLM-as-Judge]]
- [[Agent Tracing]]
- [[Multi-Agent System]]
- [[AI Hallucination]]
