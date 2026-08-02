---
type: concept
status: seed
sources:
  - "[[NLP Transformers - Chapter 03 - Transformer Anatomy]]"
  - "[[Encoder-Decoder Architecture]]"
tags:
  - concept
  - transformer
  - attention
  - seq2seq
---

# Cross-Attention

## Định nghĩa

Cross-attention là attention giữa hai sequence khác nhau. Trong encoder-decoder Transformer, decoder dùng cross-attention để nhìn sang encoder hidden states của input.

## Cách hiểu bằng lời của tôi

Self-attention là token nhìn các token trong cùng một sequence. Cross-attention là decoder đang sinh output nhìn sang input đã được encoder đọc hiểu.

Ví dụ dịch máy:

```text
Input:  I love NLP
Output: Tôi yêu NLP
```

Encoder đọc câu tiếng Anh và tạo hidden states. Khi decoder đang sinh từ `Tôi`, `yêu`, `NLP`, nó dùng cross-attention để hỏi: "Phần nào của câu input đang liên quan tới token output hiện tại?"

Mental model:

```text
encoder hidden states: thông tin từ input
decoder hidden state: trạng thái đang sinh output
cross-attention: decoder chọn phần input cần nhìn
```

## Query, key, value đến từ đâu?

Điểm quan trọng nhất:

- **Query** đến từ decoder hidden states.
- **Key** đến từ encoder hidden states.
- **Value** đến từ encoder hidden states.

Công thức trực giác:

$$
\text{CrossAttention}(Q_{\text{dec}}, K_{\text{enc}}, V_{\text{enc}})
$$

Nghĩa là decoder đặt câu hỏi bằng query của nó, còn encoder cung cấp key/value như bộ nhớ về input.

## So sánh với self-attention

| Loại attention | Query từ đâu | Key/Value từ đâu | Ý nghĩa |
| --- | --- | --- | --- |
| Self-attention | Cùng sequence | Cùng sequence | Token nhìn các token cùng câu/sequence |
| Causal self-attention | Decoder output prefix | Decoder output prefix | Decoder nhìn các token đã sinh |
| Cross-attention | Decoder | Encoder | Decoder nhìn input đã được encoder đọc |

## Ví dụ trực quan

Khi summarization một bài báo, encoder đọc toàn bộ bài báo. Decoder đang sinh câu tóm tắt. Ở mỗi bước sinh, decoder có thể cross-attend tới các phần quan trọng của bài báo.

```text
article -> encoder -> hidden states
summary prefix -> decoder self-attention
decoder state -> cross-attention vào article hidden states
-> token tóm tắt tiếp theo
```

Nếu không có cross-attention, decoder chỉ biết các token output đã sinh, nhưng thiếu kênh trực tiếp để tham khảo input.

## Cần biết

- Cross-attention thường xuất hiện trong encoder-decoder models như T5, BART và các model translation/summarization.
- Nó là cầu nối giữa phần "đọc input" và phần "sinh output".
- Decoder vẫn cần causal self-attention để không nhìn token output tương lai.
- Cross-attention không che tương lai của input, vì encoder input đã có sẵn toàn bộ.
- Trong cross-attention, attention weights có thể được hiểu là decoder đang tập trung vào phần nào của input.

## Khi áp dụng

- Dùng để hiểu vì sao encoder-decoder hợp với translation, summarization và seq2seq.
- Khi model sinh output không bám input, cross-attention hoặc encoder representation là nơi đáng kiểm tra.
- Khi đọc architecture, phân biệt rõ decoder self-attention và cross-attention: một cái nhìn output prefix, một cái nhìn encoder input.

## Câu hỏi review

1. Cross-attention khác self-attention ở đâu?
2. Trong encoder-decoder Transformer, query/key/value của cross-attention đến từ đâu?
3. Vì sao decoder cần cross-attention trong translation hoặc summarization?
4. Cross-attention có cần causal mask như decoder self-attention không?
5. Nếu bỏ cross-attention khỏi encoder-decoder model thì decoder mất gì?

## Gợi ý trả lời câu hỏi review

1. Self-attention nhìn trong cùng sequence; cross-attention cho decoder nhìn sang encoder hidden states của input.
2. Query đến từ decoder; key và value đến từ encoder.
3. Vì decoder cần tham khảo input đã được encoder đọc để sinh output đúng với input.
4. Không theo cùng nghĩa causal mask, vì encoder input đã có sẵn toàn bộ; decoder self-attention mới cần che token output tương lai.
5. Decoder mất kênh trực tiếp để dùng thông tin từ input, nên khó làm các task biến đổi input thành output.

## Liên kết

- [[Encoder-Decoder Architecture]]
- [[Decoder]]
- [[Self-Attention]]
- [[Multi-Head Attention]]
- [[Attention Mask]]
- [[NLP Transformers - Chapter 03 - Transformer Anatomy]]
