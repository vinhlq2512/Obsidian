---
type: course-source
course: "[[CS224N]]"
status: completed
source_type: paper
title: "2017 - Derivatives Backpropagation and Vectorization - Justin Johnson"
year: 2017
venue: ""
arxiv: ""
source_file: "[[2017 - Derivatives Backpropagation and Vectorization - Justin Johnson.pdf]]"
pages: 7
created_at: 2026-08-02
updated_at: 2026-08-03
completed_at: 2026-08-03
related_concepts:
  - "[[Loss Function]]"
tags:
  - cs224n
  - paper
---

# 2017 - Derivatives Backpropagation and Vectorization - Justin Johnson

## Nguồn

- PDF gốc: [[2017 - Derivatives Backpropagation and Vectorization - Justin Johnson.pdf]]
- Vai trò trong CS224N: note toán nền cho derivatives, chain rule, gradient, Jacobian và vectorization khi train neural networks.

## Câu hỏi trung tâm

Làm thế nào hiểu derivative/backprop từ scalar đến vector/matrix để triển khai neural network đúng shape?

## Kiến thức cốt lõi

- Derivative đo mức output thay đổi khi input thay đổi nhỏ.
- Gradient là vector đạo hàm khi input là vector và output là scalar.
- Jacobian tổng quát hoá đạo hàm cho vector-to-vector functions.
- Backprop là chain rule có tổ chức qua computation graph.
- Vectorization giúp viết gradient theo tensor/matrix để chạy hiệu quả và kiểm tra shape.

## Cơ chế / công thức / kiến trúc

Chain rule scalar:

$$
rac{dz}{dx}=rac{dz}{dy}rac{dy}{dx}
$$

Trong vector case, phải theo dõi shape của Jacobian. Một cách debug quan trọng: dimension của các tích gradient phải khớp.

## Khi áp dụng

- Dùng khi tự derive backprop cho assignment CS224N.
- Khi code gradient, luôn kiểm tra shape trước khi kiểm tra số.
- Hữu ích để hiểu vì sao framework autodiff vẫn cần tư duy computation graph.

## Kết quả / bằng chứng đáng giữ

- Source bắt đầu từ derivative scalar rồi mở rộng sang gradient/Jacobian.
- Note nhấn mạnh derivative như xấp xỉ thay đổi local.
- Các ví dụ matrix/vector giúp nối toán với vectorized implementation.

## Cách hiểu bằng lời của tôi

Đạo hàm trong deep learning không đáng sợ nếu xem nó như tracking local change. Backprop chỉ là cách ghép nhiều local changes lại cho đúng shape.

## Câu hỏi review

1. Gradient khác derivative scalar thế nào?
2. Jacobian dùng khi function có input/output dạng gì?
3. Vì sao kiểm tra shape giúp tránh lỗi gradient?

## Liên kết

- [[Loss Function]]
- [[Feed-Forward Layer]]
- [[CS224N 2026 - Lecture 03 - Neural Network Foundations]]
- [[CS224N]]
