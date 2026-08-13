---
type: concept
status: seed
sources:
  - "[[Adaptive Prompting for Continual Relation Extraction]]"
  - "[[WAVE++ - Capturing Within-Task Variance for Continual Relation Extraction]]"
source_sections:
  - "[[Adaptive Prompting for Continual Relation Extraction#1. Prefix tuning như thêm experts vào self-attention]]"
  - "[[WAVE++ - Capturing Within-Task Variance for Continual Relation Extraction#1. Prefix-tuning nhìn từ Mixture of Experts]]"
first_seen: 2026-08-13
last_updated: 2026-08-13
created_at: 2026-08-13
updated_at: 2026-08-13
tags:
  - concept
  - mixture-of-experts
  - sparse-models
  - transformer
---

# Mixture of Experts

## Định nghĩa

Mixture of Experts (MoE) là kiến trúc gồm nhiều expert functions và một gating/router quyết định expert nào đóng góp cho từng input. Mục tiêu là tăng capacity hoặc specialization mà không nhất thiết chạy toàn bộ experts cho mọi sample.

## Công thức cơ bản

Với experts $f_j(x)$ và score functions $s_j(x)$:

$$
y=\sum_{j=1}^{N}G_j(x)f_j(x),\qquad
G_j(x)=\frac{\exp s_j(x)}{\sum_{\ell=1}^{N}\exp s_\ell(x)}
$$

Dense MoE trộn mọi expert. Sparse MoE chỉ giữ top-$K$ scores:

$$
y=\sum_{j=1}^{N}
softmax(TopK(s(x),K))_j f_j(x)
$$

## Cách hiểu bằng lời của tôi

MoE tách hai câu hỏi:

1. “Ai biết xử lý input này?” — router/gate.
2. “Xử lý như thế nào?” — expert.

Capacity có thể lớn vì có nhiều experts, nhưng compute mỗi token/sample vẫn giới hạn nếu chỉ route tới top-$K$.

## Dense và sparse

| Dạng | Experts chạy mỗi input | Điểm mạnh | Rủi ro |
|---|---:|---|---|
| Dense mixture | Gần như tất cả | Smooth combination | Compute tăng theo số experts |
| Sparse MoE | Top-$K$ | Tăng capacity mà compute thấp hơn | Router imbalance, communication overhead |

## Attention nhìn như MoE

WAVE/WAVE++ chỉ ra một attention-head output tại position $i$:

$$
h_i=\sum_j
\frac{\exp s_{i,j}(X)}{\sum_k\exp s_{i,k}(X)}f_j(X)
$$

có cùng hình thức với MoE:

- value-transformed token $j$ đóng vai expert output $f_j$;
- query-key score đóng vai gate $s_{i,j}$;
- mỗi query position dùng gate riêng nhưng chia sẻ expert set.

Vì vậy một attention head có thể được nhìn như nhiều gated mixtures, không phải Transformer đã cài một sparse-MoE feed-forward layer theo nghĩa triển khai phổ biến. [[Capturing Within-Task Variance for Continual Relation Extraction with Adaptive Prompting.pdf#page=6|WAVE++ PDF, tr. 6]] [[Capturing Within-Task Variance for Continual Relation Extraction with Adaptive Prompting.pdf#page=7|WAVE++ PDF, tr. 7]]

## Prefix tuning như thêm experts

Khi thêm prefix key/value:

- prefix value tạo expert output mới;
- prefix key tạo score mới với mỗi query;
- attention trộn prefix experts với pretrained token experts.

Lens này giải thích vì sao [[Prompt Pool]] giống sparse expert pool: query chọn top-$K$ prompts/prefix experts theo keys.

Nhưng prefix experts trong formulation này là simple offset/constant functions. Chúng không có capacity tùy ý như MLP experts, nên “tương đương MoE” là tương đương về **dạng weighted mixture**, không phải mọi thuộc tính kiến trúc.

## Router là điểm nghẽn

MoE chỉ mạnh khi routing tốt. Failure modes:

- load imbalance: một vài experts nhận hầu hết tokens;
- expert collapse/dead experts;
- router noise/instability;
- capacity overflow và dropped tokens;
- communication cost giữa devices;
- semantic specialization không xuất hiện dù loss tốt;
- task/input shift làm router chọn sai experts.

Trong continual learning, router còn có thể quên hoặc prompt keys bị drift, nên routing accuracy cần được đo riêng.

## MoE trong continual learning

Một expert/pool riêng theo task giảm interference:

```text
task cũ -> freeze experts cũ
task mới -> thêm experts mới
```

Nhưng capacity tăng theo task và inference không biết sẵn expert nào đúng. WAVE++ xử lý bằng [[Task Identity Inference|cascade voting]] rồi route bên trong task pool.

## Khi áp dụng

MoE hữu ích khi:

- data có nhiều modes/domains/tasks;
- muốn tăng model capacity nhưng giữ active compute có giới hạn;
- có đủ traffic/data để experts chuyên môn hóa;
- hệ thống chịu được routing và distributed communication complexity.

Không nên dùng chỉ vì “nhiều experts nghe mạnh”: với dataset nhỏ, router có thể học kém và overhead lớn hơn lợi ích.

## Câu hỏi review

1. Gate và expert có vai trò gì?
2. Sparse MoE giảm compute bằng cách nào?
3. Attention giống MoE ở dạng toán nào?
4. Prefix token trở thành expert theo cách hiểu nào?
5. Vì sao task-specific experts không tự giải quyết continual learning?

## Gợi ý trả lời

1. Gate chọn/trộn; expert biến đổi input.
2. Chỉ active top-$K$ experts thay vì tất cả.
3. Output là weighted sum các value/expert outputs với normalized query-key/gating scores.
4. Prefix key tạo gate score, prefix value tạo output được trộn vào attention.
5. Phải suy đúng task/expert ở test, shared components vẫn có thể quên, và memory tăng theo task.

## Liên kết

- [[Prefix Tuning]]
- [[Prompt Pool]]
- [[Self-Attention]]
- [[Multi-Head Attention]]
- [[Transformer]]
- [[Continual Learning]]
- [[Task Identity Inference]]
