---
type: course-source
course: "[[CS224N]]"
status: completed
source_type: paper
title: "2024 - Transfusion - Predict the Next Token and Diffuse Images with One Multi-Modal Model"
year: 2024
venue: "arXiv"
arxiv: "2408.11039v1"
source_file: "[[2024 - Transfusion - Predict the Next Token and Diffuse Images with One Multi-Modal Model - arXiv 2408.11039v1.pdf]]"
pages: 23
created_at: 2026-08-02
updated_at: 2026-08-03
completed_at: 2026-08-03
related_concepts:
  - "[[Tokenization]]"
tags:
  - cs224n
  - paper
---

# 2024 - Transfusion - Predict the Next Token and Diffuse Images with One Multi-Modal Model - arXiv 2408.11039v1

## Nguồn

- PDF gốc: [[2024 - Transfusion - Predict the Next Token and Diffuse Images with One Multi-Modal Model - arXiv 2408.11039v1.pdf]]
- Vai trò trong CS224N: paper kết hợp next-token prediction cho text với diffusion cho image trong một multimodal model.

## Câu hỏi trung tâm

Một model duy nhất có thể học text bằng language modeling và image bằng diffusion trong cùng framework không?

## Kiến thức cốt lõi

- Transfusion kết hợp loss next-token prediction với diffusion objective.
- Text là modality rời rạc; image thường là modality liên tục.
- Model xử lý mixed-modality sequences nhưng dùng objective phù hợp từng modality.
- Modality-specific encoding/decoding layers cải thiện performance.
- Paper giải quyết giới hạn của việc ép image thành discrete tokens thuần.

## Cơ chế / công thức / kiến trúc

```text
text tokens -> next-token prediction loss
image latents/patches -> diffusion loss
shared multimodal Transformer
-> modality-specific encoders/decoders
-> sinh text và image
```

## Khi áp dụng

- Dùng khi so sánh discrete image tokenization với continuous diffusion.
- Cần chú ý objective mismatch giữa modalities.
- Multimodal model không nhất thiết phải dùng một loss cho mọi thứ.

## Kết quả / bằng chứng đáng giữ

- Abstract nói Transfusion combines language modeling loss with diffusion.
- Source nêu Transfusion scale tới 7B và 2T multimodal tokens.
- Paper báo cáo scaling tốt hơn quantizing images thành discrete image tokens theo abstract.

## Cách hiểu bằng lời của tôi

Transfusion nói rằng thống nhất model không nhất thiết là thống nhất objective. Text và ảnh có bản chất khác nhau, nên loss cũng có thể khác.

## Câu hỏi review

1. Transfusion dùng loss nào cho text và image?
2. Vì sao quantize image thành token rời rạc có giới hạn?
3. Modality-specific layers giúp gì?

## Liên kết

- [[Multimodal LLM]]
- [[Generative Model]]
- [[Autoregressive Language Model]]
- [[CS224N]]
