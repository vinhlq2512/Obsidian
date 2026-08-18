---
type: moc
status: evolving
area: continual-learning
concepts:
  - "[[Continual Learning]]"
  - "[[Catastrophic Forgetting]]"
  - "[[Continual Relation Extraction]]"
  - "[[Continual Few-Shot Relation Extraction]]"
  - "[[Replay in Continual Learning]]"
  - "[[Prototype Learning]]"
  - "[[Prompt Pool]]"
  - "[[Task Identity Inference]]"
  - "[[Relation Extraction]]"
  - "[[Few-shot Learning]]"
  - "[[Contrastive Learning]]"
  - "[[Data Augmentation]]"
syntheses: []
questions: []
created_at: 2026-08-18
updated_at: 2026-08-18
tags:
  - moc
  - continual-learning
  - paper
  - nlp
---

# Continual Learning

MOC này gom các note về [[Continual Learning]] trong vault, đặc biệt là tuyến paper về [[Continual Relation Extraction]] và [[Continual Few-Shot Relation Extraction]]. Trục đọc chính không chỉ là “method nào accuracy cao hơn”, mà là mỗi paper lưu kiến thức cũ ở đâu, chống [[Catastrophic Forgetting]] bằng cơ chế nào, và protocol đánh giá có công bằng không.

> [!note] Trạng thái đọc
> Một số paper note đã được agent phân tích từ PDF để phục vụ nghiên cứu, nhưng `reading_status` của người đọc vẫn được giữ riêng. MOC này không đánh dấu paper nào là đã đọc xong.

## Bản đồ nhanh

```text
Continual Learning
-> Catastrophic Forgetting
-> Replay / Regularization / Parameter Isolation / Prototype
-> Continual Relation Extraction
-> Continual Few-Shot Relation Extraction
-> Paper line: ConPL, CPL, WAVE-CRE, WAVE++
```

## Khái niệm lõi

- [[Continual Learning]] — bài toán học theo chuỗi task/data distributions, phải cân bằng stability và plasticity.
- [[Catastrophic Forgetting]] — hiện tượng học task mới làm giảm năng lực trên task cũ.
- [[Replay in Continual Learning]] — giữ hoặc sinh lại tín hiệu từ quá khứ để chống quên.
- [[Prototype Learning]] — biểu diễn class/relation bằng vector neo; quan trọng trong ConPL và CPL.
- [[Prompt Pool]] — dùng nhiều prompt/prefix như các “module” nhỏ để cô lập hoặc route tri thức theo task/input.
- [[Task Identity Inference]] — bài toán chọn đúng task/module khi test không cung cấp task ID.
- [[Few-shot Learning]] — bối cảnh ít mẫu làm continual learning dễ overfit và khó đánh giá hơn.

## Nhánh NLP và relation extraction

- [[Relation Extraction]] — task nền: phát hiện quan hệ giữa hai entity mention trong context.
- [[Continual Relation Extraction]] — relation types xuất hiện dần theo task; sau mỗi task model phải dự đoán trên toàn bộ relation đã thấy.
- [[Continual Few-Shot Relation Extraction]] — biến thể khó hơn, mỗi relation/task chỉ có rất ít ví dụ gán nhãn.

Mental model khi đọc paper CRE:

```text
Input sentence + entity pair
-> representation / prompt / encoder
-> task identity hoặc task pool
-> relation classifier hoặc nearest prototype
-> đánh giá trên tất cả relation đã thấy
```

Mỗi mũi tên là một nơi có thể quên: representation drift, routing sai, prototype méo, classifier bias về relation mới.

## Tuyến paper chính

| Paper | Trọng tâm | Cơ chế chống quên | Trạng thái đọc |
|---|---|---|---|
| [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction]] | NK-CRE, prototype distortion, consistency | Lưu exemplar + prototype, memory replay, consistency loss, hard negatives | `in-progress` |
| [[Making Pre-trained Language Models Better Continual Few-Shot Relation Extractors]] | CPL, prompt representation, contrastive learning, augmentation | Contrastive prompt learning, exemplar replay, GPT-3.5 augmentation, nearest-class-mean | `not-started` |
| [[Adaptive Prompting for Continual Relation Extraction]] | WAVE-CRE, within-task variance, prompt pool | Task-specific prompt pools, latent Gaussian replay, relation-level task predictor | `not-started` |
| [[WAVE++ - Capturing Within-Task Variance for Continual Relation Extraction]] | WAVE++ mở rộng WAVE-CRE | Prompt pools, label descriptions, cascade voting, latent replay | `not-started` |

## Cách đọc theo câu hỏi nghiên cứu

### 1. Kiến thức cũ được lưu ở đâu?

- [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction]] lưu raw exemplar và prototype vector cho mỗi relation.
- [[Making Pre-trained Language Models Better Continual Few-Shot Relation Extractors]] lưu exemplar rồi augment thêm bằng LLM để mở rộng memory nhỏ.
- [[Adaptive Prompting for Continual Relation Extraction]] và [[WAVE++ - Capturing Within-Task Variance for Continual Relation Extraction]] tránh lưu raw examples, thay bằng prompt parameters và latent replay.

### 2. Cơ chế nào bảo vệ phần shared?

- Replay bảo vệ classifier/representation bằng cách đưa lại tín hiệu cũ.
- Consistency giữ sample, prototype hoặc distribution không drift quá xa.
- Prompt/prefix isolation giảm interference trực tiếp giữa task.
- Task identity inference/cascade voting quyết định đúng “ngăn tri thức” khi inference.

### 3. Failure mode chính là gì?

- Memory nhỏ có thể không đại diện đủ distribution cũ.
- Synthetic augmentation có thể tạo noise hoặc câu không đúng relation.
- Prototype đơn có thể che mất class có nhiều mode.
- Prompt pool cần routing đúng; sai task pool làm train-test mismatch.
- Latent Gaussian replay phụ thuộc assumption distribution trong latent space đủ gần thực tế.

## So sánh hướng tiếp cận

| Hướng | Note nên đọc | Khi hữu ích | Cần cảnh giác |
|---|---|---|---|
| Prototype + replay | [[Prototype Learning]], [[Replay in Continual Learning]], ConPL | Khi relation có thể neo bằng centroid hoặc exemplar đại diện | Prototype distortion, boundary cases |
| Prompt + contrastive | CPL, [[Contrastive Learning]], [[Data Augmentation]] | Khi muốn tận dụng PLM và vài mẫu làm neo nghĩa | Overfit few-shot, synthetic noise |
| Prompt pool + latent replay | WAVE-CRE, WAVE++, [[Prompt Pool]], [[Task Identity Inference]] | Khi không muốn lưu raw examples | Routing sai, inference cost, shared classifier vẫn có thể quên |

## Checklist khi thêm paper continual learning mới

- Paper thuộc task-incremental, class-incremental, domain-incremental hay online continual learning?
- Test có cung cấp task identity không?
- Có lưu raw data cũ, synthetic data, prototypes, distributions hay parameters riêng?
- Memory budget được báo rõ chưa?
- Metric có báo average accuracy, forgetting, nhiều task orders/seeds không?
- Protocol có công bằng với baseline về backbone, task split, số shot và memory không?
- Failure mode có nằm ở representation, memory/prototype, routing hay classifier?

## Câu hỏi nghiên cứu đang mở

- Làm sao đo riêng lỗi do [[Task Identity Inference]] và lỗi do within-task relation classification?
- Khi nào latent replay đủ thay raw replay, và khi nào Gaussian assumption làm kết quả lạc quan?
- Prototype distortion có quan hệ nhân quả với forgetting hay chỉ là tín hiệu tương quan?
- Với CFRE, LLM-based augmentation giúp vì tăng diversity hay vì vô tình đưa thêm prior knowledge từ pretraining?
- Có thể thiết kế benchmark CRE có memory/privacy constraint sát thực tế hơn không?

## Liên kết liên quan

- [[NLP]]
- [[LLM]]
- [[Transformers]]
- [[Relation Extraction]]
- [[Continual Learning]]
- [[Continual Relation Extraction]]
- [[Continual Few-Shot Relation Extraction]]
- [[Catastrophic Forgetting]]
- [[Replay in Continual Learning]]
- [[Prompt Pool]]
- [[Task Identity Inference]]
- [[Prototype Learning]]
