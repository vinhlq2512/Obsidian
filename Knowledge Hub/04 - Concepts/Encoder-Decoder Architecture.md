---
type: concept
status: seed
source:
  - "[[NLP Transformers - Chapter 01 - Hello Transformers]]"
  - "[[NLP Transformers - Chapter 03 - Transformer Anatomy]]"
tags:
  - concept
  - transformer
  - seq2seq
  - nlp
---

# Encoder-Decoder Architecture

## Định nghĩa

Encoder-decoder architecture là kiến trúc Transformer gồm hai phần: encoder đọc input sequence và tạo representation giàu ngữ cảnh; decoder dùng representation đó để sinh output sequence.

## Cách hiểu bằng lời của tôi

Encoder giống người đọc đề bài. Nó đọc toàn bộ input và nén thông tin thành các hidden states. Decoder giống người viết câu trả lời. Nó sinh từng token của output, vừa nhìn các token đã sinh trước đó, vừa nhìn lại thông tin từ encoder.

Mental model:

```text
input sequence
-> encoder: đọc hiểu input
-> encoder hidden states
-> decoder: sinh output từng token
-> output sequence
```

Ví dụ trong translation:

```text
English sentence
-> encoder
-> representation của câu nguồn
-> decoder
-> Vietnamese sentence
```

## Encoder làm gì?

Encoder nhận toàn bộ input ngay từ đầu. Vì vậy encoder thường dùng bidirectional self-attention: mỗi token có thể nhìn cả token bên trái và bên phải trong input.

Vai trò chính:

- Tạo representation giàu ngữ cảnh cho input.
- Giữ thông tin cần thiết để decoder sinh output.
- Phù hợp với phần "hiểu" trong các task sequence-to-sequence.

## Decoder làm gì?

Decoder sinh output từ trái sang phải. Khi đang sinh token tiếp theo, decoder chỉ được nhìn các token output đã sinh trước đó, nên nó dùng causal self-attention.

Vai trò chính:

- Dùng prefix đã sinh để quyết định token tiếp theo.
- Dùng cross-attention để nhìn encoder hidden states.
- Biến representation thành output sequence.

## Cross-attention

[[Cross-Attention]] là cầu nối giữa encoder và decoder. Trong cross-attention:

- Query đến từ decoder hidden states.
- Key và value đến từ encoder hidden states.

Cách hiểu:

```text
decoder hỏi: "Ở bước sinh hiện tại, tôi cần thông tin gì?"
encoder cung cấp: "Đây là các phần quan trọng của input."
cross-attention chọn phần input phù hợp để decoder dùng.
```

Nếu self-attention là token nhìn các token trong cùng sequence, thì cross-attention là decoder nhìn sang representation của input đã được encoder xử lý.

## So sánh ba nhóm Transformer

| Nhóm | Nhìn input thế nào | Sinh output thế nào | Model ví dụ | Task phù hợp |
| --- | --- | --- | --- | --- |
| Encoder-only | Đọc toàn bộ input hai chiều | Không sinh từng token | BERT, RoBERTa | Classification, NER, retrieval |
| Decoder-only | Nhìn prefix/quá khứ bằng causal mask | Sinh token tiếp theo | GPT | Chat, completion, text generation |
| Encoder-decoder | Encoder đọc input; decoder nhìn encoder qua cross-attention | Sinh output từng token | T5, BART | Translation, summarization, seq2seq |

## Công thức trực giác

Encoder đọc input:

$$
H = \text{Encoder}(x_1, ..., x_n)
$$

Decoder sinh output dựa trên prefix đã sinh và encoder output:

$$
p(y_t \mid y_{<t}, H)
$$

Nghĩa là token output hiện tại được dự đoán từ hai nguồn:

- Các token output trước đó $y_{<t}$.
- Representation của input $H$ từ encoder.

## Cần biết

- Encoder-decoder phù hợp với task biến đổi một sequence thành sequence khác.
- Encoder thường dùng bidirectional attention vì toàn bộ input có sẵn.
- Decoder dùng causal self-attention vì output được sinh từng bước.
- [[Cross-Attention]] giúp decoder "tham khảo" input đã được encoder đọc.
- T5, BART và nhiều model translation/summarization thuộc nhóm encoder-decoder.

## Khi áp dụng

- Dùng encoder-decoder cho translation, summarization, paraphrasing hoặc các task cần đọc input rồi sinh output mới.
- Dùng encoder-only khi chỉ cần hiểu input và chọn nhãn/embedding.
- Dùng decoder-only khi task chính là viết tiếp hoặc hội thoại dựa trên prefix.

## Câu hỏi review

1. Encoder và decoder chia việc như thế nào?
2. Vì sao encoder có thể dùng bidirectional attention?
3. Vì sao decoder cần causal self-attention?
4. Cross-attention khác self-attention ở đâu?
5. Khi nào nên chọn encoder-decoder thay vì decoder-only?

## Gợi ý trả lời câu hỏi review

1. Encoder đọc hiểu input; decoder sinh output dựa trên input đã được encoder biểu diễn và các token output đã sinh.
2. Vì encoder nhận toàn bộ input ngay từ đầu nên không cần che token tương lai trong input.
3. Vì decoder sinh output từng token, nếu nhìn token tương lai thì sẽ ăn gian next-token prediction.
4. Self-attention nhìn trong cùng sequence; cross-attention cho decoder nhìn sang encoder hidden states.
5. Khi task cần biến đổi input thành output mới có điều kiện rõ ràng, như translation hoặc summarization.

## Liên kết

- [[Transformer]]
- [[Decoder]]
- [[Cross-Attention]]
- [[Attention Mask]]
- [[Self-Attention]]
- [[Multi-Head Attention]]
- [[Bidirectional Attention]]
- [[NLP Transformers - Chapter 01 - Hello Transformers]]
- [[NLP Transformers - Chapter 03 - Transformer Anatomy]]
