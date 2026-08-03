---
type: course-source
course: "[[CS224N]]"
status: completed
source_type: paper
title: "2024 - Chameleon - Mixed-Modal Early-Fusion Foundation Models"
year: 2024
venue: "arXiv"
arxiv: "2405.09818v2"
source_file: "[[2024 - Chameleon - Mixed-Modal Early-Fusion Foundation Models - arXiv 2405.09818v2.pdf]]"
pages: 27
created_at: 2026-08-02
updated_at: 2026-08-03
completed_at: 2026-08-03
related_concepts:
  - "[[Multimodal LLM]]"
tags:
  - cs224n
  - paper
---

# 2024 - Chameleon - Mixed-Modal Early-Fusion Foundation Models - arXiv 2405.09818v2

## Nguồn

- PDF gốc: [[2024 - Chameleon - Mixed-Modal Early-Fusion Foundation Models - arXiv 2405.09818v2.pdf]]
- Vai trò trong CS224N: paper về mixed-modal early-fusion foundation models cho hiểu và sinh text/image.

## Câu hỏi trung tâm

Có thể xây một model early-fusion token-based xử lý và sinh text/image trong chuỗi tuỳ ý không?

## Kiến thức cốt lõi

- Chameleon hướng tới mixed-modal documents, không chỉ image-to-text hoặc text-to-image riêng lẻ.
- Early fusion nghĩa là modalities được đưa vào chung sớm trong backbone.
- Token-based mixed-modal modeling cho phép hiểu và sinh chuỗi gồm cả text và images.
- Training stable và alignment recipe là phần quan trọng để model hoạt động.
- Paper cho thấy hướng unified multimodal foundation model.

## Cơ chế / công thức / kiến trúc

```text
text tokens + image tokens
-> shared mixed-modal sequence
-> early-fusion Transformer backbone
-> understanding/generation tasks
-> alignment để làm theo prompt tốt hơn
```

## Khi áp dụng

- Dùng khi so sánh early fusion với modular/compositional multimodal systems.
- Cần chú ý image tokenization và data mixture.
- Mixed-modal generation cần đánh giá cả text quality và image quality.

## Kết quả / bằng chứng đáng giữ

- First page nói Chameleon là early-fusion token-based mixed-modal model.
- Source nêu model có thể understand and generate images and text in arbitrary sequence.
- Paper đặt trong cụm FAIR multimodal sources CS224N.

## Cách hiểu bằng lời của tôi

Chameleon cố làm cho ảnh và chữ sống trong cùng một dòng token, để model học tài liệu đa phương thức như một sequence chung.

## Câu hỏi review

1. Early fusion khác late fusion thế nào?
2. Mixed-modal document khác captioning đơn giản ra sao?
3. Image tokenization tạo trade-off gì?

## Liên kết

- [[Multimodal LLM]]
- [[Transformer]]
- [[Autoregressive Language Model]]
- [[CS224N]]
