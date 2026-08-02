---
type: course-source
course: "[[CS224N]]"
status: developing
source_type: paper
title: "2020 - Language Models are Few-Shot Learners"
year: 2020
venue: "arXiv"
arxiv: "2005.14165v4"
source_file: "[[2020 - Language Models are Few-Shot Learners - arXiv 2005.14165v4.pdf]]"
pages: 75
created_at: 2026-08-02
updated_at: 2026-08-02
related_concepts:
  - "[[Large Language Model]]"
  - "[[Autoregressive Language Model]]"
tags:
  - cs224n
  - paper
---

# 2020 - Language Models are Few-Shot Learners - arXiv 2005.14165v4

## Nguồn

- PDF gốc: [[2020 - Language Models are Few-Shot Learners - arXiv 2005.14165v4.pdf]]
- Đọc cùng: [[CS224N 2026 - Lecture 07 - Pretraining]]
- Concept: [[Large Language Model]], [[Prompt Engineering]], [[Autoregressive Language Model]]

## Vấn đề paper giải quyết

Fine-tuning truyền thống cần nhiều labeled examples cho mỗi task. Paper hỏi: nếu scale language model đủ lớn, model có thể làm task mới chỉ từ instruction hoặc vài ví dụ trong prompt không?

## Đóng góp chính

- Đưa few-shot, one-shot và zero-shot prompting thành chế độ đánh giá trung tâm cho LLM.
- Cho thấy scale pretraining có thể tạo năng lực in-context learning.
- Dịch trọng tâm từ task-specific fine-tuning sang prompting với model general-purpose.

## Cơ chế cần nhớ

```text
prompt chứa instruction + vài examples
-> decoder-only LM tiếp tục chuỗi
-> output được xem như lời giải task
-> không cập nhật weight
```

## Vì sao quan trọng với CS224N

Paper này là cầu nối từ pretraining sang kỷ nguyên LLM assistant. Nó giải thích vì sao Lecture 07 nói về very large models và in-context learning.

## Hạn chế / câu hỏi

- Few-shot prompting phụ thuộc mạnh vào prompt format và example selection.
- Model lớn vẫn có thể hallucinate và thiếu alignment với intent.
- Chi phí inference/training cao, mở ra nhu cầu efficient adaptation và small models.

## Câu hỏi review

1. In-context learning khác fine-tuning ở đâu?
2. Vì sao few-shot prompting là dấu hiệu quan trọng của scaling?
3. Prompt sensitivity gây vấn đề gì khi đánh giá model?
