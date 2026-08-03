---
type: course-source
course: "[[CS224N]]"
status: completed
source_type: paper
title: "2021 - Measuring Massive Multitask Language Understanding"
year: 2021
venue: "arXiv"
arxiv: "2009.03300v3"
source_file: "[[2021 - Measuring Massive Multitask Language Understanding - arXiv 2009.03300v3.pdf]]"
pages: 27
created_at: 2026-08-02
updated_at: 2026-08-03
completed_at: 2026-08-03
related_concepts:
  - "[[NLP]]"
tags:
  - cs224n
  - paper
---

# 2021 - Measuring Massive Multitask Language Understanding - arXiv 2009.03300v3

## Nguồn

- PDF gốc: [[2021 - Measuring Massive Multitask Language Understanding - arXiv 2009.03300v3.pdf]]
- Vai trò trong CS224N: paper nền cho MMLU và đánh giá multitask knowledge/reasoning của LLM.

## Câu hỏi trung tâm

Làm thế nào đo language understanding trên nhiều lĩnh vực thay vì một benchmark hẹp?

## Kiến thức cốt lõi

- MMLU gom nhiều subject/task để kiểm tra knowledge và reasoning rộng.
- Multitask benchmark đo khả năng generalization across domains.
- Điểm mạnh là coverage rộng; điểm yếu là có thể bị contamination và không đo mọi năng lực thực tế.
- Benchmark kiểu này trở thành thước đo phổ biến cho LLM frontier.
- Trong CS224N, nó nằm ở trục evaluation và benchmark design.

## Cơ chế / công thức / kiến trúc

```text
nhiều môn / lĩnh vực
-> câu hỏi chuẩn hoá
-> model trả lời
-> aggregate accuracy theo subject và overall
```

MMLU đo final answer, không tự đảm bảo model reasoning đúng hoặc không dùng shortcut.

## Khi áp dụng

- Dùng khi so sánh model ở năng lực kiến thức rộng.
- Luôn kiểm tra data contamination và prompt format.
- Không dùng một benchmark duy nhất để kết luận model tốt toàn diện.

## Kết quả / bằng chứng đáng giữ

- Title nêu measuring massive multitask language understanding.
- Lecture 11 bàn về benchmark proliferation và benchmark shelf-life.
- MMLU là ví dụ tiêu biểu của multitask benchmark.

## Cách hiểu bằng lời của tôi

MMLU giống một bài thi tổng hợp cho LLM. Nó hữu ích, nhưng vẫn chỉ là một lát cắt của năng lực thật.

## Câu hỏi review

1. MMLU đo gì hơn single-task benchmark?
2. Data contamination làm sai lệch benchmark như thế nào?
3. Vì sao benchmark rộng vẫn không đủ để đánh giá toàn diện?

## Liên kết

- [[Measuring the Quality of Generated Text]]
- [[Large Language Model]]
- [[Exact Match]]
- [[CS224N]]
