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

# GRU

## Định nghĩa

GRU, Gated Recurrent Unit, là biến thể RNN dùng gates để kiểm soát lượng thông tin cũ được giữ lại và lượng thông tin mới được ghi vào hidden state.

## Cách hiểu bằng lời của tôi

GRU giống một RNN có van điều tiết. Thay vì luôn ghi đè memory ở mỗi bước, nó học khi nào nên giữ ký ức cũ và khi nào nên cập nhật.

## Cần biết

- GRU giúp giảm vấn đề [[Loss Function|vanishing gradients]] trong sequence modeling.
- GRU thường nhẹ hơn [[LSTM]] vì có ít gates hơn.
- GRU vẫn xử lý tuần tự theo thời gian, nên kém parallel hơn [[Transformer]].

## Liên kết

- [[Autoregressive Language Model]]
- [[LSTM]]
- [[Transformer]]
- [[CS224N]]
