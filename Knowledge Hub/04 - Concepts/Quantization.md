---
type: concept
status: developing
sources:
  - "[[QLoRA]]"
  - "[[NLP Transformers - Chapter 08 - Making Transformers Efficient in Production]]"
source_sections:
  - "[[QLoRA]]"
  - "[[NLP Transformers - Chapter 08 - Making Transformers Efficient in Production]]"
first_seen: 2026-08-03
last_updated: 2026-08-03
tags:
  - concept
  - compression
  - llm
---

# Quantization

## Định nghĩa

Quantization là kỹ thuật biểu diễn trọng số hoặc activation của model bằng số bit thấp hơn, ví dụ 8-bit hoặc 4-bit, thay vì dùng precision cao như FP16/BF16/FP32.

## Cơ chế chung

Ý tưởng cơ bản là ánh xạ một tập giá trị precision cao sang một tập giá trị rời rạc nhỏ hơn.

```text
Weight precision cao
-> Chia thành miền hoặc block
-> Tính scale/zero-point hoặc normalization
-> Mã hóa bằng số bit thấp hơn
-> Dequantize khi cần tính toán xấp xỉ
```

## Vì sao dùng trong LLM

- Giảm memory để load hoặc fine-tune model lớn.
- Giảm bandwidth khi đọc weight.
- Có thể giúp triển khai model trên phần cứng hạn chế hơn.

## Trong production inference

Trong [[NLP Transformers - Chapter 08 - Making Transformers Efficient in Production]], quantization là một trong bốn kỹ thuật để tăng tốc prediction và giảm memory footprint của Transformer, cùng với [[Knowledge Distillation]], [[Pruning]] và graph optimization bằng [[ONNX]] / [[ONNX Runtime]].

Điểm cần nhớ: quantization không đổi bài toán mô hình hóa, mà đổi cách biểu diễn số học của model để chạy gọn hơn. Vì vậy luôn cần benchmark lại accuracy, latency và memory.

## Making models faster

Quantization có thể làm model nhanh hơn vì low-precision numbers chiếm ít bộ nhớ hơn và có thể được tính bằng kernels tối ưu hơn trên phần cứng phù hợp.

```text
FP32/FP16 weights
-> INT8 hoặc low-bit representation
-> Ít byte hơn mỗi tham số
-> Đọc weight nhanh hơn / cache hiệu quả hơn
-> Matrix multiplication có thể rẻ hơn
-> Latency thấp hơn nếu runtime hỗ trợ
```

Lợi ích quan trọng không chỉ nằm ở phép nhân số học. Với Transformer lớn, việc đọc weight từ memory cũng rất đắt. Khi mỗi weight dùng ít byte hơn, memory bandwidth giảm, nên inference có thể nhanh hơn ngay cả khi mô hình logic không đổi.

## Công thức trực giác

Một cách nhìn đơn giản là ánh xạ giá trị thực sang integer:

```text
x_quant = round(x / scale) + zero_point
x_approx = scale * (x_quant - zero_point)
```

Trong đó:

- `x`: giá trị gốc precision cao;
- `scale`: hệ số đổi miền giá trị thực sang miền integer;
- `zero_point`: điểm dịch để biểu diễn được miền giá trị mong muốn;
- `x_quant`: giá trị đã lượng tử hóa;
- `x_approx`: giá trị xấp xỉ khi dequantize.

Trực giác: quantization đổi một trục số liên tục/dày sang một số mức rời rạc ít hơn. Càng ít bit thì càng tiết kiệm memory, nhưng lỗi xấp xỉ thường tăng.

## Dynamic quantization

Dynamic quantization thường quantize weight trước, còn activation có thể được quantize động khi inference. Đây là cách dễ thử cho inference vì không cần huấn luyện lại model đầy đủ.

Phù hợp khi:

- muốn giảm size/memory nhanh;
- muốn thử tăng tốc inference với ít thay đổi training pipeline;
- chấp nhận benchmark để xem quality có giảm không.

## Static quantization

Static quantization quantize weight và activation trước khi inference. Để làm được việc đó, thường cần calibration data: một tập input đại diện được chạy qua model để ước lượng range của activation.

Luồng trực giác:

```text
Model precision cao
-> Chạy calibration data
-> Ước lượng range của activation
-> Chọn scale/zero-point cho weight và activation
-> Export/chạy model quantized
```

Static quantization có thể nhanh hơn dynamic quantization vì nhiều quyết định quantization đã được cố định trước inference. Đổi lại, nó nhạy với chất lượng calibration data: nếu calibration không đại diện cho input thật, activation range bị ước lượng sai và quality có thể giảm.

## Quantization-aware training

Quantization-aware training mô phỏng hiệu ứng quantization trong lúc train/fine-tune để model học cách chịu lỗi xấp xỉ tốt hơn.

So với dynamic quantization:

- thường phức tạp hơn;
- cần training/fine-tuning;
- có thể giữ quality tốt hơn khi quantization gây nhiễu mạnh.

## Ba approach chính

| Approach | Cách làm | Khi nào hợp |
|---|---|---|
| Dynamic quantization | Quantize weight trước, activation xử lý động khi inference | Muốn thử nhanh, ít thay đổi training |
| Static quantization | Quantize weight và activation trước, cần calibration data | Muốn inference ổn định/nhanh hơn và có dữ liệu calibration đại diện |
| Quantization-aware training | Mô phỏng quantization trong lúc train/fine-tune | Khi quality drop của post-training quantization quá lớn |

Mental model:

```text
Dynamic -> dễ thử nhất
Static -> cần calibration, có thể tối ưu inference tốt hơn
QAT -> tốn training nhất, thường giữ quality tốt hơn
```

## Benchmarking quantized model

Sau khi quantize, phải đo lại model bằng cùng benchmark production đã dùng cho baseline.

```text
Baseline precision model
-> quality / latency / memory / size
Quantized model
-> quality / latency / memory / size
-> Đọc trade-off
```

Các câu hỏi cần trả lời:

- Quality giảm bao nhiêu so với model gốc?
- Latency trung bình và p95/p99 có thấp hơn thật không?
- Model size và memory footprint giảm bao nhiêu?
- Backend/hardware có tận dụng low-precision kernels không?
- Input benchmark có đại diện cho workload thật không?

Điểm quan trọng: model quantized nhỏ hơn không tự động nhanh hơn. Nếu runtime không hỗ trợ tốt INT8/low-bit computation, hoặc chi phí quantize/dequantize lớn, latency có thể cải thiện ít hoặc không cải thiện.

## Liên hệ với QLoRA

Trong [[QLoRA]], base model được quantize xuống 4-bit, còn phần task-specific được học bằng [[LoRA]]. Vì vậy quantization giảm chi phí giữ model gốc trong bộ nhớ, còn LoRA giảm số tham số cần train.

QLoRA nhấn mạnh ba điểm:

- NF4: kiểu dữ liệu 4-bit phù hợp với trọng số có phân phối gần chuẩn.
- Blockwise quantization: lượng tử hóa theo từng khối để giảm lỗi xấp xỉ do scale cục bộ.
- Double quantization: quantize tiếp scaling constants của các block để giảm overhead memory.

## Blockwise quantization

Thay vì dùng một scale chung cho toàn bộ ma trận, blockwise quantization chia weight thành nhiều block nhỏ. Mỗi block có scale riêng, nên các giá trị trong block được biểu diễn chính xác hơn.

Trade-off:

- Block nhỏ hơn: ít lỗi hơn nhưng nhiều scaling constants hơn.
- Block lớn hơn: ít metadata hơn nhưng dễ mất chi tiết hơn.

## Cần nhớ

- Quantization tiết kiệm memory nhưng có thể gây lỗi xấp xỉ.
- Chất lượng phụ thuộc format quantization, calibration và cách thực hiện compute.
- Với fine-tuning, cần cẩn thận vì training nhạy với nhiễu hơn inference.
- Tăng tốc chỉ chắc chắn khi runtime/hardware có kernels hỗ trợ kiểu số đã quantize.
- Luôn so sánh model gốc và model quantized bằng cùng benchmark production.

## Cách hiểu bằng lời của tôi

Quantization giống như đổi cách ghi số của model sang dạng ngắn hơn. Model vẫn làm cùng bài toán, nhưng weight/activation được lưu hoặc tính bằng ít bit hơn.

Điểm cần nhớ là "ít bit hơn" không tự động nghĩa là "tốt hơn". Nếu phần cứng không tận dụng được INT8/low-bit, tốc độ có thể không tăng nhiều. Nếu lỗi xấp xỉ quá lớn, quality giảm. Vì vậy quantization phải đi cùng benchmark.

## Câu hỏi review

1. Quantization khác distillation ở đâu?
2. Vì sao giảm số bit có thể giảm memory footprint?
3. Vì sao quantization có thể tăng tốc inference?
4. Dynamic quantization khác quantization-aware training ở đâu?
5. Vì sao model quantized phải benchmark lại?
6. Ba approach chính của quantization là gì?
7. Static quantization cần calibration data để làm gì?
8. Vì sao model quantized nhỏ hơn nhưng vẫn có thể không nhanh hơn?

## Liên kết

- [[QLoRA]]
- [[LoRA]]
- [[Transformer Inference Optimization]]
- [[Model Benchmarking]]
- [[ONNX Runtime]]
- [[Large Language Model]]
