---
type: course-source
course: "[[CS224N]]"
status: completed
source_type: course-note
title: "CS224N 2019 - Notes - Computing Neural Network Gradients"
year: 2019
venue: ""
arxiv: ""
source_file: "[[CS224N 2019 - Notes - Computing Neural Network Gradients.pdf]]"
pages: 7
created_at: 2026-08-02
updated_at: 2026-08-03
completed_at: 2026-08-03
related_concepts:
  - "[[Feed-Forward Layer]]"
  - "[[Loss Function]]"
tags:
  - cs224n
  - course-note
---

# CS224N 2019 - Notes - Computing Neural Network Gradients

## Nguồn

- PDF gốc: [[CS224N 2019 - Notes - Computing Neural Network Gradients.pdf]]
- Vai trò trong CS224N: note phụ trợ về tính gradient neural network có kiểm soát shape.

## Câu hỏi trung tâm

Làm sao tính gradient cho neural network bằng vector/matrix calculus mà không lẫn dimensions?

## Kiến thức cốt lõi

- Jacobian biểu diễn đạo hàm vector-to-vector.
- Chain rule trong vector case tương ứng nhân Jacobian đúng thứ tự.
- Error terms giúp viết backprop gọn theo layer.
- Dimension matching là công cụ debug gradient quan trọng.
- Note giúp nối toán Lecture 03 với code assignment.

## Cơ chế / công thức / kiến trúc

```text
layer output z = Wx + b
loss L
upstream gradient dL/dz
-> dL/dW, dL/db, dL/dx
-> truyền tiếp về layer trước
```

## Khi áp dụng

- Dùng khi tự derive gradient cho affine layer, activation và loss.
- Nếu tích ma trận gradient không khớp shape, công thức sai.
- Nên viết dimensions bên cạnh từng tensor.

## Kết quả / bằng chứng đáng giữ

- Source text trình bày Jacobian identities và gradient dimensions.
- Note kết thúc với kiểm tra dimensions của các gradient terms.
- Đây là tài liệu học sâu hơn cho Lecture 03.

## Cách hiểu bằng lời của tôi

Tính gradient không chỉ là nhớ công thức; đó là giữ một bản đồ shape nhất quán từ loss quay ngược về từng tensor.

## Câu hỏi review

1. Jacobian của $z=Wx$ theo $x$ là gì?
2. Vì sao thứ tự nhân Jacobian quan trọng?
3. Error term trong backprop giúp gì?

## Liên kết

- [[Loss Function]]
- [[Feed-Forward Layer]]
- [[CS224N]]
