---
type: course-source
course: "[[CS224N]]"
status: completed
source_type: paper
title: "2023 - Toolformer - Language Models Can Teach Themselves to Use Tools"
year: 2023
venue: "arXiv"
arxiv: "2302.04761v1"
source_file: "[[2023 - Toolformer - Language Models Can Teach Themselves to Use Tools - arXiv 2302.04761v1.pdf]]"
pages: 17
created_at: 2026-08-02
updated_at: 2026-08-03
completed_at: 2026-08-03
related_concepts:
  - "[[Large Language Model]]"
  - "[[Autoregressive Language Model]]"
  - "[[LLM Agent]]"
tags:
  - cs224n
  - paper
---

# 2023 - Toolformer - Language Models Can Teach Themselves to Use Tools - arXiv 2302.04761v1

## Nguồn

- PDF gốc: [[2023 - Toolformer - Language Models Can Teach Themselves to Use Tools - arXiv 2302.04761v1.pdf]]
- Vai trò trong CS224N: paper nền về tool use cho LLM và language agents.

## Câu hỏi trung tâm

Language model có thể tự học khi nào gọi tool/API bằng dữ liệu tự tạo không?

## Kiến thức cốt lõi

- Toolformer nghiên cứu cách LM dùng external tools qua API calls.
- Tools có thể hỗ trợ calculator, search, translation hoặc QA systems.
- Model cần học cả lúc nào gọi tool, gọi với input gì và dùng kết quả ra sao.
- Tool use mở rộng năng lực model ngoài parametric memory.
- Paper thuộc trục agent/tool use trong Lecture 10.

## Cơ chế / công thức / kiến trúc

```text
raw text
-> chèn candidate API calls
-> giữ calls giúp cải thiện likelihood/output
-> fine-tune model trên data có tool-use annotations
-> model học gọi tool khi cần
```

## Khi áp dụng

- Dùng khi agent cần năng lực ngoài text generation.
- Tool call phải có schema và error handling rõ.
- Cần đánh giá cả quyết định gọi tool và chất lượng final answer.

## Kết quả / bằng chứng đáng giữ

- Title nói language models can teach themselves to use tools.
- Lecture 10 đặt tool use như một thành phần của language agents.
- Tool use giúp xử lý giới hạn factuality/calculation/current information.

## Cách hiểu bằng lời của tôi

Toolformer biến tool use thành một hành vi học được trong text. Model không chỉ trả lời; nó học chèn hành động vào quá trình sinh.

## Câu hỏi review

1. Toolformer học tool-use data bằng cách nào?
2. Tool use giải quyết giới hạn nào của LM?
3. Khi đánh giá tool use cần đo những gì?

## Liên kết

- [[Tool Use]]
- [[LLM Agent]]
- [[Retrieval-Augmented Generation]]
- [[CS224N]]
