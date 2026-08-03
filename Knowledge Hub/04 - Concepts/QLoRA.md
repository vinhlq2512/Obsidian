---
type: concept
status: understood
sources:
  - "[[LoRA]]"
  - "[[CS224N 2026 - Lecture 09 - Efficient Adaptation]]"
source_sections:
  - "[[LoRA]]"
  - "[[CS224N 2026 - Lecture 09 - Efficient Adaptation]]"
first_seen: 2026-08-03
last_updated: 2026-08-03
tags:
  - concept
  - peft
  - quantization
  - llm
  - cs224n
---

# QLoRA

## Định nghĩa

QLoRA (Quantized Low-Rank Adaptation) là biến thể của [[LoRA]] kết hợp [[Quantization]] trọng số model gốc với low-rank adapters để giảm mạnh memory khi fine-tune LLM.

Điểm QLoRA giải quyết thêm so với LoRA: LoRA đã giảm số tham số cần train, nhưng base model vẫn phải được load vào VRAM. Nếu model có hàng chục tỷ tham số, riêng việc giữ trọng số gốc ở 16-bit đã rất đắt. QLoRA giảm phần này bằng cách quantize base model xuống 4-bit, trong khi vẫn train adapter LoRA.

## Cơ chế

- Model gốc được quantize xuống 4-bit, thường dùng 4-bit NormalFloat.
- Trọng số gốc vẫn được freeze.
- Phần task-specific được học bằng LoRA adapters.
- Paged optimizers giúp tránh spike memory khi optimizer state hoặc gradient cần nhiều bộ nhớ.

```text
Base LLM 16-bit
-> Quantize base weights xuống 4-bit NF4
-> Freeze base weights
-> Gắn LoRA adapters nhỏ vào các layer mục tiêu
-> Train LoRA adapters
-> Dùng paged optimizers để xử lý memory spike
```

## Ba cải tiến kỹ thuật cốt lõi

### 1. 4-bit NormalFloat

NF4 (NormalFloat 4-bit) là kiểu dữ liệu 4-bit được thiết kế cho trọng số có phân phối gần chuẩn, vốn thường gặp trong mạng nơ-ron.

Điểm cần nhớ:

- Không quantize tuyến tính một cách thô.
- Dùng blockwise quantization: chia trọng số thành từng khối rồi scale/normalize theo từng khối.
- Các mức biểu diễn của NF4 phù hợp hơn với phân phối chuẩn, nên giữ nhiều thông tin hơn so với các cách nén 4-bit đơn giản.
- Mục tiêu là biểu diễn trọng số gốc 16-bit bằng 4-bit với tổn thất chất lượng nhỏ.

Trực giác: nếu các trọng số tập trung nhiều quanh 0, ta nên dành nhiều mức biểu diễn hơn cho vùng có mật độ cao thay vì chia đều toàn trục số.

### 2. Double Quantization

Khi quantize theo khối, mỗi block cần một scaling constant để khôi phục xấp xỉ giá trị ban đầu. Các scaling constants này cũng tốn memory.

Double quantization tiếp tục quantize chính các scaling constants đó. Đây là "nén phần metadata của quá trình nén".

Tác dụng:

- Giảm thêm memory ngoài việc quantize trọng số.
- Hữu ích khi model rất lớn vì số lượng block và scaling constants cũng lớn.
- Giữ ý tưởng blockwise quantization nhưng giảm overhead đi kèm.

### 3. Paged Optimizers

Trong training, memory không luôn ổn định. Một số batch hoặc bước backward có thể tạo memory spike và gây Out-Of-Memory.

Paged optimizers dùng cơ chế giống virtual memory:

```text
GPU memory gần đầy
-> Một phần optimizer state được page sang CPU memory
-> Khi cần lại, dữ liệu được đưa về GPU
-> Training tránh bị crash vì spike tạm thời
```

Tác dụng chính không phải làm computation nhanh hơn, mà làm training ổn định hơn khi VRAM giới hạn.

## Vì sao quan trọng

QLoRA làm cho fine-tuning LLM lớn khả thi hơn trên GPU phổ thông. Thay vì cần lưu và train toàn bộ model ở precision cao, ta giữ base model ở dạng nén và chỉ học một phần nhỏ.

Ví dụ trực giác: nếu một model nhỏ cần khoảng 4GB VRAM để load ở precision cao, quantization có thể giảm đáng kể phần memory này, thậm chí xuống cỡ 1GB trong ví dụ đơn giản. Với model lớn hơn, lợi ích này quyết định việc model có fit vào GPU hay không.

## So với LoRA

| Điểm so sánh | [[LoRA]] | QLoRA |
|---|---|---|
| Base model | Giữ nguyên precision thường dùng | Quantize base model xuống 4-bit |
| Trainable weights | Low-rank adapters | Low-rank adapters |
| Mục tiêu chính | Giảm tham số trainable và latency | Giảm thêm memory để fine-tune model lớn hơn |
| Rủi ro | Rank/target module thiếu capacity | Thêm lỗi xấp xỉ do quantization nếu cấu hình kém |

## Khi nào dùng

Dùng QLoRA khi:

- Muốn fine-tune LLM lớn nhưng VRAM không đủ để load base model ở 16-bit.
- Chỉ cần train task/domain adapter thay vì full fine-tuning.
- Muốn thử nghiệm nhiều biến thể với chi phí lưu trữ thấp.
- Chấp nhận trade-off giữa memory và lỗi xấp xỉ do quantization.

Không nên xem QLoRA là "free lunch": nếu task cực kỳ nhạy với precision hoặc cần thay đổi sâu trong toàn bộ model, cần đánh giá kỹ với baseline.

## Cách hiểu bằng lời của tôi

LoRA giảm phần cần học. QLoRA giảm thêm phần cần giữ trong bộ nhớ. Vì vậy QLoRA là cách đưa PEFT từ "tiết kiệm tham số" sang "thực dụng trên phần cứng hạn chế".

Nói gọn: LoRA nói "đừng train cả model"; QLoRA nói thêm "và cũng đừng giữ cả model ở precision đắt nếu không cần".

## Câu hỏi review

1. QLoRA khác LoRA ở điểm nào?
2. Vì sao quantize base model giúp giảm memory fine-tuning?
3. Paged optimizer giải quyết vấn đề gì?
4. Khi nào QLoRA hữu ích hơn LoRA thường?
5. NF4 khác gì với quantization tuyến tính đơn giản?
6. Double quantization nén cái gì?
7. Vì sao memory spike có thể gây lỗi dù trung bình VRAM có vẻ đủ?

## Gợi ý trả lời câu hỏi review

1. LoRA tiêu chuẩn freeze toàn bộ trọng số của model gốc, thường vẫn giữ ở precision cao như 16-bit, và chỉ train các ma trận low-rank được chèn thêm. QLoRA giữ ý tưởng đó nhưng quantize chính base model xuống 4-bit bằng NF4, đồng thời dùng paged optimizers để quản lý memory khi huấn luyện.
2. Dù base model bị freeze trong LoRA, nó vẫn phải nằm trong VRAM để thực hiện forward pass. Khi quantize base model từ 16-bit xuống 4-bit, phần memory dùng để chứa trọng số gốc giảm trực tiếp, nên tổng VRAM cần cho fine-tuning giảm mạnh.
3. Paged optimizer xử lý các memory spikes trong training. Khi VRAM gần đầy, một phần optimizer state có thể được page giữa GPU memory và CPU RAM, tương tự cơ chế virtual memory, giúp giảm nguy cơ Out-Of-Memory.
4. QLoRA hữu ích hơn LoRA thường khi giới hạn phần cứng, đặc biệt là VRAM, là nút thắt chính. Nếu riêng base model ở 16-bit đã quá lớn để load lên GPU, LoRA thường vẫn không chạy được; QLoRA nén base model xuống 4-bit để model có thể fit trên GPU phổ thông hơn.
5. NF4 dùng các mức biểu diễn phù hợp với phân phối chuẩn của weight, không chia đều tuyến tính đơn giản.
6. Double quantization nén các scaling constants sinh ra từ blockwise quantization.
7. Vì peak memory mới là giới hạn thật; chỉ cần một bước vượt VRAM là training có thể crash.

## Trả lời bằng lời của tôi

- QLoRA = LoRA + quantized base model. LoRA chỉ làm cho phần cần train nhỏ đi; QLoRA còn làm cho phần model gốc cần giữ trong VRAM nhỏ đi.
- Quantization giúp vì frozen không có nghĩa là không cần memory. Base model vẫn phải tham gia forward pass, nên giảm bit-width của weight làm giảm trực tiếp VRAM.
- Paged optimizer là cơ chế chống OOM khi memory tăng vọt tạm thời, bằng cách luân chuyển state giữa GPU và CPU.
- QLoRA đáng dùng nhất khi LoRA thường bị kẹt ở bước load model: model gốc 16-bit quá lớn so với VRAM.

## Liên kết

- [[LoRA]]
- [[Parameter-Efficient Fine-Tuning]]
- [[Quantization]]
- [[Large Language Model]]
- [[CS224N]]
