---
type: concept
status: understood
sources:
  - "[[NLP Transformers - Chapter 08 - Making Transformers Efficient in Production]]"
  - "[[2026-01-20_this-isnt-an-ai-summarizer-and-that-matters-byte-sized-design]]"
source_sections:
  - "[[NLP Transformers - Chapter 08 - Making Transformers Efficient in Production]]"
first_seen: 2026-08-03
last_updated: 2026-08-03
tags:
  - concept
  - evaluation
  - production
  - transformer
---

# Model Benchmarking

## Định nghĩa

Model benchmarking là quá trình đo model bằng các chỉ số thực tế của deployment, không chỉ bằng accuracy.

## Trong production

Với Transformer production, benchmark nên theo dõi:

- accuracy hoặc metric task chính;
- latency trung bình;
- p95/p99 latency;
- throughput;
- memory footprint;
- model size;
- chi phí phần cứng.

## Creating a Performance Benchmark

Một performance benchmark là một phép đo lặp lại được, dùng cùng input, cùng hardware và cùng điều kiện chạy để so sánh nhiều model hoặc nhiều phiên bản tối ưu của cùng một model.

Benchmark tối thiểu nên trả lời:

- Model dự đoán đúng đến đâu?
- Mỗi prediction mất bao lâu?
- Latency đuôi như p95/p99 có chấp nhận được không?
- Model chiếm bao nhiêu disk/memory?
- Thay đổi tối ưu có làm metric task giảm quá nhiều không?

## Quy trình benchmark

```text
Chọn dataset / sample đại diện
-> Chọn metric task chính
-> Warm up model
-> Chạy nhiều prediction lặp lại
-> Đo latency trung bình và p95/p99
-> Đo memory footprint và model size
-> So sánh với baseline
```

## Checklist thực hành

- Giữ input benchmark cố định giữa các lần chạy.
- Tách warmup khỏi lần đo thật vì lần đầu thường chậm hơn.
- Đo nhiều lần thay vì chỉ một request.
- Báo cáo cả latency trung bình và p95/p99, vì production hay đau ở tail latency.
- Ghi hardware/runtime, ví dụ CPU/GPU, batch size, framework, ONNX/ORT hay PyTorch.
- So sánh accuracy/F1 cùng với latency/memory, không chỉ tối ưu tốc độ.

## Ví dụ code tối thiểu

```python
import time
from statistics import mean

def benchmark(fn, inputs, warmup=5):
    for x in inputs[:warmup]:
        fn(x)

    times = []
    for x in inputs:
        start = time.perf_counter()
        fn(x)
        times.append(time.perf_counter() - start)

    times_ms = [t * 1000 for t in times]
    times_ms_sorted = sorted(times_ms)
    p95 = times_ms_sorted[int(len(times_ms_sorted) * 0.95)]

    return {
        "avg_latency_ms": round(mean(times_ms), 2),
        "p95_latency_ms": round(p95, 2),
        "num_runs": len(times_ms),
    }
```

## Vì sao quan trọng

Các kỹ thuật như [[Knowledge Distillation]], [[Quantization]], [[Pruning]] và [[ONNX Runtime]] đều là trade-off. Một thay đổi có thể giảm memory nhưng làm giảm accuracy, hoặc giảm size nhưng không tăng tốc nếu runtime không khai thác được.

## Benchmark distilled model

Với [[Knowledge Distillation]], benchmark không chỉ hỏi student đúng đến đâu, mà hỏi student có đáng thay teacher trong production không.

So sánh tối thiểu:

| Model | Vai trò | Cần đo |
|---|---|---|
| Teacher | Mốc quality cao nhưng thường chậm/nặng | quality, latency, memory |
| Student trước distillation | Mốc model nhỏ chưa học teacher | quality, latency, memory |
| Distilled student | Candidate deploy | quality, latency, memory |

Một distilled model tốt có thể thấp hơn teacher một chút về quality, miễn là latency/memory cải thiện đủ nhiều và quality vẫn đạt ngưỡng sản phẩm.

Checklist đọc kết quả:

- Quality drop so với teacher có chấp nhận được không?
- Student có nhanh hơn thật trên runtime/hardware mục tiêu không?
- Memory footprint và model size có giảm đủ không?
- Student có tốt hơn baseline student chưa distill không?
- Kết quả có được đo cùng input, cùng batch size và cùng điều kiện chạy không?

## Cách hiểu bằng lời của tôi

Benchmark là bảng điều khiển của production. Nếu không đo latency, memory và accuracy cùng nhau, mình không biết tối ưu có thật sự tốt hơn hay chỉ làm model khác đi.

Điểm quan trọng nhất: benchmark phải đủ ổn định để so sánh. Nếu đổi input, đổi batch size hoặc quên warmup, kết quả latency rất dễ nhiễu và có thể dẫn tới quyết định sai.

Với AI ops/agent, benchmark còn cần case thật đã label. Bits AI SRE được đánh giá trên incident production đã có root cause từ human responders, vì mục tiêu không phải summarize telemetry mà là đi đúng causal chain.

## Câu hỏi review

1. Vì sao benchmark production không thể chỉ dùng accuracy?
2. Vì sao cần warmup trước khi đo latency?
3. p95/p99 latency nói điều gì mà latency trung bình không nói?
4. Khi một model nhỏ hơn nhưng accuracy giảm, nên đọc trade-off như thế nào?
5. Khi benchmark distilled model, vì sao cần so với cả teacher và baseline student?

## Liên kết

- [[Transformer Inference Optimization]]
- [[LLM Evaluation]]
- [[Agent Evaluation]]
- [[Knowledge Distillation]]
- [[Quantization]]
- [[Pruning]]
- [[ONNX Runtime]]
