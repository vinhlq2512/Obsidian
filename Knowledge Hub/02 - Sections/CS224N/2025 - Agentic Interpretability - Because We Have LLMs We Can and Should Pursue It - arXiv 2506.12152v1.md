---
type: course-source
course: "[[CS224N]]"
status: completed
source_type: paper
title: "2025 - Agentic Interpretability - Because We Have LLMs We Can and Should Pursue It"
year: 2025
venue: "arXiv"
arxiv: "2506.12152v1"
source_file: "[[2025 - Agentic Interpretability - Because We Have LLMs We Can and Should Pursue It - arXiv 2506.12152v1.pdf]]"
pages: 15
created_at: 2026-08-02
updated_at: 2026-08-03
completed_at: 2026-08-03
related_concepts:
  - "[[LLM Agent]]"
tags:
  - cs224n
  - paper
---

# 2025 - Agentic Interpretability - Because We Have LLMs We Can and Should Pursue It - arXiv 2506.12152v1

## Nguồn

- PDF gốc: [[2025 - Agentic Interpretability - Because We Have LLMs We Can and Should Pursue It - arXiv 2506.12152v1.pdf]]
- Vai trò trong CS224N: paper về interpretability cho agentic/LLM systems.

## Câu hỏi trung tâm

Khi LLM có thể hành động như agent, interpretability nên thay đổi như thế nào?

## Kiến thức cốt lõi

- Agentic systems có hành vi nhiều bước, tool use và memory nên khó giải thích hơn single-output model.
- LLMs có thể hỗ trợ chính quá trình interpretability: tóm tắt, tìm pattern, sinh hypothesis, kiểm tra traces.
- Cần hiểu không chỉ weights mà cả policy, trajectory, tool calls và môi trường.
- Interpretability trở thành vấn đề hệ thống, không chỉ neuron-level.
- Paper liên hệ với Lecture 16 về tác động/xác minh và Lecture 10 về agents.

## Cơ chế / công thức / kiến trúc

```text
agent trajectory
-> logs / actions / observations / memory updates
-> LLM-assisted analysis
-> hypotheses về behavior/failure modes
-> targeted tests
```

## Khi áp dụng

- Dùng khi audit agent thay vì chatbot một lượt.
- Cần log đầy đủ action/observation để phân tích.
- Không để LLM explanation thay thế kiểm chứng thực nghiệm.

## Kết quả / bằng chứng đáng giữ

- Title nói agentic interpretability và lý do vì có LLMs nên theo đuổi.
- Lecture 16 đặt interpretability trong AI impact và hallucination/safety.
- Agentic workflows trong Lecture 10 tạo nhu cầu giải thích trajectory.

## Cách hiểu bằng lời của tôi

Khi model biết dùng tool, câu hỏi không còn là “nó trả lời gì?” mà là “nó đã đi qua đường nào để tới câu trả lời đó?”.

## Câu hỏi review

1. Agentic interpretability khác model interpretability truyền thống ở đâu?
2. Vì sao logs/trajectory quan trọng?
3. LLM có thể hỗ trợ interpretability nhưng vẫn cần kiểm chứng thế nào?

## Liên kết

- [[LLM Agent]]
- [[Tool Use]]
- [[AI Hallucination]]
- [[Measuring the Quality of Generated Text]]
- [[CS224N]]
