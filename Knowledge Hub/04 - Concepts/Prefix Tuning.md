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
  - peft
  - prompting
  - transformer
---

# Prefix Tuning

## Định nghĩa

Prefix tuning là một kỹ thuật [[Parameter-Efficient Fine-Tuning]] học các vector prefix liên tục rồi chèn chúng vào key/value của attention ở các layer Transformer, trong khi phần lớn hoặc toàn bộ backbone pretrained được đóng băng.

Nó là **learned continuous prompting**, khác với [[Prompt Engineering]] dùng instruction/text do con người viết ở input.

## Cách hiểu bằng lời của tôi

Thay vì sửa toàn bộ Transformer, prefix tuning thêm một số “memory slots” học được vào attention. Token thật có thể attend tới các slots này, nên prefix điều hướng representation mà không cần update hàng trăm triệu backbone parameters.

```text
input tokens -> query như cũ
prefix vectors + input tokens -> key/value mở rộng
attention -> representation thích nghi task
```

## Cơ chế

Cho input query/key/value $X_Q,X_K,X_V$ và prefix:

$$
P=[P^K;P^V],\qquad P^K,P^V\in\mathbb R^{L\times d}
$$

Prefix-tuned attention:

$$
f_{prompt}^{Pre-T}(P,X_Q,X_K,X_V)
=MSA\left(X_Q,
\begin{bmatrix}P^K\\X_K\end{bmatrix},
\begin{bmatrix}P^V\\X_V\end{bmatrix}\right)
$$

Prefix không được thêm vào query nên số output positions cho input gốc không đổi. Trong setup WAVE++, backbone projection matrices bị freeze, chỉ prefix/prompt parameters và downstream classifier được học. [[Capturing Within-Task Variance for Continual Relation Extraction with Adaptive Prompting.pdf#page=5|WAVE++ PDF, tr. 5]]

## So với các kỹ thuật gần

| Kỹ thuật | Thứ được thêm/đổi | Vị trí chính | Đặc điểm |
|---|---|---|---|
| Prompt engineering | Text tokens | Input | Không train parameters mới |
| Prompt tuning | Learned embeddings | Thường input layer | Đơn giản, capacity phụ thuộc model scale |
| Prefix tuning | Learned key/value prefixes | Nhiều attention layers | Tác động trực tiếp attention ở nhiều layer |
| [[Adapter]] | Bottleneck modules | Giữa các sublayers | Thêm computation tuần tự |
| [[LoRA]] | Low-rank weight updates | Projection matrices | Merge được vào weights trong nhiều setup |
| Full fine-tuning | Toàn bộ weights | Toàn model | Capacity cao, train/storage lớn |

## Nhìn từ Mixture of Experts

WAVE/WAVE++ diễn giải một attention head như tập [[Mixture of Experts|MoE]]: attention weights đóng vai trò gating scores, còn value transformations là expert outputs.

Theo cách nhìn này, mỗi prefix key/value thêm một **prefix expert**:

- $P^K$ ảnh hưởng score/gating của prefix expert.
- $P^V$ quyết định output vector của prefix expert.
- $L$ prefix positions tương ứng $L$ experts bổ sung.

Đây là lens hữu ích để thiết kế [[Prompt Pool]], nhưng không nên hiểu là prefix expert có capacity giống arbitrary neural expert. Trong WAVE++, prefix expert về bản chất là offset/constant function đơn giản hơn linear/MLP experts. [[Capturing Within-Task Variance for Continual Relation Extraction with Adaptive Prompting.pdf#page=7|WAVE++ PDF, tr. 7]]

## Vì sao dùng trong continual learning?

- Backbone bị freeze nên giảm representation drift ở pretrained parameters.
- Có thể dành prefix riêng cho từng task và freeze prefix cũ.
- Storage mỗi task nhỏ hơn full checkpoint.
- [[Prompt Pool]] cho phép route input tới nhiều prefix experts trong một task.

Nhưng prefix isolation không tự bảo vệ shared classifier và tạo bài toán [[Task Identity Inference]] khi test.

## Hyperparameters quan trọng

- Prefix length $L$.
- Layer nào được chèn prefix.
- Số prompt/prefix trong pool $M$.
- Số prefix được chọn $K$.
- Cách khởi tạo keys/values.
- Learning rate riêng cho prefix và classifier.
- Backbone có freeze hoàn toàn hay không.

Trong WAVE++, đặt mỗi prompt có $L=1$ giúp mỗi prefix expert có key riêng; khi giữ tổng experts cố định, setting $L=1,K=8$ tốt nhất trong sweep TACRED nhưng hơn $L=8,K=1$ chỉ 0,2 điểm ở stage cuối. [[Capturing Within-Task Variance for Continual Relation Extraction with Adaptive Prompting.pdf#page=19|WAVE++ PDF, tr. 19]]

## Giới hạn

- Prefix vectors có capacity hạn chế so với update weights hoặc experts phức tạp.
- Prefix dài làm attention KV cache/computation tăng.
- Prompt selection sai có thể làm performance giảm mạnh.
- Mỗi task thêm prefix làm parameter count tăng theo thời gian.
- Freeze backbone bảo vệ kiến thức cũ nhưng hạn chế domain adaptation sâu.

## Câu hỏi review

1. Prefix tuning thêm parameters vào đâu?
2. Vì sao không thêm prefix vào query trong formulation này?
3. Prefix tuning khác prompt engineering thế nào?
4. Một prefix token được nhìn như expert ra sao?
5. Vì sao $L=1$ có thể làm routing linh hoạt hơn trong prompt pool?

## Gợi ý trả lời

1. Learned prefix key/value ở attention layers.
2. Để giữ nguyên số query/output positions của input và chỉ mở rộng memory attention.
3. Prefix là continuous parameters được train; prompt engineering là thiết kế text/instruction.
4. Key điều khiển gate, value tạo output mà attention trộn vào token representation.
5. Mỗi expert có key riêng thay vì nhiều experts bị buộc chia sẻ một prompt key.

## Liên kết

- [[Parameter-Efficient Fine-Tuning]]
- [[Prompt Pool]]
- [[Mixture of Experts]]
- [[Self-Attention]]
- [[Multi-Head Attention]]
- [[Transformer]]
- [[Continual Learning]]
- [[Prompt Engineering]]
