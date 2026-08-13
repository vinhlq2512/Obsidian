---
type: concept
status: developing
sources:
  - "[[Adaptive Prompting for Continual Relation Extraction]]"
  - "[[WAVE++ - Capturing Within-Task Variance for Continual Relation Extraction]]"
  - "[[20 - Research/Papers/Consistent Prototype Learning for Few-Shot Continual Relation Extraction]]"
  - "[[20 - Research/Papers/Making Pre-trained Language Models Better Continual Few-Shot Relation Extractors]]"
source_sections:
  - "[[Adaptive Prompting for Continual Relation Extraction#Research gap]]"
  - "[[WAVE++ - Capturing Within-Task Variance for Continual Relation Extraction#Hạn chế và giả định]]"
  - "[[20 - Research/Papers/Consistent Prototype Learning for Few-Shot Continual Relation Extraction#Prototype distortion và forgetting]]"
  - "[[20 - Research/Papers/Making Pre-trained Language Models Better Continual Few-Shot Relation Extractors#Vấn đề paper giải quyết]]"
first_seen: 2026-08-13
last_updated: 2026-08-13
created_at: 2026-08-13
updated_at: 2026-08-13
tags:
  - concept
  - continual-learning
  - forgetting
---

# Catastrophic Forgetting

## Định nghĩa

Catastrophic forgetting là hiện tượng hiệu năng trên task/class cũ giảm mạnh sau khi model được cập nhật bằng dữ liệu mới. Đây không chỉ là “model học chưa tốt task mới”, mà là kiến thức từng sử dụng được đã bị update sau đó làm hỏng.

## Cách hiểu bằng lời của tôi

Model dùng cùng một không gian parameters cho nhiều task. Gradient của task mới không biết phần nào đang giữ kiến thức cũ; nó có thể kéo representation và decision boundary theo hướng có lợi cho dữ liệu mới nhưng phá cấu trúc cũ.

```text
Task cũ đã học tốt
-> update bằng task mới
-> representation/prototype/classifier dịch chuyển
-> accuracy task cũ giảm
```

## Forgetting xuất hiện ở đâu?

### Shared encoder hoặc shared prompt

Update task mới làm feature của sample cũ trôi đi. Dù classifier cũ còn nguyên, input không còn nằm ở vùng latent space quen thuộc.

### Prototype hoặc memory summary

Prototype cũ bị distortion hoặc buffer chỉ chứa một slice hẹp, khiến “điểm neo” class không còn đại diện đúng distribution.

### Shared classifier

Classifier chỉ thấy class mới trong update hiện tại nên logits/decision boundary bị bias về class mới. WAVE++ cho thấy freeze prompt pools vẫn chưa đủ: bỏ latent replay làm accuracy stage cuối giảm từ 87,7 xuống 62,1 trên FewRel và từ 82,5 xuống 60,3 trên TACRED. [[Capturing Within-Task Variance for Continual Relation Extraction with Adaptive Prompting.pdf#page=20|PDF, tr. 20]]

### Router/task predictor

Knowledge có thể vẫn còn trong prompt/module cũ, nhưng model chọn sai module khi test. Đây là “functional forgetting”: thông tin chưa chắc bị xóa, nhưng đường truy cập tới nó sai.

## Phân biệt với overfitting

| Hiện tượng | Câu hỏi chính |
|---|---|
| Overfitting | Model có tổng quát từ few training examples ra unseen examples cùng task không? |
| Catastrophic forgetting | Sau khi học task mới, model còn làm được task cũ không? |

Hai vấn đề có thể cùng xảy ra trong [[Continual Few-Shot Relation Extraction]]: model vừa fit quá sát vài examples mới, vừa quên class cũ.

## Cách đo

Với accuracy $a_{i,t}$ trên task $i$ sau stage $t$:

$$
F_{i,t}=\max_{k<t}a_{i,k}-a_{i,t}
$$

Average forgetting lấy trung bình qua các task cũ. Ngoài ra cần xem:

- accuracy theo từng task qua từng stage, không chỉ average;
- confusion giữa old/new classes;
- representation drift/prototype distortion;
- task-prediction error nếu dùng task-specific modules;
- nhiều task orders và seeds.

## Chiến lược giảm forgetting

### Replay

Nhắc model về distribution cũ bằng raw samples, generated samples, prototypes hoặc latent vectors. Xem [[Replay in Continual Learning]].

### Parameter isolation

Dành prompts/adapters riêng cho task và freeze phần cũ. Giảm interference nhưng tăng model size và tạo bài toán chọn đúng module.

### Consistency/regularization

Buộc output, representations hoặc distributions trước/sau update gần nhau. ConPL giữ consistency ở cả sample và prototype levels.

### Prototype stabilization

Chọn vital samples, refine prototypes và giảm prototype distortion để class cũ vẫn được kích hoạt đúng. Xem [[Prototype Learning]].

### Semantic anchors

Label descriptions hoặc pretrained knowledge làm neo nghĩa ổn định hơn vài examples cục bộ. WAVE++ dùng description contrastive loss; CPL dùng prompt representation và contrastive learning.

## Trade-off

- Replay mạnh nhưng memory/privacy cost tăng.
- Isolation giảm interference nhưng capacity/model size tăng theo task.
- Regularization bảo vệ cái cũ nhưng có thể giảm plasticity.
- Generative replay tránh raw data nhưng phụ thuộc quality/assumption của generator.
- Router tốt giúp truy cập knowledge cũ nhưng làm inference phức tạp hơn.

## Một diagnostic checklist

1. Old-task representation có drift không?
2. Classifier trên frozen old representations có còn đúng không?
3. Nếu dùng đúng task module oracle, accuracy có hồi phục không?
4. Buffer/prototype có phủ đủ modes hay chỉ vài samples gần centroid?
5. Sụt giảm đến từ task identity hay within-task classification?

Các test này giúp xác định quên nằm ở representation, classifier hay routing thay vì gọi mọi sụt giảm là cùng một lỗi.

## Câu hỏi review

1. Catastrophic forgetting khác overfitting thế nào?
2. Tại sao một model có prompts cũ bị freeze vẫn có thể quên?
3. “Functional forgetting” do router nghĩa là gì?
4. Vì sao average accuracy có thể che giấu forgetting?
5. Replay và regularization bảo vệ kiến thức cũ theo hai cách khác nhau ra sao?

## Gợi ý trả lời

1. Overfitting là tổng quát hóa kém trong task; forgetting là mất hiệu năng cũ sau update mới.
2. Shared classifier hoặc encoder vẫn đổi, hoặc inference chọn sai prompt.
3. Knowledge còn trong module nhưng hệ thống không route input tới đúng module.
4. Accuracy task mới cao có thể bù cho sụt giảm lớn ở task cũ.
5. Replay đưa tín hiệu dữ liệu cũ trở lại objective; regularization hạn chế mức thay đổi của model/representation.

## Liên kết

- [[Continual Learning]]
- [[Continual Relation Extraction]]
- [[Continual Few-Shot Relation Extraction]]
- [[Replay in Continual Learning]]
- [[Prototype Learning]]
- [[Task Identity Inference]]
- [[Data Augmentation]]
