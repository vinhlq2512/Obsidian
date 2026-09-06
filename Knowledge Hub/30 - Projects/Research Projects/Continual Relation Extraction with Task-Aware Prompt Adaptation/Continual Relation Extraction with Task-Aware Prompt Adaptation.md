---
type: project
status: draft
title: "Continual Relation Extraction with Task-Aware Prompt Adaptation"
vietnamese_title: "Trích xuất quan hệ liên tục với kỹ thuật tinh chỉnh Prompt theo tác vụ"
area: continual-learning
topic:
  - continual relation extraction
  - task-aware prompt adaptation
  - prompt tree
  - prototype memory
  - knowledge distillation
related_literature:
  - "[[20 - Research/Literature Notes/Continual Relation Extraction - Prototype, Prompt và Replay]]"
  - "[[20 - Research/Papers/Distilling the Knowledge in a Neural Network]]"
  - "[[20 - Research/Papers/Consistent Prototype Learning for Few-Shot Continual Relation Extraction]]"
  - "[[20 - Research/Papers/Making Pre-trained Language Models Better Continual Few-Shot Relation Extractors]]"
  - "[[20 - Research/Papers/Adaptive Prompting for Continual Relation Extraction]]"
  - "[[20 - Research/Papers/WAVE++ - Capturing Within-Task Variance for Continual Relation Extraction]]"
  - "[[20 - Research/Papers/Learning to Prompt for Continual Learning]]"
  - "[[20 - Research/Papers/Hierarchical Decomposition of Prompt-Based Continual Learning - Rethinking Obscured Sub-optimality]]"
  - "[[20 - Research/Papers/Mean Teachers are Better Role Models]]"
  - "[[20 - Research/Papers/Serial Contrastive Knowledge Distillation for Continual Few-shot Relation Extraction]]"
  - "[[20 - Research/Papers/Enhancing Discriminative Representation in Similar Relation Clusters for Few-Shot Continual Relation Extraction]]"
  - "[[20 - Research/Papers/Mitigating Non-Representative Prototypes and Representation Bias in Few-Shot Continual Relation Extraction]]"
  - "[[20 - Research/Papers/FewRel - A Large-Scale Supervised Few-Shot Relation Classification Dataset]]"
  - "[[20 - Research/Papers/Re-TACRED - Addressing Shortcomings of the TACRED Dataset]]"
related_concepts:
  - "[[Continual Relation Extraction]]"
  - "[[Continual Few-Shot Relation Extraction]]"
  - "[[Prompt Pool]]"
  - "[[Task Identity Inference]]"
  - "[[Prototype Learning]]"
  - "[[Replay in Continual Learning]]"
  - "[[Knowledge Distillation]]"
  - "[[Catastrophic Forgetting]]"
created_at: 2026-09-05
updated_at: 2026-09-05
tags:
  - project
  - research-project
  - continual-learning
  - relation-extraction
---

# Continual Relation Extraction with Task-Aware Prompt Adaptation

## Định vị đề tài

Đề tài nên được định vị như một phương pháp [[Continual Relation Extraction]] kết hợp ba ý tưởng:

1. **Task-aware prompt adaptation:** học prompt/prefix theo cấu trúc task hoặc nhóm relation, nhằm giảm interference giữa các task như tuyến WAVE-CRE/WAVE++.
2. **Prototype-guided routing:** dùng [[Prototype Learning]] để định tuyến mềm input tới vùng tri thức phù hợp, tránh phụ thuộc hoàn toàn vào task predictor dạng classifier.
3. **EMA teacher distillation:** dùng Student-EMA-Teacher để giữ ổn định tri thức cũ mà không cần lưu toàn bộ dữ liệu cũ.

Tên đề tài hiện tại phù hợp nếu trọng tâm chính là **prompt được điều chỉnh theo task và được chọn bằng routing dựa trên prototype**. Nếu phần EMA/KD trở thành đóng góp chính hơn prompt adaptation, tên cần mở rộng, ví dụ: `Task-Aware Prompt Adaptation with EMA Distillation for Continual Relation Extraction`.

## Đánh giá khả thi và khả năng ra paper

### Kết luận nhanh

Đề tài **khả thi**, nhưng chỉ đủ mạnh nếu triển khai theo hướng hẹp và có ablation rõ. Phiên bản hiện tại có nhiều module tốt, nhưng nếu đưa tất cả vào ngay từ đầu thì dễ bị phản biện là “ghép nhiều kỹ thuật đã có” thay vì một đóng góp khoa học rõ.

### Khả thi ở mức luận văn

Mức khả thi: **cao**, nếu scope là FewRel/TACRED và backbone BERT/RoBERTa frozen.

Lý do:

- Dataset và protocol CRE đã có trong các paper ConPL, CPL, WAVE-CRE, WAVE++.
- Các mảnh kỹ thuật đều có tiền lệ: prompt pool từ L2P/DualPrompt/WAVE, prototype từ ConPL/iCaRL, KD từ LwF, EMA từ Mean Teacher.
- MVP có thể bắt đầu bằng metric classifier/prototype, chưa cần verbalizer hoặc LoRA.

Rủi ro chính không nằm ở code, mà nằm ở **thiết kế ablation** và **định nghĩa novelty**.

### Khả năng ra paper

Mức khả năng: **trung bình đến khá**, nếu có ít nhất một trong ba kết quả sau:

1. **Accuracy/forgetting tốt hơn WAVE-CRE/EoE/WAVE++ trong cùng protocol**, hoặc ít nhất ngang accuracy nhưng giảm inference cost.
2. **Routing tốt hơn:** task identification accuracy cao hơn hoặc ít lỗi wrong-prompt hơn, đặc biệt ở các relation gần nghĩa.
3. **Ablation thuyết phục:** Prompt Tree + soft prototype routing đóng góp độc lập, không chỉ nhờ KD/EMA.

Nếu chỉ đạt “thêm EMA vào WAVE-like prompt pool” thì khả năng ra paper yếu, vì reviewer có thể xem là engineering combination. Nếu chứng minh được **prototype-guided hierarchical soft routing thay cascade voting/task predictor** thì câu chuyện paper sáng hơn.

### Mức thuyết phục hiện tại

Hiện tại ý tưởng **có hướng**, nhưng chưa đủ thuyết phục ở ba điểm:

- Chưa chốt representation dùng cho routing: `[CLS]`, `[MASK]`, hay entity-pair representation.
- Chưa rõ Prompt Tree được sinh từ task id, clustering, ontology, hay learned routing.
- Chưa có baseline/ablation tối thiểu để tách Prompt Tree khỏi KD/EMA.

Đường đi tốt nhất là đặt contribution chính như sau:

> Đề tài đề xuất một cơ chế task-aware prompt adaptation dạng cây, trong đó prototype memory phân cấp được dùng để định tuyến mềm input tới prompt composition phù hợp, giúp giảm lỗi task routing và giảm forgetting trong Continual Relation Extraction khi inference không có task id.

## Paper cần đọc thêm

### Nhóm nhập môn Teacher-Student, KD và EMA

Nếu bạn mới biết LLM nhưng chưa quen distillation, nên đọc theo thứ tự này:

1. [[20 - Research/Papers/Distilling the Knowledge in a Neural Network]] — hiểu teacher/student, soft target, temperature, KL-divergence.
2. [[20 - Research/Papers/Learning without Forgetting]] — hiểu vì sao distillation dùng được trong continual learning khi không có dữ liệu cũ đầy đủ.
3. [[20 - Research/Papers/Dark Experience for General Continual Learning]] — hiểu logit replay/dark knowledge và vì sao KD là một dạng giữ hành vi cũ.
4. [[20 - Research/Papers/Mean Teachers are Better Role Models]] — hiểu EMA Teacher là weight-averaged teacher, không phải teacher “thông minh hơn” một cách tuyệt đối.

Sau cụm này cần tự trả lời được:

- Teacher khác Student ở đâu?
- Soft labels khác hard labels ở đâu?
- Vì sao KD giúp chống quên nhưng không đảm bảo giữ mọi tri thức cũ?
- EMA khác checkpoint cuối task ở đâu?

### Nhóm nhập môn Prompt/Prefix tuning

Đây là cụm cần đọc trước khi viết `Prompt Tree`:

1. [[20 - Research/Papers/Prefix-Tuning - Optimizing Continuous Prompts for Generation]] — hiểu prefix vector trong attention.
2. [[20 - Research/Papers/The Power of Scale for Parameter-Efficient Prompt Tuning]] — hiểu soft prompt tuning với frozen LM.
3. [[20 - Research/Papers/P-Tuning v2 - Prompt Tuning Can Be Comparable to Fine-tuning Universally Across Scales and Tasks]] — hiểu prompt tuning cho NLU/classification.
4. [[02 - Sections/CS224N/2021 - LoRA - Low-Rank Adaptation of Large Language Models - arXiv 2106.09685v2]] — chỉ đọc sau khi đã có prompt baseline, để biết LoRA có cần thêm không.

Sau cụm này cần tự trả lời được:

- Prompt engineering khác prompt tuning ở đâu?
- Soft prompt, prefix prompt và LoRA khác nhau ở tham số trainable nào?
- Với relation extraction, nên lấy representation tại `[MASK]`, `[CLS]`, hay entity pair?

### Nhóm bắt buộc cho prompt continual learning

- [[20 - Research/Papers/Learning to Prompt for Continual Learning]] — nền cho prompt pool và task-agnostic prompt selection.
- [[20 - Research/Papers/DualPrompt - Complementary Prompting for Rehearsal-free Continual Learning]] — nền cho tách prompt chung và prompt riêng theo task.
- [[20 - Research/Papers/CODA-Prompt - Continual Decomposed Attention-based Prompting for Rehearsal-Free Continual Learning]] — gần với ý tưởng prompt composition bằng trọng số phụ thuộc input.
- [[20 - Research/Papers/Hierarchical Decomposition of Prompt-Based Continual Learning - Rethinking Obscured Sub-optimality]] — nền lý thuyết cho tách task-identity inference, within-task prediction và task-adaptive prediction.
- [[20 - Research/Papers/Hierarchical Prompts for Rehearsal-free Continual Learning]] — cần đọc để xác định phần hierarchy prompt nào đã có, tránh overclaim novelty.
- [[20 - Research/Papers/Consistent Prompting for Rehearsal-Free Continual Learning]] — cần đọc để xử lý train-test mismatch trong prompt selection.

### Nhóm bắt buộc cho CRE/task routing

- [[20 - Research/Papers/An Ensemble-of-Experts Framework for Rehearsal-free Continual Relation Extraction]] — baseline rất gần cho task identification và cascade voting trong CRE.
- [[20 - Research/Papers/Adaptive Prompting for Continual Relation Extraction]] — WAVE-CRE là baseline trực tiếp nhất.
- [[20 - Research/Papers/WAVE++ - Capturing Within-Task Variance for Continual Relation Extraction]] — baseline mạnh nhất trong tuyến prompt-based CRE hiện có trong vault.

### Nhóm nền cho KD, EMA và prototype

- [[20 - Research/Papers/Learning without Forgetting]] — nền cho KD khi không có dữ liệu cũ đầy đủ.
- [[20 - Research/Papers/Dark Experience for General Continual Learning]] — nền cho logit replay và dark knowledge trong continual learning.
- [[20 - Research/Papers/iCaRL - Incremental Classifier and Representation Learning]] — nền cho exemplar/prototype/NCM trong class-incremental learning.
- [[20 - Research/Papers/Mean Teachers are Better Role Models]] — nền cho EMA Teacher, nhưng cần chuyển hóa cẩn thận sang continual distillation.

## Lộ trình học cho người mới

### Giai đoạn 1: Nắm bài toán CRE

Đọc:

- [[Continual Relation Extraction]]
- [[Continual Few-Shot Relation Extraction]]
- [[20 - Research/Literature Notes/Continual Relation Extraction - Prototype, Prompt và Replay]]
- [[20 - Research/Papers/Consistent Prototype Learning for Few-Shot Continual Relation Extraction]]

Kết quả cần đạt: giải thích được task stream, old/new relation, catastrophic forgetting, prototype distortion, và vì sao protocol ConPL khác WAVE/WAVE++.

### Giai đoạn 2: Hiểu Teacher-Student/KD

Đọc:

- [[Knowledge Distillation]]
- [[20 - Research/Papers/Distilling the Knowledge in a Neural Network]]
- [[20 - Research/Papers/Learning without Forgetting]]
- [[20 - Research/Papers/Mean Teachers are Better Role Models]]

Mental model:

```text
Teacher = bản model cũ bị đóng băng
Student = model hiện tại đang học task mới
KD = ép Student không lệch quá xa hành vi của Teacher trên old labels
EMA = bản trung bình động của Student, dùng để giảm nhiễu trước khi freeze
```

Chú ý: Teacher không “biết hết”. Teacher chỉ là snapshot của quá khứ. Nếu Teacher sai, Student có thể học theo cái sai đó.

### Giai đoạn 3: Hiểu prompt trainable

Đọc:

- [[Prompt Tuning]]
- [[Prefix Tuning]]
- [[20 - Research/Papers/Prefix-Tuning - Optimizing Continuous Prompts for Generation]]
- [[20 - Research/Papers/The Power of Scale for Parameter-Efficient Prompt Tuning]]
- [[20 - Research/Papers/P-Tuning v2 - Prompt Tuning Can Be Comparable to Fine-tuning Universally Across Scales and Tasks]]

Kết quả cần đạt: phân biệt được hard prompt, soft prompt, prefix tuning, prompt pool, verbalizer, và LoRA.

### Giai đoạn 4: Hiểu prompt continual learning

Đọc:

- [[20 - Research/Papers/Learning to Prompt for Continual Learning]]
- [[20 - Research/Papers/DualPrompt - Complementary Prompting for Rehearsal-free Continual Learning]]
- [[20 - Research/Papers/CODA-Prompt - Continual Decomposed Attention-based Prompting for Rehearsal-Free Continual Learning]]
- [[20 - Research/Papers/Hierarchical Decomposition of Prompt-Based Continual Learning - Rethinking Obscured Sub-optimality]]
- [[20 - Research/Papers/Consistent Prompting for Rehearsal-Free Continual Learning]]

Kết quả cần đạt: hiểu vì sao prompt selection có thể sai ở test time, vì sao cần tách task identity inference và within-task prediction, và vì sao prompt consistency là vấn đề thật.

### Giai đoạn 5: Quay lại thiết kế đề tài

Sau khi đọc bốn giai đoạn trên, mới nên chốt:

- `Prompt Tree` học theo task hay học bằng clustering relation prototypes?
- routing dùng hard top-1, top-k, hay soft weighted path?
- classifier đầu tiên dùng NCM/prototype hay verbalizer?
- KD distill logits, prototype similarity, hay routing distribution?
- EMA dùng cho toàn bộ trainable parameters hay chỉ prompt/prototype head?

## Kế hoạch điều chỉnh đến 2027-04-30

Trạng thái thực tế ở **tuần 4**: đã đọc xong bốn paper lõi ConPL, CPL, WAVE-CRE và WAVE++, và **ngày 2026-09-05 phải có** research matrix, RQ và protocol spec từ bốn paper này. Vì quỹ thời gian là **2-3 giờ/ngày**, kế hoạch sau ngày 05/09 chuyển ngay sang dataset pipeline/evaluator, không kéo dài thêm giai đoạn literature artifact.

Các note theo dõi chi tiết:

- [[30 - Projects/Research Projects/Continual Relation Extraction with Task-Aware Prompt Adaptation/Timeline cá nhân đến 2027-04-30]]
- [[30 - Projects/Research Projects/Continual Relation Extraction with Task-Aware Prompt Adaptation/Reading Queue và Paper Decisions]]
- [[30 - Projects/Research Projects/Continual Relation Extraction with Task-Aware Prompt Adaptation/Experiment Matrix và Metrics]]
- [[30 - Projects/Research Projects/Continual Relation Extraction with Task-Aware Prompt Adaptation/Weekly Tracker]]

### Timeline rút gọn

| Thời gian | Trọng tâm | Deliverable |
|---|---|---|
| 2026-09-05 | Chuyển 4 paper đã đọc thành matrix/RQ/protocol | [[30 - Projects/Research Projects/Continual Relation Extraction with Task-Aware Prompt Adaptation/Literature Matrix v1, RQ và Protocol Spec]] |
| 2026-09-06 đến 2026-09-20 | Dataset pipeline và evaluator | FewRel loader, TACRED access check, task-order files, performance matrix |
| 2026-09-21 đến 2026-10-04 | Baseline tối thiểu | Sequential FT, Joint Training, prototype sanity |
| 2026-10-05 đến 2026-10-25 | ConPL/CPL reproduction tối thiểu | 1 seed FewRel, mismatch log nếu có |
| 2026-10-26 đến 2026-11-08 | Closest prompt/task-aware comparator | WAVE-CRE/WAVE++ hoặc EoE smoke run |
| 2026-11-09 đến 2026-11-29 | Proposed scaffold | P0 shared prompt, P1 oracle-task prompt, P2 learned router |
| 2026-11-30 đến 2026-12-20 | TAPTA minimal | P3 prototype router, P4 Prompt Tree/soft routing, first ablation |
| 2026-12-21 đến 2027-01-03 | Architecture freeze | Design decision memo, không thêm module mới |
| 2027-01-04 đến 2027-02-28 | Full experiments | FewRel/TACRED runs, ablation, router analysis, memory/latency |
| 2027-03-01 đến 2027-03-07 | Result freeze | Final tables/figures |
| 2027-03-08 đến 2027-04-30 | Writing/finalization | Full draft, near-final, reproducibility package |

### Mốc kết quả tối thiểu mới

- **2026-09-05:** có research matrix, RQ A-D và protocol spec từ bốn paper đã đọc.
- **2026-09-20:** evaluator skeleton chạy được.
- **2026-10-04:** có lower/upper baseline cơ bản.
- **2026-11-08:** có ít nhất một closest prompt/task-aware comparator smoke run.
- **2026-12-20:** có pilot cho prototype routing/Prompt Tree.
- **2027-01-03:** architecture freeze.
- **2027-02-28:** bảng chính và ablation chính gần xong.
- **2027-04-30:** hoàn tất luận văn/paper draft và artifact tái lập.

### Phần chuyển từ PDF sang note con

- Research questions, experiment matrix, metric và config skeleton đã tách sang [[30 - Projects/Research Projects/Continual Relation Extraction with Task-Aware Prompt Adaptation/Experiment Matrix và Metrics]].
- Gantt/sprint, milestone cứng và nhịp 2-3 giờ/ngày đã tách sang [[30 - Projects/Research Projects/Continual Relation Extraction with Task-Aware Prompt Adaptation/Timeline cá nhân đến 2027-04-30]].
- Danh sách paper bổ sung và decision template đã tách sang [[30 - Projects/Research Projects/Continual Relation Extraction with Task-Aware Prompt Adaptation/Reading Queue và Paper Decisions]].
- Weekly report template và checklist theo giai đoạn đã tách sang [[30 - Projects/Research Projects/Continual Relation Extraction with Task-Aware Prompt Adaptation/Weekly Tracker]].

## Chiến lược để đủ thuyết phục

### Không nên claim

- Không claim hierarchy prompt là hoàn toàn mới, vì đã có H-Prompts và các hướng hierarchical prompt khác.
- Không claim rehearsal-free nếu vẫn dùng prototype/statistics/teacher; nên nói rõ `raw-data-free` hoặc `no exemplar replay`.
- Không claim inference $O(1)$ tuyệt đối; chỉ nói số lần forward qua PLM gần hằng số.

### Nên claim

- Prompt Tree được thiết kế riêng cho Continual Relation Extraction, không chỉ class-incremental vision.
- Prototype-guided soft routing thay thế hard task predictor/cascade voting.
- Phân cấp root-internal-leaf cho phép đo riêng lỗi task-level routing và relation-level prediction.
- EMA Teacher là regularizer phụ, không phải contribution chính.

### Ablation bắt buộc

| Ablation | Nếu thiếu thì reviewer sẽ hỏi gì? |
|---|---|
| Flat prompt pool vs Prompt Tree | Tree có thật sự cần không? |
| Hard routing vs soft routing | Weighted composition có hơn argmax route không? |
| No prototype vs leaf prototype vs internal+leaf prototype | Prototype hierarchy có đóng góp gì? |
| No KD vs KD | Teacher có giúp chống quên không? |
| Student snapshot Teacher vs EMA Teacher | EMA có thật sự hơn snapshot cuối task không? |
| Metric classifier vs verbalizer | Verbalizer có cần thiết hay chỉ làm phức tạp? |

## Phiên bản paper nên hướng tới

### Version an toàn cho luận văn

**Prompt Tree + Prototype Soft Routing + KD**, không dùng LoRA và verbalizer ở bản đầu.

Lý do: ít module hơn, dễ debug, dễ giải thích, ablation sạch.

### Version có cơ hội paper hơn

**Prompt Tree + Prototype Soft Routing + constant-PLM-forward inference**, so với EoE/WAVE++ về:

- final accuracy;
- forgetting;
- task routing accuracy;
- inference forward passes;
- memory footprint.

Thông điệp paper: không nhất thiết thắng tuyệt đối mọi accuracy, nhưng nếu giữ accuracy cạnh tranh và giảm cascade inference cost thì vẫn có câu chuyện tốt.

## Gap nghiên cứu mà đề tài nhắm tới

Từ bốn paper ConPL, CPL, WAVE-CRE và WAVE++, đề tài nên bám vào bốn gap rõ nhất:

1. **Routing theo task vẫn là bottleneck:** WAVE-CRE cần learned task predictor; WAVE++ dùng cascade voting nhưng inference chậm hơn. Cần routing mềm, phân cấp, ít forward pass hơn.
2. **Một prototype hoặc một Gaussian/relation quá nghèo:** ConPL dùng một prototype/relation; WAVE/WAVE++ dùng Gaussian assumption. Cần prototype memory có cấu trúc phân cấp hoặc đa mức.
3. **Prompt adaptation chưa gắn chặt với cấu trúc relation:** WAVE dùng prompt pool theo task; chưa tận dụng rõ quan hệ cha-con hoặc nhóm relation trong ontology/prototype tree.
4. **Stability của shared modules chưa được tách sạch:** prompt isolation giúp representation, nhưng classifier/verbalizer vẫn có thể quên. Student-EMA-Teacher có thể là cơ chế ổn định hóa thêm.

## Đề xuất lõi

### Tên phương pháp tạm

**TAPTA: Task-Aware Prompt Tree Adaptation**

Tên này nhấn vào ba thứ nên là contribution chính:

- `Task-Aware`: mô hình biết task boundary khi training và dùng thông tin này để mở rộng cây.
- `Prompt Tree`: prompt không phải một vector phẳng mà nằm trên cây root-internal-leaf.
- `Adaptation`: chỉ cập nhật LoRA/prompt/verbalizer/prototype head, backbone giữ frozen.

### Thành phần mô hình

| Thành phần | Vai trò | Nguồn cảm hứng | Cần ablation |
|---|---|---|---|
| Frozen PLM Backbone | Encoder nền, giữ tri thức ngôn ngữ chung | CPL, WAVE | frozen vs fine-tune nhẹ |
| LoRA hoặc adapter nhỏ | Plasticity để học task mới | PEFT | có/không LoRA |
| Prompt Tree | Lưu prompt theo root/internal/leaf | WAVE prompt pool + hierarchy mới | flat prompt pool vs tree |
| PrototypeMemory | Lưu leaf prototypes và internal prototypes | ConPL | one prototype vs tree prototype |
| Verbalizer Head | Map hidden state sang relation labels | prompt-based RE | verbalizer vs metric classifier |
| Teacher Model | Snapshot frozen của task trước | distillation CL | KD vs no KD |
| EMA Model | Làm mượt Student trước khi freeze thành Teacher | mean teacher | Teacher từ Student cuối vs EMA |

## Training flow đề xuất

### Bước 1: Khởi tạo task mới

Khi task $t$ xuất hiện:

- Thêm leaf nodes tương ứng với relation mới vào `Prompt Tree`.
- Nếu có grouping/ontology, gắn leaf vào internal node phù hợp; nếu không có, tạo internal node theo clustering prototype ban đầu.
- Mở rộng `Verbalizer Head` cho relation mới.
- Tính prototype khởi tạo cho relation mới bằng Student ở chế độ `no_grad`.
- Với $t=1$, đồng bộ EMA từ Student; với $t>1$, giữ EMA từ trạng thái cuối task trước.

Điểm cần chỉnh so với bản nháp: prototype khởi tạo không nên gọi là tránh `Gradient Shock` nếu chưa có thực nghiệm đo gradient. Nên viết thận trọng hơn: **giúp đặt prototype ban đầu gần phân bố feature của task mới, làm routing và loss ổn định hơn ở đầu task**.

### Bước 2: Huấn luyện online trong task

Với mini-batch $(x,y)$:

1. Student forward qua prompt tree hiện tại để lấy logits trên toàn bộ relation đã thấy.
2. Teacher forward chỉ dùng khi $t>1$, lấy logits hoặc distribution trên old relations.
3. Tính loss:

$$
L = L_{CE}^{new} + \lambda_{KD}L_{KD}^{old} + \lambda_{proto}L_{proto} + \lambda_{route}L_{route}
$$

Trong đó:

- $L_{CE}^{new}$ học relation mới và các sample hiện tại.
- $L_{KD}^{old}$ giữ phân phối của Teacher trên old relations.
- $L_{proto}$ kéo representation về leaf prototype đúng và đẩy khỏi prototype gần nghĩa.
- $L_{route}$ khuyến khích routing đi qua nhánh đúng khi task id có sẵn ở training.

Sau optimizer step:

$$
\theta_{EMA} \leftarrow \alpha \theta_{EMA} + (1-\alpha)\theta_{Student}
$$

### Bước 3: Cập nhật prototype memory

Sau mỗi epoch hoặc cuối task:

- Cập nhật leaf prototype bằng mean feature hoặc EMA feature mean.
- Cập nhật internal prototype bằng weighted average từ children:

$$
p_{internal} =
\frac{\sum_{c\in children} n_c p_c}{\sum_{c\in children} n_c}
$$

- Freeze prototype của old relations hoặc chỉ cập nhật bằng EMA rất nhỏ để tránh drift.

### Bước 4: Chốt task

Cuối task:

$$
\theta_{Teacher} \leftarrow \theta_{EMA}
$$

Sau đó khóa gradient cho Teacher. Teacher của task $t$ trở thành mốc chưng cất khi học task $t+1$.

## Inference flow đề xuất

Mục tiêu inference nên viết là **task-agnostic at test time**, không phải hoàn toàn task-free. Nghĩa là test không cung cấp task id, nhưng mô hình vẫn dùng cấu trúc task đã học trong Prompt Tree.

1. Input sentence với hai entity được đưa qua encoder nhẹ để lấy vector định tuyến $h$.
2. Tính similarity giữa $h$ và internal prototypes.
3. Tính tiếp similarity giữa $h$ và leaf prototypes.
4. Tạo path weights bằng tổng log-probability rồi softmax:

$$
\log w_j = \log P(n_i\mid root,x) + \log P(r_j\mid n_i,x)
$$

5. Sinh prompt cuối bằng weighted composition:

$$
P_{final} = \sum_j w_j P_{path_j}
$$

6. Chạy PLM với prompt cuối và dự đoán relation bằng verbalizer hoặc metric classifier.

Điểm cần sửa trong bản nháp inference: claim `O(1)` chỉ đúng với **số lần forward qua PLM** nếu luôn chạy 2 forward pass. Tổng chi phí vẫn phụ thuộc số internal nodes, leaf nodes hoặc số path được xét. Nên viết là:

> Phương pháp giữ số lần forward qua PLM gần như hằng số, trong khi chi phí routing là các phép similarity nhẹ và có thể giảm bằng top-k pruning.

## Các điểm cần quyết định sớm

### 1. Dùng `[CLS]` hay `[MASK]`?

Không nên để training dùng `[MASK]` còn routing dùng `[CLS]` mà không giải thích. Có hai lựa chọn sạch:

- **Lựa chọn A:** dùng `[MASK]` representation cho cả prototype, routing và verbalizer.
- **Lựa chọn B:** dùng `[CLS]` cho routing, `[MASK]` cho prediction, nhưng thêm projection/alignment loss để hai không gian nhất quán.

Khuyến nghị ban đầu: chọn **A** để MVP đơn giản và dễ bảo vệ hơn.

### 2. Verbalizer hay metric classifier?

Verbalizer đẹp về mặt prompt learning nhưng dễ gặp vấn đề label word không tự nhiên, multi-token label, và mismatch giữa relation name với vocabulary. Metric classifier/NCM dễ kiểm soát hơn cho FewRel/TACRED.

Khuyến nghị triển khai dần:

1. MVP dùng metric classifier trên prototypes.
2. Sau đó thêm verbalizer head như biến thể.
3. So sánh `prototype-only`, `verbalizer-only`, và `hybrid`.

### 3. Có cần LoRA ngay không?

Nếu thêm cùng lúc LoRA, Prompt Tree, PrototypeMemory, Teacher, EMA, Verbalizer thì khó biết thành phần nào thật sự đóng góp.

Khuyến nghị:

1. Phase đầu chỉ train prompt tree + classifier/prototypes, backbone frozen.
2. Phase sau thêm LoRA.
3. LoRA phải có ablation riêng.

## Lộ trình triển khai dần

### Phase 0: Protocol và baseline

Mục tiêu: tái lập pipeline CRE tối thiểu trên FewRel/TACRED split.

- Chuẩn hóa task split, seeds, metrics.
- Chạy baseline NCM/prototype đơn giản.
- Báo `average accuracy`, `final accuracy`, `forgetting`, `old/new accuracy`.

Kết quả mong muốn: có bảng baseline đáng tin trước khi thêm module mới.

### Phase 1: Flat Task Prompt Adapter

Mục tiêu: kiểm tra tên đề tài ở dạng đơn giản nhất.

- Mỗi task có một prompt vector hoặc prompt pool nhỏ.
- Không dùng tree.
- Không dùng EMA/KD.
- Routing ở inference bằng nearest task prototype.

Ablation: no prompt vs task prompt.

### Phase 2: Prompt Tree + PrototypeMemory

Mục tiêu: đóng góp chính bắt đầu rõ.

- Thêm root/internal/leaf prompts.
- Leaf prototype cho relation.
- Internal prototype là weighted mean từ leaf prototypes.
- Inference dùng hierarchical soft routing.

Ablation:

- flat prompt pool vs prompt tree;
- hard routing vs soft routing;
- leaf-only prototype vs internal+leaf prototype.

### Phase 3: Knowledge Distillation từ Teacher

Mục tiêu: xử lý forgetting ở old relations mà prompt/prototype chưa giữ được.

- Freeze Teacher sau mỗi task.
- KD trên old relation logits hoặc old prototype similarity.
- Không dùng EMA trước, Teacher lấy trực tiếp từ Student cuối task.

Ablation: no KD vs KD.

### Phase 4: EMA Teacher

Mục tiêu: kiểm tra EMA có thật sự giúp hơn snapshot cuối task không.

- Duy trì EMA trong task.
- Cuối task freeze EMA thành Teacher.
- So với Teacher từ Student cuối.

Ablation: Student snapshot teacher vs EMA teacher; sweep $\alpha \in \{0.9, 0.99, 0.999\}$.

### Phase 5: Verbalizer và label semantics

Mục tiêu: đưa prompt learning gần đề tài hơn nhưng vẫn kiểm soát rủi ro.

- Thêm verbalizer head hoặc label word mapping.
- Nếu label nhiều token, dùng trainable verbalizer embeddings thay vì ép về vocab token đơn.
- Có thể thêm relation description embedding giống WAVE++ nhưng không dùng LLM ở phase đầu.

Ablation: metric classifier vs verbalizer vs hybrid.

## Giả thuyết nghiên cứu

### H1: Prompt Tree giảm lỗi routing so với flat task predictor

Nếu đúng, model nên có task routing accuracy tốt hơn hoặc relation accuracy tốt hơn ở old/new mixed test.

### H2: Soft routing ổn định hơn hard routing

Nếu đúng, soft routing sẽ giảm lỗi khi input nằm gần ranh giới giữa hai relation/task.

### H3: PrototypeMemory phân cấp giảm forgetting hơn prototype phẳng

Nếu đúng, internal prototypes giữ cấu trúc relation group tốt hơn và làm old relation accuracy giảm chậm hơn qua task.

### H4: EMA Teacher cải thiện stability so với Teacher snapshot cuối task

Nếu đúng, EMA giảm variance qua seeds và giảm forgetting, đặc biệt ở few-shot setting.

## Bảng thí nghiệm tối thiểu

| Experiment | Model | Mục tiêu |
|---|---|---|
| E0 | Frozen BERT + NCM | baseline metric đơn giản |
| E1 | E0 + task prompt | kiểm tra prompt adaptation |
| E2 | E1 + prompt tree | kiểm tra hierarchy |
| E3 | E2 + soft routing | kiểm tra task-agnostic inference |
| E4 | E3 + KD | kiểm tra chống quên |
| E5 | E4 + EMA Teacher | kiểm tra ổn định |
| E6 | E5 + verbalizer | kiểm tra prompt/verbalizer semantics |

## Rủi ro phản biện và cách viết lại

| Claim bản nháp | Rủi ro | Cách viết an toàn hơn |
|---|---|---|
| Teacher là mỏ neo giữ toàn bộ tri thức cũ | Teacher vẫn có thể sai hoặc bias từ task trước | Teacher cung cấp regularization signal cho old-label distribution |
| EMA là phiên bản hoàn hảo nhất | Quá mạnh, không có bảo chứng | EMA là phiên bản làm mượt cập nhật Student, kỳ vọng giảm nhiễu |
| Inference O(1) | Sai nếu tính routing trên nhiều node/path | Số forward qua PLM gần hằng số; routing là similarity nhẹ và có thể top-k |
| Verbalizer chứa tất cả label words | Label có thể multi-token hoặc không khớp vocab | Verbalizer là trainable label projection hoặc mapping có kiểm soát |
| Task-agnostic hoàn toàn | Training vẫn biết task boundary | Task-agnostic at inference; task-aware during training |

## Đóng góp nên viết trong luận văn

1. Đề xuất kiến trúc Prompt Tree cho CRE, trong đó prompt được tổ chức theo root-internal-leaf để mô hình hóa tri thức theo task/relation.
2. Đề xuất prototype-guided soft routing để chọn prompt mà không cần oracle task id tại inference.
3. Kết hợp PrototypeMemory phân cấp với distillation từ EMA Teacher để giảm catastrophic forgetting.
4. Thiết kế protocol ablation tách riêng đóng góp của prompt adaptation, routing, prototype hierarchy, KD và EMA.

## Việc cần làm tiếp theo

- [ ] Chốt dataset/protocol: FewRel, TACRED, số task, số shot, seeds.
- [ ] Chọn representation thống nhất: `[MASK]` hoặc `[CLS]`.
- [ ] Chọn classifier MVP: prototype/NCM trước, verbalizer sau.
- [ ] Viết pseudo-code training loop.
- [ ] Viết pseudo-code inference loop.
- [ ] Thiết kế bảng ablation và metric.
- [ ] Sau khi có protocol, chuyển sang implementation baseline.
