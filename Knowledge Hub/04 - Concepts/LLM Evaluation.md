---
type: concept
status: developing
sources:
  - "[[2026-01-12_a-guide-to-llm-evals]]"
  - "[[2026-05-30_how-doordash-built-a-testing-system-to-evaluate-llms]]"
  - "[[2025-09-16_how-anthropic-built-a-multi-agent-research-system]]"
  - "[[2026-02-09_how-yelp-built-yelp-assistant]]"
  - "[[2026-01-20_this-isnt-an-ai-summarizer-and-that-matters-byte-sized-design]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - llm
  - evaluation
  - production
---

# LLM Evaluation

## Định nghĩa

LLM evaluation là thực hành đo chất lượng hệ thống LLM bằng test set, metric, human review, benchmark, simulator hoặc model-as-judge để biết thay đổi có làm hệ thống tốt hơn không.

## Cách hiểu bằng lời của tôi

Với LLM, không thể chỉ assert output bằng một chuỗi cố định. Ta cần mô tả "tốt" nghĩa là gì cho use case, tạo dữ liệu đại diện, chấm bằng rubric, theo dõi version prompt/model/dataset và đọc failure cases.

## Các kiểu eval

- Automatic eval: exact match, keyword, semantic similarity, code execution, structured-output check.
- Human eval: preference ranking, Likert score, task completion review.
- Benchmark eval: so sánh trên dataset chuẩn, nhưng không thay thế eval theo sản phẩm thật.
- LLM-as-judge: dùng model mạnh chấm output theo rubric, cần calibration với người.
- Simulation eval: tạo môi trường giả lập, ví dụ hội thoại customer support và backend mock.

## Cần biết

- Eval set nên có case phổ biến, edge case và known failure mode.
- Cần version model, prompt, dataset và rubric.
- Tránh overfit eval set; thêm case mới khi phát hiện lỗi mới.
- Với agent, chấm cả trajectory: tool call, observation, retry, decision dừng.
- Với RAG/assistant, chấm cả retrieval: source đúng có được đưa vào context không, evidence có đủ cho claim không.
- Với incident/SRE agent, benchmark nên dùng incident thật đã label, vì synthetic task dễ bỏ qua causal chain.

## Liên kết

- [[Model Benchmarking]]
- [[LLM-as-Judge]]
- [[Agent Evaluation]]
- [[Retrieval Evaluation]]
- [[Citation Quality]]
- [[LLM Observability]]
- [[AI Hallucination]]
- [[LLM Agent]]
- [[Agentic Loop]]
- [[Tool Use]]
