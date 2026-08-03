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
  - machine-learning
  - optimization
  - training
---

# Hyperparameter Optimization

## Định nghĩa

Hyperparameter optimization là quá trình tìm bộ hyperparameters tốt cho training hoặc inference bằng cách chạy nhiều thử nghiệm có kiểm soát và chọn cấu hình đạt metric tốt nhất.

Hyperparameters là các giá trị không được học trực tiếp bằng gradient, ví dụ `learning_rate`, `weight_decay`, `num_train_epochs`, batch size, hoặc trong [[Knowledge Distillation]] là `alpha` và `temperature`.

## Vấn đề giải quyết

Chọn hyperparameters bằng tay dễ bỏ sót tương tác giữa các tham số. Một giá trị `learning_rate` tốt có thể phụ thuộc vào số epoch, weight decay, student initialization, hoặc temperature.

Hyperparameter optimization biến việc thử nghiệm thành một quy trình rõ ràng:

```text
Search space
-> Trial
-> Train / evaluate
-> Metric
-> Chọn trial tiếp theo
-> Best params
```

## Optuna

Optuna là một công cụ để chạy hyperparameter search. Người dùng định nghĩa một `objective(trial)`, trong đó `trial` đề xuất các giá trị hyperparameters. Sau mỗi trial, objective trả về metric cần tối ưu.

Trong distillation trainer, một trial có thể chọn:

- `learning_rate`;
- `weight_decay`;
- `num_train_epochs`;
- `alpha`;
- `temperature`.

Sau đó model student được train/evaluate, và Optuna ghi lại metric để tìm cấu hình tốt hơn.

## Khi dùng cho knowledge distillation

Với [[Knowledge Distillation]], hyperparameter search hữu ích vì objective có nhiều nguồn tín hiệu:

- hard labels từ dataset;
- soft labels/logits từ teacher;
- temperature làm mềm phân phối;
- student initialization;
- regularization và số epoch.

Một search setup hợp lý cần:

- validation set đại diện;
- metric rõ ràng;
- search space không quá rộng;
- giới hạn số trials theo compute budget;
- benchmark lại best model bằng [[Model Benchmarking]].

## Trade-off

- Tốt hơn thử tay nếu nhiều tham số tương tác.
- Tốn compute vì mỗi trial có thể cần train/evaluate model.
- Dễ tối ưu nhầm nếu metric không phản ánh mục tiêu thật.
- Có thể overfit validation set nếu chạy quá nhiều trial trên tập nhỏ.

## Cách hiểu bằng lời của tôi

Hyperparameter optimization là cách để máy phụ mình chọn núm chỉnh training. Thay vì tự đoán learning rate hay weight decay, mình định nghĩa khoảng giá trị hợp lý, cho Optuna thử nhiều cấu hình, rồi dùng validation metric để chọn candidate tốt.

Nhưng kết quả tốt nhất trong Optuna chưa tự động là tốt nhất cho production. Nếu production quan tâm latency, memory và quality cùng lúc, thì best params phải được đưa lại vào benchmark đầy đủ.

## Câu hỏi review

1. Hyperparameters khác learned parameters ở đâu?
2. Optuna dùng `trial` và `objective` như thế nào?
3. Vì sao hyperparameter search hữu ích trong knowledge distillation?
4. Rủi ro khi search space quá rộng là gì?
5. Vì sao best trial vẫn cần benchmark lại trước khi deploy?

## Liên kết

- [[Knowledge Distillation]]
- [[Model Benchmarking]]
- [[Loss Function]]
