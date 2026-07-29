---
type: reading-section
book: "[[Natural Language Processing with Transformers]]"
status: planned
chapter: 8
start_page: 234
end_page: 285
reading_date: 2026-08-03
planned_sessions:
  - "2026-08-03 | 234-259 | Benchmark latency, memory, accuracy và trade-off production | 60 phút"
  - "2026-08-04 | 260-285 | Distillation, quantization, ONNX, pruning và ghi lại quyết định | 60 phút"
estimated_minutes: 100
actual_minutes:
need_review: false
tags:
  - nlp
  - production
  - optimization
---

# NLP Transformers - Chapter 08 - Making Transformers Efficient in Production

## Mục tiêu đọc

- Hiểu các trade-off khi đưa Transformer vào production.
- Biết benchmark model theo latency, memory và accuracy.
- Nắm knowledge distillation, quantization, ONNX và pruning.

## Ý chính

- Model production cần cân bằng chất lượng, tốc độ, chi phí và độ ổn định.
- Distillation dùng teacher model lớn để huấn luyện student model nhỏ hơn.
- Quantization và ONNX Runtime có thể tăng tốc inference mà không cần đổi bài toán.

## Demo thực hành

Benchmark latency cơ bản cho sentiment pipeline.

```python
import time
from statistics import mean
from transformers import pipeline

classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
texts = ["Transformers are useful in production."] * 50

times = []
for text in texts:
    start = time.perf_counter()
    classifier(text)
    times.append(time.perf_counter() - start)

print("avg latency ms:", round(mean(times) * 1000, 2))
print("p95 latency ms:", round(sorted(times)[int(len(times) * 0.95)] * 1000, 2))
```

## Khái niệm quan trọng

- [[Model Benchmarking]]
- [[Knowledge Distillation]]
- [[Quantization]]
- [[ONNX Runtime]]
- [[Pruning]]

## Active Recall

1. Vì sao accuracy cao chưa đủ cho production?
2. Teacher-student distillation hoạt động như thế nào?
3. Quantization đánh đổi điều gì?
4. Benchmark nên đo những chỉ số nào?

## Checklist

- [ ] Đọc xong chapter
- [ ] Chạy demo benchmark
- [ ] Ghi lại latency trung bình
- [ ] Tách concept cần dùng lại
- [ ] Cập nhật tiến độ sách
