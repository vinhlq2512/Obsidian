---
type: paper-reading
date: 2026-08-21
status: draft
workflow: gemini-notebook
template: "[[Paper Reading Gemini Notebook Workflow]]"
paper: "[[Adaptive Prompting for Continual Relation Extraction]]"
pdf: "[[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf]]"
paper_note: "[[Adaptive Prompting for Continual Relation Extraction]]"
notebook_url:
target_minutes: 90
actual_minutes:
reading_goal: "Hiểu WAVE-CRE theo deep workflow: within-task variance, prompt pool, sparse MoE routing, latent replay, task prediction, results và ablation."
current_phase: scaffolded
completed: false
need_review: true
review_date:
created_at: 2026-08-21
updated_at: 2026-09-02
tags:
  - paper-reading
  - gemini-notebook
  - relation-extraction
  - continual-learning
---

# 2026-08-21 - WAVE-CRE - Gemini Notebook Workflow

> [!note] Ranh giới
> Đây là working note scaffold từ paper note/PDF để hỗ trợ đọc với Gemini Notebook. Những phần có dạng “gợi ý trả lời” là scaffold học tập, không phải bằng chứng bạn đã tự closed-book recall hay đọc xong paper.

## Setup

- Paper: [[Adaptive Prompting for Continual Relation Extraction]]
- PDF: [[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf]]
- Paper note chính: [[Adaptive Prompting for Continual Relation Extraction]]
- Gemini Notebook / NotebookLM URL:
- Mục tiêu buổi đọc: hiểu vì sao một prompt/task chưa đủ, WAVE-CRE route input vào prompt experts thế nào, và replay/task predictor đóng góp gì.
- Phần cần đọc trước: Introduction, Framework, Table 1, Ablations, Conclusion.
- PDF count đã kiểm tra: 9 trang.

## Từ điển khái niệm nhanh

| Khái niệm | Định nghĩa ngắn trong paper này | Vì sao quan trọng | Link |
|---|---|---|---|
| CRE | Continual Relation Extraction: học relation mới theo task stream và phân loại trên toàn bộ relation đã thấy. | Đây là setting chính của WAVE-CRE. | [[Continual Relation Extraction]] |
| WAVE-CRE | Adaptive prompting method nhìn CRE từ vấn đề within-task variance. | Đây là paper gốc trước bản mở rộng WAVE++. | [[Adaptive Prompting for Continual Relation Extraction]] |
| Within-task variance | Độ đa dạng mode/semantic pattern giữa examples trong cùng một task. | Paper cho rằng một prompt/task khó bao phủ hết variance này. | [[Adaptive Prompting for Continual Relation Extraction]] |
| Prompt pool | Tập nhiều prefix/prompt experts dành cho một task. | Cho phép nhiều cách điều kiện hóa PLM thay vì một prompt cố định. | [[Prompt Pool]] |
| Prefix tuning | Chèn trainable prefix vectors vào attention layers thay vì sửa toàn bộ backbone. | Là cơ chế parameter-efficient để tạo prompt experts. | [[Prompt Tuning]], [[Prefix Tuning]] |
| Sparse MoE routing | Chọn một phần nhỏ experts phù hợp với input/task thay vì dùng tất cả. | Giúp mỗi input đi qua prompt expert phù hợp với mode của nó. | [[Mixture of Experts]] |
| Task predictor | Module dự đoán task/relation group khi inference. | Là assumption quan trọng vì inference cần biết prompt pool nào nên dùng. | [[Continual Relation Extraction]] |
| Latent generative replay | Sinh/replay vectors trong latent space cho relation cũ thay vì lưu toàn bộ raw data. | Giảm forgetting ở classifier nhưng phụ thuộc Gaussian/latent assumption. | [[Replay in Continual Learning]] |
| Gaussian latent assumption | Mô hình hóa representation của relation cũ bằng phân phối Gaussian. | Là nền cho synthetic latent replay, nhưng có thể yếu nếu class đa mode. | [[Replay in Continual Learning]] |
| Class-incremental evaluation | Sau mỗi task, candidate labels là tất cả relation đã học. | Là cách đọc kết quả chính, khác với chỉ test task hiện tại. | [[Continual Relation Extraction]] |

## Phase 1 - Paper Map

### Prompt gửi Gemini

```text
Do not summarize the paper in detail yet. Create a structural map of this paper and identify problem, motivation, gap, contributions, pipeline, components, losses, datasets, baselines, metrics, main experiments, ablations, and limitations. For every item, point to the relevant section, figure, table, or equation. The purpose is to tell me WHERE to read, not to replace my reading.
```

### Paper map - scaffold từ nguồn

- **Problem:** CRE phải học relation mới tuần tự nhưng vẫn phân loại trên toàn bộ relation đã thấy. [[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf#page=2|PDF tr. 2]]
- **Motivation:** trong một task, examples có nhiều mode khác nhau; một prompt cố định có thể underfit within-task variance. [[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf#page=1|PDF tr. 1]]
- **Gap:** prompt-based CRE trước đó chưa mô hình hóa đủ đa dạng nội bộ của từng task.
- **Main idea:** tạo task-specific prompt pool gồm nhiều prefix experts; input route tới expert phù hợp; latent replay giữ relation cũ.
- **Main contributions:** adaptive prompting, sparse-MoE scoring, latent-space generative replay, task predictor cho inference.
- **Important figure:** framework/method ở phần chính. [[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf#page=3|PDF tr. 3]]
- **Important equations:** prefix/prompt expert, sparse scoring, objective học task mới, latent replay. [[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf#page=4|PDF tr. 4]], [[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf#page=5|PDF tr. 5]]
- **Main result table:** Table 1. [[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf#page=6|PDF tr. 6]]
- **Ablation table:** task-specific pool, number of experts, task predictor. [[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf#page=7|PDF tr. 7]]
- **Limitations:** task prediction dependency, Gaussian latent replay assumption, prompt pool cost.

### Chỗ cần đọc trước

- [x] Abstract + Introduction
- [x] Prefix tuning/MoE formulation
- [x] Task-specific prompt pool
- [x] Objective + latent replay
- [x] Table 1
- [x] Ablations

## Phase 2 - Pass 1 Recall

### Closed-book recall của tôi

**Problem**

- WAVE-CRE **không được thiết kế riêng cho kịch bản few-shot** giống như hai bài báo trước (CPL và ConPL) mà bạn đã đọc. Bài báo này giải quyết bài toán **Continual Relation Extraction (CRE) tiêu chuẩn**. Ở đây, mô hình học trên toàn bộ tập dữ liệu huấn luyện đầy đủ của FewRel và TACRED (chia làm 10 tác vụ) chứ không bị giới hạn nghiêm ngặt về số lượng mẫu huấn luyện (K-shot) ở mỗi bước học
- Thách thức song hành ở đây không phải là "overfitting do ít mẫu" mà là **catastrophic forgetting (quên lãng thảm họa) song hành với mối lo ngại về bảo mật quyền riêng tư của dữ liệu (privacy/security concerns)** khi lưu trữ mẫu vật lý trong bộ nhớ. Đây là lý do mô hình hướng tới giải pháp **không lưu mẫu vật lý (rehearsal-free)**

**Why does it matter?**

- Trong thực tế, các quan hệ mới xuất hiện liên tục. Việc học liên tục (Continual Learning) giúp hệ thống tích lũy thêm tri thức mới mà không cần giữ lại toàn bộ kho dữ liệu cũ khổng lồ (vốn có thể bị xóa đi vì lý do bảo mật hoặc giới hạn lưu trữ)
**Research gap**

1. **Shared parameters vẫn quên:** shared prompt pool, general prompt hoặc shared MLP classifier tiếp tục bị update theo task mới.
2. **Sai task/prompt ở inference:** training biết task đang học, nhưng test phải tự chọn prompt pool; chọn sai tạo train-test mismatch.
3. **Cross-task variance chưa đủ:** một shared prompt pool có thể khiến samples thuộc các task khác nhau chọn chung expert, làm task-specific knowledge khó tách biệt.
4. **Within-task variance chưa đủ:** một prompt cố định cho cả task không đủ linh hoạt để biểu diễn nhiều context/mode bên trong cùng task.

**Main idea**

- Tạo một task-specific prompt pool cho mỗi task; nhiều prompt ngắn cho phép chọn các prefix experts khác nhau theo input.
- Diễn giải [[Prefix Tuning]] qua lăng kính [[Mixture of Experts]] để giải thích vì sao một prompt có thể xem như thêm experts vào self-attention.
- Fit per-relation Gaussian distributions trong query space và prompted-representation space để replay latent samples mà không lưu instance gốc.
- Train relation-level task predictor và shared relation classifier trên synthetic representations của toàn bộ relation đã thấy. [[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf#page=2|PDF, tr. 2]]

**Main contribution**

- **Vạch rõ hạn chế của các phương pháp Prompt cũ:** Chỉ ra một cách hệ thống các điểm yếu về quên tham số chia sẻ, mismatch pha test, và quản lý phương .
- **Khung WAVE-CRE tối ưu hóa phương sai:** Sử dụng task-specific prompt pool với thiết lập độ dài prompt ngắn nhất ($L=1$ expert/prompt) để mỗi expert tự sở hữu khóa (key) riêng, tạo ra sự linh hoạt tối đa khi chọn prompt theo ngữ cảnh đầu vào (within-task variance).
- **Generative Latent Replay & Precise Task Predictor:** Sử dụng hai mô hình sinh phân phối Gaussian độc lập để vừa tái tạo đặc trưng ẩn cho bộ phân loại, vừa huấn luyện bộ dự đoán tác vụ chi tiết đến từng quan hệ (relation-level) (khắc phục việc gom cụm thô sơ của HiDe-Prompt)

**Main result**

- WAVE-CRE vượt rõ các rehearsal-free baselines ở stage cuối và gần ngang rehearsal-based methods dù không giữ raw training instances. Tuy nhiên kết luận nên có nuance:

	- WAVE-CRE vượt rehearsal-based tốt nhất ở FewRel $T_{10}$ chỉ 0,2 điểm.
	- Trên TACRED $T_{10}$, WAVE-CRE vẫn thấp hơn CRE-DAS 0,4 điểm.
	- Claim “consistently outperforms” rehearsal-free methods có ngoại lệ ở FewRel $T_1$: EPI đạt 98,3 còn WAVE-CRE đạt 97,9. [[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf#page=6|Table 1, PDF tr. 6]]

### Prompt kiểm tra recall

```text
I have completed the first pass of the paper.

Here is my understanding:

[PASTE MY NOTES]

Compare my understanding against the paper. Return what is correct, inaccurate, missing, confusing, and which sections/citations I should revisit. Do not rewrite the entire paper for me.
```

## Phase 3 - Problem / Motivation / Gap

| Mục | Diễn giải bằng lời của tôi | Evidence / citation |
|---|---|---|
| General problem | Class-incremental CRE yêu cầu model dự đoán trên tất cả relation đã học, không chỉ relation của task hiện tại. | [[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf#page=2\|PDF tr. 2]] |
| Why it matters | Relation mới xuất hiện liên tục, còn dữ liệu cũ thường không thể giữ đầy đủ. | [[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf#page=1\|PDF tr. 1]] |
| What prior work solves | Prompt tuning dùng PLM/prefix để thích nghi task với ít tham số trainable hơn. | [[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf#page=3\|PDF tr. 3]] |
| What prior work fails to solve | Một prompt/task không đủ bắt nhiều mode trong cùng task. | [[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf#page=1\|PDF tr. 1]] |
| Exact research gap | Cần adaptive prompt selection ở cấp input/task để mô hình hóa within-task variance. | [[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf#page=4\|PDF tr. 4]] |
| Hypothesis / intuition | Nhiều prompt experts giúp input khác nhau trong cùng task có adapter phù hợp hơn; latent replay bảo vệ classifier khỏi bias task mới. | inferred |
| Contribution addressing the gap | WAVE-CRE thêm task-specific prompt pool, sparse routing và latent generative replay. | [[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf#page=4\|PDF tr. 4]], [[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf#page=5\|PDF tr. 5]] |

### Câu hỏi tự kiểm tra

- [x] Within-task variance trong RE khác class imbalance như thế nào?
  - **Class imbalance** nói về số lượng mẫu không đều giữa các class/relation, ví dụ một relation có nhiều gradient hơn relation khác.
  - **Within-task variance** nói về độ đa dạng semantic/linguistic/representation bên trong cùng một task, thậm chí khi số mẫu giữa relation đã balanced. Trong RE, cùng một task có thể chứa nhiều relation khác nhau, và ngay trong một relation như `employee_of` cũng có nhiều pattern diễn đạt khác nhau.
  - Vì vậy câu hỏi của WAVE không phải “class nào thiếu mẫu?”, mà là “một prompt/task có đủ linh hoạt để bao phủ nhiều mode trong cùng task không?”. [[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf#page=1|PDF tr. 1]]
- [x] Prompt pool đang giải quyết underfitting trong task hay forgetting giữa task?
  - **Chủ yếu là representational underfitting / insufficient adaptation capacity bên trong task.** WAVE cho rằng một fixed set of simple prefix experts cho toàn bộ task có thể không đủ flexible để capture within-task variation, nên chuyển từ một prompt/task sang một task-specific prompt pool và chọn Top-K experts theo input. [[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf#page=4|PDF tr. 4]]
  - **Nhưng prompt pool cũng gián tiếp giúp forgetting** nhờ parameter isolation: khi học task mới, pool của task mới được train còn prompt pools cũ được giữ lại, làm giảm cross-task interference.
  - **Prompt pool không đủ để chống catastrophic forgetting**, vì WAVE vẫn có shared relation classifier và task predictor. Do đó paper cần latent generative replay: $G_z^r$ bảo vệ classifier, còn $G_q^r$ bảo vệ task predictor. [[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf#page=5|PDF tr. 5]]
- [x] Task predictor có phải assumption inference quan trọng không?
  - **Có.** WAVE không cần oracle task ID ở test time, nhưng vẫn không hoàn toàn task-free: nó cần suy luận $x \rightarrow \hat r \rightarrow \hat t$ để chọn đúng prompt pool $\mathcal P_{\hat t}$. [[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf#page=5|PDF tr. 5]]
  - Đây là bottleneck vì nếu task predictor đoán sai task, downstream pipeline nhận sai adaptation: wrong task -> wrong pool -> wrong prompts -> prompted representation sai -> relation classifier dễ sai.
  - Nuance quan trọng: task predictor không nhất thiết phải đoán đúng relation để routing thành công; nếu relation đoán nhầm vẫn thuộc cùng task với relation thật thì pool vẫn đúng. Vì vậy metric ngầm cần quan tâm là **TaskRoutingAccuracy**, không chỉ relation accuracy của predictor.

**Một câu nối sang research gap:** WAVE tạo trade-off: task-specific prompt pool tăng specialization và giảm interference, nhưng đổi lại phụ thuộc nhiều hơn vào routing đúng task. Câu hỏi mở tự nhiên là: **có thể giữ instance-level specialization mà không cần task-level routing không?**

## Phase 4 - Method / Architecture

### Tôi tự vẽ trước

```text
Sentence + entity markers
-> PLM encoder
-> task-specific prompt pool / prefix experts
-> sparse scoring chọn prompt experts phù hợp với input
-> relation representation
-> relation classifier trên labels đã thấy
-> latent generative replay cho relation cũ
-> task predictor hỗ trợ inference khi task identity không biết
```

### Component map

| Component | Input | Operation | Output | Purpose | Evidence |
|---|---|---|---|---|---|
| Prefix expert | hidden state/query | thêm learned prefix vào self-attention | prompted representation | parameter-efficient adaptation | [[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf#page=3\|PDF tr. 3]] |
| Task-specific prompt pool | task id, input representation | lưu nhiều experts cho một task | candidate prompts | bắt within-task variance | [[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf#page=4\|PDF tr. 4]] |
| Sparse-MoE scoring | input query + prompt keys | chọn/pha trộn prompt experts | routed representation | dùng prompt phù hợp từng input | [[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf#page=4\|PDF tr. 4]] |
| Latent generative replay | old relation latent distribution | sample latent cũ trong training task mới | replay features | giảm classifier forgetting | [[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf#page=5\|PDF tr. 5]] |
| Task predictor | input representation | dự đoán task/relation candidate | task identity estimate | inference khi không có task label | [[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf#page=5\|PDF tr. 5]] |

### Điều tôi vẫn chưa hiểu

- [x] Sparse score có dùng top-k hard selection hay soft mixture?
  - Paper dùng cơ chế **Top-K prompt selection**: query vector $q(x)$ được so với các prompt keys $k_j^{(t)}$, rồi chọn tập $K_x$ gồm $K$ prompts gần nhất. Phần được chọn là hard subset ở mức prompt/expert, còn attention bên trong BERT vẫn là soft attention trên key/value. [[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf#page=4|PDF tr. 4]]
  - Điểm mơ hồ cần giữ lại nếu reproduce: Eq. 13 dùng `argmin` trong khi text gọi $\gamma$ là cosine similarity; cách viết nhất quán hơn là hiểu $\gamma$ như distance hoặc negative similarity.
- [x] Gaussian latent replay được fit theo relation hay task?
  - Fit **theo relation** $r \in \hat R_t$, không phải theo task. Mỗi relation có hai phân phối: $G_q^r$ cho query representations và $G_z^r$ cho prompted relation representations. [[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf#page=5|PDF tr. 5]]
  - Vì fit theo relation, replay giữ decision boundary ở cấp relation label, rồi task predictor có thể map relation dự đoán về task/prompt pool.
- [x] Task predictor sai ảnh hưởng bao nhiêu đến relation classifier?
  - Paper không báo cáo ablation “oracle task predictor vs wrong predictor” trực tiếp, nên chưa định lượng chính xác được propagation error.
  - Về pipeline, sai task predictor có thể chọn sai prompt pool, khiến prompted representation $z$ sai trước khi vào relation classifier. Table 4 chỉ cho thấy WAVE-CRE cải thiện task prediction precision so với EPI/HiDe-Prompt trung bình, nhưng vẫn có task mà WAVE-CRE không cao nhất. [[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf#page=7|PDF tr. 7]]

## Phase 5 - Section Recall

### Framework - Adaptive prompting

- **Input:** sentence/entity pair và task hiện tại.
- **Process:** route input tới prompt experts trong task-specific pool.
- **Output:** representation đã được prompt điều kiện hóa.
- **Purpose:** thay một prompt cố định bằng nhiều prompt nhỏ để bao phủ variance.
- **Caveat:** prompt pools tăng số tham số theo số task/pool; paper báo tổng 114M parameters và 3.8M trainable parameters trong setup của họ, nhưng không tách chi phí theo từng $M$/task trong main text.

### Framework - Generative replay

- **Input:** latent statistics của relation cũ.
- **Process:** sample latent replay trong khi học task mới.
- **Output:** synthetic old features cho classifier.
- **Purpose:** tránh classifier bias về relation mới.
- **Caveat:** một Gaussian/relation gọn về memory, nhưng có thể yếu nếu relation distribution đa mode; paper nêu future work có thể thử generative models khác.

### Experiments - Detailed analysis

- **Task-specific prompt pool:** Table 2 kiểm trong task-incremental TACRED, nơi task identity được cung cấp để loại nhiễu task prediction. WAVE-CRE đạt 85.2 ở $T_{10}$, còn biến thể một prompt/task đạt 83.4, tức +1.8 điểm cho prompt pool. [[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf#page=6|PDF tr. 6]]
- **Number of experts per prompt:** Table 3 giữ tổng số selected experts $L\times K=8$. Cấu hình $L=1,K=8$ tốt nhất ở TACRED $T_{10}$, ủng hộ ý rằng routing mịn theo từng expert linh hoạt hơn bundle nhiều experts dưới một key. [[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf#page=7|PDF tr. 7]]
- **Task predictor:** Table 4 đo task prediction precision sau khi train task 10. WAVE-CRE cao hơn EPI/HiDe-Prompt trung bình nhờ relation-level predictor, nhưng vẫn không thắng mọi task, nên routing vẫn là bottleneck. [[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf#page=7|PDF tr. 7]]

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
| Prefix tuning / Eq. 3-12 | Diễn giải prompt như prefix experts trong self-attention. | $X,P_k,P_v$ -> hidden states đã được prompt điều kiện hóa. | Encoder stage sau khi chọn prompts. | Thích nghi frozen BERT bằng trainable prefix vectors thay vì fine-tune toàn bộ backbone. | Model mất cơ chế adaptation parameter-efficient; prompt pool không còn “experts” để route. | [[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf#page=3\|PDF tr. 3]] | source-checked |
| Top-K key-query selection / Eq. 13 | Chọn prompts phù hợp với input trong pool của task. | $q(x),k_j^{(t)}$ -> subset $K_x$ gồm $K$ prompts. | Trước khi prepend prompts vào input embedding. | Input khác nhau trong cùng task dùng experts khác nhau. | Quay về một prompt/task hoặc chọn prompt kém phù hợp, làm yếu within-task adaptation. | [[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf#page=4\|PDF tr. 4]], [[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf#page=6\|Table 2, PDF tr. 6]] | source-checked |
| Shared auxiliary score / Eq. 14 | Giảm chi phí sparse expert scoring. | $q(x),k_j^{(t)}$ -> score dùng chung cho mọi MoE model/head position. | Prompt routing trong task-specific pool. | Chỉ tính $M$ scores thay vì $N\times M$, reuse query từ task predictor. | Selection tốn hơn nhiều hoặc phải tính score riêng cho từng attention model. | [[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf#page=4\|PDF tr. 4]] | source-checked |
| New-task objective / Eq. 15 | Train pool hiện tại và relation classifier trên task mới. | $x_p,y,K_x$ -> update $P_t,\phi$. | Training task $t$. | Học relation mới và kéo prompt keys gần query features. | Prompt pool hiện tại không học specialization; classifier không cập nhật relation mới. | [[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf#page=5\|PDF tr. 5]] | source-checked |
| Gaussian $G_z^r$ / Eq. 16 | Lưu phân phối prompted representation theo relation. | $z^r=f_r(x_p^r)$ -> $\mu_z^r,\Sigma_z^r$. | Sau khi train task, trước replay classifier. | Replay old relation features không cần lưu raw examples. | Shared classifier dễ bias về relation mới. | [[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf#page=5\|PDF tr. 5]] | source-checked |
| Gaussian $G_q^r$ / Eq. 17 | Lưu phân phối query representation theo relation. | $q^r=q(x^r)$ -> $\mu_q^r,\Sigma_q^r$. | Sau khi train task, trước train task predictor. | Giữ khả năng suy luận relation/task cho routing. | Task predictor quên relation cũ, kéo theo sai prompt pool. | [[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf#page=5\|PDF tr. 5]] | source-checked |
| Task predictor loss / Eq. 18 | Train relation-level predictor để chọn task/pool. | samples từ $G_q^r$ -> logits trên $\hat R_t$. | Consolidation sau mỗi task và inference routing. | Dự đoán relation tạm có semantic meaning rồi map sang task. | Inference phải dựa vào task ID oracle hoặc dễ chọn sai pool. | [[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf#page=5\|PDF tr. 5]], [[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf#page=7\|Table 4, PDF tr. 7]] | source-checked |
| Relation classifier replay loss / Eq. 19 | Củng cố shared classifier trên toàn bộ relation đã thấy. | samples từ $G_z^r$ -> logits trên $\hat R_t$. | Consolidation sau mỗi task. | Giữ old decision boundaries dù không lưu old sentences. | Classifier bị catastrophic forgetting dù old prompt pools vẫn frozen. | [[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf#page=5\|PDF tr. 5]] | source-checked |

## Phase 7 - Loss Functions

```text
WAVE-CRE training signal
├── current-task classification
├── sparse prompt routing / expert selection
├── latent replay for old relations
└── task prediction / relation prediction at inference
```

| Loss/block | Inputs | Trains component | Behavior | Weight / hyperparameter | Ablation / evidence |
|---|---|---|---|---|---|
| Current-task classification in Eq. 15 | current task examples $(x,y)$ after prompt selection | current prompt pool $P_t$, classifier $g_\phi$ | learn new relations | paper does not isolate a named weight; standard classification term | main training objective, [[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf#page=5\|PDF tr. 5]] |
| Prompt-key matching term in Eq. 15 | $q(x)$, selected keys $k_{s_i}^{(t)}$ | prompt keys in current pool | align selected keys with query features | $\lambda$, value not specified in the 9-page paper | prompt pool/expert ablations, [[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf#page=6\|Table 2]], [[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf#page=7\|Table 3]] |
| Task predictor objective / Eq. 18 | synthetic query samples $q\sim G_q^r$ | $\hat g_\psi$ | infer relation-level routing signal, then map relation to task | no separate weight reported | Table 4 task prediction precision, [[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf#page=7\|PDF tr. 7]] |
| Relation classifier replay / Eq. 19 | synthetic prompted samples $z\sim G_z^r$ | shared classifier $g_\phi$ | retain old relation decision boundaries | no separate weight reported | paper motivates replay but does not provide a clean module-level ablation separating $G_q^r$ and $G_z^r$ |

## Phase 8 - Experiments

| Experiment | Research question | Dataset | Baselines | Metric | Table/Figure | Main result | Caveat |
|---|---|---|---|---|---|---|---|
| Main CRE results | WAVE-CRE có tốt hơn CRE baselines không? | FewRel/TACRED | prompt/replay CRE baselines | accuracy by learning stage | Table 1 | FewRel $T_{10}$ 85.0, TACRED $T_{10}$ 78.7 theo paper note chính | reported, not reproduced |
| Prompt pool ablation | nhiều prompt/task có hơn một prompt/task không? | TACRED task-incremental | WAVE-CRE vs không prompt pool | final accuracy | Table 2 | $T_{10}$ tăng từ 83.4 lên 85.2, tức +1.8 | chỉ trong framework này |
| Number of experts | thêm experts có luôn tốt hơn không? | TACRED | $L,K$ variants giữ $L\times K=8$ | accuracy | Table 3 | $L=1,K=8$ đạt 85.2 ở $T_{10}$, tốt nhất trong sweep | cost/routing trade-off |
| Task predictor | task identity inference ảnh hưởng thế nào? | FewRel/TACRED | WAVE-CRE, HiDe-Prompt, EPI | task prediction accuracy | Table 4 | trung bình WAVE-CRE cao hơn HiDe-Prompt/EPI, nhưng không thắng mọi task | predictor vẫn là bottleneck tiềm năng |

### Protocol fingerprint

- Dataset and split: FewRel có 80 relation types, 56.000 samples, chia thành 10 sub-datasets không chồng lấn theo Wang et al. 2019; TACRED có 42 relations, 106.264 samples, chia thành 10 sub-datasets theo Cui et al. 2021. [[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf#page=6|PDF tr. 6]]
- Scenario / label space: continual relation extraction, evaluate accuracy qua learning stages trên relation đã thấy.
- Backbone: BERT encoder bị freeze; WAVE-CRE có 114M parameters tổng và 3.8M trainable parameters.
- Seeds / number of runs: mean accuracy trên 5 random seeds.
- Metric and averaging: average accuracy theo từng learning stage $T_1\ldots T_{10}$.
- Memory/replay: không lưu raw training instances; lưu Gaussian statistics cho query và prompted representations theo relation.
- Task identity at inference: không nhận oracle task ID; dùng task predictor để chọn prompt pool.
- Compute / time: một NVIDIA A100; khoảng 7 giờ trên FewRel và 3 giờ trên TACRED.
- Hyperparameters: tuned bằng random search; paper nói giữ prompt-pool size $M$ nhất quán qua tasks, nhưng không nêu đầy đủ search space trong 9 trang.

## Phase 9 - Claim to Evidence

| Claim | Where claim appears | Experiment | Evidence | My judgment | Caveat |
|---|---|---|---|---|---|
| Within-task variance là motivation chính. | Introduction | motivation | [[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf#page=1\|PDF tr. 1]] | important | paper không nhất thiết đo variance trực tiếp |
| Task-specific prompt pool là novelty method. | Framework | prompt pool | [[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf#page=4\|PDF tr. 4]] | supported | routing đã source-checked ở Eq. 13-14; implementation vẫn cần đối chiếu nếu reproduce |
| Latent replay giảm forgetting. | Framework | replay | [[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf#page=5\|PDF tr. 5]] | mechanistically plausible | note/PDF chưa tách định lượng riêng $G_q^r$ và $G_z^r$ |
| WAVE-CRE cải thiện main accuracy. | Results | Table 1 | [[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf#page=6\|PDF tr. 6]] | reported/observed | protocol-specific |
| Một expert/prompt linh hoạt hơn bundle nhiều experts/prompt. | Detailed analysis | Table 3 | [[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf#page=7\|PDF tr. 7]] | supported in TACRED task-incremental ablation | không nên tổng quát thành định luật |
| Relation-level task predictor tốt hơn task-level grouping. | Section 3.3 / Table 4 | task prediction precision | [[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf#page=5\|PDF tr. 5]], [[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf#page=7\|PDF tr. 7]] | supported on average | vẫn có task WAVE-CRE không cao nhất |

## Phase 10 - Ablation Study

| Component | Intended purpose | With component | Without component | Difference | Conclusion justified | Not justified |
|---|---|---:|---:|---:|---|---|
| Task-specific prompt pool | bắt within-task variance | TACRED $T_{10}$ 85.2 | không prompt pool 83.4 | +1.8 | pool có ích trong setup này | mọi task đều cần nhiều prompts |
| Number of experts | tăng capacity prompt | $L=1,K=8$: 85.2 | $L=8,K=1$: 84.2 | +1.0 | route độc lập theo expert có lợi | càng nhiều expert càng tốt |
| Latent replay | bảo vệ relation cũ | có query/prompted replay | chưa có ablation tách riêng từng replay module trong note chính | chưa kết luận định lượng riêng | replay là cơ chế bảo vệ classifier | Gaussian replay luôn đủ |
| Task predictor | inference task identity | WAVE-CRE trung bình FewRel 86.17 / TACRED 79.31 | HiDe-Prompt 80.09 / 72.01; EPI 62.67 / 62.53 | WAVE-CRE cao hơn trung bình | predictor ảnh hưởng end-to-end | task identity đã được giải quyết hoàn toàn |

## Phase 11 - Critical Reading

- Strongest contribution: nhìn prompt tuning như expert pool để xử lý within-task variance.
- Weakest part cần kiểm: task predictor và latent Gaussian replay có thể là bottleneck.
- Main assumption: task boundaries trong training rõ; inference có thể cần task prediction.
- Alternative explanation: gain có thể đến từ replay/classifier consolidation hơn là prompt pool riêng.
- Missing experiment: measure prompt utilization, within-task clusters, latency/memory growth.
- Generalization risk: chỉ kiểm trên FewRel/TACRED; relation semantics khác domain có thể làm routing khó hơn.
- Reproducibility risk: cần code/hyperparameter để kiểm selection và replay.

## Phase 12 - Reproduction Check

| Item | Trạng thái | Cần làm |
|---|---|---|
| PDF local | done | đã có 9 trang |
| Code | lead-found | paper/PDF/arXiv không nêu code URL trực tiếp; có repo public khớp tên paper: [mrshaw01/AdaptivePromptingCRE](https://github.com/mrshaw01/AdaptivePromptingCRE), cần đối chiếu commit/code trước khi coi là official faithful implementation |
| Dataset split | source-checked | FewRel 80 relations/56.000 samples/10 sub-datasets; TACRED 42 relations/106.264 samples/10 sub-datasets |
| Hyperparameters | partial | paper nêu random search/frozen BERT/3.8M trainable params; README repo public có lệnh mẫu: `max_length=256`, `encoder_epochs=30`, `encoder_lr=2e-5`, `prompt_pool_epochs=25`, `prompt_pool_lr=1e-4`, `classifier_epochs=250`, `batch_size=16`, `prompt_pool_size=20`, `replay_epochs=200`, `classifier_lr=5e-5`, nhưng cần map lại với ký hiệu paper |
| Main table | source-checked | đã có full stage table trong PDF; note ghi các kết quả cuối và caveat chính |
| Ablation | partial | đã điền prompt pool, expert count, task predictor; replay module-level còn thiếu |
| Compute | source-checked | 1 NVIDIA A100; FewRel khoảng 7 giờ, TACRED khoảng 3 giờ |

## Phase 13 - Completeness / Oral Exam

### Gợi ý trả lời sau khi đọc

1. **WAVE-CRE định nghĩa within-task variance thế nào?**  
   Đó là độ đa dạng semantic/representation giữa các samples bên trong cùng task, không phải chỉ lệch số lượng mẫu. Một task có thể gồm nhiều relation hoặc nhiều pattern ngôn ngữ khác nhau, nên một prompt cố định có thể không đủ biểu diễn.
2. **Task-specific prompt pool khác một prompt/task ở đâu?**  
   Một prompt/task buộc mọi input trong task dùng cùng adaptation. Task-specific prompt pool cho mỗi task một tập nhiều prompt experts, rồi query của từng input chọn Top-K experts phù hợp.
3. **Sparse-MoE scoring chọn experts bằng tín hiệu nào?**  
   Frozen BERT tạo query $q(x)$; WAVE-CRE so $q(x)$ với prompt keys $k_j^{(t)}$ trong pool của task và chọn $K$ prompts gần nhất. Cùng một set experts được dùng xuyên các MoE models để giảm chi phí scoring.
4. **Latent generative replay khác exemplar replay ở đâu?**  
   Exemplar replay giữ raw examples cũ; WAVE-CRE không giữ câu gốc mà lưu mean/covariance của query và prompted representations theo relation, rồi sample synthetic latent vectors để replay.
5. **Task predictor có thể làm sai toàn pipeline như thế nào?**  
   Nếu predictor map input sang sai task, model chọn sai prompt pool. Khi đó prompted representation $z$ đã bị điều kiện hóa sai trước khi relation classifier dự đoán nhãn cuối.
6. **Kết quả nào chứng minh prompt pool, kết quả nào chứng minh replay?**  
   Table 2 là evidence trực tiếp nhất cho prompt pool: TACRED task-incremental $T_{10}$ tăng từ 83.4 lên 85.2. Replay được paper chứng minh chủ yếu qua cơ chế Eq. 16-19 và kết quả end-to-end, nhưng note/PDF chưa có ablation tách riêng từng replay distribution.
7. **Khi so sánh với WAVE++, phần nào là tiền thân trực tiếp?**  
   WAVE-CRE cung cấp nền tảng task-specific prompt pools, fine-grained prefix expert routing và Gaussian latent replay. WAVE++ kế thừa các phần này, rồi sửa thêm failure mode task inference bằng semantic label descriptions/cascade voting.

### Prompt oral exam

```text
Quiz me on WAVE-CRE. Ask one question at a time. Focus on within-task variance, prompt pools, sparse MoE routing, latent replay, task prediction, ablation interpretation, and protocol caveats. Do not give the answer until I respond.
```

## Final Paper Note Handoff

### Ý cần chuyển sang paper note

- [x] Điền lại equation/formal blocks ở mức operational từ paper note/PDF.
- [x] Điền ablation numbers chính cho prompt pool, expert count và task predictor.
- [x] Ghi rõ task predictor là assumption/bottleneck.
- [x] Khi so sánh với WAVE++, tách phần inherited WAVE-CRE và phần WAVE++ thêm mới.
- [x] Ghi rõ boundary: paper/note chưa tách định lượng riêng của $G_q^r$ và $G_z^r$; cần code/extra experiment nếu muốn isolate replay modules.
- [x] Thêm reproduction lead và hyperparameters mẫu từ repo public, kèm cảnh báo cần đối chiếu implementation trước khi reproduce.

## Liên kết

- [[Adaptive Prompting for Continual Relation Extraction]]
- [[WAVE++ - Capturing Within-Task Variance for Continual Relation Extraction]]
- [[Prompt Pool]]
- [[Prefix Tuning]]
- [[Task Identity Inference]]
- [[Replay in Continual Learning]]
