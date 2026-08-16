---
type: synthesis
status: developing
concepts:
  - "[[AI Model Serving]]"
  - "[[LLM Inference Engineering]]"
  - "[[AI Hardware Accelerator]]"
  - "[[Agent Harness]]"
  - "[[Model Router]]"
  - "[[Context Engineering]]"
  - "[[LLM Security]]"
  - "[[LLM Evaluation]]"
  - "[[LLM Observability]]"
  - "[[Evidence-Grounded Generation]]"
sources:
  - "[[2025-10-20_what-actually-happens-when-you-press-send-to-chatgpt]]"
  - "[[2025-07-29_how-cursor-serves-billions-of-ai-code-completions-every-day]]"
  - "[[2026-07-01_how-openai-delivers-low-latency-voice-ai-for-900m-users]]"
  - "[[2026-06-15_a-guide-to-ai-inference-engineering]]"
  - "[[2026-08-03_llm-security-basics-the-full-threat-model]]"
  - "[[2026-07-29_how-chatgpt-optimizes-its-agent-loop-harness-api-and-inferen]]"
  - "[[2025-09-16_how-anthropic-built-a-multi-agent-research-system]]"
  - "[[2026-02-09_how-yelp-built-yelp-assistant]]"
  - "[[2026-01-20_this-isnt-an-ai-summarizer-and-that-matters-byte-sized-design]]"
created_at: 2026-08-16
updated_at: 2026-08-16
tags:
  - synthesis
  - llm
  - production
  - system-design
---

# Production LLM System Design

## Luồng hệ thống

Production LLM system không chỉ là model endpoint. Một request thật thường đi qua auth, context assembly, tokenization, inference, streaming, tool execution, safety checks, memory retrieval, logging và monitoring.

```text
user/client
-> gateway / auth
-> context engineering
-> model serving / inference
-> streaming or action loop
-> safety and output handling
-> observability and eval feedback
```

## Các trục thiết kế

| Trục | Câu hỏi cần hỏi | Concept liên quan |
|---|---|---|
| Latency | User cần thấy token/action nhanh đến mức nào? | [[LLM Inference Engineering]], [[AI Model Serving]] |
| Context | Model cần thấy gì và bỏ gì? | [[Context Engineering]], [[LLM Memory]] |
| Hardware | Bottleneck là compute hay memory bandwidth? | [[AI Hardware Accelerator]], [[KV Cache]] |
| Tool/action | Model có quyền làm gì ngoài việc trả lời? | [[Tool Use]], [[Excessive Agency]] |
| Security | Untrusted content đi vào đâu, outbound channel ở đâu? | [[LLM Security]], [[Prompt Injection]] |
| Quality | Làm sao biết version mới tốt hơn? | [[LLM Evaluation]], [[Model Benchmarking]] |
| Observability | Khi answer sai thì sai ở retrieval, tool, prompt hay generation? | [[LLM Observability]], [[Agent Tracing]] |
| Routing | Request nên chạy bằng model nào? | [[Model Router]], [[AI Model Serving]] |

## Bài học từ case study

- ChatGPT: trải nghiệm đơn giản che giấu một pipeline dài, trong đó context, tool, safety, memory và streaming cùng tham gia.
- Cursor: code completion là workload latency cực thấp; codebase indexing giúp chat agent lấy context rộng hơn mà không gửi toàn bộ repo mỗi lần.
- OpenAI voice AI: với realtime audio, network/protocol architecture có thể quyết định cảm giác hội thoại nhiều như tốc độ model.
- Codex/ChatGPT Work: agent efficiency là tối ưu end-to-end qua harness, API và inference, trong đó mỗi lớp tránh lặp lại work đã làm.
- Anthropic multi-agent: agent production cần trace decision pattern, checkpoint/retry và eval outcome bằng rubric vì cùng prompt có thể đi nhiều path khác nhau.
- Yelp Assistant: production assistant nên tách retrieval/source selection khỏi final generation, dùng SSE để giảm perceived latency, và đánh giá tone/grounding bằng example/rubric.
- Bits AI SRE: AI ops agent hiệu quả khi follow causal evidence theo hypothesis, không nhồi mọi telemetry vào context rồi summarize.

## Ghi nhớ

Thiết kế LLM production là bài toán hệ thống. Model quality là một phần, nhưng trải nghiệm cuối phụ thuộc vào context đúng, inference nhanh, quyền tool hẹp, guardrail nhiều lớp và eval có thể bắt regression.

## Liên kết

- [[AI Engineering Systems from RAG to Agents]]
- [[Production AI Evaluation and Observability]]
- [[Coding Agent System Design]]
- [[LLM]]
- [[System Design]]
