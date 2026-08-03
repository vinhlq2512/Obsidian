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
  - production
---

# Graph Optimization

## Định nghĩa

Graph optimization là nhóm kỹ thuật tối ưu computational graph của model để prediction nhanh hơn hoặc dùng ít memory hơn.

## Trong Chapter 08

Chapter 08 đặt graph optimization cạnh [[Knowledge Distillation]], [[Quantization]] và [[Pruning]] như một trong bốn kỹ thuật bổ trợ để làm Transformer hiệu quả hơn trong production.

Với [[ONNX]] và [[ONNX Runtime]], model được biểu diễn thành graph rồi runtime tối ưu cách thực thi graph đó.

## Cách hiểu bằng lời của tôi

Nếu distillation/pruning/quantization thay đổi model hoặc cách biểu diễn trọng số, graph optimization tập trung vào cách chạy model: sắp xếp, rút gọn hoặc tối ưu graph để inference hiệu quả hơn.

## Liên kết

- [[ONNX]]
- [[ONNX Runtime]]
- [[Transformer Inference Optimization]]

