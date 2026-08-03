---
type: course-source
course: "[[CS224N]]"
status: completed
source_type: paper
title: "2022 - Scaling Instruction-Finetuned Language Models"
year: 2022
venue: "arXiv"
arxiv: "2210.11416v5"
source_file: "[[2022 - Scaling Instruction-Finetuned Language Models - arXiv 2210.11416v5.pdf]]"
pages: 54
created_at: 2026-08-02
updated_at: 2026-08-03
completed_at: 2026-08-03
related_concepts:
  - "[[Large Language Model]]"
  - "[[Autoregressive Language Model]]"
  - "[[Fine-tuning]]"
  - "[[RLHF]]"
tags:
  - cs224n
  - paper
---

# 2022 - Scaling Instruction-Finetuned Language Models - arXiv 2210.11416v5

## Nguồn

- PDF gốc: [[2022 - Scaling Instruction-Finetuned Language Models - arXiv 2210.11416v5.pdf]]
- Vai trò trong CS224N: paper nền về instruction tuning ở scale lớn.

## Câu hỏi trung tâm

Instruction fine-tuning scale theo model size/task mixture như thế nào và giúp generalization ra sao?

## Kiến thức cốt lõi

- Instruction tuning fine-tune model trên tập instruction-response đa nhiệm.
- Scale model và scale task mixture có thể cải thiện khả năng làm theo instruction mới.
- Instruction-tuned model thường hữu ích hơn pretrained LM thuần trong vai trò assistant.
- Data diversity quan trọng vì model học format và intent từ nhiều loại nhiệm vụ.
- Paper nối pretraining với post-training trong CS224N.

## Cơ chế / công thức / kiến trúc

```text
pretrained LM
-> mixture nhiều instruction tasks
-> supervised fine-tuning
-> model học mapping instruction -> response
-> generalize sang task/instruction mới
```

## Khi áp dụng

- Dùng trước RLHF/DPO như bước SFT.
- Cần chú ý chất lượng và đa dạng instruction data.
- Không nhầm instruction following với factual correctness tuyệt đối.

## Kết quả / bằng chứng đáng giữ

- Title trực tiếp nói scaling instruction-finetuned language models.
- Lecture 08 xem instruction fine-tuning là bước đầu của post-training.
- SLP Chapter 09 cũng đặt instruction tuning trước preference alignment.

## Cách hiểu bằng lời của tôi

Instruction tuning là lúc model học giao ước hội thoại: người dùng đưa yêu cầu, model phải trả lời theo mục tiêu của yêu cầu đó.

## Câu hỏi review

1. Instruction tuning khác pretraining objective ra sao?
2. Vì sao task mixture quan trọng?
3. Instruction tuning có thay thế RLHF/DPO không?

## Liên kết

- [[Instruction Fine-Tuning]]
- [[Fine-tuning]]
- [[RLHF]]
- [[Large Language Model]]
- [[CS224N]]
