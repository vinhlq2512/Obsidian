---
type: concept
status: understood
sources:
  - "[[2026-05-19_how-snapchat-serves-a-billion-predictions-per-second]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - system-design
  - machine-learning
  - prediction-serving
  - high-throughput
---

# High-Throughput Prediction Serving

## Định nghĩa

High-Throughput Prediction Serving (Hạ tầng phục vụ dự đoán ML băng thông cao) là mô hình kiến trúc được tối ưu hóa để thực thi hàng trăm triệu đến hàng tỷ lượt suy luận mô hình Machine Learning / Recommendation mỗi giây với độ trễ thấp (sub-10ms).

## Kiến trúc chính (Kinh nghiệm từ Snapchat / Meta)

```text
High QPS Request (User Activity Stream)
-> In-Memory Online Feature Store (Sub-millisecond Redis / C++ KV lookup)
-> Dynamic Request Batcher (Combine individual requests into GPU Tensor Batch)
-> Model Inference Engine (TensorRT / ONNX / C++ Operator Acceleration)
-> Prediction Response Stream
```

- **In-Memory Feature Lookup**: Đặt các feature online trong distributed in-memory cache (C++ custom store hoặc Aerospike/Redis) để đảm bảo feature retrieval time $< 2\text{ms}$.
- **Dynamic Micro-Batching**: Tự động gom hàng nghìn request lẻ trong khoảng cửa sổ vài microsecond thành một tensor duy nhất để tối ưu hóa hiệu năng tính toán song song của GPU.
- **Model Quantization & Pruning**: Chuyển đổi mô hình từ FP32/FP16 sang INT8 để giảm dung lượng bộ nhớ GPU và tăng tốc độ xử lý phần cứng.

## Trade-off

- **Latency vs Throughput**: Gom batch càng lớn thì throughput càng cao nhưng latency của request đầu tiên trong batch sẽ tăng lên.
- **Feature Freshness**: Cân đối giữa việc đọc feature sinh ra theo thời gian thực (stream feature) và feature đệm sẵn trong memory.

## Liên kết

- [[Online Feature Store]]
- [[ML Platform and Prediction Serving Patterns]]
- [[AI Model Serving]]
- [[Peak QPS]]
