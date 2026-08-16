---
type: concept
status: developing
sources:
  - "[[2026-01-19_why-ai-needs-gpus-and-tpus-the-hardware-behind-llms]]"
  - "[[2026-03-07_ep205-cpu-vs-gpu-vs-tpu]]"
  - "[[2026-01-05_how-googles-tensor-processing-unit-tpu-works]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - llm
  - hardware
  - inference
---

# AI Hardware Accelerator

## Định nghĩa

AI hardware accelerator là phần cứng tối ưu cho workload neural network, đặc biệt là matrix multiplication, parallel arithmetic và high-bandwidth memory.

## Cách hiểu bằng lời của tôi

LLM không chỉ là phần mềm; nó là bài toán di chuyển và nhân ma trận cực lớn. CPU giỏi branch/logic tuần tự, còn GPU/TPU dành nhiều silicon hơn cho arithmetic song song và memory bandwidth.

## Vì sao CPU không đủ

- Neural network ít branching nên không tận dụng tốt branch prediction/out-of-order execution.
- Matrix multiplication có nhiều phép tính độc lập, hợp với massive parallelism.
- Model lớn bị giới hạn bởi memory wall: phải đọc rất nhiều weight từ memory cho mỗi forward pass.

## GPU và TPU

- GPU dùng nhiều core đơn giản, SIMT/warp và Tensor Core để tăng throughput matrix operation.
- HBM đặt memory gần compute để tăng bandwidth.
- TPU chuyên biệt hơn, bỏ bớt logic general-purpose để tối ưu tensor operation.
- Low precision như FP16/BF16/INT8/4-bit quan trọng vì giảm memory và tăng throughput khi hardware hỗ trợ.

## Liên kết

- [[LLM Inference Engineering]]
- [[Transformer Inference Optimization]]
- [[Quantization]]
- [[KV Cache]]
- [[Model Benchmarking]]
