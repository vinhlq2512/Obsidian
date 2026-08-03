---
type: course-source
course: "[[CS224N]]"
status: completed
source_type: paper
title: "2019 - Parameter-Efficient Transfer Learning for NLP"
year: 2019
venue: "arXiv"
arxiv: "1902.00751v2"
source_file: "[[2019 - Parameter-Efficient Transfer Learning for NLP - arXiv 1902.00751v2.pdf]]"
pages: 13
created_at: 2026-08-02
updated_at: 2026-08-03
completed_at: 2026-08-03
related_concepts:
  - "[[NLP]]"
tags:
  - cs224n
  - paper
---

# 2019 - Parameter-Efficient Transfer Learning for NLP - arXiv 1902.00751v2

## Nguồn

- PDF gốc: [[2019 - Parameter-Efficient Transfer Learning for NLP - arXiv 1902.00751v2.pdf]]
- Vai trò trong CS224N: paper nền cho [[Adapter]] và [[Parameter-Efficient Fine-Tuning]].

## Câu hỏi trung tâm

Có thể adapt pretrained language model cho nhiều task mà không cần fine-tune toàn bộ tham số mỗi lần không?

## Kiến thức cốt lõi

- Full fine-tuning tạo một bản model riêng cho mỗi task, tốn storage và deployment cost.
- Adapter layers thêm module nhỏ vào model pretrained.
- Chỉ train adapter/task-specific parameters, giữ weight gốc gần như cố định.
- Cách này cho phép chia sẻ một backbone cho nhiều task.
- Paper đặt nền cho PEFT trước thời LoRA phổ biến.

## Cơ chế / công thức / kiến trúc

```text
pretrained model frozen/shared
-> chèn adapter modules vào layer
-> train adapter cho task mới
-> lưu adapter nhỏ thay vì cả model
```

Adapter thường có bottleneck để giới hạn số tham số thêm.

## Khi áp dụng

- Dùng khi cần nhiều task/domain nhưng không muốn lưu nhiều full checkpoints.
- Hữu ích khi compute/memory giới hạn.
- So sánh với LoRA: adapter thêm module, LoRA thêm low-rank update vào weight.

## Kết quả / bằng chứng đáng giữ

- Paper title và abstract tập trung vào transfer learning hiệu quả tham số.
- Lecture 09 dùng adapter như một PEFT method quan trọng.
- Adapter trade-off accuracy vs số tham số train được nhấn mạnh trong lecture.

## Cách hiểu bằng lời của tôi

Adapter là cách biến một model lớn thành nền chung, còn từng task chỉ mang theo một “miếng điều chỉnh” nhỏ.

## Câu hỏi review

1. Adapter tiết kiệm tham số bằng cách nào?
2. Vì sao sharing backbone hữu ích cho nhiều task?
3. Adapter khác LoRA ở vị trí can thiệp vào model như thế nào?

## Liên kết

- [[Adapter]]
- [[Parameter-Efficient Fine-Tuning]]
- [[Fine-tuning]]
- [[CS224N]]
