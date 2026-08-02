---
type: course-source
course: "[[CS224N]]"
status: developing
source_type: paper
title: "2023 - Direct Preference Optimization - Your Language Model is Secretly a Reward Model"
year: 2023
venue: "arXiv"
arxiv: "2305.18290v3"
source_file: "[[2023 - Direct Preference Optimization - Your Language Model is Secretly a Reward Model - arXiv 2305.18290v3.pdf]]"
pages: 27
created_at: 2026-08-02
updated_at: 2026-08-02
related_concepts:
  - "[[Large Language Model]]"
  - "[[Autoregressive Language Model]]"
  - "[[RLHF]]"
  - "[[DPO]]"
tags:
  - cs224n
  - paper
---

# 2023 - Direct Preference Optimization - Your Language Model is Secretly a Reward Model - arXiv 2305.18290v3

## Nguồn

- PDF gốc: [[2023 - Direct Preference Optimization - Your Language Model is Secretly a Reward Model - arXiv 2305.18290v3.pdf]]
- Đọc cùng: [[CS224N 2026 - Lecture 08 - Post-training]], [[CS224N 2026 - Lecture 09 - Efficient Adaptation]]
- Concept: [[DPO]], [[RLHF]]

## Vấn đề paper giải quyết

RLHF truyền thống phức tạp: train reward model rồi tối ưu policy bằng RL, dễ bất ổn và nhạy hyperparameter. DPO tìm cách học trực tiếp từ preference data mà không cần vòng RL riêng.

## Đóng góp chính

- Biến preference optimization thành objective supervised trực tiếp trên cặp chosen/rejected.
- Dựa trên quan hệ giữa reward và log-probability ratio so với reference model.
- Loại bỏ nhu cầu train reward model riêng và chạy PPO trong setup tiêu chuẩn.

## Cơ chế trực giác

Với prompt $x$, response thắng $y_w$, response thua $y_l$:

```text
tăng xác suất tương đối của y_w
-> giảm xác suất tương đối của y_l
-> so với reference model để tránh policy drift quá mạnh
```

## Vì sao quan trọng với CS224N

Lecture 08/09 dùng DPO như bước ngoặt: post-training hiện đại có thể “remove RL from RLHF” ở nhiều workflow open-source.

## Hạn chế / câu hỏi

- Chất lượng preference data vẫn là nút cổ chai.
- DPO tối ưu so sánh cặp, không tự đảm bảo factuality hay safety toàn diện.
- Reference model và beta ảnh hưởng tới mức độ drift.

## Câu hỏi review

1. DPO loại bỏ thành phần nào của RLHF truyền thống?
2. Vì sao cần reference model?
3. Preference pair chứa tín hiệu học nào?
