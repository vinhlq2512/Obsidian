---
type: course-source
course: "[[CS224N]]"
status: completed
source_type: paper
title: "2025 - Reconstruction Alignment Improves Unified Multimodal Models"
year: 2025
venue: "arXiv"
arxiv: "2509.07295v3"
source_file: "[[2025 - Reconstruction Alignment Improves Unified Multimodal Models - arXiv 2509.07295v3.pdf]]"
pages: 34
created_at: 2026-08-02
updated_at: 2026-08-03
completed_at: 2026-08-03
related_concepts:
  - "[[RLHF]]"
  - "[[DPO]]"
  - "[[Multimodal LLM]]"
tags:
  - cs224n
  - paper
---

# 2025 - Reconstruction Alignment Improves Unified Multimodal Models - arXiv 2509.07295v3

## Nguồn

- PDF gốc: [[2025 - Reconstruction Alignment Improves Unified Multimodal Models - arXiv 2509.07295v3.pdf]]
- Vai trò trong CS224N: paper về reconstruction alignment cho unified multimodal models.

## Câu hỏi trung tâm

Có thể cải thiện generation/editing fidelity của unified multimodal models bằng self-supervised reconstruction alignment không?

## Kiến thức cốt lõi

- Unified multimodal models thường dùng caption/image-text pairs nhưng captions thiếu chi tiết visual.
- RECA dùng visual understanding embeddings như dense prompts để reconstruct input image.
- Phương pháp align understanding và generation bằng reconstruction loss.
- Áp dụng cho autoregressive, masked-autoregressive và diffusion-based UMMs.
- Mục tiêu là cải thiện image generation và editing fidelity với chi phí thấp.

## Cơ chế / công thức / kiến trúc

```text
input image
-> visual understanding encoder embeddings
-> condition UMM generation branch
-> reconstruct image
-> loss kéo understanding và generation aligned hơn
```

## Khi áp dụng

- Dùng khi model hiểu ảnh nhưng sinh/chỉnh ảnh không giữ chi tiết.
- Hữu ích vì không phụ thuộc caption chi tiết thủ công.
- Cần kiểm tra fidelity, editing benchmark và generalization across architectures.

## Kết quả / bằng chứng đáng giữ

- First page nói Reconstruction Alignment cải thiện unified multimodal models.
- Source nêu captions sparse và miss fine-grained visual details.
- Abstract báo cáo RECA cải thiện GenEval/DPGBench và editing benchmarks.

## Cách hiểu bằng lời của tôi

RECA dùng chính biểu diễn hiểu ảnh của model như lời nhắc dày đặc để bắt nhánh sinh ảnh học giữ chi tiết. Nó align “nhìn” và “vẽ lại”.

## Câu hỏi review

1. Vì sao caption không đủ cho alignment visual chi tiết?
2. RECA dùng embedding nào làm dense prompt?
3. Reconstruction alignment cải thiện generation và editing như thế nào?

## Liên kết

- [[Multimodal LLM]]
- [[Generative Model]]
- [[Representation Model]]
- [[CS224N]]
