---
type: course-source
course: "[[CS224N]]"
status: completed
source_type: paper
title: "2025 - Multimodal RewardBench - Holistic Evaluation of Reward Models for Vision Language Models"
year: 2025
venue: "arXiv"
arxiv: "2502.14191v1"
source_file: "[[2025 - Multimodal RewardBench - Holistic Evaluation of Reward Models for Vision Language Models - arXiv 2502.14191v1.pdf]]"
pages: 17
created_at: 2026-08-02
updated_at: 2026-08-03
completed_at: 2026-08-03
related_concepts:
  - "[[Large Language Model]]"
  - "[[Autoregressive Language Model]]"
  - "[[Measuring the Quality of Generated Text]]"
  - "[[RLHF]]"
  - "[[DPO]]"
  - "[[Multimodal LLM]]"
tags:
  - cs224n
  - paper
---

# 2025 - Multimodal RewardBench - Holistic Evaluation of Reward Models for Vision Language Models - arXiv 2502.14191v1

## Nguồn

- PDF gốc: [[2025 - Multimodal RewardBench - Holistic Evaluation of Reward Models for Vision Language Models - arXiv 2502.14191v1.pdf]]
- Vai trò trong CS224N: benchmark/evaluation cho reward models trong vision-language setting.

## Câu hỏi trung tâm

Reward models cho VLM có đánh giá tốt preference đa phương thức không?

## Kiến thức cốt lõi

- Reward model trong multimodal setting phải chấm cả alignment text-image và preference ngôn ngữ.
- Benchmark holistic cần nhiều loại lỗi: factuality, visual grounding, safety, helpfulness.
- Reward model tốt cho text chưa chắc tốt cho vision-language.
- Evaluation reward model quan trọng vì nó có thể điều khiển post-training.
- Paper nối RLHF/DPO với Multimodal LLM evaluation.

## Cơ chế / công thức / kiến trúc

```text
image + prompt + candidate responses
-> reward model score/preference
-> benchmark so với nhãn/rubric
-> phân tích năng lực và failure modes
```

## Khi áp dụng

- Dùng khi post-train VLM bằng preference data.
- Không dùng reward model text-only để chấm visual grounding mà không kiểm chứng.
- Benchmark cần tách lỗi nhìn sai ảnh với lỗi trả lời kém.

## Kết quả / bằng chứng đáng giữ

- Title nêu holistic evaluation of reward models for vision language models.
- Lecture 11 nhấn mạnh holistic evaluation và model-based metrics.
- Source thuộc nhóm multimodal + evaluation trong CS224N.

## Cách hiểu bằng lời của tôi

Reward model là “giám khảo” của post-training. Với multimodal, giám khảo phải thật sự nhìn và hiểu ảnh, không chỉ thích văn phong.

## Câu hỏi review

1. Reward model multimodal phải chấm thêm gì so với text-only?
2. Vì sao reward model sai nguy hiểm cho alignment?
3. Holistic benchmark cần bao phủ những loại lỗi nào?

## Liên kết

- [[Reward Model]]
- [[RLHF]]
- [[Multimodal LLM]]
- [[Measuring the Quality of Generated Text]]
- [[CS224N]]
