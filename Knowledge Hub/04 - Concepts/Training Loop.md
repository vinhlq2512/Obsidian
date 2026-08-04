---
type: concept
status: seed
sources:
  - "[[NLP Transformers - Chapter 10 - Training Transformers from Scratch]]"
source_sections:
  - "[[NLP Transformers - Chapter 10 - Training Transformers from Scratch]]"
first_seen: 2026-08-04
last_updated: 2026-08-04
tags:
  - concept
  - training
  - optimization
  - nlp
---

# Training Loop

## Định nghĩa

`Training Loop` là chuỗi bước lặp đi lặp lại để model học từ dữ liệu: lấy batch, chạy forward, tính loss, backpropagate, cập nhật weights và lưu/evaluate định kỳ.

## Luồng trực giác

```text
Batch dữ liệu
-> Forward pass
-> Tính [[Loss Function]]
-> Backward pass
-> Optimizer step
-> Logging / evaluation / checkpoint
-> Lặp lại
```

## Vì sao quan trọng

- Đây là nơi compute được tiêu thụ thực sự trong training.
- Khi pretraining lớn, bottleneck thường nằm ở throughput của training loop chứ không chỉ ở kiến trúc model.
- Data loading, batching, mixed precision, distributed training và checkpointing đều sống trong vòng này.

## Cách hiểu bằng lời của tôi

Training loop là “nhịp tim” của việc train model. Dữ liệu, loss và optimizer chỉ thật sự phối hợp với nhau khi đi qua vòng lặp này hàng triệu lần.

## Liên kết

- [[Loss Function]]
- [[AdamW]]
- [[Pretraining]]
- [[NLP Transformers - Chapter 10 - Training Transformers from Scratch]]
