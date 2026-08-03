---
type: course-source
course: "[[CS224N]]"
status: completed
source_type: paper
title: "2023 - Scaling Laws for Generative Mixed-Modal Language Models"
year: 2023
venue: "arXiv"
arxiv: "2301.03728v1"
source_file: "[[2023 - Scaling Laws for Generative Mixed-Modal Language Models - arXiv 2301.03728v1.pdf]]"
pages: 19
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

# 2023 - Scaling Laws for Generative Mixed-Modal Language Models - arXiv 2301.03728v1

## Nguồn

- PDF gốc: [[2023 - Scaling Laws for Generative Mixed-Modal Language Models - arXiv 2301.03728v1.pdf]]
- Vai trò trong CS224N: paper về scaling laws cho generative mixed-modal language models.

## Câu hỏi trung tâm

Khi scale model/data/compute cho mixed-modal generation, performance thay đổi theo quy luật nào?

## Kiến thức cốt lõi

- Scaling laws giúp dự đoán hiệu quả khi tăng model size, data hoặc compute.
- Mixed-modal models thêm độ phức tạp vì phải học cả text và visual/modal tokens.
- Trade-off không chỉ là tổng tokens mà còn là tỷ lệ data giữa modalities.
- Paper giúp lập kế hoạch train model multimodal bằng compute-aware decisions.
- Nó nối với chủ đề smart scaling và multimodal LLM.

## Cơ chế / công thức / kiến trúc

```text
chọn model size + data mixture + compute budget
-> pretrain mixed-modal LM
-> đo loss/performance theo scale
-> fit scaling relationship
-> dự đoán cấu hình hiệu quả hơn
```

## Khi áp dụng

- Dùng khi quyết định scale multimodal pretraining.
- Không áp scaling law text-only một cách máy móc cho multimodal.
- Cần tách metric theo modality và task.

## Kết quả / bằng chứng đáng giữ

- Title trực tiếp nói scaling laws for generative mixed-modal language models.
- CS224N sources đặt nó cạnh các paper Chameleon/Transfusion/multimodal generation.
- Cụm này liên hệ tới compute-aware scaling trong lecture pretraining.

## Cách hiểu bằng lời của tôi

Scaling law là la bàn cho việc tiêu compute. Với multimodal, la bàn này phải tính thêm modality balance, không chỉ số token text.

## Câu hỏi review

1. Scaling law dùng để dự đoán gì?
2. Mixed-modal làm scaling phức tạp hơn text-only thế nào?
3. Vì sao data mixture là biến quan trọng?

## Liên kết

- [[Multimodal LLM]]
- [[Large Language Model]]
- [[Generative Model]]
- [[CS224N]]
