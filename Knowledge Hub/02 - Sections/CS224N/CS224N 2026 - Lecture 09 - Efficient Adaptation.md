---
type: course-source
course: "[[CS224N]]"
status: completed
source_type: lecture
title: "CS224N 2026 - Lecture 09 - Efficient Adaptation"
year: 2026
venue: ""
arxiv: ""
source_file: "[[CS224N 2026 - Lecture 09 - Efficient Adaptation.pdf]]"
pages: 67
created_at: 2026-08-02
updated_at: 2026-08-03
completed_at: 2026-08-03
related_concepts:
  - "[[Parameter-Efficient Fine-Tuning]]"
  - "[[LoRA]]"
  - "[[QLoRA]]"
  - "[[Adapter]]"
tags:
  - cs224n
  - lecture
---
# CS224N 2026 - Lecture 09 - Efficient Adaptation

## Nguồn

- PDF gốc: [[CS224N 2026 - Lecture 09 - Efficient Adaptation.pdf]]
- Vai trò trong khoá: các phương pháp adapt model lớn với ít tham số và ít compute.
- Paper đọc kèm: [[2021 - LoRA - Low-Rank Adaptation of Large Language Models - arXiv 2106.09685v2]], [[2019 - Parameter-Efficient Transfer Learning for NLP - arXiv 1902.00751v2]], [[2019 - The Lottery Ticket Hypothesis - Finding Sparse Trainable Neural Networks - arXiv 1803.03635v5]].

## Mục tiêu cần hiểu

- Vì sao full fine-tuning tốn kém khi model lớn.
- Prompting, pruning, adapters, LoRA và prompt-tuning trade-off ra sao.
- PEFT thay đổi ít tham số nhưng vẫn tạo hành vi task-specific.
- LoRA xem update trọng số như ma trận hạng thấp.

## Ý chính

- Full fine-tuning cập nhật toàn bộ model, mạnh nhưng tốn memory/compute và khó quản lý nhiều task.
- [[Adapter]] chèn module nhỏ vào giữa layer, thường có bottleneck down-projection/up-projection.
- [[LoRA]] freeze weight gốc và học update hạng thấp $\Delta W = BA$.
- [[QLoRA]] tiếp tục giảm memory bằng cách quantize base model xuống 4-bit và train LoRA adapters.
- Prompt-tuning học prompt embedding liên tục, rất ít tham số nhưng capacity thấp hơn.
- Pruning/subnetwork tìm phần model cần giữ hoặc train, liên quan tới giả thuyết lottery ticket.

## [[Adapter]]

Adapter thường có dạng bottleneck:

$$
f_\phi(x) = W_U\sigma(W_Dx)
$$

Trong đó:

- $W_D \in \mathbb{R}^{k \times d}$ giảm chiều.
- $W_U \in \mathbb{R}^{d \times k}$ tăng chiều lại.
- $k \ll d$ nên số tham số train thêm nhỏ.

## [[LoRA]]

LoRA giả định update cần thiết cho task có intrinsic rank thấp:

$$
W' = W_0 + \Delta W, \quad \Delta W = BA
$$

- Freeze $W$ gốc.
- Chỉ train $A$ và $B$.
- Nếu $W_0 \in \mathbb{R}^{d \times k}$, dùng $B \in \mathbb{R}^{d \times r}$ và $A \in \mathbb{R}^{r \times k}$ với $r \ll \min(d,k)$.
- Forward: $h = W_0x + BAx$.
- `lora_alpha` thường scale update theo $\alpha/r$.
- Target module quan trọng trong attention là $W_q$ và $W_v$.
- Giảm memory optimizer và cho phép lưu nhiều adapter/task-specific update.
- Có thể merge $BA$ vào $W_0$ nên inference không cần thêm module.

## [[QLoRA]]

QLoRA kết hợp LoRA với quantization:

- Base model được giữ ở 4-bit, thường theo NF4 (NormalFloat 4-bit).
- LoRA adapters vẫn là phần được train cho task.
- Double quantization nén thêm các scaling constants sinh ra khi quantize theo block.
- Paged optimizers giúp giảm memory spike bằng cách page optimizer state giữa GPU và CPU.
- Phù hợp khi muốn fine-tune LLM lớn trên GPU hạn chế.

## Cách hiểu bằng lời của tôi

Efficient adaptation là nghệ thuật “đổi hành vi mà không đụng quá nhiều vào model”. Thay vì sao chép và train lại toàn bộ LLM cho mỗi task, ta thêm hoặc học một phần nhỏ đủ để uốn model theo domain/task.

## Câu hỏi review

1. PEFT giải quyết vấn đề gì của full fine-tuning?
2. [[Adapter]] bottleneck tiết kiệm tham số như thế nào?
3. [[LoRA]] học cái gì nếu weight gốc bị freeze?
4. Prompt-tuning có điểm yếu gì so với adapter/LoRA?
5. Vì sao cần ràng buộc không làm model drift quá xa?
6. [[QLoRA]] thêm gì vào LoRA để giảm memory?

## Liên kết

- [[Parameter-Efficient Fine-Tuning]]
- [[LoRA]]
- [[QLoRA]]
- [[Fine-tuning]]
- [[DPO]]
- [[Large Language Model]]
- [[CS224N]]
