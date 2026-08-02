---
type: concept
status: seed
sources:
  - "[[NLP Transformers - Chapter 03 - Transformer Anatomy]]"
tags:
  - concept
  - transformer
  - neural-network
  - training
---

# Layer Normalization

## Định nghĩa

Layer normalization là kỹ thuật chuẩn hóa activation trong một layer để tín hiệu có scale ổn định hơn trong quá trình training.

Với một vector activation $x$ của một token/example, LayerNorm chuẩn hóa theo các feature trong chính vector đó:

$$
\text{LayerNorm}(x) = \gamma \frac{x - \mu}{\sqrt{\sigma^2 + \epsilon}} + \beta
$$

Trong đó $\mu$ và $\sigma^2$ được tính trên các chiều feature của $x$, còn $\gamma$ và $\beta$ là tham số học được để model vẫn có thể điều chỉnh scale và shift sau khi chuẩn hóa.

## Cách hiểu bằng lời của tôi

Khi neural network càng sâu, output của các layer có thể thay đổi scale liên tục, làm training khó ổn định. Layer normalization giống như bước "cân lại" tín hiệu sau một phép biến đổi để các layer tiếp theo nhận input dễ học hơn.

## Trong Transformer

Trong encoder layer, các sublayers như multi-head self-attention và feed-forward layer thường đi cùng skip/residual connection và layer normalization.

Mental model:

```text
input
-> sublayer
-> cộng lại input gốc bằng skip connection
-> layer normalization
-> output
```

Tùy biến thể Transformer, thứ tự chính xác có thể khác nhau, ví dụ post-layer normalization hoặc pre-layer normalization, nhưng mục tiêu chung vẫn là giúp training sâu ổn định hơn.

### Post-LN và Pre-LN

Hai cách đặt LayerNorm hay gặp:

- **Post-LN**: chạy sublayer trước, cộng residual, rồi mới normalize.

```text
y = LayerNorm(x + Sublayer(x))
```

- **Pre-LN**: normalize trước khi đưa vào sublayer, rồi cộng residual sau.

```text
y = x + Sublayer(LayerNorm(x))
```

Post-LN gần với sơ đồ Transformer gốc và dễ đọc khi mới học. Pre-LN thường ổn định hơn khi train model rất sâu vì đường residual từ layer này sang layer sau ít bị biến đổi hơn.

## Cần biết

- Layer normalization khác batch normalization ở chỗ nó chuẩn hóa theo feature trong từng example/token, không phụ thuộc batch statistics.
- Trong NLP, điểm này quan trọng vì batch size, sequence length và padding có thể thay đổi; LayerNorm không cần batch lớn để có thống kê ổn định.
- Nó thường xuất hiện trong Transformer blocks.
- Nó giúp giảm bất ổn activation và hỗ trợ gradient flow.
- Nó thường đi cùng residual connections để train các mạng rất sâu.
- Trong nhiều LLM hiện đại, có thể gặp biến thể như RMSNorm. RMSNorm bỏ bước trừ mean và chỉ normalize theo root mean square, thường rẻ hơn một chút nhưng cùng mục tiêu: giữ scale activation ổn định.

## Khi áp dụng

- Khi đọc kiến trúc Transformer, đừng chỉ nhìn attention và feed-forward. Layer normalization là phần hạ tầng giúp stack nhiều layer hoạt động ổn định.
- Khi training bị không ổn định, normalization placement là một chi tiết kiến trúc đáng kiểm tra.
- Khi đọc paper hoặc model config, nên để ý model dùng LayerNorm, RMSNorm, Pre-LN hay Post-LN vì chi tiết này ảnh hưởng lớn tới độ ổn định khi scale model.

## Câu hỏi review

1. Layer normalization giải quyết vấn đề gì?
2. Vì sao Transformer cần layer normalization khi xếp nhiều layers?
3. Layer normalization thường đi cùng kỹ thuật nào trong Transformer block?
4. Layer normalization khác batch normalization ở điểm nào?
5. Pre-LN và Post-LN khác nhau ở đâu?

## Gợi ý trả lời câu hỏi review

1. Nó giúp scale activation ổn định hơn để model dễ train.
2. Transformer sâu có nhiều phép biến đổi liên tiếp; normalization giúp tín hiệu không bị lệch scale quá mạnh qua các layer.
3. Nó thường đi cùng skip/residual connections quanh self-attention và feed-forward sublayers.
4. LayerNorm chuẩn hóa theo feature trong từng example/token, còn BatchNorm dùng thống kê trên batch.
5. Post-LN normalize sau `x + Sublayer(x)`, còn Pre-LN normalize input trước sublayer rồi cộng residual sau.

## Liên kết

- [[Transformer]]
- [[Self-Attention]]
- [[Feed-Forward Layer]]
- [[Multi-Head Attention]]
- [[NLP Transformers - Chapter 03 - Transformer Anatomy]]
