---
type: concept
status: developing
sources:
  - "[[Hands-On LLM - Chapter 10 - Creating Text Embedding Models]]"
  - "[[WAVE++ - Capturing Within-Task Variance for Continual Relation Extraction]]"
  - "[[20 - Research/Papers/Consistent Prototype Learning for Few-Shot Continual Relation Extraction]]"
  - "[[20 - Research/Papers/Making Pre-trained Language Models Better Continual Few-Shot Relation Extractors]]"
source_sections:
  - "[[Hands-On LLM - Chapter 10 - Creating Text Embedding Models]]"
  - "[[WAVE++ - Capturing Within-Task Variance for Continual Relation Extraction#3. Label descriptions và contrastive alignment]]"
  - "[[20 - Research/Papers/Consistent Prototype Learning for Few-Shot Continual Relation Extraction#Loss cho confusing classes]]"
  - "[[20 - Research/Papers/Making Pre-trained Language Models Better Continual Few-Shot Relation Extractors#2. Margin-based contrastive learning]]"
first_seen: 2026-08-03
last_updated: 2026-08-13
updated_at: 2026-08-13
tags:
  - concept
  - machine-learning
  - embeddings
---

# Contrastive Learning

## Định nghĩa

Contrastive learning là phương pháp học biểu diễn bằng cách kéo các cặp liên quan lại gần nhau và đẩy các cặp không liên quan ra xa nhau trong embedding space.

## Cách hiểu bằng lời của tôi

Model học nghĩa của "giống nhau" từ các ví dụ so sánh. Nếu dữ liệu nói hai câu là paraphrase, vector của chúng nên gần nhau. Nếu chúng không liên quan, vector nên xa nhau.

## Cần biết

- Chất lượng positive/negative pairs cực kỳ quan trọng.
- Được dùng trong embedding models, CLIP, SBERT và retrieval training.
- Similarity học được phụ thuộc vào objective.

## Supervised contrastive learning

Khi có labels, positives của anchor $i$ là samples cùng class $P(i)$ và negatives là samples khác class $N(i)$. Một dạng loss:

$$
\mathcal L_i=-\frac{1}{|P(i)|}
\sum_{p\in P(i)}
\log\frac{\exp(sim(z_i,z_p)/\tau)}
{\sum_{a\ne i}\exp(sim(z_i,z_a)/\tau)}
$$

$\tau$ là temperature. Temperature thấp làm phân phối sắc hơn và gradient tập trung mạnh vào pairs gần decision boundary.

## Ba biến thể từ các paper CRE

### Label-description contrastive loss — WAVE++

Positive không phải sample khác mà là description embeddings của đúng relation. Input representation được kéo về semantic anchors của label và đẩy khỏi descriptions của toàn bộ labels đã thấy.

Ưu điểm: descriptions chứa global relation semantics, bớt phụ thuộc vài surface examples. Rủi ro: description sinh bởi LLM có noise/bias; nhiều descriptions hơn không luôn tốt.

### Similar-class restricted loss — ConPL

Chọn nearest/confusing negative prototypes rồi tính cross-entropy trên positive + hard negatives. Điều này dồn gradient vào relations gần nghĩa.

Paper gọi đây là focal loss, nhưng công thức không có $(1-p)^\gamma$ của focal loss chuẩn. Nên mô tả theo cơ chế thật thay vì chỉ theo tên.

### Margin-based contrastive learning — CPL

CPL thay đổi contribution của mỗi pair dựa trên similarity:

$$
\alpha_{i,p}=m+k s_{i,p},\qquad
\alpha_{i,n}=1-m+k s_{i,n}
$$

rồi scale logits $\alpha s/\tau$. Mục tiêu là điều chỉnh boundary theo độ khó pair và tập trung hơn vào hard positives/negatives.

Feature bucket của current task cung cấp nhiều pairs hơn mini-batch nhỏ, nhưng stored features có thể stale sau encoder updates nếu không refresh đúng.

## Hard negatives

Hard negative là sample/prototype khác class nhưng similarity cao với anchor. Chúng giàu tín hiệu vì nằm gần boundary, song có hai rủi ro:

- false negatives: thực ra cùng nghĩa/label noise;
- quá tập trung hard negatives làm training bất ổn hoặc collapse.

Nên so random negatives, in-batch negatives và mined negatives; theo dõi error theo relation pairs chứ không chỉ average loss.

## Liên hệ với prototype learning

Contrastive loss học geometry; [[Prototype Learning]] dùng geometry đó để phân loại. Hai phần phải nhất quán:

```text
contrastive objective -> samples cùng relation tạo cluster
prototype -> tóm tắt cluster
nearest prototype -> prediction
```

Nếu contrastive training làm cluster đa mode hoặc prototype lấy một exemplar kém đại diện, metric classifier vẫn có thể sai.

## Evaluation checklist

- Positive/negative pairs được tạo thế nào?
- Có normalize embeddings và dùng cosine similarity không?
- Temperature/margin sensitivity ra sao?
- Batch/feature-bucket size có công bằng giữa methods không?
- Có false-negative filtering không?
- T-SNE chỉ minh họa; cần accuracy, retrieval/cluster metrics hoặc ablation định lượng.
- Improvement đến từ loss hay từ nhiều negatives/memory hơn?

## Câu hỏi review

1. Temperature điều khiển gì?
2. Hard negative hữu ích và nguy hiểm ở đâu?
3. Description embedding đóng vai positive anchor thế nào?
4. MCL của CPL khác supervised contrastive loss cơ bản ở đâu?
5. Vì sao t-SNE không đủ chứng minh embedding tốt hơn?

## Gợi ý trả lời

1. Độ sắc của softmax trên similarities và mức tập trung gradient.
2. Nó chỉ ra boundary khó nhưng có thể là false negative/noisy label.
3. Input được kéo về semantic representation của đúng relation thay vì chỉ sample cùng label.
4. Pair-specific factors dựa trên similarity thay đổi logits/margin và contribution của hard/easy pairs.
5. Projection 2D có thể bóp méo khoảng cách và chỉ là một slice định tính.

## Liên kết

- [[Embedding]]
- [[Semantic Search]]
- [[Multimodal LLM]]
- [[Prototype Learning]]
- [[Continual Few-Shot Relation Extraction]]
- [[Catastrophic Forgetting]]
- [[Prompt Tuning]]
