---
type: course-source
course: "[[CS224N]]"
status: completed
source_type: lecture
title: "CS224N 2026 - Lecture 04 - Language Models and Recurrent Neural Networks"
year: 2026
venue: ""
arxiv: ""
source_file: "[[CS224N 2026 - Lecture 04 - Language Models and Recurrent Neural Networks.pdf]]"
pages: 59
created_at: 2026-08-02
updated_at: 2026-08-03
completed_at: 2026-08-03
related_concepts:
  - "[[Feed-Forward Layer]]"
  - "[[Loss Function]]"
  - "[[Large Language Model]]"
  - "[[Autoregressive Language Model]]"
tags:
  - cs224n
  - lecture
---
# CS224N 2026 - Lecture 04 - Language Models and Recurrent Neural Networks

## Nguồn

- PDF gốc: [[CS224N 2026 - Lecture 04 - Language Models and Recurrent Neural Networks.pdf]]
- Vai trò trong khoá: đặt nền cho [[Autoregressive Language Model]], RNN, sequence modeling và các vấn đề gradient dẫn tới attention/Transformer.
- Paper đọc kèm: [[2013 - On the Difficulty of Training Recurrent Neural Networks - arXiv 1211.5063v2]].

## Mục tiêu cần hiểu

- Language modeling là gì và vì sao nó trở thành task nền cho NLP hiện đại.
- Cách phân rã xác suất chuỗi bằng chain rule.
- RNN xử lý chuỗi bằng hidden state lặp lại qua thời gian.
- Vì sao RNN gặp vanishing/exploding gradients khi học phụ thuộc dài.

## Ý chính

- Language model dự đoán token tiếp theo từ prefix: $P(w_t | w_{1:t-1})$.
- Một LM cũng gán xác suất cho cả chuỗi bằng tích các xác suất có điều kiện.
- Next-token prediction tưởng đơn giản nhưng buộc model học cú pháp, coreference, topic, factual association và nhiều pattern ngôn ngữ khác.
- RNN dùng hidden state để nén lịch sử đã đọc vào một vector, sau đó cập nhật state khi token mới đến.
- Điểm yếu của RNN là đường truyền thông tin dài phải đi qua nhiều bước lặp; gradient có thể nhỏ dần hoặc phình to.

## Công thức language model

Với chuỗi $w_1, ..., w_T$:

$$
P(w_1, ..., w_T) = \prod_{t=1}^{T} P(w_t | w_{1:t-1})
$$

Ở mỗi bước, model trả về phân phối trên vocabulary:

$$
P(w_t | w_{1:t-1})
$$

Training thường tối đa hoá log-likelihood của token thật, tương đương giảm cross-entropy/negative log-likelihood.

## RNN mental model

```text
x_t + h_{t-1}
-> RNN cell
-> h_t
-> output distribution for next token
```

Hidden state $h_t$ đóng vai trò “bộ nhớ nén” của prefix. Nếu câu dài, mọi thông tin cũ phải sống sót qua nhiều lần cập nhật $h$.

## Vanishing và exploding gradients

Trong backpropagation through time, gradient phải nhân qua nhiều Jacobian liên tiếp. Nếu các hệ số hiệu dụng nhỏ hơn 1, gradient giảm theo cấp số nhân; nếu lớn hơn 1, gradient tăng vọt.

Hệ quả:

- RNN khó học dependency xa.
- Model có xu hướng ưu tiên context gần.
- Training có thể không ổn định nếu gradient explode.
- Các kỹ thuật như gradient clipping, gated RNN, LSTM/GRU giúp giảm vấn đề nhưng không xoá hoàn toàn giới hạn tuần tự.

## Cách hiểu bằng lời của tôi

Language modeling là bài toán “viết tiếp” nhưng phần khó là prefix chứa rất nhiều loại thông tin. RNN giải bằng một bộ nhớ chạy tuần tự, nhưng bộ nhớ này giống một đường dây dài: tín hiệu từ đầu câu phải truyền qua nhiều bước, nên dễ bị yếu hoặc nhiễu. Đây là lý do attention xuất hiện như một cách cho token truy cập trực tiếp tới các token khác thay vì ép mọi thứ đi qua hidden state.

## Câu hỏi review

1. Vì sao LM có thể gán xác suất cho cả một đoạn text?
2. Hidden state trong RNN đại diện cho gì?
3. Vì sao next-token prediction lại học được nhiều năng lực ngôn ngữ?
4. Vanishing gradient ảnh hưởng tới dependency dài như thế nào?
5. RNN khác Transformer ở cách truyền thông tin giữa token ra sao?

## Gợi ý trả lời

1. Dùng chain rule để phân rã xác suất chuỗi thành tích xác suất từng token theo prefix.
2. Nó là biểu diễn nén của lịch sử đã đọc.
3. Để dự đoán token tiếp theo, model phải học cú pháp, nghĩa, chủ đề và quan hệ trong context.
4. Gradient từ token xa nhỏ dần khi truyền qua nhiều bước, nên model khó học liên hệ xa.
5. RNN truyền thông tin tuần tự qua state; Transformer cho token attention trực tiếp tới token khác.

## Liên kết

- [[Autoregressive Language Model]]
- [[Causal Language Model]]
- [[Text Generation]]
- [[Transformer]]
- [[CS224N]]
