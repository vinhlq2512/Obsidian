---
type: concept
status: seed
source:
  - "[[NLP Transformers - Chapter 01 - Hello Transformers]]"
  - "[[Transformer]]"
tags:
  - concept
  - transformer
  - attention
  - nlp
---

# Self-Attention

## Định nghĩa

Self-attention là cơ chế cho phép mỗi token trong cùng một sequence tính mức độ liên quan với các token còn lại, rồi dùng các mức liên quan đó để tạo biểu diễn mới giàu ngữ cảnh hơn cho chính token đó.

## Cách hiểu bằng lời của tôi

Thay vì đọc câu từ trái sang phải và hy vọng hidden state giữ đủ thông tin, self-attention cho từng token quyền "nhìn" trực tiếp các token khác trong câu. Token nào quan trọng hơn với ngữ cảnh hiện tại thì nhận trọng số attention cao hơn.

Ví dụ trong câu có nhiều đại từ hoặc quan hệ xa, self-attention giúp model nối token hiện tại với từ mà nó đang tham chiếu, kể cả khi hai từ không đứng gần nhau.

## Công thức trực giác

Thay vì dùng embedding cố định cho mỗi token, self-attention tạo embedding mới bằng cách lấy weighted average của toàn bộ sequence.

Nếu input là $x_1, ..., x_n$, output là $x'_1, ..., x'_n$, trong đó:

$$
x'_i = \sum_{j=1}^{n} w_{ji}x_j
$$

Các $w_{ji}$ là attention weights và được chuẩn hóa để:

$$
\sum_j w_{ji} = 1
$$

Cách đọc công thức: representation mới của token $i$ được tạo bằng cách trộn tất cả token embeddings $x_j$, nhưng token nào quan trọng hơn thì có trọng số lớn hơn.

Ví dụ `flies` trong `"time flies like an arrow"` nên nhận nhiều thông tin từ `time` và `arrow`, nên embedding mới của `flies` nghiêng về nghĩa động từ thay vì nghĩa côn trùng.

## Cách tính attention weights

Self-attention thường dùng scaled dot-product attention:

$$
\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V
$$

Các bước chính:

1. Từ mỗi token embedding, tạo ba projection: query, key và value.
2. Tính dot product giữa query và key để ra attention scores.
3. Chia scores cho $\sqrt{d_k}$ để scale.
4. Dùng softmax để biến scores thành attention weights.
5. Lấy tổng có trọng số của value vectors để tạo representation mới.

Query có thể hiểu là "tôi đang tìm gì", key là "tôi có tín hiệu gì để được chú ý", value là "nội dung tôi đóng góp nếu được chú ý".

Với sequence có $n$ tokens, attention scores là ma trận $n \times n$. Sau scaling và softmax, attention weights cũng là ma trận $n \times n$, nhưng các giá trị đã được chuẩn hóa thành phân phối trọng số.

Ở mức từng token, bước update dùng value vectors:

$$
x'_i = \sum_j w_{ji}v_j
$$

Nghĩa là representation mới của token $i$ là tổng có trọng số của các value vectors mà token đó chú ý tới.

### Ví dụ trực quan

Giả sử câu rút gọn có 3 token:

```text
time | flies | arrow
```

Ta đang cập nhật representation cho `flies`.

- Query của `flies` hỏi: "Context nào giúp hiểu token này?"
- Key của `time`, `flies`, `arrow` cạnh tranh để match với query đó.
- Nếu `time` và `arrow` liên quan mạnh hơn, attention weights sau softmax có thể là:

| Token đóng góp value | Attention weight |
| --- | ---: |
| `time` | 0.45 |
| `flies` | 0.10 |
| `arrow` | 0.45 |

Khi đó:

$$
x'_{\text{flies}} = 0.45v_{\text{time}} + 0.10v_{\text{flies}} + 0.45v_{\text{arrow}}
$$

Các con số chỉ để minh họa. Ý nghĩa là embedding mới của `flies` được contextualize bằng cách lấy nhiều thông tin từ `time` và `arrow`, nên token này dễ được hiểu là động từ trong `"time flies like an arrow"` thay vì danh từ "con ruồi".

## Cần biết

- Self-attention hoạt động trong cùng một sequence; khác với cross-attention, nơi decoder chú ý sang output của encoder.
- Self-attention tạo [[Embedding|contextualized embeddings]]: cùng một token có thể có representation khác nhau tùy ngữ cảnh.
- Mỗi token được biến thành ba vector chính: query, key và value.
- Attention score đo mức phù hợp giữa query của token hiện tại và key của các token khác.
- Softmax biến attention score thành trọng số, sau đó model lấy tổng có trọng số của các value vector.
- Scaling bằng $\sqrt{d_k}$ giúp attention scores không quá lớn trước softmax.
- [[Multi-Head Attention]] chạy nhiều attention head song song để học nhiều kiểu quan hệ khác nhau.
- Self-attention giúp Transformer học quan hệ dài tốt hơn RNN, nhưng chi phí tính toán tăng mạnh theo độ dài sequence.
- Trong encoder-only models, self-attention thường là [[Bidirectional Attention]], nghĩa là token được nhìn cả context trái và phải.

## Liên kết

- [[Transformer]]
- [[Multi-Head Attention]]
- [[Bidirectional Attention]]
- [[NLP Transformers - Chapter 01 - Hello Transformers]]
- [[NLP Transformers - Chapter 03 - Transformer Anatomy]]
