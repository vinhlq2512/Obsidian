---
type: paper
status: unread
title: "Consistent Prototype Learning for Few-Shot Continual Relation Extraction"
authors:
  - Xiudi Chen
  - Hui Wu
  - Xiaodong Shi
year: 2023
venue: "Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)"
url: "https://aclanthology.org/2023.acl-long.409/"
pdf: "[[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf]]"
code: "https://github.com/XiudiChen/ConPL"
zotero_key:
citekey: "chen-etal-2023-consistent"
doi: "10.18653/v1/2023.acl-long.409"
arxiv:
topic:
  - continual relation extraction
  - few-shot learning
  - prototype learning
  - catastrophic forgetting
priority: medium
reading_status: not-started
rating:
related_concepts:
  - "[[Continual Learning]]"
  - "[[Catastrophic Forgetting]]"
  - "[[Continual Relation Extraction]]"
  - "[[Continual Few-Shot Relation Extraction]]"
  - "[[Prototype Learning]]"
  - "[[Replay in Continual Learning]]"
  - "[[Few-shot Learning]]"
  - "[[Contrastive Learning]]"
  - "[[Relation Extraction]]"
created_at: 2026-08-13
updated_at: 2026-08-13
tags:
  - paper
  - continual-learning
  - relation-extraction
  - few-shot-learning
---

# Consistent Prototype Learning for Few-Shot Continual Relation Extraction

## Tóm tắt một câu

ConPL giải bài toán [[Continual Few-Shot Relation Extraction]] bằng cách lưu đồng thời một exemplar và một prototype vector cho mỗi relation, rồi dùng replay, consistency constraints và hard-negative classification để hạn chế [[Catastrophic Forgetting]] khi mọi task đều chỉ có đúng $K$ mẫu cho mỗi lớp.

## Nguồn

- PDF gốc: [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf]]
- ACL Anthology: [2023.acl-long.409](https://aclanthology.org/2023.acl-long.409/)
- DOI: [10.18653/v1/2023.acl-long.409](https://doi.org/10.18653/v1/2023.acl-long.409)
- Code: [XiudiChen/ConPL](https://github.com/XiudiChen/ConPL)
- Citekey: **chen-etal-2023-consistent**
- arXiv: PDF và ACL Anthology không công bố arXiv ID, vì vậy không suy đoán giá trị này.

## Vấn đề paper giải quyết

[[Continual Relation Extraction]] yêu cầu mô hình học relation mới theo chuỗi task nhưng vẫn phân biệt được tất cả relation đã học trước đó. Trong few-shot setting, ba vấn đề tác động lẫn nhau:

1. **Overfit memory nhỏ:** replay một vài exemplar không đảm bảo representation của relation cũ còn ổn định.
2. **Confusion giữa các lớp gần nghĩa:** relation như **father** và **mother** có context và entity pair giống nhau; học lớp mới có thể làm biến dạng prototype cũ.
3. **Protocol trước đó chưa few-shot đồng đều:** CFRL cho task đầu nhiều dữ liệu hơn các task sau. Test tích lũy vẫn chứa relation của task đầu nên kết quả được hưởng lợi từ supervision không đồng đều.

Paper quan sát prototype distortion và forgetting có xu hướng tăng cùng nhau. Giả thuyết trung tâm là: giữ prototype ổn định và tập trung phân biệt các relation gần nhau sẽ giảm forgetting. [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=1|Bằng chứng: PDF trang 1–2]]

## Đóng góp chính

- Định nghĩa **N-way-K-shot Continual Relation Extraction (NK-CRE)**, trong đó mọi task, kể cả task đầu, đều tuân thủ N-way K-shot.
- Đề xuất **ConPL** gồm prototype-based classification, memory-enhanced learning và consistent learning.
- Xây dựng multi-information episodic memory lưu cả raw exemplar lẫn prototype vector.
- Dùng discrete prompt để khai thác BERT, cùng các loss giữ sample–prototype consistency và phân biệt confusing classes.
- Đánh giá trên FewRel và TACRED với nhiều số shot và phân tích trực tiếp forgetting lẫn prototype distortion.

## Mental model

Mỗi relation có hai mốc neo:

- **Một câu đại diện** cung cấp dữ liệu thật để replay.
- **Một prototype vector** giữ vị trí tương đối của class trong embedding space.

Khi task mới đến, ConPL học dữ liệu mới quanh các mốc neo cũ, chọn một exemplar gần tâm cho relation mới, rồi chạy thêm một stage chỉ trên memory để cân bằng mọi relation. Loss cho confusing classes buộc mô hình tập trung vào ranh giới khó thay vì chỉ tách các lớp dễ.

## Bài toán NK-CRE

Mô hình học chuỗi task $T^1,T^2,\ldots,T^n$. Task $k$ có tập relation $R^k$, train set và test set riêng. Train set tuân thủ N-way K-shot:

$$
D_{\text{train}}^k=\{(x_i,y_i)\}_{i=1}^{N\times K},\qquad y_i\in R^k
$$

Mỗi $x_i$ là câu chứa head entity $e_h$ và tail entity $e_t$. Sau task $k$, model phải dự đoán trên tất cả relation đã biết:

$$
\hat R^k=\bigcup_{i=1}^{k}R^i
$$

và được đánh giá trên hợp test set đã gặp:

$$
\hat D_{\text{test}}^k=\bigcup_{i=1}^{k}D_{\text{test}}^i
$$

Memory của task $k$ là:

$$
M^k=(S^k,P^k)
$$

trong đó $S^k$ là sample memory và $P^k$ là prototype memory. Trong thí nghiệm, mỗi relation lưu đúng một sample và một prototype vector. [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=3|Bằng chứng: PDF trang 3]]

## Phương pháp

### Module 1 — Prototype-based classification

#### Prompt encoder

Input được chuyển thành discrete cloze prompt:

**[CLS], head entity, [MASK], tail entity, [SEP], sentence, [SEP]**

BERTBASE lấy hidden state tại **[MASK]** làm relation representation:

$$
h_{[\text{MASK}]}=f_\theta(x_{\text{input}})
$$

#### Prototype tạm và classifier

Prototype của relation $r_j$ là trung bình embedding của toàn bộ $K$ sample:

$$
p_j=\frac{1}{|D_j^k|}\sum_{(x_i,y_i)\in D_j^k}f_\theta(x_i)
$$

Prototype tạm của task mới được ghép với prototype memory cũ. Xác suất relation dùng softmax trên cosine similarity:

$$
p(r_i\mid x_i)=
\frac{\exp(d(f_\theta(x_i),p_i))}
{\sum_{l=1}^{|\hat R^k|}\exp(d(f_\theta(x_i),p_l))}
$$

Paper gọi $d$ là distance nhưng dùng **cosine similarity**: similarity càng lớn thì logit càng lớn.

Cross-entropy trên dữ liệu task mới cộng memory cũ:

$$
L_{ce}=-\sum_{(x_i,y_i)\in\bar D_{\text{train}}^k}\log p(r_i\mid x_i)
$$

Classification consistency kéo embedding của memory sample về prototype đúng:

$$
L_{cc}=\sum_{(x_i,y_i)\in\hat S^{k-1}}\|f_\theta(x_i)-p_i\|
$$

[[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=4|Bằng chứng: PDF trang 4]]

#### Loss cho confusing classes

Với mỗi sample, ConPL chọn negative prototype gần nhất và các negative có chênh lệch similarity so với prototype đúng nhỏ hơn $\alpha$. Tập $P_i^{sim}$ chỉ gồm prototype đúng và các confusing negatives. Model tối ưu:

$$
L_{fc}=-\sum_{(x_i,y_i)\in\bar D_{\text{train}}^k}\log p_s(r_i\mid x_i)
$$

> [!warning] Eq. 7 không phải focal loss chuẩn theo công thức
> Paper gọi $L_{fc}$ là focal loss, nhưng Eq. 7 chỉ là negative log-likelihood trên restricted set gồm confusing prototypes. Nó không có modulation factor $(1-p_t)^\gamma$ của focal loss chuẩn. Nên hiểu đây là **hard-negative/similar-class cross-entropy** và không đồng nhất với canonical focal loss nếu chưa kiểm tra code.

[[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=5|Bằng chứng: PDF trang 5, Eq. 7]]

### Module 2 — Memory-enhanced learning

ConPL dùng hai memory song song:

- **Sample memory $\hat S^k$:** raw sample có nhãn để [[Replay in Continual Learning]].
- **Prototype memory $\hat P^k$:** feature vector đại diện cho class để giữ geometry.

Cách chọn memory cho relation mới:

1. Tính prototype trung bình từ toàn bộ $K$ sample.
2. Chọn sample có representation gần prototype nhất.
3. Lưu đúng một sample cho mỗi relation.
4. Dùng representation của sample được chọn để tái khởi tạo prototype lưu trữ.
5. Refine prototype của task hiện tại trong các stage sau.

Đây là exemplar điển hình gần class center, nhưng có thể bỏ qua boundary cases hoặc class có nhiều mode. [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=5|Bằng chứng: PDF trang 5]]

### Module 3 — Consistent learning

Task mới có $N\times K$ sample trong khi mỗi relation cũ chỉ có một exemplar, nên dữ liệu train lệch về class mới. ConPL thêm một stage chỉ học trên memory của tất cả relation.

Distribution consistency giữ vector similarity của sample với toàn bộ prototype gần vector similarity của prototype đúng:

$$
L_{dc}=\sum_{(x_i,y_i)\in\hat S^k}
\left\|
d(f_\theta(x_i),\hat P^k)-d(p_i,\hat P^k)
\right\|
$$

$L_{cc}$ là ràng buộc **điểm–tâm**; $L_{dc}$ giữ **cấu trúc tương đối** của điểm với toàn bộ class space. [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=5|Bằng chứng: PDF trang 5, Eq. 8]]

## Quy trình huấn luyện ba stage

### Stage 1 — Học task mới với memory cũ

- Tạo temporary prototypes từ $K$ sample của mỗi relation mới.
- Ghép chúng với prototype memory cũ.
- Train trên $D_{\text{train}}^k\cup\hat S^{k-1}$.
- Objective:

$$
L_{\text{class}}=\lambda_{ce}L_{ce}+\lambda_{cc}L_{cc}+\lambda_{fc}L_{fc}
$$

### Stage 2 — Chọn và refine memory mới

- Chọn key sample gần class center nhất.
- Tái khởi tạo prototype mới từ key sample.
- Train trên data task mới cộng memory đã cập nhật.
- Tiếp tục dùng $L_{\text{class}}$.

### Stage 3 — Memory-only consolidation

- Chỉ train trên memory của mọi relation.
- Cân bằng old/new relations và củng cố sample–prototype geometry.
- Objective:

$$
L_{\text{cons}}=
\lambda_{ce}L_{ce}+\lambda_{cc}L_{cc}+
\lambda_{fc}L_{fc}+\lambda_{dc}L_{dc}
$$

Thiết lập: Adam, learning rate $2\times10^{-5}$, gradient clipping 10, $\alpha=0.1$, mọi $\lambda=1$, số epoch ba stage lần lượt 1, 1 và 3. [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=5|Thuật toán: PDF trang 5]]; [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=6|hyperparameters: PDF trang 6]].

## Experimental setup

### Datasets

**FewRel**

- 100 relation, 700 instance mỗi relation.
- Split relation 64 train / 16 validation / 20 test.
- Dùng 80 relation công khai, chia thành 8 task × 10 relation.
- Setting: 10-way 2-shot, 5-shot và 10-shot.

**TACRED**

- Gốc có 42 relation và hơn 100.000 instance.
- Loại **n/a**, còn 41 relation và 68.438 instance.
- 8 task: một task có 6 relation, bảy task còn lại có 5.
- Setting: 5-way 5-shot và 10-shot.

[[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=6|Setting: PDF trang 6]]; [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=12|thống kê: PDF trang 12]].

### Protocol và metrics

- Main experiments dùng 6 task sequences ngẫu nhiên và báo cáo accuracy trung bình.
- Baseline tái chạy và ConPL dùng cùng seed/task sequences.
- Phân tích distortion–forgetting riêng dùng 50 task sequences.
- Whole accuracy sau task $k$ được tính trên hợp test set từ task 1 đến $k$.
- Forgetting:

$$
F_k=\frac{1}{n-k}\sum_{j=k+1}^{n}g_k^j,\qquad
g_k^j=\max_{l\in\{k,\ldots,j-1\}}a_{l,k}-a_{j,k}
$$

Giá trị forgetting âm biểu thị backward improvement.

### Baselines

- EMR, EMAR, IDLVQ-C, RP-CRE và ERDA.
- EMAR(PT), RP-CRE(PT), ERDA(PT): thêm cùng kiểu prompt để tách lợi ích của prompt.
- SeqRun: chỉ fine-tune task mới, không replay.
- JointTrain: giữ toàn bộ dữ liệu cũ.

> [!warning] Protocol parity caveat
> Các hàng EMR, EMAR, IDLVQ-C và ERDA không có dấu † trong Table 1 được lấy trực tiếp từ CFRL, nơi task đầu có 100 sample/relation. Chúng không cùng supervision budget với NK-CRE. So sánh công bằng hơn là các hàng † được tái chạy và PT variants trên cùng task sequences. ERDA(PT) còn dùng câu Wikipedia ngoài benchmark để augmentation.

[[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=6|Bằng chứng: PDF trang 6]]; [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=7|chú thích Table 1: PDF trang 7]].

## Kết quả quan trọng

### Main results — số trực tiếp từ Table 1

| Dataset/setting | T1 | T2 | T3 | T4 | T5 | T6 | T7 | T8 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| FewRel 10-way 5-shot | 95.72 | 93.53 | 91.31 | 89.95 | 88.93 | 88.39 | 87.43 | 85.77 |
| TACRED 5-way 5-shot | 97.34 | 89.85 | 86.33 | 82.53 | 81.21 | 79.56 | 78.38 | 76.38 |

ConPL dẫn đầu FewRel từ T2–T8; tại T1, ERDA(PT) đạt 96.55 so với 95.72. Trên TACRED, ConPL dẫn đầu cả T1–T8.

| Method tại T8 | FewRel 10-way 5-shot | TACRED 5-way 5-shot |
|---|---:|---:|
| EMAR† | 59.29 | 27.87 |
| RP-CRE† | 61.17 | 24.12 |
| ERDA† | 63.60 | 28.50 |
| EMAR(PT)† | 81.34 | 68.67 |
| RP-CRE(PT)† | 80.87 | 65.31 |
| ERDA(PT)† | 77.02 | 55.97 |
| **ConPL** | **85.77** | **76.38** |

So với baseline tốt nhất ở T8, ConPL hơn EMAR(PT) 4.43 điểm phần trăm trên FewRel và 7.71 điểm trên TACRED.

Appendix báo cáo mean accuracy T1–T8 của FewRel là **90.12 ± 1.50** cho ConPL, so với EMAR(PT) **87.89 ± 2.76**, RP-CRE(PT) **85.79 ± 1.92** và ERDA(PT) **85.21 ± 5.27**.

> [!note] Ưu tiên số trong bảng
> Claim 26.48% trên FewRel khớp $85.77-59.29$. Claim 41.19% trên TACRED không suy ra trực tiếp từ các ô Table 1. Khi trích dẫn nên dùng giá trị bảng và gọi tên baseline thay vì lặp lại headline.

[[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=7|Table 1: PDF trang 7]]; [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=12|Table 4: PDF trang 12]].

### Ablation — FewRel 10-way 5-shot tại T8

| Variant | Accuracy | Giảm so với ConPL |
|---|---:|---:|
| ConPL | 85.77 | — |
| Không Prototype Memory | 82.21 | −3.56 |
| Không Consistent Learning | 84.25 | −1.52 |
| Không $L_{cc}$ | 85.69 | −0.08 |
| Không $L_{dc}$ | 85.40 | −0.37 |
| Không $L_{fc}$ | 75.11 | −10.66 |

$L_{fc}$ có tác động lớn nhất. Khi dùng sample memory thay prototype memory để tính xác suất, đóng góp của $L_{cc}$ và $L_{dc}$ tăng lên lần lượt 0.73 và 2.0 điểm tại T8; prototype memory đã cung cấp một phần consistency mà hai auxiliary loss nhắm tới.

[[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=8|Table 2: PDF trang 8]]; [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=9|phân tích consistency: PDF trang 9]].

### Forgetting — FewRel 10-way 5-shot

| Method | Mean forgetting T1–T7 |
|---|---:|
| SeqRun | 82.08 |
| JointTrain | 3.29 |
| EMAR | 13.34 |
| RP-CRE | 10.70 |
| ERDA | 20.32 |
| EMAR(PT) | 7.24 |
| RP-CRE(PT) | 5.18 |
| ERDA(PT) | 12.78 |
| **ConPL** | **3.31** |

ConPL theo T1–T7: **11.47, 6.11, 3.79, 2.47, 0.46, −0.12, −0.98**. Mean 3.31 gần JointTrain 3.29 dù chỉ lưu một exemplar và một vector mỗi relation. [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=9|Bằng chứng: PDF trang 9, Table 3]]

## Prototype distortion và forgetting

Với relation $r$ xuất hiện lần đầu ở task $i$:

$$
D_r=\frac{1}{n-i}\sum_{j=i+1}^{n}d_r^j,\qquad
d_r^j=1-s(e_{i,r},e_{j,r})
$$

trong đó $s$ là cosine similarity. Scatter trên 50 task sequences cho thấy distortion cao thường đi cùng forgetting cao. Tuy nhiên, paper không báo Pearson/Spearman coefficient và chưa giải thích outlier, nên đây là bằng chứng tương quan chứ chưa phải quan hệ nhân quả. [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=11|Bằng chứng: PDF trang 11]]

## Hạn chế và assumptions

### Tác giả thừa nhận

- Prototype memory tạo thêm storage overhead, dù chỉ một vector mỗi relation.
- Chưa giải thích các prototype ngoại lệ không theo xu hướng distortion–forgetting.
- Domain adaptability được để lại cho nghiên cứu sau.

### Cần lưu ý thêm

- ConPL vẫn rehearsal-based vì lưu raw sample; chưa giải quyết privacy constraint của rehearsal-free learning.
- Setting giả định task boundary, relation label mới và tập class theo task được cung cấp.
- Chỉ đánh giá BERTBASE trên FewRel/TACRED; chưa có cross-domain, multilingual hay encoder-scale study.
- Metric chính là accuracy; chưa báo macro-F1, calibration hoặc chi phí memory theo byte.
- Exemplar gần class center có thể bỏ qua boundary examples hoặc class đa mode.
- Không có sensitivity analysis cho $\alpha$, memory size, số stage hay epoch.
- Eq. 7 không phải focal loss chuẩn theo công thức công bố.
- Variance chi tiết chỉ có FewRel 10-way 5-shot; không có significance test.
- Section 5.4 không nêu GPU hours/infrastructure rõ ràng dù ACL checklist đánh dấu đã báo cáo.

[[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=10|Hạn chế chính thức: PDF trang 10]]; [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=13|checklist: PDF trang 13–14]].

## Tôi hiểu được gì

- Replay sample và giữ geometry là hai việc khác nhau: exemplar cho biết dữ liệu cũ trông thế nào, prototype cho biết class cũ nằm ở đâu.
- Prototype memory ổn định hơn việc tái tính class center chỉ từ một memory sample sau mỗi task.
- Forgetting đặc biệt mạnh ở relation có semantics và context gần nhau.
- Hard-negative discrimination đóng góp lớn hơn hai consistency loss khi classifier đã dùng prototype memory.
- Khi đọc benchmark phải tách lợi ích từ prompt, memory mechanism và external augmentation.

## Câu hỏi review và gợi ý trả lời

### 1. NK-CRE khác CFRL ở đâu?

Mọi task đều có đúng $K$ sample/relation; CFRL được đối chiếu có 100 sample/relation ở task đầu.

### 2. ConPL dùng representation nào?

Hidden state của token **[MASK]** trong discrete cloze prompt.

### 3. Vì sao cần cả sample memory và prototype memory?

Sample phục vụ replay; prototype giữ class anchor và geometry giữa các relation.

### 4. Exemplar được chọn thế nào?

Chọn sample có embedding gần prototype trung bình của relation nhất.

### 5. $L_{cc}$ khác $L_{dc}$ thế nào?

$L_{cc}$ kéo sample về prototype đúng; $L_{dc}$ giữ vector similarity tương đối tới mọi prototype.

### 6. $L_{fc}$ nhắm tới vấn đề gì?

Tập trung vào prototype đúng và các negative dễ nhầm để tách relation gần nghĩa.

### 7. Vì sao Eq. 7 không phải focal loss chuẩn?

Không có modulation factor $(1-p_t)^\gamma$; chỉ có negative log-likelihood trên restricted candidate set.

### 8. Ba stage làm gì?

Học task mới với memory cũ → chọn/refine memory mới → memory-only consolidation.

### 9. Thành phần quan trọng nhất theo ablation?

Bỏ $L_{fc}$ làm T8 giảm 10.66 điểm, lớn nhất trong các ablation.

### 10. ConPL có rehearsal-free không?

Không; nó lưu một raw exemplar và một prototype vector mỗi relation.

### 11. Bằng chứng distortion–forgetting mạnh đến đâu?

Có scatter trên 50 task sequences nhưng không có correlation coefficient hay causal analysis.

### 12. So sánh nào công bằng nhất?

Các baseline có dấu † và PT variants được tái chạy trên strict NK-CRE với cùng task sequences.

## Liên kết concept

- [[Continual Learning]]
- [[Catastrophic Forgetting]]
- [[Continual Relation Extraction]]
- [[Continual Few-Shot Relation Extraction]]
- [[Prototype Learning]]
- [[Replay in Continual Learning]]
- [[Few-shot Learning]]
- [[Contrastive Learning]]
- [[Relation Extraction]]

## Cần đọc và kiểm chứng tiếp

- [ ] Đối chiếu implementation của $L_{fc}$ với Eq. 7.
- [ ] Reproduce FewRel 10-way 5-shot với 6 task sequences.
- [ ] Đo memory theo byte, không chỉ đếm sample/vector.
- [ ] Thử exemplar theo boundary, clustering hoặc nhiều prototype.
- [ ] Báo cáo macro-F1 và calibration trên TACRED.
- [ ] So sánh rehearsal-free methods trên cùng strict NK-CRE.
- [ ] Kiểm định Pearson/Spearman giữa distortion và forgetting.

## Evidence map

- [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=1|PDF trang 1]] — metadata, abstract, problem, Figure 1 và code URL.
- [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=2|PDF trang 2]] — gap, similar-class confusion và related work.
- [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=3|PDF trang 3]] — NK-CRE formulation và hai loại memory.
- [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=4|PDF trang 4]] — prompt, prototypes, $L_{ce}$, $L_{cc}$ và confusing prototype selection.
- [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=5|PDF trang 5]] — Eq. 7–10, memory selection, consistent learning và Algorithm 1.
- [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=6|PDF trang 6]] — datasets, metrics, baselines và hyperparameters.
- [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=7|PDF trang 7]] — Table 1 và main results.
- [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=8|PDF trang 8]] — Figure 2, Table 2 và $L_{fc}$ ablation.
- [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=9|PDF trang 9]] — consistency analysis, Table 3 và forgetting.
- [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=10|PDF trang 10]] — limitations chính thức.
- [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=11|PDF trang 11]] — prototype distortion/forgetting formulas.
- [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=12|PDF trang 12]] — dataset details và Appendix Table 4.
- [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=13|PDF trang 13]] — Responsible NLP Checklist phần đầu.
- [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=14|PDF trang 14]] — Responsible NLP Checklist phần cuối.

