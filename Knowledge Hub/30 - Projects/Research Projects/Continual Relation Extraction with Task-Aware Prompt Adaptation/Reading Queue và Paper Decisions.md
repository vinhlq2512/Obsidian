---
type: project-plan
status: active
project: "[[30 - Projects/Research Projects/Continual Relation Extraction with Task-Aware Prompt Adaptation/Continual Relation Extraction with Task-Aware Prompt Adaptation]]"
created_at: 2026-09-05
updated_at: 2026-09-05
tags:
  - reading-plan
  - research-project
  - continual-learning
  - relation-extraction
---

# Reading Queue và Paper Decisions

## Trạng thái đọc

Đã đọc xong bốn paper lõi:

- [x] [[20 - Research/Papers/Consistent Prototype Learning for Few-Shot Continual Relation Extraction]]
- [x] [[20 - Research/Papers/Making Pre-trained Language Models Better Continual Few-Shot Relation Extractors]]
- [x] [[20 - Research/Papers/Adaptive Prompting for Continual Relation Extraction]]
- [x] [[20 - Research/Papers/WAVE++ - Capturing Within-Task Variance for Continual Relation Extraction]]

Từ tuần 4 trở đi, đọc paper không nên tách khỏi decision. Mỗi paper chỉ cần trả lời: paper này làm mình đổi formulation, baseline, module hay claim nào?

## Must-read trong tháng 09/2026

| Paper                                                                                                         | Mục tiêu đọc                                      | Decision cần rút ra                                            |
| ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------- | -------------------------------------------------------------- |
| [[20 - Research/Papers/Distilling the Knowledge in a Neural Network]]                                         | Hiểu soft target, temperature, KL-divergence      | KD trong TAPTA nên distill logits hay similarity distribution? |
| [[20 - Research/Papers/Learning without Forgetting]]                                                          | Hiểu teacher cũ trong continual learning          | Teacher dùng để giữ old-label behavior như thế nào?            |
| [[20 - Research/Papers/Mean Teachers are Better Role Models]]                                                 | Hiểu EMA teacher                                  | EMA có đáng đưa vào bản chính hay chỉ là ablation?             |
| [[20 - Research/Papers/An Ensemble-of-Experts Framework for Rehearsal-free Continual Relation Extraction]]    | Hiểu decomposition TII/WTP và comparator gần WAVE | Router của mình khác EoE/WAVE ở đâu?                           |
| [[20 - Research/Papers/Serial Contrastive Knowledge Distillation for Continual Few-shot Relation Extraction]] | Hiểu KD + contrastive trong FCRE                  | Có cần SCKD làm baseline hay chỉ dùng để biện minh KD?         |
| [[20 - Research/Papers/FewRel - A Large-Scale Supervised Few-Shot Relation Classification Dataset]]           | Nắm dataset và split                              | Task-order files cần tạo thế nào?                              |
| [[20 - Research/Papers/Re-TACRED - Addressing Shortcomings of the TACRED Dataset]]                            | Nắm limitation của TACRED                         | Có đưa Re-TACRED vào appendix hay chỉ mention limitation?      |

## Must-read trong tháng 10/2026

| Paper | Mục tiêu đọc | Decision cần rút ra |
|---|---|---|
| [[20 - Research/Papers/Continual Few-shot Relation Learning via Embedding Space Regularization and Data Augmentation]] | Nắm ERDA/protocol cũ | Có cần reproduce ERDA hay dùng làm context? |
| [[20 - Research/Papers/Sentence Embedding Alignment for Lifelong Relation Extraction]] | Nắm nguồn gốc lifelong RE | Related work phần memory-based CRE viết ra sao? |
| [[20 - Research/Papers/Continual Relation Learning via Episodic Memory Activation and Reconsolidation]] | Hiểu EMAR và replay memory | Baseline memory lineage cần trình bày thế nào? |
| [[20 - Research/Papers/Refining Sample Embeddings with Relation Prototypes to Enhance Continual Relation Extraction]] | Hiểu prototype trong CRE | Claim prototype-guided routing phải tránh trùng gì? |
| [[20 - Research/Papers/Learning to Prompt for Continual Learning]] | Hiểu prompt pool selection | TAPTA khác L2P ở task/domain nào? |
| [[20 - Research/Papers/Hierarchical Decomposition of Prompt-Based Continual Learning - Rethinking Obscured Sub-optimality]] | Hiểu decomposition task identity/prediction | Metric nào cần báo để tách lỗi routing và lỗi relation classification? |

## Đọc sau khi có baseline

| Paper | Lý do để sau | Cách dùng |
|---|---|---|
| [[20 - Research/Papers/DualPrompt - Complementary Prompting for Rehearsal-free Continual Learning]] | Không phải CRE, dễ làm loãng nếu đọc quá sớm | Related work prompt pool |
| [[20 - Research/Papers/CODA-Prompt - Continual Decomposed Attention-based Prompting for Rehearsal-Free Continual Learning]] | Gần prompt composition nhưng không phải CRE | Inspiration cho weighted prompt composition |
| [[20 - Research/Papers/Hierarchical Prompts for Rehearsal-free Continual Learning]] | Cần để tránh overclaim hierarchy prompt | Novelty audit trước architecture freeze |
| [[20 - Research/Papers/Consistent Prompting for Rehearsal-Free Continual Learning]] | Liên quan train-test mismatch | Dùng nếu P2/P3 có gap train/inference |
| [[20 - Research/Papers/Enhancing Discriminative Representation in Similar Relation Clusters for Few-Shot Continual Relation Extraction]] | Rất liên quan nhưng nên đọc khi bắt đầu error analysis | Similar-relation subset và cluster analysis |
| [[20 - Research/Papers/Mitigating Non-Representative Prototypes and Representation Bias in Few-Shot Continual Relation Extraction]] | Rất liên quan prototype quality | Cách phân tích prototype đại diện kém |

## Stretch papers

Chỉ đọc sâu sau khi P4 đã có pilot hoặc khi viết related work:

- [[20 - Research/Papers/Dynamic-prototype Contrastive Fine-tuning for Continual Few-shot Relation Extraction with Unseen Relation Detection]]
- [[20 - Research/Papers/MPBoCo - Multimodal Prompt-based Boundary-enhanced Continual Framework for Joint Entity and Relation Extraction]]
- [[20 - Research/Papers/Progressive Prompts - Continual Learning for Language Models]]
- [[20 - Research/Papers/Few-Shot No Problem - Descriptive Continual Relation Extraction]]

## Template ghi paper decision

```markdown
## Paper Decision - YYYY-MM-DD

Paper:
Problem:
Setting:
Core idea:
Memory/replay:
Task ID at inference:
Dataset/protocol:
Metric:
Kết quả cần nhớ:
Limitation:
Ảnh hưởng đến thesis:
Decision:
- [ ] đổi formulation
- [ ] thêm/bỏ baseline
- [ ] thêm/bỏ module
- [ ] thêm metric/ablation
- [ ] chỉ dùng trong related work
```

## Rule chống đọc lan man

Nếu sau 90 phút chưa biết paper này ảnh hưởng gì đến thesis, ghi nó vào nhóm `related work only` và quay lại code/evaluator.
