---
type: reading-section
book: "[[Natural Language Processing with Transformers]]"
status: completed
chapter: 8
start_page: 234
end_page: 285
reading_date: 2026-08-04
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
- Creating a performance benchmark là bước nền trước khi tối ưu: nếu không có baseline latency/memory/accuracy ổn định, ta không biết kỹ thuật tối ưu có thật sự cải thiện production hay không.
- Distillation dùng teacher model lớn để huấn luyện student model nhỏ hơn.
- Chapter này giới thiệu bốn kỹ thuật bổ trợ để tăng tốc prediction và giảm memory footprint của Transformer: [[Knowledge Distillation]], [[Quantization]], [[Pruning]], và graph optimization bằng [[ONNX]] / [[ONNX Runtime]].
- [[Quantization]] và [[ONNX Runtime]] có thể tăng tốc inference mà không cần đổi bài toán.
- Không nên đánh giá tối ưu production chỉ bằng accuracy; cần đo latency, memory footprint và chất lượng sau mỗi kỹ thuật.

## Creating a Performance Benchmark

Performance benchmark trong chapter này nên được xem là baseline đo lường trước khi áp dụng distillation, quantization, pruning hoặc ONNX/ORT.

Một benchmark tốt cần cố định:

- dataset hoặc sample input đại diện;
- metric task chính, ví dụ accuracy/F1;
- runtime và hardware;
- batch size;
- số lần chạy;
- cách đo latency và memory.

Kết quả nên ghi lại ít nhất:

- accuracy hoặc metric task chính;
- average latency;
- p95/p99 latency;
- model size;
- memory footprint;
- throughput nếu hệ thống xử lý batch/request liên tục.

## Vì sao cần benchmark trước khi optimize

```text
Baseline model
-> Đo quality / latency / memory
-> Áp dụng một kỹ thuật tối ưu
-> Đo lại cùng điều kiện
-> Chỉ giữ thay đổi nếu trade-off chấp nhận được
```

Nếu không giữ cùng điều kiện benchmark, ta có thể nhầm một thay đổi runtime hoặc input distribution thành cải thiện thật của model.

## Bốn hướng tối ưu model

| Kỹ thuật | Mục tiêu chính | Cách hiểu nhanh |
|---|---|---|
| [[Knowledge Distillation]] | Giảm kích thước model triển khai | Dùng teacher lớn để train student nhỏ |
| [[Quantization]] | Giảm chi phí biểu diễn số học | Dùng ít bit hơn cho weight/activation |
| [[Pruning]] | Loại bỏ phần ít quan trọng | Cắt bớt weight/head/neuron/block nếu ít ảnh hưởng |
| [[ONNX]] + [[ONNX Runtime]] | Tối ưu graph inference | Export model thành graph chuẩn và chạy bằng runtime tối ưu |

## Making Models Smaller via Knowledge Distillation

Knowledge distillation dùng một teacher model lớn để truyền hành vi dự đoán sang một student model nhỏ hơn. Mục tiêu không phải làm teacher nhanh hơn, mà là train student đủ tốt để deploy thay teacher.

Cơ chế học:

```text
Teacher model lớn
-> Tạo logits / soft labels
-> Student model nhỏ học bắt chước phân phối của teacher
-> So sánh student với teacher bằng benchmark cố định
-> Deploy student nếu latency/memory giảm và quality còn chấp nhận được
```

Điểm cần nắm:

- Hard labels chỉ nói class đúng.
- Soft labels/logits cho biết teacher phân bổ niềm tin ra sao giữa các class.
- Temperature có thể làm mềm phân phối để student học được quan hệ giữa các class.
- [[KL Divergence]] đo độ khác nhau giữa phân phối xác suất của teacher và student, nên thường được dùng làm distillation loss.
- Distillation vẫn là trade-off: student nhỏ hơn thường nhanh hơn/gọn hơn, nhưng có thể mất accuracy hoặc học lỗi của teacher.

## Knowledge Distillation for Fine-Tuning

Trong fine-tuning, distillation dùng teacher đã học tốt task mục tiêu để hướng dẫn student nhỏ hơn. Student không chỉ học hard labels của dataset, mà còn học logits/soft labels do teacher sinh ra.

```text
Teacher fine-tuned tốt
-> Sinh soft labels cho dữ liệu task
-> Student fine-tune bằng hard labels + distillation loss như KL divergence
-> Benchmark student so với teacher
```

Ý chính: distillation for fine-tuning biến teacher thành nguồn tín hiệu phụ trong quá trình student học task. Nếu thành công, student giữ được phần lớn task performance nhưng có latency/memory thấp hơn.

## Knowledge Distillation for Pretraining

Knowledge distillation cũng có thể áp dụng ở giai đoạn [[Pretraining]], không chỉ ở giai đoạn fine-tuning cho task cụ thể.

Trong pretraining distillation, teacher thường là model pretrained lớn. Student nhỏ hơn được huấn luyện trên corpus thô/unlabeled và học từ logits hoặc soft targets của teacher. Tín hiệu này có thể đi cùng pretraining objective gốc như [[Masked Language Modeling]] hoặc next-token prediction trong [[Autoregressive Language Model]].

```text
Teacher pretrained lớn
-> Unlabeled text corpus
-> Teacher logits / soft targets
-> Student học pretraining objective + distillation loss
-> Student checkpoint nhỏ hơn để fine-tune downstream
```

Điểm quan trọng: fine-tuning distillation truyền năng lực của teacher trên một task đã biết, còn pretraining distillation cố truyền năng lực biểu diễn/ngôn ngữ tổng quát. Vì vậy kết quả của pretraining distillation thường là một base model nhỏ hơn, chưa gắn chặt với một task duy nhất.

Trade-off:

- Có thể tạo student nhỏ hơn ngay từ nền pretrained.
- Có thể tận dụng unlabeled data vì teacher tự sinh soft targets.
- Tốn chi phí chạy teacher trên corpus lớn.
- Student vẫn có thể học bias/lỗi của teacher nếu corpus hoặc teacher không tốt.

## Creating a Knowledge Distillation Trainer

Trong Hugging Face, cách triển khai distillation gọn là tạo một trainer riêng kế thừa từ `Trainer`. Ý chính không phải viết lại toàn bộ training loop, mà chỉ thay phần tính loss để student học thêm từ teacher.

Luồng triển khai:

```text
Base Trainer
-> Thêm teacher_model
-> Trong compute_loss:
   -> chạy student trên batch
   -> chạy teacher không tính gradient
   -> lấy student_logits và teacher_logits
   -> làm mềm logits bằng temperature
   -> tính distillation loss bằng KL divergence
   -> trộn với hard-label loss
-> train student như Trainer bình thường
```

Vai trò của từng thành phần:

- `student_model`: model nhỏ được cập nhật gradient.
- `teacher_model`: model lớn đã train/fine-tune tốt, đặt ở chế độ eval và không cập nhật gradient.
- `temperature`: làm mềm phân phối logits để student học được quan hệ giữa các class.
- `alpha`: điều khiển tỉ lệ giữa loss từ nhãn thật và loss bắt chước teacher.
- `compute_loss`: điểm mở rộng quan trọng vì distillation khác fine-tuning thường chủ yếu ở objective.

Công thức trực giác:

```text
loss = alpha * hard_label_loss + (1 - alpha) * distillation_loss
```

Trong đó `distillation_loss` thường dùng [[KL Divergence]] giữa:

```text
softmax(student_logits / T)
softmax(teacher_logits / T)
```

`T` là temperature. Khi `T` cao hơn, phân phối bớt sắc, giúp student thấy thêm các class mà teacher cho là gần đúng. Trong triển khai thực tế, distillation loss thường được scale theo `T^2` để giữ cỡ gradient ổn định hơn khi đổi temperature.

Điểm cần cẩn thận:

- Teacher phải chạy trong `torch.no_grad()` để không tốn memory cho gradient.
- Teacher nên được đưa về cùng device với student.
- Teacher cần ở `eval()` để dropout/layer behavior ổn định.
- Batch input cho teacher và student phải tương thích.
- Sau khi train, vẫn cần benchmark lại student theo [[Model Benchmarking|quality, latency và memory]], vì loss thấp không đảm bảo production trade-off tốt.

### Tinh chỉnh hyperparameters mặc định

Khi tạo `DistillationTrainer`, sách cũng chỉnh một vài giá trị mặc định như số epoch, weight decay và learning rate. Đây là tín hiệu quan trọng: distillation không nên dùng máy móc cùng setup với fine-tuning thường.

Các hyperparameter cần để ý:

- `num_train_epochs`: student có thể cần đủ epoch để hấp thụ soft targets từ teacher, nhưng quá nhiều epoch có thể overfit vào teacher/dataset.
- `learning_rate`: nếu quá cao, student dễ làm hỏng representation pretrained; nếu quá thấp, student học tín hiệu teacher chậm.
- `weight_decay`: regularization giúp student không bám quá sát noise của dataset hoặc lỗi của teacher.
- `alpha`: quyết định student nghe hard labels hay teacher logits nhiều hơn.
- `temperature`: quyết định mức mềm của phân phối teacher.

Mental model:

```text
TrainingArguments mặc định
-> Chỉnh epochs / learning_rate / weight_decay
-> Thêm alpha / temperature cho distillation
-> Train student
-> Đo lại quality / latency / memory
```

Không có bộ hyperparameter đúng tuyệt đối. Với distillation, cần xem chúng như một phần của benchmark: thay đổi setup training thì phải đo lại student trên cùng evaluation set và cùng điều kiện production.

### Finding Good Hyperparameters with Optuna

Optuna được dùng để tự động tìm bộ hyperparameters tốt hơn thay vì thử tay từng giá trị. Trong distillation, search space thường xoay quanh các tham số vừa ảnh hưởng quality vừa ảnh hưởng training stability.

Luồng tổng quát:

```text
Định nghĩa objective(trial)
-> trial đề xuất hyperparameters
-> train/evaluate student với bộ tham số đó
-> trả về metric cần tối ưu
-> Optuna chọn trial tiếp theo
-> lấy best_trial / best_params
```

Các hyperparameters có thể đưa vào search:

- `learning_rate`: thường search theo log scale vì độ lớn quan trọng hơn sai khác tuyến tính.
- `num_train_epochs`: kiểm soát student học bao lâu từ teacher.
- `weight_decay`: regularization để giảm overfit.
- `alpha`: cân bằng hard labels và teacher logits.
- `temperature`: độ mềm của teacher distribution.

Điểm cần nắm: Optuna không thay thế benchmark. Nó chỉ giúp chọn candidate tốt hơn trong không gian thử nghiệm. Sau khi có `best_params`, vẫn phải train/evaluate lại student theo cùng [[Model Benchmarking|benchmark quality, latency và memory]] trước khi coi là lựa chọn production.

Rủi ro:

- Search space quá rộng làm tốn compute.
- Chọn metric sai sẽ tối ưu sai mục tiêu production.
- Nếu validation set nhỏ hoặc lệch distribution, `best_params` có thể chỉ là overfit vào validation.
- Mỗi trial distillation phải chạy teacher/student nên chi phí cao hơn fine-tuning thường.

## Benchmarking Our Distilled Model

Sau khi train student bằng distillation và chọn hyperparameters tốt, bước bắt buộc là benchmark distilled model. Đây là lúc kiểm tra xem student có thật sự đạt mục tiêu production hay chỉ có validation metric đẹp.

Benchmark distilled model cần so sánh ít nhất ba điểm:

```text
Teacher model lớn
vs baseline student / pretrained student
vs distilled student
```

Các chỉ số cần ghi:

- quality metric của task, ví dụ accuracy/F1;
- latency trung bình;
- p95/p99 latency nếu quan tâm request production;
- model size;
- memory footprint;
- throughput nếu chạy batch hoặc server.

Mental model:

```text
Train distilled student
-> Load best checkpoint
-> Chạy cùng benchmark với teacher/baseline
-> So sánh quality drop
-> So sánh latency/memory gain
-> Quyết định có deploy student không
```

Điểm quan trọng là quality không cần luôn bằng teacher tuyệt đối. Distillation thành công khi student giữ được quality đủ tốt trong khi latency hoặc memory giảm đủ nhiều cho mục tiêu triển khai.

Khi đọc kết quả, nên hỏi:

- Student mất bao nhiêu quality so với teacher?
- Student nhanh hơn bao nhiêu lần?
- Memory/model size giảm bao nhiêu?
- Trade-off này có phù hợp SLA hoặc ràng buộc phần cứng không?
- Distilled student có tốt hơn student chưa distill không?

## Making Models Faster with Quantization

[[Quantization]] làm model nhanh hơn và gọn hơn bằng cách biểu diễn weight/activation với ít bit hơn. Thay vì giữ toàn bộ phép tính ở FP32/FP16, một phần model có thể dùng kiểu số rẻ hơn như INT8.

Trực giác:

```text
Weight/activation precision cao
-> Ánh xạ sang miền số bit thấp hơn
-> Tính toán/đọc bộ nhớ rẻ hơn
-> Giảm model size và memory bandwidth
-> Có thể giảm latency nếu hardware/runtime hỗ trợ tốt
```

Vì Transformer inference thường bị ảnh hưởng bởi chi phí đọc weight và nhân ma trận lớn, biểu diễn số học nhỏ hơn có thể giúp:

- giảm model size trên disk;
- giảm RAM/VRAM khi load model;
- giảm memory bandwidth;
- tăng tốc inference trên backend hỗ trợ INT8 hoặc low-precision kernels.

Có hai nguồn lợi chính:

```text
Ít bit hơn mỗi weight
-> Ít byte hơn phải đọc từ memory
-> Cache/memory bandwidth hiệu quả hơn

Kiểu số thấp hơn như INT8
-> Có thể dùng kernel nhân ma trận tối ưu
-> Nhiều phép tính hơn trên cùng phần cứng
```

Với Transformer, lợi ích memory bandwidth rất quan trọng vì nhiều lớp chủ yếu là phép nhân ma trận lớn. Nếu weight nhỏ hơn, runtime có thể đọc dữ liệu nhanh hơn và giữ được nhiều tham số hơn trong cache.

Nhưng quantization không miễn phí. Nó đưa lỗi xấp xỉ vào weight/activation, nên luôn cần benchmark lại quality. Nếu model nhỏ hơn nhưng accuracy/F1 giảm quá nhiều, hoặc runtime không thật sự nhanh hơn trên hardware mục tiêu, quantization chưa chắc đáng dùng.

Điểm cần nhớ:

- Quantization chủ yếu đổi cách biểu diễn số học, không nhất thiết đổi architecture.
- Lợi ích tốc độ phụ thuộc runtime/hardware, không chỉ phụ thuộc số bit.
- Cần đo lại [[Model Benchmarking|quality, latency và memory]] sau khi quantize.
- Có thể kết hợp quantization với [[Knowledge Distillation]], [[Pruning]] hoặc [[ONNX Runtime]].
- Overhead quantize/dequantize có thể ăn mất lợi ích tốc độ nếu backend không tối ưu tốt.
- CPU thường là nơi dynamic quantization dễ thấy lợi ích ban đầu; GPU cần đúng kernel/backend hỗ trợ low precision.

### Ba approach chính của quantization

Thường có ba hướng chính:

| Approach | Ý tưởng | Trade-off |
|---|---|---|
| Dynamic quantization | Quantize weight trước, activation xử lý động khi inference | Dễ thử, ít thay đổi pipeline, nhưng chưa tối ưu hết |
| Static quantization | Quantize cả weight và activation trước inference, cần calibration data | Có thể nhanh/ổn định hơn, nhưng phụ thuộc dữ liệu calibration |
| Quantization-aware training | Mô phỏng quantization trong lúc train/fine-tune | Phức tạp và tốn training hơn, nhưng có thể giữ quality tốt hơn |

Điểm phân biệt nhanh:

```text
Dynamic: quyết định một phần lúc inference
Static: chuẩn bị quantization trước bằng calibration
QAT: cho model học với nhiễu quantization trong training
```

Nếu muốn thử nhanh, dynamic quantization là lựa chọn dễ bắt đầu. Nếu có calibration data tốt và backend hỗ trợ, static quantization có thể phù hợp hơn cho inference production. Nếu post-training quantization làm quality giảm quá nhiều, quantization-aware training là hướng mạnh hơn nhưng đắt hơn.

Quy tắc chọn nhanh:

- dùng dynamic quantization khi muốn thử inference nhanh/gọn với ít thay đổi;
- dùng static quantization khi có calibration data đại diện và muốn quantize activation ổn định hơn;
- dùng QAT khi post-training quantization làm quality giảm quá nhiều nhưng vẫn cần lợi ích low precision.

## Benchmarking Our Quantized Model

Sau khi quantize, bước quan trọng là benchmark quantized model so với model gốc. Mục tiêu không chỉ là xác nhận model nhỏ hơn, mà là kiểm tra toàn bộ trade-off production.

So sánh tối thiểu:

```text
Original model
-> Benchmark quality / latency / memory
Quantized model
-> Benchmark cùng input, cùng hardware, cùng runtime nếu có thể
-> So sánh quality drop với latency/memory gain
```

Các chỉ số cần đọc cùng nhau:

- quality metric của task, ví dụ accuracy/F1;
- model size trên disk;
- memory footprint khi load/chạy inference;
- average latency;
- p95/p99 latency;
- throughput nếu chạy batch hoặc service.

Điểm dễ nhầm: quantized model nhỏ hơn không đảm bảo luôn nhanh hơn. Nếu backend không tận dụng tốt INT8/low-precision kernels, hoặc overhead quantize/dequantize lớn, latency có thể không cải thiện như kỳ vọng. Vì vậy kết quả phải được đo trên runtime và hardware mục tiêu.

Một quantized model đáng dùng khi:

- quality giảm trong ngưỡng chấp nhận được;
- latency hoặc memory cải thiện đủ rõ;
- kết quả ổn định trên input đại diện;
- deployment stack thật sự hỗ trợ format/operation đã quantize.

## Optimizing Inference with ONNX and the ONNX Runtime

[[ONNX]] là định dạng graph trung gian, còn [[ONNX Runtime]] là engine chạy graph đó. Trong chapter này, ONNX/ORT được dùng như một hướng tối ưu inference mà không nhất thiết thay đổi kiến trúc hoặc retrain model.

Luồng triển khai:

```text
Model trong PyTorch / Transformers
-> Export sang ONNX graph
-> Kiểm tra output parity với model gốc
-> Chạy graph bằng ONNX Runtime
-> Benchmark latency / memory / quality
```

ORT có thể tăng tốc bằng [[Graph Optimization|graph optimization]] và runtime optimization:

- hợp nhất các operator thường đi cùng nhau;
- bỏ node hoặc computation không cần thiết;
- tối ưu constant trong graph;
- chọn execution provider phù hợp với CPU/GPU/hardware backend;
- giảm overhead của framework training khi chỉ cần inference.

Điều phải kiểm tra sau export:

- output của ONNX model có gần output của model gốc không;
- dynamic axes có đúng cho batch size và sequence length khác nhau không;
- opset/runtime có hỗ trợ đầy đủ operation cần dùng không;
- latency/memory có cải thiện trên workload thật không.

Mental model:

```text
Training framework tối ưu cho training
Production runtime tối ưu cho inference
ONNX là cầu nối graph
ORT là engine chạy graph đó nhanh/gọn hơn
```

## Making Models Sparser with Weight Pruning

[[Pruning]] làm model sparse hơn bằng cách loại bỏ phần được xem là ít quan trọng. Với weight pruning, đơn vị bị loại thường là từng trọng số riêng lẻ hoặc một cấu trúc lớn hơn trong model.

Cách làm phổ biến nhất là magnitude pruning:

```text
Weight matrix
-> Tính độ quan trọng theo |weight|
-> Chọn một tỉ lệ sparsity mục tiêu
-> Đưa các weight nhỏ nhất về 0
-> Fine-tune hoặc evaluate lại
-> Benchmark quality / latency / memory
```

Hai kiểu pruning cần phân biệt:

| Kiểu pruning | Cắt cái gì | Trade-off |
|---|---|---|
| Unstructured pruning | Từng weight riêng lẻ | Dễ tạo sparsity cao, nhưng chưa chắc tăng tốc nếu runtime không tối ưu sparse matrix |
| Structured pruning | Cả neuron, attention head, channel, block hoặc layer | Dễ chuyển thành speedup thật hơn, nhưng rủi ro giảm quality mạnh hơn |

Sparsity là tỉ lệ weight bằng 0:

```text
sparsity = số weight bằng 0 / tổng số weight
```

Điểm production quan trọng: pruning chỉ có ý nghĩa nếu sparsity được runtime/hardware khai thác. Nếu model chỉ có thêm nhiều số 0 nhưng vẫn chạy bằng dense kernels, latency có thể gần như không đổi.

Trade-off:

- pruning nhẹ có thể giảm redundancy với quality drop nhỏ;
- pruning mạnh có thể làm model mất năng lực biểu diễn;
- thường cần fine-tune sau pruning để phục hồi chất lượng;
- structured pruning thường hữu ích hơn cho speed thực tế;
- phải benchmark lại vì giảm tham số không đồng nghĩa giảm latency.

## Choosing a Good Student Initialization

Student initialization là quyết định chọn student model bắt đầu từ đâu trước khi distillation. Với Transformer, khởi tạo student từ một checkpoint pretrained nhỏ thường tốt hơn nhiều so với khởi tạo random.

Lý do:

- Distillation dataset thường không đủ lớn để dạy lại toàn bộ ngôn ngữ từ đầu.
- Pretrained student đã có representation nền, nên teacher chỉ cần "uốn" student theo task hoặc hành vi mong muốn.
- Training ổn định hơn vì student không bắt đầu từ phân phối logits hỗn loạn.
- Nếu student và teacher dùng tokenizer/input format tương thích, việc so khớp logits và chạy pipeline đơn giản hơn.

Luồng quyết định:

```text
Mục tiêu production
-> Chọn student architecture nhỏ hơn teacher
-> Ưu tiên checkpoint đã pretrained
-> Kiểm tra tokenizer / label space / output shape
-> Distill bằng teacher logits
-> Benchmark quality / latency / memory
```

Một student tốt không chỉ là model nhỏ. Nó cần đủ capacity để học task từ teacher, tương thích với dữ liệu đầu vào, và tạo được output cùng không gian nhãn với teacher. Nếu student quá yếu, distillation loss có thể giảm nhưng quality thực tế vẫn thấp.

Khi chọn student, cần kiểm tra:

- Student có cùng task head hoặc có thể thêm task head phù hợp không?
- Student có dùng tokenizer giống teacher hoặc ít nhất tương thích với dữ liệu không?
- Output logits có cùng số class/vocabulary dimension với teacher không?
- Student có đủ nhỏ để thật sự giảm latency/memory không?
- Student có checkpoint pretrained phù hợp domain không?

Ý chính: student initialization tốt làm distillation giống "chuyển giao hành vi" hơn là "huấn luyện model nhỏ từ con số không".

## Viết lại bằng lời của tôi

Chapter 08 không chỉ nói "làm model nhanh hơn", mà tách vấn đề production thành nhiều đòn bẩy khác nhau. Ta có thể làm model nhỏ hơn bằng distillation, làm phép tính rẻ hơn bằng quantization, cắt phần dư thừa bằng pruning, hoặc giữ model gần như cũ nhưng chạy bằng graph/runtime tối ưu hơn với ONNX và ORT.

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

Ghi chú: demo này đo latency mức tối thiểu. Khi làm benchmark nghiêm túc hơn, nên thêm warmup, đo memory, ghi hardware/runtime và đo metric task trên tập đánh giá cố định.

## Khái niệm quan trọng

- [[Model Benchmarking]]
- [[Transformer Inference Optimization]]
- [[Knowledge Distillation]]
- [[Hyperparameter Optimization]]
- [[KL Divergence]]
- [[Pretraining]]
- [[Quantization]]
- [[ONNX]]
- [[ONNX Runtime]]
- [[Pruning]]

## Active Recall

1. Vì sao accuracy cao chưa đủ cho production?
2. Teacher-student distillation hoạt động như thế nào?
3. Quantization đánh đổi điều gì?
4. Benchmark nên đo những chỉ số nào?
5. Bốn kỹ thuật trong chapter khác nhau ở chỗ tác động vào đâu?
6. Vì sao phải benchmark baseline trước khi dùng ONNX hoặc quantization?
7. Soft labels giúp student học được gì mà hard labels không thể hiện rõ?
8. Knowledge distillation for fine-tuning dùng teacher như thế nào?
9. KL divergence đo gì giữa teacher và student?
10. Knowledge distillation for pretraining khác fine-tuning distillation ở đâu?
11. Vì sao pretraining distillation có thể học từ unlabeled text?
12. Vì sao `DistillationTrainer` thường override `compute_loss` thay vì viết lại toàn bộ training loop?
13. `alpha` và `temperature` ảnh hưởng gì đến quá trình student học từ teacher?
14. Vì sao student nên khởi tạo từ checkpoint pretrained thay vì random?
15. Khi chọn student, cần kiểm tra những điểm tương thích nào với teacher?
16. Vì sao distillation cần chỉnh lại `num_train_epochs`, `learning_rate` và `weight_decay` thay vì giữ nguyên mặc định?
17. Optuna giúp gì trong việc tìm hyperparameters cho distillation trainer?
18. Vì sao best hyperparameters từ Optuna vẫn cần benchmark lại trước khi dùng production?
19. Khi benchmark distilled model, cần so sánh student với những baseline nào?
20. Vì sao distilled student có thể đáng deploy dù accuracy thấp hơn teacher một chút?
21. Quantization làm model nhanh hơn bằng cơ chế nào?
22. Vì sao model quantized vẫn phải benchmark lại trên hardware/runtime mục tiêu?
23. Ba approach chính của quantization khác nhau ở đâu?
24. Vì sao static quantization cần calibration data?
25. Khi benchmark quantized model, cần so với baseline nào?
26. Vì sao model quantized nhỏ hơn nhưng latency chưa chắc thấp hơn?
27. ONNX và ONNX Runtime khác nhau ở đâu?
28. Vì sao phải kiểm tra output parity sau khi export ONNX?
29. Weight pruning làm model sparse bằng cách nào?
30. Unstructured pruning và structured pruning khác nhau thế nào?
31. Vì sao sparse model không tự động nhanh hơn?
32. Sau pruning, vì sao thường cần fine-tune hoặc benchmark lại?

## Gợi ý trả lời Active Recall

1. Accuracy cao chưa đủ vì production còn bị ràng buộc bởi latency, throughput, memory, model size, chi phí và độ ổn định.
2. Teacher-student distillation dùng teacher lớn sinh logits/soft labels, rồi train student nhỏ học theo hard labels và/hoặc phân phối dự đoán của teacher.
3. Quantization đánh đổi precision số học lấy memory thấp hơn và inference có thể nhanh hơn; rủi ro là lỗi xấp xỉ làm giảm quality.
4. Benchmark nên đo quality metric, average latency, p95/p99 latency, throughput, model size, memory footprint, batch size, runtime và hardware.
5. Distillation làm model nhỏ hơn; quantization làm biểu diễn số học rẻ hơn; pruning cắt phần ít quan trọng; ONNX/ORT tối ưu graph/runtime inference.
6. Cần baseline vì nếu không có số đo ban đầu, ta không biết ONNX hoặc quantization thật sự cải thiện hay chỉ làm đổi điều kiện chạy.
7. Soft labels cho student biết teacher phân bổ niềm tin giữa các class ra sao, gồm cả các class gần đúng mà hard label không thể hiện.
8. Trong fine-tuning, teacher đã mạnh trên task sinh logits/soft labels để student học task với tín hiệu giàu hơn nhãn thật.
9. KL divergence đo độ khác nhau giữa phân phối xác suất của teacher và student.
10. Fine-tuning distillation truyền năng lực trên task cụ thể; pretraining distillation truyền năng lực ngôn ngữ/biểu diễn tổng quát trên corpus chưa gán nhãn.
11. Pretraining distillation dùng unlabeled text vì teacher tự sinh soft targets/logits, còn pretraining objective cũng có thể tự tạo tín hiệu học từ dữ liệu.
12. `DistillationTrainer` override `compute_loss` vì khác biệt chính nằm ở objective, còn batching, evaluation, logging và checkpointing vẫn dùng được từ `Trainer`.
13. `alpha` quyết định student nghe hard labels hay teacher nhiều hơn; `temperature` làm mềm logits để student học quan hệ giữa các class.
14. Student pretrained đã có representation nền, nên distillation chỉ cần chuyển hành vi/task signal thay vì dạy model từ random weights.
15. Cần kiểm tra tokenizer/input format, task head, output logit shape, label space/vocabulary, capacity và mục tiêu latency/memory.
16. Distillation có objective khác fine-tuning thường, nên epochs, learning rate và weight decay cần chỉnh để student học teacher ổn định mà không overfit.
17. Optuna tự chạy nhiều trial, mỗi trial chọn một bộ hyperparameters rồi evaluate student để tìm cấu hình tốt hơn.
18. Best params từ Optuna chỉ tốt theo validation metric đã chọn; production vẫn cần benchmark lại quality, latency và memory.
19. Nên so distilled student với teacher lớn và baseline student chưa distill/pretrained student.
20. Distilled student đáng deploy nếu quality giảm ít nhưng latency hoặc memory cải thiện đủ nhiều cho ràng buộc production.
21. Quantization làm model nhanh/gọn hơn bằng cách biểu diễn weight/activation với ít bit hơn, giảm model size, memory bandwidth và có thể dùng low-precision kernels.
22. Model quantized phải benchmark trên runtime/hardware mục tiêu vì lợi ích tốc độ phụ thuộc backend và quality có thể giảm do lỗi xấp xỉ.
23. Dynamic quantization dễ thử nhất và xử lý activation động; static quantization cần calibration để cố định weight/activation trước inference; QAT mô phỏng quantization trong training để giữ quality tốt hơn.
24. Static quantization cần calibration data để ước lượng activation range, từ đó chọn scale/zero-point đại diện cho input thật.
25. Cần so quantized model với original/baseline model bằng cùng input, cùng metric, cùng hardware/runtime để đọc quality drop và latency/memory gain.
26. Vì tốc độ phụ thuộc runtime, hardware, batch size và kernel low-precision; nếu backend không tận dụng được INT8 hoặc overhead dequantize lớn, model nhỏ hơn vẫn có thể không nhanh hơn.
27. ONNX là định dạng graph trung gian của model; ONNX Runtime là engine thực thi graph đó và áp dụng tối ưu inference.
28. Vì quá trình export/optimize có thể gây sai khác số học, lỗi dynamic axis hoặc unsupported ops; cần đảm bảo output vẫn gần model gốc trước khi tin benchmark.
29. Weight pruning chọn các weight được xem là ít quan trọng, thường theo trị tuyệt đối nhỏ, rồi đưa chúng về 0 hoặc loại bỏ khỏi model.
30. Unstructured pruning cắt từng weight riêng lẻ; structured pruning cắt cả cấu trúc như neuron/head/block, thường dễ tạo speedup thật hơn nhưng rủi ro quality cao hơn.
31. Sparse model không tự động nhanh hơn vì nếu runtime vẫn dùng dense kernels, các số 0 vẫn bị xử lý gần như weight bình thường.
32. Sau pruning cần fine-tune để phục hồi chất lượng hoặc benchmark lại để xem sparsity có thật sự đổi thành quality/latency/memory trade-off tốt không.

## Checklist

- [x] Đọc xong chapter
- [ ] Chạy demo benchmark
- [ ] Ghi lại latency trung bình
- [x] Tách concept cần dùng lại
- [x] Cập nhật tiến độ sách cho ngày 03-08
- [x] Cập nhật tiến độ sách cho ngày 04-08
