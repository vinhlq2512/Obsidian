---
type: synthesis
status: seed
concepts:
  - "[[LLM Observability]]"
  - "[[Agent Evaluation]]"
  - "[[Agent Tracing]]"
  - "[[Retrieval Evaluation]]"
  - "[[Evidence-Grounded Generation]]"
  - "[[LLM-as-Judge]]"
sources:
  - "[[2025-09-16_how-anthropic-built-a-multi-agent-research-system]]"
  - "[[2026-02-09_how-yelp-built-yelp-assistant]]"
  - "[[2026-01-20_this-isnt-an-ai-summarizer-and-that-matters-byte-sized-design]]"
created_at: 2026-08-16
updated_at: 2026-08-16
tags:
  - synthesis
  - llm
  - evaluation
  - observability
---

# Production AI Evaluation and Observability

## Ý chính

AI production không ổn định chỉ bằng prompt tốt. Cần eval đại diện, trace được trajectory, đo retrieval/latency/cost, và buộc answer bám evidence.

## Bài học từ các case

- Anthropic multi-agent: chấm outcome bằng rubric, LLM-as-judge calibrate với human, tracing decision pattern để debug agent không deterministic.
- Yelp Assistant: tách retrieval khỏi generation, đo latency từng stage, source selection để tránh search sai store, few-shot/prompt được version như code.
- Bits AI SRE: benchmark trên incident thật đã label, theo causal chain thay vì nhồi mọi telemetry vào context.

## Mental model

```text
production traffic / labeled cases
-> retrieval và tool trajectory
-> grounded output + citations
-> rubric eval + human calibration
-> trace/failure analysis
-> prompt/model/retrieval update
```

## Liên kết

- [[Production LLM System Design]]
- [[AI Engineering Systems from RAG to Agents]]
- [[LLM Evaluation]]
- [[LLM Observability]]
