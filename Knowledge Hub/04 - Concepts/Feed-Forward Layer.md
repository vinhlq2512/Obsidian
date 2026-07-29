---
type: concept
status: seed
source:
  - "[[NLP Transformers - Chapter 03 - Transformer Anatomy]]"
tags:
  - concept
  - transformer
  - neural-network
  - nlp
---

# Feed-Forward Layer

## Định nghĩa

Feed-forward layer trong Transformer là một fully connected neural network nhỏ được áp dụng độc lập lên từng token embedding sau self-attention.

## Cách hiểu bằng lời của tôi

Trong encoder layer, self-attention cho các token trao đổi thông tin với nhau. Sau đó feed-forward layer xử lý representation của từng token riêng biệt, giống như một bước "suy nghĩ thêm" trên từng token sau khi token đã nhận context.

Attention trả lời: token này nên lấy thông tin từ token nào?

Feed-forward trả lời: sau khi đã có thông tin đó, representation của token này nên được biến đổi ra sao?

## Công thức trực giác

Feed-forward layer trong Transformer thường có dạng:

$$
\text{FFN}(x) = W_2\sigma(W_1x + b_1) + b_2
$$

Cách đọc:

- $x$ là representation của một token sau attention.
- $W_1$ mở rộng hidden representation sang một intermediate dimension lớn hơn.
- $\sigma$ là activation function, thường là GELU hoặc ReLU.
- $W_2$ chiếu representation về lại hidden size ban đầu.

Ví dụ shape:

```text
token representation: 768 chiều
-> linear layer: 3072 chiều
-> activation
-> linear layer: 768 chiều
```

Điểm cần nhớ: input và output có cùng hidden size để nhiều Transformer blocks có thể xếp chồng lên nhau.

## Vì sao cần feed-forward layer?

Self-attention chủ yếu trộn thông tin giữa token bằng weighted sum của value vectors. Nhưng nếu chỉ trộn tuyến tính như vậy, model thiếu khả năng biến đổi representation theo cách phức tạp. Feed-forward layer thêm năng lực phi tuyến cho từng token sau khi token đã nhận context.

Nói ngắn:

- Attention quyết định token nên lấy thông tin từ đâu.
- Feed-forward quyết định biến đổi representation đã có context như thế nào.
- Residual connection và layer normalization giúp bước biến đổi này ổn định khi xếp nhiều layer.

## Ví dụ trực quan

Giả sử token `flies` trong câu `"time flies like an arrow"` đã nhận context từ attention. Sau attention, representation của `flies` đã chứa tín hiệu từ `time` và `arrow`, nên nó nghiêng về nghĩa động từ.

Feed-forward layer không đi tìm thêm token khác. Nó nhận vector đã có context đó và biến đổi tiếp:

```text
flies sau attention
-> MLP position-wise
-> flies phiên bản đã được xử lý sâu hơn
```

Có thể hiểu đây là bước "diễn giải lại" representation: attention đưa nguyên liệu ngữ cảnh vào, feed-forward nấu representation đó thành dạng hữu ích hơn cho layer tiếp theo hoặc task downstream.

## Cần biết

- Feed-forward layer còn được gọi là position-wise feed-forward layer vì cùng một mạng được áp dụng cho từng vị trí/token.
- Nó thường gồm hai linear layers với một activation ở giữa.
- Nó không tự trộn thông tin giữa các token; việc trộn thông tin nằm ở self-attention.
- Input và output thường giữ cùng hidden size để encoder layer có thể xếp chồng nhiều lần.
- Trong Transformer block thực tế, feed-forward layer đi cùng residual connection và layer normalization.
- Feed-forward/MLP thường chiếm nhiều tham số và compute trong Transformer, nên đây là thành phần quan trọng khi tối ưu model.

## Trong encoder layer

```text
sequence embeddings
-> multi-head self-attention
-> feed-forward layer
-> contextualized embeddings
```

Self-attention tạo representation có ngữ cảnh; feed-forward layer tăng năng lực biến đổi phi tuyến cho từng representation đó.

## Khi áp dụng

- Khi đọc Transformer, đừng nghĩ encoder layer chỉ có attention. Attention là phần trộn thông tin, còn feed-forward layer là phần xử lý representation.
- Khi debug hoặc tối ưu Transformer, feed-forward/MLP thường chiếm nhiều tham số và compute đáng kể.

## Câu hỏi review

1. Feed-forward layer trong Transformer làm gì?
2. Vì sao gọi là position-wise feed-forward layer?
3. Feed-forward layer khác self-attention ở đâu?

## Gợi ý trả lời câu hỏi review

1. Nó biến đổi từng token representation sau self-attention bằng một mạng fully connected.
2. Vì cùng một mạng được áp dụng độc lập cho từng vị trí/token trong sequence.
3. Self-attention trộn thông tin giữa token; feed-forward layer xử lý từng token riêng biệt.

## Liên kết

- [[Self-Attention]]
- [[Multi-Head Attention]]
- [[Transformer]]
- [[NLP Transformers - Chapter 03 - Transformer Anatomy]]
