---
type: project-plan
status: active
project: "[[30 - Projects/Research Projects/Continual Relation Extraction with Task-Aware Prompt Adaptation/Continual Relation Extraction with Task-Aware Prompt Adaptation]]"
created_at: 2026-09-05
updated_at: 2026-09-05
tags:
  - project-plan
  - research-project
  - continual-learning
  - relation-extraction
---

# Timeline cá nhân đến 2027-04-30

## Trạng thái thực tế

Tại **tuần 4**, tiến độ thực tế là: đã đọc xong bốn paper lõi [[20 - Research/Papers/Consistent Prototype Learning for Few-Shot Continual Relation Extraction]], [[20 - Research/Papers/Making Pre-trained Language Models Better Continual Few-Shot Relation Extractors]], [[20 - Research/Papers/Adaptive Prompting for Continual Relation Extraction]] và [[20 - Research/Papers/WAVE++ - Capturing Within-Task Variance for Continual Relation Extraction]].

Điều này nghĩa là các phần dataset pipeline, evaluator, Sequential FT, Joint Training và reproduce baseline trong kế hoạch PDF cần được dời lại. Mục tiêu vẫn giữ: có kết quả chính trước cuối tháng 02/2027, đóng băng kết quả đầu tháng 03/2027 và hoàn thiện bản luận văn/paper trong tháng 04/2027.

## Quỹ thời gian làm việc

Giả định làm việc: **2-3 giờ/ngày**, tương đương khoảng **14-18 giờ/tuần** nếu làm đều 6 ngày.

Nhịp ngày nên giữ đơn giản:

- 20-30 phút: đọc paper hoặc ghi literature decision.
- 90-120 phút: code, chạy experiment, debug hoặc phân tích log.
- 15-20 phút: cập nhật tracker, commit/log kết quả, ghi blocker.

Cuối tuần nên dành 60-90 phút để gom kết quả thành weekly report. Nếu một ngày chỉ có 2 giờ, ưu tiên code/evidence hơn đọc thêm paper.

## Nguyên tắc điều chỉnh

- Bốn paper đã đọc là trục chính; paper bổ sung chỉ là `decision papers`, không làm kéo dài timeline.
- Không bắt đầu method phức tạp trước khi evaluator và baseline tối thiểu chạy được.
- Mỗi tuần phải tạo ít nhất một research artifact: một bảng kết quả, một script chạy được, một config, một figure, một baseline smoke run hoặc một design decision có evidence.
- Không thêm module mới sau **2027-01-03**.
- Từ **2027-03-07** trở đi không còn làm research mới, chỉ sửa lỗi kỹ thuật rõ ràng và viết.

## Timeline điều chỉnh

| Giai đoạn | Thời gian                 | Trọng tâm                                                        | Deliverable                                                                                                                                   |
| --------- | ------------------------- | ---------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| W4-gate   | 2026-09-05                | Chuyển 4 paper đã đọc thành research matrix, RQ và protocol spec | [[30 - Projects/Research Projects/Continual Relation Extraction with Task-Aware Prompt Adaptation/Literature Matrix v1, RQ và Protocol Spec]] |
| W5-W6     | 2026-09-06 đến 2026-09-20 | Dataset pipeline và evaluator                                    | FewRel loader, TACRED access/preprocess check, task-order files, performance matrix `A_t,j`                                                   |
| W7-W8     | 2026-09-21 đến 2026-10-04 | Baseline tối thiểu                                               | Sequential FT, Joint Training, Frozen BERT + linear/prototype sanity                                                                          |
| W9-W11    | 2026-10-05 đến 2026-10-25 | Reproduce ConPL/CPL tối thiểu                                    | ConPL/CPL 1 seed FewRel; ghi rõ mismatch nếu lệch paper                                                                                       |
| W12-W13   | 2026-10-26 đến 2026-11-08 | Closest prompt/task-aware baseline                               | WAVE-CRE/WAVE++ hoặc EoE smoke run; baseline protocol freeze v1                                                                               |
| W14-W16   | 2026-11-09 đến 2026-11-29 | Proposed method scaffold                                         | P0 shared prompt, P1 oracle-task prompt, P2 learned router                                                                                    |
| W17-W19   | 2026-11-30 đến 2026-12-20 | Prototype routing và Prompt Tree                                 | P3 prototype router, P4 TAPTA minimal, first ablation table                                                                                   |
| W20       | 2026-12-21 đến 2027-01-03 | Architecture freeze                                              | Design decision memo; quyết định có giữ EMA/verbalizer/LoRA không                                                                             |
| W21-W25   | 2027-01-04 đến 2027-02-07 | Full runs round 1                                                | FewRel + TACRED 3 seeds cho finalists                                                                                                         |
| W26-W29   | 2027-02-08 đến 2027-02-28 | Ablation, sensitivity, error analysis                            | bảng ablation chính, router analysis, memory/latency report                                                                                   |
| W30       | 2027-03-01 đến 2027-03-07 | Result freeze                                                    | final results table, figures, appendix draft                                                                                                  |
| W31-W34   | 2027-03-08 đến 2027-04-04 | Viết bản đầy đủ                                                  | full draft Chương 1-5                                                                                                                         |
| W35-W36   | 2027-04-05 đến 2027-04-18 | Sửa và hoàn thiện                                                | near-final thesis, references, figures, appendix                                                                                              |
| W37-W38   | 2027-04-19 đến 2027-04-30 | Buffer cuối                                                      | reproducibility package, slide/demo, final submission package                                                                                 |

## Reading milestones theo giai đoạn

Không phải chỉ cần bốn paper. Bốn paper ConPL, CPL, WAVE-CRE và WAVE++ là **core foundation** để chốt gap ban đầu. Từ sau 2026-09-05, paper bổ sung phải đọc theo kiểu `decision reading`: mỗi paper cần tạo ra một quyết định rõ về formulation, metric, baseline, module hoặc limitation.

Reading queue chi tiết nằm ở [[30 - Projects/Research Projects/Continual Relation Extraction with Task-Aware Prompt Adaptation/Reading Queue và Paper Decisions]].

| Thời gian                 | Paper cần đọc                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Mục đích đọc                                                               | Output tối thiểu                                                                                                                              |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| 2026-09-05                | Đã xong: [[20 - Research/Papers/Consistent Prototype Learning for Few-Shot Continual Relation Extraction]], [[20 - Research/Papers/Making Pre-trained Language Models Better Continual Few-Shot Relation Extractors]], [[20 - Research/Papers/Adaptive Prompting for Continual Relation Extraction]], [[20 - Research/Papers/WAVE++ - Capturing Within-Task Variance for Continual Relation Extraction]]                                                                | Chốt research matrix, RQ và protocol spec                                  | [[30 - Projects/Research Projects/Continual Relation Extraction with Task-Aware Prompt Adaptation/Literature Matrix v1, RQ và Protocol Spec]] |
| 2026-09-06 đến 2026-09-20 | [[20 - Research/Papers/FewRel - A Large-Scale Supervised Few-Shot Relation Classification Dataset]], [[20 - Research/Papers/Re-TACRED - Addressing Shortcomings of the TACRED Dataset]], [[20 - Research/Papers/Distilling the Knowledge in a Neural Network]], [[20 - Research/Papers/Learning without Forgetting]]                                                                                                                                                    | Dataset/protocol và nền KD cơ bản                                          | dataset access note, evaluator spec, quyết định KD logits/similarity                                                                          |
| 2026-09-21 đến 2026-10-04 | [[20 - Research/Papers/Mean Teachers are Better Role Models]], [[20 - Research/Papers/Serial Contrastive Knowledge Distillation for Continual Few-shot Relation Extraction]]                                                                                                                                                                                                                                                                                            | Hiểu EMA teacher và KD trong FCRE                                          | quyết định EMA là main module hay ablation; SCKD có cần baseline không                                                                        |
| 2026-10-05 đến 2026-10-25 | [[20 - Research/Papers/Continual Few-shot Relation Learning via Embedding Space Regularization and Data Augmentation]], [[20 - Research/Papers/Sentence Embedding Alignment for Lifelong Relation Extraction]], [[20 - Research/Papers/Continual Relation Learning via Episodic Memory Activation and Reconsolidation]], [[20 - Research/Papers/Refining Sample Embeddings with Relation Prototypes to Enhance Continual Relation Extraction]]                          | Nắm lineage memory/prototype CRE để viết related work và chọn baseline     | baseline decision log, paragraph related work memory-based CRE                                                                                |
| 2026-10-26 đến 2026-11-08 | [[20 - Research/Papers/An Ensemble-of-Experts Framework for Rehearsal-free Continual Relation Extraction]], [[20 - Research/Papers/Learning to Prompt for Continual Learning]], [[20 - Research/Papers/Hierarchical Decomposition of Prompt-Based Continual Learning - Rethinking Obscured Sub-optimality]]                                                                                                                                                             | Kiểm tra novelty task routing/prompt selection                             | quyết định TAPTA khác EoE/L2P/HiDe ở đâu                                                                                                      |
| 2026-11-09 đến 2026-12-20 | [[20 - Research/Papers/DualPrompt - Complementary Prompting for Rehearsal-free Continual Learning]], [[20 - Research/Papers/CODA-Prompt - Continual Decomposed Attention-based Prompting for Rehearsal-Free Continual Learning]], [[20 - Research/Papers/Hierarchical Prompts for Rehearsal-free Continual Learning]], [[20 - Research/Papers/Consistent Prompting for Rehearsal-Free Continual Learning]]                                                              | Chỉ đọc khi ảnh hưởng đến Prompt Tree/composition hoặc train-test mismatch | architecture decision memo trước 2027-01-03                                                                                                   |
| 2027-01-04 đến 2027-02-28 | [[20 - Research/Papers/Enhancing Discriminative Representation in Similar Relation Clusters for Few-Shot Continual Relation Extraction]], [[20 - Research/Papers/Mitigating Non-Representative Prototypes and Representation Bias in Few-Shot Continual Relation Extraction]]                                                                                                                                                                                           | Phục vụ error analysis và prototype-quality analysis                       | similar-relation analysis, prototype failure cases                                                                                            |
| Sau khi có P4 pilot       | [[20 - Research/Papers/Dynamic-prototype Contrastive Fine-tuning for Continual Few-shot Relation Extraction with Unseen Relation Detection]], [[20 - Research/Papers/MPBoCo - Multimodal Prompt-based Boundary-enhanced Continual Framework for Joint Entity and Relation Extraction]], [[20 - Research/Papers/Progressive Prompts - Continual Learning for Language Models]], [[20 - Research/Papers/Few-Shot No Problem - Descriptive Continual Relation Extraction]] | Stretch hoặc related work, không chặn kết quả chính                        | appendix/related-work note nếu còn thời gian                                                                                                  |

Rule thực dụng: trong tháng 09-10, mỗi tuần tối đa 1-2 paper đọc sâu; các paper còn lại đọc skim 60-90 phút để lấy decision. Nếu paper không làm thay đổi code, baseline, metric hoặc claim, đưa vào related work thay vì kéo dài timeline.

## Milestone cứng

| Deadline | Gate phải đạt | Nếu chưa đạt |
|---|---|---|
| 2026-09-05 | [[30 - Projects/Research Projects/Continual Relation Extraction with Task-Aware Prompt Adaptation/Literature Matrix v1, RQ và Protocol Spec]] | Không đọc thêm paper mới; khóa formulation trước |
| 2026-09-20 | Dataset pipeline + evaluator skeleton | Dừng baseline reproduce, sửa evaluator trước |
| 2026-10-04 | Sequential FT + Joint + prototype sanity | Chưa implement TAPTA |
| 2026-11-08 | Có ít nhất một prompt/task-aware baseline smoke run | Dùng EoE/WAVE reimplementation comparator nếu repo khó chạy |
| 2026-11-29 | P0/P1/P2 chạy được | Nếu P1 oracle không hơn P0, xem lại prompt design |
| 2026-12-20 | P3/P4 pilot có tín hiệu | Nếu không có tín hiệu, thu hẹp thành prototype router + analysis |
| 2027-01-03 | Architecture freeze | Không thêm module mới |
| 2027-02-28 | Ablation chính gần xong | Bỏ stretch datasets/papers |
| 2027-03-07 | Result freeze | Chỉ rerun lỗi kỹ thuật nghiêm trọng |
| 2027-04-30 | Final package | Không thêm experiment |

## Thứ tự ưu tiên nếu thiếu thời gian

Giữ:

- FewRel 5-shot.
- TACRED 5-shot hoặc bản TACRED protocol nhỏ hơn nếu compute hạn chế.
- Sequential FT, Joint Training, ConPL/CPL, WAVE-CRE/WAVE++ hoặc EoE.
- P0, P1, P2, P3, P4.
- Ablation tree vs flat, hard vs soft routing, no KD vs KD.

Cắt:

- Re-TACRED robustness.
- DPC-FT full reproduction.
- MPBoCo implementation.
- LoRA/verbalizer nếu bản prototype classifier đã đủ kể chuyện.
- 5 seeds cho mọi model; chỉ 5 seeds cho finalists, baseline khác có thể 3 seeds nếu compute thiếu.

## Câu chuyện kết quả cần hướng tới

Thesis không bắt buộc phải đạt SOTA tuyệt đối. Câu chuyện đủ tốt là:

> Khi inference không có task ID, prompt-based CRE dễ mất điểm ở bước chọn prompt/task. Nếu tách oracle-task upper bound, learned router và prototype-guided hierarchical router, ta đo được chính xác phần mất mát do routing và kiểm tra liệu semantic/prototype hierarchy có giảm lỗi này, đặc biệt với các relation gần nghĩa.
