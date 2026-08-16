---
type: concept
status: developing
sources:
  - "[[2025-09-16_how-anthropic-built-a-multi-agent-research-system]]"
  - "[[2026-04-06_a-guide-to-context-engineering-for-llms]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - agent
  - llm
  - architecture
---

# Multi-Agent System

## Định nghĩa

Multi-agent system là kiến trúc chia một nhiệm vụ phức tạp cho nhiều agent, mỗi agent có context, tool và vai trò riêng, rồi hợp nhất kết quả ở agent điều phối hoặc bước tổng hợp.

## Cách hiểu bằng lời của tôi

Thay vì nhồi mọi thứ vào một context rất dài, ta chia não làm nhiều workspace nhỏ. Một agent nghiên cứu, một agent kiểm chứng, một agent viết, hoặc nhiều sub-agent chạy song song trên các nhánh tìm kiếm khác nhau.

## Khi hữu ích

- Nhiệm vụ có thể phân rã độc lập.
- Cần tìm kiếm rộng, nhiều nguồn hoặc nhiều giả thuyết.
- Context của từng vai trò khác nhau và dễ làm nhiễu nhau nếu đặt chung.

## Trade-off

- Có thể tăng chất lượng nhờ context sạch và song song hóa.
- Chi phí token tăng mạnh vì nhiều agent dùng context riêng.
- Cần checkpoint, retry, tracing và cách tổng hợp kết quả đáng tin.
- Không phải task nào cũng đáng dùng multi-agent; nhiều workflow ổn hơn với một agent và context compression tốt.

## Production notes từ Anthropic

Anthropic case cho thấy multi-agent hợp với research rộng, nhưng production cần rubric eval, [[Agent Tracing]], durable recovery, prompt/tool description rõ và rollout thận trọng. Một thay đổi prompt nhỏ có thể làm division of labor hoặc tool choice đổi mạnh.

## Liên kết

- [[LLM Agent]]
- [[Context Engineering]]
- [[Agentic Loop]]
- [[LLM Evaluation]]
- [[Agent Evaluation]]
- [[Agent Tracing]]
