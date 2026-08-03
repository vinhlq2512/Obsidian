---
type: course-source
course: "[[CS224N]]"
status: completed
source_type: paper
title: "2025 - OneFlow - Concurrent Mixed-Modal and Interleaved Generation with Edit Flows"
year: 2025
venue: "arXiv"
arxiv: "2510.03506v3"
source_file: "[[2025 - OneFlow - Concurrent Mixed-Modal and Interleaved Generation with Edit Flows - arXiv 2510.03506v3.pdf]]"
pages: 32
created_at: 2026-08-02
updated_at: 2026-08-03
completed_at: 2026-08-03
related_concepts:
  - "[[Multimodal LLM]]"
tags:
  - cs224n
  - paper
---

# 2025 - OneFlow - Concurrent Mixed-Modal and Interleaved Generation with Edit Flows - arXiv 2510.03506v3

## Nguồn

- PDF gốc: [[2025 - OneFlow - Concurrent Mixed-Modal and Interleaved Generation with Edit Flows - arXiv 2510.03506v3.pdf]]
- Vai trò trong CS224N: paper về non-autoregressive mixed-modal generation với edit flows.

## Câu hỏi trung tâm

Có thể sinh text-image interleaved theo cách concurrent/variable-length thay vì autoregressive cứng nhắc không?

## Kiến thức cốt lõi

- OneFlow là non-autoregressive multimodal model cho variable-length concurrent generation.
- Kết hợp insertion-based Edit Flow cho discrete text tokens với Flow Matching cho image latents.
- Mục tiêu là sinh text và ảnh xen kẽ linh hoạt hơn autoregressive order cố định.
- Hierarchical sampling ưu tiên content trước grammar.
- Paper mở hướng mới cho multimodal generation và iterative refinement.

## Cơ chế / công thức / kiến trúc

```text
initial state
-> edit flow chèn/sửa text tokens
-> flow matching sinh image latents
-> refine concurrent text-image output
-> hỗ trợ interleaved generation
```

## Khi áp dụng

- Dùng khi autoregressive left-to-right order hạn chế generation multimodal.
- Cần đánh giá cả coherence, controllability và editing fidelity.
- Non-autoregressive generation có trade-off khác về training/inference.

## Kết quả / bằng chứng đáng giữ

- First page nói OneFlow là non-autoregressive multimodal model cho variable-length concurrent mixed-modal generation.
- Source nêu kết hợp Edit Flow và Flow Matching.
- Abstract nói model outperforms autoregressive baselines trong controlled experiments theo nhiều kích thước.

## Cách hiểu bằng lời của tôi

OneFlow không bắt model viết từng token theo một hàng cứng. Nó cho phép sửa/chèn và sinh nhiều modality cùng lúc, gần giống quá trình phác thảo rồi chỉnh dần.

## Câu hỏi review

1. OneFlow khác autoregressive generation ở đâu?
2. Edit Flow xử lý modality nào?
3. Concurrent generation tạo lợi ích gì cho multimodal output?

## Liên kết

- [[Multimodal LLM]]
- [[Generative Model]]
- [[Autoregressive Language Model]]
- [[CS224N]]
