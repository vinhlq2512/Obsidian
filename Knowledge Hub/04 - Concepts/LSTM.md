---
type: concept
status: developing
sources:
  - "[[CS224N 2019 - Notes 05 - Language Models RNN GRU and LSTM]]"
source_sections:
  - "[[CS224N 2019 - Notes 05 - Language Models RNN GRU and LSTM]]"
first_seen: 2026-08-03
last_updated: 2026-08-03
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

## Liên kết

- [[GRU]]
- [[Autoregressive Language Model]]
- [[Transformer]]
- [[CS224N]]
