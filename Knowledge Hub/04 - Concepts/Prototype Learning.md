---
type: concept
status: seed
sources:
  - "[[20 - Research/Papers/Consistent Prototype Learning for Few-Shot Continual Relation Extraction]]"
source_sections:
  - "[[20 - Research/Papers/Consistent Prototype Learning for Few-Shot Continual Relation Extraction#Module 1 — Prototype-based classification]]"
  - "[[20 - Research/Papers/Consistent Prototype Learning for Few-Shot Continual Relation Extraction#Module 2 — Memory-enhanced learning]]"
first_seen: 2026-08-13
last_updated: 2026-08-13
created_at: 2026-08-13
updated_at: 2026-08-13
tags:
  - concept
  - prototype-learning
  - metric-learning
  - few-shot
---

# Prototype Learning

## Định nghĩa

Prototype learning biểu diễn mỗi class bằng một hoặc nhiều vector đại diện trong embedding space và phân loại sample dựa trên độ gần/similarity tới các prototypes.

Với class $c$ có support set $S_c$:

$$
p_c=\frac{1}{|S_c|}\sum_{(x_i,y_i=c)}f_\theta(x_i)
$$

Một classifier đơn giản dùng:

$$
P(y=c\mid x)=
\frac{\exp(sim(f_\theta(x),p_c)/\tau)}
{\sum_{c'}\exp(sim(f_\theta(x),p_{c'})/\tau)}
$$

## Cách hiểu bằng lời của tôi

Prototype là “điểm neo nghĩa” của class. Sample mới được gán nhãn theo điểm neo gần nhất. Trong few-shot setting, đây là inductive bias mạnh: thay vì học classifier head có nhiều parameters từ vài examples, ta học không gian mà samples cùng class tụ lại.

## Prototype có thể được tạo thế nào?

- Mean của support embeddings.
- Medoid/exemplar gần center nhất.
- Learned parameter được update bằng gradient.
- Refined prototype kết hợp support, memory hoặc attention.
- Nhiều prototypes cho một class đa mode.
- Distribution $(\mu,\Sigma)$ thay vì một điểm.

ConPL tính mean prototype từ $K$ examples, chọn exemplar gần mean nhất rồi dùng feature của exemplar để khởi tạo/refine prototype lưu trong memory. [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=4|ConPL PDF, tr. 4]] [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=5|ConPL PDF, tr. 5]]

## Prototype distortion

Trong continual learning, encoder $f_\theta$ đổi theo task mới. Khi đó:

- sample cũ đi tới vị trí latent mới;
- prototype lưu từ encoder cũ có thể không còn khớp;
- hoặc prototype được update bằng memory quá nhỏ và trôi khỏi class center thật.

Prototype distortion làm old class activation yếu đi và tăng confusion với relation gần nghĩa. ConPL quan sát distortion và forgetting có quan hệ, nhưng paper không báo hệ số tương quan và vẫn có outliers; đây là evidence gợi ý chứ chưa phải causal proof.

## Sample memory + prototype memory

Hai dạng memory bổ sung nhau:

| Dạng | Giữ gì? | Điểm yếu |
|---|---|---|
| Exemplar | Một input/instance thật | Coverage thấp, privacy/storage |
| Prototype | Summary của class | Mất within-class modes |

ConPL lưu một exemplar và một prototype vector mỗi relation. Exemplar dùng replay; prototype làm anchor hình học và classifier. Vì vẫn lưu raw exemplar, method là rehearsal-based.

## Consistency ở hai mức

### Classification consistency

Kéo memory sample về đúng prototype:

$$
\mathcal L_{cc}=\sum_i\|f_\theta(x_i)-p_{y_i}\|
$$

### Distribution consistency

Giữ vector similarity từ sample tới **toàn bộ** prototypes gần với vector similarity từ đúng prototype tới toàn bộ prototypes:

$$
\mathcal L_{dc}
=\sum_i\|d(f_\theta(x_i),P)-d(p_{y_i},P)\|
$$

Vế thứ hai bảo vệ relative class geometry, không chỉ khoảng cách sample–own-prototype.

## Hard/similar classes

Nếu hai relation prototypes gần nhau, full softmax có thể dành gradient cho nhiều negatives dễ. ConPL tạo tập gồm positive prototype và confusing negative prototypes rồi tính classification loss trong tập đó.

Paper gọi loss này là focal loss, nhưng công thức công bố không có hệ số $(1-p)^\gamma$ của focal loss chuẩn. Cách diễn giải sát công thức hơn là **hard/similar-negative restricted cross-entropy**.

Ablation cho thấy bỏ loss này làm FewRel 10-way 5-shot ở $T_8$ giảm 10,66 điểm, lớn hơn nhiều so với bỏ các consistency terms riêng lẻ. [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=8|ConPL PDF, tr. 8]]

## Failure modes

- K-shot mean có variance cao.
- Class đa mode không phù hợp một centroid.
- Cosine distance/similarity convention bị dùng lẫn.
- Prototype collapse hoặc classes quá gần.
- Encoder drift làm stored prototype stale.
- Chọn sample gần center bỏ qua boundary/hard examples.
- Prototype accuracy tốt nhưng calibration kém.

## Khi áp dụng

- Few-shot classification với embedding tốt.
- Incremental classes cần memory nhỏ.
- Cần classifier giải thích bằng nearest class anchors.
- Labels có geometry/semantic similarity đáng khai thác.

Nên dùng nhiều prototypes hoặc distribution model nếu một class có nhiều modes rõ rệt.

## Câu hỏi review

1. Prototype classifier khác learned linear head thế nào?
2. Vì sao prototype hữu ích trong few-shot setting?
3. Prototype distortion xảy ra do đâu?
4. Exemplar và prototype memory bổ sung nhau ra sao?
5. $L_{dc}$ giữ thông tin gì mà $L_{cc}$ không giữ?

## Gợi ý trả lời

1. Nó phân loại bằng similarity tới class anchors thay vì học riêng weight/logit boundary từ nhiều data.
2. Mean/anchor là inductive bias đơn giản, ít parameters và tận dụng embedding geometry.
3. Encoder update, memory nhỏ hoặc update prototype không đại diện làm class anchor trôi.
4. Exemplar giữ input cụ thể; prototype giữ summary và relative class geometry.
5. Quan hệ của sample/class với toàn bộ prototypes, không chỉ khoảng cách tới own prototype.

## Liên kết

- [[Few-shot Learning]]
- [[Continual Few-Shot Relation Extraction]]
- [[Continual Learning]]
- [[Replay in Continual Learning]]
- [[Embedding]]
- [[Contrastive Learning]]
- Cosine similarity
