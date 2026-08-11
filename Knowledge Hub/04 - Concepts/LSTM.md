---
type: concept
status: developing
sources:
  - "[[CS224N 2019 - Notes 05 - Language Models RNN GRU and LSTM]]"
  - "[[Practical Natural Language Processing]]"
source_sections:
  - "[[CS224N 2019 - Notes 05 - Language Models RNN GRU and LSTM]]"
  - "[[Practical NLP - Chapter 04 - Text Classification]]"
first_seen: 2026-08-03
last_updated: 2026-08-10
tags:
  - concept
  - nlp
  - cs224n
---

# LSTM

## Định nghĩa

LSTM, Long Short-Term Memory, là RNN có cell state và nhiều gates để lưu, quên và xuất thông tin qua chuỗi dài.

## Cách hiểu bằng lời của tôi

LSTM tách "bộ nhớ dài hạn" khỏi hidden state tức thời. Gates quyết định thông tin nào đi vào memory, thông tin nào bị quên và thông tin nào được lộ ra output.

## Cần biết

- LSTM được thiết kế để học dependency dài tốt hơn RNN thuần.
- Các gates thường gồm input, forget và output gate.
- Dù mạnh hơn RNN đơn giản, LSTM vẫn bị giới hạn bởi tính tuần tự.

## Khi dùng cho text classification

```text
Text
-> token index sequence
-> padding
-> embedding layer
-> LSTM
-> dense classification layer
```

- Practical NLP dùng LSTM như một deep-learning architecture cho [[Text Classification]], sau khi text đã được tokenize, pad và đưa qua embedding layer.
- LSTM/RNN hợp với text vì ngôn ngữ là dữ liệu tuần tự: meaning của một word phụ thuộc vào context trước/sau.
- Trong ví dụ IMDB sentiment, architecture là `Embedding(MAX_NUM_WORDS, 128)` -> `LSTM(128, dropout=0.2, recurrent_dropout=0.2)` -> `Dense(2, activation="sigmoid")`.
- LSTM chạy lâu hơn CNN trong notebook của sách và thường cần nhiều data hơn. Nếu kết quả thấp, có thể do dataset chưa đủ để tận dụng sức mạnh của model, không nhất thiết do LSTM sai hướng.
- Khi dùng LSTM cho classification, vẫn phải tune activation/layer size/loss/optimizer/epochs/batch size và so sánh với baseline.

## Liên kết

- [[GRU]]
- [[Autoregressive Language Model]]
- [[Transformer]]
- [[Text Classification]]
- [[Embedding]]
- [[CS224N]]
