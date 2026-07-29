---
type: reading-section
book: "[[Natural Language Processing with Transformers]]"
status: completed
chapter: 3
start_page: 78
end_page: 118
reading_date: 2026-07-26
planned_sessions:
  - "2026-07-26 | 78-98 | Self-attention, embedding vị trí và intuition | 55 phút"
  - "2026-07-27 | 99-118 | Encoder, decoder, encoder-decoder và tóm tắt bằng lời của tôi | 55 phút"
estimated_minutes: 90
actual_minutes:
need_review: false
tags:
  - nlp
  - transformer
  - attention
---

# NLP Transformers - Chapter 03 - Transformer Anatomy

## Mục tiêu đọc

- Hiểu cấu trúc bên trong Transformer.
- Nắm self-attention, feed-forward layer, layer normalization, positional embeddings.
- Phân biệt encoder, decoder và encoder-decoder models.

## Ý chính

- Transformer gốc được thiết kế cho sequence-to-sequence tasks như machine translation, nhưng encoder block và decoder block nhanh chóng được dùng riêng thành các model độc lập.
- Mỗi encoder layer nhận một sequence embeddings và xử lý qua hai sublayers chính: multi-head self-attention và position-wise feed-forward layer.
- Mỗi sublayer trong encoder thường được bọc bởi skip/residual connection và layer normalization để train mạng sâu ổn định hơn.
- Self-attention cho phép mỗi token nhìn vào các token khác trong cùng sequence.
- [[Bidirectional Attention]] là đặc trưng của encoder-only models như BERT/DistilBERT: token được contextualize bằng cả ngữ cảnh bên trái và bên phải.
- [[Decoder|Decoder-only models]] như GPT dùng causal/autoregressive attention: token hiện tại chỉ được nhìn các token trước nó để phục vụ next-token prediction.
- Positional embeddings bổ sung thông tin thứ tự vì attention không tự biết vị trí.
- Các nhánh model khác nhau phù hợp task khác nhau: encoder cho understanding, decoder cho generation, encoder-decoder cho seq2seq.

## Định nghĩa quan trọng

- **Self-attention**: cơ chế để mỗi token tính trọng số chú ý với các token khác trong cùng sequence và tạo representation mới từ tổng có trọng số của các value vectors.
- **Bidirectional attention**: self-attention trong đó token có thể dùng cả context bên trái và context bên phải. Đây là lý do encoder-only models rất mạnh cho language understanding.
- **Causal attention**: self-attention có mask để token chỉ nhìn các token trước nó. Đây là cơ chế phù hợp với decoder-only generation.
- **Attention mask**: ma trận/mask quy định token nào được phép chú ý tới token nào.
- **Encoder-only model**: Transformer chỉ dùng encoder stack, phù hợp để hiểu input và tạo representation.
- **[[Decoder|Decoder-only model]]**: Transformer chỉ dùng decoder stack, phù hợp để sinh văn bản theo next-token prediction.
- **Encoder-decoder model**: Transformer dùng cả encoder và decoder, phù hợp cho bài toán biến đổi một sequence thành sequence khác.
- **[[Multi-Head Attention|Multi-head self-attention layer]]**: sublayer cho mỗi token nhìn nhiều kiểu quan hệ khác nhau với các token còn lại trong sequence.
- **Position-wise feed-forward layer**: MLP được áp dụng độc lập lên từng token embedding sau attention.
- **Skip/residual connection**: cộng input của sublayer vào output của sublayer để giữ đường truyền thông tin và gradient.
- **Layer normalization**: chuẩn hóa activation trong layer để training ổn định hơn.

## Ba nhóm Transformer chính

Transformer ban đầu được tạo ra cho sequence-to-sequence tasks như machine translation. Trong setup gốc, encoder đọc input sequence và decoder sinh output sequence. Sau đó, hai khối này được tái sử dụng độc lập, tạo thành ba nhóm model lớn:

- **Encoder-only**: chỉ dùng encoder. Representation của token phụ thuộc cả context trái và phải, nên hợp với language understanding. Ví dụ: BERT, RoBERTa, DistilBERT.
- **Decoder-only**: chỉ dùng decoder. Model sinh từng token từ trái sang phải và dùng causal attention để không nhìn token tương lai. Ví dụ: GPT family.
- **Encoder-decoder**: dùng encoder để hiểu input và decoder để sinh output. Hợp với task cần ánh xạ một chuỗi sang chuỗi khác. Ví dụ: T5, BART.

Mental model:

```text
Encoder-only     -> đọc hiểu input
Decoder-only     -> viết tiếp output
Encoder-decoder  -> đọc input rồi sinh output mới
```

Khi chọn model, câu hỏi đầu tiên nên là: task của mình cần hiểu, sinh, hay chuyển đổi chuỗi?

## Encoder Layer

Mỗi encoder layer nhận vào một sequence embeddings và đưa chúng qua hai sublayers chính:

1. [[Multi-Head Attention|Multi-head self-attention layer]].
2. Fully connected feed-forward layer áp dụng lên từng input embedding.

Cách hiểu:

- Multi-head self-attention là bước trộn thông tin giữa các token. Mỗi token hỏi: "Trong sequence này, token nào liên quan tới mình và liên quan theo kiểu gì?"
- [[Feed-Forward Layer|Feed-forward layer]] là bước xử lý riêng từng token sau khi token đã nhận context từ attention. Nó giúp biến đổi representation theo cách phi tuyến tính và tăng năng lực biểu diễn của model.
- Vì feed-forward layer xử lý từng vị trí độc lập, nó không tạo luồng thông tin giữa các token. Luồng thông tin giữa token chủ yếu đến từ self-attention.
- Trong Transformer thực tế, hai sublayers này thường đi cùng residual/skip connections và layer normalization để training sâu ổn định hơn.

### Skip connections và layer normalization

Mỗi sublayer trong encoder thường không chỉ nhận input rồi trả output trực tiếp. Nó được bọc bằng hai kỹ thuật quan trọng:

- **Skip/residual connection**: cộng input ban đầu vào output của sublayer. Nếu sublayer học một phép biến đổi chưa tốt, model vẫn giữ được đường đi gần như identity để thông tin không bị phá hỏng quá mạnh.
- **Layer normalization**: chuẩn hóa activation để scale của tín hiệu ổn định hơn qua nhiều layer.

Cách hiểu:

```text
input
-> sublayer
-> cộng lại với input ban đầu
-> layer normalization
-> output ổn định hơn
```

Điểm cần nhớ: self-attention và feed-forward layer tạo năng lực biểu diễn, còn skip connections và layer normalization làm cho việc train nhiều layer sâu trở nên thực tế hơn.

Mental model:

```text
sequence embeddings
-> multi-head self-attention: token trao đổi thông tin với nhau
-> feed-forward layer: từng token tự xử lý representation mới
-> output embeddings cùng shape với input
```

## Bidirectional Attention

Bidirectional attention xuất hiện trong phần phân loại các kiến trúc Transformer. Encoder-only models như BERT, RoBERTa và DistilBERT tạo representation cho mỗi token bằng cách dùng cả token đứng trước và token đứng sau trong input sequence.

Điểm quan trọng:

- Vì encoder nhận toàn bộ input ngay từ đầu, nó không cần che token tương lai.
- Mỗi token có thể được contextualize bằng toàn câu.
- Điều này giúp các task understanding vì ý nghĩa của token thường phụ thuộc cả hai phía.
- Ví dụ `flies` có thể là danh từ hoặc động từ; các token xung quanh như `time`, `arrow`, `fruit`, `banana` giúp model phân biệt nghĩa.
- Trong BERT-style models, `[CLS]` cũng nhận thông tin hai chiều từ toàn sequence, nên thường được dùng cho [[Classification Head|classification head]].

So sánh nhanh:

| Cơ chế | Token được nhìn | Kiến trúc thường gặp | Task phù hợp |
| --- | --- | --- | --- |
| Bidirectional attention | Cả trái và phải | Encoder-only, BERT, DistilBERT | Classification, NER, semantic understanding |
| Causal attention | Chỉ token trước đó | Decoder-only, GPT | Text generation, next-token prediction |
| Cross-attention | Decoder nhìn output encoder | Encoder-decoder, T5, BART | Translation, summarization, seq2seq |

## Self-Attention như weighted average

Ý tưởng chính của self-attention là không dùng một embedding cố định cho mỗi token. Thay vào đó, representation mới của mỗi token được tính bằng cách nhìn toàn bộ sequence và lấy một weighted average của các token embeddings.

Nếu input là sequence embeddings $x_1, ..., x_n$, self-attention tạo ra sequence mới $x'_1, ..., x'_n$, trong đó:

$$
x'_i = \sum_{j=1}^{n} w_{ji}x_j
$$

Các hệ số $w_{ji}$ là attention weights. Chúng được chuẩn hóa để:

$$
\sum_j w_{ji} = 1
$$

Cách hiểu:

- $x_i$ là embedding ban đầu của token thứ $i$.
- $x'_i$ là embedding mới của token thứ $i$ sau khi đã dùng context.
- $w_{ji}$ cho biết token $j$ quan trọng bao nhiêu khi cập nhật representation cho token $i$.
- Vì các weights cộng lại bằng 1, có thể xem self-attention như weighted average, nhưng các trọng số được học theo context chứ không cố định.

Ví dụ, token `flies` khi đứng riêng có thể gợi nghĩa "con ruồi". Nhưng trong câu `"time flies like an arrow"`, các token như `time` và `arrow` nên có trọng số cao hơn để representation của `flies` nghiêng về nghĩa động từ "bay/trôi qua". Embedding mới này gọi là **contextualized embedding**.

Điểm cần nhớ: self-attention không chỉ tìm token giống nhau; nó tạo representation mới bằng cách trộn thông tin từ những token hữu ích nhất trong toàn sequence.

## Multi-Head Attention

Multi-head attention là cách Transformer chạy nhiều self-attention heads song song thay vì chỉ dùng một attention head duy nhất. Mỗi head có bộ projection query/key/value riêng, nên mỗi head có thể học một kiểu quan hệ khác nhau giữa các token.

Mental model:

```text
input embeddings
-> head 1: nhìn một kiểu quan hệ
-> head 2: nhìn một kiểu quan hệ khác
-> ...
-> concat các head
-> linear projection cuối
-> output embedding
```

### Vì sao cần nhiều heads?

Một câu có nhiều loại quan hệ cùng tồn tại: quan hệ cú pháp, quan hệ ngữ nghĩa, quan hệ đại từ - thực thể, quan hệ local context, keyword cho task downstream. Nếu chỉ có một head, token hiện tại chỉ có một attention distribution chính. Với nhiều heads, cùng một token có thể có nhiều attention distributions song song.

Ví dụ với câu:

```text
The cat sat on the mat because it was tired
```

Khi cập nhật token `it`, các head có thể học các góc nhìn khác nhau:

| Head | Có thể chú ý mạnh tới | Ý nghĩa |
| --- | --- | --- |
| Head 1 | `cat` | Tìm thực thể mà `it` tham chiếu |
| Head 2 | `tired` | Nắm trạng thái liên quan tới `it` |
| Head 3 | `because` | Nhận biết quan hệ nguyên nhân |
| Head 4 | token gần `it` | Giữ local context |

Các pattern này là ví dụ trực giác. Trong model thật, không phải head nào cũng diễn giải được rõ ràng bằng ngôn ngữ người, nhưng ý tưởng chính vẫn là: nhiều heads giúp model học nhiều kiểu quan hệ cùng lúc.

### Công thức trực giác

Với mỗi head $h$, model tạo query/key/value riêng:

$$
Q_h = XW_h^Q,\quad K_h = XW_h^K,\quad V_h = XW_h^V
$$

Mỗi head chạy attention riêng:

$$
\text{head}_h = \text{Attention}(Q_h, K_h, V_h)
$$

Sau đó concat các head và project về output:

$$
\text{MultiHead}(X) = \text{Concat}(\text{head}_1, ..., \text{head}_m)W^O
$$

Nếu hidden size là $d_{\text{model}} = 768$ và có 12 heads, mỗi head thường làm việc trên 64 chiều. Sau khi 12 heads chạy xong, outputs được nối lại thành 768 chiều rồi đưa qua projection $W^O$.

Điểm cần nhớ: multi-head attention không chỉ là "attention lớn hơn". Nó là nhiều attention heads nhỏ hơn, mỗi head học một attention pattern riêng, sau đó model trộn các góc nhìn này lại.

## The Feed-Forward Layer

Sau multi-head attention, mỗi token embedding đã chứa thông tin ngữ cảnh từ các token khác. Feed-forward layer nhận từng embedding đó và biến đổi nó bằng một mạng fully connected nhỏ. Trong Transformer, layer này thường được gọi là **position-wise feed-forward layer** vì cùng một mạng được áp dụng độc lập cho từng vị trí trong sequence.

Công thức thường gặp:

$$
\text{FFN}(x) = W_2\sigma(W_1x + b_1) + b_2
$$

Cách đọc:

- $x$ là representation của một token sau attention.
- $W_1$ chiếu $x$ sang một intermediate dimension lớn hơn.
- $\sigma$ là activation function, thường là GELU hoặc ReLU, để thêm phi tuyến.
- $W_2$ chiếu representation về lại hidden size ban đầu.

Ví dụ shape:

```text
hidden size 768
-> linear layer mở rộng lên 3072
-> activation
-> linear layer nén về 768
```

Điểm quan trọng là feed-forward layer xử lý từng token riêng biệt. Nếu sequence có 10 token, cùng một FFN được áp dụng 10 lần, một lần cho mỗi token representation. Nó không trực tiếp tính attention giữa token này và token khác.

So sánh với attention:

| Thành phần | Vai trò | Có trộn thông tin giữa token không? |
| --- | --- | --- |
| Multi-head self-attention | Chọn và trộn context từ các token khác | Có |
| Feed-forward layer | Biến đổi representation của từng token bằng MLP | Không trực tiếp |

Mental model: attention là bước "token nên nghe ai?", feed-forward là bước "sau khi nghe xong, token nên tự cập nhật representation ra sao?"

Vì feed-forward layer có hai linear layers lớn, nó thường chiếm nhiều tham số và compute đáng kể trong Transformer. Đây là lý do trong nhiều LLM hiện đại, phần MLP/feed-forward là một trong các nơi quan trọng để tối ưu kiến trúc.

## Cách tính attention weights

Sau khi hiểu self-attention như weighted average, câu hỏi tiếp theo là: các trọng số $w_{ji}$ đến từ đâu?

Transformer dùng scaled dot-product attention. Quy trình có bốn bước chính:

1. Project mỗi token embedding thành ba vector: query, key và value.
2. Tính attention scores bằng dot product giữa query và key.
3. Tính attention weights bằng scaling và softmax.
4. Update token embeddings bằng cách nhân attention weights với value vectors.

Công thức:

$$
\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V
$$

Cách hiểu query/key/value:

- **Query**: token hiện tại đang "hỏi" hoặc tìm loại thông tin nào.
- **Key**: mỗi token khác cung cấp tín hiệu để được match với query.
- **Value**: nội dung thật sự được trộn vào output nếu token đó được chú ý.

Dot product giữa query và key càng lớn thì token đó càng liên quan trong ngữ cảnh hiện tại. Softmax biến các scores thành phân phối trọng số, nên mỗi token nhận được một mức đóng góp khác nhau vào representation mới.

Lý do cần scale: nếu dot product quá lớn, softmax có thể trở nên quá sắc, gần như chọn một token duy nhất và làm gradient kém ổn định. Chia cho $\sqrt{d_k}$ giúp scores có scale ổn hơn khi chiều vector lớn.

### Chi tiết bốn bước

1. **Project token embeddings thành Q/K/V**
   - Mỗi token embedding được đưa qua ba linear projections để tạo query, key và value.
   - Query dùng để hỏi "tôi cần thông tin gì?"
   - Key dùng để trả lời "tôi có khớp với query này không?"
   - Value là nội dung sẽ được trộn vào output nếu token đó được chú ý.

2. **Compute attention scores**
   - Attention score đo độ khớp giữa query và key bằng dot product.
   - Với sequence có $n$ tokens, ta nhận được một ma trận attention scores kích thước $n \times n$.
   - Entry trong ma trận cho biết một token đang chú ý tới token khác mạnh hay yếu.
   - Query và key càng giống nhau thì dot product càng lớn; nếu không liên quan thì dot product nhỏ.

3. **Compute attention weights**
   - Dot products có thể rất lớn, nên scores được scale bằng $\sqrt{d_k}$.
   - Sau đó softmax biến scores thành attention weights $w_{ji}$.
   - Các weights được chuẩn hóa để tổng bằng 1, nên có thể xem chúng như mức phân bổ chú ý của token hiện tại lên toàn sequence.
   - Kết quả vẫn là một ma trận $n \times n$, nhưng lúc này các giá trị đã là trọng số attention.

4. **Update token embeddings**
   - Sau khi có attention weights, model nhân chúng với value vectors $v_1, ..., v_n$.
   - Representation mới của token $i$ là:

$$
x'_i = \sum_j w_{ji}v_j
$$

   - Nghĩa là output của token hiện tại là tổng có trọng số của nội dung/value từ các token mà nó chú ý tới.

### Ví dụ trực quan

Giả sử sequence rút gọn chỉ có 3 token:

```text
time | flies | arrow
```

Ta muốn cập nhật representation cho token `flies`.

1. **Project thành Q/K/V**
   - `flies` có query riêng: "Tôi cần context nào để hiểu nghĩa của mình?"
   - `time`, `flies`, `arrow` đều có key riêng: "Tôi có tín hiệu gì để được chú ý?"
   - Cả ba token đều có value riêng: "Nếu được chú ý, tôi đóng góp nội dung gì?"

2. **Tính attention scores**
   - Query của `flies` được dot product với key của `time`, `flies`, `arrow`.
   - Nếu score với `time` và `arrow` cao, model đang nhận ra hai token này giúp giải nghĩa `flies`.

3. **Softmax thành attention weights**
   - Ví dụ sau scaling và softmax, weights cho output của `flies` có thể là:

| Token đóng góp value | Attention weight |
| --- | ---: |
| `time` | 0.45 |
| `flies` | 0.10 |
| `arrow` | 0.45 |

4. **Update embedding**

$$
x'_{\text{flies}} = 0.45v_{\text{time}} + 0.10v_{\text{flies}} + 0.45v_{\text{arrow}}
$$

Các số này chỉ là ví dụ để hình dung. Điều quan trọng là `flies` không được biểu diễn bằng embedding cố định nữa. Representation mới của nó đã "mượn" nhiều thông tin từ `time` và `arrow`, nên trong câu `"time flies like an arrow"` nó dễ nghiêng về nghĩa động từ hơn là nghĩa côn trùng.

Mental model: attention scores quyết định token nào liên quan; softmax biến liên quan đó thành tỷ lệ đóng góp; value vectors là phần nội dung thật sự được trộn vào output.

## Demo thực hành

Mô phỏng scaled dot-product attention bằng PyTorch.

```python
import torch
import torch.nn.functional as F

torch.manual_seed(42)

tokens = torch.randn(1, 4, 8)
query = torch.nn.Linear(8, 8)(tokens)
key = torch.nn.Linear(8, 8)(tokens)
value = torch.nn.Linear(8, 8)(tokens)

scores = query @ key.transpose(-2, -1) / (8 ** 0.5)
weights = F.softmax(scores, dim=-1)
context = weights @ value

print("attention weights:", weights.round(decimals=3))
print("context shape:", context.shape)
```

## Khái niệm quan trọng

- [[Self-Attention]]
- [[Multi-Head Attention]]
- [[Bidirectional Attention]]
- [[Feed-Forward Layer]]
- [[Layer Normalization]]
- [[Positional Embeddings]]
- [[Decoder]]
- [[Encoder-Decoder Architecture]]

## Active Recall

1. Self-attention tạo representation mới cho token như thế nào?
2. Vì sao phải scale dot product trước softmax?
3. Positional embeddings giải quyết thiếu sót gì?
4. Khi nào nên dùng encoder-only, decoder-only, encoder-decoder?
5. Bidirectional attention khác causal attention ở điểm nào?
6. Vì sao bidirectional attention hợp với text classification hơn text generation?
7. Một encoder layer gồm hai sublayers chính nào?
8. Feed-forward layer trong encoder khác self-attention ở điểm nào?
9. Multi-head attention khác single-head attention ở điểm nào?
10. Vì sao nhiều heads có thể giúp model học nhiều loại quan hệ song song?
11. Skip connection trong encoder sublayer giúp gì?
12. Layer normalization giúp gì khi train Transformer sâu?
13. Vì sao self-attention tạo ra contextualized embeddings?
14. Attention weights trong công thức weighted average có ý nghĩa gì?
15. Scaled dot-product attention tính attention weights qua những bước nào?
16. Vì sao attention scores cần được chia cho $\sqrt{d_k}$?

## Gợi ý trả lời câu hỏi review

1. Self-attention tạo representation mới bằng cách cho token hiện tại tính attention score với các token khác, chuẩn hóa thành attention weights, rồi lấy tổng có trọng số của value vectors.
2. Cần scale dot product để attention scores không quá lớn trước softmax, giúp training ổn định hơn.
3. Positional embeddings thêm thông tin thứ tự token, vì attention tự thân không biết token nào đứng trước hay sau.
4. Encoder-only hợp với understanding, decoder-only hợp với generation, encoder-decoder hợp với mapping từ sequence này sang sequence khác.
5. Bidirectional attention nhìn được cả context trái và phải; causal attention chỉ nhìn được quá khứ/token trước đó.
6. Text classification có toàn bộ input sẵn nên model nên đọc cả câu trước khi dự đoán. Text generation phải sinh từng token nên không được nhìn token tương lai.
7. Một encoder layer gồm multi-head self-attention layer và fully connected/position-wise feed-forward layer.
8. Self-attention trộn thông tin giữa các token; feed-forward layer xử lý từng token embedding độc lập sau khi đã có context.
9. Single-head attention tạo một attention distribution chính cho mỗi token; multi-head attention tạo nhiều distributions song song, mỗi head có Q/K/V riêng.
10. Vì mỗi head có projection riêng, mỗi head có thể học một kiểu match khác nhau: cú pháp, coreference, local context, keyword cho task, hoặc quan hệ ngữ nghĩa xa.
11. Skip connection giữ lại input ban đầu và tạo đường truyền thông tin/gradient dễ hơn qua nhiều layer.
12. Layer normalization giữ scale activation ổn định hơn, giúp training sâu bớt bất ổn.
13. Vì representation mới của mỗi token được tính từ toàn bộ sequence, nên cùng một token có thể có embedding khác nhau tùy ngữ cảnh.
14. Attention weights cho biết token nào đóng góp nhiều hay ít khi cập nhật representation cho token hiện tại.
15. Project token thành query/key/value, tính dot product giữa query và key để tạo ma trận scores $n \times n$, scale scores, softmax thành weights, rồi nhân weights với value vectors.
16. Vì dot product có thể lớn khi chiều vector tăng; scaling giúp softmax ổn định hơn và training dễ hơn.

## Checklist

- [ ] Vẽ lại kiến trúc Transformer
- [ ] Giải thích self-attention bằng lời của tôi
- [ ] Chạy demo attention
- [x] Tách concept quan trọng: [[Bidirectional Attention]]
- [x] Tách concept quan trọng: [[Multi-Head Attention]]
- [x] Tách concept quan trọng: [[Feed-Forward Layer]]
- [x] Tách concept quan trọng: [[Layer Normalization]]
- [x] Tách concept quan trọng: [[Positional Embeddings]]
- [x] Tách concept quan trọng: [[Classification Head]]
- [x] Tách concept quan trọng: [[Decoder]]
- [x] Cập nhật tiến độ sách
