---
type: paper-reading
date: 2026-08-19
status: completed
workflow: gemini-notebook
template: "[[Paper Reading Gemini Notebook Workflow]]"
paper: "[[Consistent Prototype Learning for Few-Shot Continual Relation Extraction]]"
pdf: "[[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf]]"
paper_note: "[[Consistent Prototype Learning for Few-Shot Continual Relation Extraction]]"
notebook_url:
target_minutes: 90
actual_minutes:
reading_goal: "Hiểu ConPL theo workflow Gemini Notebook: problem/gap, method ba stage, losses, protocol NK-CRE, claim-evidence, ablation và reproducibility."
current_phase: completed
completed: true
need_review: true
review_date:
created_at: 2026-08-19
updated_at: 2026-09-01
tags:
  - paper-reading
  - gemini-notebook
  - relation-extraction
  - continual-learning
  - few-shot-learning
---

# 2026-08-19 - ConPL - Gemini Notebook Workflow

> [!note] Ranh giới
> Đây là working note đã được scaffold từ paper note/PDF để hỗ trợ đọc với Gemini Notebook. User đã báo đã đọc xong vào 2026-08-27; các phần được điền thêm sau đó là scaffold/handoff từ note và citation sẵn có, không phải bằng chứng reproduction hay kiểm code.

## Setup

- Paper: [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction]]
- PDF: [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf]]
- Paper note chính: [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction]]
- Gemini Notebook / NotebookLM URL:
- Mục tiêu buổi đọc: hiểu vì sao ConPL cần cả sample memory và prototype memory, cách ba stage huấn luyện vận hành, và ablation chứng minh gì.
- Phần cần đọc trước: Introduction, Section 3, Section 4, Table 1-3, limitations.
- PDF count đã kiểm tra: 14 trang.

## Từ điển khái niệm nhanh

| Khái niệm | Định nghĩa ngắn trong paper này | Vì sao quan trọng | Link |
|---|---|---|---|
| CRE | Continual Relation Extraction: học relation mới theo chuỗi task và vẫn phải phân loại được tất cả relation đã thấy. | Là khung bài toán nền trước khi paper siết thêm ràng buộc few-shot. | [[Continual Relation Extraction]] |
| NK-CRE | N-way K-shot Continual Relation Extraction: mỗi task có $N$ relation mới và mỗi relation chỉ có $K$ training samples, kể cả task đầu. | Đây là protocol nghiêm ngặt mà ConPL đề xuất để tránh lợi thế base task nhiều dữ liệu. | [[Continual Few-Shot Relation Extraction]] |
| ConPL | Consistent Prototype Learning: framework dùng prompt encoder, prototype classifier, sample memory, prototype memory và consistent learning. | Đây là đóng góp chính của paper để giảm forgetting/prototype distortion. | [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction]] |
| Prototype | Vector đại diện cho một relation, thường lấy từ mean embedding hoặc exemplar gần class center. | Là class anchor cho classifier và cũng là đối tượng có thể bị distortion qua task. | [[Prototype Learning]] |
| Prototype distortion | Hiện tượng prototype/embedding geometry của relation cũ bị lệch sau khi model học task mới. | Paper coi đây là cơ chế liên quan trực tiếp đến catastrophic forgetting. | [[Prototype Learning]], [[Catastrophic Forgetting]] |
| Sample memory $\hat S^k$ | Bộ nhớ lưu raw exemplar đã chọn cho mỗi relation đến task $k$. | Cung cấp dữ liệu thật để replay, nhưng vẫn tạo storage/privacy trade-off. | [[Replay in Continual Learning]] |
| Prototype memory $\hat P^k$ | Bộ nhớ lưu prototype vector cho mỗi relation đã thấy đến task $k$. | Giữ class anchors cũ để classifier không phải recompute từ memory quá ít. | [[Prototype Learning]] |
| Temporary prototype $\tilde P^k$ | Prototype tạm của relation mới, tính từ $K$ samples trong current task trước khi chọn exemplar chính thức. | Dùng trong Stage 1 để học task mới cùng old prototype memory. | [[Prototype Learning]] |
| Current all prototypes $\bar P^k$ | Tập prototype đang tham gia loss ở task hiện tại: old prototypes cộng prototype của relation mới. | Giúp Stage 1/2 phân loại trên toàn bộ label space đã thấy. | [[Prototype Learning]] |
| $L_{cc}$ | Classification consistency loss: kéo embedding của memory sample về gần prototype đúng đã lưu. | Chống encoder drift làm old sample rời khỏi class anchor. | [[Embedding Space Regularization]] |
| $L_{dc}$ | Distribution consistency loss: giữ quan hệ similarity tương đối giữa memory sample và toàn bộ prototype memory. | Bảo vệ geometry toàn cục, không chỉ khoảng cách sample-prototype đúng. | [[Embedding Space Regularization]] |
| $L_{fc}$ | Loss trên tập target + confusing negative prototypes; paper gọi là focal loss nhưng công thức giống restricted cross-entropy hơn. | Đây là thành phần ablation mạnh nhất, tập trung vào relation dễ nhầm. | [[Contrastive Learning]] |
| Whole accuracy | Accuracy sau task $k$ trên test set của tất cả relation đã thấy. | Là metric chính trong Table 1, cần phân biệt với accuracy chỉ trên task mới. | [[Continual Few-Shot Relation Extraction]] |
| Mean forgetting | Metric đo mức giảm hiệu năng trên task cũ sau khi học các task sau. | Table 3 dùng nó để bổ sung evidence ngoài final accuracy. | [[Catastrophic Forgetting]] |

## Phase 1 — Paper Map

### Prompt gửi Gemini

```text
Do not summarize the paper in detail yet. Create a structural map of this paper and identify problem, motivation, gap, contributions, pipeline, components, losses, datasets, baselines, metrics, main experiments, ablations, and limitations. For every item, point to the relevant section, figure, table, or equation. The purpose is to tell me WHERE to read, not to replace my reading.
```

### Paper map — scaffold từ nguồn

- **Problem:** Few-shot continual relation extraction: model học relation mới theo chuỗi task nhưng vẫn phải phân loại đúng tất cả relation đã thấy. Đọc Introduction và Section 3. [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=1|PDF tr. 1]], [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=3|PDF tr. 3]]
- **Motivation:** replay ít exemplar có thể không giữ representation/prototype cũ ổn định; relation gần nghĩa như `father`/`mother` dễ bị confusion. [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=1|PDF tr. 1]]
- **Gap:** protocol CFRL trước đó không strict few-shot cho task đầu; các phương pháp memory trước đó chưa giải quyết đủ prototype distortion và confusing classes. [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=2|PDF tr. 2]]
- **Main idea:** lưu cả sample memory và prototype memory; dùng prototype classifier, consistency losses và confusing-class classification.
- **Main contributions:** NK-CRE setting, ConPL architecture, multi-information memory, ba-stage training, evaluation trên FewRel/TACRED.
- **Important figure:** Figure 1 về prototype distortion/forgetting; Figure 2 về distribution của class gần nhau.
- **Important equations:** Eq. 1 prompt encoder; Eq. 2 prototype; Eq. 3 classifier; Eq. 5 $L_{cc}$; Eq. 7 $L_{fc}$; Eq. 8 $L_{dc}$; Eq. 9-10 objectives. [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=4|PDF tr. 4]], [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=5|PDF tr. 5]]
- **Main result table:** Table 1 accuracy theo task. [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=7|PDF tr. 7]]
- **Ablation table:** Table 2 component ablation; Figure 4 consistency loss analysis. [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=8|PDF tr. 8]], [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=9|PDF tr. 9]]
- **Limitations:** storage overhead của prototype memory, outlier distortion-forgetting chưa phân tích, domain adaptability để future work. [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=10|PDF tr. 10]]

### Chỗ cần đọc trước

- [x] Abstract + Introduction
- [x] Section 3 NK-CRE
- [x] Section 4.1-4.4 method và Algorithm 1
- [x] Table 1-3
- [x] Limitations + Appendix prototype distortion

## Phase 2 — Pass 1 Recall

### Closed-book recall của tôi

**Problem**

- xử lí continual learning, giảm quên lãng các task và các relation sau

**Why does it matter?**

- Khi xuất hiện các quan hệ mới, mô hình **vẫn bắt buộc phải được huấn luyện tiếp** (continually trained). Ý nghĩa thực sự của Continual Learning là giúp mô hình học thêm kiến thức mới **mà không cần phải huấn luyện lại từ đầu** (retrain từ scratch) trên toàn bộ dữ liệu của tất cả các lớp cũ (vốn rất tốn kém hoặc dữ liệu cũ đã bị xóa vì lý do bảo mật) và **tránh hiện tượng quên lãng thảm họa** (catastrophic forgetting)

**Research gap**

- **Tăng cường phân tách:** Khớp phân phối là chưa đủ. Nên kết hợp thêm **Supervised Contrastive Learning** để đẩy các prototypes của những quan hệ (relations) khác nhau ra xa, tối đa hóa lề (margin) thay vì chỉ co cụm chúng lại.
    
- **Tham số hóa bộ nhớ (Parameter-Efficient Memory):** Hướng đi SOTA hiện tại là từ bỏ hoàn toàn việc lưu trữ mẫu thô (Replay Buffer). Thay vào đó, có thể mã hóa "phân phối" này trực tiếp vào các task-specific soft prompts (Prompt Tuning) hoặc dùng **LoRA**, giải quyết triệt để bài toán rò rỉ dữ liệu và Overfitting trên memory.

**Main idea**

- Mô hình thực sự lưu trữ và sử dụng lại các **prototype** (véc-tơ đại diện cho lớp quan hệ) đã được tối ưu từ các tác vụ huấn luyện trước đó để giữ vững đặc trưng của chúng

**Main contribution**

1. Định nghĩa và thiết lập bài toán **N-way-K-shot Continual Relation Extraction (NK-CRE)** nghiêm ngặt, sát với thực tế few-shot học liên tục.
2. Đề xuất phương pháp **Consistent Prototype Learning (ConPL)** kết hợp học mẫu gợi ý (**Prompt Learning**) và cấu trúc bộ nhớ kép: **Sample Memory** (lưu mẫu dữ liệu) và **Prototype Memory** (lưu véc-tơ prototype cố định của lớp cũ).
3. Đưa ra các hàm mất mát **Consistency Loss** (đảm bảo tính nhất quán phân phối) và **Focal Loss** để mô hình tập trung phân biệt các quan hệ dễ nhầm lẫn

**Main result**

1. ConPL vượt trội hơn hẳn so với các mô hình mạnh nhất trước đó trên hai bộ dữ liệu FewRel và TACRED.
2. Mô hình giảm thiểu đáng kể tỷ lệ quên lãng (forgetting rate), đạt mức rất gần với cận trên lý tưởng là **JointTrain** (huấn luyện chung trên tất cả dữ liệu gộp lại).
3. Giảm thiểu tối đa sự biến dạng của prototype theo thời gian (prototype distortion)

### Prompt kiểm tra recall

```text
I have completed the first pass of the paper.

Here is my understanding:

[PASTE MY NOTES]

Compare my understanding against the paper. Return what is correct, inaccurate, missing, confusing, and which sections/citations I should revisit. Do not rewrite the entire paper for me.
```

## Phase 3 — Problem / Motivation / Gap

| Mục | Diễn giải bằng lời của tôi | Evidence / citation |
|---|---|---|
| General problem | Continual relation extraction yêu cầu học relation mới tuần tự và vẫn phân loại được relation cũ. | [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=1\|PDF tr. 1]] |
| Why it matters | Relation mới xuất hiện liên tục, nhãn ít, và relation gần nghĩa dễ gây nhầm lẫn sau khi model update. | [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=1\|PDF tr. 1]] |
| What prior work solves | Replay/prototype/prompt/data augmentation giúp giảm forgetting ở CFRE/CRE. | [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=2\|PDF tr. 2]] |
| What prior work fails to solve | Một số protocol không few-shot đồng đều; memory exemplar ít không đủ giữ class geometry; confusing classes chưa được nhấn mạnh đủ. | [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=2\|PDF tr. 2]] |
| Exact research gap | Strict N-way K-shot cho mọi task và giảm forgetting/prototype distortion trong điều kiện memory cực nhỏ. | [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=3\|PDF tr. 3]] |
| Hypothesis / intuition | Giữ prototype ổn định và ép phân biệt confusing negatives sẽ giảm catastrophic forgetting. | [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=4\|PDF tr. 4]] |
| Contribution addressing the gap | ConPL kết hợp prototype memory, sample memory, $L_{cc}$, $L_{dc}$ và $L_{fc}$ trong training ba stage. | [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=5\|PDF tr. 5]] |

### Câu hỏi tự kiểm tra

- [x] NK-CRE khác CFRL ở task đầu như thế nào?
	- **CFRL (Continual Few-Shot Relation Learning):** Thường sử dụng chiến lược thiết lập dữ liệu bất đối xứng. Ở task đầu tiên (Task 0), mô hình được cung cấp một tập dữ liệu rất lớn chứa nhiều quan hệ và dồi dào mẫu huấn luyện. Mục đích là để học một không gian biểu diễn (Representation Space) và bộ trích xuất đặc trưng nền tảng vững chắc trước khi bước vào các task tiếp theo vốn bị giới hạn dữ liệu (Few-shot).
    
	- **NK-CRE (N-way-K-shot Continual Relation Extraction):** Thiết lập sự khắt khe ngay từ vạch xuất phát bằng cách áp dụng **Few-shot cho toàn bộ quá trình**. Ở task đầu tiên, mô hình không có lợi thế từ dữ liệu lớn mà phải học và khởi tạo các prototype chỉ từ một số lượng mẫu $K$ rất nhỏ cho $N$ quan hệ. Điều này ép mô hình phải có cơ chế như Prompt Learning hoặc Consistent Prototype Learning để tránh việc khởi tạo biểu diễn bị sai lệch ngay từ đầu.
- [x] Vì sao một exemplar/relation chưa đủ để giữ representation cũ?
	- Việc chỉ lưu một mẫu (Exemplar) để đại diện cho một quan hệ sẽ gây ra hiệu ứng ngược do các giới hạn về mặt thống kê và học máy:

		- **Sự đa dạng ngữ cảnh (Intra-class Variance):** Một quan hệ trong ngôn ngữ tự nhiên (ví dụ: _Thành lập tại_) có thể được biểu đạt bằng hàng trăm cấu trúc cú pháp và từ vựng khác nhau. Một mẫu duy nhất chỉ phản ánh được một mảnh ghép cực nhỏ, làm mất đi tính đa dạng của không gian đặc trưng.
		    
		- **Bẫy quá khớp trên bộ nhớ (Overfitting on Memory):** Khi sử dụng lại một mẫu duy nhất để củng cố (Replay) qua nhiều epoch, mô hình sẽ có xu hướng "học vẹt" các đặc trưng nhiễu (noise) của câu văn cụ thể đó thay vì bản chất của quan hệ.
		    
		- **Sụp đổ phân phối (Distribution Collapse):** Các phương pháp như NK-CRE cần tính toán khoảng cách giữa các phân phối để duy trì kiến thức cũ. Một điểm dữ liệu đơn lẻ không thể tạo ra phương sai (variance), làm cho cụm phân phối của quan hệ cũ bị thu hẹp thành một điểm, dễ dàng bị phá vỡ khi mô hình cập nhật trọng số cho task mới.
- [x] Vì sao confusing negatives quan trọng trong relation extraction?

	"Confusing Negatives" (Các mẫu âm tính gây nhầm lẫn) là những câu có cấu trúc từ vựng hoặc loại thực thể cực kỳ giống với mẫu dương tính nhưng thực chất lại mang một quan hệ khác hoặc không có quan hệ (No_Relation).

	- **Ngăn chặn học đường tắt (Shortcut Learning):** Nếu không có confusing negatives, mô hình dễ dàng đoán quan hệ chỉ dựa trên loại thực thể (Ví dụ: Thấy thực thể [Người] và [Thành phố] là tự động đoán quan hệ _Sinh ra tại_). Confusing negatives ép mô hình phải tập trung vào cấu trúc ngữ nghĩa sâu của câu để phân loại.
	    
	- **Tinh chỉnh ranh giới quyết định (Decision Boundary Refinement):** Trong học đối chiếu (Contrastive Learning), việc đưa các mẫu gây nhầm lẫn vào quá trình huấn luyện sẽ ép mô hình đẩy các class tương đồng ra xa nhau, tạo ra một ranh giới quyết định sắc nét hơn và làm giảm sự ảnh hưởng của các dữ liệu nhiễu (context noise).
	    
	- **Tối ưu hóa Gradient:** Thay vì để mô hình học qua hàng ngàn mẫu negatives dễ (easy negatives) vốn không cung cấp thêm lượng thông tin hữu ích nào và gây mất cân bằng dữ liệu, tập trung vào confusing negatives giúp quá trình hội tụ nhanh hơn và biểu diễn không gian nhúng có tính phân biệt cao hơn.

## Phase 4 — Method / Architecture

### Tôi tự vẽ trước

```text
Sentence + head/tail entity
-> discrete prompt với [MASK]
-> BERTBASE
-> [MASK] relation embedding
-> temporary prototypes cho relation mới
-> merge với prototype memory cũ
-> prototype classifier + confusing prototype set
-> Stage 1 train task mới + memory cũ
-> Stage 2 chọn exemplar gần center và refine memory mới
-> Stage 3 memory-only consolidation
-> classify trong toàn bộ relation đã thấy
```

### Component map

| Component | Input | Operation | Output | Purpose | Evidence |
|---|---|---|---|---|---|
| Prompt encoder | sentence, head, tail | `[CLS], head, [MASK], tail, [SEP], sentence, [SEP]` vào BERT | relation embedding tại `[MASK]` | khai thác PLM cho RE | [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=4\|PDF tr. 4]] |
| Prototype classifier | embedding + prototypes | cosine-softmax | relation probability | classify bằng class anchors | [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=4\|PDF tr. 4]] |
| Confusing class selection | sample embedding + prototype set | chọn nearest negative và negatives trong margin $\alpha$ | $P_i^{sim}$ | tập trung vào class dễ nhầm | [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=5\|PDF tr. 5]] |
| Sample memory | selected exemplar | lưu một sample/relation | replay data | nhắc model bằng input thật | [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=5\|PDF tr. 5]] |
| Prototype memory | selected feature/prototype | lưu một vector/relation | class anchor | giữ geometry cũ | [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=5\|PDF tr. 5]] |
| Consistent learning | memory samples + prototypes | $L_{cc}$ và $L_{dc}$ | regularized embedding geometry | cân bằng old/new và giữ relative similarity | [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=5\|PDF tr. 5]] |

### Điều tôi vẫn chưa hiểu

- [x] $P^k$, $\hat P^k$, $\bar P^k$, $\tilde P^k$ khác nhau chính xác ở mỗi stage ra sao?

	Tác giả sử dụng một hệ thống ký hiệu khá dày đặc để phục vụ các mục đích cấp phát bộ nhớ khác nhau trong từng giai đoạn huấn luyện. Dựa vào nội dung bài báo, bản chất của chúng như sau:
	
	- **$\tilde{P}^k$ (Temporary Prototypes):** Là nguyên mẫu _tạm thời_ của task thứ $k$. Chúng được khởi tạo ngay ở đầu Stage 1 bằng cách trung bình hóa toàn bộ mẫu huấn luyện của quan hệ mới trong $D_{train}^k$.
	    
	- **$P^k$ (Memory Prototypes):** Là nguyên mẫu _chính thức_ của task thứ $k$ được lưu trữ cố định. Khác với $\tilde{P}^k$, $P^k$ chỉ được tính toán lại dựa trên các mẫu tiêu biểu (typical samples) đã được chọn lọc để lưu vào Sample Memory $S^k$ ở Stage 2.
	    
	- **$\bar{P}^k$ (Current All Prototypes):** Là tập hợp tất cả các prototype đang tham gia vào quá trình tính loss tại task hiện tại. Trong Stage 1, nó là sự kết hợp của kiến thức cũ và nguyên mẫu tạm thời: $\bar{P}^k = \hat{P}^{k-1} \cup \tilde{P}^k$. Sang Stage 2 và 3, nó được cập nhật bằng nguyên mẫu chính thức: $\bar{P}^k = \hat{P}^{k-1} \cup P^k$.
	    
	- **$\hat{P}^k$ (Global Prototype Memory):** Là kho lưu trữ nguyên mẫu toàn cục của tất cả các task tính đến $k$. Nó chỉ được chốt lại ở cuối quá trình huấn luyện: $\hat{P}^k = \hat{P}^{k-1} \cup P^k$.
- [x] Code có triển khai Eq. 7 đúng như paper hay có focal modulation không?
	- **Về mặt công thức (Paper):** Tác giả khẳng định họ sử dụng "focal loss" để giải quyết sự nhầm lẫn giữa các lớp tương đồng. Tuy nhiên, công thức $L_{fc} = - \sum \log p_s(r_i\vert{}x_i)$ (Eq. 7) về mặt toán học chỉ là hàm **Cross-Entropy Loss tiêu chuẩn**. Khác biệt duy nhất là phân phối xác suất $p_s$ không tính trên toàn bộ các lớp, mà chỉ tính softmax trên một tập bị thu hẹp $P_{sim}^i$ (gồm target prototype và các confusing negative prototypes).
	    
	- **Khoảng trống lý thuyết:** Công thức này hoàn toàn vắng bóng nhân tử điều biến (modulating factor) $(1 - p_s)^\gamma$ – linh hồn của Focal Loss nguyên bản.
	    
	- **Đánh giá việc triển khai (Code):** Có hai khả năng xảy ra trong mã nguồn thực tế. Một là tác giả đã tự định nghĩa lại khái niệm "focal" theo nghĩa bóng (tức là "focus" việc tính loss vào các hard negatives) và thực sự code hàm Cross-Entropy giới hạn logits. Hai là họ có implement $(1 - p_s)^\gamma$ trong code nhưng lại trình bày thiếu trong bài báo. Cách tính toán trong Eq. 6 và 7 mang dáng dấp của _Hard Negative Mining_ hơn là cấu trúc Focal Loss truyền thống.

## Phase 5 — Section Recall

### Section 4.1 — Prototype-based classification

- **Input:** current task samples, old sample memory, old prototype memory.
- **Process:** tạo prompt, encode `[MASK]`, tính temporary prototype, phân loại bằng cosine-softmax, thêm $L_{cc}$ và $L_{fc}$.
- **Output:** updated encoder parameters và temporary/current prototype representations.
- **Purpose:** học relation mới trong khi vẫn giữ activation của relation cũ qua memory/prototype.
- **Still unclear:** vì sao paper gọi Eq. 7 là focal loss dù công thức giống restricted cross-entropy?

### Section 4.2-4.3 — Memory-enhanced + Consistent learning

- **Input:** selected key samples, sample memory, prototype memory.
- **Process:** chọn exemplar gần prototype nhất; lưu sample + prototype; chạy memory-only consolidation với $L_{dc}$.
- **Output:** memory cân bằng cho tất cả relation đã thấy và prototype geometry ổn định hơn.
- **Purpose:** giảm lệch old/new relation và hạn chế prototype distortion.

## Phase 6 — Equations

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

> [!note] Cách dùng phần này
> Bảng dưới là **scaffold từ Gemini output đã lọc lại theo paper note/PDF**. Dùng nó để kiểm tra công thức khi đọc lại Section 4, không coi là closed-book recall cá nhân.

| Eq/block                                     | Dùng để làm gì?                                                                      | Input -> Output                                                                                                                                                  | Dùng ở đâu trong pipeline                                                            | Behavior được khuyến khích                                                                                | Nếu bỏ/yếu đi thì sao?                                                                                                                        | Evidence / ablation                                                                                                                                                                                                                                                                                                                              | Status       |
| -------------------------------------------- | ------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------ |
| Eq. 1 — Prompt-based relation representation | Encode câu thành relation representation qua prompt cloze                            | Input: câu $x$, head $e_h$, tail $e_t$, encoder $f_\theta$ -> Output: hidden state tại `[MASK]`, $h_{[\text{MASK}]}$                                             | Bước đầu của train/inference trước khi tính prototype hoặc classify                  | Khai thác prior knowledge của BERT bằng template `[CLS], head, [MASK], tail, [SEP], sentence, [SEP]`      | Nếu dùng pooling thường, boundary ngữ nghĩa giữa relation có thể nhiễu hơn và few-shot sample efficiency kém hơn                              | Prompt encoder: [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=4\|PDF tr. 4]]; prompt-tuning baselines cải thiện ở Table 1: [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=7\|PDF tr. 7]]                                                                              | gemini-draft |
| Eq. 2 + Stage 2 memory update                | Tính temporary prototype và chọn exemplar/prototype để lưu memory                    | Input: $D_j^k$, embedding $f_\theta(x_i)$, key sample gần class center -> Output: $p_j$, sample memory $\hat S^k$, prototype memory $\hat P^k$                   | Stage 1 tính prototype tạm; Stage 2 chọn key sample và tái khởi tạo prototype memory | Khóa class anchor cũ thay vì để prototype cũ bị recompute/trôi theo encoder mới                           | Nếu không có Prototype Memory, class anchor cũ dễ bị prototype distortion khi học task mới                                                    | Bỏ PM giảm T8 từ 85.77 xuống 82.21 (-3.56): [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=8\|Table 2, PDF tr. 8]]; distortion/forgetting: [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=1\|Figure 1, PDF tr. 1]]                                                     | gemini-draft |
| Eq. 3-4 — Prototype classifier + $L_{ce}$    | Classify bằng cosine-softmax tới prototypes của các relation đã thấy                 | Input: $f_\theta(x_i)$, prototypes $p_l$, seen relations $\hat R^k$ -> Output: $p(r_i\mid x_i)$ và CE loss                                                       | Stage 1/2/3 như core classification signal                                           | Ép embedding gần prototype đúng và xa prototype sai trong toàn bộ label space đã thấy                     | Nếu thiếu core CE, model không có tín hiệu phân loại relation ổn định; các consistency loss chỉ giữ geometry chứ không thay mục tiêu classify | Công thức classifier/CE: [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=4\|PDF tr. 4]]                                                                                                                                                                                                                      | gemini-draft |
| Eq. 5 — $L_{cc}$ classification consistency  | Giữ memory sample gần prototype đúng đã lưu                                          | Input: old memory samples $\hat S^{k-1}$, prototype đúng $p_i$, current embedding $f_\theta(x_i)$ -> Output: khoảng cách L2/scalar penalty                       | Stage 1/2 trong $L_{class}$ và Stage 3 trong $L_{cons}$                              | Chống encoder drift làm sample cũ rời khỏi anchor cũ                                                      | Nếu bỏ, embedding của old samples có thể trôi khỏi prototype memory và gây misclassification/forgetting                                       | Bỏ $L_{cc}$ giảm nhẹ trong setting chính; khi tính probability bằng sample memory, $L_{cc}$ tăng 0.73 tại T8: [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=8\|Table 2, PDF tr. 8]], [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=9\|Figure 4, PDF tr. 9]]          | gemini-draft |
| Eq. 6-7 — Confusing-class loss $L_{fc}$      | Tập trung phân biệt positive prototype với hard/confusing negative prototypes        | Input: $f_\theta(x_i)$, prototype đúng $p_i$, nearest negative $p_i^{mn}$, negatives qua threshold $\alpha$ trong $P_i^{sim}$ -> Output: restricted softmax loss | Stage 1/2 trong $L_{class}$ và Stage 3 trong $L_{cons}$                              | Làm ranh giới giữa relation gần nghĩa sắc hơn, ví dụ các relation dễ nhầm như family relations            | Nếu bỏ, model dễ merge/overwrite boundary của class gần nhau; đây là ablation rơi mạnh nhất                                                   | Bỏ $L_{fc}$ giảm T8 từ 85.77 xuống 75.11 (-10.66): [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=8\|Table 2, PDF tr. 8]]; confusing-class visualization: [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=8\|Figure 3, PDF tr. 8]]                                      | gemini-draft |
| Eq. 8 — Distribution consistency $L_{dc}$    | Giữ cấu trúc khoảng cách tương đối giữa sample embedding và toàn bộ prototype memory | Input: memory samples $\hat S^k$, target prototype $p_i$, all prototypes $\hat P^k$ -> Output: penalty giữa hai vector similarity/distance distributions         | Chỉ ở Stage 3 memory-only consolidation                                              | Giữ global geometry: không chỉ sample gần prototype đúng, mà còn giữ quan hệ tương đối với các class khác | Nếu bỏ, memory-only replay dễ overfit vào vài exemplar và làm layout old/new relation mất cân bằng                                            | Bỏ $L_{dc}$ giảm nhẹ trong setting chính; Figure 4 cho thấy $L_{dc}$ tăng 2.0 điểm khi dùng sample-memory probability: [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=8\|Table 2, PDF tr. 8]], [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=9\|Figure 4, PDF tr. 9]] | gemini-draft |
| Eq. 9-10 — Objectives theo stage             | Ghép các loss thành mục tiêu huấn luyện cho Stage 1/2 và Stage 3                     | Input: $\lambda_{ce},\lambda_{cc},\lambda_{fc},\lambda_{dc}$ cùng các loss tương ứng -> Output: $L_{class}$ hoặc $L_{cons}$                                      | Stage 1/2 dùng $L_{class}$; Stage 3 dùng $L_{cons}$ có thêm $L_{dc}$                 | Tách học task mới + memory cũ khỏi bước consolidation chỉ trên memory                                     | Nếu không có Stage 3/$L_{cons}$, model thiếu bước cân bằng lại tất cả relation đã thấy sau khi thêm memory mới                                | Objective và Algorithm 1: [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=5\|PDF tr. 5]]; bỏ consistent learning module giảm 85.77 -> 84.25: [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=8\|Table 2, PDF tr. 8]]                                                     | gemini-draft |

### Điểm cần kiểm tra lại khi đọc công thức

- [x] Paper gọi Eq. 7 là focal loss, nhưng công thức giống restricted cross-entropy hơn focal loss chuẩn vì không có modulation factor $(1-p_t)^\gamma$.
- [x] Phân biệt rõ $L_{cc}$ giữ **sample-prototype point alignment**, còn $L_{dc}$ giữ **relative distribution/geometry** với toàn bộ prototype memory.
- [x] Không lấy claim từ Gemini nếu không trỏ lại được về PDF/Table/Figure; các số ablation chính nên ưu tiên Table 2 và Figure 4.

## Phase 7 — Loss Functions

```text
Total training
├── L_ce -> classify current/memory samples by prototype similarity
├── L_cc -> keep memory sample close to its stored prototype
├── L_fc -> focus on confusing negative prototypes
└── L_dc -> preserve relative similarity distribution in memory-only consolidation
```

| Loss | Equation | Inputs | Trains component | Behavior | Weight | Ablation |
|---|---|---|---|---|---|---|
| $L_{ce}$ | Eq. 4 | current task + sample memory | encoder/classifier via prototypes | correct relation classification | $\lambda_{ce}=1$ | core loss, not individually removed |
| $L_{cc}$ | Eq. 5 | old/current memory samples + prototypes | encoder | sample-prototype consistency | $\lambda_{cc}=1$ | small individual gain; larger when classifier uses sample memory |
| $L_{fc}$ | Eq. 7 | restricted confusing prototype set | encoder/classifier | hard-negative discrimination | $\lambda_{fc}=1$ | strongest: -10.66 when removed |
| $L_{dc}$ | Eq. 8 | memory samples + prototype memory | encoder | relative distribution consistency | $\lambda_{dc}=1$ | small individual gain; +2.0 in Figure 4 variant |

## Phase 8 — Experiments

| Experiment | Research question | Dataset | Baselines | Metric | Table/Figure | Main result | Caveat |
|---|---|---|---|---|---|---|---|
| Main NK-CRE accuracy | ConPL có tốt hơn continual baselines trong strict few-shot không? | FewRel/TACRED | EMAR, RP-CRE, ERDA, PT variants | whole accuracy after each task | Table 1 | ConPL dẫn đầu đa số T2-T8 và toàn bộ TACRED | các baseline không † có budget task đầu khác |
| Ablation components | Thành phần nào đóng góp? | FewRel 10-way 5-shot | ConPL variants | T8 accuracy | Table 2 | bỏ $L_{fc}$ giảm mạnh nhất; bỏ PM giảm 3.56 | chỉ một setting chính |
| Consistency loss importance | $L_{cc}$/$L_{dc}$ còn hữu ích khi không dùng prototype memory cho logits? | FewRel 10-way 5-shot | variants dùng sample memory | accuracy curve | Figure 4 | $L_{dc}$ tăng 2.0, $L_{cc}$ tăng 0.73 | hyperparameter retuned |
| Forgetting | ConPL giảm forgetting đến đâu? | FewRel 10-way 5-shot | SeqRun, JointTrain, baselines | mean forgetting | Table 3 | ConPL 3.31 gần JointTrain 3.29 | JointTrain dùng toàn bộ dữ liệu cũ |
| Distortion-forgetting | Prototype distortion có liên hệ forgetting không? | FewRel analysis, 50 task sequences | scatter analysis | distortion vs forgetting | Appendix/Figure | xu hướng distortion cao đi cùng forgetting cao | không báo correlation coefficient |

### Protocol fingerprint

- Dataset and split: FewRel 80 public relations, 8 tasks x 10 relations; TACRED bỏ `n/a`, còn 41 relations.
- Scenario / label space: N-way K-shot continual relation extraction, evaluation trên tất cả relation đã thấy.
- Backbone: BERTBASE với discrete prompt.
- Seeds / number of runs: main experiments dùng 6 random task sequences; distortion analysis dùng 50 task sequences.
- Metric and averaging: accuracy sau từng task; forgetting metric theo Chaudhry et al.
- Baseline implementation: PT variants và ConPL dùng cùng seeds/task sequences; một số baseline legacy lấy từ CFRL.
- External data: ERDA(PT) dùng Wikipedia augmentation; ConPL không dùng LLM augmentation.
- Memory budget: một raw sample và một prototype vector mỗi relation.
- Evaluation after each task: yes, T1-T8.

## Phase 9 — Claim → Evidence

| Claim | Where claim appears | Experiment | Evidence | My judgment | Caveat |
|---|---|---|---|---|---|
| ConPL cải thiện NK-CRE accuracy. | Abstract/Results | Table 1 | FewRel 10-way 5-shot T8: ConPL 85.77 vs EMAR(PT) 81.34; TACRED 5-shot T8: 76.38 vs 68.67. [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=7\|PDF tr. 7]] | Strong reported evidence | chưa reproduced local |
| Prototype memory hữu ích. | Method/Ablation | Table 2 | bỏ Prototype Memory giảm 85.77 -> 82.21. [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=8\|PDF tr. 8]] | Supported | chỉ FewRel 10-way 5-shot |
| $L_{fc}$ là thành phần mạnh nhất. | Ablation | Table 2 | bỏ $L_{fc}$ giảm 85.77 -> 75.11. [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=8\|PDF tr. 8]] | Strong | tên "focal loss" cần kiểm code/công thức |
| ConPL giảm forgetting gần JointTrain. | Forgetting analysis | Table 3 | mean forgetting ConPL 3.31, JointTrain 3.29. [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=9\|PDF tr. 9]] | Interesting | JointTrain có full old data |
| Prototype distortion liên hệ forgetting. | Appendix analysis | distortion scatter | paper quan sát xu hướng qua 50 task sequences. [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=11\|PDF tr. 11]] | Partial | không causal/correlation coefficient |

## Phase 10 — Ablation Study

| Component | Intended purpose | With component | Without component | Difference | Conclusion justified | Not justified |
|---|---|---:|---:|---:|---|---|
| Prototype Memory | giữ class anchors cũ | 85.77 | 82.21 | -3.56 | PM có ích rõ trong FewRel 5-shot | PM luôn đủ cho class đa mode |
| Consistent Learning Module | memory-only consolidation | 85.77 | 84.25 | -1.52 | consolidation có ích | chứng minh mọi consistency term đều quan trọng ngang nhau |
| $L_{cc}$ | sample-prototype consistency | 85.77 | 85.69 | -0.08 | đóng góp nhỏ khi dùng PM logits | loss này vô dụng nói chung |
| $L_{dc}$ | relative distribution consistency | 85.77 | 85.40 | -0.37 | đóng góp nhỏ trong setting chính | không cần trong setting khác |
| $L_{fc}$ | confusing-class discrimination | 85.77 | 75.11 | -10.66 | thành phần quan trọng nhất theo ablation | focal loss chuẩn được validate |

## Phase 11 — Critical Reading

- Strongest contribution: strict NK-CRE framing + prototype/sample memory với ablation rõ thành phần $L_{fc}$.
- Weakest part: Eq. 7 naming và thiếu phân tích sâu vì sao prototype outliers không theo distortion-forgetting trend.
- Main assumption: task boundary và relation set mới được biết; được phép lưu raw exemplar.
- Alternative explanation: gains có thể đến nhiều từ prompt + hard-negative discrimination hơn là consistency losses riêng lẻ.
- Missing experiment: sensitivity cho $\alpha$, memory size, nhiều prototypes/class, macro-F1/calibration.
- Generalization risk: chỉ BERTBASE, FewRel/TACRED, English relation extraction.
- Reproducibility risk: chi tiết compute/GPU hours không rõ, code cần kiểm Eq. 7.

## Phase 12 — Reproduction Check

| Item | Status | Detail | Missing detail / risk |
|---|---|---|---|
| Dataset and split | Partially specified | FewRel/TACRED task setup, public FewRel 80 relations | exact task order files/seeds cần code |
| Preprocessing | Partially specified | discrete prompt with entities | entity markers/tokenization details cần code |
| Input representation | Clearly specified | `[CLS], head, [MASK], tail, [SEP], sentence, [SEP]` |  |
| Model / backbone | Clearly specified | BERTBASE | checkpoint variant cần code |
| Training procedure | Clearly specified | 3 stages, epochs 1/1/3 | batching details |
| Sampling procedure | Clearly specified | exemplar gần prototype nhất | tie cases/multi-mode not discussed |
| Memory / replay strategy | Clearly specified | one sample + one prototype per relation | byte budget not reported |
| Loss functions | Partially specified | Eq. 4/5/7/8/9/10 | Eq. 7 naming/code mismatch risk |
| Optimizer | Clearly specified | Adam |  |
| Learning rate | Clearly specified | $2e^{-5}$ | schedule unclear |
| Batch size | Missing | not in note/PDF scaffold | reproduction risk |
| Epochs | Clearly specified | 1, 1, 3 |  |
| Hyperparameters | Partially specified | $\alpha=0.1$, lambdas=1, clipping=10 | sensitivity absent |
| Random seeds | Partially specified | 6 sequences; same seeds for reruns | exact seed values need code |
| Evaluation protocol | Clearly specified | cumulative test set after each task |  |
| Inference procedure | Partially specified | prototype classifier over known relations | task identity assumptions should be checked |

## Phase 13 — Completeness / Oral Exam

- [x] Giải thích NK-CRE không nhìn paper.
	NK-CRE là một thiết lập bài toán học liên tục (Continual Learning) cực kỳ nghiêm ngặt. Trong đó, luồng dữ liệu (data stream) được chia thành nhiều task tuần tự. Tại _bất kỳ_ task nào, mô hình cũng chỉ được cung cấp chính xác $N$ quan hệ (relations) mới, và mỗi quan hệ chỉ có đúng $K$ mẫu dữ liệu (samples) được gán nhãn.
	
	**Bản chất:** Nó ép mô hình giải quyết đồng thời hai bài toán khó nhất: **Data Sparsity** (Dữ liệu thưa thớt - không đủ để hội tụ trọng số) và **Catastrophic Forgetting** (Quên thảm khốc - mất đi ranh giới quyết định của các quan hệ ở task trước).
- [x] Phân biệt CFRL vs NK-CRE ở task đầu.
	CFRL trong các baseline cũ cho task đầu nhiều dữ liệu hơn, nên model có một representation nền khá mạnh trước khi bước vào few-shot continual tasks. NK-CRE nghiêm ngặt hơn: task đầu cũng chỉ có $N$ relation và $K$ sample/relation, vì vậy không có lợi thế pretraining từ task đầu giàu nhãn.
- [x] Vẽ ba stage ConPL.
	```text
	Task k arrives
	-> Stage 1: train on new task samples + old sample memory with temporary new prototypes and old prototype memory
	-> Stage 2: select center-nearest exemplar for each new relation, update sample/prototype memory, refine with L_class
	-> Stage 3: train only on all memory with L_cons, adding L_dc to rebalance old/new relation geometry
	-> evaluate over all seen relations
	```
- [x] Giải thích $L_{cc}$ vs $L_{dc}$.
	$L_{cc}$ là ràng buộc cục bộ: embedding của memory sample phải ở gần prototype đúng của nó. $L_{dc}$ là ràng buộc hình học toàn cục hơn: quan hệ similarity từ memory sample tới toàn bộ prototype memory phải giống quan hệ similarity từ prototype đúng tới toàn bộ prototype memory.
- [x] Giải thích vì sao $L_{fc}$ có impact lớn nhất.
	$L_{fc}$ đánh trực tiếp vào lỗi dễ gây forgetting trong relation extraction: các relation gần nghĩa/cùng kiểu entity bị kéo lẫn vào nhau. Vì loss này thu hẹp softmax vào target và confusing negatives, gradient tập trung vào decision boundary khó; Table 2 cho thấy bỏ $L_{fc}$ làm T8 giảm mạnh nhất, từ 85.77 xuống 75.11.
- [x] Đọc Table 1-3 và nêu caveat.
	Table 1 ủng hộ claim ConPL mạnh hơn các baseline trong NK-CRE, nhưng cần so sánh ưu tiên với các baseline được tái chạy/có dấu † và PT variants vì baseline CFRL cũ có budget task đầu khác. Table 2 cho thấy $L_{fc}$ và Prototype Memory là các thành phần rõ nhất. Table 3 cho thấy forgetting của ConPL gần JointTrain, nhưng JointTrain là upper bound dùng toàn bộ dữ liệu cũ.
- [x] Nêu ít nhất 3 limitation/assumption.
	ConPL vẫn rehearsal-based vì lưu raw exemplar; giả định task boundary/relation set mới được biết; chỉ dùng một prototype/class nên có thể yếu với class đa mode; metric chính là accuracy, thiếu macro-F1/calibration; chưa có sensitivity analysis cho $\alpha$, memory size hoặc nhiều prototype.
- [x] So sánh ConPL với CPL/WAVE++ ở mức protocol, không chỉ headline.
	ConPL tập trung vào strict NK-CRE và giữ class anchors bằng sample memory + prototype memory + hard-negative/confusing-class loss. CPL cùng họ prompt/prototype cho continual few-shot RE nhưng không phải điểm nhấn chính ở dual memory và distribution consistency như ConPL. WAVE++ nhìn vấn đề từ within-task variance/adaptive prompting, nhấn vào variance của task hiện tại và prompt adaptation; vì vậy khi so sánh cần tách protocol, memory budget, external augmentation, prompt design và cách mỗi paper xử lý forgetting.

### Prompt oral exam

```text
Act as my PhD advisor. Quiz me on ConPL one question at a time. Start from NK-CRE problem/gap, then method stages, equations/losses, experiments/ablation, assumptions/limitations, and finally ask me to propose improvements. Do not reveal the ideal answer before I attempt it.
```

## Final Paper Note Handoff

Chỉ chuyển sang paper note chính những ý đã tự kiểm tra lại bằng PDF citation.

### Ý cần chuyển sang paper note

- [x] Problem/gap: strict NK-CRE và task đầu few-shot.
- [x] Method overview: prompt encoder + prototype classifier + dual memory + 3 stages.
- [x] Important equations: Eq. 2/3/5/7/8/9/10.
- [x] Protocol fingerprint: FewRel/TACRED, 6 sequences, memory one exemplar + one vector.
- [x] Main results: Table 1 T8 và Appendix mean/std.
- [x] Ablation: $L_{fc}$ strongest, PM meaningful, consistency smaller under PM logits.
- [x] Limitations: rehearsal-based, task boundary, no macro-F1/calibration, no sensitivity.
- [x] Concepts: [[Prototype Learning]], [[Embedding Space Regularization]], [[Replay in Continual Learning]], [[Continual Few-Shot Relation Extraction]].

## Liên kết

- Paper note: [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction]]
- PDF: [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf]]
- Related reading log: [[2026-08-16 - Consistent Prototype Learning for Few-Shot Continual Relation Extraction]]
- Concepts: [[Prototype Learning]], [[Embedding Space Regularization]], [[Replay in Continual Learning]], [[Continual Few-Shot Relation Extraction]]
