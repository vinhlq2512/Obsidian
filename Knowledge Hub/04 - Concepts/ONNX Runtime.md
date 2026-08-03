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

# ONNX Runtime

## Định nghĩa

ONNX Runtime (ORT) là runtime dùng để chạy model ở định dạng [[ONNX]], thường nhằm tối ưu inference latency và memory.

## Vấn đề giải quyết

Một model Transformer có thể đúng về mặt accuracy nhưng chưa đủ tốt cho production nếu latency cao hoặc memory footprint lớn. ORT hỗ trợ graph optimization để cải thiện prediction speed.

## Cơ chế

```text
ONNX graph
-> Graph optimization
-> Runtime execution tối ưu
-> Prediction nhanh hơn hoặc memory footprint thấp hơn
```

## Workflow inference

Trong workflow production, ORT thường xuất hiện sau khi model đã được export sang [[ONNX]].

```text
Model trong framework training
-> Export sang ONNX
-> Kiểm tra output parity
-> Load bằng ONNX Runtime
-> Chọn execution provider
-> Benchmark latency / memory / quality
```

Output parity nghĩa là output của ONNX/ORT model phải đủ gần output của model gốc trên cùng input. Nếu không kiểm tra bước này, ta có thể benchmark một model nhanh hơn nhưng đã đổi hành vi dự đoán.

## Tối ưu thường gặp

ORT có thể cải thiện inference bằng cách:

- tối ưu graph trước khi chạy;
- hợp nhất operator;
- loại bỏ computation không cần thiết;
- tối ưu constant trong graph;
- dùng execution provider phù hợp với CPU/GPU hoặc backend tăng tốc.

Điểm cần nhớ: ORT không đảm bảo mọi model đều nhanh hơn. Lợi ích phụ thuộc graph, opset, hardware, execution provider, batch size và shape của input.

## Trade-off

- Có thể tăng tốc inference mà không đổi bài toán học.
- Cần benchmark thực tế vì lợi ích phụ thuộc model, hardware và backend.
- Cần kiểm tra output parity sau khi export/optimize.
- Có thể gặp lỗi do unsupported ops, dynamic axes sai, opset không phù hợp hoặc sai khác số học nhỏ.

## Cách hiểu bằng lời của tôi

ORT là phần chạy model sau khi đã export sang ONNX. Nếu ONNX là bản graph chuẩn, ORT là engine cố gắng chạy graph đó nhanh và gọn hơn trong production.

Trong đầu mình nên xem ONNX/ORT như bước đổi "đường chạy" của model: model vẫn là model đó, nhưng inference được đưa sang graph/runtime tối ưu hơn. Vì vậy cần kiểm tra cả hai thứ: output còn đúng không và latency/memory có cải thiện thật không.

## Câu hỏi review

1. ONNX và ONNX Runtime khác nhau ở đâu?
2. Vì sao cần output parity test sau khi export ONNX?
3. Graph optimization giúp inference bằng những cách nào?
4. Vì sao ORT vẫn cần benchmark trên hardware mục tiêu?

## Liên kết

- [[ONNX]]
- [[Graph Optimization]]
- [[Transformer Inference Optimization]]
- [[Model Benchmarking]]
