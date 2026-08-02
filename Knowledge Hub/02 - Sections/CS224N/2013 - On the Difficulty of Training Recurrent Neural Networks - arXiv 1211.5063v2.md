---
type: course-source
course: "[[CS224N]]"
status: developing
source_type: paper
title: "2013 - On the Difficulty of Training Recurrent Neural Networks"
year: 2013
venue: "arXiv"
arxiv: "1211.5063v2"
source_file: "[[2013 - On the Difficulty of Training Recurrent Neural Networks - arXiv 1211.5063v2.pdf]]"
pages: 12
created_at: 2026-08-02
updated_at: 2026-08-02
related_concepts:
  - "[[Feed-Forward Layer]]"
  - "[[Loss Function]]"
tags:
  - cs224n
  - paper
---

# 2013 - On the Difficulty of Training Recurrent Neural Networks - arXiv 1211.5063v2

## Nguồn

- PDF gốc: [[2013 - On the Difficulty of Training Recurrent Neural Networks - arXiv 1211.5063v2.pdf]]
- Đọc cùng: [[CS224N 2026 - Lecture 04 - Language Models and Recurrent Neural Networks]], [[CS224N 2026 - Lecture 05 - Attention and Transformers]]
- Concept: [[Autoregressive Language Model]], [[Loss Function]]

## Vấn đề paper giải quyết

RNN khó train vì vanishing và exploding gradients. Paper phân tích vấn đề này từ góc nhìn analytical, geometric và dynamical systems, rồi đề xuất giải pháp đơn giản cho exploding gradients.

## Đóng góp chính

- Làm rõ vì sao gradient qua nhiều bước thời gian có thể biến mất hoặc bùng nổ.
- Đề xuất gradient norm clipping để xử lý exploding gradients.
- Đặt nền trực giác cho việc tại sao sequence models tuần tự khó học dependency dài.

## Cơ chế cần nhớ

Trong BPTT, gradient phải nhân qua nhiều bước:

```text
loss tại thời điểm xa
-> gradient truyền ngược qua h_T, h_{T-1}, ..., h_1
-> nhân nhiều Jacobian
-> nhỏ dần hoặc lớn vọt
```

Nếu product có spectral behavior nhỏ hơn 1, gradient vanish; nếu lớn hơn 1, gradient explode.

## Vì sao quan trọng với CS224N

Lecture 04/05 dùng vấn đề này để giải thích tại sao attention và Transformer trở nên hấp dẫn: token không phải truyền thông tin qua một chuỗi hidden state dài nữa.

## Hạn chế / câu hỏi

- Gradient clipping giúp exploding gradients nhưng không giải quyết triệt để vanishing gradients.
- LSTM/GRU cải thiện RNN nhưng vẫn tuần tự, kém parallel hơn Transformer.

## Câu hỏi review

1. Vì sao gradient trong RNN phải nhân qua nhiều bước?
2. Gradient clipping xử lý exploding gradient như thế nào?
3. Vấn đề này dẫn tới nhu cầu attention ra sao?
