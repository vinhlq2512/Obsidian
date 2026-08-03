---
type: course-source
course: "[[CS224N]]"
status: completed
source_type: lecture
title: "CS224N 2026 - Lecture 06 - Final Projects and Practical Tips"
year: 2026
venue: ""
arxiv: ""
source_file: "[[CS224N 2026 - Lecture 06 - Final Projects and Practical Tips.pdf]]"
pages: 53
created_at: 2026-08-02
updated_at: 2026-08-03
completed_at: 2026-08-03
related_concepts:
  - "[[NLP]]"
tags:
  - cs224n
  - lecture
---
# CS224N 2026 - Lecture 06 - Final Projects and Practical Tips

## Nguồn

- PDF gốc: [[CS224N 2026 - Lecture 06 - Final Projects and Practical Tips.pdf]]
- Vai trò trong khoá: recap Transformer và hướng dẫn chuyển kiến thức NLP thành project nghiên cứu/ứng dụng.

## Mục tiêu cần hiểu

- Phân biệt decoder, encoder và encoder-decoder Transformer.
- Hiểu cross-attention như cơ chế nối source representation với target generation.
- Biết cách chọn topic/data/baseline cho final project.

## Ý chính

- Transformer decoder dùng causal/unidirectional context, phù hợp với [[Autoregressive Language Model]].
- Transformer encoder bỏ masking trong self-attention, cho phép bidirectional context, phù hợp với understanding tasks.
- Encoder-decoder dùng encoder đọc source và decoder sinh target; decoder có thêm cross-attention vào output encoder.
- Cross-attention lấy keys/values từ encoder và queries từ decoder, nên decoder có thể “hỏi” source sentence khi sinh target token.
- Một project tốt cần câu hỏi rõ, dữ liệu có thể dùng, baseline đủ đơn giản và metric phù hợp.

## Cross-attention

Nếu encoder tạo các vector $h_1, ..., h_n$ và decoder có state $z_i$:

```text
keys, values: từ encoder outputs h
queries: từ decoder states z
```

$$
k_i = K h_i, \quad v_i = V h_i, \quad q_i = Q z_i
$$

Trực giác: decoder đang viết câu đích; ở mỗi bước nó query lại memory của câu nguồn để lấy thông tin cần thiết.

## Cách hiểu bằng lời của tôi

Encoder là phần đọc hiểu, decoder là phần viết tiếp, encoder-decoder là “đọc rồi viết”. Cross-attention là cầu nối: output encoder trở thành bộ nhớ để decoder truy cập khi sinh từng token.

## Câu hỏi review

1. Encoder khác decoder ở masking như thế nào?
2. Cross-attention lấy Q/K/V từ đâu?
3. Vì sao encoder-decoder hợp với translation/summarization?
4. Một final project NLP cần baseline để làm gì?

## Liên kết

- [[Decoder]]
- [[Encoder-Decoder Architecture]]
- [[Cross-Attention]]
- [[Transformer]]
- [[CS224N]]
