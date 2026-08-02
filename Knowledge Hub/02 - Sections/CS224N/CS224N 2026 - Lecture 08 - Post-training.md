---
type: course-source
course: "[[CS224N]]"
status: developing
source_type: lecture
title: "CS224N 2026 - Lecture 08 - Post-training"
year: 2026
venue: ""
arxiv: ""
source_file: "[[CS224N 2026 - Lecture 08 - Post-training.pdf]]"
pages: 64
created_at: 2026-08-02
updated_at: 2026-08-02
related_concepts:
  - "[[RLHF]]"
  - "[[DPO]]"
  - "[[Fine-tuning]]"
tags:
  - cs224n
  - lecture
---

# CS224N 2026 - Lecture 08 - Post-training

## Nguồn

- PDF gốc: [[CS224N 2026 - Lecture 08 - Post-training.pdf]]
- Vai trò trong khoá: từ pretrained LM sang assistant qua instruction tuning, [[RLHF]] và [[DPO]].
- Paper đọc kèm: [[2023 - Direct Preference Optimization - Your Language Model is Secretly a Reward Model - arXiv 2305.18290v3]], [[2022 - Scaling Instruction-Finetuned Language Models - arXiv 2210.11416v5]].

## Mục tiêu cần hiểu

- Language modeling không đồng nghĩa với biết giúp người dùng.
- [[Instruction Fine-Tuning|Instruction fine-tuning]] dạy model theo định dạng chỉ dẫn/phản hồi.
- RLHF dùng preference data và reward model để tối ưu hành vi.
- DPO thay phần RL phức tạp bằng loss trực tiếp trên cặp preferred/rejected.

## Ý chính

- Pretrained LM học phân phối text; assistant cần học intent, helpfulness, safety và format trả lời.
- [[Instruction Fine-Tuning|Instruction fine-tuning]] dùng data có prompt và response mong muốn để kéo model về hành vi “làm theo lệnh”.
- RLHF thường gồm: collect preference, train reward model, optimize policy với ràng buộc không lệch quá xa base model.
- RL/PPO có thể đắt, nhạy hyperparameter và phức tạp về infrastructure.
- DPO tận dụng quan hệ giữa reward và log-probability ratio để học trực tiếp từ preference pairs.

## Pipeline post-training

```text
pretrained LM
-> supervised [[Instruction Fine-Tuning|instruction fine-tuning]]
-> preference data: y_w tốt hơn y_l
-> reward modeling hoặc DPO
-> assistant model aligned hơn với người dùng
```

## DPO intuition

DPO dùng cặp $(x, y_w, y_l)$, trong đó $y_w$ là response được chọn và $y_l$ là response bị chê. Mục tiêu là tăng log-probability tương đối của $y_w$ so với $y_l$, đồng thời so với reference model để tránh drift quá mạnh.

Trực giác:

```text
Không cần train reward model riêng rồi chạy PPO.
Học trực tiếp: với cùng prompt, response thắng phải có xác suất tương đối cao hơn response thua.
```

## Cách hiểu bằng lời của tôi

Pretraining tạo model biết ngôn ngữ; post-training tạo model biết cư xử trong vai trò assistant. RLHF/DPO không chủ yếu dạy facts mới, mà định hình preference: trả lời nào được con người xem là hữu ích, đúng format, an toàn và đáng tin hơn.

## Câu hỏi review

1. Vì sao LM thuần có thể không làm assistant tốt?
2. [[Instruction Fine-Tuning|Instruction fine-tuning]] khác pretraining ở dữ liệu và mục tiêu nào?
3. RLHF gồm các bước chính nào?
4. DPO loại bỏ phần khó nào của RLHF truyền thống?
5. Preference pair chứa thông tin gì?

## Liên kết

- [[Fine-tuning]]
- [[RLHF]]
- [[DPO]]
- [[Large Language Model]]
- [[CS224N]]
