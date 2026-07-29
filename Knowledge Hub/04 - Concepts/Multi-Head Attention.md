---
type: concept
status: seed
source:
  - "[[NLP Transformers - Chapter 03 - Transformer Anatomy]]"
  - "[[Self-Attention]]"
tags:
  - concept
  - transformer
  - attention
  - nlp
---

# Multi-Head Attention

## Định nghĩa

Multi-head attention là phiên bản mở rộng của [[Self-Attention]], trong đó model chạy nhiều attention heads song song. Mỗi head có bộ projection query/key/value riêng, nên có thể học một kiểu quan hệ khác nhau giữa các token.

## Cách hiểu bằng lời của tôi

Một self-attention head giống như một "góc nhìn" về câu. Nếu chỉ có một head, model phải nén mọi loại quan hệ vào cùng một attention pattern. Với nhiều heads, model có thể chia việc:

- Một head chú ý quan hệ cú pháp, ví dụ chủ ngữ với động từ.
- Một head chú ý các token gần nhau.
- Một head chú ý đại từ với danh từ mà nó tham chiếu.
- Một head chú ý từ khóa quan trọng cho classification.

Vì vậy multi-head attention không chỉ hỏi "token nào quan trọng?", mà hỏi câu đó theo nhiều cách khác nhau cùng lúc.

## Công thức trực giác

Với mỗi head $h$, model tạo bộ projection riêng:

$$
Q_h = XW_h^Q,\quad K_h = XW_h^K,\quad V_h = XW_h^V
$$

Sau đó mỗi head chạy scaled dot-product attention:

$$
\text{head}_h = \text{Attention}(Q_h, K_h, V_h)
$$

Các head được nối lại rồi đưa qua một linear projection cuối:

$$
\text{MultiHead}(X) = \text{Concat}(\text{head}_1, ..., \text{head}_m)W^O
$$

Cách đọc công thức: mỗi head tạo một contextualized representation riêng cho cùng sequence. Sau đó model concat các góc nhìn này lại, rồi trộn chúng bằng ma trận $W^O$ để tạo output cuối cùng.

## Shape cần nhớ

Giả sử hidden size là $d_{\text{model}} = 768$ và có $m = 12$ heads.

- Mỗi token embedding ban đầu có 768 chiều.
- Mỗi head thường xử lý một phần nhỏ hơn: $d_k = 768 / 12 = 64$ chiều.
- Mỗi head tạo attention pattern riêng trên toàn sequence.
- Sau khi 12 heads chạy xong, outputs được concat lại thành 768 chiều rồi project tiếp.

Điểm quan trọng: multi-head attention không nhất thiết làm output rộng hơn. Nó chia hidden dimension thành nhiều head nhỏ, chạy attention song song, rồi ghép lại về cùng kích thước ban đầu.

## Ví dụ trực quan

Với câu:

```text
The cat sat on the mat because it was tired
```

Khi cập nhật representation cho `it`, các head có thể học các pattern khác nhau:

| Head | Có thể chú ý mạnh tới | Lý do |
| --- | --- | --- |
| Head 1 | `cat` | Tìm antecedent của đại từ `it` |
| Head 2 | `tired` | Nắm trạng thái/mô tả liên quan |
| Head 3 | `because` | Nhận ra quan hệ nguyên nhân |
| Head 4 | token gần `it` | Giữ local context |

Các pattern này chỉ là minh họa. Trong model thật, ta không luôn diễn giải được từng head rõ ràng như vậy, nhưng mental model này giúp hiểu vì sao nhiều heads hữu ích.

## Vì sao không dùng một head lớn?

Một head lớn có nhiều chiều hơn, nhưng vẫn chỉ tạo một attention distribution cho mỗi token. Nhiều heads cho phép model tạo nhiều attention distributions khác nhau cùng lúc.

So sánh:

- **Single-head attention**: một token có một cách phân bổ chú ý chính.
- **Multi-head attention**: một token có nhiều cách phân bổ chú ý song song, mỗi cách có thể tập trung vào một loại quan hệ khác nhau.

Điểm cần nhớ: lợi ích chính của multi-head attention là đa dạng hóa các kiểu quan hệ được học, không chỉ là tăng số tham số.

## Khi áp dụng

- Encoder dùng multi-head self-attention để mỗi token nhìn toàn bộ input theo nhiều góc nhìn.
- Decoder dùng masked multi-head self-attention để mỗi token nhìn quá khứ theo nhiều góc nhìn.
- Encoder-decoder models dùng [[Cross-Attention|cross-attention]], nơi query đến từ decoder còn key/value đến từ encoder output.

## Cần biết

- Mỗi head có bộ $W^Q$, $W^K$, $W^V$ riêng.
- Các heads chạy song song, không chạy tuần tự.
- Attention weights của mỗi head có thể khác nhau.
- Output của các heads được concat rồi project bằng $W^O$.
- Số heads là hyperparameter quan trọng; quá ít heads có thể thiếu góc nhìn, quá nhiều heads có thể làm mỗi head quá nhỏ hoặc gây dư thừa.
- Multi-head attention vẫn có chi phí attention theo độ dài sequence, thường là $O(n^2)$ theo số token.

## Liên kết

- [[Self-Attention]]
- [[Cross-Attention]]
- [[Bidirectional Attention]]
- [[Transformer]]
- [[NLP Transformers - Chapter 03 - Transformer Anatomy]]
