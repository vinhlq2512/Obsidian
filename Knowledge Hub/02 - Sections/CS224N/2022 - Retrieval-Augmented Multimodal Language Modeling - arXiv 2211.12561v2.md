---
type: course-source
course: "[[CS224N]]"
status: completed
source_type: paper
title: "2022 - Retrieval-Augmented Multimodal Language Modeling"
year: 2022
venue: "arXiv"
arxiv: "2211.12561v2"
source_file: "[[2022 - Retrieval-Augmented Multimodal Language Modeling - arXiv 2211.12561v2.pdf]]"
pages: 15
created_at: 2026-08-02
updated_at: 2026-08-03
completed_at: 2026-08-03
related_concepts:
  - "[[Large Language Model]]"
  - "[[Autoregressive Language Model]]"
  - "[[Retrieval-Augmented Generation]]"
  - "[[Retriever]]"
  - "[[Multimodal LLM]]"
tags:
  - cs224n
  - paper
---

# 2022 - Retrieval-Augmented Multimodal Language Modeling - arXiv 2211.12561v2

## Nguồn

- PDF gốc: [[2022 - Retrieval-Augmented Multimodal Language Modeling - arXiv 2211.12561v2.pdf]]
- Vai trò trong CS224N: paper nối retrieval augmentation với multimodal language modeling.

## Câu hỏi trung tâm

Retrieval có thể giúp multimodal model tận dụng memory ngoài tham số khi xử lý/generate text-image không?

## Kiến thức cốt lõi

- Multimodal models cần xử lý thông tin không chỉ trong text mà cả image/visual context.
- Retrieval augmentation thêm nguồn tri thức hoặc examples liên quan ngoài parametric memory.
- Cách này mở rộng intuition của RAG sang multimodal setting.
- Challenge gồm representation chung, retrieval relevance và cách fuse retrieved items vào generator.
- Source này nằm trong trục RAG và multimodal CS224N.

## Cơ chế / công thức / kiến trúc

```text
multimodal input/query
-> retrieve text/image/multimodal neighbors
-> condition generator trên retrieved context
-> sinh output multimodal hoặc text grounded hơn
```

## Khi áp dụng

- Dùng khi parametric model thiếu tri thức visual cụ thể.
- Retriever phải hiểu cross-modal similarity, không chỉ text overlap.
- Cần đánh giá cả retrieved evidence và generated answer.

## Kết quả / bằng chứng đáng giữ

- Title nêu retrieval-augmented multimodal language modeling.
- CS224N đặt paper này cạnh RAG và multimodal generation.
- Nó mở rộng vấn đề provenance/update knowledge sang không gian multimodal.

## Cách hiểu bằng lời của tôi

Nếu RAG là “mở sách” cho text LM, multimodal RAG là “mở cả thư viện ảnh-văn bản” cho model nhìn và nói.

## Câu hỏi review

1. Multimodal retrieval khác text retrieval ở đâu?
2. Retrieved visual context có thể giúp generation như thế nào?
3. Evaluation cần đo thêm thành phần nào?

## Liên kết

- [[Retrieval-Augmented Generation]]
- [[Multimodal LLM]]
- [[Retriever]]
- [[CS224N]]
