---
type: course-source
course: "[[CS224N]]"
status: developing
source_type: paper
title: "2023 - ReAct - Synergizing Reasoning and Acting in Language Models"
year: 2023
venue: "arXiv"
arxiv: "2210.03629v3"
source_file: "[[2023 - ReAct - Synergizing Reasoning and Acting in Language Models - arXiv 2210.03629v3.pdf]]"
pages: 33
created_at: 2026-08-02
updated_at: 2026-08-02
related_concepts:
  - "[[Large Language Model]]"
  - "[[Autoregressive Language Model]]"
  - "[[LLM Agent]]"
  - "[[Prompt Engineering]]"
tags:
  - cs224n
  - paper
---

# 2023 - ReAct - Synergizing Reasoning and Acting in Language Models - arXiv 2210.03629v3

## Nguồn

- PDF gốc: [[2023 - ReAct - Synergizing Reasoning and Acting in Language Models - arXiv 2210.03629v3.pdf]]
- Đọc cùng: [[CS224N 2026 - Lecture 10 - RAG and Language Agents]]
- Concept: [[LLM Agent]], [[Prompt Engineering]]

## Vấn đề paper giải quyết

Reasoning traces và acting/tool interaction thường được nghiên cứu tách rời. ReAct kết hợp chúng theo dạng xen kẽ: model vừa suy nghĩ vừa hành động trong môi trường.

## Đóng góp chính

- Sinh reasoning traces và task-specific actions xen kẽ.
- Reasoning giúp theo dõi plan, cập nhật trạng thái và xử lý ngoại lệ.
- Actions giúp model lấy thông tin từ môi trường hoặc tool thay vì chỉ dựa vào parametric memory.

## Cơ chế

```text
Thought: phân tích trạng thái và kế hoạch
Action: gọi tool / tìm kiếm / tương tác môi trường
Observation: nhận kết quả
Thought: cập nhật suy luận
...
Answer: kết luận
```

## Vì sao quan trọng với CS224N

Lecture 10 dùng ReAct như pattern nền cho language agents. Nó cho thấy agent không chỉ là LM trả lời dài hơn, mà là loop reasoning-action-observation.

## Hạn chế / câu hỏi

- Reasoning trace có thể sai nhưng vẫn tự tin.
- Tool result cần được parse và kiểm tra.
- Evaluation phải đo cả trajectory, không chỉ final answer.

## Câu hỏi review

1. ReAct xen kẽ hai loại output nào?
2. Observation giúp model sửa plan ra sao?
3. Vì sao agent evaluation khó hơn QA thường?
