---
type: concept
status: seed
sources:
  - "[[NLP Transformers - Chapter 08 - Making Transformers Efficient in Production]]"
source_sections:
  - "[[NLP Transformers - Chapter 08 - Making Transformers Efficient in Production]]"
first_seen: 2026-08-03
last_updated: 2026-08-03
tags:
  - concept
  - transformer
  - inference
  - production
---

# Transformer Inference Optimization

## Định nghĩa

Transformer inference optimization là nhóm kỹ thuật làm prediction của Transformer nhanh hơn và/hoặc giảm memory footprint khi triển khai production.

## Bốn kỹ thuật trong Chapter 08

Chapter 08 giới thiệu bốn kỹ thuật bổ trợ:

| Kỹ thuật | Tác động chính | Mental model |
|---|---|---|
| [[Knowledge Distillation]] | Model nhỏ hơn | Chuyển hành vi từ teacher lớn sang student nhỏ |
| [[Quantization]] | Weight/activation ít bit hơn | Dùng biểu diễn số học rẻ hơn |
| [[Pruning]] | Ít phần model hơn | Loại bỏ phần ít quan trọng |
| [[ONNX Runtime]] / [[ONNX]] | Graph chạy tối ưu hơn | Chạy model bằng graph/runtime production |

## Quantization

[[Quantization]] là đòn bẩy làm số học rẻ hơn. Nó không nhất thiết làm model ít layer hơn hay đổi kiến trúc, mà đổi cách weight/activation được biểu diễn, ví dụ từ FP32/FP16 sang INT8 hoặc low-bit.

Tác động chính:

- giảm model size;
- giảm memory footprint;
- giảm memory bandwidth;
- có thể giảm latency nếu runtime/hardware hỗ trợ low-precision compute tốt.

Vì lợi ích phụ thuộc backend, model quantized phải được benchmark trên hardware/runtime mục tiêu, không chỉ đo trong notebook.

## Trục đánh đổi

Khi tối ưu Transformer cho production, không chỉ nhìn accuracy. Cần đo:

- latency;
- throughput;
- memory footprint;
- model size;
- accuracy hoặc metric task chính;
- độ ổn định khi chạy trên hardware thật.

## Vai trò của benchmark

Trước khi dùng distillation, quantization, pruning hoặc ONNX/ORT, cần tạo [[Model Benchmarking|performance benchmark]] cho baseline. Benchmark này là điểm neo để biết một kỹ thuật tối ưu có thật sự tốt hơn hay chỉ giảm một chỉ số và làm hỏng chỉ số khác.

Với [[Knowledge Distillation]], benchmark đặc biệt quan trọng vì student nhỏ hơn thường giảm latency/memory, nhưng cần kiểm tra quality có còn đủ gần teacher không.

## Cách hiểu bằng lời của tôi

Chapter này không nói "chọn một mẹo duy nhất", mà đưa bốn đòn bẩy khác nhau: làm model nhỏ hơn, làm số học rẻ hơn, cắt phần dư thừa, hoặc chạy graph hiệu quả hơn. Điểm chung là mọi thứ phải được benchmark theo latency, memory và accuracy.

## Câu hỏi review

1. Bốn kỹ thuật chính để tối ưu Transformer production là gì?
2. Kỹ thuật nào thay đổi model architecture hoặc size?
3. Kỹ thuật nào chủ yếu thay đổi cách biểu diễn/trình chạy inference?
4. Vì sao phải benchmark sau mỗi bước tối ưu?

## Liên kết

- [[Knowledge Distillation]]
- [[Quantization]]
- [[Pruning]]
- [[ONNX]]
- [[ONNX Runtime]]
- [[Model Benchmarking]]
- [[Transformer]]
