---
type: course-source
course: "[[CS224N]]"
status: completed
source_type: lecture
title: "CS224N 2026 - Lecture 03 - Neural Network Foundations"
year: 2026
venue: ""
arxiv: ""
source_file: "[[CS224N 2026 - Lecture 03 - Neural Network Foundations.pdf]]"
pages: 80
created_at: 2026-08-02
updated_at: 2026-08-03
completed_at: 2026-08-03
related_concepts:
  - "[[Feed-Forward Layer]]"
  - "[[Loss Function]]"
tags:
  - cs224n
  - lecture
---
# CS224N 2026 - Lecture 03 - Neural Network Foundations

## Nguồn

- PDF gốc: [[CS224N 2026 - Lecture 03 - Neural Network Foundations.pdf]]
- Vai trò trong khoá: nền toán và triển khai cho [[Loss Function]], backpropagation, matrix calculus và neural network training.
- Note đọc kèm: [[CS224N 2019 - Notes 03 - Neural Networks and Backpropagation]], [[CS224N 2019 - Notes - Computing Neural Network Gradients]], [[2017 - Derivatives Backpropagation and Vectorization - Justin Johnson]].

## Mục tiêu cần hiểu

- Neural network là chuỗi phép biến đổi differentiable có tham số.
- Loss function biến chất lượng dự đoán thành một scalar cần tối ưu.
- Backpropagation dùng chain rule để tính gradient hiệu quả qua computation graph.
- Matrix calculus giúp viết gradient cho batch/vector thay vì từng scalar.

## Ý chính

- Lecture nối từ word vector evaluation sang câu hỏi lớn hơn: làm sao train một model có nhiều tầng bằng gradient.
- Neural network không chỉ là nhiều linear layers; nonlinearity là điều làm model biểu diễn được hàm phức tạp.
- Training gồm forward pass để tính prediction/loss và backward pass để tính gradient theo từng tham số.
- Backpropagation là dynamic programming trên computation graph: lưu intermediate values ở forward, truyền gradient ngược ở backward.
- Trong NLP, phần lớn kiến trúc hiện đại vẫn dựa trên cùng nguyên lý: tensor đi qua các layer differentiable, loss scalar kéo toàn bộ tham số đi theo hướng giảm lỗi.

## Mental model

```text
input x
-> linear / affine transform
-> nonlinearity
-> prediction y_hat
-> loss L(y_hat, y)
-> backprop tính dL/dtheta
-> optimizer cập nhật theta
```

Điểm cần giữ: backprop không phải “thuật toán riêng cho neural net”, mà là chain rule có tổ chức trên graph tính toán.

## Công thức lõi

Một layer tuyến tính thường có dạng:

$$
z = Wx + b
$$

Sau đó qua nonlinearity:

$$
h = f(z)
$$

Nếu loss là $L$, gradient cần cho update là:

$$
\frac{\partial L}{\partial W}, \quad \frac{\partial L}{\partial b}
$$

Với chain rule, nếu $L$ phụ thuộc vào $h$, $h$ phụ thuộc vào $z$, và $z$ phụ thuộc vào $W$:

$$
\frac{\partial L}{\partial W} = \frac{\partial L}{\partial h}\frac{\partial h}{\partial z}\frac{\partial z}{\partial W}
$$

Trực giác: mỗi node trong graph nhận “mức lỗi từ downstream”, nhân với đạo hàm local của nó, rồi gửi tiếp gradient về upstream.

## Backpropagation như luồng tín hiệu lỗi

- Forward pass trả lời: với tham số hiện tại, model dự đoán gì?
- Loss trả lời: dự đoán sai bao nhiêu?
- Backward pass trả lời: tham số nào góp bao nhiêu vào lỗi?
- Optimizer trả lời: nên đổi tham số theo hướng nào?

Nếu một tham số làm loss tăng khi tăng tham số, gradient dương; gradient descent sẽ giảm tham số đó. Nếu gradient âm, update sẽ tăng tham số.

## Cách hiểu bằng lời của tôi

Neural network học bằng cách biến mọi quyết định thành phép tính liên tục. Khi output sai, loss tạo một tín hiệu lỗi scalar. Backprop lan tín hiệu đó ngược qua từng phép tính, mỗi phép tính chỉ cần biết đạo hàm local của mình. Vì vậy một mạng rất lớn vẫn train được nếu graph differentiable và gradient không bị mất ổn định.

## Câu hỏi review

1. Vì sao cần nonlinearity giữa các linear layers?
2. Forward pass và backward pass khác nhau thế nào?
3. Backprop dùng chain rule ở đâu?
4. Vì sao loss phải là scalar?
5. Matrix calculus giúp gì khi train theo batch?

## Gợi ý trả lời

1. Nhiều linear layers ghép lại vẫn là một linear transform; nonlinearity tạo khả năng biểu diễn hàm phức tạp.
2. Forward tính output/loss; backward tính gradient của loss theo tham số.
3. Mỗi node nhân gradient downstream với đạo hàm local để truyền ngược.
4. Scalar loss cho ta một mục tiêu tối ưu duy nhất để lấy gradient.
5. Nó cho phép biểu diễn gradient gọn bằng ma trận/tensor, chạy hiệu quả trên batch và GPU.

## Liên kết

- [[Loss Function]]
- [[Feed-Forward Layer]]
- [[Embedding]]
- [[CS224N]]
