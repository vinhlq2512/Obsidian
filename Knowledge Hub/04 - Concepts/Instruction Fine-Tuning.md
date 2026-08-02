---
type: concept
status: developing
sources:
  - "[[CS224N 2026 - Lecture 08 - Post-training]]"
  - "[[2022 - Scaling Instruction-Finetuned Language Models - arXiv 2210.11416v5]]"
source_sections:
  - "[[CS224N 2026 - Lecture 08 - Post-training]]"
first_seen: 2026-08-02
last_updated: 2026-08-02
tags:
  - concept
  - llm
  - cs224n
---

# Instruction Fine-Tuning

## Định nghĩa

Instruction fine-tuning là bước fine-tune [[Large Language Model]] trên dữ liệu dạng instruction-response để model học cách làm theo yêu cầu của người dùng thay vì chỉ dự đoán token tiếp theo theo phân phối text thô.

## Cách hiểu bằng lời của tôi

Pretraining dạy model "ngôn ngữ thường tiếp diễn như thế nào"; instruction fine-tuning dạy model "khi người dùng yêu cầu việc này, phản hồi hữu ích nên trông như thế nào".

## Pipeline

```text
pretrained LM
-> tập dữ liệu prompt / instruction / answer mẫu
-> supervised fine-tuning
-> model biết format trả lời và hành vi assistant cơ bản
-> có thể tiếp tục bằng RLHF hoặc DPO
```

## Điều cần biết

- Đây là cầu nối từ LM thuần sang assistant.
- Không nhất thiết thêm nhiều tri thức mới; chủ yếu định hình hành vi và format.
- Chất lượng data instruction ảnh hưởng mạnh tới helpfulness và robustness.

## Liên kết

- [[Fine-tuning]]
- [[RLHF]]
- [[DPO]]
- [[Large Language Model]]
- [[CS224N]]
