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
  - inference
  - transformer
  - production
---

# ONNX

## Định nghĩa

ONNX (Open Neural Network Exchange) là một định dạng trao đổi model dùng để biểu diễn neural network dưới dạng graph có thể được tối ưu và chạy bởi runtime chuyên dụng.

## Vấn đề giải quyết

Khi đưa Transformer vào production, framework training không phải lúc nào cũng là lựa chọn inference nhanh nhất. ONNX giúp tách model khỏi framework gốc và mở đường cho graph optimization.

## Cơ chế trực giác

```text
Model trong framework training
-> Export sang ONNX graph
-> Runtime tối ưu graph
-> Chạy inference bằng backend tối ưu hơn
```

## Liên kết với ORT

[[ONNX Runtime]] là runtime dùng để chạy graph ONNX và áp dụng các tối ưu inference.

## Cách hiểu bằng lời của tôi

ONNX là lớp trung gian: biến model thành một graph chuẩn để các runtime production có thể tối ưu tốt hơn so với cách chạy trực tiếp trong framework huấn luyện.

## Liên kết

- [[ONNX Runtime]]
- [[Transformer Inference Optimization]]
- [[Graph Optimization]]
- [[Transformer]]

