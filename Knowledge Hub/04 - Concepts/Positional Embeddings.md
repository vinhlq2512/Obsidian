---
type: concept
status: seed
source:
  - "[[NLP Transformers - Chapter 03 - Transformer Anatomy]]"
tags:
  - concept
  - transformer
  - embedding
  - nlp
---

# Positional Embeddings

## Định nghĩa

Positional embeddings là các vector biểu diễn vị trí của token trong sequence. Transformer cộng hoặc kết hợp positional embeddings với token embeddings để model biết thứ tự token.

## Cách hiểu bằng lời của tôi

Self-attention nhìn toàn bộ sequence cùng lúc, nên bản thân nó không tự biết token nào đứng trước, token nào đứng sau. Nếu chỉ đưa token embeddings vào attention, câu có cùng các token nhưng đảo thứ tự có thể trở nên quá giống nhau với model.

Positional embeddings giống như nhãn vị trí được gắn thêm vào mỗi token. Token embedding nói "đây là từ gì"; positional embedding nói "từ này nằm ở đâu trong câu".

Mental model:

```text
input token
-> token embedding: nội dung của token
-> positional embedding: vị trí của token
-> cộng hai vector
-> Transformer layer
```

## Vì sao Transformer cần positional embeddings?

Attention tính quan hệ giữa các token bằng query, key và value. Cơ chế này rất mạnh để trộn thông tin giữa token, nhưng nếu không thêm tín hiệu vị trí thì attention không có bias tự nhiên về thứ tự.

Ví dụ:

```text
dog bites man
man bites dog
```

Hai câu dùng cùng token nhưng ý nghĩa khác nhau vì thứ tự khác nhau. Positional embeddings giúp model phân biệt hai trường hợp này.

## Công thức trực giác

Với token thứ $i$, input ban đầu cho Transformer thường là:

$$
h_i = e_i + p_i
$$

Trong đó:

- $e_i$ là token embedding của token ở vị trí $i$.
- $p_i$ là positional embedding của vị trí $i$.
- $h_i$ là vector đầu vào đã chứa cả nội dung token và thông tin vị trí.

Điểm cần nhớ: positional embedding không thay thế token embedding; nó bổ sung thông tin thứ tự vào representation ban đầu.

## Các kiểu positional embeddings

- **Absolute positional embeddings**: mỗi vị trí có một vector riêng, ví dụ vị trí 1, 2, 3, ... Loại này dễ hiểu và thường được học như tham số của model.
- **Sinusoidal positional encodings**: dùng các hàm sin/cos cố định để tạo vector vị trí. Transformer gốc dùng cách này để model có thể suy rộng phần nào sang độ dài sequence khác.
- **Relative positional embeddings**: biểu diễn khoảng cách tương đối giữa token thay vì chỉ vị trí tuyệt đối. Cách này hữu ích vì nhiều quan hệ ngôn ngữ phụ thuộc vào khoảng cách giữa token.
- **Rotary positional embeddings, RoPE**: mã hóa vị trí bằng phép xoay trong không gian vector, rất phổ biến trong nhiều LLM hiện đại.

## Vì sao positional embeddings có thể learnable?

Positional embeddings không bắt buộc phải learnable. Transformer gốc dùng sinusoidal positional encodings cố định. Nhưng nhiều model, đặc biệt là BERT-style models, dùng **learnable positional embeddings**: mỗi vị trí trong context window có một vector riêng và vector đó được cập nhật bằng backpropagation trong quá trình training.

Cách hiểu:

```text
position 0 -> vector p_0
position 1 -> vector p_1
position 2 -> vector p_2
...
```

Ban đầu các vector này thường được khởi tạo ngẫu nhiên. Khi model học task ngôn ngữ, gradient sẽ điều chỉnh chúng để vị trí 0, 1, 2, ... mang tín hiệu hữu ích nhất cho dữ liệu và objective.

Lý do làm vậy:

- Model không bị ép dùng một công thức vị trí cố định; nó tự học cách biểu diễn vị trí có ích cho task.
- Một số vị trí có thể mang bias đặc biệt, ví dụ đầu câu, cuối câu, vị trí gần token phân tách, hoặc vùng thường chứa prompt/instruction.
- Learnable positional embeddings đơn giản để triển khai: chỉ là một embedding table giống token embeddings.

Trade-off:

- Ưu điểm: linh hoạt và thường hoạt động tốt trong phạm vi context length đã train.
- Nhược điểm: khó suy rộng tự nhiên sang vị trí dài hơn max length đã học, vì các vị trí mới không có vector đã train.
- Vì vậy các model cần context dài thường dùng hoặc cải tiến các cách mã hóa vị trí như sinusoidal, relative position, RoPE hoặc biến thể mở rộng context.

## Cần biết

- Positional embeddings giải quyết điểm yếu của self-attention: attention tự thân không biết thứ tự token.
- Chúng thường được cộng vào token embeddings trước khi đi vào Transformer blocks.
- Thông tin vị trí ảnh hưởng tới cả encoder-only, decoder-only và encoder-decoder models.
- Context length của model thường liên quan tới cách positional embeddings được thiết kế hoặc học.
- Khi mở rộng context length, positional encoding/embedding là một chi tiết kiến trúc cần kiểm tra kỹ.
- Learnable positional embeddings là tham số học được, nhưng không phải lựa chọn duy nhất.

## Khi áp dụng

- Khi đọc kiến trúc Transformer, hãy tìm xem model dùng absolute position, relative position, sinusoidal encoding, RoPE hay biến thể khác.
- Khi model xử lý sequence dài kém, positional strategy có thể là một trong các nguyên nhân.
- Khi so sánh các LLM hiện đại, RoPE và các biến thể mở rộng context là điểm đáng chú ý.

## Câu hỏi review

1. Vì sao self-attention cần thêm positional embeddings?
2. Token embedding và positional embedding khác nhau thế nào?
3. Vì sao hai câu có cùng token nhưng đảo thứ tự vẫn cần representation khác nhau?
4. Absolute positional embeddings và relative positional embeddings khác nhau ở đâu?
5. Context length liên quan gì tới positional embeddings?
6. Vì sao một số model dùng learnable positional embeddings?
7. Learnable positional embeddings có hạn chế gì khi gặp sequence dài hơn lúc train?

## Gợi ý trả lời câu hỏi review

1. Vì self-attention tự thân không biết token nào đứng trước hoặc đứng sau; nó cần tín hiệu vị trí để hiểu thứ tự.
2. Token embedding biểu diễn nội dung token, còn positional embedding biểu diễn vị trí của token trong sequence.
3. Thứ tự token có thể đổi vai trò ngữ pháp và ý nghĩa của câu, ví dụ chủ thể và đối tượng bị đảo.
4. Absolute embedding gắn vector cho từng vị trí cụ thể; relative embedding biểu diễn quan hệ/khoảng cách giữa các token.
5. Cách mã hóa vị trí ảnh hưởng tới khả năng model xử lý sequence dài hơn hoặc khác độ dài đã train.
6. Vì model có thể tự học vector vị trí phù hợp nhất với dữ liệu và objective thay vì dùng công thức cố định.
7. Những vị trí vượt ngoài max length đã học không có vector đã train, nên khả năng extrapolate thường kém hơn các cách mã hóa vị trí được thiết kế cho context dài.

## Liên kết

- [[Transformer]]
- [[Embedding]]
- [[Self-Attention]]
- [[Multi-Head Attention]]
- [[NLP Transformers - Chapter 03 - Transformer Anatomy]]
