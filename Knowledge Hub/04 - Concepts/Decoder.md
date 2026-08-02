---
type: concept
status: seed
sources:
  - "[[NLP Transformers - Chapter 03 - Transformer Anatomy]]"
tags:
  - concept
  - transformer
  - attention
  - generation
---

# Decoder

## Định nghĩa

Decoder là phần của Transformer dùng để sinh output sequence từng token một. Trong decoder-only models như GPT, toàn bộ model là một stack decoder blocks phục vụ next-token prediction.

## Cách hiểu bằng lời của tôi

Encoder giống một bộ đọc hiểu toàn bộ input. Decoder giống một bộ viết tiếp: nó nhìn những token đã có, tạo representation cho token hiện tại, rồi dự đoán token tiếp theo.

Điểm khác biệt lớn nhất là decoder không được nhìn token tương lai. Nếu đang sinh token thứ $t$, nó chỉ được dùng các token trước đó hoặc hiện có trong prefix.

Mental model:

```text
tokens đã có
-> masked/causal self-attention
-> feed-forward layer
-> logits cho token tiếp theo
-> chọn/sinh token mới
```

## Causal attention

Decoder dùng causal attention để tránh "ăn gian" token tương lai. [[Attention Mask]] che các vị trí phía sau token hiện tại.

Ví dụ sequence:

```text
I love natural language
```

Khi cập nhật token `love`, decoder chỉ được nhìn:

```text
I love
```

Nó không được nhìn `natural language` nếu các token đó nằm ở tương lai trong quá trình generation.

So sánh nhanh:

| Cơ chế | Token được nhìn | Phù hợp |
| --- | --- | --- |
| Bidirectional attention | Trái và phải | Understanding, classification, NER |
| Causal attention | Chỉ quá khứ/prefix | Generation, next-token prediction |

## Decoder block gồm gì?

Trong decoder-only model, mỗi decoder block thường có:

1. Masked multi-head self-attention.
2. Feed-forward/MLP layer.
3. Residual connections và layer normalization quanh các sublayers.

Trong encoder-decoder model, decoder còn có thêm [[Cross-Attention|cross-attention]] để nhìn output của encoder:

```text
decoder self-attention: nhìn các token output đã sinh
cross-attention: nhìn representation từ encoder
feed-forward: xử lý representation từng token
```

## Công thức trực giác

Với next-token prediction:

$$
p(x_t \mid x_{<t})
$$

Nghĩa là model dự đoán token hiện tại hoặc token tiếp theo dựa trên các token trước đó, không dựa vào tương lai.

Sau decoder stack, model tạo logits trên vocabulary:

```text
decoder hidden state
-> language modeling head
-> logits over vocabulary
-> next token
```

## Cần biết

- Decoder-only models như GPT dùng causal/autoregressive attention.
- Decoder phù hợp với text generation vì nó sinh token theo thứ tự từ trái sang phải.
- Causal mask là điểm làm decoder khác encoder trong generation.
- Causal mask thường là một mask matrix dạng tam giác dưới, quy định token hiện tại chỉ được nhìn chính nó và prefix trước nó.
- Trong encoder-decoder models, decoder vừa dùng causal self-attention vừa dùng [[Cross-Attention|cross-attention]] sang encoder output.
- Decoder không chỉ "copy token trước"; nó tạo representation ngữ cảnh từ prefix rồi dự đoán phân phối token tiếp theo.

## Khi áp dụng

- Dùng decoder-only model khi task chính là sinh tiếp văn bản, chat, completion hoặc code generation.
- Dùng encoder-only model khi cần hiểu toàn bộ input để phân loại hoặc trích xuất thông tin.
- Dùng encoder-decoder model khi cần đọc một input rồi sinh một output khác, ví dụ translation hoặc summarization.

## Câu hỏi review

1. Decoder khác encoder ở điểm nào quan trọng nhất?
2. Vì sao decoder cần causal attention?
3. Decoder-only model phù hợp với task nào?
4. Trong encoder-decoder model, cross-attention giúp decoder làm gì?
5. Vì sao next-token prediction có dạng $p(x_t \mid x_{<t})$?

## Gợi ý trả lời câu hỏi review

1. Encoder có thể nhìn toàn bộ input; decoder khi generation chỉ được nhìn các token trước đó.
2. Vì nếu nhìn token tương lai, model sẽ "ăn gian" mục tiêu dự đoán token tiếp theo.
3. Text generation, chat, completion, code generation hoặc các task cần sinh chuỗi từng bước.
4. Nó cho decoder nhìn representation của input đã được encoder đọc hiểu.
5. Vì token hiện tại/tiếp theo phải được dự đoán từ prefix đã có, không từ phần tương lai.

## Liên kết

- [[Transformer]]
- [[Self-Attention]]
- [[Multi-Head Attention]]
- [[Cross-Attention]]
- [[Attention Mask]]
- [[Feed-Forward Layer]]
- [[Bidirectional Attention]]
- [[Encoder-Decoder Architecture]]
- [[NLP Transformers - Chapter 03 - Transformer Anatomy]]
