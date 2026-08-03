---
type: course-source
course: "[[CS224N]]"
status: completed
source_type: paper
title: "2025 - Mixture-of-Transformers - A Sparse and Scalable Architecture for Multi-Modal Foundation Models"
year: 2025
venue: "TMLR 2025"
arxiv: ""
source_file: "[[2025 - Mixture-of-Transformers - A Sparse and Scalable Architecture for Multi-Modal Foundation Models - TMLR 2025.pdf]]"
pages: 48
created_at: 2026-08-02
updated_at: 2026-08-03
completed_at: 2026-08-03
related_concepts:
  - "[[Transformer]]"
  - "[[Self-Attention]]"
  - "[[Multi-Head Attention]]"
tags:
  - cs224n
  - paper
---

# 2025 - Mixture-of-Transformers - A Sparse and Scalable Architecture for Multi-Modal Foundation Models - TMLR 2025

## Nguồn

- PDF gốc: [[2025 - Mixture-of-Transformers - A Sparse and Scalable Architecture for Multi-Modal Foundation Models - TMLR 2025.pdf]]
- Vai trò trong CS224N: paper về sparse multimodal Transformer architecture.

## Câu hỏi trung tâm

Có thể giảm compute pretraining multimodal bằng cách tách tham số theo modality nhưng vẫn giữ global attention không?

## Kiến thức cốt lõi

- Mixture-of-Transformers decouple non-embedding parameters theo modality.
- Các thành phần như FFN, attention matrices, layer norm có thể modality-specific.
- Global self-attention vẫn cho các modality tương tác trong cùng sequence.
- Sparse architecture giảm FLOPs so với dense baseline trong nhiều setting.
- Paper là hướng kiến trúc cho scaling multimodal hiệu quả hơn.

## Cơ chế / công thức / kiến trúc

```text
input mixed modalities
-> route qua modality-specific parameters
-> global self-attention trên full sequence
-> output multimodal
-> giảm compute bằng sparsity/modality specialization
```

## Khi áp dụng

- Dùng khi dense multimodal model quá đắt.
- Cần cân bằng specialization theo modality và interaction chung.
- Evaluation phải đo riêng từng modality và cross-modal tasks.

## Kết quả / bằng chứng đáng giữ

- First page nói MoT decouples non-embedding parameters by modality.
- Source nêu MoT matches dense baseline với phần FLOPs thấp hơn trong Chameleon/Transfusion settings.
- Paper được publish TMLR 2025 theo first page.

## Cách hiểu bằng lời của tôi

MoT không ép mọi modality dùng cùng toàn bộ tham số. Nó cho mỗi modality phần xử lý riêng, nhưng vẫn giữ attention chung để nói chuyện với nhau.

## Câu hỏi review

1. MoT sparse ở đâu?
2. Vì sao vẫn cần global self-attention?
3. Compute saving có thể đánh đổi với điều gì?

## Liên kết

- [[Multimodal LLM]]
- [[Transformer]]
- [[Self-Attention]]
- [[CS224N]]
