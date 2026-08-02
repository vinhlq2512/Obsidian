---
type: concept
status: seed
sources:
  - "[[NLP Transformers - Chapter 03 - Transformer Anatomy]]"
tags:
  - concept
  - transformer
  - attention
  - nlp
---

# Attention Mask

## Định nghĩa

Attention mask là ma trận hoặc tensor cho model biết token nào được phép chú ý tới token nào trong attention. Trong decoder, causal mask là attention mask dùng để che token tương lai.

## Cách hiểu bằng lời của tôi

Self-attention tạo một ma trận attention scores, trong đó mỗi hàng là token đang hỏi, mỗi cột là token có thể được nhìn. Mask matrix giống như một bộ luật đặt lên ma trận này: ô nào được nhìn thì giữ lại, ô nào không được nhìn thì che đi trước softmax.

Mental model:

```text
attention scores
-> cộng mask
-> softmax
-> attention weights
```

Các vị trí bị mask thường được cộng một số rất âm, ví dụ `-inf` hoặc `-1e9`, để sau softmax trọng số gần như bằng 0.

## Causal mask trong decoder

Với decoder sinh từ trái sang phải, token hiện tại chỉ được nhìn chính nó và các token trước đó. Nếu sequence có 4 token:

```text
t1 t2 t3 t4
```

Causal mask có thể hình dung như ma trận tam giác dưới:

```text
      key:  t1  t2  t3  t4
query
t1         1   0   0   0
t2         1   1   0   0
t3         1   1   1   0
t4         1   1   1   1
```

Trong đó:

- `1` nghĩa là được chú ý.
- `0` nghĩa là bị che/mask.

Ví dụ hàng `t2` là token `t2` đang query. Nó được nhìn `t1` và `t2`, nhưng không được nhìn `t3`, `t4` vì đó là tương lai.

## Dạng cộng vào attention scores

Trong code thực tế, mask thường được cộng vào attention scores trước softmax:

```text
scores = QK^T / sqrt(d_k)
masked_scores = scores + mask
weights = softmax(masked_scores)
```

Causal mask dạng số có thể là:

```text
      t1    t2    t3    t4
t1     0  -inf  -inf  -inf
t2     0     0  -inf  -inf
t3     0     0     0  -inf
t4     0     0     0     0
```

Các ô `-inf` sau softmax sẽ có attention weight gần 0.

## Padding mask và causal mask

Không phải mask nào cũng để che tương lai:

- **Padding mask**: che các token `[PAD]` để model không chú ý vào phần padding giả.
- **Causal mask**: che token tương lai để decoder không nhìn trước khi sinh token tiếp theo.
- **Combined mask**: trong decoder training, có thể cần cả causal mask và padding mask cùng lúc.

## Cần biết

- Attention mask không tạo representation mới; nó chỉ giới hạn token nào được phép tương tác trong attention.
- Encoder thường dùng padding mask, nhưng không cần causal mask nếu được phép nhìn toàn bộ input.
- Decoder dùng causal mask để phục vụ autoregressive/next-token prediction.
- Mask được áp dụng trước softmax, vì softmax là bước biến scores thành attention weights.
- Nếu mask sai, model có thể học sai: nhìn vào padding hoặc ăn gian token tương lai.

## Khi áp dụng

- Khi debug decoder generation, kiểm tra causal mask nếu model nhìn được token tương lai hoặc loss bất thường.
- Khi batch có padding, kiểm tra padding mask để tránh model chú ý vào `[PAD]`.
- Khi đọc attention matrix, nhớ phân biệt ô bị mask và ô có attention thấp tự nhiên.

## Câu hỏi review

1. Attention mask làm gì trong self-attention?
2. Vì sao causal mask có dạng tam giác dưới?
3. Vì sao mask được áp dụng trước softmax?
4. Padding mask khác causal mask ở đâu?
5. Nếu decoder không dùng causal mask thì chuyện gì xảy ra?

## Gợi ý trả lời câu hỏi review

1. Nó quy định token nào được phép chú ý tới token nào.
2. Vì token ở vị trí hiện tại chỉ được nhìn các token trước nó và chính nó, không được nhìn tương lai.
3. Vì các ô bị mask cần bị đẩy về trọng số gần 0 sau softmax.
4. Padding mask che token giả `[PAD]`; causal mask che token tương lai.
5. Model có thể nhìn trước đáp án trong training, làm sai mục tiêu next-token prediction.

## Liên kết

- [[Self-Attention]]
- [[Multi-Head Attention]]
- [[Decoder]]
- [[Bidirectional Attention]]
- [[NLP Transformers - Chapter 03 - Transformer Anatomy]]
