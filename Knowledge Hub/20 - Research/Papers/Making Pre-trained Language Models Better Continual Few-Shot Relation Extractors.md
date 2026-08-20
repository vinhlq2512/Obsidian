---
type: paper
status: unread
title: "Making Pre-trained Language Models Better Continual Few-Shot Relation Extractors"
authors:
  - Shengkun Ma
  - Jiale Han
  - Yi Liang
  - Bo Cheng
year: 2024
venue: "Proceedings of the 2024 Joint International Conference on Computational Linguistics, Language Resources and Evaluation (LREC-COLING 2024), 10970-10983"
url: "https://aclanthology.org/2024.lrec-main.957/"
pdf: "[[Making Pre-trained Language Models Better Continual Few-Shot Relation Extractors.pdf]]"
zotero_key:
citekey: ma-etal-2024-making
doi:
arxiv: "2402.15713"
code: "https://github.com/mashengkun/CPL"
topic:
  - continual few-shot relation extraction
  - continual learning
  - prompt learning
  - contrastive learning
  - data augmentation
priority: medium
reading_status: not-started
rating:
related_concepts:
  - "[[04 - Concepts/Continual Learning|Continual Learning]]"
  - "[[Catastrophic Forgetting]]"
  - "[[Continual Relation Extraction]]"
  - "[[Continual Few-Shot Relation Extraction]]"
  - "[[Replay in Continual Learning]]"
  - "[[Few-shot Learning]]"
  - "[[Contrastive Learning]]"
  - "[[Data Augmentation]]"
  - "[[Relation Extraction]]"
  - "[[Masked Language Modeling]]"
created_at: 2026-08-13
updated_at: 2026-08-13
tags:
  - paper
  - continual-learning
  - continual-relation-extraction
  - few-shot-learning
  - relation-extraction
---

# Making Pre-trained Language Models Better Continual Few-Shot Relation Extractors

## Tóm tắt một câu

- Paper đề xuất **Contrastive Prompt Learning (CPL)**: biểu diễn relation bằng hidden state tại `[MASK]` trong một hybrid prompt, huấn luyện embedding bằng margin-based contrastive loss, replay một exemplar thật cho mỗi relation cùng dữ liệu do GPT-3.5 sinh, rồi dự đoán bằng Nearest-Class-Mean để giảm đồng thời [[Catastrophic Forgetting]] và overfitting trong [[Continual Few-Shot Relation Extraction]].

## Nguồn

- PDF gốc: [[Making Pre-trained Language Models Better Continual Few-Shot Relation Extractors.pdf]]
- ACL Anthology: [2024.lrec-main.957](https://aclanthology.org/2024.lrec-main.957/)
- arXiv: [2402.15713](https://arxiv.org/abs/2402.15713)
- Code: [mashengkun/CPL](https://github.com/mashengkun/CPL)
- Citekey: `ma-etal-2024-making`
- DOI proceedings: ACL Anthology không công bố DOI; `10.48550/arXiv.2402.15713` chỉ là DOI DataCite của bản arXiv, vì vậy property `doi` được để trống.
- Venue đầy đủ: *Proceedings of the 2024 Joint International Conference on Computational Linguistics, Language Resources and Evaluation (LREC-COLING 2024)*, Torino, Italia, 20-25/05/2024, trang 10970-10983, ELRA and ICCL.

## Trạng thái và phạm vi ghi chú

> [!note]
> Frontmatter vẫn giữ `status: unread` và `reading_status: not-started` theo trạng thái quản lý paper hiện tại. Nội dung bên dưới là bản phân tích có đối chiếu đủ 14 trang PDF; nó không tự động thay đổi trạng thái đọc cá nhân hoặc rating.

## Vấn đề paper giải quyết

### Continual Few-Shot Relation Extraction là gì?

[[Relation Extraction]] thông thường giả định train và test dùng cùng một label space. Trong thực tế, relation mới xuất hiện theo thời gian và dữ liệu gắn nhãn cho relation mới thường rất ít. [[Continual Few-Shot Relation Extraction]] kết hợp hai ràng buộc:

- Model phải học tuần tự các relation mới.
- Model không được quên các relation đã học.
- Các task mới chỉ có vài mẫu có nhãn cho mỗi relation.

Paper formalize một chuỗi task:

$$
\mathcal{T}=\{\mathcal{T}^1,\mathcal{T}^2,\ldots,\mathcal{T}^n\}
$$

Mỗi task $\mathcal{T}^k$ có relation set $R^k$ riêng; relation giữa các task là disjoint. Một instance gồm câu $x$, head entity $e_h$, tail entity $e_t$ và relation label. Sau khi học xong task $k$, dữ liệu của task đó không còn được dùng trực tiếp ở các task sau, ngoại trừ số exemplar được giữ trong replay memory.

Thiết lập few-shot của paper không làm mọi task đều few-shot:

- Task đầu có 100 mẫu cho mỗi relation.
- Từ task thứ hai trở đi mới dùng 5-shot hoặc 10-shot.
- Model được đánh giá trên test data của **tất cả relation đã thấy**, không chỉ relation của task hiện tại.

### Hai vấn đề trung tâm

1. **Catastrophic forgetting:** cập nhật encoder trên relation mới làm representation của relation cũ dịch chuyển hoặc mất khả năng phân biệt.
2. **Overfitting:** với 5-10 mẫu cho mỗi relation, model dễ học noise, lexical shortcut hoặc cấu trúc quá riêng của training examples.

### Research gap

Các hướng trước đó dùng embedding-space regularization, knowledge distillation, prototype learning, memory replay hoặc data augmentation. Theo paper, các phương pháp này chưa khai thác đủ knowledge implicit trong pretrained language model để đồng thời:

- học biểu diễn có thể chuyển từ relation cũ sang relation mới;
- phân biệt các relation gần nghĩa khi dữ liệu rất ít;
- làm replay memory đa dạng hơn.

Novelty claim cần hiểu đúng phạm vi: paper tự nhận là lần đầu khảo sát prompt technology trong **CFRE**; prompt-based framework cho continual relation extraction nói chung đã tồn tại trước đó.

## Đóng góp chính

- Đề xuất framework **Contrastive Prompt Learning (CPL)** kết hợp prompt representation, margin-based contrastive learning và memory augmentation.
- Dùng hybrid prompt không có verbalizer để đưa RE gần masked-language pretraining hơn và lấy hidden state tại `[MASK]` làm relation representation.
- Đề xuất margin-based contrastive objective nhằm điều chỉnh contribution của positive/negative pairs theo similarity và nhấn mạnh hard samples.
- Dùng GPT-3.5-turbo để sinh thêm replay examples từ relation description và một exemplar thật.
- Dùng Nearest-Class-Mean thay cho softmax head cố định, phù hợp hơn khi class set tăng dần.
- Báo cáo kết quả tốt nhất trong nhóm continual baselines được so sánh trên FewRel và TACRED ở cả 5-shot lẫn 10-shot.

## Mental model tổng thể

```text
Task mới
-> Hybrid prompt đưa entity và [MASK] vào input
-> BERT biến [MASK] thành relation embedding
-> MCL học geometry phân biệt relation mới
-> K-means chọn exemplar thật cho từng relation
-> GPT-3.5 sinh thêm replay samples
-> MCL replay relation cũ
-> NCM so test embedding với prototype của mọi relation đã thấy
```

Ba thành phần xử lý ba lớp vấn đề khác nhau:

| Thành phần | Vai trò chính | Vấn đề nhắm tới |
| --- | --- | --- |
| Hybrid prompt | Căn task RE với pretraining objective và tạo relation representation tổng quát | Forgetting, transfer sang relation mới |
| Margin-based contrastive learning | Làm embedding phân biệt hơn, chú ý hard pairs | Overfitting, relation gần nghĩa |
| Memory augmentation | Tăng support set cho replay từ một exemplar thật | Sparse replay data |

## Phương pháp

### 1. Hybrid prompt representation

Vanilla prompt classification thường có:

- **Template:** biến input thành cloze-style input.
- **Verbalizer:** map mỗi label sang một token hoặc cụm token.

CPL bỏ verbalizer. Với câu $x$, head entity $e_h$ và tail entity $e_t$, template là:

$$
T(x)=x.[v_{0:n_0-1}]e_h[v_{n_0:n_1-1}][MASK]
[v_{n_1:n_2-1}]e_t[v_{n_2:n_3-1}]
$$

Trong đó:

- Bốn nhóm $[v]$ là continuous learnable prompt vectors.
- Entity mentions là phần hard structure cung cấp prior cho RE.
- `[MASK]` nằm giữa hai entity và đại diện cho relation giữa chúng.
- Cấu hình chính dùng 4 nhóm prompt, mỗi nhóm dài 3 token, tức 12 learnable prompt tokens.
- Prompt vectors được random initialization.

Embedding sequence được đưa qua encoder $E$; hidden state của `[MASK]` là relation representation:

$$
m=Enc(Emb(T(x)))
$$

Không có verbalizer nghĩa là model không phải dự đoán relation name như một vocabulary token. Nó học geometry của relation embedding, sau đó dùng metric classifier ở inference.

### Vì sao hybrid thay vì hard-only hoặc soft-only?

- Entity marker chỉ cho model biết vị trí entity nhưng không đưa task về masked-language form.
- Hard prompt có expert prior tốt nhưng phải thiết kế thủ công.
- Soft-only prompt linh hoạt nhưng random vectors khó hội tụ với vài mẫu.
- Hybrid prompt giữ entity structure làm anchor và để continuous vectors tự thích nghi.

Figure 3 cho thứ tự kết quả sau task cuối: **hybrid > hard > entity marker > soft-only** trên cả FewRel và TACRED. Figure không in số trên từng bar nên chỉ nên dùng cho ranking, không suy số chính xác từ chiều cao cột.

### 2. Margin-based contrastive learning

Với normalized feature $z_i$:

$$
s_{i,p}=z_i^\top z_p,\qquad s_{i,n}=z_i^\top z_n
$$

Trong đó $p$ là positive sample cùng relation, còn $n$ là negative sample khác relation.

Normalization term:

$$
Z(i)=
\sum_{p\in P(i)}\exp\left(\frac{\alpha_{i,p}s_{i,p}}{\tau}\right)
+
\sum_{n\in N(i)}\exp\left(\frac{\alpha_{i,n}s_{i,n}}{\tau}\right)
$$

Similarity-dependent relaxation factors:

$$
\alpha_{i,p}=m+k s_{i,p},\qquad
\alpha_{i,n}=1-m+k s_{i,n}
$$

Batch loss:

$$
\mathcal{L}_{MCL}
=
\sum_{i\in I}\frac{-1}{|P(i)|}
\sum_{p\in P(i)}
\log
\frac{\exp(\alpha_{i,p}s_{i,p}/\tau)}{Z(i)}
$$

Hyperparameters chính:

- Margin $m=0.3$.
- Normalization constant $k=0.5$.
- Temperature $\tau=0.1$.

Theo paper, $\alpha_{i,p}$ và $\alpha_{i,n}$ làm contribution và decision boundary thay đổi theo similarity, giúp model tập trung hơn vào hard pairs. Mục tiêu cuối là:

- positive samples cùng relation gần nhau;
- negative samples khác relation tách nhau;
- feature space đồng đều hơn supervised contrastive learning;
- giảm nhầm lẫn giữa relation gần nghĩa như `child` và `father`.

### Feature bucket cho contrastive training

Supervised contrastive learning thường cần batch lớn để có đủ positive và negative pairs. CPL tránh tăng batch bằng một feature bucket $C^k$:

1. Encode current training set thành features và lưu vào $C^k$.
2. Với mỗi anchor trong batch, sample một tập features từ bucket để tạo $S_i$.
3. Tính MCL trên $S_i$.
4. Sau backpropagation, refresh các entries tương ứng trong $C^k$ bằng feature mới.

`contrastive_sample_number` được đặt là 500. Bucket này là auxiliary memory trong current-task optimization, không phải episodic memory dùng qua nhiều task.

### 3. Ba loại memory trong CPL

| Ký hiệu / tên | Chứa gì? | Tồn tại bao lâu? | Dùng để làm gì? |
| --- | --- | --- | --- |
| $C^k$ / feature bucket | Features của current task | Trong khi train task $k$ | Tạo nhiều contrastive pairs mà không cần batch lớn |
| $\hat{\mathcal M}$ / replay memory | Exemplar thật được chọn cho từng relation | Qua các task | Giữ evidence thật của relation cũ và tạo prototype |
| $\mathcal A$ / augmented samples | Structured examples do GPT-3.5 sinh | Trong replay training | Mở rộng support set quanh exemplar thật |

Việc tách ba memory giúp tránh nhầm rằng CPL chỉ có một replay buffer hoặc generated samples được dùng trực tiếp làm class prototype.

### 4. Representative memory sampling

Sau current-task training:

1. Encode samples của từng relation.
2. Chạy K-means với $L$ clusters cho mỗi relation.
3. Trong mỗi cluster, chọn sample thật gần centroid nhất.
4. Lưu sample đó vào replay memory.

Thí nghiệm chính dùng $L=1$, nên mỗi relation chỉ giữ một exemplar thật gần mean embedding nhất.

### 5. GPT-3.5 memory augmentation

Với mỗi historical relation, prompt generation gồm:

- mô tả format của một RE example;
- relation name;
- semantic relation explanation;
- một demonstration thật có context, head entity và tail entity;
- yêu cầu sinh $g$ examples mới cùng relation.

Paper dùng `GPT-3.5-turbo`, temperature `0`, sinh:

- 2 samples/relation cho FewRel;
- 5 samples/relation cho TACRED.

Output được parse thành structured dataset $\mathcal A$, rồi ghép với real memory để replay bằng MCL.

#### Vì sao demonstration quan trọng?

Case study với relation `child` cho thấy relation name và description chưa chắc đủ để GPT hiểu đúng hướng head-tail. Khi có exemplar, output đúng relation; khi bỏ exemplar, một output mô tả hai entity là siblings nhưng vẫn gắn nhãn `child`.

Appendix C cũng cho thấy hai failure modes:

- Generated samples lặp nhiều lexical pattern như `mother`, `father`, `son`, `daughter`.
- Có thể tạo câu gần nghĩa về mặt từ vựng nhưng sai relation thật giữa head và tail.

### 6. Hai lượt training ở mỗi task

Prompt parameters $\theta_1$ và encoder parameters $\theta_2$ được khởi tạo từ checkpoint của task trước.

```text
Current-task training
  D_train^k
  -> hybrid prompt
  -> encoder
  -> MCL

Memory construction
  -> K-means exemplar selection
  -> GPT-3.5 augmentation

Memory replay
  real exemplars + generated samples
  -> hybrid prompt
  -> encoder
  -> MCL lần hai
```

Lượt đầu học relation mới. Lượt replay củng cố relation cũ và tránh overfit vào một exemplar/relation.

### 7. Relation prediction bằng Nearest-Class-Mean

Sau contrastive training, prototype của relation $r$ được tính từ real memory:

$$
p_r=\frac{1}{L}\sum_i E(\hat{x}_i^r)
$$

Với test sample $x$:

$$
y^*=\arg\min_r\|E(x)-p_r\|_2
$$

NCM phù hợp class-incremental setting vì:

- không có softmax head với output dimension cố định;
- relation mới chỉ cần thêm prototype;
- inference tận dụng trực tiếp feature space đã được MCL làm discriminative.

Với $L=1$, prototype chỉ dựa trên một exemplar thật, vì vậy chất lượng exemplar selection và stability của encoder đặc biệt quan trọng.

## Experimental protocol

### Datasets và task split

| Dataset | Dữ liệu gốc | Task đầu | Task 2-8 | Setting |
| --- | --- | --- | --- | --- |
| FewRel | 100 relations, 700 examples/relation; thí nghiệm dùng 80 public relations | 10 relations, 100 examples/relation | 10 relations/task, 5 hoặc 10 examples/relation | 10-way 5-shot / 10-way 10-shot |
| TACRED | 106,264 examples; 41 positive relations và `no_relation` | Bỏ `no_relation`; 6 relations, 100 examples/relation | 5 relations/task, 5 hoặc 10 examples/relation | 5-way 5-shot / 5-way 10-shot |

FewRel cân bằng theo relation. TACRED mất cân bằng và gần real-world distribution hơn.

### Evaluation

- Sau task $T^k$, model được đánh giá trên union test sets của mọi relation từ $T^1$ đến $T^k$.
- Metric là overall accuracy.
- Kết quả được average qua 6 rounds.
- Dùng **strict evaluation**: mọi seen relation đều là candidate label.
- Loose protocol chỉ chọn 10 candidate labels không được dùng vì có thể làm task dễ hơn.
- Task orders/random seeds được đặt theo prior CFRE work để tăng khả năng so sánh.

### Baselines

- `Finetune`: train tuần tự không memory; lower bound cho forgetting.
- `Joint-train`: giữ toàn bộ dữ liệu cũ; upper bound phi-continual.
- `RP-CRE`, `CRL`, `CRECL`: continual RE methods, gồm prototype/contrastive approaches.
- `EMAR+ACA`, `InfoCL`: được re-run trong few-shot setting.
- `ERDA`, `SCKD`: CFRE methods có memory và augmentation/distillation.
- `ConPL` không được đưa vào vì paper cho rằng task setting khác.

Một số số liệu được lấy từ Wang et al. (2023), một số do authors re-run; đây là caveat khi so sánh tuyệt đối.

### Implementation details

| Hyperparameter | Giá trị |
| --- | ---: |
| Encoder | BERT-base-uncased |
| PyTorch / Transformers | 1.7.0 / 4.10.0 |
| Batch size | 16 |
| Current-task epochs | 10 |
| Memory replay epochs | 10 |
| Learning rate | $10^{-5}$ |
| Optimizer | Adam |
| Max input length | 256 |
| Hidden/output size | 768 |
| Margin $m$ | 0.3 |
| Normalization $k$ | 0.5 |
| Contrastive temperature $\tau$ | 0.1 |
| Contrastive sample number | 500 |
| Soft prompt initialization | random |
| Soft prompt groups × length | 4 × 3 |
| ChatGPT temperature | 0 |
| Generated samples: FewRel / TACRED | 2 / 5 |

Experiments chạy trên một NVIDIA Tesla P40 24 GB và Intel Xeon Gold 5118; hyperparameters được chọn bằng grid search.

## Kết quả chính

### Accuracy sau task cuối $T^8$

| Setting | Finetune | SCKD | CPL | Joint-train | CPL - SCKD | Gap CPL tới Joint |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| FewRel 5-shot | 9.78 | 62.87 | **64.50** | 70.33 | +1.63 | -5.83 |
| TACRED 5-shot | 7.90 | 51.11 | **57.39** | 58.26 | +6.28 | -0.87 |
| FewRel 10-shot | 10.70 | 66.58 | **67.49** | 74.93 | +0.91 | -7.44 |
| TACRED 10-shot | 8.45 | 53.42 | **58.57** | 61.42 | +5.15 | -2.85 |

Các hiệu số trên là **accuracy points**, không phải relative percentage improvement.

### Trajectory của CPL trong 5-shot

| Dataset | $T^1$ | $T^2$ | $T^3$ | $T^4$ | $T^5$ | $T^6$ | $T^7$ | $T^8$ |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| FewRel | 94.87 | 85.14 | 78.80 | 75.10 | 72.57 | 69.57 | 66.85 | 64.50 |
| TACRED | 86.27 | 81.55 | 73.52 | 68.96 | 63.96 | 62.66 | 59.96 | 57.39 |

### Cách đọc kết quả

- Finetune rơi từ 94.58 xuống 9.78 trên FewRel và từ 88.12 xuống 7.90 trên TACRED, cho thấy sequential fine-tuning không replay bị forgetting rất mạnh.
- CPL không luôn tốt nhất ở $T^1$, đặc biệt trên TACRED, nhưng giữ accuracy tốt hơn qua chuỗi task.
- TACRED 5-shot là kết quả nổi bật nhất: CPL chỉ thấp hơn Joint-training 0.87 điểm khi episodic memory giữ một real exemplar/relation và replay còn được bổ sung 5 synthetic samples/relation do GPT-3.5 sinh. Vì vậy đây không phải kết quả của chỉ một exemplar đơn lẻ.
- Lợi thế trên TACRED lớn hơn FewRel, gợi ý augmentation hữu ích hơn khi data distribution khó và mất cân bằng.
- Tuy vậy paper không báo backward transfer hoặc forgetting score riêng; kết luận giảm forgetting được suy từ accuracy trajectory.

## Ablation study

Final accuracy tại $T^8$ trong 5-shot:

| Biến thể | FewRel | Drop so với CPL | TACRED | Drop so với CPL |
| --- | ---: | ---: | ---: | ---: |
| CPL | 64.50 | - | 57.39 | - |
| Không prompt representation | 51.09 | -13.41 | 42.61 | -14.78 |
| Thay MCL bằng supervised contrastive loss | 61.78 | -2.72 | 54.75 | -2.64 |
| Không generated replay samples | 63.78 | -0.72 | 50.63 | -6.76 |
| Bỏ cả prompt, MCL và generation | 48.29 | -16.21 | 38.06 | -19.33 |

Kết luận an toàn từ ablation:

- Prompt representation là component mạnh và ổn định nhất trên cả hai datasets.
- MCL có contribution dương nhưng nhỏ hơn prompt representation.
- GPT augmentation phụ thuộc dataset: gần như không thêm nhiều trên FewRel nhưng rất quan trọng trên TACRED.
- Các components bổ trợ nhau; không nên quy toàn bộ improvement cho ChatGPT.

## Sensitivity và qualitative analysis

### Prompt format

- Hybrid prompt tốt nhất trên cả hai datasets.
- Hard prompt đứng thứ hai nhưng cần manual expert design.
- Entity marker thấp hơn hybrid đáng kể.
- Soft-only prompt tệ nhất; paper quy nguyên nhân cho random initialization khó hội tụ trong low-resource setting.

Figure 3 không gắn số trực tiếp trên bars, nên chỉ dùng ranking thay vì ghi số ước lượng như số đo chính thức.

### Số generated samples

Figure 5 thử `0, 1, 2, 5, 10` generated samples/relation:

- FewRel đạt tốt nhất quanh 2 samples; tăng lên 5 hoặc 10 làm accuracy giảm.
- TACRED tiếp tục tăng đến 5 samples rồi giảm ở 10.
- Điểm `0` được Table 2 xác nhận là 63.78 trên FewRel và 50.63 trên TACRED.
- Điểm cấu hình được chọn là 64.50 với 2 samples trên FewRel và 57.39 với 5 samples trên TACRED.

Điều này bác bỏ giả định “càng nhiều synthetic data càng tốt”. Noise, lexical monotony và distribution mismatch có thể lấn át lợi ích augmentation.

### Memory size

Figure 6 dùng 10-shot, không data generation, và thay đổi $L\in\{1,2,5,7,10\}$:

- Accuracy tăng rõ khi lưu nhiều exemplar/relation hơn.
- $L=10$ tiến gần Joint-training.
- Kết quả chính dùng $L=1$ để giữ setting tiết kiệm memory và so sánh công bằng với baselines.

### Feature visualization

t-SNE cho thấy MCL tạo clusters đều và tách relation gần nghĩa tốt hơn SCL. Đây chỉ là qualitative visualization; t-SNE không phải bằng chứng định lượng cho global geometry hay generalization.

## Hạn chế

### Hạn chế authors công bố

1. **Time efficiency:** số relation, real memory và generated replay samples tích lũy theo task, nên later-task training ngày càng chậm.
2. **Result stability:** GPT-3.5 có thể trả output khác nhau với cùng input ngay cả khi temperature bằng 0. Authors average 6 rounds nhưng không loại bỏ hoàn toàn variance.

### Hạn chế và assumptions suy ra từ protocol

- CPL không rehearsal-free: vẫn lưu real examples, nên privacy/storage concern chưa biến mất.
- Phụ thuộc external GPT-3.5 API, model version, cost, availability và data handling policy.
- Không có quality filter rõ ràng cho generated samples trước replay.
- Giả định task boundary, entity spans, head-tail orientation, relation name và relation description đều có sẵn.
- Relation sets giữa các task disjoint; không xử lý relation tái xuất hiện hoặc label semantics thay đổi.
- Bỏ `no_relation`, nên chưa giải quyết unknown/open-set rejection trong production RE.
- Task đầu có 100 samples/relation; chưa chứng minh robustness khi mọi task đều few-shot.
- Chỉ thử BERT-base trên hai English sentence-level datasets; chưa có multilingual, document-level RE hoặc noisy upstream NER.
- Chỉ dùng accuracy; không báo macro-F1, backward transfer, explicit forgetting, confidence interval, statistical significance, latency hoặc API cost.
- Some baseline results được trích từ prior work trong khi một số khác được re-run.
- NCM với $L=1$ khiến prototype rất nhạy với exemplar và representation drift.

## Discrepancies và evidence caveats

> [!warning] Các điểm cần giữ khi tái lập hoặc trích dẫn
> Không nên làm phẳng các điểm dưới đây thành kết luận chắc chắn; chúng là bất nhất hoặc thiếu chi tiết ngay trong paper.

1. **Ablation MCL:** prose ghi improvement `2.27%` và `2.26%`, nhưng Table 2 cho phép tính trực tiếp $64.50-61.78=2.72$ và $57.39-54.75=2.64$ accuracy points. Note này ưu tiên số trong bảng.
2. **Dấu của loss:** Eq. 4 viết log-ratio chưa có dấu âm; dấu âm chỉ xuất hiện rõ trong batch loss Eq. 7. Khi reproduce nên kiểm tra implementation chính thức.
3. **NCM indexing:** Eq. 9 viết tổng từ $i=0$ đến $L$ nhưng chia cho $L$, có vẻ là off-by-one notation; diễn giải hợp lý là average đúng $L$ exemplars.
4. **Memory size:** text nói $L=10$ chứa “all previous samples”, nhưng protocol cho task đầu 100 samples/relation. Cách xử lý task đầu trong phát biểu này không được giải thích đủ.
5. **Randomness:** Table 5 chỉ ghi `seed: 100`, trong khi main text nói average 6 rounds và dùng task-order seeds của prior work. Mapping giữa config seed và sáu rounds không rõ.
6. **Generated-data stability:** temperature 0 không đảm bảo deterministic output và API model có thể đổi theo thời gian.
7. **Prompt chart:** Figure 3 không in numeric labels trên bars; chỉ nên dùng ranking.
8. **Forgetting claim:** accuracy qua task hỗ trợ kết luận nhưng không thay cho một forgetting metric trực tiếp.

## Tôi hiểu được gì

- Giá trị lớn nhất của CPL không nằm ở “dùng ChatGPT”, mà ở việc phối hợp representation, geometry và replay.
- Hybrid prompt làm relation extraction trông giống task mà BERT đã biết từ pretraining; nó là một dạng task alignment, không chỉ là thêm vài token.
- MCL và NCM tạo một pipeline metric-learning nhất quán: train để feature space phân biệt, infer bằng khoảng cách trong chính feature space đó.
- Replay memory giải quyết retention; generated samples chủ yếu làm support set quanh memory exemplar bớt quá hẹp.
- Data augmentation có giá trị mạnh trên TACRED nhưng chỉ nhẹ trên FewRel, nên phải tune theo dataset và kiểm tra synthetic quality.
- Một exemplar/relation là lựa chọn rất cực đoan. Kết quả sensitivity cho thấy performance tăng rõ nếu memory budget được nới.

## Khi áp dụng

CPL phù hợp khi:

- relation label space tăng theo thời gian;
- có entity pair và relation descriptions rõ;
- mỗi relation mới chỉ có vài labeled samples;
- được phép giữ một episodic memory nhỏ;
- có thể dùng external LLM để tạo replay data;
- inference cần thêm class mới mà không thiết kế lại softmax head.

Cần thận trọng khi:

- dữ liệu nhạy cảm không được rời hệ thống;
- relation direction/semantics khó mô tả bằng prompt;
- có nhiều `no_relation` hoặc open-world examples;
- LLM-generated errors không thể được tự động kiểm duyệt;
- task stream dài khiến replay cost tăng quá nhanh.

## Câu hỏi review

1. CFRE khác static few-shot RE và continual RE thông thường ở đâu?
2. Vì sao task đầu của protocol không phải few-shot?
3. CPL bỏ verbalizer bằng cách nào?
4. `[MASK]` hidden state đóng vai trò gì?
5. Tại sao template của CPL được gọi là hybrid prompt?
6. Vì sao soft-only prompt hoạt động kém trong setting này?
7. $C^k$, $\hat{\mathcal M}$ và $\mathcal A$ khác nhau như thế nào?
8. MCL khác supervised contrastive loss ở thành phần nào?
9. Vì sao MCL được dùng cả current-task training lẫn replay?
10. Khi $L=1$, K-means exemplar selection thực hiện điều gì?
11. Demonstration giúp GPT-3.5 tránh lỗi relation như thế nào?
12. Vì sao thêm nhiều generated samples có thể làm accuracy giảm?
13. Tại sao NCM phù hợp class-incremental prediction hơn fixed softmax head?
14. Component nào có ablation impact lớn nhất?
15. Vì sao augmentation quan trọng hơn trên TACRED so với FewRel?
16. Kết quả nào cho thấy CPL giảm forgetting, và bằng chứng nào vẫn còn thiếu?
17. Vì sao `Joint-train` chỉ là upper bound chứ không phải continual baseline thực tế?
18. Những assumptions nào khó giữ trong production relation extraction?

## Gợi ý trả lời câu hỏi review

1. CFRE vừa tăng label space theo task, vừa yêu cầu giữ relation cũ, vừa giới hạn relation mới ở vài labeled samples.
2. Task đầu dùng 100 samples/relation để tạo initial knowledge base; chỉ task 2-8 là 5-shot hoặc 10-shot.
3. CPL không map relation label sang token; nó học embedding tại `[MASK]` rồi phân loại bằng distance tới prototype.
4. `[MASK]` hidden state là relation representation của head-tail pair trong context.
5. Template kết hợp entity structure cố định với continuous learnable prompt vectors.
6. Random soft vectors khó học ổn định từ vài examples nếu không có hard structural prior.
7. $C^k$ là feature bucket tạm cho contrastive pairs; $\hat{\mathcal M}$ là real replay memory qua task; $\mathcal A$ là generated replay data.
8. MCL thêm similarity-dependent relaxation factors $\alpha_{i,p}$ và $\alpha_{i,n}$ vào contrastive logits.
9. Lượt đầu tạo geometry cho relation mới; lượt replay củng cố geometry của relation cũ và giảm overfit vào sparse memory.
10. Một cluster được tạo cho relation và sample thật gần centroid nhất được giữ.
11. Exemplar chỉ rõ context, head-tail orientation và surface realization của relation; relation name/description một mình có thể mơ hồ.
12. Synthetic data có thể noisy, lặp lexical pattern hoặc lệch distribution; sau một ngưỡng, lỗi nhiều hơn thông tin mới.
13. NCM thêm class bằng prototype mới và không phụ thuộc fixed output dimension.
14. Prompt representation: bỏ nó làm mất 13.41 điểm trên FewRel và 14.78 điểm trên TACRED tại $T^8$.
15. TACRED mất cân bằng và khó hơn; generated replay thêm 6.76 điểm, trong khi FewRel chỉ thêm 0.72 điểm.
16. Accuracy trajectory và final-task gaps hỗ trợ claim; paper thiếu explicit forgetting/BWT metric và uncertainty.
17. Joint-train giữ toàn bộ old data, vi phạm memory constraint của continual setting.
18. Task boundaries, known entity spans, disjoint labels, relation descriptions, external API và permission lưu real examples có thể không tồn tại trong production.

## Cần đọc tiếp

- [ ] Đối chiếu implementation của MCL với dấu và indexing trong Equations 4-9.
- [ ] Kiểm tra code tạo GPT prompt, parser và cách xử lý generated sample lỗi.
- [ ] Xác định chính xác sáu random seeds/task orders dùng để average kết quả.
- [ ] So sánh CPL với [[Replay in Continual Learning]] không dùng external LLM dưới cùng compute/API budget.
- [ ] Đo explicit forgetting, macro-F1, variance, replay latency và token cost.
- [ ] Kiểm tra setting có `no_relation`, noisy entity spans và multilingual data.

## Liên quan đến

- [[04 - Concepts/Continual Learning|Continual Learning]]
- [[Catastrophic Forgetting]]
- [[Continual Relation Extraction]]
- [[Continual Few-Shot Relation Extraction]]
- [[Replay in Continual Learning]]
- [[Few-shot Learning]]
- [[Contrastive Learning]]
- [[Data Augmentation]]
- [[Relation Extraction]]
- [[Masked Language Modeling]]

## Evidence map

| Evidence | Vị trí trong PDF |
| --- | --- |
| Metadata, abstract, CFRE problem, catastrophic forgetting và overfitting | [[Making Pre-trained Language Models Better Continual Few-Shot Relation Extractors.pdf#page=1\|PDF tr. 1]] |
| Research gap, contributions, code footnote, continual/prompt-learning related work | [[Making Pre-trained Language Models Better Continual Few-Shot Relation Extractors.pdf#page=2\|PDF tr. 2]] |
| Task formalization, $N$-way $K$-shot, $L=1$ memory, framework overview, prompt template | [[Making Pre-trained Language Models Better Continual Few-Shot Relation Extractors.pdf#page=3\|PDF tr. 3]] |
| Figure 2, `[MASK]` encoding, MCL Equations 3-8, feature bucket | [[Making Pre-trained Language Models Better Continual Few-Shot Relation Extractors.pdf#page=4\|PDF tr. 4]] |
| Replay, K-means exemplar selection, GPT prompt, two-stage training, NCM Equation 9 | [[Making Pre-trained Language Models Better Continual Few-Shot Relation Extractors.pdf#page=5\|PDF tr. 5]] |
| Table 1, dataset split, evaluation, baselines và implementation | [[Making Pre-trained Language Models Better Continual Few-Shot Relation Extractors.pdf#page=6\|PDF tr. 6]] |
| Main-result interpretation, Table 2 ablation, Table 3 prompt formats | [[Making Pre-trained Language Models Better Continual Few-Shot Relation Extractors.pdf#page=7\|PDF tr. 7]] |
| Figures 3-5, t-SNE, generation sensitivity, demonstration/no-demonstration case | [[Making Pre-trained Language Models Better Continual Few-Shot Relation Extractors.pdf#page=8\|PDF tr. 8]] |
| Conclusion, declared limitations và result instability | [[Making Pre-trained Language Models Better Continual Few-Shot Relation Extractors.pdf#page=9\|PDF tr. 9]] |
| Bibliographical references, gồm prompt tuning, replay, MCL foundations | [[Making Pre-trained Language Models Better Continual Few-Shot Relation Extractors.pdf#page=10\|PDF tr. 10]] |
| Bibliographical và language-resource references cho FewRel/TACRED | [[Making Pre-trained Language Models Better Continual Few-Shot Relation Extractors.pdf#page=11\|PDF tr. 11]] |
| Appendix dataset details, baseline caveats, hardware và Table 5 hyperparameters | [[Making Pre-trained Language Models Better Continual Few-Shot Relation Extractors.pdf#page=12\|PDF tr. 12]] |
| Figure 6 memory-size sensitivity, Table 6 10-shot results, generated-data observations | [[Making Pre-trained Language Models Better Continual Few-Shot Relation Extractors.pdf#page=13\|PDF tr. 13]] |
| Table 7 generated cases và relation-error example | [[Making Pre-trained Language Models Better Continual Few-Shot Relation Extractors.pdf#page=14\|PDF tr. 14]] |

## Trích dẫn đáng giữ

- Không lưu đoạn trích dài nguyên văn. Ý chính cần giữ bằng lời của tôi: CPL coi prompt alignment, contrastive geometry và replay augmentation là ba mảnh bổ trợ nhau; generated data chỉ hữu ích đến một ngưỡng và không thay thế real exemplar.
