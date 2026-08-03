---
type: course-source
course: "[[CS224N]]"
status: completed
source_type: course-note
title: "CS224N 2019 - Notes 03 - Neural Networks and Backpropagation"
year: 2019
venue: ""
arxiv: ""
source_file: "[[CS224N 2019 - Notes 03 - Neural Networks and Backpropagation.pdf]]"
pages: 18
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

# CS224N 2019 - Notes 03 - Neural Networks and Backpropagation

## Nguồn

- PDF gốc: [[CS224N 2019 - Notes 03 - Neural Networks and Backpropagation.pdf]]
- Vai trò trong CS224N: lecture note chi tiết về neural network, loss, optimization và practical training tips.

## Câu hỏi trung tâm

Một neural network classifier được xây và train bằng backprop như thế nào?

## Kiến thức cốt lõi

- Single neuron thực hiện affine transform rồi qua activation.
- Nhiều neurons/layers tạo multilayer network cho classification.
- Loss như max-margin hoặc cross-entropy biến prediction thành objective.
- Backprop dùng chain rule để tính gradients tuần tự qua layers.
- Training thực tế cần initialization, learning rate, gradient check và optimizer như AdaGrad/RMSProp/Adam.

## Cơ chế / công thức / kiến trúc

```text
x
-> affine transform Wx+b
-> nonlinearity
-> hidden layer(s)
-> scores
-> loss
-> backprop gradients
-> optimizer update
```

## Khi áp dụng

- Dùng cho assignment neural network/dependency parsing.
- Luôn chạy gradient check khi tự viết backward.
- Initialization và learning rate có thể quyết định train thành công hay không.

## Kết quả / bằng chứng đáng giữ

- Source first page liệt kê keyphrases: neural networks, forward computation, backward propagation, max-margin loss, gradient checks, Xavier initialization, learning rates, Adagrad.
- Trang 2 giải thích sigmoid neuron và layer of neurons.
- Cuối note nhắc optimizer variants như RMSProp/Adam.

## Cách hiểu bằng lời của tôi

Lecture note này là cầu từ toán sang code: không chỉ biết đạo hàm, mà còn phải làm cho training chạy ổn định.

## Câu hỏi review

1. Một neuron tính gì?
2. Backprop dùng chain rule ra sao?
3. Gradient check phát hiện lỗi gì?
4. Vì sao optimizer khác SGD thuần hữu ích?

## Liên kết

- [[Loss Function]]
- [[Feed-Forward Layer]]
- [[Fine-tuning]]
- [[CS224N]]
