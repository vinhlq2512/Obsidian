---
type: concept
status: developing
sources:
  - "[[NLP Transformers - Chapter 08 - Making Transformers Efficient in Production]]"
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

# Knowledge Distillation

## Định nghĩa

Knowledge distillation là kỹ thuật dùng một teacher model lớn để huấn luyện một student model nhỏ hơn, nhằm giữ lại nhiều năng lực dự đoán nhưng giảm chi phí inference.

Trong Chapter 08, đây là hướng "making models smaller": thay vì deploy teacher lớn, ta train một student nhỏ bắt chước hành vi dự đoán của teacher.

## Vấn đề giải quyết

Trong production, model Transformer lớn có thể quá chậm hoặc quá tốn memory. Distillation cố gắng chuyển hành vi hữu ích của model lớn sang model nhỏ hơn.

## Cơ chế

```text
Teacher model lớn
-> Sinh logits / soft targets cho dữ liệu
-> Student model nhỏ học từ hard labels và/hoặc soft targets
-> Benchmark student theo quality / latency / memory
-> Deploy student nếu trade-off chấp nhận được
```

## Soft labels và logits

Trong supervised training thường dùng hard label, ví dụ câu này thuộc class `positive`.

Teacher model cho thêm tín hiệu mềm hơn: phân phối xác suất trên tất cả class. Ví dụ:

```text
positive: 0.70
neutral: 0.25
negative: 0.05
```

Soft labels giàu thông tin hơn hard label vì chúng cho biết quan hệ giữa các class. Student không chỉ học đáp án đúng, mà còn học "teacher phân vân như thế nào".

## Temperature

Temperature làm mềm phân phối xác suất của teacher trước khi student học.

- Temperature thấp: phân phối sắc, class cao nhất áp đảo.
- Temperature cao: phân phối phẳng hơn, giúp lộ ra quan hệ giữa các class phụ.

Trực giác: nếu teacher quá tự tin, student chỉ thấy gần như hard labels. Nếu làm mềm vừa đủ, student học được thêm dark knowledge, tức các xác suất nhỏ nhưng có ý nghĩa ở những class không phải đáp án chính.

## Loss khi distillation

Student thường học bằng cách kết hợp hai mục tiêu:

```text
Hard-label loss: student khớp nhãn thật
Distillation loss: student khớp phân phối của teacher
```

Một cách hiểu gọn:

```text
total_loss = alpha * hard_label_loss + (1 - alpha) * distillation_loss
```

Trong đó `alpha` điều khiển mức tin vào nhãn thật so với tín hiệu teacher.

Distillation loss thường dùng [[KL Divergence]] để đo sự khác nhau giữa hai phân phối xác suất: phân phối của teacher và phân phối của student. Training giảm KL divergence để student bắt chước teacher tốt hơn.

## Knowledge Distillation for Fine-Tuning

Trong fine-tuning, distillation thường dùng một teacher đã mạnh trên task mục tiêu để hướng dẫn một student nhỏ hơn học cùng task.

Quy trình trực giác:

```text
Fine-tune teacher model lớn trên task
-> Teacher sinh logits / soft labels cho train set
-> Fine-tune student model nhỏ
-> Student học từ hard labels và soft labels của teacher
-> Benchmark student với teacher và baseline
```

Điểm khác với fine-tuning thường:

- Fine-tuning thường: student chỉ học từ nhãn thật.
- Distillation for fine-tuning: student học cả nhãn thật và phân phối dự đoán của teacher.

Soft labels giúp student thấy cấu trúc task tinh hơn. Ví dụ trong classification, teacher có thể cho biết class đúng là `A`, nhưng class `B` cũng gần đúng hơn class `C`. Tín hiệu này giúp student học decision boundary mềm hơn hard labels.

## Knowledge Distillation for Pretraining

Trong [[Pretraining]], distillation dùng teacher lớn để dạy student nhỏ ngay ở giai đoạn học biểu diễn ngôn ngữ tổng quát, trước khi student được fine-tune cho downstream task.

Điểm khác với fine-tuning distillation là dữ liệu không nhất thiết cần nhãn task. Teacher chạy trên corpus thô hoặc dữ liệu unlabeled, sinh logits/soft targets để student học phân phối ngôn ngữ tổng quát.

Quy trình trực giác:

```text
Teacher pretrained lớn
-> Chạy trên unlabeled corpus
-> Sinh logits cho masked token hoặc next token
-> Student pretrained bằng pretraining loss + distillation loss
-> Fine-tune / deploy student nhỏ hơn
```

Với encoder kiểu BERT, tín hiệu teacher thường nằm ở phân phối dự đoán cho các vị trí bị mask trong [[Masked Language Modeling]]. Với decoder/generative model, tín hiệu thường là phân phối next-token trong [[Autoregressive Language Model]].

Mục tiêu không chỉ là học một task cụ thể, mà là chuyển một phần "năng lực ngôn ngữ nền" của teacher sang student. Vì vậy pretraining distillation tạo ra một student checkpoint tổng quát, sau đó mới dùng tiếp cho fine-tuning, inference hoặc các pipeline production khác.

## Distillation Trainer

Trong thực hành với Hugging Face, có thể tạo một `DistillationTrainer` bằng cách kế thừa `Trainer` và override `compute_loss`.

Ý tưởng:

```text
Batch
-> Student forward pass
-> Teacher forward pass không tính gradient
-> Hard-label loss từ nhãn thật
-> Distillation loss từ teacher logits
-> Weighted sum thành loss cuối
```

Công thức:

```text
loss = alpha * hard_label_loss + (1 - alpha) * T^2 * KL(
  softmax(student_logits / T),
  softmax(teacher_logits / T)
)
```

Thành phần:

- `alpha`: mức ưu tiên nhãn thật so với teacher signal.
- `T`: temperature dùng để làm mềm phân phối logits.
- `hard_label_loss`: loss supervised bình thường, ví dụ cross entropy với nhãn thật.
- `KL(...)`: [[KL Divergence]] giữa phân phối dự đoán của student và teacher.
- `T^2`: hệ số scale thường dùng để giữ độ lớn gradient ổn định hơn khi dùng temperature.

Điểm triển khai cần nhớ:

- Student là model được train.
- Teacher nên đặt `eval()` và chạy trong `no_grad()`.
- Teacher không được cập nhật tham số.
- `compute_loss` là nơi thay objective, còn batching/evaluation/checkpointing vẫn để `Trainer` xử lý.
- Nếu teacher và student dùng cùng tokenizer/input format thì trainer đơn giản hơn nhiều.

### Hyperparameters trong distillation trainer

Distillation thêm các nguồn nhạy cảm mới vào training objective, nên không nên giữ nguyên toàn bộ default hyperparameters một cách máy móc.

Các giá trị thường cần chỉnh:

- `num_train_epochs`: số lần student đi qua dataset.
- `learning_rate`: tốc độ cập nhật student.
- `weight_decay`: regularization lên trọng số student.
- `alpha`: tỉ lệ hard-label loss so với distillation loss.
- `temperature`: độ mềm của teacher/student distribution trước khi tính KL.

Trực giác:

```text
learning_rate -> student đổi nhanh hay chậm
num_train_epochs -> student có bao nhiêu cơ hội học từ teacher
weight_decay -> student bị kéo về nghiệm gọn/ít overfit hơn
alpha -> nghe nhãn thật hay nghe teacher nhiều hơn
temperature -> teacher nói "mềm" đến mức nào
```

Nếu learning rate quá lớn, student pretrained có thể bị phá representation. Nếu quá nhỏ, student học teacher rất chậm. Nếu train quá lâu hoặc regularization yếu, student có thể overfit vào dữ liệu distillation hoặc lặp lại lỗi của teacher.

### Tìm hyperparameters bằng Optuna

Có thể dùng [[Hyperparameter Optimization|Optuna/hyperparameter search]] để tìm bộ tham số tốt cho distillation thay vì chọn thủ công.

Quy trình:

```text
Tạo objective function
-> Mỗi trial chọn learning_rate / weight_decay / epochs / alpha / temperature
-> Train student bằng DistillationTrainer
-> Evaluate trên validation set
-> Trả về metric
-> Chọn best_params
```

Optuna đặc biệt hữu ích khi các tham số tương tác với nhau. Ví dụ `temperature` cao có thể cần `alpha` khác; `learning_rate` phù hợp còn phụ thuộc student initialization và số epoch.

Cần nhớ: best trial chỉ tốt theo metric và validation setup đã chọn. Nếu mục tiêu là deploy, vẫn phải đo lại [[Model Benchmarking|latency, memory và quality]] trên điều kiện production.

## Benchmarking distilled model

Sau khi train xong student, phải benchmark distilled model trước khi coi distillation là thành công.

So sánh nên có:

```text
Teacher lớn
-> baseline quality / latency / memory

Student trước distillation
-> baseline student

Distilled student
-> quality sau khi học từ teacher
-> latency/memory sau khi nén
```

Distillation tốt khi student đạt trade-off hợp lý:

- quality giảm ít so với teacher;
- latency giảm rõ;
- memory/model size giảm rõ;
- student tốt hơn chính nó trước distillation;
- kết quả ổn định trên benchmark đại diện production.

Điểm cần tránh: chỉ nhìn accuracy/F1. Nếu distilled student nhỏ hơn nhưng runtime không nhanh hơn, hoặc memory không giảm đáng kể trong môi trường thật, thì distillation chưa chắc có giá trị production.

## Student Initialization

Student initialization là cách chọn điểm xuất phát cho student trước khi distillation.

Với Transformer, nên ưu tiên student bắt đầu từ một checkpoint đã [[Pretraining|pretrained]] thay vì random initialization, nếu nguồn học cho phép. Lý do là distillation thường nhằm chuyển hành vi của teacher sang một model nhỏ hơn, không nhằm dạy lại toàn bộ ngôn ngữ từ đầu.

Checklist khi chọn student:

- Student nhỏ hơn teacher đủ nhiều để có lợi latency/memory.
- Student vẫn đủ capacity để học task hoặc hành vi cần distill.
- Student có tokenizer/input format tương thích với dữ liệu.
- Student có output head/logit shape tương thích với teacher hoặc task.
- Student checkpoint pretrained gần domain càng tốt.

So sánh:

| Cách khởi tạo | Điểm mạnh | Rủi ro |
|---|---|---|
| Pretrained student | Học nhanh hơn, representation nền tốt hơn, distillation ổn định hơn | Có thể không đủ nhỏ hoặc không khớp domain |
| Random student | Tự do chọn kiến trúc rất nhỏ | Cần nhiều dữ liệu/training hơn, dễ học kém từ teacher |

Trực giác: teacher có thể dạy tốt hơn nếu student đã "biết đọc" ở mức cơ bản. Nếu student bắt đầu từ random weights, distillation phải vừa dạy ngôn ngữ nền vừa dạy task, nên khó hơn nhiều.

## Khi fine-tuning student

Cần kiểm soát:

- Teacher phải đủ tốt, nếu không student sẽ học sai.
- Student phải đủ capacity để bắt chước teacher.
- Student initialization nên tận dụng checkpoint pretrained nếu có thể.
- Nếu distill ở giai đoạn pretraining, corpus unlabeled phải đủ đại diện cho năng lực nền muốn giữ lại.
- Dataset distillation cần đại diện cho input production.
- Loss weight giữa hard labels và teacher signals không nên chọn mù; cần benchmark.
- Hyperparameters như `num_train_epochs`, `learning_rate` và `weight_decay` nên được xem là một phần của distillation setup, không chỉ là chi tiết phụ.
- Có thể dùng [[Hyperparameter Optimization]] với Optuna để search các tham số distillation thay vì thử tay.
- Sau khi train, phải so sánh student theo [[Model Benchmarking|quality, latency và memory]], không chỉ loss train.
- Benchmark nên so student với teacher và baseline student để biết distillation có thật sự tạo thêm giá trị.

## Khi áp dụng

Distillation hữu ích khi:

- Teacher đạt quality tốt nhưng inference quá chậm.
- Cần model nhỏ hơn cho production hoặc edge deployment.
- Có đủ dữ liệu hoặc unlabeled examples để teacher sinh soft labels.
- Chấp nhận train thêm student để đổi lấy latency/memory thấp hơn khi deploy.

## Trade-off

- Tăng tốc prediction nếu student nhỏ hơn đáng kể.
- Giảm memory footprint vì deploy model nhỏ hơn.
- Có thể mất accuracy nếu student không đủ capacity hoặc dữ liệu distillation không đại diện.
- Cần thêm chi phí training vì teacher phải chạy để tạo tín hiệu học cho student.
- Student có thể học cả lỗi/bias của teacher.

## Cách hiểu bằng lời của tôi

Distillation giống như dùng model lớn làm người hướng dẫn, rồi đưa model nhỏ đi làm production. Ta không bê nguyên model lớn vào hệ thống nếu mục tiêu là latency và cost.

Điểm hay là teacher không chỉ nói "đáp án đúng là gì", mà còn cho biết các đáp án khác gần đúng tới đâu. Phần phân vân đó giúp student học cấu trúc của task tốt hơn hard labels đơn thuần.

## Câu hỏi review

1. Teacher và student đóng vai trò gì trong knowledge distillation?
2. Vì sao soft labels có nhiều thông tin hơn hard labels?
3. Temperature ảnh hưởng gì đến phân phối xác suất của teacher?
4. KL divergence đo gì trong distillation loss?
5. Vì sao distillation phải được benchmark lại bằng latency, memory và accuracy?
6. Khi nào student nhỏ quá có thể làm distillation thất bại?
7. Knowledge distillation for fine-tuning khác fine-tuning thường ở đâu?
8. Vì sao teacher cần được fine-tune tốt trước khi dùng để dạy student?
9. Knowledge distillation for pretraining khác gì với distillation for fine-tuning?
10. Vì sao pretraining distillation có thể dùng unlabeled corpus?
11. `DistillationTrainer` cần thay đổi phần nào so với `Trainer` thông thường?
12. Vì sao teacher model nên chạy với `no_grad()`?
13. Vì sao student initialization ảnh hưởng mạnh đến chất lượng distillation?
14. Khi nào random initialization cho student là lựa chọn rủi ro?
15. `learning_rate`, `num_train_epochs` và `weight_decay` tác động gì đến student trong distillation?
16. Optuna tối ưu hyperparameters bằng cách lặp qua các trial như thế nào?
17. Vì sao metric chọn cho Optuna phải khớp mục tiêu production?
18. Benchmark distilled model cần đo những gì ngoài accuracy?
19. Vì sao cần so với baseline student chưa distill?

## Liên kết

- [[Transformer Inference Optimization]]
- [[Model Benchmarking]]
- [[Hyperparameter Optimization]]
- [[KL Divergence]]
- [[Loss Function]]
- [[Pretraining]]
- [[Masked Language Modeling]]
- [[Autoregressive Language Model]]
- [[Transformer]]
