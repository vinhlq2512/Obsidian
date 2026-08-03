---
type: concept
status: seed
sources:
  - "[[NLP Transformers - Chapter 08 - Making Transformers Efficient in Production]]"
  - "[[2019 - The Lottery Ticket Hypothesis - Finding Sparse Trainable Neural Networks - arXiv 1803.03635v5]]"
source_sections:
  - "[[NLP Transformers - Chapter 08 - Making Transformers Efficient in Production]]"
first_seen: 2026-08-03
last_updated: 2026-08-03
tags:
  - concept
  - model-compression
  - transformer
  - production
---

# Pruning

## Định nghĩa

Pruning là kỹ thuật loại bỏ các phần ít quan trọng của model để giảm kích thước, giảm memory footprint hoặc tăng tốc inference.

## Vấn đề giải quyết

Transformer có nhiều tham số và phép tính dư thừa so với nhu cầu của một task production cụ thể. Pruning đặt câu hỏi: phần nào của model có thể bỏ đi mà chất lượng vẫn còn chấp nhận được?

## Cơ chế trực giác

```text
Model đầy đủ
-> Ước lượng mức quan trọng của weight/head/neuron/block
-> Loại bỏ phần ít quan trọng
-> Đánh giá lại accuracy, latency, memory
-> Fine-tune hoặc hiệu chỉnh nếu cần
```

## Weight pruning

Weight pruning là dạng pruning tác động trực tiếp lên trọng số. Một heuristic phổ biến là magnitude pruning: các weight có trị tuyệt đối nhỏ được xem là ít quan trọng hơn và bị đưa về 0 trước.

```text
W = ma trận trọng số
-> Tính |W|
-> Chọn ngưỡng hoặc tỉ lệ sparsity
-> W nhỏ hơn ngưỡng được đặt thành 0
-> Model trở nên sparse hơn
```

Sparsity là tỉ lệ trọng số bằng 0:

```text
sparsity = số weight bằng 0 / tổng số weight
```

Sau pruning, thường cần evaluate hoặc fine-tune lại vì việc đưa weight về 0 có thể làm giảm chất lượng. Fine-tuning giúp các weight còn lại thích nghi với cấu trúc sparse mới.

## Unstructured và structured pruning

| Kiểu pruning | Đơn vị bị prune | Khi nào đáng chú ý |
|---|---|---|
| Unstructured pruning | Từng weight riêng lẻ | Dễ tạo nhiều số 0, nhưng speedup phụ thuộc sparse kernel |
| Structured pruning | Neuron, attention head, channel, block hoặc layer | Dễ chuyển thành model nhỏ/chạy nhanh hơn, nhưng rủi ro quality lớn hơn |

Điểm mấu chốt cho production: giảm số tham số không đồng nghĩa giảm latency. Nếu runtime vẫn dùng dense computation, các weight bằng 0 không nhất thiết làm phép tính nhanh hơn.

## Trade-off

- Có thể giảm size và memory.
- Có thể tăng tốc nếu phần bị prune thật sự được runtime/hardware khai thác.
- Có nguy cơ giảm accuracy nếu loại bỏ quá mạnh.
- Sparse model không tự động nhanh hơn nếu backend inference không tối ưu cho sparsity.
- Structured pruning thường dễ tạo speedup thực tế hơn unstructured pruning, nhưng có thể làm mất capacity mạnh hơn.
- Cần benchmark lại bằng cùng [[Model Benchmarking|benchmark]] sau mỗi mức sparsity.

## Cách hiểu bằng lời của tôi

Pruning là ép model gọn hơn bằng cách cắt phần ít đóng góp. Nhưng cắt được tham số chưa chắc đã nhanh hơn; phải benchmark trên runtime thật.

Weight pruning có thể hiểu như biến một phần trọng số thành "im lặng". Nếu hệ thống chạy inference biết bỏ qua các trọng số im lặng đó, model có thể gọn/nhanh hơn. Nếu không, pruning chỉ làm model sparse trên giấy.

## Câu hỏi review

1. Weight pruning khác quantization ở đâu?
2. Magnitude pruning dựa trên giả định gì?
3. Sparsity được tính như thế nào?
4. Vì sao unstructured pruning chưa chắc tăng tốc inference?
5. Vì sao sau pruning thường cần fine-tune lại?

## Liên kết

- [[Transformer Inference Optimization]]
- [[Model Benchmarking]]
- [[Transformer]]
- [[Quantization]]
- [[CS224N 2026 - Lecture 09 - Efficient Adaptation]]
