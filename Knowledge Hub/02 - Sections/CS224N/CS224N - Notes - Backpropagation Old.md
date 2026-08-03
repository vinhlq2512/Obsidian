---
type: course-source
course: "[[CS224N]]"
status: completed
source_type: course-note
title: "CS224N - Notes - Backpropagation Old"
year: 
venue: ""
arxiv: ""
source_file: "[[CS224N - Notes - Backpropagation Old.pdf]]"
pages: 4
created_at: 2026-08-02
updated_at: 2026-08-03
completed_at: 2026-08-03
related_concepts:
  - "[[Loss Function]]"
tags:
  - cs224n
  - course-note
---

# CS224N - Notes - Backpropagation Old

## Nguồn

- PDF gốc: [[CS224N - Notes - Backpropagation Old.pdf]]
- Vai trò trong CS224N: note phụ trợ về backpropagation bản cũ, hữu ích cho assignment và hiểu chain rule trong neural networks.

## Câu hỏi trung tâm

Backprop tính gradient trong mạng nhiều tầng bằng cách nào và vì sao hiệu quả hơn tính đạo hàm từng tham số thủ công?

## Kiến thức cốt lõi

- Backprop là chain rule trên computation graph.
- Forward pass lưu intermediate activations.
- Backward pass truyền error signal từ loss về từng layer.
- Gradient của tham số được tính từ local derivative và upstream gradient.
- Hiểu backprop giúp debug assignment trước khi phó mặc cho autodiff.

## Cơ chế / công thức / kiến trúc

```text
x -> layer1 -> layer2 -> loss
forward: lưu activation
backward: dL/dlayer2 -> dL/dlayer1 -> dL/dW
update: W = W - lr * gradient
```

## Khi áp dụng

- Dùng khi derive gradient cho neural net assignment.
- Luôn kiểm tra dimensions của gradient.
- So sánh analytic gradient với numerical gradient để debug.

## Kết quả / bằng chứng đáng giữ

- Tên note và cụm CS224N backprop chỉ ra vai trò phụ trợ toán/training.
- Nó được đọc cùng Lecture 03 Neural Network Foundations.
- Backprop là nền cho mọi kiến trúc sau này trong khoá.

## Cách hiểu bằng lời của tôi

Backprop là kế toán lỗi: mỗi node trong graph nhận phần lỗi downstream, nhân với đạo hàm local, rồi chuyển phần trách nhiệm về input/tham số của mình.

## Câu hỏi review

1. Forward pass cần lưu gì cho backward?
2. Upstream gradient là gì?
3. Vì sao numerical gradient check hữu ích?

## Liên kết

- [[Loss Function]]
- [[Feed-Forward Layer]]
- [[CS224N 2026 - Lecture 03 - Neural Network Foundations]]
- [[CS224N]]
