---
type: paper
status: unread
title: "Adaptive Prompting for Continual Relation Extraction: A Within-Task Variance Perspective"
authors:
  - Minh Le
  - Tien Ngoc Luu
  - An Nguyen The
  - Thanh-Thien Le
  - Trang Nguyen
  - Tung Thanh Nguyen
  - Linh Ngo Van
  - Thien Huu Nguyen
year: 2025
venue: "Proceedings of the AAAI Conference on Artificial Intelligence, 39(23), 24384-24392"
url: "https://ojs.aaai.org/index.php/AAAI/article/view/34616"
pdf: "[[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf]]"
zotero_key:
citekey:
doi: "10.1609/aaai.v39i23.34616"
arxiv: "2412.08285v5"
topic:
  - continual relation extraction
  - prompt-based continual learning
  - mixture of experts
  - generative replay
priority: medium
reading_status: not-started
rating:
related_concepts:
  - "[[04 - Concepts/Continual Learning|Continual Learning]]"
  - "[[Catastrophic Forgetting]]"
  - "[[Continual Relation Extraction]]"
  - "[[Prefix Tuning]]"
  - "[[Prompt Pool]]"
  - "[[Mixture of Experts]]"
  - "[[Task Identity Inference]]"
  - "[[Replay in Continual Learning]]"
  - "[[Relation Extraction]]"
created_at: 2026-08-13
updated_at: 2026-08-13
tags:
  - paper
  - continual-learning
  - relation-extraction
  - prompting
---

# Adaptive Prompting for Continual Relation Extraction: A Within-Task Variance Perspective

## Tóm tắt một câu

WAVE-CRE giải bài toán [[Continual Relation Extraction]] không lưu raw examples bằng ba cơ chế phối hợp: một [[Prompt Pool|prompt pool]] riêng cho mỗi task để tách kiến thức giữa task và thích nghi theo từng input, Gaussian replay trong latent space để giữ shared classifier khỏi quên, và một relation-level task predictor để chọn đúng pool khi inference.

## Nguồn

- PDF gốc: [[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf]]
- AAAI: [Proceedings page](https://ojs.aaai.org/index.php/AAAI/article/view/34616)
- DOI: `10.1609/aaai.v39i23.34616`
- arXiv: `2412.08285v5 [cs.CL]`, bản PDF ngày 18-01-2025.
- Venue: AAAI 2025, volume 39, issue 23, trang 24384-24392.

> [!info] Ranh giới trạng thái
> Note này được tổng hợp từ toàn bộ PDF 9 trang để phục vụ học tập và nghiên cứu. `reading_status` vẫn là `not-started` vì chưa có bằng chứng người dùng đã tự đọc paper.

## Bài toán và formulation

Trong [[Continual Relation Extraction]] (CRE), model học tuần tự một chuỗi task:

$$
\{T_1,T_2,\ldots,T_T\}.
$$

Task $T_t$ có dataset gán nhãn

$$
D_t=\{(x_i^t,y_i^t)\}_{i=1}^{N_t},\qquad y_i^t\in R_t,
$$

trong đó $R_t$ là tập relation của task hiện tại. Sau khi học xong task $t$, model phải dự đoán trên toàn bộ relation đã thấy:

$$
\hat R_t=\bigcup_{i=1}^{t}R_i.
$$

Điểm khó là model không chỉ học relation mới mà còn phải giữ decision boundary của relation cũ. Các rehearsal-based methods giải quyết bằng memory buffer, nhưng việc lưu câu gốc tạo chi phí bộ nhớ và lo ngại privacy. [[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf#page=2|PDF, tr. 2]]

## Research gap

Paper chỉ ra bốn failure modes của prompt-based continual learning:

1. **Shared parameters vẫn quên:** shared prompt pool, general prompt hoặc shared MLP classifier tiếp tục bị update theo task mới.
2. **Sai task/prompt ở inference:** training biết task đang học, nhưng test phải tự chọn prompt pool; chọn sai tạo train-test mismatch.
3. **Cross-task variance chưa đủ:** một shared prompt pool có thể khiến samples thuộc các task khác nhau chọn chung expert, làm task-specific knowledge khó tách biệt.
4. **Within-task variance chưa đủ:** một prompt cố định cho cả task không đủ linh hoạt để biểu diễn nhiều context/mode bên trong cùng task.

Hai câu có bề mặt gần giống nhau nhưng biểu diễn relation khác nhau là trường hợp đặc biệt dễ làm shared pool chọn nhầm prompt. [[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf#page=1|PDF, tr. 1]]

## Câu hỏi trung tâm

> Có thể xây một hệ CRE không lưu raw examples nhưng vẫn đồng thời chọn đúng prompt pool, biểu diễn được biến thiên bên trong task và giữ shared classifier ổn định qua nhiều task hay không?

## Đóng góp chính

- Đề xuất **WAVE-CRE** (*Within-Task Variance Awareness for Continual Relation Extraction*).
- Tạo một task-specific prompt pool cho mỗi task; nhiều prompt ngắn cho phép chọn các prefix experts khác nhau theo input.
- Diễn giải [[Prefix Tuning]] qua lăng kính [[Mixture of Experts]] để giải thích vì sao một prompt có thể xem như thêm experts vào self-attention.
- Fit per-relation Gaussian distributions trong query space và prompted-representation space để replay latent samples mà không lưu instance gốc.
- Train relation-level task predictor và shared relation classifier trên synthetic representations của toàn bộ relation đã thấy. [[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf#page=2|PDF, tr. 2]]

## Mental model

```text
Task mới
-> tạo prompt pool riêng
-> query của mỗi input chọn K prompt/expert phù hợp
-> frozen BERT + prompt tạo relation representation
-> classifier học relation mới

Sau mỗi task
-> fit Gaussian cho query và prompted representation của từng relation
-> sample latent vectors của relation cũ và mới
-> củng cố task predictor + shared classifier

Inference
-> task predictor suy ra relation/task gần nhất
-> chọn đúng task-specific pool
-> query chọn prompt trong pool
-> BERT encode + nối hai entity representations
-> classifier dự đoán relation
```

Mental model quan trọng nhất là WAVE-CRE bảo vệ ba tầng khác nhau:

```text
Interference giữa task        -> task-specific prompt pools
Đa dạng bên trong một task    -> input-dependent prompt selection
Forgetting ở shared classifier -> latent generative replay
Sai pool lúc inference        -> relation-level task predictor
```

## Framework

### 1. Prefix tuning như thêm experts vào self-attention

Với input matrix $X$, prefix tuning chia prompt $P$ thành key prefix $P_k$ và value prefix $P_v$, rồi nối chúng vào key/value của attention:

$$
\hat h_i=
\operatorname{Attention}
\left(
XW_i^Q,
[P_k;X]W_i^K,
[P_v;X]W_i^V
\right).
$$

Theo cách diễn giải paper kế thừa, self-attention có thể xem như nhiều MoE models; mỗi prefix vector đóng vai trò một expert mới phối hợp với các experts có sẵn. Prefix experts chỉ là offset vectors, đơn giản hơn pre-trained experts vốn phụ thuộc tuyến tính vào input. Vì vậy một expert cố định khó phủ hết biến thiên của cả task. [[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf#page=3|PDF, tr. 3]]

### 2. Task-specific prompt pool

Mỗi task $t$ có $M$ cặp key-prompt:

$$
P_t=
\{(k_1^{(t)},P_1^{(t)}),\ldots,(k_M^{(t)},P_M^{(t)})\}.
$$

Frozen BERT tạo query $q(x)$. Hệ thống chọn tập $K_x$ gồm $K$ keys gần query nhất:

$$
K_x=
\underset{S\subseteq\{1,\ldots,M\},\ |S|=K}{\arg\min}
\sum_{s\in S}\gamma(q(x),k_s^{(t)}).
$$

Paper đặt prompt length $L_p=2$, nên mỗi prompt chứa đúng một prefix expert, $L=L_p/2=1$. Mỗi expert có key riêng giúp chọn linh hoạt hơn một prompt dài chứa nhiều experts nhưng buộc chúng dùng chung key. Pool riêng giảm parameter sharing giữa task; chọn prompt theo input tăng khả năng mô hình hóa within-task variation. [[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf#page=4|PDF, tr. 4]]

### 3. Sparse-MoE scoring hiệu quả hơn

Nếu chấm điểm mỗi prefix expert riêng cho từng attention position/model, chi phí có thể là $N\times M$ score functions. WAVE-CRE dùng cùng auxiliary score cho mọi $i$:

$$
\hat s_{i,N+j}(\tilde X)=\gamma(q(x),k_j^{(t)}),
$$

nên chỉ cần $M$ scores và dùng cùng tập $K$ prefix experts xuyên các attention positions. Query $q(x)$ đồng thời được task predictor sử dụng nên không cần một lượt encode phụ chỉ để chọn prompt. [[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf#page=4|PDF, tr. 4]]

### 4. Objective học task mới

Với prompted input $x_p$, frozen encoder $f_r$ và classifier $g_\phi$, objective là:

$$
\min_{P_t,\phi}
\mathcal L\left(g_\phi(f_r(x_p)),y\right)
+\lambda\sum_{s_i\in K_x}\gamma(q(x),k_{s_i}^{(t)}).
$$

- Term đầu là relation classification loss.
- Term sau buộc prompt keys khớp với query features.
- Chỉ pool hiện tại $P_t$ và classifier $g_\phi$ được update.
- BERT và các pool cũ $P_1,\ldots,P_{t-1}$ bị freeze. [[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf#page=5|PDF, tr. 5]]

> [!warning] Mơ hồ ký hiệu trong paper
> Eq. 13 dùng `argmin`, Eq. 15 cũng minimize $\gamma$, nhưng text gọi $\gamma$ là cosine similarity. Hai phương trình chỉ nhất quán nếu $\gamma$ thực chất là cosine distance hoặc negative similarity; nếu là similarity đúng nghĩa thì phép chọn phải là `argmax`. Paper không làm rõ dấu này.

### 5. Generative replay trong latent space

Với mỗi relation $r$, WAVE-CRE fit hai Gaussian.

Prompted-representation distribution:

$$
G_z^r\sim\mathcal N(\mu_z^r,\Sigma_z^r),
\qquad z^r=f_r(x_p^r).
$$

Query distribution:

$$
G_q^r\sim\mathcal N(\mu_q^r,\Sigma_q^r),
\qquad q^r=q(x^r).
$$

Mean và covariance được ước lượng từ representations của relation tương ứng. $G_q^r$ sinh query để củng cố task predictor; $G_z^r$ sinh prompted representations để củng cố shared classifier. Đây là [[Replay in Continual Learning|generative replay]] không lưu raw sentences, chứ không phải không replay bất kỳ thông tin quá khứ nào. [[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf#page=5|PDF, tr. 5]]

### 6. Task predictor và relation classifier

Task predictor $\hat g_\psi$ là feed-forward MLP có output dimension bằng số relation đã thấy, $|\hat R_t|$. Nó dự đoán relation trên query representation, rồi relation đó xác định task/prompt pool cần dùng. Thiết kế relation-level tránh việc coi mỗi task là một class tùy ý, vốn có meaning phụ thuộc task order.

Task-predictor loss:

$$
\mathcal L(\psi)=
\sum_{r\in\hat R_t}
\sum_{q\sim G_q^r}
-\log
\frac{\exp(\hat g_\psi(q)[r])}
{\sum_{r'\in\hat R_t}\exp(\hat g_\psi(q)[r'])}.
$$

Relation-classifier consolidation loss:

$$
\mathcal L(\phi)=
\sum_{r\in\hat R_t}
\sum_{z\sim G_z^r}
-\log
\frac{\exp(g_\phi(z)[r])}
{\sum_{r'\in\hat R_t}\exp(g_\phi(z)[r'])}.
$$

Hai loss giải quyết hai shared components khác nhau: $G_q^r$ giữ khả năng chọn đúng pool; $G_z^r$ giữ decision boundary của classifier trên relation cũ. [[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf#page=5|PDF, tr. 5]]

### 7. Luồng train và inference

Algorithm 1 có bốn bước chính:

1. Khởi tạo pool $P_t$ cho task mới.
2. Train $P_t$ và classifier trên real data của task hiện tại bằng Eq. 15.
3. Fit $G_q^r$ và $G_z^r$ cho từng relation mới.
4. Sample representations của toàn bộ relation trong $\hat R_t$, rồi train lại task predictor và relation classifier bằng Eq. 18-19.

Khi inference, task predictor chọn pool; query chọn prompt trong pool; prompt được prepend vào input embedding; BERT encode; hai hidden states tại entity positions $E_1,E_2$ được concatenate và đưa vào relation classifier. [[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf#page=4|Figure 2, PDF tr. 4]] [[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf#page=5|Algorithm 1, PDF tr. 5]]

## Experimental setup

| Thành phần | Thiết lập |
|---|---|
| FewRel | 80 relations, 56.000 samples, chia thành 10 sub-datasets không chồng lấn |
| TACRED | 42 relations, 106.264 samples, chia thành 10 sub-datasets |
| Backbone | BERT frozen |
| Metric | Mean accuracy qua 5 random seeds |
| Rehearsal-free/prompt baselines | L2P, EPI, HiDe-Prompt |
| Rehearsal-based baselines | EA-EMR, RP-CRE, CRL, CRE-DAS, CDec+ACA |
| Compute | Một NVIDIA A100 |
| Parameters | 114M tổng, 3,8M trainable |
| Training time | Khoảng 7 giờ trên FewRel, 3 giờ trên TACRED |

Các prompt baselines vốn được thiết kế cho computer vision và được authors reimplement bằng BERT cho CRE. Hyperparameters của WAVE-CRE được tune bằng random search; prompt-pool size $M$ được giữ cố định qua các task. [[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf#page=6|PDF, tr. 6]]

## Main results

### Accuracy ở learning stage cuối

| Dataset | WAVE-CRE | Rehearsal-free tốt nhất | Chênh lệch | Rehearsal-based tốt nhất | Chênh lệch |
|---|---:|---:|---:|---:|---:|
| FewRel, $T_{10}$ | **85,0** | HiDe-Prompt 67,2 | +17,8 | CDec+ACA 84,8 | +0,2 |
| TACRED, $T_{10}$ | **78,7** | HiDe-Prompt 72,6 | +6,1 | CRE-DAS 79,1 | -0,4 |

WAVE-CRE vượt rõ các rehearsal-free baselines ở stage cuối và gần ngang rehearsal-based methods dù không giữ raw training instances. Tuy nhiên kết luận nên có nuance:

- WAVE-CRE vượt rehearsal-based tốt nhất ở FewRel $T_{10}$ chỉ 0,2 điểm.
- Trên TACRED $T_{10}$, WAVE-CRE vẫn thấp hơn CRE-DAS 0,4 điểm.
- Claim “consistently outperforms” rehearsal-free methods có ngoại lệ ở FewRel $T_1$: EPI đạt 98,3 còn WAVE-CRE đạt 97,9. [[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf#page=6|Table 1, PDF tr. 6]]

## Ablations và phân tích chi tiết

### Task-specific pool so với một prompt/task

Trong task-incremental TACRED, task identity được cung cấp để loại nhiễu từ task prediction:

| Model | $T_1$ | $T_5$ | $T_{10}$ |
|---|---:|---:|---:|
| WAVE-CRE | 98,4 | 92,7 | **85,2** |
| Không prompt pool | 96,8 | 90,6 | 83,4 |

Prompt pool đem lại +1,8 điểm ở $T_{10}$, là evidence trực tiếp nhất cho within-task variation hypothesis. [[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf#page=6|Table 2, PDF tr. 6]]

### Số experts trong mỗi prompt

Authors giữ tổng số selected experts $L\times K=8$:

| Expert/prompt $L$ | Prompt được chọn $K$ | TACRED $T_{10}$ |
|---:|---:|---:|
| 8 | 1 | 84,2 |
| 4 | 2 | 84,1 |
| 2 | 4 | 84,0 |
| 1 | 8 | **85,2** |

Một expert/prompt tốt nhất ở stage cuối. Cách hiểu là mỗi expert có key riêng và có thể được route độc lập; nhiều experts dùng chung một key làm routing thô hơn. [[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf#page=7|Table 3, PDF tr. 7]]

### Task predictor

Trung bình tự tính từ 10 cột của Table 4:

| Dataset | WAVE-CRE | HiDe-Prompt | EPI |
|---|---:|---:|---:|
| FewRel | 86,17 | 80,09 | 62,67 |
| TACRED | 79,31 | 72,01 | 62,53 |

Relation-level predictor cải thiện task inference trung bình, nhưng không thắng mọi task. Trên TACRED, HiDe-Prompt cao hơn WAVE-CRE ở $T_6$ và $T_8$. Prompt-pool misrouting vì vậy vẫn là failure mode thật, không chỉ là vấn đề đã được giải quyết hoàn toàn. [[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf#page=7|Table 4, PDF tr. 7]]

## Tôi hiểu được gì

- Freeze old prompt pools chỉ bảo vệ task-specific parameters; nó không bảo vệ shared relation classifier. Vì vậy WAVE-CRE vẫn cần latent replay.
- Prompt pool làm hai việc khác nhau: pool riêng tạo separation giữa task; routing theo query tạo specialization bên trong task.
- Task predictor mang tên “task predictor” nhưng thực chất học relation-level logits rồi ánh xạ relation về task. Đây là cách tạo semantic classes ổn định hơn task IDs phụ thuộc thứ tự.
- “Rehearsal-free” ở paper có nghĩa không lưu raw examples. WAVE-CRE vẫn replay synthetic query/prompted representations và vẫn lưu statistics của quá khứ.
- Contribution mạnh nhất không phải một loss đơn lẻ mà là decomposition của forgetting theo nơi nó xuất hiện: pool, router và classifier.

## Quan hệ với WAVE++

[[WAVE++ - Capturing Within-Task Variance for Continual Relation Extraction|WAVE++]] là phần mở rộng trực tiếp của WAVE-CRE. WAVE++ ghi rõ một phần công trình đã xuất hiện trong paper này, rồi giữ lại task-specific prompt pools và Gaussian latent replay nhưng thay đổi hai mảnh quan trọng. [[Capturing Within-Task Variance for Continual Relation Extraction with Adaptive Prompting.pdf#page=15|WAVE++ PDF, tr. 15]]

| Thành phần | WAVE-CRE | WAVE++ |
|---|---|---|
| Prompt pools | Task-specific, query-key routing | Giữ lại, phân tích sâu hơn theo sparse-MoE |
| Semantic anchor | Không dùng label descriptions | Thêm label-description contrastive alignment |
| Task inference | Train relation-level MLP predictor | Cascade voting, không train task predictor riêng |
| Shared classifier | Gaussian latent replay | Giữ lại và ablate sâu hơn |
| Trainable parameters | 3,8M | 3,5M |
| Trade-off | Inference nhanh hơn, predictor có thể drift | Accuracy/task inference tốt hơn nhưng inference chậm hơn |

Ở $T_{10}$, WAVE++ tăng từ 85,0 lên 87,7 trên FewRel và từ 78,7 lên 82,5 trên TACRED, tương ứng +2,7 và +3,8 điểm so với WAVE-CRE. Vì vậy nên đọc WAVE-CRE như nền tảng kiến trúc, còn WAVE++ là bản sửa failure mode task inference và representation discrimination. [[Capturing Within-Task Variance for Continual Relation Extraction with Adaptive Prompting.pdf#page=16|WAVE++ PDF, tr. 16]]

## Hạn chế và giả định

### Paper tự nêu

- Retaining past-task knowledge vẫn khó; forgetting xuất hiện khi prompt pools không được sử dụng đúng ở testing.
- Prefix-tuning experts hiện là các offset vectors tương đối đơn giản; capacity còn hạn chế.
- Gaussian được chọn vì gọn, nhưng alternative generative models có thể mô hình hóa distribution tốt hơn. [[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf#page=5|PDF, tr. 5]] [[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf#page=7|PDF, tr. 7]]

### Đánh giá từ evidence

- **Không phải zero-memory:** raw text không được lưu, nhưng mỗi relation vẫn có prompt parameters, mean và covariance matrices. Nếu covariance là full matrix, memory có thể tăng theo $O(|R|D^2)$; paper không nói rõ diagonalization hoặc shrinkage.
- **Privacy là động cơ, chưa phải kết luận:** không có membership-inference test, reconstruction attack hoặc formal privacy guarantee.
- **Single-Gaussian assumption:** một Gaussian/relation có thể không mô tả tốt representation đa mode; paper không đánh giá distribution fit.
- **Task boundary/closed world:** training biết task hiện tại và relation sets; inference chỉ xét cumulative known relation set. Chưa phải online/open-world CRE có boundary mơ hồ.
- **Evaluation hẹp:** chỉ FewRel và TACRED theo một protocol 10-task; chưa kiểm tra domain shift rộng hoặc nhiều task orders.
- **Thiếu uncertainty:** tables chỉ báo mean của 5 seeds, không có standard deviation, confidence interval hoặc significance test.
- **Thiếu ablation module replay:** không tách riêng tác dụng của $G_q^r$, $G_z^r$ và relation-level predictor.
- **Reproducibility:** 9 trang không nêu đầy đủ $M$, $\lambda$, batch size, epochs và random-search space; không thấy code URL.
- **Variance chưa được đo trực tiếp:** within-task/cross-task variance được lập luận qua kiến trúc và accuracy ablations, không có metric variance riêng.
- **Ký hiệu routing mơ hồ:** `argmin`/cosine similarity ở Eq. 13-15 cần đối chiếu implementation trước khi tái lập.

## Câu hỏi review

1. CRE khác supervised relation extraction thông thường ở điểm nào?
2. Vì sao freeze old prompt pools vẫn chưa đủ ngăn catastrophic forgetting?
3. Task-specific prompt pool đồng thời xử lý cross-task và within-task variance như thế nào?
4. Prefix tuning được diễn giải như Mixture of Experts ra sao?
5. Vì sao paper chọn một expert cho mỗi prompt?
6. Tại sao WAVE-CRE cần hai Gaussian $G_q^r$ và $G_z^r$?
7. Task predictor dự đoán task ID trực tiếp hay relation?
8. Main results chứng minh điều gì và chưa chứng minh điều gì?
9. Ablation nào hỗ trợ trực tiếp nhất cho prompt-pool hypothesis?
10. Vì sao gọi WAVE-CRE là rehearsal-free cần thêm điều kiện?
11. WAVE++ thay đổi failure mode nào của WAVE-CRE?

## Gợi ý trả lời câu hỏi review

1. CRE nhận relation sets tuần tự và phải giữ accuracy trên toàn bộ relation cũ sau mỗi task, thay vì train một lần trên dataset cố định.
2. Old pools giữ task-specific knowledge, nhưng shared classifier vẫn bị update trên relation mới và có thể dịch decision boundary khỏi relation cũ.
3. Pool riêng giảm sharing giữa task; query-key routing chọn experts khác nhau cho các vùng dữ liệu khác nhau trong cùng task.
4. Prefix key/value vectors được xem như các experts mới tham gia attention cùng pre-trained experts.
5. Mỗi expert có key riêng, route độc lập và không bị buộc đi cùng các experts khác trong một prompt dài.
6. $G_q^r$ củng cố task/pool inference; $G_z^r$ củng cố shared relation classifier.
7. Predictor xuất logits theo relation trong $\hat R_t$, sau đó relation dự đoán được ánh xạ về task/pool.
8. Kết quả cho thấy WAVE-CRE mạnh hơn các rehearsal-free baselines và cạnh tranh với rehearsal-based methods trên hai benchmark; chưa chứng minh privacy, zero-memory hoặc generalization ngoài protocol đó.
9. Table 2: task-incremental TACRED tăng từ 83,4 lên 85,2 ở $T_{10}$ khi dùng prompt pool.
10. Method không giữ raw examples nhưng vẫn sinh và replay latent representations từ per-relation Gaussian statistics.
11. WAVE++ thêm semantic label descriptions và thay learned task predictor bằng cascade voting; prompt pools và latent replay vẫn là nền tảng kế thừa.

## Câu hỏi nghiên cứu tiếp theo

- [ ] Full covariance, diagonal covariance và low-rank covariance đánh đổi memory/accuracy thế nào khi số relation tăng?
- [ ] Mixture of Gaussians, normalizing flow hoặc diffusion latent generator có giảm replay bias so với một Gaussian/relation không?
- [ ] Task-pool routing error đóng góp bao nhiêu vào relation error tổng, và có thể calibrate uncertainty để fallback qua nhiều pools không?
- [ ] WAVE-CRE ổn định thế nào dưới nhiều task orders và khi relation distributions drift theo thời gian?
- [ ] Latent statistics có cho phép reconstruction hoặc membership inference không?
- [ ] Có thể bỏ task boundaries lúc training và phát hiện task/relation mới online không?
- [ ] Đóng góp riêng của query replay, prompted-representation replay và relation-level predictor là bao nhiêu?
- [ ] Within-task variance có thể được đo trực tiếp bằng representation geometry thay vì chỉ suy ra từ accuracy không?
- [ ] Khi backbone được phép thích nghi, cần bảo vệ shared encoder khỏi forgetting bằng cơ chế nào?

## Evidence map

| Trang PDF | Evidence chính | Dùng để kết luận |
|---|---|---|
| [[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf#page=1\|PDF tr. 1]] | Abstract, CRE motivation, bốn hạn chế của prompt-based methods | Problem, gap, đóng góp |
| [[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf#page=2\|PDF tr. 2]] | Figure 1, CRE formulation, MoE và sparse routing | Objective tổng quát, background |
| [[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf#page=3\|PDF tr. 3]] | Prefix tuning như experts, ba stage methodology, Eq. 3-12 | MoE interpretation, pool definition |
| [[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf#page=4\|PDF tr. 4]] | Figure 2, key-query selection, $L_p=2$, sparse-MoE score | Data flow, within-task routing, inference |
| [[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf#page=5\|PDF tr. 5]] | Eq. 15-19, Gaussian replay, task predictor, Algorithm 1 | Losses, training loop, classifier consolidation |
| [[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf#page=6\|PDF tr. 6]] | Datasets, baselines, compute, Table 1-2 | Protocol, main results, prompt-pool ablation |
| [[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf#page=7\|PDF tr. 7]] | Table 3-4 và conclusion | Expert-count ablation, task prediction, limitations |
| [[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf#page=8\|PDF tr. 8]] | References phần đầu | Nguồn nền về CRE, BERT, prompt tuning, MoE |
| [[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf#page=9\|PDF tr. 9]] | References phần cuối | Nguồn nền về continual learning và prompting |

## Liên kết

- [[04 - Concepts/Continual Learning|Continual Learning]]
- [[Catastrophic Forgetting]]
- [[Continual Relation Extraction]]
- [[Relation Extraction]]
- [[Prefix Tuning]]
- [[Prompt Pool]]
- [[Mixture of Experts]]
- [[Task Identity Inference]]
- [[Replay in Continual Learning]]
- [[WAVE++ - Capturing Within-Task Variance for Continual Relation Extraction]]
- [[Zotero Integration Workflow]]
