---
type: course-source
course: "[[CS224N]]"
status: completed
source_type: paper
title: "2023 - Lets Verify Step by Step"
year: 2023
venue: "arXiv"
arxiv: "2305.20050v1"
source_file: "[[2023 - Lets Verify Step by Step - arXiv 2305.20050v1.pdf]]"
pages: 29
created_at: 2026-08-02
updated_at: 2026-08-03
completed_at: 2026-08-03
related_concepts:
  - "[[NLP]]"
tags:
  - cs224n
  - paper
---

# 2023 - Lets Verify Step by Step - arXiv 2305.20050v1

## Nguồn

- PDF gốc: [[2023 - Lets Verify Step by Step - arXiv 2305.20050v1.pdf]]
- Vai trò trong CS224N: paper về process supervision/verifier cho reasoning từng bước.

## Câu hỏi trung tâm

Đánh giá từng bước suy luận có giúp model reasoning tốt hơn chỉ chấm đáp án cuối không?

## Kiến thức cốt lõi

- Outcome supervision chỉ thưởng/phạt final answer.
- Process supervision đánh giá các bước trung gian trong lời giải.
- Verifier từng bước có thể hướng model tới reasoning đáng tin hơn.
- Cách này liên quan trực tiếp tới reasoning, math problems và inference-time selection.
- Nó bổ sung cho CoT/self-consistency bằng tín hiệu kiểm tra quá trình.

## Cơ chế / công thức / kiến trúc

```text
problem
-> model sinh solution steps
-> process verifier chấm từng bước
-> chọn/cải thiện trajectory có bước đúng
-> final answer đáng tin hơn
```

## Khi áp dụng

- Dùng khi final answer đúng/sai chưa đủ để dạy reasoning.
- Cần annotation hoặc verifier chất lượng cho từng bước.
- Có thể kết hợp với sampling nhiều lời giải và chọn trajectory tốt.

## Kết quả / bằng chứng đáng giữ

- Title nêu verify step by step.
- Lecture 13 đưa paper này cạnh speculative decoding và reasoning.
- Reasoning evaluation hiện đại quan tâm process, không chỉ output cuối.

## Cách hiểu bằng lời của tôi

Nếu chỉ chấm đáp án cuối, model có thể may mắn đúng. Chấm từng bước giúp biết đường đi có thật sự hợp lý không.

## Câu hỏi review

1. Process supervision khác outcome supervision thế nào?
2. Verifier từng bước giúp chọn lời giải ra sao?
3. Tại sao reasoning trace vẫn cần kiểm chứng?

## Liên kết

- [[Prompt Engineering]]
- [[Test-Time Compute]]
- [[Large Language Model]]
- [[Measuring the Quality of Generated Text]]
- [[CS224N]]
