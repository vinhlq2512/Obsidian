---
type: paper
status: draft
title: "FewRel: A Large-Scale Supervised Few-Shot Relation Classification Dataset with State-of-the-Art Evaluation"
aliases:
  - FewRel
authors:
  - Xu Han
  - Hao Zhu
  - Pengfei Yu
  - Ziyun Wang
  - Yuan Yao
  - Zhiyuan Liu
  - Maosong Sun
year: 2018
venue: "EMNLP 2018"
url: "https://aclanthology.org/D18-1514/"
pdf: "[[FewRel - A Large-Scale Supervised Few-Shot Relation Classification Dataset with State-of-the-Art Evaluation.pdf]]"
doi: "10.18653/v1/D18-1514"
arxiv: "1810.10147"
code_url: "https://github.com/thunlp/FewRel"
dataset_url: "http://zhuhao.me/fewrel"
topic:
  - few-shot relation classification
  - dataset
priority: high
reading_status: not-started
related_concepts:
  - "[[Relation Extraction]]"
  - "[[Few-shot Learning]]"
created_at: 2026-09-05
updated_at: 2026-09-07
tags:
  - paper
  - dataset
  - relation-extraction
---

# FewRel: A Large-Scale Supervised Few-Shot Relation Classification Dataset

## Tóm tắt một câu

FewRel là benchmark few-shot [[Relation Extraction|relation classification]] gồm 70.000 câu từ Wikipedia trên 100 relations, được tạo bằng distant supervision rồi lọc thủ công để đánh giá khả năng nhận diện relation mới chỉ từ vài support examples.

## Nguồn

- Paper ACL: [D18-1514](https://aclanthology.org/D18-1514/)
- PDF trong vault: [[FewRel - A Large-Scale Supervised Few-Shot Relation Classification Dataset with State-of-the-Art Evaluation.pdf]]
- Dataset/code: [thunlp/FewRel](https://github.com/thunlp/FewRel), [FewRel project page](http://zhuhao.me/fewrel)

## Vấn đề paper giải quyết

Relation classification truyền thống cần nhiều dữ liệu gán nhãn theo từng relation. Distant supervision giúp mở rộng dữ liệu nhưng tạo nhãn nhiễu, đặc biệt khó cho long-tail relations. Paper lập luận rằng cần một benchmark supervised, sạch hơn, để kiểm tra xem các mô hình [[Few-shot Learning|few-shot learning]] có thật sự phân loại được relation mới chỉ từ vài ví dụ hay không. [[FewRel - A Large-Scale Supervised Few-Shot Relation Classification Dataset with State-of-the-Art Evaluation.pdf#page=1|PDF, tr. 1]]

## Gap và đóng góp

- Paper chuyển relation classification sang thiết lập few-shot, thay vì chỉ coi đây là supervised RC với nhiều dữ liệu.
- Paper tạo dataset FewRel từ Wikipedia/Wikidata: distant supervision sinh candidate set, crowdworkers lọc nhãn sai, rồi giữ 100 relations có chất lượng annotation tốt.
- Paper điều chỉnh nhiều few-shot methods cho RC và báo cáo benchmark đầu tiên trên bốn setting: 5-way 1-shot, 5-way 5-shot, 10-way 1-shot, 10-way 5-shot. [[FewRel - A Large-Scale Supervised Few-Shot Relation Classification Dataset with State-of-the-Art Evaluation.pdf#page=2|PDF, tr. 2]]

## Bài toán/formalization

Few-shot relation classification học một hàm:

$$
F:(R,S,x) \mapsto y
$$

Trong đó:

- $R = \{r_1,\ldots,r_m\}$ là tập relation candidate trong episode.
- $S$ là support set chứa $n_i$ câu đã gán nhãn cho từng relation $r_i$.
- $x$ là query sentence kèm cặp entity cần phân loại.
- $y \in R$ là relation dự đoán.

Với thiết lập $N$-way $K$-shot, paper dùng $N=m=|R|$ và $K=n_1=\ldots=n_m$. [[FewRel - A Large-Scale Supervised Few-Shot Relation Classification Dataset with State-of-the-Art Evaluation.pdf#page=3|PDF, tr. 3]] [[FewRel - A Large-Scale Supervised Few-Shot Relation Classification Dataset with State-of-the-Art Evaluation.pdf#page=4|PDF, tr. 4]]

## Phương pháp tạo dataset

### Distant supervision

Paper dùng Wikipedia làm corpus và Wikidata làm knowledge base. Với mỗi câu chứa head entity và tail entity, nếu Wikidata có statement $(e_1,e_2,r)$ thì câu đó trở thành candidate instance cho relation $r$. Để giảm shortcut ghi nhớ entity pair, paper chỉ giữ một instance cho mỗi entity pair duy nhất trong một relation. Sau đó bỏ relation có dưới 1.000 candidate instances và lấy ngẫu nhiên 1.000 instances cho các relation còn lại, tạo candidate set 122 relations và 122.000 instances. [[FewRel - A Large-Scale Supervised Few-Shot Relation Classification Dataset with State-of-the-Art Evaluation.pdf#page=2|PDF, tr. 2]] [[FewRel - A Large-Scale Supervised Few-Shot Relation Classification Dataset with State-of-the-Art Evaluation.pdf#page=3|PDF, tr. 3]]

### Human annotation

Annotator xem sentence, hai entities, relation do distant supervision gán, tên/description của entities và relation trong Wikidata. Họ đánh dấu positive khi relation có thể suy ra chỉ từ semantics của câu; đánh dấu negative nếu câu không hoàn chỉnh, link entity sai, hoặc relation không được câu hỗ trợ. Mỗi instance có ít nhất hai annotators đồng ý; nếu bất đồng thì thêm annotator thứ ba. Sau annotation, paper giữ relations có ít nhất 700 positive instances và chọn top 100 theo free-marginal multirater kappa. [[FewRel - A Large-Scale Supervised Few-Shot Relation Classification Dataset with State-of-the-Art Evaluation.pdf#page=3|PDF, tr. 3]]

## Protocol fingerprint

| Trường | Giá trị paper gốc |
|---|---|
| Dataset source | Wikipedia sentences + Wikidata relations |
| Quy mô | 100 relations, 700 instances/relation, tổng 70.000 instances |
| Split | 64 train relations, 16 validation relations, 20 test relations |
| Unit dự đoán | Sentence + head/tail entity pair -> relation label |
| Episode | 5-way hoặc 10-way; 1-shot hoặc 5-shot |
| Support/query | Support set có $K$ labeled instances cho mỗi relation trong episode; query là unlabeled instance cần gán vào một relation trong $R$ |
| Models | CNN/PCNN finetune, CNN/PCNN kNN, Meta Network, GNN, SNAIL, Prototypical Network |
| Encoder chính | CNN và PCNN với word embeddings + position embeddings; few-shot methods trong bảng chính dùng CNN |
| Metric | Accuracy phần trăm, báo cáo mean ± interval/variance theo evaluation runs của paper |
| Human baseline | Chỉ đo 5-way 1-shot và 10-way 1-shot; annotators không được cung cấp tên relation hay extra information |

Ghi chú cho research CRE hiện tại: nhiều paper continual relation extraction sau này nói “FewRel” nhưng thường dùng 80 public relations và chia thành 8 hoặc 10 tasks. Đó là protocol downstream, không phải split few-shot gốc 64/16/20 của paper FewRel. Khi so sánh ConPL/CPL/WAVE/WAVE++ phải ghi lại task construction riêng.

## Kết quả chính

Paper báo cáo Prototypical Network là baseline mạnh nhất trong bảng chính, nhưng vẫn cách xa human performance ở 1-shot. [[FewRel - A Large-Scale Supervised Few-Shot Relation Classification Dataset with State-of-the-Art Evaluation.pdf#page=4|PDF, tr. 4]]

| Model | 5-way 1-shot | 5-way 5-shot | 10-way 1-shot | 10-way 5-shot |
|---|---:|---:|---:|---:|
| Finetune CNN | 44.21 ± 0.44 | 68.66 ± 0.41 | 27.30 ± 0.28 | 55.04 ± 0.31 |
| kNN PCNN | 60.28 ± 0.43 | 72.41 ± 0.39 | 46.15 ± 0.31 | 59.11 ± 0.30 |
| Meta Network CNN | 64.46 ± 0.54 | 80.57 ± 0.48 | 53.96 ± 0.56 | 69.23 ± 0.52 |
| GNN CNN | 66.23 ± 0.75 | 81.28 ± 0.62 | 46.27 ± 0.80 | 64.02 ± 0.77 |
| SNAIL CNN | 67.29 ± 0.26 | 79.40 ± 0.22 | 53.28 ± 0.27 | 68.33 ± 0.25 |
| Prototypical Network CNN | 69.20 ± 0.20 | 84.79 ± 0.16 | 56.44 ± 0.22 | 75.55 ± 0.19 |
| Human performance | 92.22 ± 5.53 | - | 85.88 ± 7.40 | - |

Quan sát quan trọng:

- Few-shot methods vượt các vanilla RC strategies như finetune/kNN, nên episode-based metric learning/meta-learning có ích cho RC.
- Khoảng cách với human rất lớn ở 1-shot: Prototypical Network đạt 69.20 trong 5-way 1-shot so với human 92.22; 10-way 1-shot đạt 56.44 so với human 85.88.
- PCNN không mặc định tốt hơn CNN trong few-shot setup; paper nói các few-shot methods với PCNN kém CNN khoảng 3-10 điểm phần trăm trong preliminary experiments, nên bảng chính chỉ giữ CNN cho few-shot methods. [[FewRel - A Large-Scale Supervised Few-Shot Relation Classification Dataset with State-of-the-Art Evaluation.pdf#page=5|PDF, tr. 5]]

## Hạn chế, giả định, failure modes

- Dataset dựa trên Wikipedia/Wikidata nên relation schema và sentence style nghiêng về encyclopedia text, chưa đại diện cho domain như biomedical, legal, social media hoặc Vietnamese.
- Annotation yêu cầu relation được suy ra từ sentence semantics, nhưng annotator vẫn được xem relation/entity description từ Wikidata trong quá trình lọc; evaluation human baseline thì không cung cấp tên relation, nên hai ngữ cảnh này không giống nhau hoàn toàn.
- Dataset không tập trung vào negative/no-relation instances; bảng so sánh RC datasets cũng bỏ qua negative instances ở một số dataset. Điều này làm FewRel phù hợp hơn cho closed-set relation choice trong episode hơn là open-world extraction.
- Paper chỉ báo cáo CNN/PCNN-era baselines; chưa có pretrained Transformer, prompt-based hoặc instruction-based baselines.
- Các ví dụ `educated at` cho thấy cùng một relation có thể cần pattern đơn giản, commonsense, logical reasoning hoặc co-reference. Đây là failure mode chính: model không chỉ cần lexical matching mà phải xử lý nhiều kiểu reasoning. [[FewRel - A Large-Scale Supervised Few-Shot Relation Classification Dataset with State-of-the-Art Evaluation.pdf#page=5|PDF, tr. 5]]

## Đánh giá từ evidence

FewRel là nền tảng tốt cho nghiên cứu few-shot relation classification vì nó cân bằng số instances/relation, có split theo relation để test generalization sang labels chưa thấy, và có quy trình lọc nhiễu rõ hơn distant supervision thuần. Tuy vậy, khi dùng FewRel cho [[Continual Few-Shot Relation Extraction]], không nên mặc định rằng kết quả paper FewRel gốc tương thích với protocol continual: downstream papers thường thay đổi relation subset, task stream, số shots, memory budget và metric sau mỗi task.

Một cách diễn giải có thể là: FewRel đo “học relation mới từ vài ví dụ trong một episode đóng”, còn CFRE/CRE đo thêm “giữ relation cũ qua chuỗi tasks”. Hai trục này liên quan nhưng không thay thế nhau.

## Diễn giải học tập

FewRel đáng chú ý vì nó biến relation extraction thành bài kiểm tra về khả năng dùng support examples như “định nghĩa bằng ví dụ”. Model không chỉ học label name; trong episode, nó phải nhìn vài câu mẫu của relation rồi quyết định query giống nhóm nào. Vì vậy prototype/metric learning hợp tự nhiên: mỗi relation được nén thành một vùng trong embedding space, query được gán theo khoảng cách.

Nhưng Table 5 nhắc rằng “giống” không chỉ là cùng từ khóa. Với relation `educated at`, có câu nói trực tiếp “graduated from”, có câu cần commonsense về “obtained honours at”, có câu cần suy luận từ vai trò professor tại trường, và có câu cần co-reference. Nếu embedding chỉ bắt lexical pattern, model có thể thắng những case dễ nhưng hụt những case cần reasoning.

## Câu hỏi review

1. Vì sao FewRel giữ tối đa một instance cho mỗi unique entity pair trong một relation?
2. Split 64/16/20 theo relation khác gì với split random theo sentence?
3. Vì sao human baseline chỉ đo 1-shot mà không đo 5-shot?
4. Khi paper CRE nói dùng FewRel 80 relations, điều gì cần kiểm tra trước khi so sánh với FewRel gốc?
5. Prototypical Network thắng các baseline khác trong Table 4 gợi ý gì về geometry của relation representations?
6. Vì sao no-relation/open-world setting là một điểm thiếu nếu muốn dùng FewRel cho IE production?

## Gợi ý trả lời câu hỏi review

1. Để tránh model ghi nhớ entity pair thay vì học semantics của câu; nếu nhiều câu cùng entity pair, relation có thể bị shortcut.
2. Split theo relation buộc model generalize sang relation classes chưa thấy, đúng tinh thần few-shot classification; split theo sentence có thể cho model thấy relation đó trong training.
3. 1-shot là setting khó và tiết kiệm annotation human; paper nói 5-shot dễ hơn nên không đánh giá human cho 5-shot.
4. Cần kiểm tra relation subset, số tasks, số examples/relation ở task đầu và task sau, task order, metric sau từng task, và memory/replay budget.
5. Nó gợi ý representation metric/prototype là inductive bias mạnh cho few-shot RC, nhất là khi mỗi class chỉ có vài support examples.
6. Vì production IE thường phải quyết định “không có relation nào phù hợp” hoặc schema mở; FewRel gốc chủ yếu là closed-set choice giữa relations trong episode.

## Cần đọc tiếp

- Kiểm tra GitHub split files để xác định chính xác public/private relation IDs được release.
- Ghi riêng mapping từ FewRel gốc sang các protocol ConPL/CPL/WAVE/WAVE++ trong project CRE.
- Nếu cần reproduce, tạo dataset access note: nguồn tải, checksum, license/usage, relation description leakage risk.

## Evidence map

| Claim | Evidence | Nhãn |
|---|---|---|
| FewRel có 70.000 sentences trên 100 relations từ Wikipedia và được crowdworkers lọc từ distant supervision. | [[FewRel - A Large-Scale Supervised Few-Shot Relation Classification Dataset with State-of-the-Art Evaluation.pdf#page=1\|PDF tr. 1]], [[FewRel - A Large-Scale Supervised Few-Shot Relation Classification Dataset with State-of-the-Art Evaluation.pdf#page=3\|PDF tr. 3]] | reported/observed |
| Candidate construction dùng Wikipedia/Wikidata, giữ một instance cho mỗi entity pair và tạo 122.000 candidates trước annotation. | [[FewRel - A Large-Scale Supervised Few-Shot Relation Classification Dataset with State-of-the-Art Evaluation.pdf#page=2\|PDF tr. 2]], [[FewRel - A Large-Scale Supervised Few-Shot Relation Classification Dataset with State-of-the-Art Evaluation.pdf#page=3\|PDF tr. 3]] | observed |
| Split gốc là 64 train, 16 validation, 20 test relations. | [[FewRel - A Large-Scale Supervised Few-Shot Relation Classification Dataset with State-of-the-Art Evaluation.pdf#page=3\|PDF tr. 3]] | observed |
| Formalization dùng $F:(R,S,x) \mapsto y$ và $N$-way $K$-shot. | [[FewRel - A Large-Scale Supervised Few-Shot Relation Classification Dataset with State-of-the-Art Evaluation.pdf#page=3\|PDF tr. 3]], [[FewRel - A Large-Scale Supervised Few-Shot Relation Classification Dataset with State-of-the-Art Evaluation.pdf#page=4\|PDF tr. 4]] | observed |
| Prototypical Network là baseline mạnh nhất trong Table 4 nhưng còn xa human ở 1-shot. | [[FewRel - A Large-Scale Supervised Few-Shot Relation Classification Dataset with State-of-the-Art Evaluation.pdf#page=4\|PDF tr. 4]] | observed/reported |
| Relation classification trong FewRel cần nhiều kiểu reasoning khác nhau, không chỉ pattern matching. | [[FewRel - A Large-Scale Supervised Few-Shot Relation Classification Dataset with State-of-the-Art Evaluation.pdf#page=5\|PDF tr. 5]] | observed/inferred |

## Liên kết

- [[Relation Extraction]]
- [[Few-shot Learning]]
- [[Continual Few-Shot Relation Extraction]]
- [[20 - Research/Literature Notes/Continual Relation Extraction - Prototype, Prompt và Replay]]
- [[30 - Projects/Research Projects/Continual Relation Extraction with Task-Aware Prompt Adaptation/Reading Queue và Paper Decisions]]
