---
type: course-source
course: "[[CS224N]]"
status: completed
source_type: course-note
title: "CS224N 2017 - Review of Differential Calculus Theory"
year: 2017
venue: ""
arxiv: ""
source_file: "[[CS224N 2017 - Review of Differential Calculus Theory.pdf]]"
pages: 10
created_at: 2026-08-02
updated_at: 2026-08-03
completed_at: 2026-08-03
related_concepts:
  - "[[NLP]]"
tags:
  - cs224n
  - course-note
---

# CS224N 2017 - Review of Differential Calculus Theory

## Nguồn

- PDF gốc: [[CS224N 2017 - Review of Differential Calculus Theory.pdf]]
- Vai trò trong CS224N: tài liệu ôn differential calculus cho machine learning gradients.

## Câu hỏi trung tâm

Những khái niệm đạo hàm nào cần chắc để học backprop và optimization?

## Kiến thức cốt lõi

- Derivative đo local rate of change.
- Partial derivative đo thay đổi theo một biến khi giữ biến khác cố định.
- Gradient gom các partial derivatives của scalar function theo vector input.
- Chain rule là nền của backpropagation.
- Matrix/vector derivatives cần kiểm tra shape nghiêm túc.

## Cơ chế / công thức / kiến trúc

```text
scalar derivative
-> partial derivatives
-> gradient vector
-> Jacobian matrix
-> chain rule trên computation graph
```

Mục tiêu của note là làm toán phục vụ implementation, không phải calculus thuần lý thuyết.

## Khi áp dụng

- Ôn trước Lecture 03 nếu thấy backprop khó.
- Khi đọc công thức gradient, dịch về “output đổi bao nhiêu nếu input đổi một chút”.
- Dùng shape để kiểm tra đạo hàm vector/matrix.

## Kết quả / bằng chứng đáng giữ

- Tên source là review of differential calculus theory.
- Nó nằm trong folder CS224N source phụ trợ cho neural network foundations.
- Các note backprop khác trong folder dùng chung nền này.

## Cách hiểu bằng lời của tôi

Calculus trong CS224N là ngôn ngữ để nói model nên đổi tham số thế nào khi sai.

## Câu hỏi review

1. Gradient có cùng shape với đại lượng nào?
2. Chain rule xuất hiện ở đâu trong neural network?
3. Partial derivative khác total derivative thế nào?

## Liên kết

- [[Loss Function]]
- [[CS224N 2026 - Lecture 03 - Neural Network Foundations]]
- [[CS224N]]
