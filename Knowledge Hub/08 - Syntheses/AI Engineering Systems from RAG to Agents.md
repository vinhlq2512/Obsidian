---
type: synthesis
status: developing
concepts:
  - "[[Retrieval-Augmented Generation]]"
  - "[[Agentic RAG]]"
  - "[[LLM Agent]]"
  - "[[Tool Use]]"
  - "[[Model Context Protocol]]"
  - "[[Agent Harness]]"
  - "[[Coding Agent]]"
  - "[[Context Engineering]]"
  - "[[LLM Evaluation]]"
sources:
  - "[[2026-05-23_ep216-rags-vs-agents]]"
  - "[[2026-05-16_ep215-the-anatomy-of-an-ai-agent]]"
  - "[[2026-05-04_connecting-llms-to-the-real-world-tool-use-function-calling]]"
  - "[[2026-04-06_a-guide-to-context-engineering-for-llms]]"
  - "[[2026-01-12_a-guide-to-llm-evals]]"
  - "[[2026-03-18_how-openai-codex-works]]"
created_at: 2026-08-16
updated_at: 2026-08-16
tags:
  - synthesis
  - llm
  - ai-engineering
---

# AI Engineering Systems from RAG to Agents

## Luồng tổng quát

Cụm bài ByteByteGo về AI engineering cho thấy một phổ kiến trúc:

- [[Retrieval-Augmented Generation]]: retrieve context liên quan rồi generate.
- [[Agentic RAG]]: thêm loop để refine query, route nguồn và self-evaluate retrieval.
- [[LLM Agent]]: dùng [[Agentic Loop]] và [[Tool Use]] để hành động nhiều bước.
- [[Coding Agent]]: áp agent loop vào codebase với tool đọc/sửa/chạy test.
- [[Multi-Agent System]]: tách task thành nhiều context riêng khi một agent quá tải.

## Mental model

RAG giải bài toán "model cần biết gì". Agent giải bài toán "model cần làm gì tiếp". Context engineering giải bài toán "model nên thấy gì ở đúng thời điểm". LLM evaluation giải bài toán "làm sao biết thay đổi này thật sự tốt hơn".

## Quyết định thiết kế

| Nhu cầu | Pattern hợp lý | Cẩn thận |
|---|---|---|
| Hỏi đáp trên tài liệu sạch | [[Retrieval-Augmented Generation]] | Retrieval phải đúng và context không nhiễu |
| Câu hỏi mơ hồ, nhiều nguồn | [[Agentic RAG]] | Latency/cost tăng theo số vòng |
| Cần gọi API hoặc thao tác | [[LLM Agent]] + [[Tool Use]] | Guardrail, permission, logging |
| Nhiều nhánh nghiên cứu song song | [[Multi-Agent System]] | Token cost, tổng hợp kết quả, tracing |
| Production cần đo chất lượng | [[LLM Evaluation]] | Eval set phải đại diện và được version |
| Context dài, tool output nhiều | [[Context Engineering]] | Compression có thể làm mất chi tiết |

## Ghi nhớ

Không nên mặc định "agent hóa" mọi thứ. Nếu tri thức nằm trong một corpus sạch và query đơn giản, RAG chuẩn thường dễ vận hành hơn. Agentic loop đáng tiền khi hệ thống cần quyết định lại giữa chừng: chọn nguồn khác, gọi tool khác, kiểm tra kết quả, hoặc sửa kế hoạch.

## Liên kết

- [[LLM]]
- [[System Design]]
- [[Scalable Distributed Systems Patterns]]
- [[AI Hallucination]]
- [[LLM Inference Engineering]]
- [[Coding Agent System Design]]
