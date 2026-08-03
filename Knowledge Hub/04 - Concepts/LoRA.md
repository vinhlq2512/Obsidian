---
type: concept
status: understood
sources:
  - "[[2021 - LoRA - Low-Rank Adaptation of Large Language Models - arXiv 2106.09685v2]]"
  - "[[CS224N 2026 - Lecture 09 - Efficient Adaptation]]"
source_sections:
  - "[[2021 - LoRA - Low-Rank Adaptation of Large Language Models - arXiv 2106.09685v2]]"
  - "[[CS224N 2026 - Lecture 09 - Efficient Adaptation]]"
first_seen: 2026-08-03
last_updated: 2026-08-03
tags:
  - concept
  - peft
  - llm
  - cs224n
---

# LoRA

## Định nghĩa

LoRA (Low-Rank Adaptation) là một phương pháp [[Parameter-Efficient Fine-Tuning]] dùng để tinh chỉnh model lớn bằng cách đóng băng trọng số gốc và chỉ học một update hạng thấp cho một số ma trận quan trọng.

Thay vì tạo một bản full fine-tuned model cho từng task, ta giữ chung model pretrained và lưu riêng các ma trận LoRA nhỏ.

## Vấn đề LoRA giải quyết

Full fine-tuning LLM tốn kém ở ba chỗ:

- Cần lưu một bản model lớn cho mỗi task/domain.
- Cần VRAM lớn vì phải giữ gradient, optimizer state và activation cho rất nhiều tham số.
- Khó triển khai nhiều biến thể model nếu mỗi biến thể đều là một checkpoint đầy đủ.

LoRA nhắm vào câu hỏi: nếu update khi fine-tune thực ra nằm trong một không gian con rất nhỏ, ta có cần cập nhật toàn bộ ma trận trọng số không?

## Giả thuyết low-rank

Cơ sở trực giác của LoRA là các LLM thường có intrinsic dimension thấp: tuy model có rất nhiều tham số, thay đổi cần thiết để thích ứng với một task có thể nằm trong không gian chiều thấp hơn nhiều.

LoRA giả thuyết rằng weight update trong fine-tuning có intrinsic rank thấp. Nói cách khác, phần $\Delta W$ cần học không cần là một ma trận đầy đủ; nó có thể được biểu diễn bằng tích của hai ma trận nhỏ hơn.

## Cơ chế

Với một ma trận trọng số pretrained $W_0$, LoRA làm ba việc:

- Freeze $W_0$: trọng số gốc không nhận gradient.
- Tạo nhánh trainable song song gồm hai ma trận nhỏ $A$ và $B$.
- Cộng update hạng thấp $\Delta W = BA$ vào output của layer.

Khi train, chỉ $A$ và $B$ được cập nhật. Khi deploy, update này có thể merge vào $W_0$.

## Công thức

Giả sử:

$$
W_0 \in \mathbb{R}^{d \times k}
$$

LoRA biểu diễn update:

$$
\Delta W = BA
$$

Trong đó:

$$
B \in \mathbb{R}^{d \times r}, \quad A \in \mathbb{R}^{r \times k}, \quad r \ll \min(d, k)
$$

Output của layer:

$$
h = W_0x + \Delta Wx = W_0x + BAx
$$

Số tham số trainable giảm từ $d \times k$ xuống $r(d + k)$.

## Khởi tạo

LoRA thường khởi tạo:

- $A$ ngẫu nhiên theo Gaussian.
- $B = 0$.

Vì $B = 0$, ban đầu $\Delta W = BA = 0$. Model bắt đầu với hành vi giống model pretrained, rồi dần học phần điều chỉnh qua LoRA.

## Hyperparameters

- Rank $r$: kích thước bottleneck của update hạng thấp. $r$ càng lớn thì capacity càng cao nhưng số tham số càng nhiều. Paper cho thấy LoRA vẫn hiệu quả ngay cả với rank rất nhỏ như $r=1$ hoặc $r=2$ trong một số thiết lập.
- `lora_alpha` $\alpha$: hệ số scale cho update LoRA, thường dùng dạng $\alpha / r$. Nó kiểm soát mức độ ảnh hưởng của update mới so với trọng số gốc.
- Dropout: đôi khi dùng trên nhánh LoRA để regularize khi fine-tune trên dữ liệu nhỏ.
- Target modules: chọn ma trận nào trong Transformer để gắn LoRA.

## Target modules

LoRA có thể áp dụng cho nhiều linear layer, nhưng thường được gắn vào self-attention.

Các target phổ biến:

- $W_q$: ma trận tạo query.
- $W_v$: ma trận tạo value.
- Đôi khi thêm $W_k$, $W_o$ hoặc MLP projection nếu cần nhiều capacity hơn.

Trong paper LoRA, áp dụng cho cả $W_q$ và $W_v$ thường cho trade-off tốt hơn so với dồn toàn bộ tham số vào một loại ma trận.

## Vì sao không tăng inference latency?

Adapter truyền thống thường thêm module mới vào đường forward, nên inference có thể chậm hơn.

LoRA thì khác: sau khi train, ta có thể merge:

$$
W = W_0 + BA
$$

Khi đã merge, inference vẫn chỉ dùng một phép nhân tuyến tính như model gốc. Vì vậy LoRA không làm tăng độ trễ suy luận nếu dùng chế độ merged weights.

## So sánh với Adapter

| Điểm so sánh | [[Adapter]] | LoRA |
|---|---|---|
| Cách thêm capacity | Chèn module bottleneck vào layer | Thêm update hạng thấp cho ma trận trọng số |
| Trọng số gốc | Thường freeze | Freeze |
| Inference latency | Có thể tăng vì thêm module | Không tăng nếu merge $BA$ vào $W_0$ |
| Lưu nhiều task | Lưu nhiều adapter | Lưu nhiều cặp $A, B$ |
| Mental model | Thêm một hàm biến đổi phụ | Học một hướng cập nhật nén cho weight |

## Ưu điểm

- Giảm mạnh số tham số cần train, được báo cáo có thể tới khoảng 10,000 lần so với full fine-tuning trong các thiết lập lớn.
- Giảm nhu cầu VRAM, gồm cả optimizer state, được báo cáo khoảng 3 lần trong paper.
- Không tăng inference latency khi merge update vào weight gốc.
- Có thể đạt chất lượng ngang bằng hoặc tốt hơn full fine-tuning trên các model như RoBERTa, DeBERTa, GPT-2 và GPT-3.
- Dễ swap task: giữ một base model, thay các LoRA weights nhỏ theo task/domain.

## Hạn chế

- Rank quá thấp có thể thiếu capacity cho task hoặc domain khác xa pretraining.
- Chọn target modules sai có thể làm hiệu quả kém.
- Nếu merge nhiều LoRA adapter không kiểm soát, hành vi model có thể xung đột.
- LoRA tiết kiệm tham số trainable nhưng không tự giải quyết toàn bộ chi phí activation, dữ liệu và đánh giá.

## QLoRA

[[QLoRA]] mở rộng LoRA bằng cách quantize trọng số model gốc xuống 4-bit, thường dùng 4-bit NormalFloat, trong khi vẫn train các LoRA adapters ở độ chính xác phù hợp.

Ý tưởng chính: base model được nén để giảm memory, còn update task-specific vẫn được học bằng LoRA. Kết hợp này giúp fine-tune LLM lớn trên GPU tiêu dùng dễ hơn.

Ba mảnh kỹ thuật chính của QLoRA:

- NF4: định dạng 4-bit phù hợp với trọng số có phân phối gần chuẩn.
- Double quantization: nén thêm scaling constants sinh ra khi quantize theo block.
- Paged optimizers: xử lý memory spike bằng cách page optimizer state giữa GPU và CPU.

## Cách hiểu bằng lời của tôi

LoRA giống như không viết lại cả cuốn sách của model, mà chỉ kẹp thêm một tờ ghi chú rất nhỏ vào đúng vài trang quan trọng. Tờ ghi chú đó nói model nên lệch theo hướng nào cho task mới. Vì tờ ghi chú nhỏ, ta lưu được nhiều task; vì nó có thể nhập vào sách gốc khi deploy, lúc đọc không bị chậm hơn.

## Câu hỏi review

1. Vì sao LoRA giả định $\Delta W$ có thể có rank thấp?
2. Nếu $W_0 \in \mathbb{R}^{d \times k}$ và rank là $r$, số tham số trainable của LoRA là bao nhiêu?
3. Vì sao khởi tạo $B = 0$ giúp LoRA không làm xáo trộn model ở bước đầu?
4. `lora_alpha` ảnh hưởng gì tới update LoRA?
5. Vì sao LoRA không tăng inference latency sau khi merge?
6. Khi nào nên tăng rank $r$ hoặc mở rộng target modules?

## Liên kết

- [[Parameter-Efficient Fine-Tuning]]
- [[QLoRA]]
- [[Adapter]]
- [[Fine-tuning]]
- [[Transformer]]
- [[Large Language Model]]
- [[CS224N]]
