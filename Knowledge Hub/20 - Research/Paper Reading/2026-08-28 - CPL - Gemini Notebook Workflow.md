---
type: paper-reading
date: 2026-08-28
status: draft
workflow: gemini-notebook
template: "[[Paper Reading Gemini Notebook Workflow]]"
paper: "[[Making Pre-trained Language Models Better Continual Few-Shot Relation Extractors]]"
pdf: "[[Making Pre-trained Language Models Better Continual Few-Shot Relation Extractors.pdf]]"
paper_note: "[[Making Pre-trained Language Models Better Continual Few-Shot Relation Extractors]]"
notebook_url:
target_minutes: 90
actual_minutes:
reading_goal: "Hiểu CPL theo deep workflow: CFRE protocol, hybrid prompt, MCL, feature bucket, memory augmentation bằng GPT-3.5, NCM inference, results, ablations và caveat."
current_phase: scaffolded
completed: false
need_review: true
review_date:
created_at: 2026-08-28
updated_at: 2026-09-01
tags:
  - paper-reading
  - gemini-notebook
  - continual-learning
  - continual-relation-extraction
  - few-shot-learning
  - relation-extraction
---

# 2026-08-28 - CPL - Gemini Notebook Workflow

> [!note] Ranh giới
> Đây là working note scaffold từ paper note/PDF để hỗ trợ đọc với Gemini Notebook. Các phần recall/draft bên dưới dùng để tự kiểm và hỏi Gemini; chỉ những đoạn bạn tự viết sau khi đọc mới được coi là closed-book recall cá nhân. Không coi note này là bằng chứng đã đọc xong paper.

## Setup

- Paper: [[Making Pre-trained Language Models Better Continual Few-Shot Relation Extractors]]
- PDF: [[Making Pre-trained Language Models Better Continual Few-Shot Relation Extractors.pdf]]
- Paper note chính: [[Making Pre-trained Language Models Better Continual Few-Shot Relation Extractors]]
- Gemini Notebook / NotebookLM URL:
- Mục tiêu buổi đọc: hiểu CPL phối hợp prompt representation, margin-based contrastive learning và memory augmentation như thế nào trong continual few-shot relation extraction.
- Phần cần đọc trước: Abstract, Section 3-4, Table 1-3, Figure 2-6, limitations, Appendix.
- PDF count đã kiểm tra: 14 trang.

## Từ điển khái niệm nhanh

| Khái niệm | Định nghĩa ngắn trong paper này | Vì sao quan trọng | Link |
|---|---|---|---|
| CFRE | Continual Few-Shot Relation Extraction: học tuần tự các relation mới với ít labeled examples ở các task sau, trong khi vẫn đánh giá trên tất cả relation đã thấy. | Đây là bài toán trung tâm; vừa có forgetting, vừa có overfitting. | [[Continual Few-Shot Relation Extraction]] |
| CPL | Contrastive Prompt Learning: framework gồm hybrid prompt, MCL, memory augmentation và NCM inference. | Đây là đóng góp chính của paper. | [[Making Pre-trained Language Models Better Continual Few-Shot Relation Extractors]] |
| Prompt representation | Biến câu RE thành cloze-style input có `[MASK]`, rồi dùng hidden state tại `[MASK]` làm relation embedding. | Tận dụng pretraining interface của PLM mà không cần verbalizer. | [[Prompt Tuning]], [[Masked Language Modeling]] |
| Hybrid prompt | Prompt kết hợp hard structure như entity positions/`[MASK]` với continuous learnable vectors `[v]`. | Giữ prior có cấu trúc nhưng vẫn cho model tự học phần prompt mềm. | [[Prompt Tuning]] |
| Verbalizer | Bảng map label sang token/cụm token để dự đoán tại `[MASK]`. CPL không dùng verbalizer. | Nếu không có verbalizer, inference phải dựa vào metric/prototype thay vì label-token probability. | [[Prompt Tuning]] |
| MCL | Margin-based Contrastive Learning: contrastive objective có relaxation factors phụ thuộc similarity của positive/negative pairs. | Tăng lực học ở hard pairs và làm feature space phân biệt hơn trong few-shot. | [[Contrastive Learning]] |
| Feature bucket $C^k$ | Bộ nhớ tạm chứa features của current task để sample thêm contrastive pairs trong khi train task $k$. | Không phải replay memory qua task; chỉ giúp MCL có nhiều positives/negatives hơn batch nhỏ. | [[Contrastive Learning]] |
| Replay memory $\hat{\mathcal M}$ | Exemplars thật được chọn bằng K-means và giữ qua các task, chính setting là $L=1$ exemplar/relation. | Là bằng chứng cũ để replay và tạo prototypes; CPL không rehearsal-free. | [[Replay in Continual Learning]] |
| Augmented samples $\mathcal A$ | Structured examples do GPT-3.5 sinh từ relation description và exemplar thật. | Mở rộng support set cho replay, nhưng có rủi ro noise/label drift. | [[Data Augmentation]], [[Replay in Continual Learning]] |
| NCM | Nearest-Class-Mean classifier: gán nhãn theo prototype gần nhất trong embedding space. | Phù hợp class-incremental inference vì thêm relation mới bằng prototype, không cần fixed softmax head. | [[Prototype Learning]] |
| Strict evaluation | Sau task $k$, candidate labels là toàn bộ relation đã thấy, không chỉ vài label được chọn lỏng lẻo. | Làm kết quả khó hơn và công bằng hơn cho continual setting. | [[Continual Few-Shot Relation Extraction]] |

## Phase 1 - Paper Map

### Prompt gửi Gemini

```text
Do not summarize the paper in detail yet. Create a structural map of this paper and identify problem, motivation, gap, contributions, pipeline, components, losses, datasets, baselines, metrics, main experiments, ablations, and limitations. For every item, point to the relevant section, figure, table, or equation. The purpose is to tell me WHERE to read, not to replace my reading.
```

### Paper map - scaffold từ nguồn

- **Problem:** CFRE yêu cầu học relation mới liên tục với ít labeled data, đồng thời tránh catastrophic forgetting và overfitting. [[Making Pre-trained Language Models Better Continual Few-Shot Relation Extractors.pdf#page=1|PDF tr. 1]]
- **Motivation:** PLM có implicit knowledge nhưng các CFRE methods trước đó chưa tận dụng prompt learning đủ trực tiếp trong few-shot continual relation extraction. [[Making Pre-trained Language Models Better Continual Few-Shot Relation Extractors.pdf#page=2|PDF tr. 2]]
- **Gap:** cần representation có khả năng chuyển giữa old/new relations và objective làm feature space phân biệt hơn trong low-resource setting.
- **Main idea:** dùng hybrid prompt lấy `[MASK]` hidden state làm relation embedding, MCL để tập trung hard pairs, exemplar replay + GPT-3.5 generated samples để mở rộng memory, rồi dự đoán bằng NCM.
- **Main contributions:** Contrastive Prompt Learning, hybrid prompt không verbalizer, margin-based contrastive objective, GPT memory augmentation, NCM inference.
- **Important figure:** Figure 2 framework CPL. [[Making Pre-trained Language Models Better Continual Few-Shot Relation Extractors.pdf#page=4|PDF tr. 4]]
- **Important equations:** prompt template Eq. 1-3, MCL Eq. 4-8, NCM Eq. 9. [[Making Pre-trained Language Models Better Continual Few-Shot Relation Extractors.pdf#page=4|PDF tr. 4]], [[Making Pre-trained Language Models Better Continual Few-Shot Relation Extractors.pdf#page=5|PDF tr. 5]]
- **Main result table:** Table 1 cho 5-shot; Table 6 cho 10-shot. [[Making Pre-trained Language Models Better Continual Few-Shot Relation Extractors.pdf#page=6|PDF tr. 6]], [[Making Pre-trained Language Models Better Continual Few-Shot Relation Extractors.pdf#page=13|PDF tr. 13]]
- **Ablation table:** Table 2 components, Table 3 prompt formats, Figure 5 generated samples, Figure 6 memory size. [[Making Pre-trained Language Models Better Continual Few-Shot Relation Extractors.pdf#page=7|PDF tr. 7]], [[Making Pre-trained Language Models Better Continual Few-Shot Relation Extractors.pdf#page=8|PDF tr. 8]], [[Making Pre-trained Language Models Better Continual Few-Shot Relation Extractors.pdf#page=13|PDF tr. 13]]
- **Limitations:** training time tăng theo memory/generated samples; GPT-3.5 output không hoàn toàn ổn định. [[Making Pre-trained Language Models Better Continual Few-Shot Relation Extractors.pdf#page=9|PDF tr. 9]]

### Chỗ cần đọc trước

- [x] Abstract + Introduction
- [x] Section 3 task formalization
- [x] Section 4 framework
- [x] Table 1-3
- [x] Figure 3-6
- [x] Limitations + Appendix

## Phase 2 - Pass 1 Recall

### Recall draft cần kiểm tra

> [!note] Cách dùng phần này
> Các gạch đầu dòng dưới đây là bản recall/draft để đem đi kiểm với Gemini hoặc tự kiểm lại PDF. Nếu phần nào không phải do bạn tự viết sau khi đọc, đừng coi nó là closed-book recall cá nhân.

**Problem**

- Bài toán cụ thể ở đây là **Continual Few-Shot Relation Extraction (CFRE)**. Điểm mấu chốt là mô hình vừa phải học liên tục các quan hệ mới, vừa phải đối mặt với giới hạn ngặt nghèo về mặt dữ liệu (few-shot), dẫn đến hai thách thức song hành là **quên lãng thảm họa (catastrophic forgetting)** và **quá khớp (overfitting)**

**Why does it matter?**

- Trong thực tế, các quan hệ mới xuất hiện liên tục. Việc học liên tục (Continual Learning) giúp hệ thống tích lũy thêm tri thức mới mà không cần giữ lại toàn bộ kho dữ liệu cũ khổng lồ (vốn có thể bị xóa đi vì lý do bảo mật hoặc giới hạn lưu trữ)

**Research gap**

- Theo claim của paper, chưa có hướng nào khai thác trực tiếp prompt technology trong **CFRE** để kéo implicit knowledge của PLM vào bài toán này. Cần giữ caveat: prompt-based continual relation extraction đã có trước đó, nhưng không cùng setting CFRE mà paper nhắm tới.

**Main idea**

- Sử dụng Contrastive prompt learning
	- Prompt representation: chuyển bài toán classification thành cloze/text-infilling style với `[MASK]`, rồi lấy hidden state tại `[MASK]` làm relation embedding.
	- **Margin-based Contrastive Learning (MCL):** tập trung lực học vào các mẫu khó (hard samples), làm feature distribution đều hơn và giảm overfitting trong low-resource setting.
	- **Memory Augmentation:** hướng dẫn GPT-3.5 sinh thêm dữ liệu replay từ relation description và exemplar thật để mở rộng support set của memory nhỏ.

**Main contribution**

- Đề xuất Contrastive Prompt Learning: kết hợp hybrid prompt, MCL, memory augmentation và NCM để giảm forgetting/overfitting trong setting paper.
- Giới thiệu memory augmentation bằng GPT-3.5, nhưng kết quả của phần này phụ thuộc dataset và chất lượng synthetic samples.

**Main result**

- Paper báo cáo CPL đạt T8 accuracy cao hơn SCKD trên 5-shot: +1.63 điểm ở FewRel và +6.28 điểm ở TACRED; đây là **reported accuracy points**, chưa phải kết quả reproduce cục bộ.

### Feedback đối chiếu recall với PDF

| Mục | Đánh giá | Cần chỉnh / bổ sung | Evidence |
|---|---|---|---|
| Problem | Đúng hướng | Nói rõ task đầu của protocol có 100 examples/relation; chỉ task 2-8 mới là 5/10-shot. | [[Making Pre-trained Language Models Better Continual Few-Shot Relation Extractors.pdf#page=3\|PDF tr. 3]], [[Making Pre-trained Language Models Better Continual Few-Shot Relation Extractors.pdf#page=6\|PDF tr. 6]] |
| Motivation | Đúng nhưng còn chung | Lý do chính là relation mới xuất hiện liên tục và labeled data đắt/ít, không chỉ là không muốn giữ toàn bộ data cũ. | [[Making Pre-trained Language Models Better Continual Few-Shot Relation Extractors.pdf#page=1\|PDF tr. 1]] |
| Research gap | Cần thu hẹp claim | Paper claim “first exploration of prompt technologies in CFRE”; không nên viết thành mọi phương pháp trước đó đều chưa khai thác PLM/prompt trong mọi setting CRE. | [[Making Pre-trained Language Models Better Continual Few-Shot Relation Extractors.pdf#page=2\|PDF tr. 2]] |
| Main idea | Đúng | Bổ sung NCM vì nó là phần inference quan trọng và thay softmax classifier. | [[Making Pre-trained Language Models Better Continual Few-Shot Relation Extractors.pdf#page=5\|PDF tr. 5]] |
| Main contribution | Đúng nhưng thiếu caveat | Memory augmentation dùng GPT-3.5 vẫn có instability/noise; authors tự ghi temperature 0 vẫn không đảm bảo output giống nhau. | [[Making Pre-trained Language Models Better Continual Few-Shot Relation Extractors.pdf#page=9\|PDF tr. 9]], [[Making Pre-trained Language Models Better Continual Few-Shot Relation Extractors.pdf#page=12\|PDF tr. 12]] |
| Main result | Quá mơ hồ | Nên ghi metric, dataset, baseline và T8 accuracy; không gọi “SOTA” ngoài phạm vi baselines/protocol paper so sánh. | [[Making Pre-trained Language Models Better Continual Few-Shot Relation Extractors.pdf#page=6\|PDF tr. 6]] |

### Prompt kiểm tra recall

```text
I have completed the first pass of the paper.

Here is my understanding:

[PASTE MY NOTES]

Compare my understanding against the paper. Return what is correct, inaccurate, missing, confusing, and which sections/citations I should revisit. Do not rewrite the entire paper for me.
```

## Phase 3 - Problem / Motivation / Gap

| Mục | Diễn giải học tập | Evidence / citation |
|---|---|---|
| General problem | Continual few-shot relation extraction cần học relation mới tuần tự với rất ít mẫu và vẫn giữ relation cũ. | [[Making Pre-trained Language Models Better Continual Few-Shot Relation Extractors.pdf#page=1\|PDF tr. 1]] |
| Why it matters | Relation mới xuất hiện theo thời gian; labeled data ít làm model dễ quên và overfit. | [[Making Pre-trained Language Models Better Continual Few-Shot Relation Extractors.pdf#page=1\|PDF tr. 1]] |
| What prior work solves | Replay, prototype, distillation, data augmentation và contrastive learning đã được dùng cho CRE/CFRE. | [[Making Pre-trained Language Models Better Continual Few-Shot Relation Extractors.pdf#page=2\|PDF tr. 2]] |
| What prior work fails to solve | Theo paper, prompt technology chưa được khai thác đầy đủ trong CFRE, và low-resource training vẫn khó với hard/similar relations. | [[Making Pre-trained Language Models Better Continual Few-Shot Relation Extractors.pdf#page=2\|PDF tr. 2]] |
| Exact research gap | Cần framework tận dụng PLM prompt knowledge, tạo feature space phân biệt, và bổ sung replay memory trong few-shot continual setting. | [[Making Pre-trained Language Models Better Continual Few-Shot Relation Extractors.pdf#page=2\|PDF tr. 2]] |
| Hypothesis / intuition | Prompt alignment giúp representation tổng quát hơn; MCL xử lý hard pairs; generated replay giảm overfitting quanh một exemplar. | inferred từ method/results |
| Contribution addressing the gap | CPL kết hợp hybrid prompt, MCL, feature bucket, memory augmentation bằng GPT-3.5 và NCM classifier. | [[Making Pre-trained Language Models Better Continual Few-Shot Relation Extractors.pdf#page=4\|PDF tr. 4]], [[Making Pre-trained Language Models Better Continual Few-Shot Relation Extractors.pdf#page=5\|PDF tr. 5]] |

### Câu hỏi tự kiểm tra

- [ ] CFRE trong CPL khác strict NK-CRE của ConPL ở task đầu như thế nào?
- [ ] Prompt representation giải quyết forgetting hay overfitting, hay cả hai theo cách khác nhau?
- [ ] Generated replay samples là evidence thật hay synthetic support?

## Phase 4 - Method / Architecture

### Sơ đồ pipeline nháp

```text
Sentence + head/tail entity
-> hybrid prompt with learnable vectors + [MASK]
-> BERT-base encoder
-> [MASK] relation embedding
-> feature bucket for contrastive pairs
-> MCL current-task training
-> K-means select real exemplars
-> GPT-3.5 generate replay samples
-> MCL memory replay
-> NCM over prototypes of seen relations
```

### Component map

| Component | Input | Operation | Output | Purpose | Evidence |
|---|---|---|---|---|---|
| Hybrid prompt | sentence, head, tail, learnable prompt vectors | đặt entity và `[MASK]` vào template có hard + soft prompt | prompted input | align RE với masked-language pretraining | [[Making Pre-trained Language Models Better Continual Few-Shot Relation Extractors.pdf#page=4\|PDF tr. 4]] |
| `[MASK]` representation | prompted input | BERT encode, lấy hidden state tại `[MASK]` | relation embedding $m$ | biểu diễn relation không cần verbalizer | [[Making Pre-trained Language Models Better Continual Few-Shot Relation Extractors.pdf#page=4\|PDF tr. 4]] |
| MCL | normalized features, positive/negative pairs | similarity-dependent contrastive weighting | discriminative feature geometry | tập trung hard pairs, giảm overfitting | [[Making Pre-trained Language Models Better Continual Few-Shot Relation Extractors.pdf#page=4\|PDF tr. 4]] |
| Feature bucket $C^k$ | current-task features | lưu và sample contrastive features | larger contrastive pair set | tránh cần batch rất lớn | [[Making Pre-trained Language Models Better Continual Few-Shot Relation Extractors.pdf#page=4\|PDF tr. 4]] |
| Real replay memory $\hat{\mathcal M}$ | current-task embeddings | K-means, chọn sample gần centroid | exemplar memory | giữ support thật cho relation cũ | [[Making Pre-trained Language Models Better Continual Few-Shot Relation Extractors.pdf#page=5\|PDF tr. 5]] |
| GPT augmentation $\mathcal A$ | relation description + exemplar | GPT-3.5 sinh structured examples | synthetic replay samples | mở rộng memory quanh exemplar | [[Making Pre-trained Language Models Better Continual Few-Shot Relation Extractors.pdf#page=5\|PDF tr. 5]], [[Making Pre-trained Language Models Better Continual Few-Shot Relation Extractors.pdf#page=14\|PDF tr. 14]] |
| NCM classifier | test embedding + prototypes | nearest class mean by L2 distance | predicted relation | thêm class mới không cần fixed softmax head | [[Making Pre-trained Language Models Better Continual Few-Shot Relation Extractors.pdf#page=5\|PDF tr. 5]] |

### Điểm còn cần kiểm tra

- [ ] Eq. 4 có thiếu dấu âm trong notation không, hay implementation xử lý ở loss cuối?
- [ ] Eq. 9 indexing từ $0$ đến $L$ nhưng chia $L$ là notation hay off-by-one?
- [ ] Generated samples có được filter tự động trước replay không?

## Phase 5 - Section Recall

### Section 4.2 - Prompt representation

- **Input:** sentence, head/tail entity, continuous prompt vectors.
- **Process:** tạo hybrid prompt, encode bằng BERT, lấy `[MASK]`.
- **Output:** relation embedding.
- **Purpose:** tận dụng PLM knowledge mà không cần verbalizer thủ công.
- **Still unclear:** prompt random initialization ổn định đến đâu trong mỗi seed?

### Section 4.3 - Margin-based contrastive learning

- **Input:** normalized features, positive/negative samples, bucket features.
- **Process:** tính similarity và relaxation factors theo margin.
- **Output:** MCL loss.
- **Purpose:** tạo feature space tách hard/similar relations tốt hơn SCL.
- **Still unclear:** dấu của Eq. 4 và cách bucket refresh trong code.

### Section 4.4 - Memory augmentation

- **Input:** real exemplar, relation name/description, current memory.
- **Process:** K-means chọn exemplar; GPT-3.5 sinh generated samples; replay bằng MCL.
- **Output:** augmented replay set.
- **Purpose:** giảm forgetting và overfitting khi replay chỉ có ít exemplar thật.
- **Still unclear:** chất lượng generated samples được kiểm như thế nào?

## Phase 6 - Equations

### Prompt operational equation walkthrough

```text
Walk me through the key equations or formal blocks in this paper.

For each equation/block, explain:
1. Input: what variables or objects go into it.
2. Output: what it produces.
3. Where it is used in the training/inference pipeline.
4. What behavior it encourages.
5. What would likely break or become weaker if removed.
6. Which table, figure, ablation, or result supports its usefulness.

Do not summarize the whole paper. Focus only on operational understanding of the equations and formal mechanisms.
```

| Eq/block | Dùng để làm gì? | Input -> Output | Dùng ở đâu trong pipeline | Behavior được khuyến khích | Nếu bỏ/yếu đi thì sao? | Evidence / ablation | Status |
|---|---|---|---|---|---|---|---|
| Eq. 1-3 - Hybrid prompt + `[MASK]` embedding | chuyển RE thành prompt representation | sentence/entity/prompt vectors -> `[MASK]` embedding $m$ | trước MCL và NCM | align với PLM pretraining, tránh verbalizer | nếu bỏ prompt representation, Table 2 giảm mạnh nhất | [[Making Pre-trained Language Models Better Continual Few-Shot Relation Extractors.pdf#page=4\|PDF tr. 4]], [[Making Pre-trained Language Models Better Continual Few-Shot Relation Extractors.pdf#page=7\|Table 2, PDF tr. 7]] | source-checked |
| Eq. 4-8 - MCL | học contrastive geometry với hard pairs | normalized features, positive/negative pairs, $m,k,\tau$ -> MCL loss | current-task training và memory replay | positive gần hơn, negative/hard relations tách hơn | thay bằng SCL làm T8 giảm 2.72 FewRel và 2.64 TACRED | [[Making Pre-trained Language Models Better Continual Few-Shot Relation Extractors.pdf#page=4\|PDF tr. 4]], [[Making Pre-trained Language Models Better Continual Few-Shot Relation Extractors.pdf#page=7\|Table 2, PDF tr. 7]] | source-checked |
| Feature bucket $C^k$ | tạo nhiều contrastive pairs | current-task features -> sampled support set $S_i$ | trong MCL current task | đủ positives/negatives mà không cần batch lớn | thiếu bucket có thể làm contrastive signal nghèo hơn, nhưng paper không ablate riêng | [[Making Pre-trained Language Models Better Continual Few-Shot Relation Extractors.pdf#page=4\|PDF tr. 4]] | source-checked |
| K-means exemplar selection | chọn memory thật | embeddings per relation -> $L$ center-nearest samples | sau current-task training | lưu exemplar đại diện cho relation | $L=1$ nhạy với exemplar; Figure 6 cho thấy tăng $L$ cải thiện accuracy | [[Making Pre-trained Language Models Better Continual Few-Shot Relation Extractors.pdf#page=5\|PDF tr. 5]], [[Making Pre-trained Language Models Better Continual Few-Shot Relation Extractors.pdf#page=13\|Figure 6, PDF tr. 13]] | source-checked |
| GPT augmentation | mở rộng replay set | relation description + exemplar -> generated structured examples | trước memory replay | tăng đa dạng replay, nhất là TACRED | bỏ generation giảm TACRED mạnh hơn FewRel | [[Making Pre-trained Language Models Better Continual Few-Shot Relation Extractors.pdf#page=5\|PDF tr. 5]], [[Making Pre-trained Language Models Better Continual Few-Shot Relation Extractors.pdf#page=7\|Table 2, PDF tr. 7]] | source-checked |
| Eq. 9 - NCM prediction | classify seen relations | test embedding + relation prototypes -> nearest relation | inference sau mỗi task | thêm relation bằng prototype, không fixed softmax head | nếu prototype/exemplar yếu, prediction nhạy với representation drift | [[Making Pre-trained Language Models Better Continual Few-Shot Relation Extractors.pdf#page=5\|PDF tr. 5]] | source-checked |

### Điểm cần kiểm tra lại khi đọc công thức

- [ ] Eq. 4/7: đối chiếu dấu loss trong implementation, vì paper note ghi Eq. 4 có thể thiếu dấu âm còn Eq. 7 mới ghi rõ batch loss.
- [ ] Eq. 9: kiểm tra indexing NCM, vì notation tổng từ $i=0$ đến $L$ nhưng chia cho $L$ có thể gây hiểu nhầm off-by-one.
- [ ] Tách rõ $C^k$ feature bucket với replay memory $\hat{\mathcal M}$ và generated samples $\mathcal A$.

## Phase 7 - Loss Functions

```text
CPL training signal
├── MCL current-task training -> learn new relation geometry
├── MCL memory replay -> retain old relation geometry
├── GPT-generated augmentation -> enlarge replay support
└── NCM inference -> classify by nearest relation prototype
```

| Loss/block | Equation | Inputs | Trains component | Behavior | Weight | Ablation |
|---|---|---|---|---|---|---|
| MCL | Eq. 4-8 | positive/negative pairs, $m=0.3$, $k=0.5$, $\tau=0.1$ | prompt vectors + encoder | hard-pair contrastive geometry | built into loss | w.o. MCL drops T8 by 2.72 FewRel / 2.64 TACRED |
| Current-task training | MCL | $D_{train}^k$ + feature bucket | PLM/prompt representation | learn new relations | 10 epochs | not separately ablated from full framework |
| Memory replay | MCL | real memory + generated samples | PLM/prompt representation | retain old relations and reduce overfit | 10 epochs | w.o. generation tested; w.o. replay not isolated |
| NCM | Eq. 9 | prototypes from real exemplars | classifier-free inference | class-incremental prediction | $L=1$ main | memory size sensitivity Figure 6 |

### Cách đọc MCL cẩn thận

- Eq. 4 trong PDF viết log-ratio cho một anchor-positive pair nhưng chưa có dấu âm; Eq. 7 mới đưa dấu âm vào batch loss. Khi giải thích học tập, nên hiểu objective tối ưu như **minimize negative log probability của positive pair trong tập positive + negative features**, còn Eq. 4 là notation trung gian cần kiểm code nếu reproduce.
- Paper prose ghi MCL improvement là `2.27%` và `2.26%`, nhưng Table 2 cho số T8 trực tiếp là `64.50 - 61.78 = 2.72` trên FewRel và `57.39 - 54.75 = 2.64` trên TACRED. Khi trích dẫn định lượng, ưu tiên số tính từ bảng và gọi là **accuracy points**.
- MCL không phải supervised contrastive loss chuẩn đổi tên. Điểm khác là $\alpha_{i,p}=m+k s_{i,p}$ và $\alpha_{i,n}=1-m+k s_{i,n}$ làm contribution của pair phụ thuộc similarity, nhằm nhấn mạnh hard positives/negatives.

## Phase 8 - Experiments

| Experiment | Research question | Dataset | Baselines | Metric | Table/Figure | Main result | Caveat |
|---|---|---|---|---|---|---|---|
| Main 5-shot CFRE | CPL có outperform CFRE baselines không? | FewRel/TACRED | Finetune, Joint-train, RP-CRE, CRECL, ERDA, SCKD, etc. | overall accuracy after each task | Table 1 | T8 FewRel 64.50, TACRED 57.39 | reported, not reproduced; task đầu 100/relation |
| Component ablation | prompt/MCL/generation đóng góp thế nào? | FewRel/TACRED 5-shot | CPL variants | T8 accuracy | Table 2 | bỏ prompt giảm mạnh nhất; generation quan trọng hơn trên TACRED | components tương tác với nhau |
| Prompt format | hybrid prompt có tốt hơn hard/soft/entity marker không? | FewRel/TACRED | marker, hard, soft, hybrid | final accuracy/ranking | Table 3/Figure 3 | hybrid tốt nhất | Figure 3 không có numeric labels |
| MCL visualization | MCL có tách hard/similar relations tốt hơn SCL không? | FewRel examples | SCL vs MCL | t-SNE qualitative | Figure 4 | MCL clusters đều và tách hơn | qualitative, không phải metric |
| Generated sample sensitivity | càng nhiều synthetic samples có tốt hơn không? | FewRel/TACRED | 0/1/2/5/10 generated samples | final accuracy | Figure 5 | FewRel tốt quanh 2, TACRED quanh 5 | synthetic noise khi quá nhiều |
| Memory size sensitivity | tăng exemplar/relation có giúp không? | 10-shot no generation | $L=1,2,5,7,10$ | accuracy | Figure 6 | $L$ tăng thì accuracy tăng, $L=10$ gần Joint-train | không phải setting main |

### Protocol fingerprint

- Dataset and split: FewRel 80 public relations; TACRED bỏ `no_relation`, còn 41 relation.
- Scenario / label space: continual few-shot relation extraction, strict evaluation trên all seen relation labels.
- Backbone: BERT-base-uncased.
- Frozen/trainable components: paper note ghi prompt vectors và encoder parameters được cập nhật từ checkpoint task trước; cần đối chiếu code nếu muốn biết frozen phần nào.
- Seeds / number of runs: reported average qua 6 rounds; Table 5 chỉ ghi `seed 100`, nên mapping giữa seed config và 6 rounds cần kiểm code.
- Metric and averaging: overall accuracy sau mỗi task.
- Baseline implementation: một số lấy từ prior work, một số authors re-run.
- External data / teacher / generated data: GPT-3.5-turbo, temperature 0, generated samples 2/relation cho FewRel và 5/relation cho TACRED.
- Memory budget: main setting $L=1$ real exemplar/relation + generated replay samples; feature bucket $C^k$ chỉ trong current-task optimization.
- Evaluation after each task: yes, T1-T8.
- Compute / hardware: NVIDIA Tesla P40 24 GB, Intel Xeon Gold 5118.

### Những định nghĩa protocol dễ nhầm

- **Continual N-way K-shot trong CPL:** task đầu là base task có nhiều dữ liệu; các task sau mới có $N$ relation/task và $K$ examples/relation. Vì vậy CPL không cùng strict NK-CRE với ConPL, nơi mọi task đều bị ràng buộc few-shot.
- **Overall accuracy after task $T^k$:** accuracy trên union test set của tất cả relation đã thấy đến task $k$, không phải chỉ accuracy của relation mới.
- **Memory size $L$:** số exemplar thật giữ cho mỗi relation. Main experiment dùng $L=1$; generated samples không thay thế khái niệm exemplar thật này.
- **Generated number:** số synthetic samples/relation do GPT-3.5 sinh cho replay; paper chọn 2 cho FewRel và 5 cho TACRED theo hyperparameter table.
- **Reported vs reproduced:** toàn bộ số trong note này là paper-reported/source-checked, chưa phải kết quả chạy lại trong vault.

## Phase 9 - Claim to Evidence

| Claim | Where claim appears | Experiment | Evidence | My judgment | Caveat |
|---|---|---|---|---|---|
| CPL cải thiện CFRE accuracy. | Abstract/Results | Table 1 | T8 FewRel 64.50 vs SCKD 62.87; TACRED 57.39 vs SCKD 51.11. [[Making Pre-trained Language Models Better Continual Few-Shot Relation Extractors.pdf#page=6\|PDF tr. 6]] | supported/reported | chưa reproduced; baseline provenance mixed |
| Prompt representation là component mạnh. | Ablation | Table 2 | w.o. prompt giảm 13.41 FewRel và 14.78 TACRED. [[Making Pre-trained Language Models Better Continual Few-Shot Relation Extractors.pdf#page=7\|PDF tr. 7]] | strong within ablation | không tách hoàn toàn prompt khỏi downstream training choices |
| MCL tốt hơn SCL. | Ablation/visualization | Table 2/Figure 4 | w.o. MCL giảm 2.72/2.64; t-SNE cho hard relations tách hơn. [[Making Pre-trained Language Models Better Continual Few-Shot Relation Extractors.pdf#page=7\|PDF tr. 7]], [[Making Pre-trained Language Models Better Continual Few-Shot Relation Extractors.pdf#page=8\|PDF tr. 8]] | supported | t-SNE qualitative |
| GPT augmentation hữu ích. | Ablation/sensitivity | Table 2/Figure 5 | w.o. gen giảm 0.72 FewRel nhưng 6.76 TACRED. [[Making Pre-trained Language Models Better Continual Few-Shot Relation Extractors.pdf#page=7\|PDF tr. 7]] | dataset-dependent | synthetic quality/noise chưa filter rõ |
| CPL giảm forgetting. | Abstract/Results | accuracy trajectory | Finetune rơi mạnh, CPL giữ T8 cao hơn. [[Making Pre-trained Language Models Better Continual Few-Shot Relation Extractors.pdf#page=6\|PDF tr. 6]] | partial | paper không báo explicit forgetting/BWT metric |

## Phase 10 - Ablation Study

| Component | Intended purpose | With component | Without component | Difference | Conclusion justified | Not justified |
|---|---|---:|---:|---:|---|---|
| Prompt representation - FewRel | align RE với PLM prompt form | 64.50 | 51.09 | -13.41 | prompt representation rất quan trọng | hybrid prompt luôn tốt mọi domain |
| Prompt representation - TACRED | align RE với PLM prompt form | 57.39 | 42.61 | -14.78 | prompt vẫn là component mạnh nhất | chỉ prompt đủ giải quyết CFRE |
| MCL - FewRel | hard-pair contrastive geometry | 64.50 | 61.78 | -2.72 | MCL có ích hơn SCL | t-SNE chứng minh định lượng toàn cục |
| MCL - TACRED | hard-pair contrastive geometry | 57.39 | 54.75 | -2.64 | contribution ổn định | MCL là nguồn gain lớn nhất |
| Generated samples - FewRel | mở rộng replay support | 64.50 | 63.78 | -0.72 | ích nhẹ trên FewRel | generation luôn cần thiết |
| Generated samples - TACRED | mở rộng replay support | 57.39 | 50.63 | -6.76 | rất quan trọng trên TACRED | synthetic samples luôn đúng |
| All components | phối hợp prompt + MCL + generation | 64.50 / 57.39 | 48.29 / 38.06 | -16.21 / -19.33 | components bổ trợ nhau | có thể cộng tuyến tính từng gain |

## Phase 11 - Critical Reading

- Strongest contribution: pipeline metric-learning nhất quán gồm hybrid prompt, MCL, replay augmentation và NCM.
- Weakest part: phụ thuộc GPT-3.5 generated samples nhưng quality filtering, cost và determinism chưa đủ chặt.
- Main assumption: task đầu có 100 samples/relation; từ task 2-8 mới là few-shot.
- Alternative explanation: gain lớn có thể đến từ prompt representation hơn là memory augmentation.
- Missing experiment: explicit forgetting/BWT, macro-F1, calibration, generated sample quality filter, same compute/API-budget comparison.
- Generalization risk: chỉ BERT-base, FewRel/TACRED English sentence-level RE, bỏ `no_relation`.
- Reproducibility risk: seed mapping 6 rounds, GPT API version, parser generated data, Eq. 4/9 notation.

## Phase 12 - Reproduction Check

| Item | Status | Detail | Missing detail / risk |
|---|---|---|---|
| PDF local | Clearly specified | 14 pages, local PDF exists |  |
| Dataset and split | Partially specified | FewRel/TACRED, task đầu 100/relation, task sau 5/10-shot | exact task order files |
| Preprocessing | Partially specified | hybrid prompt with head/tail and `[MASK]` | exact entity formatting/tokenization in code |
| Model / backbone | Clearly specified | BERT-base-uncased | checkpoint hash not stated |
| Training procedure | Partially specified | current-task training + memory replay | exact optimizer schedule/checkpointing |
| Memory strategy | Partially specified | $L=1$ real exemplar/relation main; generated samples 2/5 | generated sample parsing/filtering |
| Loss functions | Partially specified | MCL Eq. 4-8 | sign/indexing should be checked against code |
| Optimizer | Clearly specified | Adam |  |
| Learning rate | Clearly specified | $10^{-5}$ | schedule unclear |
| Batch size | Clearly specified | 16 |  |
| Epochs | Clearly specified | 10 current-task, 10 replay |  |
| Hyperparameters | Clearly specified | $m=0.3$, $k=0.5$, $\tau=0.1$, sample number 500 | tuning grid details |
| Random seeds | Partially specified | 6 rounds; Table 5 seed 100 | mapping unclear |
| Evaluation protocol | Clearly specified | all seen relations after each task |  |
| Compute | Clearly specified | Tesla P40 24 GB, Xeon Gold 5118 | runtime/API cost not reported |

## Phase 13 - Completeness / Oral Exam

### Câu hỏi oral exam để mình tự trả lời sau khi đọc

1. CFRE khác static few-shot RE và continual RE thông thường ở đâu?
2. Vì sao task đầu của CPL không strict few-shot giống ConPL?
3. Hybrid prompt bỏ verbalizer bằng cách nào?
4. MCL khác SCL ở chỗ nào?
5. $C^k$, $\hat{\mathcal M}$ và $\mathcal A$ khác nhau thế nào?
6. Vì sao generated samples giúp TACRED nhiều hơn FewRel?
7. NCM phù hợp class-incremental inference ở đâu?
8. Kết quả nào chứng minh prompt representation là component mạnh nhất?
9. Điểm nào của paper chưa đủ để claim giảm forgetting thật mạnh?
10. Nếu reproduce, bạn kiểm Eq. 4/9 và GPT parser thế nào?

### Prompt oral exam

```text
Quiz me on CPL one question at a time. Focus on CFRE protocol, hybrid prompt, MCL, feature bucket, replay memory, GPT augmentation, NCM inference, ablation interpretation, and protocol caveats. Do not reveal the ideal answer before I attempt it.
```

## Final Paper Note Handoff

### Ý cần chuyển sang paper note

- [x] Problem/gap: CFRE, catastrophic forgetting, overfitting và prompt-learning gap.
- [x] Method overview: hybrid prompt, MCL, feature bucket, exemplar memory, GPT augmentation, NCM.
- [x] Important equations/formal blocks: Eq. 1-3, Eq. 4-8, K-means memory, GPT augmentation, Eq. 9.
- [x] Protocol fingerprint: FewRel/TACRED, 8 tasks, task đầu 100/relation, task sau 5/10-shot, 6 rounds, BERT-base.
- [x] Main results: Table 1 T8 5-shot, Table 6 10-shot.
- [x] Ablation: prompt strongest, MCL moderate, generation dataset-dependent.
- [x] Limitations: not rehearsal-free, GPT dependency, no explicit forgetting, no `no_relation`, mixed baseline provenance.
- [x] Concepts: [[Continual Few-Shot Relation Extraction]], [[Contrastive Learning]], [[Replay in Continual Learning]], [[Data Augmentation]], [[Masked Language Modeling]].

## Liên kết

- [[Making Pre-trained Language Models Better Continual Few-Shot Relation Extractors]]
- [[Continual Few-Shot Relation Extraction]]
- [[Contrastive Learning]]
- [[Replay in Continual Learning]]
- [[Data Augmentation]]
- [[Masked Language Modeling]]
