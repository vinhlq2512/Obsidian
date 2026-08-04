---
type: concept
status: seed
sources:
  - "[[NLP Transformers - Chapter 02 - Text Classification]]"
  - "[[NLP Transformers - Chapter 08 - Making Transformers Efficient in Production]]"
source_sections:
  - "[[NLP Transformers - Chapter 02 - Text Classification]]"
  - "[[NLP Transformers - Chapter 08 - Making Transformers Efficient in Production]]"
first_seen: 2026-08-04
last_updated: 2026-08-04
tags:
  - concept
  - optimization
  - training
  - transformers
---

# AdamW

## Định nghĩa

`AdamW` là một optimizer rất phổ biến khi fine-tune Transformer. Có thể hiểu ngắn gọn: nó giữ cách update thích nghi theo từng tham số của [[Adam]], nhưng tách `weight decay` ra khỏi phần gradient update.

## Ý chính cần nhớ

- `Adam` dùng moving average của gradient và bình phương gradient để tự điều chỉnh step size theo từng tham số.
- `AdamW` thêm regularization kiểu weight decay theo cách **decoupled**, tức là phần shrink trọng số được tách riêng thay vì trộn trực tiếp vào gradient.
- Vì thế, `weight_decay` trong training config thường được hiểu tự nhiên hơn và ổn định hơn khi fine-tune model lớn.

## Công thức trực giác

Thay vì nghĩ:

```text
gradient = gradient + lambda * w
-> rồi Adam update
```

AdamW nghĩ theo kiểu:

```text
Adam update theo gradient
-> sau đó shrink weights một chút theo weight decay
```

Trực giác:

- gradient trả lời: "đi hướng nào để giảm [[Loss Function]]?"
- weight decay trả lời: "đừng để trọng số phình quá mức"

## Vì sao cần nó?

Khi fine-tuning, đặc biệt với mô hình nhiều tham số, chỉ tối ưu loss thôi có thể làm model overfit hoặc làm trọng số tăng không cần thiết. `AdamW` giúp:

- giữ lợi thế update thích nghi của Adam;
- thêm regularization qua `weight_decay`;
- làm việc chỉnh `learning_rate` và `weight_decay` dễ tách bạch hơn trong thực hành.

## Khi áp dụng

- Fine-tuning các mô hình Transformer qua `Trainer` hoặc training loop chuẩn.
- Các bài toán classification, token classification, seq2seq fine-tuning.
- Khi training config có các hyperparameters như `learning_rate`, `weight_decay`, `num_train_epochs`.

## Cần biết

- `weight_decay` là một hyperparameter, không phải learned parameter.
- `learning_rate` và `weight_decay` thường tương tác với nhau; giá trị tốt phụ thuộc dataset, số epoch và objective.
- Dù `AdamW` rất phổ biến, nó không thay thế việc cần validation set và [[Hyperparameter Optimization]].

## Cách hiểu bằng lời của tôi

AdamW là optimizer kiểu "Adam nhưng có kỷ luật hơn". Nó vẫn đi nhanh và linh hoạt theo gradient, nhưng đồng thời giữ trọng số không phình vô tội vạ bằng một lực kéo nhỏ từ `weight_decay`.

## Câu hỏi review

1. AdamW khác Adam ở ý chính nào?
2. Vì sao `weight_decay` lại quan trọng khi fine-tune?
3. Vì sao `learning_rate` tốt chưa chắc đi kèm `weight_decay` tốt?

## Liên kết

- [[Loss Function]]
- [[Hyperparameter Optimization]]
- [[Fine-Tuning XLM-RoBERTa]]
- [[NLP Transformers - Chapter 02 - Text Classification]]
