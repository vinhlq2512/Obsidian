---
type: course-source
course: "[[CS224N]]"
status: completed
source_type: paper
title: "2024 - Visual Sketchpad - Sketching as a Visual Chain of Thought for Multimodal Language Models"
year: 2024
venue: "arXiv"
arxiv: "2406.09403v3"
source_file: "[[2024 - Visual Sketchpad - Sketching as a Visual Chain of Thought for Multimodal Language Models - arXiv 2406.09403v3.pdf]]"
pages: 32
created_at: 2026-08-02
updated_at: 2026-08-03
completed_at: 2026-08-03
related_concepts:
  - "[[Large Language Model]]"
  - "[[Autoregressive Language Model]]"
  - "[[Multimodal LLM]]"
tags:
  - cs224n
  - paper
---

# 2024 - Visual Sketchpad - Sketching as a Visual Chain of Thought for Multimodal Language Models - arXiv 2406.09403v3

## Nguồn

- PDF gốc: [[2024 - Visual Sketchpad - Sketching as a Visual Chain of Thought for Multimodal Language Models - arXiv 2406.09403v3.pdf]]
- Vai trò trong CS224N: paper về visual chain-of-thought: dùng sketch như scratchpad cho multimodal reasoning.

## Câu hỏi trung tâm

Multimodal model có thể cải thiện reasoning bằng cách tạo intermediate visual sketches thay vì chỉ text reasoning không?

## Kiến thức cốt lõi

- Visual sketchpad mở rộng chain-of-thought sang không gian hình ảnh.
- Sketch có thể làm intermediate representation cho spatial/geometric reasoning.
- Multimodal reasoning đôi khi cần thao tác visual, không chỉ giải thích bằng text.
- Kỹ thuật này nối prompting, tool-like externalization và multimodal reasoning.
- Paper thuộc trục reasoning + multimodal trong CS224N.

## Cơ chế / công thức / kiến trúc

```text
visual problem
-> model tạo sketch/intermediate visual state
-> dùng sketch để suy luận tiếp
-> trả answer hoặc refine output
```

## Khi áp dụng

- Dùng cho bài toán spatial, geometry, diagram reasoning.
- Cần đánh giá sketch có giúp reasoning thật hay chỉ là artifact.
- Có thể kết hợp với verifier hoặc tool visual.

## Kết quả / bằng chứng đáng giữ

- Title nêu sketching as a visual chain of thought.
- CS224N source đặt paper này cạnh test-time compute và multimodal reasoning.
- Ý tưởng phù hợp với xu hướng externalize reasoning traces.

## Cách hiểu bằng lời của tôi

Nếu CoT là giấy nháp bằng chữ, visual sketchpad là giấy nháp bằng hình. Với bài toán thị giác, giấy nháp đúng modality có thể quan trọng hơn lời giải bằng text.

## Câu hỏi review

1. Visual CoT khác text CoT ở đâu?
2. Sketch giúp loại bài toán nào?
3. Làm sao đánh giá sketch có thật sự hữu ích?

## Liên kết

- [[Multimodal LLM]]
- [[Prompt Engineering]]
- [[Test-Time Compute]]
- [[CS224N]]
