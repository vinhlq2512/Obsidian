---
type: course-source
course: "[[CS224N]]"
status: completed
source_type: paper
title: "2021 - LoRA - Low-Rank Adaptation of Large Language Models"
year: 2021
venue: "arXiv"
arxiv: "2106.09685v2"
source_file: "[[2021 - LoRA - Low-Rank Adaptation of Large Language Models - arXiv 2106.09685v2.pdf]]"
pages: 26
created_at: 2026-08-02
updated_at: 2026-08-03
completed_at: 2026-08-03
related_concepts:
  - "[[Large Language Model]]"
  - "[[Autoregressive Language Model]]"
  - "[[Parameter-Efficient Fine-Tuning]]"
  - "[[LoRA]]"
  - "[[QLoRA]]"
  - "[[Adapter]]"
tags:
  - cs224n
  - paper
---
# 2021 - LoRA - Low-Rank Adaptation of Large Language Models - arXiv 2106.09685v2

## Nguồn

- PDF gốc: [[2021 - LoRA - Low-Rank Adaptation of Large Language Models - arXiv 2106.09685v2.pdf]]
- Đọc cùng: [[CS224N 2026 - Lecture 09 - Efficient Adaptation]]
- Concept: [[LoRA]], [[Parameter-Efficient Fine-Tuning]], [[QLoRA]]

## Vấn đề paper giải quyết

Full fine-tuning LLM rất tốn kém, đặc biệt khi phải deploy nhiều model/task-specific copies. LoRA hỏi: có thể giữ nguyên weight pretrained và chỉ học một update nhỏ hạng thấp không?

Với model cỡ GPT-3, lưu một bản fine-tuned đầy đủ cho mỗi task gần như không thực tế. Paper đặt mục tiêu giữ chất lượng tương đương full fine-tuning nhưng giảm số tham số trainable, giảm memory và tránh thêm latency inference.

## Đóng góp chính

- Freeze pretrained weights.
- Inject trainable low-rank decomposition matrices vào Transformer layers.
- Giảm mạnh số tham số trainable và memory optimizer, được báo cáo tới khoảng 10,000 lần ít tham số trainable hơn và khoảng 3 lần ít VRAM hơn trong thiết lập lớn.
- Hỗ trợ lưu nhiều task adapters nhẹ hơn so với nhiều bản full fine-tuned model.
- Có thể merge update vào weight gốc khi inference, nên không thêm độ trễ như [[Adapter]] truyền thống.

## Giả thuyết chính

LoRA dựa trên trực giác rằng LLM có intrinsic dimension thấp, và update khi fine-tune cũng có intrinsic rank thấp. Điều cần học cho task mới không nhất thiết phải là một ma trận full-rank lớn; nó có thể nằm trong một không gian con nhỏ hơn nhiều.

## Cơ chế

$$
W' = W_0 + \Delta W, \quad \Delta W = BA
$$

Với:

$$
W_0 \in \mathbb{R}^{d \times k}, \quad B \in \mathbb{R}^{d \times r}, \quad A \in \mathbb{R}^{r \times k}
$$

và:

$$
r \ll \min(d, k)
$$

Forward của layer:

$$
h = W_0x + \Delta Wx = W_0x + BAx
$$

Trong quá trình train:

- $W_0$ bị freeze.
- Chỉ $A$ và $B$ nhận gradient.
- Số tham số trainable là $r(d + k)$ thay vì $dk$.

## Khởi tạo

- $A$ được khởi tạo ngẫu nhiên theo Gaussian.
- $B$ được khởi tạo bằng 0.

Nhờ vậy ở bước đầu $\Delta W = BA = 0$, nên model bắt đầu đúng từ hành vi pretrained thay vì bị nhiễu bởi nhánh LoRA chưa học gì.

## Hyperparameters cần nhớ

- Rank $r$: điều khiển capacity của update hạng thấp. Rank rất nhỏ như $r=1$ hoặc $r=2$ vẫn có thể hoạt động tốt trong một số task, cho thấy update cần thiết có thể rất nén.
- `lora_alpha` $\alpha$: scale update LoRA, thường theo $\alpha / r$.
- Target modules: paper cho thấy gắn LoRA vào cả $W_q$ và $W_v$ thường cho trade-off tốt, thay vì dồn toàn bộ tham số chỉ vào một ma trận.

## Inference

Sau training, có thể merge:

$$
W = W_0 + BA
$$

Khi đã merge, layer vẫn là một phép linear như ban đầu. Đây là lý do LoRA không tăng inference latency, trong khi adapter bottleneck có thể làm forward path dài hơn.

## Kết quả và ý nghĩa

- LoRA đạt chất lượng ngang bằng hoặc tốt hơn full fine-tuning trên các model như RoBERTa, DeBERTa, GPT-2 và GPT-3 trong các thí nghiệm của paper.
- Một base model có thể phục vụ nhiều task bằng cách swap các LoRA weights nhỏ.
- LoRA trở thành nền tảng thực dụng cho nhiều pipeline fine-tuning LLM sau này, đặc biệt khi kết hợp với [[QLoRA]].

## Vì sao quan trọng với CS224N

Lecture 09 dùng LoRA như ví dụ PEFT cốt lõi: adapt model lớn bằng một phần nhỏ tham số.

## Hạn chế / câu hỏi

- Rank quá thấp có thể thiếu capacity.
- Chọn layer nào để áp dụng LoRA là quyết định quan trọng.
- Không thay thế hoàn toàn full fine-tuning trong mọi domain/task.
- Khi kết hợp nhiều adapter/task, cần kiểm soát xung đột hành vi.

## Câu hỏi review

1. LoRA freeze cái gì và train cái gì?
2. Vì sao low-rank update tiết kiệm tham số?
3. LoRA khác adapter bottleneck như thế nào?
4. Vì sao khởi tạo $B=0$ làm training ổn định hơn ở bước đầu?
5. `lora_alpha` và rank $r$ ảnh hưởng gì tới update?
6. Vì sao LoRA có thể không tăng latency khi inference?

## Gợi ý trả lời câu hỏi review

1. LoRA freeze $W_0$ của model pretrained và chỉ train hai ma trận nhỏ $A$, $B$.
2. Vì update full $dk$ tham số được thay bằng $r(d+k)$ tham số, với $r$ nhỏ hơn nhiều so với $d$ và $k$.
3. Adapter thêm module mới vào đường forward; LoRA học update trên ma trận trọng số và có thể merge vào weight gốc.
4. Vì khi $B=0$, $\Delta W=0$, model ban đầu không bị lệch khỏi pretrained behavior.
5. $r$ tăng capacity, còn $\alpha/r$ scale độ mạnh của update.
6. Vì sau training có thể dùng $W = W_0 + BA$ như một ma trận linear duy nhất.
