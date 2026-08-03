---
type: course-source
course: "[[CS224N]]"
status: completed
source_type: paper
title: "2016 - Layer Normalization"
year: 2016
venue: "arXiv"
arxiv: "1607.06450v1"
source_file: "[[2016 - Layer Normalization - arXiv 1607.06450v1.pdf]]"
pages: 14
created_at: 2026-08-02
updated_at: 2026-08-03
completed_at: 2026-08-03
related_concepts:
  - "[[Layer Normalization]]"
tags:
  - cs224n
  - paper
---

# 2016 - Layer Normalization - arXiv 1607.06450v1

## Nguồn

- PDF gốc: [[2016 - Layer Normalization - arXiv 1607.06450v1.pdf]]
- Vai trò trong CS224N: paper nền cho [[Layer Normalization]], kỹ thuật cực quan trọng trong RNN và Transformer.

## Câu hỏi trung tâm

Có thể chuẩn hoá activation mà không phụ thuộc mini-batch như batch normalization không?

## Kiến thức cốt lõi

- Batch normalization phụ thuộc mini-batch, khó dùng cho online learning, batch nhỏ và RNN.
- Layer normalization tính mean/variance trên các unit trong cùng layer của một training case.
- Vì không phụ thuộc các example khác trong batch, layer norm phù hợp hơn với sequence models.
- Layer norm giúp training nhanh và ổn định hơn.
- Trong Transformer, layer norm trở thành thành phần mặc định quanh attention/feed-forward blocks.

## Cơ chế / công thức / kiến trúc

Với hidden vector $h$ trong một layer:

```text
mean = trung bình các chiều của h
variance = phương sai các chiều của h
normalized = (h - mean) / sqrt(variance + eps)
output = gamma * normalized + beta
```

Khác batch norm: thống kê lấy theo feature trong một sample, không lấy theo batch.

## Khi áp dụng

- Dùng trong Transformer blocks để ổn định training.
- Đặc biệt hữu ích khi batch size nhỏ hoặc sequence model có độ dài thay đổi.
- Khi đọc architecture, chú ý pre-norm vs post-norm vì ảnh hưởng ổn định training.

## Kết quả / bằng chứng đáng giữ

- Abstract so sánh batch normalization với layer normalization.
- Source nêu batch norm phụ thuộc mini-batch và khó áp dụng cho RNN.
- Paper cho thấy layer norm cải thiện training time và generalization trong nhiều RNN models.

## Cách hiểu bằng lời của tôi

Layer norm là cách giữ scale tín hiệu ổn định bên trong một sample. Nó làm deep network bớt “trôi” activation, đặc biệt khi batch không phải nơi đáng tin để lấy thống kê.

## Câu hỏi review

1. Layer norm khác batch norm ở trục lấy mean/variance nào?
2. Vì sao batch norm khó dùng trong RNN?
3. Layer norm nằm ở đâu trong Transformer block?

## Liên kết

- [[Layer Normalization]]
- [[Transformer]]
- [[Feed-Forward Layer]]
- [[CS224N]]
