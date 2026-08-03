---
type: course-source
course: "[[CS224N]]"
status: completed
source_type: paper
title: "2024 - The Llama 3 Herd of Models"
year: 2024
venue: "arXiv"
arxiv: "2407.21783v3"
source_file: "[[2024 - The Llama 3 Herd of Models - arXiv 2407.21783v3.pdf]]"
pages: 92
created_at: 2026-08-02
updated_at: 2026-08-03
completed_at: 2026-08-03
related_concepts:
  - "[[Large Language Model]]"
tags:
  - cs224n
  - paper
---

# 2024 - The Llama 3 Herd of Models - arXiv 2407.21783v3

## Nguồn

- PDF gốc: [[2024 - The Llama 3 Herd of Models - arXiv 2407.21783v3.pdf]]
- Vai trò trong CS224N: technical report về Llama 3 family, pretraining/post-training/evaluation và mở rộng multimodal.

## Câu hỏi trung tâm

Một family foundation models hiện đại được xây, post-train, đánh giá và phát hành như thế nào?

## Kiến thức cốt lõi

- Llama 3 gồm nhiều model, hỗ trợ multilinguality, coding, reasoning và tool usage.
- Report mô tả cả pretrained và post-trained versions.
- Context window lớn và evaluation rộng là điểm đáng chú ý.
- Có thử nghiệm tích hợp image/video/speech theo hướng compositional.
- Đây là case study hệ thống cho toàn bộ pipeline CS224N: pretraining -> post-training -> evaluation -> deployment.

## Cơ chế / công thức / kiến trúc

```text
large-scale data + Transformer backbone
-> pretraining
-> post-training/alignment
-> safety model / guardrails
-> broad empirical evaluation
-> release model family
```

## Khi áp dụng

- Dùng như case study khi đọc lifecycle foundation model.
- Không chỉ xem benchmark score; đọc data, safety, post-training và release choices.
- So sánh với DeepSeek, GPT-style và open-source ecosystem.

## Kết quả / bằng chứng đáng giữ

- First page nêu Llama 3 hỗ trợ multilinguality, coding, reasoning, tool usage.
- Source nói model lớn nhất dense Transformer 405B và context tới 128K tokens.
- Report công bố cả pretrained/post-trained versions và Llama Guard 3.

## Cách hiểu bằng lời của tôi

Llama 3 không chỉ là một model; nó là một hệ sinh thái model family, data recipe, post-training, safety và evaluation.

## Câu hỏi review

1. Model family khác một checkpoint đơn lẻ ở đâu?
2. Pretrained và post-trained versions phục vụ mục đích gì?
3. Vì sao safety model là một phần của release?

## Liên kết

- [[Large Language Model]]
- [[Instruction Fine-Tuning]]
- [[RLHF]]
- [[Multimodal LLM]]
- [[CS224N]]
