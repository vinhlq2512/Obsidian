---
type: course-source
course: "[[CS224N]]"
status: completed
source_type: paper
title: "2024 - LMFusion - Adapting Pretrained Language Models for Multimodal Generation"
year: 2024
venue: "arXiv"
arxiv: "2412.15188v4"
source_file: "[[2024 - LMFusion - Adapting Pretrained Language Models for Multimodal Generation - arXiv 2412.15188v4.pdf]]"
pages: 15
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

# 2024 - LMFusion - Adapting Pretrained Language Models for Multimodal Generation - arXiv 2412.15188v4

## Nguồn

- PDF gốc: [[2024 - LMFusion - Adapting Pretrained Language Models for Multimodal Generation - arXiv 2412.15188v4.pdf]]
- Vai trò trong CS224N: paper về adapt text-only LLM sang multimodal generation bằng module song song.

## Câu hỏi trung tâm

Có thể tận dụng pretrained text-only LLM để hiểu/sinh multimodal mà không train mọi thứ từ đầu không?

## Kiến thức cốt lõi

- LMFusion giữ lại năng lực text của Llama-3/pretrained LLM.
- Thêm module riêng cho image/diffusion trong khi shared self-attention cho phép tương tác text-image.
- Freeze text-specific modules và train image-specific modules để tiết kiệm compute.
- Mục tiêu là multimodal generation trong arbitrary sequences.
- Paper nằm ở giao điểm PEFT, multimodal và diffusion.

## Cơ chế / công thức / kiến trúc

```text
pretrained text LLM
-> freeze text modules
-> thêm image-specific modules / diffusion path
-> shared attention cho cross-modal interaction
-> train phần image để thêm visual generation
```

## Khi áp dụng

- Dùng khi muốn tái sử dụng investment vào text-only LLM.
- Cần giữ language capability không bị phá khi thêm vision.
- So sánh với training multimodal model from scratch.

## Kết quả / bằng chứng đáng giữ

- First page nói LMFusion adapts pretrained text-only LLMs for multimodal generation.
- Source nêu freeze text-specific modules và chỉ train image-specific modules.
- Paper báo cáo cải thiện bằng ít FLOPs hơn so với pretrain từ đầu theo abstract.

## Cách hiểu bằng lời của tôi

LMFusion là chiến lược “đừng bỏ model text đã học tốt”. Thêm đường xử lý ảnh bên cạnh, giữ phần ngôn ngữ càng nguyên càng tốt.

## Câu hỏi review

1. LMFusion freeze module nào?
2. Shared self-attention giúp text-image interaction ra sao?
3. Lợi ích của adapt thay vì pretrain from scratch là gì?

## Liên kết

- [[Multimodal LLM]]
- [[Parameter-Efficient Fine-Tuning]]
- [[Transformer]]
- [[CS224N]]
